"""Hardened fundamentals fetcher.

Replaces deep_fetch.py / scratch_fetch.py. Fixes, in order of damage caused:

  1. Owner Earnings. The old code looked up cash_flow.loc["Net Income"], which does
     not exist in yfinance's index (the label is "Net Income From Continuing
     Operations"). net_income silently became 0 and Owner Earnings collapsed to
     (D&A - CapEx) -- understating UNH by 21x, LAD by 17x, and flipping RR.L's sign.
     We now resolve every row against a candidate list and RAISE if none match.

  2. Bare `except:`. Every failure became "Data unavailable" or a silently wrong
     number. Errors are now typed, recorded per-ticker, and never coerced to a value.

  3. Currency. RR.L quotes in GBp (pence) but reports financials in GBP (pounds) --
     a 100x mismatch. Every record now carries quote/financial currency, is
     normalised to major units, and gets a USD translation for cross-holding work.

  4. null vs 0. Missing fields stay None and are flagged. The old pipeline turned
     Nintendo's missing DebtToEquity into the claim "Zero debt" in a BUY thesis.

  5. Staleness. Every record and file is timestamped `as_of`.

Usage:
    python3 methodologies/fundamentals.py AAPL MSFT RR.L
    python3 methodologies/fundamentals.py --universe        # portfolio from UNIVERSE
"""
from __future__ import annotations

import fcntl
import json
import math
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any

import yfinance as yf

UNIVERSE = ("LAD UNH RR.L SYK NVO AES ZBH VEEV BRK-B VOO MDT MC.PA ACAD WKL.AS ABT "
            "AERO.SW PFE VXUS CNQ INSM PRAX BABA TM MSFT 7974.T MDGL RVMD CELC").split()

# Quote currencies reported in minor units (pence, cents) -> (major code, divisor)
MINOR_UNITS = {"GBp": ("GBP", 100.0), "ZAc": ("ZAR", 100.0), "ILA": ("ILS", 100.0)}

# Funds/ETFs have no income statement; skip the operating-company checks.
FUND_TYPES = {"ETF", "MUTUALFUND", "INDEX", "CURRENCY"}


class DataQualityError(Exception):
    """Raised when a required input is missing or fails a sanity bound."""


# --------------------------------------------------------------------------- #
# row resolution
# --------------------------------------------------------------------------- #
ROW_CANDIDATES = {
    "net_income": (
        "Net Income",
        "Net Income From Continuing Operations",
        "Net Income Common Stockholders",
        "Net Income Continuous Operations",
    ),
    "d_and_a": (
        "Depreciation And Amortization",
        "Depreciation Amortization Depletion",
        "Depreciation",
    ),
    "capex": (
        "Capital Expenditure",
        "Capital Expenditures",
        "Purchase Of PPE",
        "Net PPE Purchase And Sale",
    ),
    "fcf_reported": (
        "Free Cash Flow",
    ),
    "ocf": (
        "Operating Cash Flow",
        "Cash Flow From Continuing Operating Activities",
        "Total Cash From Operating Activities",
    ),
}


def resolve_row(df, key: str, *, required: bool = True) -> float | None:
    """Return the most recent value for a logical row, or raise if unresolvable.

    This is the fix for the Owner Earnings bug: never silently default to 0.
    """
    if df is None or getattr(df, "empty", True):
        if required:
            raise DataQualityError(f"{key}: statement is empty")
        return None
    for label in ROW_CANDIDATES[key]:
        if label in df.index:
            series = df.loc[label].dropna()
            if not series.empty:
                return float(series.iloc[0])
    if required:
        raise DataQualityError(
            f"{key}: none of {ROW_CANDIDATES[key]} found in index {list(df.index)[:8]}..."
        )
    return None


# --------------------------------------------------------------------------- #
# currency
# --------------------------------------------------------------------------- #
_FX_CACHE: dict[str, float] = {"USD": 1.0}


def fx_to_usd(code: str) -> float:
    """Spot rate: 1 unit of `code` -> USD. Raises rather than assuming parity."""
    if code in _FX_CACHE:
        return _FX_CACHE[code]
    hist = yf.Ticker(f"{code}USD=X").history(period="5d")
    if hist.empty:
        raise DataQualityError(f"no FX rate available for {code}USD")
    rate = float(hist["Close"].dropna().iloc[-1])
    _FX_CACHE[code] = rate
    return rate


def normalise_quote(price: float | None, quote_ccy: str | None) -> tuple[float | None, str | None]:
    """Convert a minor-unit quote (GBp pence) to major units (GBP). The old
    pipeline compared RR.L's 1529.8 pence against a GBP market cap -- a 100x error."""
    if price is None or quote_ccy is None:
        return price, quote_ccy
    if quote_ccy in MINOR_UNITS:
        major, divisor = MINOR_UNITS[quote_ccy]
        return price / divisor, major
    return price, quote_ccy


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #
def _finite(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def validate(rec: "Record") -> list[str]:
    """Bounds checks that turn silent corruption into visible warnings.

    Every rule here corresponds to a specific defect found in the existing
    reports -- see methodologies/METHODOLOGY_AUDIT.md.
    """
    w: list[str] = []
    is_fund = (rec.quote_type or "").upper() in FUND_TYPES

    # ownership fractions must be 0..1 (LAD came through at 1.16 -> "116%")
    for name in ("institutional_pct", "insider_pct"):
        v = getattr(rec, name)
        if _finite(v) and not (0.0 <= v <= 1.0):
            w.append(f"{name}={v:.4f} outside 0..1 - vendor artifact, do not quote as a fact")

    # ROE outside +/-100% is almost always a depressed/negative equity base (RR.L: 623%)
    if _finite(rec.roe) and abs(rec.roe) > 1.0:
        w.append(f"roe={rec.roe:.2%} implies a distorted equity base - use ROCE/ROIC instead")

    # owner earnings larger than market cap is impossible (TM came through at -$2.9T)
    if _finite(rec.owner_earnings_usd) and _finite(rec.market_cap_usd) and rec.market_cap_usd:
        if abs(rec.owner_earnings_usd) > 3 * rec.market_cap_usd:
            w.append("owner_earnings exceeds 3x market cap - almost certainly a unit/FX error")

    # PEG is void when earnings are shrinking; this is the NVO failure mode
    if _finite(rec.trailing_pe) and _finite(rec.forward_pe):
        if rec.forward_pe > rec.trailing_pe and _finite(rec.peg) and rec.peg > 0:
            w.append(
                f"forward P/E ({rec.forward_pe:.1f}) > trailing ({rec.trailing_pe:.1f}): earnings "
                f"are declining, so PEG={rec.peg} is meaningless - VOID, use FCF yield / DCF"
            )

    # null must never be read as zero (Nintendo's missing D/E became "Zero debt")
    if not is_fund:
        for name in ("debt_to_equity", "roe", "market_cap_usd"):
            if getattr(rec, name) is None:
                w.append(f"{name} is MISSING (null) - absent, not zero; do not assert a value")

    if _finite(rec.owner_earnings_usd) and rec.owner_earnings_usd < 0:
        w.append("owner earnings negative - confirm against the cash flow statement before use")

    return w


# --------------------------------------------------------------------------- #
# record
# --------------------------------------------------------------------------- #
@dataclass
class Record:
    ticker: str
    as_of: str
    name: str | None = None
    sector: str | None = None
    industry: str | None = None
    quote_type: str | None = None

    quote_currency: str | None = None
    financial_currency: str | None = None
    fx_to_usd: float | None = None

    price: float | None = None                 # major units of quote_currency
    price_usd: float | None = None
    market_cap_usd: float | None = None

    trailing_pe: float | None = None
    forward_pe: float | None = None
    peg: float | None = None
    peg_valid: bool | None = None
    roe: float | None = None
    debt_to_equity: float | None = None

    net_income: float | None = None            # financial_currency
    d_and_a: float | None = None
    capex: float | None = None                 # negative as reported
    ocf: float | None = None
    owner_earnings: float | None = None        # NI + D&A - CapEx, financial_currency
    owner_earnings_usd: float | None = None
    fcf: float | None = None                   # OCF - CapEx
    fcf_usd: float | None = None

    gross_margins: list[float] = field(default_factory=list)
    operating_margins: list[float] = field(default_factory=list)

    institutional_pct: float | None = None
    insider_pct: float | None = None
    beta: float | None = None          # vendor raw beta; Quant Blume-adjusts

    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# fetch
# --------------------------------------------------------------------------- #
def _margin_series(income, n: int = 5) -> tuple[list[float], list[float]]:
    if income is None or getattr(income, "empty", True):
        return [], []
    if "Total Revenue" not in income.index:
        return [], []
    rev = income.loc["Total Revenue"]
    gross, oper = [], []
    if "Gross Profit" in income.index:
        gross = (income.loc["Gross Profit"] / rev).dropna().head(n).tolist()
    if "Operating Income" in income.index:
        oper = (income.loc["Operating Income"] / rev).dropna().head(n).tolist()
    return gross, oper


def fetch(ticker: str) -> Record:
    """Build one validated record. Never returns a silently-wrong number:
    anything unresolvable lands in .errors or .warnings."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rec = Record(ticker=ticker, as_of=now)
    t = yf.Ticker(ticker)

    try:
        info = t.info or {}
    except Exception as exc:                                  # network/vendor failure
        rec.errors.append(f"info fetch failed: {type(exc).__name__}: {exc}")
        return rec

    rec.name = info.get("longName")
    rec.sector = info.get("sector")
    rec.industry = info.get("industry")
    rec.quote_type = info.get("quoteType")

    raw_price = info.get("currentPrice") or info.get("regularMarketPrice")
    rec.price, rec.quote_currency = normalise_quote(raw_price, info.get("currency"))
    rec.financial_currency = info.get("financialCurrency") or rec.quote_currency

    if rec.quote_currency:
        try:
            rec.fx_to_usd = fx_to_usd(rec.quote_currency)
            if _finite(rec.price):
                rec.price_usd = rec.price * rec.fx_to_usd
        except DataQualityError as exc:
            rec.errors.append(str(exc))

    # marketCap is denominated in the MAJOR unit of the QUOTE currency (already
    # normalised above), NOT the financial currency. ADRs like TM quote in USD while
    # reporting in JPY; using financial_currency understated TM by 159x.
    mcap = info.get("marketCap")
    if _finite(mcap):
        try:
            rec.market_cap_usd = mcap * fx_to_usd(rec.quote_currency or "USD")
        except DataQualityError as exc:
            rec.errors.append(f"market cap FX: {exc}")

    rec.trailing_pe = info.get("trailingPE")
    rec.forward_pe = info.get("forwardPE")
    rec.peg = info.get("pegRatio")
    rec.roe = info.get("returnOnEquity")
    d2e = info.get("debtToEquity")
    rec.debt_to_equity = d2e / 100.0 if _finite(d2e) else None   # vendor reports percent
    rec.institutional_pct = info.get("heldPercentInstitutions")
    rec.insider_pct = info.get("heldPercentInsiders")
    rec.beta = info.get("beta") if _finite(info.get("beta")) else None

    if (rec.quote_type or "").upper() in FUND_TYPES:
        rec.warnings.append("fund/ETF: operating-company metrics do not apply")
        rec.warnings.extend(validate(rec))
        return rec

    # ---- statements -------------------------------------------------------
    try:
        cf = t.cashflow
        rec.net_income = resolve_row(cf, "net_income")
        # IFRS cash-flow statements start from PRE-tax profit, which yfinance still labels
        # "Net Income From Continuing Operations" (TSM: NT$2.04T pre-tax vs NT$1.70T net,
        # overstating owner earnings ~20%). The income statement is authoritative.
        try:
            ni_is = resolve_row(t.financials, "net_income", required=False)
        except Exception:
            ni_is = None
        if _finite(ni_is) and _finite(rec.net_income) and ni_is and \
                abs(rec.net_income / ni_is - 1) > 0.05:
            rec.warnings.append(
                f"cash-flow net income {rec.net_income:,.0f} differs from income-statement "
                f"{ni_is:,.0f} by {rec.net_income / ni_is - 1:+.0%} (IFRS pre-tax start?) - "
                "income statement used")
            rec.net_income = ni_is
        rec.d_and_a = resolve_row(cf, "d_and_a")
        rec.capex = resolve_row(cf, "capex", required=False)
        rec.ocf = resolve_row(cf, "ocf", required=False)
        if rec.capex is None:
            # Asset-light issuers (e.g. VEEV) publish no capex line. FCF = OCF + capex,
            # so capex = FCF - OCF. Derive rather than fail the record.
            reported_fcf = resolve_row(cf, "fcf_reported", required=False)
            if reported_fcf is not None and rec.ocf is not None:
                rec.capex = reported_fcf - rec.ocf
                rec.warnings.append(
                    "capex not reported; derived as (Free Cash Flow - Operating Cash Flow)")
            else:
                raise DataQualityError("capex unresolvable and cannot be derived from FCF/OCF")
        # Owner Earnings = Net Income + D&A - CapEx. yfinance reports CapEx negative,
        # so we add it. The old code got here with net_income silently 0.
        rec.owner_earnings = rec.net_income + rec.d_and_a + rec.capex
        if rec.ocf is not None:
            rec.fcf = rec.ocf + rec.capex
    except DataQualityError as exc:
        rec.errors.append(f"owner earnings unavailable: {exc}")
    except Exception as exc:
        rec.errors.append(f"cash flow parse failed: {type(exc).__name__}: {exc}")

    try:
        fx = fx_to_usd(rec.financial_currency or "USD")
        if _finite(rec.owner_earnings):
            rec.owner_earnings_usd = rec.owner_earnings * fx
        if _finite(rec.fcf):
            rec.fcf_usd = rec.fcf * fx
    except DataQualityError as exc:
        rec.errors.append(f"statement FX: {exc}")

    try:
        rec.gross_margins, rec.operating_margins = _margin_series(t.financials)
    except Exception as exc:
        rec.errors.append(f"margins failed: {type(exc).__name__}: {exc}")

    rec.warnings.extend(validate(rec))
    rec.peg_valid = not any("PEG" in w for w in rec.warnings) and _finite(rec.peg)
    return rec


def main(argv: list[str]) -> int:
    args = argv[1:] or ["--universe"]
    tickers = UNIVERSE if args[0] == "--universe" else args
    out, bad = {}, 0
    for tk in tickers:
        rec = fetch(tk)
        out[tk] = asdict(rec)
        flag = ""
        if rec.errors:
            flag, bad = "  ERROR", bad + 1
        elif rec.warnings:
            flag = "  WARN"
        oe = f"{rec.owner_earnings_usd/1e9:,.2f}B" if _finite(rec.owner_earnings_usd) else "n/a"
        print(f"{tk:<9} px={rec.price_usd or float('nan'):>10,.2f} USD  "
              f"ownerEarn={oe:>12}{flag}")
        for e in rec.errors:
            print(f"            ERROR: {e}")
        for wn in rec.warnings:
            print(f"            warn:  {wn}")

    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    # Merge into the existing file under a lock: the /analyse pipeline runs several
    # Researchers in parallel, and a plain overwrite left only the last ticker standing.
    path = "data/fundamentals.json"
    with open(path + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        records = {}
        if os.path.exists(path):
            with open(path) as fh:
                records = json.load(fh).get("records", {})
        records.update(out)
        payload = {"as_of": stamp, "source": "yfinance", "records": records}
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(payload, fh, indent=2, default=str)
        os.replace(tmp, path)
    print(f"\nwrote data/fundamentals.json  as_of={stamp}  "
          f"({len(tickers)} tickers, {bad} with errors)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
