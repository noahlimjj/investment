"""Verified pipeline results: the only source of verdicts for the portfolio audit and Telegram.

A run counts as VERIFIED when (1) report_lint passes it now, which includes provenance (every
stage file matches what its value-* subagent wrote), and (2) its report carries a lint seal made
inside a Claude Code session. Anything else is UNVERIFIED or MISSING, the reasons are listed, and
its verdict is never displayed. Figures come from the report's own verdict block, in the report's
own currency. The ledger is a prediction log, not a display source: it stores USD conversions
and has held rows from runs that later failed verification.

    python3 methodologies/pipeline_store.py NVO MC.PA        # status of each ticker's latest run
    python3 methodologies/pipeline_store.py --ledger         # audit ledger rows against runs
"""
from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import provenance  # noqa: E402
import report_lint  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "reports" / "runs"
LEDGER = PROJECT_ROOT / "reports" / "prediction_ledger.csv"
REUSE_DAYS = 14         # analyse skill: a run from the last 14 days may be reused
REFRESH_MOVE = 0.15     # a price move this large since the run calls for a re-run
_RUN_RE = re.compile(r"^(?P<ticker>.+)_(?P<date>\d{4}-\d{2}-\d{2})$")


@dataclass
class PipelineResult:
    ticker: str
    status: str = "MISSING"                 # VERIFIED | UNVERIFIED | MISSING
    problems: list[str] = field(default_factory=list)
    run_dir: Path | None = None
    report_path: Path | None = None
    name: str | None = None
    as_of: date | None = None
    template: str | None = None
    verdict: str | None = None
    conviction: str | None = None
    price: float | None = None
    currency: str | None = None
    fair_value: float | None = None
    fair_value_text: str | None = None
    upside_pct: float | None = None
    entry_below: float | None = None
    exit_above: float | None = None
    key_risk: str | None = None
    data_warnings: str | None = None
    two_minute_drill: str | None = None
    bear_thesis: str | None = None
    skipped_runs: list[str] = field(default_factory=list)   # newer runs that failed verification

    @property
    def verified(self) -> bool:
        return self.status == "VERIFIED"

    @property
    def age_days(self) -> int | None:
        return (datetime.now(timezone.utc).date() - self.as_of).days if self.as_of else None

    @property
    def is_fund(self) -> bool:
        return (self.template or "").upper().startswith("FUND")


def run_dirs(ticker: str) -> list[Path]:
    """Run folders for exactly this ticker, newest first."""
    out = []
    for p in RUNS_DIR.glob(f"{ticker}_*"):
        m = _RUN_RE.match(p.name)
        if p.is_dir() and m and m.group("ticker") == ticker:
            out.append(p)
    return sorted(out, key=lambda p: p.name[-10:], reverse=True)


def known_tickers() -> set[str]:
    return {m.group("ticker") for p in RUNS_DIR.glob("*_*") if (m := _RUN_RE.match(p.name))}


def _section(text: str, heading_re: str) -> str | None:
    m = re.search(rf"^##\s*{heading_re}[^\n]*\n+(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else None


def assess(run_dir: Path, warnings: dict | None = None) -> tuple[list[str], dict]:
    """(problems, parsed verdict fields) for one run. No problems means VERIFIED."""
    ticker = _RUN_RE.match(run_dir.name).group("ticker")
    report = run_dir / f"{ticker}_report.md"
    if not report.exists():
        return [f"{report.name} missing: the run never finished"], {}
    text = report.read_text()
    issues = report_lint.lint(report, warnings if warnings is not None else report_lint.load_warnings())
    problems = [msg for lvl, msg in issues if lvl == "ERROR"]
    seal = provenance.verify_run(run_dir)["report"]
    if seal == "modified":
        problems.append("report changed after it passed lint in Claude Code (seal broken)")
    elif seal != "sealed":
        problems.append("report was never passed by report_lint inside a Claude Code session (no seal)")
    fields = report_lint.parse_verdict_block(text)
    head = re.search(r"^# Equity Analysis:\s*\S+\s*[—-]\s*(.+)$", text, re.M)
    tmpl = re.search(r"Template\s+([A-Za-z-]+)", text)
    fields["_name"] = head.group(1).strip() if head else None
    fields["_template"] = tmpl.group(1) if tmpl else None
    fields["_drill"] = _section(text, r"0\.\s*Two-Minute Drill")
    bear = re.search(r"^\s*-\s*\*\*Bear thesis:?\*\*:?\s*(.+)$", text, re.M)
    fields["_bear"] = bear.group(1).strip() if bear else None
    return problems, fields


def latest(ticker: str, warnings: dict | None = None) -> PipelineResult:
    """The newest VERIFIED run for a ticker. Newer runs that fail verification are skipped and
    named, never used. If no run verifies, the result is UNVERIFIED with the newest run's problems."""
    res = PipelineResult(ticker=ticker)
    dirs = run_dirs(ticker)
    if not dirs:
        res.problems = ["no pipeline run on file"]
        return res
    warnings = warnings if warnings is not None else report_lint.load_warnings()
    first_problems: list[str] | None = None
    for d in dirs:
        problems, fields = assess(d, warnings)
        if problems:
            res.skipped_runs.append(d.name)
            if first_problems is None:
                first_problems, res.run_dir = problems, d
            continue
        _fill(res, d, fields)
        res.status = "VERIFIED"
        res.skipped_runs = [s for s in res.skipped_runs if s > d.name]
        return res
    res.status, res.problems = "UNVERIFIED", first_problems or []
    return res


def _fill(res: PipelineResult, run_dir: Path, f: dict) -> None:
    price = report_lint.parse_money(f.get("PRICE"))
    fv = report_lint.parse_money(f.get("FAIR_VALUE"))
    entry = report_lint.parse_money(f.get("ENTRY_BELOW"))
    exit_ = report_lint.parse_money(f.get("EXIT_ABOVE"))
    res.run_dir = run_dir
    res.report_path = run_dir / f"{res.ticker}_report.md"
    res.name = f.get("_name")
    res.template = f.get("_template")
    res.verdict = (f.get("VERDICT") or "").upper() or None
    res.conviction = f.get("CONVICTION")
    try:
        res.as_of = date.fromisoformat(f.get("AS_OF", "")[:10])
    except ValueError:
        res.as_of = None
    res.price, res.currency = (price if price else (None, None))
    res.fair_value = fv[0] if fv else None
    res.fair_value_text = f.get("FAIR_VALUE")
    res.upside_pct = report_lint.parse_pct(f.get("UPSIDE"))
    res.entry_below = entry[0] if entry else None
    res.exit_above = exit_[0] if exit_ else None
    res.key_risk = f.get("KEY_RISK")
    res.data_warnings = f.get("DATA_WARNINGS")
    res.two_minute_drill = f.get("_drill")
    res.bear_thesis = f.get("_bear")


# --------------------------------------------------------------------------- #
# live price vs the run's bands
# --------------------------------------------------------------------------- #
@dataclass
class Quote:
    price: float
    currency: str | None
    fetched_at: str


def live_quote(ticker: str) -> Quote | None:
    """Vendor last price (yfinance, may be delayed), minor units normalised (GBp -> GBP)."""
    try:
        import yfinance as yf
        from fundamentals import normalise_quote
        fi = yf.Ticker(ticker).fast_info
        price, ccy = normalise_quote(float(fi.last_price), fi.currency)
        if not price or price <= 0:
            return None
        return Quote(price=price, currency=ccy,
                     fetched_at=datetime.now(timezone.utc).isoformat(timespec="minutes"))
    except Exception:
        return None


def band(price: float | None, res: PipelineResult) -> str | None:
    if price is None or res.fair_value is None or res.entry_below is None or res.exit_above is None:
        return None
    if price <= res.entry_below:
        return "at or below ENTRY_BELOW"
    if price <= res.fair_value:
        return "between ENTRY_BELOW and EV"
    if price <= res.exit_above:
        return "between EV and EXIT_ABOVE"
    return "above EXIT_ABOVE"


@dataclass
class PriceCheck:
    quote: Quote | None = None
    change_pct: float | None = None          # live vs the run's PRICE
    upside_now_pct: float | None = None      # EV vs live price
    band_then: str | None = None
    band_now: str | None = None
    refresh_reasons: list[str] = field(default_factory=list)


def price_check(res: PipelineResult, quote: Quote | None) -> PriceCheck:
    """Compare a verified run with the live price. The verdict itself is never recomputed here:
    if the price has crossed one of the run's bands, the answer is to re-run the pipeline."""
    chk = PriceCheck(quote=quote, band_then=band(res.price, res))
    if res.age_days is not None and res.age_days > REUSE_DAYS:
        chk.refresh_reasons.append(f"run is {res.age_days} days old (the skill re-runs after {REUSE_DAYS})")
    if quote is None or res.price is None:
        return chk
    if res.currency and quote.currency and quote.currency != res.currency:
        chk.refresh_reasons.append(f"live quote is in {quote.currency}, the run in {res.currency}: not compared")
        return chk
    chk.change_pct = (quote.price / res.price - 1) * 100
    if res.fair_value is not None and not res.is_fund:
        chk.upside_now_pct = (res.fair_value / quote.price - 1) * 100
    chk.band_now = band(quote.price, res)
    if chk.band_then and chk.band_now and chk.band_now != chk.band_then:
        chk.refresh_reasons.append(f"price moved from '{chk.band_then}' to '{chk.band_now}' since the run, "
                                   "so the verdict rules may now give a different answer")
    if abs(chk.change_pct) >= REFRESH_MOVE * 100:
        chk.refresh_reasons.append(f"price moved {chk.change_pct:+.1f}% since the run")
    return chk


# --------------------------------------------------------------------------- #
# ledger audit
# --------------------------------------------------------------------------- #
def ledger_audit(path: Path = LEDGER) -> list[dict]:
    """Classify each ledger row by the run it came from: verified / unverified / no run folder."""
    rows = list(csv.DictReader(path.open())) if path.exists() else []
    warnings = report_lint.load_warnings()
    cache: dict[Path, list[str]] = {}
    out = []
    for row in rows:
        run = RUNS_DIR / f"{row.get('ticker', '').strip()}_{row.get('as_of', '').strip()}"
        if not run.is_dir():
            status, why = "no-run-folder", "predates reports/runs or the run folder is gone"
        else:
            if run not in cache:
                cache[run] = assess(run, warnings)[0]
            status = "unverified" if cache[run] else "verified"
            why = "; ".join(cache[run][:2])
        out.append({**row, "_status": status, "_why": why, "_run": run.name})
    return out


def main(argv: list[str]) -> int:
    if "--ledger" in argv:
        for r in ledger_audit():
            print(f"{r['as_of']} {r['ticker']:<10} {r['verdict']:<6} {r['_status']:<14} {r['_why'][:110]}")
        return 0
    for t in argv[1:]:
        r = latest(t)
        print(f"{t:<10} {r.status:<10} " + (f"{r.verdict} ({r.conviction}) as of {r.as_of}, "
              f"price {r.price:g} {r.currency}, FV {r.fair_value_text}" if r.verified else "; ".join(r.problems[:3])))
        if r.skipped_runs:
            print(f"           skipped unverified: {', '.join(r.skipped_runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
