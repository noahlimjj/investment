"""Programmatic value screen: Stage 1 (Scout) of /discover.

Filters curated universes with Buffett/Lynch-style thresholds on vendor (yfinance) data and tags
Singapore-resident tax facts. Output is a list of CANDIDATES for the 3-agent /analyse pipeline:
what passed the filters and what the data flags. It is never a recommendation, and the text it
writes contains only figures computed here from the vendor data, never a story.

Presets (thresholds in SCREEN_RULES below; the discover skill and COMMANDS.md quote these):
  BUFFETT_MOAT      return blend >= 12%, operating margin >= 12%, net debt/EBITDA <= 3.5x
                    (financials: ROE >= 12%)
  LYNCH_GARP        0 < forward P/E <= 25 and Lynch ratio (EPS growth % + yield %) / P/E >= 1.0
  NET_CASH_BARGAIN  non-financial, net cash >= 10% of market cap, forward P/E <= 20
  SINGAPORE_INCOME  non-US domicile, dividend yield >= 3%, net debt/EBITDA <= 3.5x
                    (financials: ROE >= 10%)

Vendor-format notes (checked against yfinance 1.7.0, Oct 2026):
  * `dividendYield` is a PERCENT (KO 2.36 = 2.36%). The old "< 0.2 means a fraction" guess turned
    a 0.15% yield into 15%. `trailingAnnualDividendYield` is a fraction but is 100x too small for
    LSE pence quotes, so it isn't used.
  * Margins, ROE, ROA and `earningsGrowth` are FRACTIONS (GOOGL earningsGrowth 2.94 = +294%). The
    old "< 1 means a fraction" guess read 2.94 as 2.94% and any ROE above 100% as about 1%.
  * `earningsGrowth` is the latest quarter year-on-year. It is noisy, so growth above 100% is
    treated as a one-off and no Lynch ratio is computed from it.

Usage:
  python3 methodologies/screener.py --preset BUFFETT_MOAT --universe EURO_COMPOUNDERS
  python3 methodologies/screener.py --preset LYNCH_GARP --tickers GOOGL,ULVR.L,DGE.L
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fundamentals import MINOR_UNITS, fx_to_usd  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CURATED_UNIVERSES = {
    "GLOBAL_QUALITY": [
        "GOOGL", "AAPL", "MSFT", "AMZN", "META", "BRK-B", "UNH", "JNJ", "PG", "V",
        "MA", "HD", "COST", "ABT", "PEP", "KO", "TMO", "MCD", "CSCO", "ACN", "LIN",
        "TXN", "PM", "NEE", "BMY", "DHR", "NKE", "INTU", "LOW", "UPS", "DE",
        "ULVR.L", "DGE.L", "REL.L", "AZN.L", "GSK.L", "BATS.L", "SHEL.L", "RIO.L",
        "NESN.SW", "NOVN.SW", "ROG.SW", "ASML.AS", "OR.PA", "SAN.PA", "AIR.PA",
        "7203.T", "6758.T", "9984.T", "8058.T", "8001.T", "8031.T", "6861.T", "4063.T",
    ],
    "FALLEN_STALWARTS": [
        "NKE", "SBUX", "LULU", "EL", "MDLZ", "TGT", "DE", "ZTS", "ILMN", "BTI",
        "DGE.L", "ULVR.L", "BATS.L", "BAYN.DE", "BN.PA", "KER.PA", "7974.T",
    ],
    "DIVIDEND_NON_US": [
        "BATS.L", "ULVR.L", "DGE.L", "RIO.L", "GSK.L", "AZN.L", "SHEL.L", "REL.L",
        "D05.SI", "O39.SI", "U11.SI", "NG.L", "VOD.L", "BTI", "UL", "DEO", "RIO",
    ],
    "SP500_DEFENSIVE": [
        "JNJ", "PG", "KO", "PEP", "CL", "MDT", "LMT", "RTX", "NOC", "GD", "ABBV", "MRK", "HRL", "GIS", "KMB",
    ],
    "ASIA_COMPOUNDERS": [
        "7203.T", "6758.T", "8058.T", "8031.T", "4063.T", "6861.T", "D05.SI", "O39.SI", "U11.SI", "7974.T",
    ],
    "EURO_COMPOUNDERS": [
        "NESN.SW", "NOVN.SW", "ROG.SW", "ASML.AS", "OR.PA", "SAN.PA", "AIR.PA", "SAP.DE", "RACE", "ITX.MC", "MC.PA",
    ],
}
PRESETS = ("BUFFETT_MOAT", "LYNCH_GARP", "NET_CASH_BARGAIN", "SINGAPORE_INCOME")
SCREEN_RULES = {
    "BUFFETT_MOAT": {"min_return_blend": 12.0, "min_op_margin": 12.0, "max_nd_ebitda": 3.5, "min_fin_roe": 12.0},
    "LYNCH_GARP": {"max_fwd_pe": 25.0, "min_lynch_ratio": 1.0},
    "NET_CASH_BARGAIN": {"min_net_cash_pct": 10.0, "max_fwd_pe": 20.0},
    "SINGAPORE_INCOME": {"min_yield": 3.0, "max_nd_ebitda": 3.5, "min_fin_roe": 10.0},
}
MAX_CREDIBLE_GROWTH = 100.0      # % YoY; above this the quarter is treated as a one-off
MAX_CREDIBLE_YIELD = 15.0        # %; above this the vendor yield is flagged
FINANCIAL_SECTORS = {"Financial Services", "Financials", "Banking"}
ZERO_WHT = {"United Kingdom": "UK: 0% dividend WHT",
            "Singapore": "Singapore: 0% dividend WHT (one-tier)",
            "Hong Kong": "Hong Kong: 0% dividend WHT for HK companies (H-shares differ)"}


@dataclass
class ScreenResult:
    ticker: str
    name: str
    sector: str
    country: str
    currency: str
    price: float
    high_52w: float
    drawdown_52w_pct: float
    market_cap_usd_bn: float | None
    trailing_pe: float | None
    forward_pe: float | None
    peg_ratio: float | None
    lynch_ratio: float | None
    eps_growth_pct: float | None
    net_cash_per_share: float
    net_cash_pct_price: float
    net_cash_adj_pe: float | None
    dividend_yield_pct: float
    roic_proxy_pct: float | None          # 0.6*ROE + 0.4*ROA: a return blend, NOT ROIC
    gross_margin_pct: float | None
    operating_margin_pct: float | None
    debt_to_equity: float | None
    net_debt_to_ebitda: float | None
    ev_to_ebitda: float | None = None
    is_financial: bool = False
    tax: str = ""
    why: str = ""                         # the thresholds it passed, with its own figures
    flags: list[str] = field(default_factory=list)
    score: float = 0.0
    qualifies: bool = True
    rejection_reason: str | None = None


def _pct(x) -> float | None:
    """yfinance ratio fields are fractions; return percent, keeping None as None."""
    return None if x is None else float(x) * 100.0


def tax_tag(ticker: str, country: str) -> str:
    if country in ("United States", "US"):
        return "US-domiciled: 30% dividend WHT; US-situs for estate tax (above US$60k)"
    tag = ZERO_WHT.get(country) or (
        "Japan: 15.315% dividend WHT" if country == "Japan" else f"{country}: local dividend WHT (check treaty rate)")
    if "." not in ticker:
        tag += ("; US-listed foreign issuer (ADR or direct listing): check depositary fees; US estate-tax "
                "treatment unsettled, the home-market listing avoids it")
    return tag


def fetch_and_screen_ticker(ticker: str, preset: str) -> ScreenResult | None:
    """Screen one ticker. Returns None only when the vendor has no usable price."""
    info = yf.Ticker(ticker).info or {}
    price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
    if not price or price <= 0:
        return None
    name = (info.get("shortName") or info.get("longName") or ticker).strip()
    sector = info.get("sector") or "Unknown"
    country = info.get("country") or "Unknown"
    currency = info.get("currency") or "USD"
    high_52w = info.get("fiftyTwoWeekHigh") or price
    if currency in MINOR_UNITS:
        major, div = MINOR_UNITS[currency]
        price, high_52w, currency = price / div, high_52w / div, major
    drawdown = (price / high_52w - 1) * 100.0 if high_52w > 0 else 0.0

    market_cap = info.get("marketCap") or 0.0
    try:
        mcap_usd_bn = market_cap * fx_to_usd(currency) / 1e9 if market_cap else None
    except Exception:
        mcap_usd_bn = None

    trailing_pe, forward_pe, peg = info.get("trailingPE"), info.get("forwardPE"), info.get("pegRatio")
    div_yield = float(info.get("dividendYield") or 0.0)            # already a percent
    growth = _pct(info.get("earningsGrowth"))
    if growth is None:
        growth = _pct(info.get("earningsQuarterlyGrowth"))
    gross, oper = _pct(info.get("grossMargins")), _pct(info.get("operatingMargins"))
    roe, roa = _pct(info.get("returnOnEquity")), _pct(info.get("returnOnAssets"))
    return_blend = (roe * 0.6 + roa * 0.4) if (roe and roa and roe > 0 and roa > 0) else (roe if roe and roe > 0 else None)

    pe_for_lynch = forward_pe if forward_pe and forward_pe > 0 else trailing_pe
    growth_spike = growth is not None and growth > MAX_CREDIBLE_GROWTH
    lynch = ((growth + div_yield) / pe_for_lynch
             if pe_for_lynch and pe_for_lynch > 0 and growth is not None and growth > 0 and not growth_spike
             else None)

    cash, debt = info.get("totalCash") or 0.0, info.get("totalDebt") or 0.0
    shares = info.get("sharesOutstanding") or 0.0
    net_cash = cash - debt
    net_cash_ps = net_cash / shares if shares > 0 else 0.0
    net_cash_pct = net_cash_ps / price * 100.0 if price > 0 else 0.0
    eps = info.get("trailingEps")
    nc_adj_pe = (price - net_cash_ps) / eps if eps and eps > 0 and price > net_cash_ps else None
    ebitda = info.get("ebitda") or 0.0
    nd_ebitda = (-net_cash / ebitda) if ebitda > 0 else None
    d2e = info.get("debtToEquity")
    is_fin = sector in FINANCIAL_SECTORS
    ev = info.get("enterpriseValue") or ((market_cap + debt - cash) if market_cap else None)
    ev_ebitda = round(ev / ebitda, 1) if (not is_fin and ebitda > 0 and ev and ev > 0) else None
    is_us = country in ("United States", "US")

    flags = []
    if is_fin:
        flags.append("financial: judged on ROE, not EV/EBITDA or net cash")
    if forward_pe and trailing_pe and forward_pe > trailing_pe:
        flags.append(f"forward P/E {forward_pe:.1f} > trailing {trailing_pe:.1f}: earnings expected to fall")
    if growth_spike:
        flags.append(f"EPS growth {growth:+.0f}% (latest quarter YoY) looks one-off: no Lynch ratio")
    if div_yield > MAX_CREDIBLE_YIELD:
        flags.append(f"yield {div_yield:.1f}% is implausible: vendor artifact or special dividend")
    if nd_ebitda is not None and nd_ebitda > 2.5:
        flags.append(f"net debt/EBITDA {nd_ebitda:.1f}x")
    if drawdown < -30:
        flags.append(f"{drawdown:.0f}% from 52w high: find out why before anything else")
    if is_us and div_yield > 2.0:
        flags.append(f"30% US WHT cuts the {div_yield:.1f}% yield to {div_yield * 0.7:.1f}%")

    rules = SCREEN_RULES[preset]
    qualifies, rejection, score, why = True, None, 0.0, ""
    if preset == "BUFFETT_MOAT":
        if is_fin:
            if roe is None or roe < rules["min_fin_roe"]:
                qualifies, rejection = False, f"financial ROE {roe if roe is None else round(roe, 1)}% < {rules['min_fin_roe']}%"
            else:
                score, why = roe * 0.6 + abs(min(drawdown, 0)) * 0.4, f"ROE {roe:.1f}%, {drawdown:.1f}% from 52w high"
        elif return_blend is None or return_blend < rules["min_return_blend"]:
            qualifies, rejection = False, f"return blend {return_blend if return_blend is None else round(return_blend, 1)}% < {rules['min_return_blend']}%"
        elif oper is None or oper < rules["min_op_margin"]:
            qualifies, rejection = False, f"operating margin {oper if oper is None else round(oper, 1)}% < {rules['min_op_margin']}%"
        elif nd_ebitda is not None and nd_ebitda > rules["max_nd_ebitda"]:
            qualifies, rejection = False, f"net debt/EBITDA {nd_ebitda:.1f}x > {rules['max_nd_ebitda']}x"
        else:
            score = return_blend * 0.4 + oper * 0.3 + abs(min(drawdown, 0)) * 0.3
            why = (f"return blend {return_blend:.1f}% (0.6 ROE + 0.4 ROA), operating margin {oper:.1f}%, "
                   f"net debt/EBITDA {'n/a' if nd_ebitda is None else f'{nd_ebitda:.1f}x'}, {drawdown:.1f}% from 52w high")
    elif preset == "LYNCH_GARP":
        if not forward_pe or forward_pe <= 0 or forward_pe > rules["max_fwd_pe"]:
            qualifies, rejection = False, f"forward P/E {forward_pe} outside 0-{rules['max_fwd_pe']:.0f}x"
        elif lynch is None or lynch < rules["min_lynch_ratio"]:
            qualifies = False
            rejection = ("no usable EPS growth for a Lynch ratio" if lynch is None
                         else f"Lynch ratio {lynch:.2f} < {rules['min_lynch_ratio']}")
        else:
            cash_bonus = 0.0 if is_fin else net_cash_pct * 0.5
            score = lynch * 20.0 + 100.0 / forward_pe + cash_bonus
            why = (f"Lynch ratio {lynch:.2f} = ({growth:.1f}% EPS growth, latest quarter YoY + {div_yield:.1f}% "
                   f"yield) / {pe_for_lynch:.1f}x P/E; forward P/E {forward_pe:.1f}x")
    elif preset == "NET_CASH_BARGAIN":
        if is_fin:
            qualifies, rejection = False, "financial: deposits are operating liabilities, net cash doesn't apply"
        elif net_cash_pct < rules["min_net_cash_pct"]:
            qualifies, rejection = False, f"net cash {net_cash_pct:.1f}% of price < {rules['min_net_cash_pct']}%"
        elif not forward_pe or forward_pe <= 0 or forward_pe > rules["max_fwd_pe"]:
            qualifies, rejection = False, f"forward P/E {forward_pe} outside 0-{rules['max_fwd_pe']:.0f}x"
        else:
            score = net_cash_pct * 1.5 + 100.0 / forward_pe
            why = (f"net cash {net_cash_pct:.1f}% of price, forward P/E {forward_pe:.1f}x"
                   + (f", net-cash-adjusted P/E {nc_adj_pe:.1f}x" if nc_adj_pe else ""))
    elif preset == "SINGAPORE_INCOME":
        if is_us:
            qualifies, rejection = False, "US domicile: 30% dividend WHT"
        elif div_yield < rules["min_yield"]:
            qualifies, rejection = False, f"dividend yield {div_yield:.1f}% < {rules['min_yield']}%"
        elif div_yield > MAX_CREDIBLE_YIELD:
            qualifies, rejection = False, f"dividend yield {div_yield:.1f}% not credible (vendor artifact?)"
        elif is_fin:
            if roe is None or roe < rules["min_fin_roe"]:
                qualifies, rejection = False, f"bank ROE {roe if roe is None else round(roe, 1)}% < {rules['min_fin_roe']}%"
            else:
                score, why = div_yield * 12.0 + roe * 0.8, f"yield {div_yield:.1f}%, ROE {roe:.1f}%"
        elif nd_ebitda is not None and nd_ebitda > rules["max_nd_ebitda"]:
            qualifies, rejection = False, f"net debt/EBITDA {nd_ebitda:.1f}x > {rules['max_nd_ebitda']}x"
        else:
            score = div_yield * 10.0 + (return_blend or 10.0) * 0.5 + abs(min(drawdown, 0)) * 0.2
            why = (f"yield {div_yield:.1f}%, net debt/EBITDA {'n/a' if nd_ebitda is None else f'{nd_ebitda:.1f}x'}"
                   + (f", return blend {return_blend:.1f}%" if return_blend else ""))

    return ScreenResult(
        ticker=ticker, name=name, sector=sector, country=country, currency=currency, price=price,
        high_52w=high_52w, drawdown_52w_pct=drawdown, market_cap_usd_bn=mcap_usd_bn,
        trailing_pe=trailing_pe, forward_pe=forward_pe, peg_ratio=peg, lynch_ratio=lynch,
        eps_growth_pct=growth, net_cash_per_share=net_cash_ps, net_cash_pct_price=net_cash_pct,
        net_cash_adj_pe=nc_adj_pe, dividend_yield_pct=div_yield, roic_proxy_pct=return_blend,
        gross_margin_pct=gross, operating_margin_pct=oper,
        debt_to_equity=d2e / 100.0 if d2e is not None else None, net_debt_to_ebitda=nd_ebitda,
        ev_to_ebitda=ev_ebitda, is_financial=is_fin, tax=tax_tag(ticker, country), why=why,
        flags=flags, score=score, qualifies=qualifies, rejection_reason=rejection)


def metrics_line(r: ScreenResult) -> str:
    pe = "/".join(f"{x:.1f}x" if x else "n/m" for x in (r.trailing_pe, r.forward_pe))
    parts = [f"{r.price:,.2f} {r.currency}", f"{r.drawdown_52w_pct:.1f}% vs 52w high", f"P/E (ttm/fwd) {pe}",
             f"EV/EBITDA {r.ev_to_ebitda:.1f}x" if r.ev_to_ebitda else "EV/EBITDA n/a",
             f"yield {r.dividend_yield_pct:.1f}%"]
    return " · ".join(parts)


def run_screen(tickers: list[str], preset: str, top_n: int = 10,
               diagnostics: dict | None = None) -> list[ScreenResult]:
    """Qualifying candidates, best score first. Fetch failures and rejections go to
    `diagnostics` instead of disappearing (a vendor outage used to look like "nothing qualified")."""
    diag = diagnostics if diagnostics is not None else {}
    diag.setdefault("failures", [])
    diag.setdefault("rejected", {})
    diag["screened"] = len(tickers)
    results = []
    print(f"Screening {len(tickers)} tickers under preset: {preset}...")
    for t in tickers:
        t = t.strip().upper()
        try:
            res = fetch_and_screen_ticker(t, preset)
        except Exception as exc:
            diag["failures"].append(f"{t}: {type(exc).__name__}")
            continue
        if res is None:
            diag["failures"].append(f"{t}: no price from vendor")
        elif not res.qualifies:
            diag["rejected"][t] = res.rejection_reason
        else:
            results.append(res)
    results.sort(key=lambda r: r.score, reverse=True)
    diag["qualified"] = len(results)
    return results[:top_n]


def format_markdown_table(results: list[ScreenResult], preset: str) -> str:
    lines = [f"### Screen results: `{preset}`",
             f"*{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · vendor data (yfinance) · "
             "candidates for /analyse, not recommendations*", "",
             "| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) |",
             "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| **{r.ticker}** | {r.name[:24]} | {metrics_line(r)} | {r.why} | "
                     f"{'; '.join(r.flags) or 'none'} | {r.tax} |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Value screen (Stage 1 of /discover)")
    parser.add_argument("--preset", choices=PRESETS, default="BUFFETT_MOAT")
    parser.add_argument("--universe", choices=list(CURATED_UNIVERSES), default=None)
    parser.add_argument("--tickers", type=str, default=None, help="comma-separated tickers")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--out", type=str, default=str(PROJECT_ROOT / "data" / "screened_candidates.json"))
    args = parser.parse_args()

    if args.tickers:
        tickers = [x.strip() for x in args.tickers.split(",") if x.strip()]
    elif args.universe:
        tickers = CURATED_UNIVERSES[args.universe]
    else:
        tickers = list(dict.fromkeys(CURATED_UNIVERSES["FALLEN_STALWARTS"] + CURATED_UNIVERSES["DIVIDEND_NON_US"]))
    diag: dict = {}
    top = run_screen(tickers, args.preset, top_n=args.top, diagnostics=diag)
    print("\n" + format_markdown_table(top, args.preset))
    if diag["failures"]:
        print(f"\nFetch failures ({len(diag['failures'])}): {', '.join(diag['failures'])}")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"as_of": datetime.now(timezone.utc).isoformat(), "preset": args.preset,
                               "rules": SCREEN_RULES[args.preset], "count": len(top),
                               "diagnostics": diag, "candidates": [asdict(r) for r in top]}, indent=2))
    print(f"\n[OK] Saved {len(top)} candidates to {out}")


if __name__ == "__main__":
    main()
