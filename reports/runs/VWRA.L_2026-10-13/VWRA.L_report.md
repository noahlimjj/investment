# Equity Analysis: VWRA.L — Vanguard FTSE All-World UCITS ETF (USD Acc)
As of 2026-10-13 · Price 193.34 USD · Template FUND · Run: `reports/runs/VWRA.L_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
No Lynch category: this is an index fund, not a company. **Why own it:** it's a cheap, tax-efficient way for a Singapore resident to own about 3,800 global stocks. Fees are 0.14%, US dividends are taxed at 15% inside the fund, and the fund is not counted for US estate tax. **What has to happen:** global per-share earnings have to compound at roughly 4% or more a year for it to beat a 10-year Treasury, and at about 8% for a normal equity premium. **What could go wrong:** you're buying a 62%-US, AI-heavy index at 21x earnings. Its earnings yield (4.76%) is below the 5.22% Treasury yield, so a decade that only matches bonds is plausible without any recession.

## 1. Executive Summary & Expected Value
- **Current Price:** 193.34 USD (LSE close 2026-10-13) · **12-mo change:** +18.1% (3-yr +81.0%)
- **Bear / Base / Bull (10-yr net annual return):** 0.72% (25%) / 6.30% (55%) / 10.25% (20%)
- **Expected Value (probability-weighted):** 6.13%/yr. Margin of safety: n/a under the FUND rules. For reference, it's −46% at a 10.22% CAPM hurdle and +8.2% at bond parity.
- **SBC-adjusted Expected Value:** n/a (fund). If the index P/E uses operating EPS that excludes SBC, the true P/E is higher and the bear case drops to about −0.3%/yr.
- **Price implies:** index per-share EPS growth of 3.92%/yr at a constant 21x just to match the 5.22% 10-yr Treasury, and 7.92%/yr to earn Treasury + 4%. That 7.92% is ambitious from above-trend margins (CAPE/PE 1.25–1.39x).
- **Implied equity risk premium:** about +0.9–1.1% over Treasuries. **Thin.**
- **Asymmetry:** n/a (fund).
- **Recommendation:** HOLD as core (MEDIUM conviction)

## 2. Business Quality (Buffett)
Moat: n/a for a fund. The quality of the underlying index looks high: look-through ROE is 17.1% (P/B 3.6 ÷ P/E 21.0, Vanguard, 31 Aug 2026). **Circle of competence:** a broad index is the textbook "know-nothing investor" holding Buffett recommends. The real question is price, not understanding. **Diversification is narrower than it looks:** the top 10 holdings are 23.6% of the fund. AI-semiconductor suppliers (NVIDIA, TSMC, Broadcom, Micron) are 9.1%, and the hyperscalers who buy from them are 10.3%. About a fifth of the index rests on one capex cycle.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | n/a (fund) | n/a | n/a |
| P/E (ttm / fwd) | 21.0x (Vanguard) / UNKNOWN (MSCI ACWI proxy 23.2x / 17.1x; vendor definitions differ) | UNKNOWN | UNKNOWN |
| P/FCF (SBC-adjusted) | n/a | n/a | n/a |
| FCF Yield / Earnings Yield | earnings yield 4.76% vs 10y UST 5.22% | UNKNOWN | UNKNOWN |
| PEG (or VOID + reason) | VOID: no sourced index growth input | n/a | n/a |
| Lynch ratio (g + yield) / PE | n/a (fund) | n/a | n/a |
| ROIC vs WACC | look-through ROE 17.1% vs CAPM 10.22% | UNKNOWN | UNKNOWN |
| TER / tracking error | 0.14% / 0.07% (1y), 0.08% (5y) | — | peer TER and tracking difference UNKNOWN |

## 4. DCF Scenarios
No DCF of a fund. Instead, a 10-yr return decomposition (dividend yield + EPS growth + P/E change − costs and withholding), run in `02_model.py` and re-run with the sourced risk-free rate in `03_rerun.py`. Risk-free rate: 10-yr US Treasury 5.22% (FRED DGS10, 2026-10-08). The CAPM discount rate is 10.22%; terminal growth is capped at 4%. Reverse DCF: the perpetual model says today's 21x already discounts about 4.3% growth forever at an 8% required return. The biggest single driver is the exit P/E: going from 21x to 19x moves the base from 6.30% to 5.26%/yr.
- **Bear (25%):** 0.72%/yr. EPS growth 3%, de-rating to 15x, dividend yield 1.40%. A lost decade like 2000–09 (high starting valuation).
- **Base (55%):** 6.30%/yr. EPS growth 5%, no re-rating at 21x, dividend yield 1.59%.
- **Bull (20%):** 10.25%/yr. EPS growth 7.5%, re-rating to 24x.

## 5. The Skeptic's Audit
- **Number audit:** 18 checked, 2 failed, 2 minor flags. (1) The risk-free rate was UNKNOWN, so the 8% floor was binding. Sourced at 5.22%, which raises the CAPM hurdle to 10.22% and drops every hurdle-dependent value by 18–36%. The base return is unchanged. (2) The Quant's top-ranked sensitivity test was mis-specified: exit P/E, not starting P/E, is the real driver. Flags: the dividend yield is borrowed from MSCI (Vanguard shows an unlabeled 1.32%, −0.24 pp), and the withholding-drag formula is rough (±0.1 pp).
- **Structure Grade: A** (provisional; replaces the capital-allocation grade for a fund). TER is 0.14% (Vanguard). The 15% US dividend withholding **is verified from primary sources**: US–Ireland treaty Art. 10(2)(b), Art. 4(1)(d), and the limitation-on-benefits test in Art. 23(2)(d)(i). It is **not US-situs for estate tax**: 26 USC §2104(a) counts only stock "issued by a domestic corporation", and VWRA's issuer is an Irish PLC. It's provisional only because peer TER and tracking difference were not sourced.
- **Quality of Earnings:** index EPS looks cyclically flattered. Hyperscaler capex far exceeds depreciation (future depreciation drag), and AI suppliers are booking that capex as revenue at possibly peak margins. A 10% earnings reset cuts the base to 5.20%/yr.
- **Bear thesis:** a valuation and discount-rate squeeze on a market whose earnings are increasingly one trade. A 10% earnings normalisation plus a de-rating to 19x gives 4.17%/yr, below today's Treasury yield.
- **Primary Downside Catalysts:**
  1. **AI-capex rollover.** Signpost: combined MSFT/AMZN/GOOGL/META capex guidance falls for two straight quarters, or NVIDIA revenue falls year on year.
  2. **Rate squeeze.** Signpost: the 10-yr Treasury holds above 5.5% for 3 months while index P/E stays at 20x or above, or index P/E prints below 18x.
- **Unresolved disagreements (Quant vs Skeptic):**

| Issue | Quant | Skeptic | Effect |
|---|---|---|---|
| Discount rate | 8% floor (rate UNKNOWN) | 10.22% (rate sourced) | **Corrected.** Base return unchanged; hurdle values down 18–36% |
| Base exit P/E 21x | neutral | generous with Treasuries above the earnings yield; justified 12.8–15.3x | 19x exit → 5.26%/yr (−16.5% of fair value); held in the bear weight, not the base |
| Earnings above trend | open | yes, partial reset likely | 10% reset → 5.20%/yr; in the bear weight |

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-quoted, global look-through; USD/SGD drift is UNKNOWN (±1%/yr moves the 10-yr outcome by about ±10%).
- **Dividends:** accumulating, so there is no distribution event for you. US dividends are taxed at 15% inside the fund (verified), against 30% if you held US-domiciled funds directly.
- **Estate tax:** not US-situs (verified).
- **Overlap:** you also hold TSM, SK Hynix and SK Square directly, so semiconductors stack on top of the fund's 9.1% AI-supplier weight. Look-through totals are UNKNOWN until position sizes are known.
- **The actionable finding is elsewhere:** **VXUS (and VOO, if still held) are US-situs and carry 30% US withholding.** VWRA already covers VXUS's ex-US exposure in a better wrapper. Any TRIM in your book belongs on VXUS/VOO, not VWRA.

## 7. Sources
1. Vanguard UK product page, VWRA (TER, holdings, weights, P/E 21.0x, P/B 3.6x, as of 31 Aug 2026): https://www.vanguard.co.uk/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating
2. FRED DGS10 (10-yr US Treasury 5.22%, 2026-10-08): https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
3. US–Ireland income tax treaty: https://www.irs.gov/pub/irs-trty/ireland.pdf
4. 26 USC §2104: https://www.law.cornell.edu/uscode/text/26/2104 · IRS nonresident estate tax page: https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
5. justETF profile (sector weights, cross-check): https://www.justetf.com/en/etf-profile.html?isin=IE00BK5BQT80
6. MSCI ACWI index page (proxy valuation, 31 Jul 2026): https://www.msci.com/indexes/index/892400/msci-acwi-index · Siblis global CAPE (proxy): https://siblisresearch.com/data/world-cape-ratio/
7. yfinance price history via `methodologies/fundamentals.py` (data/fundamentals.json, 2026-10-13)
8. Run files: `01_research.md`, `02_quant.md`, `02_model.py`, `03_skeptic.md`, `03_rerun.py`

VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          193.34 USD
FAIR_VALUE:     6.30%/yr base 10-yr net return (probability-weighted 6.13%/yr)
UPSIDE:         n/a (FUND)
ENTRY_BELOW:    n/a
EXIT_ABOVE:     n/a
CONVICTION:     MEDIUM
KEY_RISK:       Implied equity premium ~1% over a 5.22% 10y Treasury on a 62%-US, AI-concentrated index at 21x
DATA_WARNINGS:  1
