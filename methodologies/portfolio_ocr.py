"""IBKR portfolio screenshot parser.

Extracts tickers and position sizes from Interactive Brokers screenshots (Apple Vision OCR on
macOS, Tesseract fallback), validates the tickers with yfinance, and returns a PREVIEW. Nothing
is written to the portfolio memory until the preview is confirmed (`save_portfolio`, `--save`,
or /confirm in Telegram).

Fixes (14 Oct 2026):
  * IBKR's mobile Positions view pins the Instrument column over the left edge of the Position
    column. Fractional positions then OCR as ".1087" (VWRA, really ~3.1 shares) or as
    "NASDAQ.NMS.5925" (VXUS, ~10.6 shares). The old regex read those as 1,087 and 5,925 shares,
    and the next-line fallback stripped decimal points ("59.25" -> 5925). A position starting
    with "." is now UNKNOWN with a note, and decimals are kept.
  * The old second pass added any known ticker that appeared anywhere in the OCR text as a
    holding. Now only a line that is exactly a known symbol counts, and it is flagged.
  * The exchange regex lacked ARCA, AMEX, SEHK, IBIS and others in the suffix map.
  * The hard-coded "legacy positions" note is replaced by a computed diff against the previous
    snapshot.

    python3 methodologies/portfolio_ocr.py SCREENSHOT.png           # preview only
    python3 methodologies/portfolio_ocr.py SCREENSHOT.png --save    # preview, then save
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PORTFOLIO_JSON = DATA_DIR / "portfolio.json"
ACTIVE_RULE = PROJECT_ROOT / ".agents" / "rules" / "active_portfolio.md"
APPLE_VISION_BIN = Path(__file__).resolve().parent / "apple_vision_ocr"
TESSERACT_BIN = "/opt/homebrew/bin/tesseract"

# IBKR exchange codes -> Yahoo suffix
EXCHANGE_SUFFIX_MAP = {
    "NYSE": "", "ARCA": "", "AMEX": "", "BATS": "", "NASDAQ": "", "IEX": "",
    "LSE": ".L", "LSEETF": ".L", "LON": ".L",
    "SBF": ".PA", "PAR": ".PA", "AEB": ".AS", "AMS": ".AS", "ENEXT.BE": ".BR",
    "EBS": ".SW", "SWX": ".SW", "IBIS": ".DE", "IBIS2": ".DE", "FWB": ".DE", "FWB2": ".DE",
    "BVME": ".MI", "BM": ".MC", "VSE": ".VI",
    "TSEJ": ".T", "TYO": ".T", "SEHK": ".HK", "HKEX": ".HK", "SGX": ".SI",
    "KRX": ".KS", "KSE": ".KS", "ASX": ".AX", "TSE": ".TO",
}
_EXCH = "|".join(re.escape(e) for e in sorted(EXCHANGE_SUFFIX_MAP, key=len, reverse=True))
# 'TSM NYSE', 'VWRA LSEETF .1087', 'VXUS NASDAQ.NMS.5925', 'MDGL NASDAR.NMS' (OCR's R for Q),
# 'BRK B NYSE' (share class -> BRK-B)
PAIR_RE = re.compile(rf"^([A-Z0-9]{{1,8}})(?:\s([A-Z]))?\s+(NASDA[QR]\.[A-Z]+|{_EXCH})(?![A-Z0-9])(?P<tail>.*)$", re.I)
QTY_RE = re.compile(r"^\d{1,3}(?:,\d{3})+(?:\.\d+)?$|^\d+(?:\.\d+)?$")

STOP_WORDS = {
    "IBKR", "POS", "POSITION", "POSITIONS", "LAST", "PRICE", "AVG", "COST", "BASIS", "CHG",
    "CHANGE", "PNL", "UNRL", "REAL", "PROFIT", "LOSS", "TOTAL", "NAV", "CASH", "BALANCE",
    "ACCOUNT", "PORTFOLIO", "STOCKS", "FUNDS", "ETF", "ETFS", "EQUITY", "SECURITIES", "CURRENCY",
    "USD", "SGD", "EUR", "GBP", "JPY", "HKD", "AUD", "CAD", "CHF", "ORDERS", "TRADES", "WATCHLIST",
    "MENU", "HOME", "SEARCH", "MORE", "BUY", "SELL", "CLOSE", "OPEN", "MARKET", "LIMIT", "DAY",
    "GTC", "FINANCIAL", "INSTRUMENT", "VALUE", "MKT", "VAL", "DAILY", "RETURN", "TODAY",
    "YESTERDAY", "WEEK", "MONTH", "YEAR", "PERCENT", "SHARE", "SHARES", "QTY", "QUANTITY", "TRADE",
    "SETTINGS", "NOTIFICATIONS", "SUMMARY", "OVERVIEW", "IMPACT", "MARKETS", "BALANCES",
}
TRUNCATED_NOTE = ("position column truncated in the screenshot ('{raw}'): leading digits hidden "
                  "behind the Instrument column, so the share count is UNKNOWN. Re-send a screenshot "
                  "with the Position column fully visible (landscape, or scroll right).")


def run_ocr(image_path: Path) -> tuple[str, str]:
    """(text, engine). Apple Vision, retried once (it was SIGKILLed transiently on 14 Oct while
    another job ran), then Tesseract, which on the same screenshot read only 10 of 19 positions."""
    if APPLE_VISION_BIN.exists():
        for attempt in (1, 2):
            try:
                res = subprocess.run([str(APPLE_VISION_BIN), str(image_path)], capture_output=True,
                                     text=True, check=True, timeout=90)
                if res.stdout.strip():
                    return res.stdout, "apple-vision"
            except Exception as e:
                print(f"[ocr warning] Apple Vision OCR attempt {attempt} failed: {e}")
    tess = TESSERACT_BIN if Path(TESSERACT_BIN).exists() else "tesseract"
    res = subprocess.run([tess, str(image_path), "stdout", "--psm", "6"], capture_output=True, text=True)
    return res.stdout, "tesseract"


def parse_quantity(raw: str) -> tuple[float | None, str | None]:
    """'47' -> 47; '1,087.5' -> 1087.5; '.1087' -> (None, truncated note)."""
    s = raw.strip().lstrip("•·").strip()
    if not s:
        return None, None
    if re.fullmatch(r"\.\d+", s):
        return None, TRUNCATED_NOTE.format(raw=s)
    if QTY_RE.fullmatch(s):
        q = float(s.replace(",", ""))
        return (int(q) if q.is_integer() else q), None
    return None, None


def _known_symbols() -> dict[str, str]:
    """Base symbol -> full ticker, from the last snapshot and the pipeline run folders."""
    known = []
    try:
        known += json.loads(PORTFOLIO_JSON.read_text()).get("tickers", [])
    except (OSError, json.JSONDecodeError):
        pass
    known += [p.name.rsplit("_", 1)[0] for p in (PROJECT_ROOT / "reports" / "runs").glob("*_*") if p.is_dir()]
    return {t.split(".")[0].upper(): t for t in known}


def parse_ibkr_text(ocr_text: str) -> list[dict[str, Any]]:
    """Raw OCR text -> [{ticker, exchange, shares, shares_note}]."""
    lines = [l.strip() for l in ocr_text.splitlines() if l.strip()]
    holdings: dict[str, dict[str, Any]] = {}
    for i, line in enumerate(lines):
        m = PAIR_RE.match(line)
        if not m:
            continue
        sym = m.group(1).upper() + (f"-{m.group(2).upper()}" if m.group(2) else "")
        exch = m.group(3).upper()
        suffix = "" if exch.startswith(("NASDAQ", "NASDAR")) else EXCHANGE_SUFFIX_MAP.get(exch, "")
        ticker = f"{sym}{suffix}"
        tail = m.group("tail").split()
        shares, note = parse_quantity(tail[0] if tail else "")
        if shares is None and note is None and i + 1 < len(lines) and not PAIR_RE.match(lines[i + 1]):
            shares, note = parse_quantity(lines[i + 1])
        if shares is None and note is None:
            note = "share count not read from the screenshot"
        if ticker not in holdings and sym not in STOP_WORDS:
            holdings[ticker] = {"ticker": ticker, "exchange": exch, "shares": shares, "shares_note": note}

    # A line that is exactly a known symbol, where OCR lost the exchange token.
    found_bases = {t.split(".")[0] for t in holdings}
    for base, full in _known_symbols().items():
        if base not in found_bases and base not in STOP_WORDS and any(l.upper() == base for l in lines):
            holdings[full] = {"ticker": full, "exchange": "UNREAD", "shares": None,
                              "shares_note": "exchange and share count not read; matched a known symbol on its own line"}
    return list(holdings.values())


def validate_tickers(parsed: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    """Keep tickers yfinance can price. Returns (validated, rejected)."""
    import yfinance as yf
    from fundamentals import normalise_quote
    ok, bad = [], []
    for item in parsed:
        sym = item["ticker"]
        try:
            t = yf.Ticker(sym)
            price, ccy = normalise_quote(float(t.fast_info.last_price), t.fast_info.currency)
            if not price or price <= 0:
                raise ValueError("no price")
            try:
                name = t.info.get("shortName") or t.info.get("longName") or sym
            except Exception:
                name = sym
            ok.append({**item, "name": name, "price": round(price, 4), "currency": ccy})
        except Exception:
            bad.append(sym)
    return ok, bad


def _diff(new: list[dict[str, Any]]) -> dict[str, list[str]]:
    try:
        old = {h["ticker"]: h for h in json.loads(PORTFOLIO_JSON.read_text()).get("holdings", [])}
    except (OSError, json.JSONDecodeError):
        old = {}
    new_map = {h["ticker"]: h for h in new}
    changed = [f"{t}: {old[t].get('shares')} -> {new_map[t].get('shares')}" for t in new_map
               if t in old and old[t].get("shares") != new_map[t].get("shares")]
    return {"added": sorted(set(new_map) - set(old)), "removed": sorted(set(old) - set(new_map)),
            "changed": changed}


def parse_ibkr_screenshot(image_path: Path, save: bool = False) -> dict[str, Any]:
    """OCR + parse + validate. Returns a preview; writes the portfolio only if save=True."""
    image_path = Path(image_path)
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    text, engine = run_ocr(image_path)
    parsed = parse_ibkr_text(text)
    holdings, rejected = validate_tickers(parsed)
    warnings = [f"{h['ticker']}: {h['shares_note']}" for h in holdings if h.get("shares_note")]
    if engine != "apple-vision":
        warnings.insert(0, "Apple Vision OCR failed, so the lower-accuracy Tesseract fallback was used: "
                           "check every line, or /cancel and send the screenshot again")
    preview = {
        "as_of": datetime.now(timezone.utc).isoformat(), "source_file": image_path.name,
        "ocr_engine": engine, "total_holdings_count": len(holdings),
        "tickers": [h["ticker"] for h in holdings], "holdings": holdings, "rejected": rejected,
        "diff": _diff(holdings), "warnings": warnings,
    }
    if save:
        save_portfolio(preview, via="portfolio_ocr.py --save")
    return preview


def save_portfolio(preview: dict[str, Any], via: str = "portfolio_ocr.py --save") -> None:
    """Persist a preview to data/portfolio.json and .agents/rules/active_portfolio.md. `via` records
    how it was accepted (Telegram /confirm or the CLI), so the memory file never overstates it."""
    holdings = preview["holdings"]
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {k: preview[k] for k in ("as_of", "source_file", "total_holdings_count", "tickers", "holdings")}
    payload["confirmed_at"] = datetime.now(timezone.utc).isoformat()
    payload["confirmed_via"] = via
    PORTFOLIO_JSON.write_text(json.dumps(payload, indent=2))

    diff = preview.get("diff", {})
    lines = [
        "# Active Stock Portfolio", "",
        f"> **Last synchronized:** {preview['as_of'][:16].replace('T', ' ')} UTC from IBKR screenshot "
        f"`{preview['source_file']}` (saved via {via}).",
        f"> **Positions:** {len(holdings)}. Source of truth: `data/portfolio.json`.", "",
        f"The user's active portfolio is these {len(holdings)} tickers:", "",
        ", ".join(h["ticker"] for h in holdings) + ".", "",
        "## Holdings", "",
        "| Ticker | Name | Shares | Price at sync | Currency |", "|---|---|---|---|---|",
    ]
    for h in holdings:
        shares = "UNKNOWN (see note)" if h.get("shares") is None else f"{h['shares']:g}"
        lines.append(f"| **{h['ticker']}** | {h.get('name', '')} | {shares} | {h.get('price', 0):,.2f} | {h.get('currency', '')} |")
    notes = [f"- **{h['ticker']}**: {h['shares_note']}" for h in holdings if h.get("shares_note")]
    if notes:
        lines += ["", "## Data notes", ""] + notes
    if diff.get("removed"):
        lines += ["", f"Not in this snapshot (were in the previous one): {', '.join(diff['removed'])}. "
                      "Treat them as sold unless the user says otherwise."]
    ACTIVE_RULE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_RULE.write_text("\n".join(lines) + "\n")
    print(f"[OK] Saved {len(holdings)} holdings to {PORTFOLIO_JSON} and {ACTIVE_RULE}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse an IBKR screenshot into a portfolio preview")
    parser.add_argument("image", type=str)
    parser.add_argument("--save", action="store_true", help="write data/portfolio.json after parsing")
    args = parser.parse_args()
    res = parse_ibkr_screenshot(Path(args.image), save=args.save)
    for h in res["holdings"]:
        shares = "UNKNOWN" if h.get("shares") is None else f"{h['shares']:g}"
        print(f"  {h['ticker']:<12} {h['name'][:26]:<26} {shares:>10}  {h['price']:>12,.2f} {h['currency']}")
    for w in res["warnings"]:
        print(f"  ! {w}")
    if res["rejected"]:
        print(f"  rejected (no vendor price): {', '.join(res['rejected'])}")
    d = res["diff"]
    print(f"  diff vs saved portfolio: added {d['added'] or '-'} removed {d['removed'] or '-'} changed {d['changed'] or '-'}")
    if not args.save:
        print("\nPreview only. Re-run with --save (or /confirm in Telegram) to store it.")


if __name__ == "__main__":
    main()
