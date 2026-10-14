# Equity Analysis: INSM — Insmed Incorporated
As of 2026-10-13 · Price 98.50 USD · Template rNPV · Run: `reports/runs/INSM_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**Fast Grower transitioning from clinical development to commercial scale.** Insmed's base business is anchored by Arikayce in refractory MAC lung disease (~$500M run-rate), but the company's valuation exploded following the successful Phase 3 ASPEN trial of brensocatib in non-cystic fibrosis bronchiectasis (NCFB). **Why own it:** First-in-class oral DPP1 inhibitor targeting neutrophil serine proteases in an underserved indication with >450,000 diagnosed US patients and zero approved pharmacotherapies. **What has to happen to justify today's tape:** At $98.50 USD ($21.5B market cap), the stock discounts **>$14.5B in peak annual company sales**—demanding that brensocatib become one of the top five pharmaceutical blockbusters globally across multiple unproven autoimmune indications. **What could go wrong:** Payors mandate strict step-therapy through generic airway clearance devices, capping NCFB peak sales at $2.0B–$3.0B, while ongoing trial and commercial SG&A expenses exceed $1.0B annually. Because the stock trades at nearly double our Bull case ($50.53), the risk/reward is severely asymmetric to the downside.

## 1. Executive Summary & Expected Value
- **Current Price:** $98.50 USD · **12-mo change:** -40.0% (retracing from all-time highs of $211.41).
- **Valuation Scenarios (rNPV):**
  - **Bear Case (25%):** **$14.52 USD** (-85.3% downside) — Peak sales $2.5B, 30% margin, WACC 11.0%.
  - **Base Case (55%):** **$27.36 USD** (-72.2% downside) — Peak sales $4.5B, 36% margin, WACC 10.2%.
  - **Bull Case (20%):** **$50.53 USD** (-48.7% downside) — Peak sales $7.5B, 42% margin, WACC 9.5%.
- **Probability-Weighted Expected Value:** **$28.78 USD** (Margin of Safety: **-242.2%**, Upside: **-70.8%**).
- **Reverse-DCF & Market Implication:** Today's price already discounts a **>$14.5B peak sales run-rate**, requiring brensocatib to achieve near-impossible multi-indication dominance with zero formulary or pricing resistance.
- **Portfolio Verdict:** **TRIM** (Conviction: **HIGH**). Spot price ($98.50) trades 163.2% above the Exit Above threshold ($37.42).

## 2. Business Quality (Buffett)
- **Economic Moat:** Rated **Narrow (Potential Wide)**. Regulatory exclusivity and breakthrough clinical data in NCFB establish a strong competitive moat against potential followers. Gross margins are resilient at 80%–83%.
- **Circle of Competence:** Commercial respiratory biopharma with high clinical binary risk outside the traditional core circle of competence.
- **ROIC vs WACC:** Trailing ROIC is negative due to heavy Phase 3 clinical spend (-$840.6M TTM operating loss) against a WACC hurdle rate of 10.20%.
- **Runway & Solvency:** $1.16B in cash and short-term investments against $0.58B in long-term debt provides **$580.4M in net cash ($2.66/share)**. Runway covers ~1.8–2.0 years of operations, requiring commercial cash flow inflection by 2027 to avoid further equity dilution.

## 3. GARP & Valuation Matrix
| Metric | Current / TTM | FY24 | FY25 | Peer Median (VRTX, REGN, ALNY) |
| :--- | :--- | :--- | :--- | :--- |
| EV / Sales | 18.4x | 57.5x | 34.5x | 8.5x |
| P / E (trailing / forward) | n/m / n/m | n/m | n/m | 26.0x |
| Gross Margin | 83.5% | 76.4% | 79.7% | 85.0% |
| Operating Cash Flow | -$778.9M | -$683.9M | -$935.0M | +$850M |
| PEG (or VOID + reason) | VOID: negative trailing earnings base | n/a | n/a | n/a |
| Net Cash / Share | $2.66 | $1.84 | $4.47 | $12.50 |
| ROIC vs WACC | Negative (-840M loss) | Negative | Negative | 14.5% vs 8.5% |
| Net Debt / EBITDA | Net Cash ($580M Net Cash) | Net Cash | Net Cash | Net Cash |

## 4. DCF Scenarios (rNPV)
Modeled via explicit rNPV cash flows in `02_model.py`. Terminal value is set strictly to **0.0%** post-2039 patent expiration (brensocatib composition of matter LOE). Cost of capital build incorporates 10-yr US Treasury 5.22% (FRED DGS10), biopharma beta 1.00, ERP 5.00% (WACC 10.20%).
- **Bear Case ($14.52):** Peak company sales $2.5B; strict payor prior authorizations limit NCFB adoption; TPIP fails Phase 3; operating margin 30.0%; WACC 11.00%.
- **Base Case ($27.36):** Peak company sales $4.5B; brensocatib standard-of-care in NCFB ($3.2B peak); Arikayce expands to frontline MAC ($0.8B peak); TPIP niche PAH ($0.5B); operating margin 36.0%; WACC 10.20%.
- **Bull Case ($50.53):** Peak company sales $7.5B; brensocatib achieves multi-indication blockbuster status in NCFB + CRSwNP ($5.5B peak); TPIP succeeds in PAH ($1.5B peak); operating margin 42.0%; WACC 9.50%.
- **Reverse DCF Check:** At $98.50 spot, the market price implies peak company sales exceeding $14.5B worldwide, which is unsubstantiated by underlying addressable patient epidemiology.

## 5. The Skeptic's Audit
- **Number audit:** 9 primary balance sheet and share count variables verified against SEC 10-Q Q2-26 filings; 0 failed. Spot price ($98.50), share count (218.38M), liquid investments ($1,160.3M), debt ($579.9M), and net cash ($580.4M) audited.
- **Capital Allocation Grade: C+**
  - High historical dilution: share count expanded at 15.3% CAGR over 5 years (from 98.4M in FY20 to 218.4M in 2026).
  - Accumulated deficit sits at -$4.85B. Management has achieved genuine scientific success in ASPEN, but has funded it entirely through continuous equity dilution.
- **Quality of Earnings:** TTM operating cash burn was -$778.9M. Stock-based compensation is heavy at $157.5M TTM (20.2% of cash burn).
- **Primary Downside Catalysts:**
  1. Commercial payor pushback in NCFB mandating step-therapy through generic clearance therapies.
  2. Phase 2/3 trial failures in secondary indications (CRSwNP, HS).
  3. Failure of TPIP to demonstrate superiority over Tyvaso DPI in PAH.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency & Withholding:** Quoted in USD. No dividend payments, so 30% US dividend withholding tax is not an active drag.
- **Estate Tax Exposure:** US-situs asset subject to US federal estate tax over the US$60,000 threshold (26 USC §2104).
- **Capital Gains:** Singapore's 0% capital gains tax allows tax-free execution of portfolio trims.
- **Portfolio Overlap:** Sizing must be managed aggressively given correlated biotech exposure across the book (MDGL, RVMD, PRAX, CELC, ACAD).

## 7. Sources
1. SEC EDGAR: Insmed Incorporated 10-Q Q2 2026 (accn `0001104506-26-000041`) and 10-K FY2025 (`0001104506-26-000009`).
2. New England Journal of Medicine / Company Press Release: Phase 3 ASPEN Trial of Brensocatib in Bronchiectasis (May 2024).
3. Federal Reserve Bank of St. Louis (FRED): 10-Year Treasury Constant Maturity Rate (DGS10).
4. Run Artifacts: `01_research.md`, `facts.json`, `02_model.py`, `02_quant.md`, `03_skeptic.md`.

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          98.50 USD
FAIR_VALUE:     28.78 USD
UPSIDE:         -70.8%
ENTRY_BELOW:    20.15 USD
EXIT_ABOVE:     37.42 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts >$14.5B peak sales; commercial payor friction and multi-indication attrition cap upside
DATA_WARNINGS:  2
