# Equity Analysis: MDGL — Madrigal Pharmaceuticals, Inc.
As of 2026-10-13 · Price 455.53 USD · Template rNPV · Run: `reports/runs/MDGL_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**Fast Grower transitioning to commercial maturity.** Madrigal successfully navigated the first-ever FDA approval in noncirrhotic MASH (Rezdiffra / resmetirom), growing revenue from $0 to $958.4M in FY25. **Why own it:** First-mover advantage in liver fibrosis without mandatory liver biopsy requirements on commercial formularies, backed by pristine ~95% gross margins and a solid balance sheet ($510M net cash). **What has to happen to justify today's tape:** Spot price of $455.53 USD ($10.5B market cap) requires Rezdiffra to become an undisputed monopoly blockbuster achieving **~$6.8B to $7.0B in peak annual sales** with 38%+ operating margins through its 2038 patent cliff. **What could go wrong:** Next-generation GLP-1/GIP co-agonists (tirzepatide, CagriSema) and rival THR-beta/FGF21 therapies trigger aggressive formulary rebating, capping peak sales at $2.2B–$3.8B. Because the stock trades at an 18% premium even to our optimistic Bull case ($374.18), the risk/reward is severely skewed to the downside.

## 1. Executive Summary & Expected Value
- **Current Price:** $455.53 USD · **12-mo change:** +195.4% (52-wk range $148.20–$482.50).
- **Valuation Scenarios (rNPV):**
  - **Bear Case (25%):** **$128.54 USD** (-71.8% downside) — Peak sales $2.2B, 32% margin, WACC 11.0%.
  - **Base Case (55%):** **$239.36 USD** (-47.5% downside) — Peak sales $3.8B, 38% margin, WACC 10.2%.
  - **Bull Case (20%):** **$374.18 USD** (-17.9% downside) — Peak sales $5.2B, 44% margin, WACC 9.5%.
- **Probability-Weighted Expected Value:** **$238.62 USD** (Margin of Safety: **-90.9%**, Upside: **-47.6%**).
- **Reverse-DCF & Market Implication:** Today's price already discounts a **~$7.0B peak sales run-rate**, or >150,000 active US patients at current net realized prices. This leaves zero buffer for competitive pricing concessions or real-world compliance drop-offs.
- **Portfolio Verdict:** **TRIM** (Conviction: **HIGH**). Spot price ($455.53) sits 46.8% above the Exit Above threshold ($310.21).

## 2. Business Quality (Buffett)
- **Economic Moat:** Rated **Narrow (Transitioning to Wide pending EU approval)**. Madrigal holds first-in-class exclusivity in moderate-to-advanced MASH fibrosis (F2–F3). High gross margins (94%–96%) and formulary lock-in create high switching costs for existing stabilized patients.
- **Circle of Competence:** Single-asset commercial biotech carries elevated concentration risk. Long-term commercial durability depends on hepatology prescription habits and payor tier management.
- **ROIC vs WACC:** Trailing ROIC is negative due to commercial launch costs, inflecting toward >25% at scale by 2028 vs a WACC hurdle of 10.20%.
- **Runway & Solvency:** $850M cash and investments vs $340M Hercules term loan gives **$510M in net cash ($22.07/share)**, providing over 4 years of operational runway and ensuring commercial break-even in H1 2027 without secondary equity dilution.

## 3. GARP & Valuation Matrix
| Metric | Current / TTM | FY24 | FY25 | Peer Median (VRTX, BMRN, ALNY) |
| :--- | :--- | :--- | :--- | :--- |
| EV / Sales | 10.4x | 55.6x | 10.4x | 7.5x |
| P / E (trailing / forward) | n/m / 47.3x | n/m | n/m | 24.5x |
| Gross Margin | 96.5% | 94.1% | 96.5% | 88.0% |
| Operating Cash Flow | -$189.6M | -$455.6M | -$189.6M | +$450M |
| PEG (or VOID + reason) | VOID: negative trailing earnings base | n/a | n/a | n/a |
| Net Cash / Share | $22.07 | $4.80 | $8.71 | $14.20 |
| ROIC vs WACC | Negative inflecting | Negative | Negative | 16.0% vs 9.0% |
| Net Debt / EBITDA | Net Cash ($510M Net Cash) | Net Cash | Net Cash | Net Cash |

## 4. DCF Scenarios (rNPV)
Valuation executed via explicit rNPV modeling in `02_model.py`. Terminal value is set to **0.0%** post-2038 patent expiry (Hatch-Waxman LOE cliff). Cost of capital build uses 10-yr US Treasury 5.22% (FRED DGS10), biotech beta 1.00, ERP 5.00% (WACC 10.20%).
- **Bear Case ($128.54):** Peak sales $2.2B by 2030; payor step-therapy requires failed GLP-1 trial; operating margin 32.0%; WACC 11.00%.
- **Base Case ($239.36):** Peak sales $3.8B by 2031; oral backbone standard-of-care alongside GLP-1s; operating margin 38.0%; WACC 10.20%.
- **Bull Case ($374.18):** Peak sales $5.2B by 2031; global EU/Japan expansion; operating margin 44.0%; WACC 9.50%.
- **Reverse DCF Check:** At $455.53 spot, the market price requires ~$7.0B peak sales, a 18% 10-year sales CAGR from FY25, and flawless commercial execution.

## 5. The Skeptic's Audit
- **Number audit:** 9 core balance sheet and cash flow parameters audited against SEC 10-Q Q2-26 filings; 0 failed. Spot price, share count (23.104M), net cash ($510.0M), and WACC inputs fully validated.
- **Capital Allocation Grade: B**
  - Dilution over 5 years restricted to ~28% cumulative through prudent use of structured term debt.
  - Market value created per dollar of accumulated deficit stands at +4.8x ($2.1B deficit vs $10.5B market capitalization).
- **Quality of Earnings:** Free cash flow burn is rapidly narrowing (-$189.6M in FY25 vs -$455.6M in FY24). SBC represents ~$42M (4.4% of sales), an acceptable level for commercial biopharma.
- **Primary Downside Catalysts:**
  1. Novo Nordisk / Eli Lilly MASH phase 3 readouts establishing superior metabolic fibrosis prevention.
  2. Commercial payor formulary renegotiations forcing net price cuts below $30,000/patient/year.
  3. Real-world GI discontinuation rates exceeding 25%.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency & Withholding:** Quoted in USD. Madrigal does not pay dividends, so US 30% dividend withholding tax is not an active drag.
- **Estate Tax Exposure:** US-situs asset subject to US federal estate tax over the US$60,000 non-resident threshold (26 USC §2104).
- **Capital Gains:** 0% Singapore capital gains tax enables a completely frictionless tax-free harvest of the +195% gain over the trailing 12 months.
- **Portfolio Overlap:** Sizing should be reduced given overlapping biotech exposure in the portfolio (RVMD, INSM, PRAX, CELC, ACAD).

## 7. Sources
1. SEC EDGAR: Madrigal Pharmaceuticals 10-Q Q2 2026 (accn `0001628280-26-050845`) and 10-K FY2025 (`0001628280-26-015822`).
2. FDA Approval Package: Rezdiffra (resmetirom) NDA 217785 (March 14, 2024).
3. Federal Reserve Bank of St. Louis (FRED): 10-Year Treasury Constant Maturity Rate (DGS10).
4. Run Artifacts: `01_research.md`, `facts.json`, `02_model.py`, `02_quant.md`, `03_skeptic.md`.

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          455.53 USD
FAIR_VALUE:     238.62 USD
UPSIDE:         -47.6%
ENTRY_BELOW:    167.03 USD
EXIT_ABOVE:     310.21 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts ~$7B peak sales; GLP-1 and rival THR-beta competition cap durability
DATA_WARNINGS:  2
