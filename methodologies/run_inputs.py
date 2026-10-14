"""Shared market inputs for one /analyse run -> RUN_DIR/00_inputs.json.

Why: in the Oct 2026 pilot every agent sourced its own risk-free rate. One left it UNKNOWN
(an 8% floor silently bound), one used an undated secondary quote 75bp off the OECD
series, and two agents in the same run used different US 10y prints. The orchestrator
now fetches these once; all three agents must use this file and cite it.

    python3 methodologies/run_inputs.py TICKER RUN_DIR

Sources: FRED (no API key). US 10y is daily (DGS10); other countries use the OECD
monthly long-term rate (IRLTLT01<CC>M156N), which lags by 1-2 months -- the file says so,
and the Researcher should look for a fresher dated quote if the gap matters.
"""
from __future__ import annotations

import csv
import io
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fundamentals import MINOR_UNITS, fx_to_usd, normalise_quote  # noqa: E402

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
# currency -> FRED 10y series. None = no free series; the Researcher must source it.
TEN_YEAR = {
    "USD": "DGS10", "EUR": "IRLTLT01EZM156N", "GBP": "IRLTLT01GBM156N",
    "JPY": "IRLTLT01JPM156N", "KRW": "IRLTLT01KRM156N", "CHF": "IRLTLT01CHM156N",
    "CAD": "IRLTLT01CAM156N", "AUD": "IRLTLT01AUM156N", "DKK": "IRLTLT01DKM156N",
    "SEK": "IRLTLT01SEM156N", "TWD": None, "HKD": None, "CNY": None, "SGD": None,
}
# Country series for euro members (used when the issuer's country is known).
EURO_COUNTRY = {"FR": "IRLTLT01FRM156N", "DE": "IRLTLT01DEM156N", "NL": "IRLTLT01NLM156N",
                "IT": "IRLTLT01ITM156N", "ES": "IRLTLT01ESM156N", "IE": "IRLTLT01IEM156N"}
SUFFIX_COUNTRY = {".PA": "FR", ".DE": "DE", ".AS": "NL", ".MI": "IT", ".MC": "ES", ".IR": "IE"}


def fred_latest(series: str) -> dict:
    req = urllib.request.Request(FRED.format(series), headers={"User-Agent": "value-research-script"})
    with urllib.request.urlopen(req, timeout=30) as r:
        rows = [row for row in csv.reader(io.StringIO(r.read().decode())) if len(row) == 2]
    for date_s, val in reversed(rows[1:]):
        if val not in ("", "."):
            return {"value_pct": float(val), "date": date_s, "series": series,
                    "source": FRED.format(series),
                    "frequency": "daily" if series == "DGS10" else "monthly average (OECD, lags 1-2 months)"}
    raise ValueError(f"{series}: no observations")


ECB = "https://data-api.ecb.europa.eu/service/data/{}?format=csvdata&lastNObservations=1"


def ecb_latest(key: str, frequency: str) -> dict:
    """ECB data portal: fresher than the OECD/FRED copy for euro members (pilot: FR Sep 4.44%
    from ECB vs FR Aug 4.00% from FRED, while the Quant used an undated 4.75%)."""
    url = ECB.format(key)
    req = urllib.request.Request(url, headers={"User-Agent": "value-research-script"})
    with urllib.request.urlopen(req, timeout=30) as r:
        row = next(csv.DictReader(io.StringIO(r.read().decode())))
    return {"value_pct": round(float(row["OBS_VALUE"]), 3), "date": row["TIME_PERIOD"],
            "series": key, "source": url, "frequency": frequency}


def build(ticker: str) -> dict:
    rec = {}
    path = "data/fundamentals.json"
    if os.path.exists(path):
        rec = json.load(open(path)).get("records", {}).get(ticker, {})
    quote, fin = rec.get("quote_currency") or "USD", rec.get("financial_currency") or rec.get("quote_currency") or "USD"

    rates = {}
    for ccy in dict.fromkeys([quote, fin, "USD"]):
        series = TEN_YEAR.get(ccy, None)
        if ccy == "EUR":
            cc = next((c for s, c in SUFFIX_COUNTRY.items() if ticker.upper().endswith(s)), None)
            series = EURO_COUNTRY.get(cc, series)
        cc = next((c for s, c in SUFFIX_COUNTRY.items() if ticker.upper().endswith(s)), None)
        if ccy == "EUR" and cc:
            try:
                rates[ccy] = ecb_latest(f"IRS/M.{cc}.L.L40.CI.0000.EUR.N.Z",
                                        f"monthly average, {cc} 10y (ECB convergence rate)")
                rates["EUR_AAA_daily"] = ecb_latest("YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y",
                                                    "daily, euro-area AAA 10y (reference only)")
                continue
            except Exception:
                pass  # fall back to FRED below
        try:
            rates[ccy] = fred_latest(series) if series else \
                {"value_pct": None, "note": f"no free FRED series for {ccy}: Researcher must source a dated quote"}
        except Exception as exc:  # network / series failure is recorded, never coerced
            rates[ccy] = {"value_pct": None, "error": f"{type(exc).__name__}: {exc}"}

    fx = {}
    for ccy in dict.fromkeys([quote, fin, "SGD"]):
        try:
            fx[f"{ccy}USD"] = fx_to_usd(ccy)
        except Exception as exc:
            fx[f"{ccy}USD"] = None
            fx[f"{ccy}USD_error"] = str(exc)

    close = {}
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        h = t.history(period="10d", auto_adjust=False)["Close"].dropna()
        raw, raw_ccy = float(h.iloc[-1]), None
        try:
            raw_ccy = t.fast_info.currency
        except Exception:
            pass
        # LSE history is quoted in pence (GBp) while the data layer normalises to pounds. The old
        # file stored 4194 labelled GBP next to a 41.94 GBP verdict price: a 100x mismatch.
        price, _ = normalise_quote(raw, raw_ccy or quote)
        note = f"converted from {raw_ccy}" if raw_ccy in MINOR_UNITS else None
        if raw_ccy is None and ticker.upper().endswith(".L") and quote == "GBP" and raw > 1000:
            price, note = raw / 100.0, "vendor currency unknown; assumed pence and divided by 100"
        close = {"close": round(price, 4), "date": str(h.index[-1].date())}
        if note:
            close["note"] = note
    except Exception as exc:
        close = {"error": f"{type(exc).__name__}: {exc}"}

    return {
        "ticker": ticker, "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "price": close.get("close"), "price_date": close.get("date"), "price_note": close.get("note"),
        "price_basis": "official raw close (yfinance history, auto_adjust=False), in major units of "
                       "quote_currency; use this for verdicts",
        "vendor_current_price": rec.get("price"), "quote_currency": quote, "financial_currency": fin,
        "price_as_of": rec.get("as_of"),
        "risk_free_10y": rates,
        "fx_spot_to_usd": fx,
        "equity_risk_premium_pct": 5.0,
        "discount_rate_floor": {"USD": 8.0, "other": "local 10y + 4.0"},
        "rule": "All agents use these values. If an agent believes one is wrong or stale, it says so "
                "in its output and shows the effect, but does not silently substitute another figure.",
    }


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    d = build(argv[1])
    os.makedirs(argv[2], exist_ok=True)
    out = os.path.join(argv[2], "00_inputs.json")
    with open(out, "w") as fh:
        json.dump(d, fh, indent=1)
    for ccy, r in d["risk_free_10y"].items():
        print(f"10y {ccy}: {r.get('value_pct')}  {r.get('date', '')}  {r.get('frequency', r.get('note', r.get('error', '')))}")
    print(f"FX: {d['fx_spot_to_usd']}\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
