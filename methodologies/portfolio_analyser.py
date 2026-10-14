"""Portfolio audit built only from verified 3-agent pipeline runs.

For each holding in data/portfolio.json this reads the newest VERIFIED run (pipeline_store:
lint pass + stage-file provenance + lint seal) and reports its verdict block as written, in the
run's own currency, next to the live price. It never computes, guesses or carries a verdict of
its own. A holding without a verified run is listed as needing `/analyse`, with the reason.

The previous version mixed a few ledger fields with ~50 lines of hand-written narrative
(fixed prices, "€" labels on USD values, a "$6B" debt figure the report never contained) that
was sent to Telegram unchanged whatever the data said. All of that is gone.

    python3 methodologies/portfolio_analyser.py                 # holdings from data/portfolio.json
    python3 methodologies/portfolio_analyser.py TSM NVO --no-live
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline_store  # noqa: E402
import report_lint  # noqa: E402
from pipeline_store import PipelineResult, PriceCheck  # noqa: E402

PORTFOLIO_JSON = PROJECT_ROOT / "data" / "portfolio.json"
REPORTS_DIR = PROJECT_ROOT / "reports" / "portfolio"
VERDICT_ORDER = ("SELL", "TRIM", "HOLD", "PASS", "ACCUMULATE", "BUY")


@dataclass
class HoldingRow:
    ticker: str
    name: str | None
    shares: float | None
    shares_note: str | None
    result: PipelineResult
    check: PriceCheck | None = None
    value_usd: float | None = None


@dataclass
class Audit:
    rows: list[HoldingRow]
    generated: str
    snapshot: dict = field(default_factory=dict)
    live: bool = True

    @property
    def verified(self) -> list[HoldingRow]:
        return [r for r in self.rows if r.result.verified]

    @property
    def unverified(self) -> list[HoldingRow]:
        return [r for r in self.rows if not r.result.verified]

    @property
    def refresh(self) -> list[HoldingRow]:
        return [r for r in self.verified if r.check and r.check.refresh_reasons]

    def by_verdict(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for r in self.verified:
            out.setdefault(r.result.verdict or "?", []).append(r.ticker)
        return out


def load_portfolio() -> dict:
    try:
        return json.loads(PORTFOLIO_JSON.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def build_audit(tickers: list[str] | None = None, live: bool = True) -> Audit:
    snap = load_portfolio()
    holdings = {h["ticker"]: h for h in snap.get("holdings", [])}
    order = tickers or list(holdings)
    warnings = report_lint.load_warnings()
    rows = []
    for t in order:
        h = holdings.get(t, {})
        res = pipeline_store.latest(t, warnings)
        row = HoldingRow(ticker=t, name=res.name or h.get("name"), shares=h.get("shares"),
                         shares_note=h.get("shares_note"), result=res)
        if live:
            quote = pipeline_store.live_quote(t)
            if res.verified:
                row.check = pipeline_store.price_check(res, quote)
            if quote and row.shares and not row.shares_note:
                try:
                    from fundamentals import fx_to_usd
                    row.value_usd = row.shares * quote.price * fx_to_usd(quote.currency or "USD")
                except Exception:
                    row.value_usd = None
        rows.append(row)
    return Audit(rows=rows, generated=datetime.now(timezone.utc).isoformat(timespec="minutes"),
                 snapshot={k: snap.get(k) for k in ("as_of", "source_file", "total_holdings_count")},
                 live=live)


# --------------------------------------------------------------------------- #
# formatting helpers (shared with telegram_notifier)
# --------------------------------------------------------------------------- #
def fmt_amount(x: float | None, ccy: str | None = None) -> str:
    if x is None:
        return "UNKNOWN"
    s = f"{x:,.0f}" if (ccy in ("KRW", "JPY") or abs(x) >= 100_000) else f"{x:,.2f}"
    return f"{s} {ccy}" if ccy else s


def fmt_pct(x: float | None) -> str:
    return "n/a" if x is None else f"{x:+.1f}%"


def ev_text(res: PipelineResult) -> str:
    if res.is_fund or res.fair_value is None:
        return res.fair_value_text or "UNKNOWN"
    return fmt_amount(res.fair_value, res.currency)


# --------------------------------------------------------------------------- #
# markdown report
# --------------------------------------------------------------------------- #
def write_report(audit: Audit) -> Path:
    date_str = audit.generated[:10]
    snap = audit.snapshot
    groups = audit.by_verdict()
    lines = [
        f"# Portfolio audit ({date_str})",
        "",
        "> Built only from verified `/analyse` runs: report_lint pass, stage-file provenance (each "
        "stage written by its value-* subagent) and a lint seal from a Claude Code session. Runs "
        "that fail verification are listed with the reason and contribute nothing.",
        f"> Generated {audit.generated} UTC · holdings snapshot `{snap.get('source_file') or 'UNKNOWN'}` "
        f"({snap.get('as_of') or 'UNKNOWN'})"
        + (" · live prices: yfinance last price (may be delayed)" if audit.live else " · no live prices"),
        "",
        "## Coverage",
        f"- Holdings: {len(audit.rows)} · verified verdicts: {len(audit.verified)} · "
        f"need a pipeline run: {len(audit.unverified)}",
        "- Verified verdicts: " + (" · ".join(
            f"{v} {len(groups[v])} ({', '.join(groups[v])})" for v in VERDICT_ORDER if v in groups) or "none"),
    ]
    if audit.unverified:
        lines.append("- No verified verdict (run `/analyse`): " + ", ".join(r.ticker for r in audit.unverified))
    if audit.refresh:
        lines.append("- Re-run advised: " + ", ".join(r.ticker for r in audit.refresh))

    lines += ["", "## Verified verdicts", "",
              "| Ticker | Verdict | Run (age) | Run price | Live | EV / expected return | EV vs live | "
              "Entry / Exit | Live vs bands | Key risk |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(audit.verified, key=lambda r: (VERDICT_ORDER.index(r.result.verdict)
                                                   if r.result.verdict in VERDICT_ORDER else 9, r.ticker)):
        res, chk = r.result, r.check
        live = fmt_amount(chk.quote.price, chk.quote.currency) if chk and chk.quote else "n/a"
        bands = "n/a (FUND)" if res.is_fund else \
            f"{fmt_amount(res.entry_below, res.currency)} / {fmt_amount(res.exit_above, res.currency)}"
        lines.append(
            f"| **{r.ticker}** | {res.verdict} ({res.conviction}) | {res.as_of} ({res.age_days}d) | "
            f"{fmt_amount(res.price, res.currency)} | {live} | {ev_text(res)} | "
            f"{fmt_pct(chk.upside_now_pct) if chk else 'n/a'} | {bands} | "
            f"{(chk.band_now if chk and chk.band_now else 'n/a')} | {res.key_risk or ''} |")

    if audit.refresh:
        lines += ["", "## Re-run advised", ""]
        for r in audit.refresh:
            lines.append(f"- **{r.ticker}**: " + "; ".join(r.check.refresh_reasons))

    if audit.unverified:
        lines += ["", "## No verified verdict", "",
                  "| Ticker | Shares | Status | Why |", "|---|---|---|---|"]
        for r in audit.unverified:
            res = r.result
            why = "; ".join(res.problems[:2]) or "no pipeline run on file"
            if res.skipped_runs:
                why = f"runs {', '.join(res.skipped_runs)} failed verification: {why}"
            lines.append(f"| **{r.ticker}** | {r.shares if r.shares is not None else 'UNKNOWN'} | "
                         f"{res.status} | {why} |")

    lines += ["", "## Holding notes (verbatim from the verified reports)", ""]
    for r in audit.verified:
        res = r.result
        lines += [f"### {r.ticker} — {res.name or ''} ({res.verdict}, {res.conviction})", ""]
        if res.two_minute_drill:
            lines += [res.two_minute_drill, ""]
        if res.bear_thesis:
            lines += [f"- **Bear thesis:** {res.bear_thesis}"]
        lines += [f"- **Report:** `{res.report_path.relative_to(PROJECT_ROOT)}`", ""]

    notes = [f"- **{r.ticker}**: {r.shares_note}" for r in audit.rows if r.shares_note]
    if notes:
        lines += ["## Data notes", ""] + notes + [""]

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"PORTFOLIO_AUDIT_{date_str}.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def run_portfolio_analysis(tickers: list[str] | None = None, live: bool = True) -> Path:
    """Build the audit and write the markdown report. Returns the report path."""
    report = write_report(build_audit(tickers, live=live))
    print(f"[OK] Portfolio audit written to {report}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Portfolio audit from verified pipeline runs")
    parser.add_argument("tickers", nargs="*", help="default: holdings in data/portfolio.json")
    parser.add_argument("--no-live", action="store_true", help="skip live prices")
    args = parser.parse_args()
    run_portfolio_analysis(args.tickers or None, live=not args.no_live)


if __name__ == "__main__":
    main()
