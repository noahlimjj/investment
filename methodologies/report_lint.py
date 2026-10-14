"""Verification pass. Run on every report before it counts as done.

Each check maps to a defect found in the v1 reports (METHODOLOGY_AUDIT.md) or in the Oct 2026
pipeline runs. Exit code 1 if any ERROR-level check fails.

    python3 methodologies/report_lint.py reports/runs/<TICKER>_<DATE>/<TICKER>_report.md

For run reports (reports/runs/*) this also checks provenance: each stage file must match what
its value-* subagent wrote (see provenance.py). A look-alike file with a typed header fails.
When a Claude Code session runs this and the report passes, a hook seals the report; the
Telegram bot and the portfolio audit only use sealed reports.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import provenance  # noqa: E402

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
VERDICTS = {"BUY", "ACCUMULATE", "HOLD", "TRIM", "SELL", "PASS"}
REQUIRED = ["VERDICT", "AS_OF", "PRICE", "FAIR_VALUE", "UPSIDE",
            "ENTRY_BELOW", "EXIT_ABOVE", "CONVICTION", "KEY_RISK", "DATA_WARNINGS"]
STAGE_HEADERS = {"01_research.md": "value-researcher", "02_quant.md": "value-quant",
                 "03_skeptic.md": "value-skeptic"}
MOS_LEVELS = (0.20, 0.30, 0.40)          # analyse skill: Wide / Narrow / none-cyclical-rNPV
SYMBOL_CCY = {"$": "USD", "€": "EUR", "£": "GBP", "¥": "JPY", "₩": "KRW"}
BANNED = [
    (r"target\s+mean|price target|analyst.*target|targetMeanPrice",
     "cites a sell-side price target (banned as a valuation input - RULE 2)"),
    (r"recommendationKey|\"?strong_buy\"?",
     "cites an analyst rating (banned as an input - RULE 2)"),
    (r"insider (buying|selling|activity).{0,40}0\.0*[0-9]+%",
     "reports heldPercentInsiders as insider TRADING activity (FIX-7)"),
    (r"[Zz]ero debt|[Nn]o debt\b",
     "asserts zero debt - confirm this is a real 0 and not a null (FIX-4)"),
    (r"[Ii]nstitutional [Oo]wnership:?\s*>?\s*1[0-9][0-9]%",
     "reports institutional ownership >100% as fact (vendor artifact - FIX-6)"),
]


# --------------------------------------------------------------------------- #
# verdict block parsing (also used by pipeline_store.py)
# --------------------------------------------------------------------------- #
def parse_verdict_block(text: str) -> dict[str, str]:
    """Raw string of each verdict-block field (last occurrence wins)."""
    fields = {}
    for f in REQUIRED:
        found = re.findall(rf"^{f}:[ \t]*(.+?)[ \t]*$", text, re.M)
        if found:
            fields[f] = found[-1].strip("* ")
    return fields


def parse_money(raw: str | None) -> tuple[float, str | None] | None:
    """'381.65 EUR' -> (381.65, 'EUR'); '$45.40' -> (45.40, 'USD'); '6.30%/yr' -> None."""
    if not raw or "%" in raw.split("(")[0]:
        return None
    m = re.match(r"^\s*([$€£¥₩])?\s*(-?[\d,]*\.?\d+)\s*([A-Z]{3}|GBp)?\b", raw)
    if not m:
        return None
    value = float(m.group(2).replace(",", ""))
    ccy = m.group(3) or SYMBOL_CCY.get(m.group(1) or "")
    if ccy == "GBp":
        value, ccy = value / 100.0, "GBP"
    return value, ccy


def parse_pct(raw: str | None) -> float | None:
    m = re.match(r"^\s*([+-]?\d+(?:\.\d+)?)\s*%", raw or "")
    return float(m.group(1)) if m else None


def held_tickers() -> set[str]:
    p = PROJECT_ROOT / "data" / "portfolio.json"
    try:
        return set(json.loads(p.read_text()).get("tickers", []))
    except (OSError, json.JSONDecodeError):
        return set()


def load_warnings() -> dict:
    p = PROJECT_ROOT / "data" / "fundamentals.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text())
    return {k: v.get("warnings", []) for k, v in d.get("records", {}).items()}


def check_verdict_block(fields: dict[str, str], ticker: str, *, is_fund: bool,
                        held: set[str] | None = None) -> list[tuple[str, str]]:
    """Arithmetic and rule consistency of the verdict block (analyse skill, Verdict rules)."""
    issues: list[tuple[str, str]] = []
    if is_fund:
        return issues
    price, fv = parse_money(fields.get("PRICE")), parse_money(fields.get("FAIR_VALUE"))
    entry, exit_ = parse_money(fields.get("ENTRY_BELOW")), parse_money(fields.get("EXIT_ABOVE"))
    if not price or not fv:
        issues.append(("ERROR", "PRICE or FAIR_VALUE is not a number with a currency"))
        return issues
    ccys = {c for _, c in (price, fv, entry or (0, None), exit_ or (0, None)) if c}
    if len(ccys) > 1:
        issues.append(("ERROR", f"verdict block mixes currencies {sorted(ccys)}: PRICE, FAIR_VALUE, "
                                "ENTRY_BELOW and EXIT_ABOVE must share the quote currency"))
        return issues
    p, v = price[0], fv[0]
    upside = parse_pct(fields.get("UPSIDE"))
    implied = (v / p - 1) * 100
    if upside is None:
        issues.append(("ERROR", "UPSIDE is not a percentage"))
    elif abs(upside - implied) > 1.5:
        issues.append(("ERROR", f"UPSIDE {upside:+.1f}% doesn't match FAIR_VALUE/PRICE ({implied:+.1f}%)"))
    if entry and exit_:
        e, x = entry[0], exit_[0]
        if not e < v < x:
            issues.append(("ERROR", f"expected ENTRY_BELOW < FAIR_VALUE < EXIT_ABOVE, got {e:g} / {v:g} / {x:g}"))
        else:
            if abs(x / v - 1.3) > 0.015:
                issues.append(("WARN", f"EXIT_ABOVE is {x / v:.2f}x EV; the skill sets it at 1.30x"))
            mos = 1 - e / v
            if min(abs(mos - m) for m in MOS_LEVELS) > 0.015:
                issues.append(("WARN", f"ENTRY_BELOW implies a {mos:.0%} margin of safety; the skill "
                                       "uses 20% (wide moat), 30% (narrow) or 40% (none/cyclical/rNPV)"))
        verdict = fields.get("VERDICT", "").upper()
        if p > x and verdict in ("BUY", "ACCUMULATE", "HOLD"):
            issues.append(("ERROR", f"price {p:g} is above EXIT_ABOVE {x:g}: the rules give TRIM (held) "
                                    f"or PASS (not held), not {verdict}"))
        elif v < p <= x and verdict in ("BUY", "ACCUMULATE"):
            issues.append(("ERROR", f"price {p:g} is above EV {v:g}: {verdict} isn't allowed there"))
        elif e < p <= v and verdict == "BUY":
            issues.append(("ERROR", f"BUY needs price at or below ENTRY_BELOW {e:g} (EV x (1 - MoS)); "
                                    f"at {p:g} the rules give ACCUMULATE or HOLD"))
        elif p <= e and verdict == "TRIM":
            issues.append(("WARN", f"price {p:g} is at or below ENTRY_BELOW {e:g} yet the verdict is TRIM"))
        if held is not None and ticker not in held and verdict in ("HOLD", "TRIM", "SELL"):
            issues.append(("WARN", f"{verdict} is a held-position verdict but {ticker} isn't in "
                                   "data/portfolio.json (BUY / ACCUMULATE / PASS apply)"))
    return issues


def lint(path: pathlib.Path, data_warnings: dict) -> list[tuple[str, str]]:
    text = path.read_text()
    issues: list[tuple[str, str]] = []

    # --- banned inputs -----------------------------------------------------
    for pat, msg in BANNED:
        if re.search(pat, text, re.I):
            issues.append(("ERROR", msg))

    # --- verdict block -----------------------------------------------------
    missing = [f for f in REQUIRED if not re.search(rf"^{f}:", text, re.M)]
    if missing:
        issues.append(("ERROR", f"verdict block missing fields: {', '.join(missing)}"))

    m = re.search(r"^VERDICT:\s*(\S+)", text, re.M)
    if m and m.group(1).upper().strip("*") not in VERDICTS:
        issues.append(("ERROR", f"verdict '{m.group(1)}' not in closed vocabulary {sorted(VERDICTS)}"))

    # --- staleness ---------------------------------------------------------
    m = re.search(r"^AS_OF:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    if m:
        age = datetime.now(timezone.utc) - datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
        if age > timedelta(days=30):
            issues.append(("ERROR", f"report is {age.days} days stale (>30) - re-run before acting"))
        elif age > timedelta(days=14):
            issues.append(("WARN", f"report is {age.days} days old"))
    else:
        issues.append(("ERROR", "no AS_OF date - stale reports become indistinguishable from fresh (FIX-12)"))

    # --- valuation actually performed --------------------------------------
    if not re.search(r"discount rate|WACC|terminal (growth|value)", text, re.I):
        issues.append(("ERROR", "no DCF evidence (no WACC / discount rate / terminal value) - Part 5 (FIX-3)"))
    if not re.search(r"reverse[ _-]?dcf|implies? a ~?\d|already discount", text, re.I):
        issues.append(("WARN", "no reverse-DCF: 'what must be true?' is the most useful line in Part 5"))

    # --- PEG gate ----------------------------------------------------------
    stem = path.stem
    ticker = (stem[:-len("_report")] if stem.endswith("_report") else stem.split("_")[0]).upper()
    warns = data_warnings.get(ticker, [])
    peg_void = any("PEG" in w for w in warns)
    if peg_void and re.search(r"\bPEG\b", text):
        issues.append(("ERROR", f"cites PEG but the data layer VOIDED it for {ticker} (FIX-6)"))

    # --- data warnings surfaced -------------------------------------------
    if warns:
        m = re.search(r"^DATA_WARNINGS:\s*(\d+)", text, re.M)
        if not m:
            issues.append(("ERROR", f"{len(warns)} data warnings exist for {ticker}, none declared"))
        elif int(m.group(1)) != len(warns):
            issues.append(("WARN", f"DATA_WARNINGS={m.group(1)} but data layer has {len(warns)}"))

    # --- verdict block arithmetic and rules ---------------------------------
    fields = parse_verdict_block(text)
    is_fund = bool(re.search(r"Template\s+FUND", text)) or "%" in fields.get("FAIR_VALUE", "").split("(")[0]
    if not missing:
        issues += check_verdict_block(fields, ticker, is_fund=is_fund, held=held_tickers())

    # --- three-agent pipeline sections (reports/runs/*) --------------------
    if "runs" in path.parts:
        for pat, what in ((r"Expected Value", "probability-weighted Expected Value"),
                          (r"(Capital Allocation|Structure) Grade:?\**\s*\**[A-F]", "Capital Allocation (or FUND Structure) Grade A-F"),
                          (r"Number audit", "Skeptic number audit"),
                          (r"Two-Minute Drill", "Lynch two-minute drill")):
            if not re.search(pat, text, re.I):
                issues.append(("ERROR", f"pipeline report missing {what} (analyse skill)"))
        run = path.parent
        for f in ("01_research.md", "02_quant.md", "02_model.py", "03_skeptic.md"):
            if not (run / f).exists():
                issues.append(("ERROR", f"run folder missing {f} - all three agents must run"))
        for f, stage in STAGE_HEADERS.items():
            p = run / f
            if p.exists() and not p.read_text().startswith(f"<!-- pipeline:{stage} -->"):
                issues.append(("ERROR", f"{f} lacks the <!-- pipeline:{stage} --> header: not pipeline output"))
        for prob in provenance.stage_problems(run):
            if "missing" not in prob:
                issues.append(("ERROR", f"provenance: {prob} - re-run that stage through /analyse"))
        inputs = run / "00_inputs.json"
        price = parse_money(fields.get("PRICE"))
        if inputs.exists() and price:
            try:
                ref = json.loads(inputs.read_text())
                close, qccy = ref.get("price"), ref.get("quote_currency")
                if qccy == "GBp" and close:
                    close, qccy = close / 100.0, "GBP"
                if close and price[1] in (None, qccy) and abs(price[0] / close - 1) > 0.02:
                    issues.append(("WARN", f"PRICE {price[0]:g} differs from the 00_inputs.json official "
                                           f"close {close:g} by {price[0] / close - 1:+.1%}"))
            except (json.JSONDecodeError, TypeError, ZeroDivisionError):
                pass

    # --- sourcing ----------------------------------------------------------
    if not re.search(r"\]\(https?://|[Ss]ources?:|^#+\s*(\d+\.\s*)?Sources|https?://|accn\s*\d{10}-\d{2}-\d{6}", text, re.M):
        issues.append(("WARN", "no sources cited (1 of 37 v1 reports cited any source)"))
    return issues


def main(argv: list[str]) -> int:
    paths = [pathlib.Path(a) for a in argv[1:]]
    if not paths:
        print(__doc__); return 2
    dw = load_warnings()
    total_err = 0
    for p in paths:
        if not p.exists():
            print(f"{p}: NOT FOUND"); total_err += 1; continue
        issues = lint(p, dw)
        errs = sum(1 for lvl, _ in issues if lvl == "ERROR")
        total_err += errs
        status = "FAIL" if errs else ("warn" if issues else "PASS")
        print(f"\n{p}  [{status}]")
        for lvl, msg in issues:
            print(f"   {lvl:<5} {msg}")
    print(f"\n{len(paths)} file(s), {total_err} error(s)")
    return 1 if total_err else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
