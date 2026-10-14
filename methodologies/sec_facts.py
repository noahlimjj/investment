"""Primary-source financials from SEC EDGAR XBRL (companyfacts API).

Why this exists: yfinance is a single unaudited vendor (see METHODOLOGY_AUDIT.md). Every
number this script emits carries the filing it came from (form, accession, filed date),
so the Skeptic can trace any figure in a report back to a 10-K / 10-Q / 20-F.

Covers US-GAAP filers (10-K/10-Q) and IFRS filers that submit XBRL to EDGAR (20-F, e.g.
TSM, NVO, BABA). Companies that do not file with the SEC (RR.L, MC.PA, 7974.T, ...) are
not covered -- the script exits 3 and the Researcher must use the company's IR filings.

Rules carried over from fundamentals.py:
  * a missing tag is None, never 0
  * nothing is coerced silently; every gap is listed under "gaps"

Usage:
    python3 methodologies/sec_facts.py ZBH                       # print summary
    python3 methodologies/sec_facts.py ZBH --out path/facts.json # also write JSON
    python3 methodologies/sec_facts.py 000660.KS --sec-ticker SKHY  # dual listing: SEC ticker differs

Set SEC_USER_AGENT="<name> <email>" to identify yourself to the SEC (their fair-access
policy asks for a contact); a generic default is used otherwise.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import date, datetime, timezone

UA = os.environ.get("SEC_USER_AGENT", "value-research-script research@example.com")
YEARS = 6

# (taxonomy, tag) candidates, tried in order per period. Tags change over time
# (e.g. Revenues -> RevenueFromContractWithCustomer...), so periods are merged across them.
DURATION = {
    "revenue": [("us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"),
                ("us-gaap", "Revenues"), ("us-gaap", "SalesRevenueNet"),
                ("us-gaap", "RevenueFromContractWithCustomerIncludingAssessedTax"),
                ("ifrs-full", "Revenue")],
    "gross_profit": [("us-gaap", "GrossProfit"), ("ifrs-full", "GrossProfit")],
    "cost_of_revenue": [("us-gaap", "CostOfGoodsAndServicesSold"), ("us-gaap", "CostOfRevenue"),
                        ("us-gaap", "CostOfGoodsSold"), ("ifrs-full", "CostOfSales")],
    "operating_income": [("us-gaap", "OperatingIncomeLoss"),
                         ("ifrs-full", "ProfitLossFromOperatingActivities")],
    "pretax_income": [("us-gaap", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"),
                      ("us-gaap", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"),
                      ("ifrs-full", "ProfitLossBeforeTax")],
    "income_tax": [("us-gaap", "IncomeTaxExpenseBenefit"), ("ifrs-full", "IncomeTaxExpenseContinuingOperations")],
    "net_income": [("us-gaap", "NetIncomeLoss"), ("us-gaap", "ProfitLoss"),
                   ("ifrs-full", "ProfitLossAttributableToOwnersOfParent"), ("ifrs-full", "ProfitLoss")],
    "interest_expense": [("us-gaap", "InterestExpense"), ("us-gaap", "InterestExpenseNonoperating"),
                         ("us-gaap", "InterestExpenseDebt"), ("ifrs-full", "FinanceCosts")],
    "d_and_a": [("us-gaap", "DepreciationDepletionAndAmortization"),
                ("us-gaap", "DepreciationAmortizationAndAccretionNet"),
                ("us-gaap", "DepreciationAndAmortization"),
                ("ifrs-full", "DepreciationAndAmortisationExpense")],
    "depreciation": [("us-gaap", "Depreciation"), ("ifrs-full", "DepreciationExpense")],
    "amort_intangibles": [("us-gaap", "AmortizationOfIntangibleAssets"),
                          ("ifrs-full", "AmortisationExpense")],
    "sbc": [("us-gaap", "ShareBasedCompensation"),
            ("us-gaap", "AllocatedShareBasedCompensationExpense"),
            ("ifrs-full", "AdjustmentsForSharebasedPayments")],
    "ocf": [("us-gaap", "NetCashProvidedByUsedInOperatingActivities"),
            ("us-gaap", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"),
            ("ifrs-full", "CashFlowsFromUsedInOperatingActivities")],
    "capex": [("us-gaap", "PaymentsToAcquirePropertyPlantAndEquipment"),
              ("us-gaap", "PaymentsToAcquireProductiveAssets"),
              ("ifrs-full", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
              ("ifrs-full", "PurchaseOfPropertyPlantAndEquipment")],
    "capex_intangibles": [("us-gaap", "PaymentsToAcquireIntangibleAssets"),
                          ("us-gaap", "PaymentsToDevelopSoftware"),
                          ("ifrs-full", "PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities")],
    "investing_cf": [("us-gaap", "NetCashProvidedByUsedInInvestingActivities"),
                     ("us-gaap", "NetCashProvidedByUsedInInvestingActivitiesContinuingOperations"),
                     ("ifrs-full", "CashFlowsFromUsedInInvestingActivities")],
    "securities_bought": [("us-gaap", "PaymentsToAcquireAvailableForSaleSecuritiesDebt"),
                          ("us-gaap", "PaymentsToAcquireMarketableSecurities"),
                          ("us-gaap", "PaymentsToAcquireShortTermInvestments"),
                          ("us-gaap", "PaymentsToAcquireInvestments"),
                          ("us-gaap", "PaymentsForProceedsFromShortTermInvestments"),
                          ("us-gaap", "PaymentsForProceedsFromInvestments")],
    "securities_sold": [("us-gaap", "ProceedsFromSaleMaturityAndCollectionsOfInvestments"),
                        ("us-gaap", "ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities"),
                        ("us-gaap", "ProceedsFromSaleAndMaturityOfMarketableSecurities"),
                        ("us-gaap", "ProceedsFromSaleOfAvailableForSaleSecuritiesDebt")],
    "buybacks": [("us-gaap", "PaymentsForRepurchaseOfCommonStock"),
                 ("ifrs-full", "PaymentsToAcquireOrRedeemEntitysShares")],
    "dividends_paid": [("us-gaap", "PaymentsOfDividendsCommonStock"), ("us-gaap", "PaymentsOfDividends"),
                       ("ifrs-full", "DividendsPaidClassifiedAsFinancingActivities")],
    "acquisitions": [("us-gaap", "PaymentsToAcquireBusinessesNetOfCashAcquired"),
                     ("us-gaap", "PaymentsToAcquireBusinessTwoNetOfCashAcquired"),
                     ("us-gaap", "PaymentsToAcquireBusinessesGross"),
                     ("us-gaap", "PaymentsToAcquireBusinessesAndInterestInAffiliates"),
                     ("ifrs-full", "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities")],
    "diluted_shares": [("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"),
                       ("ifrs-full", "AdjustedWeightedAverageShares")],
    "eps_diluted": [("us-gaap", "EarningsPerShareDiluted"), ("ifrs-full", "DilutedEarningsLossPerShare")],
}
INSTANT = {
    "cash": [("us-gaap", "CashAndCashEquivalentsAtCarryingValue"),
             ("ifrs-full", "CashAndCashEquivalents")],
    "short_term_investments": [("us-gaap", "ShortTermInvestments"),
                               ("us-gaap", "MarketableSecuritiesCurrent"),
                               ("us-gaap", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"),
                               ("ifrs-full", "CurrentInvestments")],
    "debt_current": [("us-gaap", "LongTermDebtCurrent"), ("us-gaap", "DebtCurrent"),
                     ("ifrs-full", "CurrentBorrowings")],
    "debt_noncurrent": [("us-gaap", "LongTermDebtNoncurrent"), ("us-gaap", "LongTermDebt"),
                        ("ifrs-full", "NoncurrentBorrowings")],
    "equity": [("us-gaap", "StockholdersEquity"), ("ifrs-full", "EquityAttributableToOwnersOfParent")],
    "total_assets": [("us-gaap", "Assets"), ("ifrs-full", "Assets")],
    "goodwill": [("us-gaap", "Goodwill"), ("ifrs-full", "Goodwill")],
    "inventory": [("us-gaap", "InventoryNet"), ("ifrs-full", "Inventories")],
    "receivables": [("us-gaap", "AccountsReceivableNetCurrent"),
                    ("ifrs-full", "TradeAndOtherCurrentReceivables")],
    "retained_earnings": [("us-gaap", "RetainedEarningsAccumulatedDeficit"), ("ifrs-full", "RetainedEarnings")],
}
ANNUAL_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}
QUARTER_FORMS = {"10-Q", "10-Q/A", "6-K"}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def cik_for(ticker: str) -> tuple[int, str]:
    t = ticker.upper().replace(".", "-")
    for row in _get("https://www.sec.gov/files/company_tickers.json").values():
        if row["ticker"].upper() == t:
            return int(row["cik_str"]), row["title"]
    raise LookupError(f"{ticker} not found in SEC ticker map (non-SEC filer?)")


def _days(a: str, b: str) -> int:
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


def _units(facts: dict, tax: str, tag: str) -> tuple[str, list] | None:
    node = facts.get(tax, {}).get(tag)
    if not node:
        return None
    units = node["units"]
    # prefer a currency/share unit over odd ones; EPS is "<CCY>/shares"
    unit = next(iter(units))
    return unit, units[unit]


def _latest_filed(entries: list) -> dict:
    return max(entries, key=lambda e: e["filed"])


def _cite(e: dict, tax: str, tag: str, unit: str) -> dict:
    return {"val": e["val"], "start": e.get("start"), "end": e["end"], "unit": unit,
            "form": e["form"], "accn": e["accn"], "filed": e["filed"], "tag": f"{tax}:{tag}"}


def annual_series(facts: dict, cands: list, instant: bool) -> dict[str, dict]:
    """{fiscal_year_end: cited value}, merged across candidate tags, restatements -> latest filing."""
    out: dict[str, dict] = {}
    for tax, tag in cands:
        got = _units(facts, tax, tag)
        if not got:
            continue
        unit, entries = got
        by_end: dict[str, list] = {}
        for e in entries:
            if e.get("form") not in ANNUAL_FORMS:
                continue
            if not instant and not (e.get("start") and 350 <= _days(e["start"], e["end"]) <= 380):
                continue
            if instant and e.get("fp") not in (None, "FY"):
                continue
            by_end.setdefault(e["end"], []).append(e)
        for end, es in by_end.items():
            out.setdefault(end, _cite(_latest_filed(es), tax, tag, unit))
    return dict(sorted(out.items()))


def ttm(facts: dict, cands: list, fy_end: str) -> dict | None:
    """TTM = last FY + current YTD - prior-year YTD, when a 10-Q after the last FY exists."""
    for tax, tag in cands:
        got = _units(facts, tax, tag)
        if not got:
            continue
        unit, entries = got
        q = [e for e in entries if e.get("form") in QUARTER_FORMS and e.get("start")
             and e["end"] > fy_end and abs(_days(fy_end, e["start"]) - 1) <= 7]
        if not q:
            continue
        cur = max(q, key=lambda e: (e["end"], e["filed"]))
        span = _days(cur["start"], cur["end"])
        prior = [e for e in entries if e.get("start") and abs(_days(e["start"], e["end"]) - span) <= 7
                 and 358 <= _days(e["end"], cur["end"]) <= 372]
        fy = [e for e in entries if e.get("form") in ANNUAL_FORMS and e["end"] == fy_end and e.get("start")
              and 350 <= _days(e["start"], e["end"]) <= 380]
        if not prior or not fy:
            continue
        p, f = _latest_filed(prior), _latest_filed(fy)
        return {"val": f["val"] + cur["val"] - p["val"], "end": cur["end"], "unit": unit,
                "form": cur["form"], "accn": cur["accn"], "filed": cur["filed"], "tag": f"{tax}:{tag}",
                "method": f"FY{f['end']} + YTD{cur['end']} - YTD{p['end']}"}
    return None


def _v(series: dict, end: str):
    x = series.get(end)
    return None if x is None else x["val"]


def derive(years: list[str], s: dict) -> dict[str, dict]:
    """Deterministic metrics. Same formulas for Quant and Skeptic -- no re-deriving in prose."""
    out = {}
    for end in years:
        g = lambda k: _v(s[k], end)
        ni, da, capex, ocf, sbc = g("net_income"), g("d_and_a"), g("capex"), g("ocf"), g("sbc")
        # The aggregate D&A tag can carry amortisation whose cash spend sits in OCF, not capex
        # (SYK FY25: $1,570M tag vs $461M depreciation + $732M intangible amortisation; the $377M
        # gap is loaner-instrument amortisation). Adding it back without the replacement spend
        # overstates owner earnings, so use the smaller figure and say so.
        m: dict = {}
        dep, amo = g("depreciation"), g("amort_intangibles")
        if da is not None and dep is not None and amo is not None and da and abs((dep + amo) / da - 1) > 0.05:
            m["d_and_a_warning"] = (f"D&A tag {da/1e6:,.0f}M vs depreciation+intangible amortisation "
                                    f"{(dep+amo)/1e6:,.0f}M; owner earnings use the smaller")
            da = min(da, dep + amo)
        m["d_and_a_used"] = da
        rev, op, pre, tax = g("revenue"), g("operating_income"), g("pretax_income"), g("income_tax")
        cash, sti = g("cash"), g("short_term_investments")
        debt = None if g("debt_current") is None and g("debt_noncurrent") is None else \
            (g("debt_current") or 0) + (g("debt_noncurrent") or 0)
        eq = g("equity")
        # Capitalised software / intangibles are real reinvestment (ZBH: $52M of $277M in FY25).
        capex_all = None if capex is None else capex + (g("capex_intangibles") or 0)
        m["capex_total"] = capex_all
        m["fcf"] = None if ocf is None or capex_all is None else ocf - capex_all
        m["sbc_adjusted_fcf"] = None if m["fcf"] is None or sbc is None else m["fcf"] - sbc
        m["owner_earnings"] = None if None in (ni, da, capex_all) else ni + da - capex_all
        m["sbc_pct_of_ocf"] = None if not ocf or sbc is None else sbc / ocf
        gp = g("gross_profit")
        if gp is None and rev is not None and g("cost_of_revenue") is not None:
            gp = rev - g("cost_of_revenue")
        m["gross_margin"] = None if not rev or gp is None else gp / rev
        m["operating_margin"] = None if not rev or op is None else op / rev
        m["fcf_margin"] = None if not rev or m["fcf"] is None else m["fcf"] / rev
        rate = tax / pre if pre and tax is not None and pre > 0 else None
        m["effective_tax_rate"] = rate
        t = rate if rate is not None and 0 <= rate <= 0.40 else 0.21
        m["net_cash"] = None if cash is None or debt is None else cash + (sti or 0) - debt
        ic = None if eq is None or debt is None or cash is None else eq + debt - cash - (sti or 0)
        m["invested_capital"] = ic
        m["roic"] = None if op is None or not ic or ic <= 0 else op * (1 - t) / ic
        m["roic_tax_rate_used"] = t
        m["interest_coverage"] = None if op is None or not g("interest_expense") else op / g("interest_expense")
        m["debt_to_equity"] = None if debt is None or not eq or eq <= 0 else debt / eq
        out[end] = m
    # Company-specific capex lines (e.g. ZBH "Additions to instruments", $300M/yr) use
    # extension tags that companyfacts does not expose, so capex looks complete when it is
    # not. Flag investing outflows that the visible tags cannot explain.
    for end in years:
        inv, cap = _v(s["investing_cf"], end), out[end].get("capex_total")
        rev = _v(s["revenue"], end)
        if inv is None or cap is None or not rev:
            continue
        explained = cap + (_v(s["acquisitions"], end) or 0) + \
            (_v(s["securities_bought"], end) or 0) - (_v(s["securities_sold"], end) or 0)
        resid = -inv - explained
        out[end]["unexplained_investing_outflow"] = resid
        if resid > max(0.25 * cap, 0.005 * rev):
            out[end]["capex_completeness_warning"] = (
                f"{resid/1e6:,.0f}M of investing outflow not explained by capex/acquisitions/"
                "securities tags - check the filing's cash-flow statement for company-specific "
                "capex lines before using FCF")
    # Lynch: inventories growing faster than sales is a red flag
    for a, b in zip(years, years[1:]):
        ia, ib = _v(s["inventory"], a), _v(s["inventory"], b)
        ra, rb = _v(s["revenue"], a), _v(s["revenue"], b)
        if None not in (ia, ib, ra, rb) and ia and ra:
            out[b]["inventory_growth_minus_sales_growth"] = (ib / ia - 1) - (rb / ra - 1)
    return out


def cagr(first, last, n):
    if first is None or last is None or n <= 0 or first <= 0 or last <= 0:
        return None
    return (last / first) ** (1 / n) - 1


def build(ticker: str, sec_ticker: str | None = None) -> dict:
    cik, title = cik_for(sec_ticker or ticker)
    raw = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
    facts = raw["facts"]
    series = {k: annual_series(facts, c, False) for k, c in DURATION.items()}
    series |= {k: annual_series(facts, c, True) for k, c in INSTANT.items()}

    years = sorted(series["revenue"] or series["net_income"])[-YEARS:]
    gaps = [f"{k}: no data for FY ending {y}" for k, s in series.items() for y in years if y not in s]
    last = years[-1] if years else None
    stale = None
    if last and (date.today() - date.fromisoformat(last)).days > 455:
        stale = (f"STALE: latest annual XBRL period ends {last}. EDGAR has not got a newer annual "
                 "filing tagged -- pull recent periods from the company's IR filings / 6-K and cite them")

    ttm_vals = {k: ttm(facts, c, last) for k, c in DURATION.items()
                if k not in ("diluted_shares", "eps_diluted")} if last else {}
    sh = series["diluted_shares"]
    share_cagr = cagr(_v(sh, years[0]), _v(sh, years[-1]), len(years) - 1) if years else None

    dei = facts.get("dei", {}).get("EntityCommonStockSharesOutstanding", {}).get("units", {}).get("shares", [])
    so = _latest_filed(dei) if dei else None
    share_warning = None
    if so and years and _v(sh, years[-1]):
        ratio = so["val"] / _v(sh, years[-1])
        if not 0.5 <= ratio <= 2.0:
            share_warning = (f"cover-page shares {so['val']:,.0f} vs FY diluted weighted {_v(sh, years[-1]):,.0f} "
                             f"(ratio {ratio:.2f}) - issuer XBRL scale/class error likely; use the filing text")
    return {
        "ticker": ticker.upper(), "cik": cik, "entity": title, "share_count_warning": share_warning,
        "retrieved": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",
        "fiscal_year_ends": years,
        "annual": {k: {y: s[y] for y in years if y in s} for k, s in series.items()},
        "derived": derive(years, series),
        "ttm": {k: v for k, v in ttm_vals.items() if v},
        "shares_outstanding_latest": None if not so else
            {"val": so["val"], "end": so["end"], "form": so["form"], "accn": so["accn"], "filed": so["filed"]},
        "diluted_share_cagr": share_cagr,
        "revenue_cagr": cagr(_v(series["revenue"], years[0]), _v(series["revenue"], years[-1]), len(years) - 1) if years else None,
        "stale": stale,
        "gaps": gaps,
    }


def _fmt(v, pct=False):
    if v is None:
        return "—"
    if pct:
        return f"{v:6.1%}"
    return f"{v/1e6:,.0f}" if abs(v) >= 1e5 else f"{v:,.2f}"


def summary(d: dict) -> str:
    ys = d["fiscal_year_ends"]
    if not ys:
        return (f"{d['ticker']}  {d['entity']}  CIK {d['cik']}: SEC registrant, but no annual XBRL financials "
                "yet (e.g. a new ADS issuer before its first 20-F). Use the filed 6-K/F-1/424B exhibits.")
    unit = next((x["unit"] for x in d["annual"]["revenue"].values()), "?")
    lines = [f"{d['ticker']}  {d['entity']}  CIK {d['cik']}  (amounts in {unit} millions; retrieved {d['retrieved']})",
             f"{'FY end':<26}" + "".join(f"{y:>13}" for y in ys)]
    for k in ("revenue", "gross_profit", "operating_income", "net_income", "d_and_a", "sbc", "ocf",
              "capex", "buybacks", "dividends_paid", "acquisitions", "cash", "debt_noncurrent", "equity",
              "diluted_shares"):
        lines.append(f"{k:<26}" + "".join(f"{_fmt(_v(d['annual'][k], y)):>13}" for y in ys))
    lines.append("-- derived --")
    for k, pct in (("fcf", 0), ("sbc_adjusted_fcf", 0), ("owner_earnings", 0), ("net_cash", 0),
                   ("gross_margin", 1), ("operating_margin", 1), ("fcf_margin", 1), ("roic", 1),
                   ("sbc_pct_of_ocf", 1)):
        lines.append(f"{k:<26}" + "".join(f"{_fmt(d['derived'][y].get(k), pct):>13}" for y in ys))
    lines.append(f"diluted share CAGR: {_fmt(d['diluted_share_cagr'], True)}   "
                 f"revenue CAGR: {_fmt(d['revenue_cagr'], True)}")
    if d["ttm"]:
        lines.append("TTM: " + ", ".join(f"{k}={_fmt(v['val'])} (to {v['end']})" for k, v in d["ttm"].items()))
    warn = [(y, "capex may be incomplete: " + d["derived"][y]["capex_completeness_warning"]) for y in ys
            if "capex_completeness_warning" in d["derived"][y]][-2:]
    warn += [(y, "D&A basis: " + d["derived"][y]["d_and_a_warning"]) for y in ys
             if "d_and_a_warning" in d["derived"][y]][-1:]
    for y, w in warn:
        lines.append(f"!! FY{y[:4]} {w}")
    if d.get("share_count_warning"):
        lines.append("!! shares: " + d["share_count_warning"])
    if d["stale"]:
        lines.append("!! " + d["stale"])
    lines.append(f"gaps ({len(d['gaps'])}): " + ("; ".join(d["gaps"][:12]) + (" ..." if len(d["gaps"]) > 12 else "")))
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    alias = argv[argv.index("--sec-ticker") + 1] if "--sec-ticker" in argv else None
    try:
        d = build(argv[1], alias)
    except LookupError as exc:
        print(f"NOT AN SEC FILER: {exc}")
        return 3
    if "--out" in argv:
        path = argv[argv.index("--out") + 1]
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as fh:
            json.dump(d, fh, indent=1)
    print(summary(d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
