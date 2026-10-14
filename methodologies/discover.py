"""Opportunity screen: the programmatic part of /discover (Stage 1, the Scout).

Runs the screener for one or all presets, removes ADR duplicates, checks overlap with current
holdings, and cross-references every candidate with the verified pipeline (pipeline_store).
The output is a list of candidates for `/analyse`. It is never a recommendation: only the
3-agent pipeline issues a verdict.

What changed (14 Oct 2026): this script used to write Stage 2-4 files itself from templates (a
"Vetter" that advanced every candidate, a "Skeptic" whose falsification metric was placeholder
text, a "Strategist" that labelled the top screen hit DEPLOY CAPITAL). On 14 Oct that put ASML.AS
in front of you as DEPLOY CAPITAL on the day the pipeline rated it PASS. The real Stages 2-4 are
the opportunity-vetter / opportunity-skeptic / allocation-strategist agents in the discover skill.

Usage:
  python3 methodologies/discover.py --all
  python3 methodologies/discover.py --preset SINGAPORE_INCOME --universe DIVIDEND_NON_US
  python3 methodologies/discover.py --preset LYNCH_GARP --tickers GOOGL,ULVR.L,DEO
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notify  # noqa: E402
import pipeline_store  # noqa: E402
import report_lint  # noqa: E402
import screener  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DISCOVERY_DIR = PROJECT_ROOT / "reports" / "discovery"
PORTFOLIO_JSON = PROJECT_ROOT / "data" / "portfolio.json"
DOWNSTREAM = ("02_vetted_theses.md", "03_skeptic_critique.md", "03_allocation_recommendation.md",
              "04_allocation_recommendation.md")
# US ADR -> primary listing (the primary listing avoids depositary fees)
ADR_PRIMARY = {"BTI": "BATS.L", "RIO": "RIO.L", "UL": "ULVR.L", "DEO": "DGE.L", "GSK": "GSK.L",
               "AZN": "AZN.L", "SHEL": "SHEL.L", "BP": "BP.L", "RELX": "REL.L"}
SCANS = [
    ("SINGAPORE_INCOME", "DIVIDEND_NON_US", "Non-US dividend payers (0% WHT for a Singapore resident)"),
    ("BUFFETT_MOAT", "EURO_COMPOUNDERS", "High-return European compounders"),
    ("LYNCH_GARP", "FALLEN_STALWARTS", "Lynch growth at a reasonable price / fallen stalwarts"),
    ("NET_CASH_BARGAIN", "ASIA_COMPOUNDERS", "Cash-rich Asian companies"),
]


def load_active_portfolio() -> list[str]:
    """Current holdings from data/portfolio.json (written by portfolio_ocr after /confirm)."""
    try:
        return list(json.loads(PORTFOLIO_JSON.read_text()).get("tickers", []))
    except (OSError, json.JSONDecodeError):
        return []


def _is_held(ticker: str, holdings: list[str]) -> bool:
    primary = ADR_PRIMARY.get(ticker, ticker)
    return ticker in holdings or primary in holdings


def _pipeline_view(ticker: str, warnings: dict) -> dict | None:
    res = pipeline_store.latest(ticker, warnings)
    if res.status == "MISSING":
        return None
    if not res.verified:
        return {"status": res.status, "skipped_runs": res.skipped_runs}
    return {"status": "VERIFIED", "verdict": res.verdict, "conviction": res.conviction,
            "as_of": str(res.as_of), "fair_value_text": res.fair_value_text,
            "report": str(res.report_path.relative_to(PROJECT_ROOT))}


def _candidate(r: screener.ScreenResult, holdings: list[str], warnings: dict) -> dict:
    return {"ticker": r.ticker, "name": r.name, "country": r.country, "sector": r.sector,
            "metrics": screener.metrics_line(r), "why": r.why, "flags": r.flags, "tax": r.tax,
            "score": round(r.score, 2), "held": _is_held(r.ticker, holdings),
            "pipeline": _pipeline_view(r.ticker, warnings), "screen": asdict(r)}


def run_discovery_pipeline(preset: str, universe: str | None = None,
                           custom_tickers: list[str] | None = None, top_n: int = 5) -> dict:
    """Screen one preset and write run_<DATE>_<PRESET>/01_scout_report.md + screened.json.
    Always returns a dict (an empty screen is a result, not a crash)."""
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    run_dir = DISCOVERY_DIR / f"run_{date_str}_{preset}"
    run_dir.mkdir(parents=True, exist_ok=True)
    tickers = custom_tickers or screener.CURATED_UNIVERSES.get(universe or "", []) or \
        list(dict.fromkeys(screener.CURATED_UNIVERSES["FALLEN_STALWARTS"] + screener.CURATED_UNIVERSES["DIVIDEND_NON_US"]))

    diag: dict = {}
    hits = screener.run_screen(tickers, preset, top_n=max(top_n * 3, 10), diagnostics=diag)
    found = {r.ticker for r in hits}
    hits = [r for r in hits if not (r.ticker in ADR_PRIMARY and ADR_PRIMARY[r.ticker] in found)]

    holdings = load_active_portfolio()
    warnings = report_lint.load_warnings()
    candidates, held_hits, analysed = [], [], []
    for r in hits:
        c = _candidate(r, holdings, warnings)
        if c["held"]:
            held_hits.append(c)
        elif (c["pipeline"] or {}).get("status") == "VERIFIED":
            analysed.append(c)          # already has a verdict: show it, don't re-pitch it
        else:
            candidates.append(c)
    candidates = candidates[:top_n]

    # A fresh Stage 1 makes any older Stage 2-4 files describe a different list: move them aside.
    stale = [f for f in DOWNSTREAM if (run_dir / f).exists()]
    if stale:
        dest = run_dir / "_superseded" / datetime.now().strftime("%Y%m%d_%H%M%S")
        dest.mkdir(parents=True, exist_ok=True)
        for f in stale:
            shutil.move(str(run_dir / f), str(dest / f))

    result = {"preset": preset, "universe": universe or ("custom" if custom_tickers else "default"),
              "run_dir": str(run_dir.relative_to(PROJECT_ROOT)), "screened": diag.get("screened", 0),
              "qualified": diag.get("qualified", 0), "failures": diag.get("failures", []),
              "rejected": diag.get("rejected", {}), "rules": screener.SCREEN_RULES[preset],
              "candidates": candidates, "held_hits": held_hits, "analysed": analysed}
    (run_dir / "screened.json").write_text(json.dumps(result, indent=2, default=str))
    (run_dir / "01_scout_report.md").write_text(_scout_markdown(result, date_str))
    print(f"[OK] {preset}: {len(candidates)} new candidates, {len(held_hits)} held, "
          f"{len(analysed)} already analysed, {len(result['failures'])} fetch failures -> {run_dir}")
    return result


def _cand_rows(cands: list[dict]) -> list[str]:
    rows = ["| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |",
            "|---|---|---|---|---|---|---|"]
    for c in cands:
        p = c.get("pipeline") or {}
        view = (f"{p['verdict']} ({p['conviction']}, {p['as_of']})" if p.get("status") == "VERIFIED"
                else f"none verified: `/analyse {c['ticker']}`")
        rows.append(f"| **{c['ticker']}** | {c['name'][:24]} | {c['metrics']} | {c['why']} | "
                    f"{'; '.join(c['flags']) or 'none'} | {c['tax']} | {view} |")
    return rows


def _scout_markdown(res: dict, date_str: str) -> str:
    lines = [f"<!-- pipeline:discover-screen -->",
             f"# Discovery Stage 1: screen, {res['preset']} on {res['universe']} ({date_str})", "",
             "> Quantitative screen on vendor data. Candidates for `/analyse`, not recommendations.",
             f"> Rules: {res['rules']}. Screened {res['screened']}, qualified {res['qualified']}, "
             f"fetch failures {len(res['failures'])}.", "", "## New candidates", ""]
    lines += _cand_rows(res["candidates"]) if res["candidates"] else ["None passed."]
    if res["held_hits"]:
        lines += ["", "## Held positions that passed this screen", "",
                  "Passing a screen is not a reason to add. Use the pipeline verdict.", ""]
        lines += _cand_rows(res["held_hits"])
    if res["analysed"]:
        lines += ["", "## Already analysed by the pipeline", ""] + _cand_rows(res["analysed"])
    if res["failures"]:
        lines += ["", "## Fetch failures", "", ", ".join(res["failures"])]
    return "\n".join(lines) + "\n"


def run_all_presets(top_n: int = 5) -> Path:
    """Run every preset and write MASTER_OPPORTUNITIES_<DATE>.md plus a .json sidecar (the
    Telegram cards are built from the sidecar)."""
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    presets = []
    for preset, universe, desc in SCANS:
        print(f"\n--- {preset} on {universe} ({desc}) ---")
        res = run_discovery_pipeline(preset, universe=universe, top_n=top_n)
        res["description"] = desc
        presets.append(res)

    holdings = load_active_portfolio()
    lines = [f"# Opportunity screen ({date_str})", "",
             "> Screen results from quantitative filters on vendor data (yfinance). These are candidates "
             "for the 3-agent `/analyse` pipeline, not recommendations. A buy, hold or sell view only "
             "comes from a verified pipeline run.",
             f"> Holdings used for the overlap check: {len(holdings)} (data/portfolio.json).", ""]
    for res in presets:
        lines += [f"## {res['preset']}: {res['description']}", "",
                  f"Universe {res['universe']} · screened {res['screened']} · qualified {res['qualified']}"
                  + (f" · fetch failures: {', '.join(res['failures'])}" if res["failures"] else ""), ""]
        lines += _cand_rows(res["candidates"]) if res["candidates"] else ["No new candidates passed."]
        lines.append("")
    held = {c["ticker"]: c for r in presets for c in r["held_hits"]}
    analysed = {c["ticker"]: c for r in presets for c in r["analysed"]}
    if held:
        lines += ["## Held positions that passed a screen", "",
                  "Passing a screen is not a reason to add. The pipeline verdict decides.", ""]
        lines += _cand_rows(list(held.values())) + [""]
    if analysed:
        lines += ["## Screen hits the pipeline has already rated", ""] + _cand_rows(list(analysed.values())) + [""]
    nxt = [c["ticker"] for r in presets for c in r["candidates"][:1]]
    if nxt:
        lines += ["## Next step", "", "Run the 3-agent pipeline on a candidate before any decision:", ""]
        lines += [f"- `/analyse {t}`" for t in nxt]

    DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)
    out = DISCOVERY_DIR / f"MASTER_OPPORTUNITIES_{date_str}.md"
    out.write_text("\n".join(lines) + "\n")
    out.with_suffix(".json").write_text(json.dumps(
        {"as_of": datetime.now(timezone.utc).isoformat(timespec="minutes"), "holdings": len(holdings),
         "presets": presets}, indent=2, default=str))
    print(f"\n[OK] Master screen written to {out}")
    if nxt:
        notify.notify(f"Opportunity screen done ({date_str}): {len(nxt)} candidates for /analyse",
                      title="Opportunity screen complete")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Opportunity screen (Stage 1 of /discover)")
    parser.add_argument("--all", action="store_true", help="run every preset and write the master file")
    parser.add_argument("--preset", choices=screener.PRESETS, default="BUFFETT_MOAT")
    parser.add_argument("--universe", choices=list(screener.CURATED_UNIVERSES), default="FALLEN_STALWARTS")
    parser.add_argument("--tickers", type=str, default=None)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if args.all:
        run_all_presets(top_n=args.top)
    else:
        custom = [x.strip() for x in args.tickers.split(",") if x.strip()] if args.tickers else None
        run_discovery_pipeline(args.preset, universe=args.universe, custom_tickers=custom, top_n=args.top)


if __name__ == "__main__":
    main()
