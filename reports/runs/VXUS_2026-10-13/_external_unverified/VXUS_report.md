# Equity Analysis: VXUS — Vanguard Total International Stock ETF
As of 2026-10-13 · Price 84.52 USD · Template FUND · Run: `reports/runs/VXUS_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
No Lynch category: this is an all-cap ex-US index ETF holding 8,755 stocks across developed and emerging markets outside the United States. **Why own it:** provides broad international market diversification with a rock-bottom 0.05% headline expense ratio. **What has to happen:** non-US corporate earnings must accelerate and narrow the valuation discount relative to US equities while overcoming heavy currency and tariff friction. **What could go wrong:** for a Singapore tax resident, holding a US-domiciled ETF holding foreign stocks causes severe structural tax drag. The US IRS withholds 30% on all distributions despite ~89% of income being non-US source, creating a permanent ~62 bp/yr drag ($1,125 per $10k over 10 years) compared to an Irish UCITS vehicle, while exposing assets exceeding US$60k to US federal estate tax.

## 1. Executive Summary & Expected Value
- **Current Price:** 84.52 USD (close 2026-10-13) · **12-mo change:** +15.35% (total return +18.30%)
- **Bear / Base / Bull (10-yr net annual return for SG holder):** 2.20% (30%) / 6.64% (50%) / 9.80% (20%)
- **Expected Value (probability-weighted):** 5.92%/yr (Base: 6.64%/yr). Margin of safety: n/a under FUND rules.
- **SBC-adjusted Expected Value:** n/a (fund).
- **Price implies:** ex-US per-share EPS growth of 2.89% to 4.5% to justify current multiple against a 5.22% risk-free rate.
- **Implied equity risk premium:** about +0.70% to +1.42% over Treasuries after withholding tax. **Thin.**
- **Structural Drag:** 61.5 bp/yr net tax leakage vs Irish UCITS ex-US exposure (30% WHT on 2.35% yield minus 9 bp TER advantage).
- **Recommendation:** TRIM (HIGH conviction on vehicle transition to VWRA / Irish UCITS)

## 2. Business Quality (Buffett)
Moat: n/a for an index fund. Look-through quality of the index: look-through ROE is 12.57% (P/B 2.3 ÷ P/E 18.3, Vanguard factsheet, 2026-06-30). **Circle of competence:** broad indexing is ideal for passive exposure, but the vehicle choice is actively destructive for a non-US resident. **Underlying concentration:** the top 10 holdings represent 15.0% of the fund. Four semiconductor and hardware manufacturers (TSMC 4.3%, Samsung 2.6%, SK Hynix 2.2%, ASML 1.7%) make up 10.8% of total assets, tying international performance heavily to the memory/foundry capex cycle.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | n/a (fund) | n/a | n/a |
| P/E (ttm / fwd) | 18.3x (factsheet) / 16.14x (yfinance) | UNKNOWN | UNKNOWN |
| P/FCF (SBC-adjusted) | n/a | n/a | n/a |
| FCF Yield / Earnings Yield | earnings yield 5.46% vs 10y UST 5.22% | UNKNOWN | UNKNOWN |
| PEG (or VOID + reason) | VOID: factsheet growth is trailing | n/a | n/a |
| Lynch ratio (g + yield) / PE | 0.82 (trailing informational only) | n/a | n/a |
| ROIC vs WACC | look-through ROE 12.57% vs CAPM 10.22% | UNKNOWN | UNKNOWN |
| Net debt / Owner earnings | n/a (fund) | n/a | n/a |

## 4. DCF Scenarios
No DCF of an index fund. Expected return modeled via 10-year Bogle decomposition (dividend yield + EPS growth + P/E re-rating − costs − withholding tax leakage) executed in `02_model.py`. Risk-free rate: 10-yr US Treasury 5.22% (FRED DGS10, 2026-10-08). Base gross dividend yield is 2.57%. In VXUS, US 30% withholding reduces the yield by 70.5 bp, netting a 61.5 bp underperformance vs holding the same sleeve in an Irish UCITS.
Reverse DCF: solving for the required index EPS growth shows today's 18.3x discounts 2.89% (buyback reinvestment at E/P) to 4.5% perpetual earnings growth to match Treasuries.
- **Bear (30%):** 2.20%/yr. Multiple de-rates to 14.0x, EPS growth slows to 2.5%, cyclical semiconductor reset.
- **Base (50%):** 6.64%/yr. Multiple steady at 18.0x, EPS growth compounds at 4.5%, net distribution yield 1.64%.
- **Bull (20%):** 9.80%/yr. Multiple expands to 20.0x, EPS growth 6.5%, global economic re-acceleration.

## 5. The Skeptic's Audit
- **Number audit:** 10 load-bearing inputs verified against SEC filings, Vanguard factsheets, and statutory tax code.
- **Structure Grade: D** (for Singapore NRA investor). The Delaware statutory trust / RIC wrapper incurs unrecoverable 30% US withholding under 26 USC §871(a)(1)(A) on non-US source corporate dividends, and creates US-situs estate exposure under 26 USC §2104(a) above US$60,000.
- **Quality of Earnings:** 16.6% exposure to Taiwan and Korea creates cyclical peak-earnings vulnerability from global hardware AI capex.
- **Bear thesis:** A combination of permanent structural tax leakage (-61.5 bp/yr) and a cyclical downturn in global tech hardware capex that compresses multiples while reducing dividend distributions.
- **Primary Downside Catalysts:**
  1. **AI hardware capex deceleration:** TSMC and memory foundries cut capital spending guidance.
  2. **Yield curve steepening:** US 10-year Treasury above 5.5% compresses non-US equity multiples below 15x.
- **Unresolved disagreements (Quant vs Skeptic):** None.

## 6. Investor Fit (Singapore resident, SGD base)
- **Tax Inefficiency:** As a Singapore resident with 0% local capital gains tax, holding VXUS forces 30% US dividend withholding and US estate tax liability.
- **Portfolio Overlap:** VWRA already contains an ex-US sleeve covering ~38.3% of its portfolio. Holding VXUS alongside VWRA overweights international equities and introduces vehicle inefficiency.
- **Substitution Strategy:**
  - Consolidating into **VWRA (IE00BK5BQT80)** eliminates US estate tax and cuts US dividend leakage.
  - If a dedicated ex-US sleeve is strictly desired, the newly launched **Vanguard FTSE All-World ex-US UCITS ETF (IE0009A5ADV9, 0.12% TER)** is Irish-domiciled and avoids US withholding and estate situs.

## 7. Sources
1. Vanguard Institutional Factsheet F3369_062026 (VXUS, as of 2026-06-30): https://institutional.vanguard.com/iippdf/pdfs/FS3369R.pdf
2. 26 USC §2104, §851, §871, §861: https://www.law.cornell.edu/uscode/text/26/2104
3. IRS Form 706-NA Instructions (Rev. 08-2025): https://www.irs.gov/pub/irs-pdf/i706na.pdf
4. Vanguard 2024 Foreign Tax Credit Worksheet: https://investor.vanguard.com/content/dam/retail/publicsite/en/documents/taxes/FTCWS_012025.pdf
5. FRED DGS10 (10-yr US Treasury 5.22%, 2026-10-08): https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
6. Yahoo Finance market data via `methodologies/fundamentals.py` (2026-10-13)
7. Run files: `reports/runs/VXUS_2026-10-13/01_research.md`, `02_quant.md`, `02_model.py`, `03_skeptic.md`

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          84.52 USD
FAIR_VALUE:     6.64
UPSIDE:         
ENTRY_BELOW:    
EXIT_ABOVE:     
CONVICTION:     HIGH
KEY_RISK:       30% US dividend withholding (61.5 bp/yr drag) and US$60k US estate-tax situs on foreign equities
DATA_WARNINGS:  1
