# Equity Analysis: CELC — Celcuity Inc.
As of 2026-10-13 · Price 64.38 USD · Template rNPV · Run: `reports/runs/CELC_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**Pre-revenue clinical-stage oncology biotech advancing through pivotal Phase 3.** Celcuity's entire investment thesis rests on gedatolisib, a dual pan-PI3K and mTOR inhibitor licensed from Pfizer, currently evaluated in the registrational Phase 3 VIKTORIA-1 trial for post-CDK4/6 HR+/HER2- metastatic breast cancer. **Why own it:** Gedatolisib provides comprehensive pathway blockade without the debilitating hyperglycemia (>30% Grade 3/4) that impaired Novartis' Piqray (alpelisib), backed by $754.0M in liquid assets that fully fund Phase 3 readouts. **What has to happen to justify today's tape:** Spot price of $64.38 USD ($3.15B market cap / $3.15B EV) requires **~$2.8B to $3.0B in peak annual sales**, demanding that gedatolisib become the dominant second-line standard of care globally with minimal competitive loss to oral AKT inhibitors (AstraZeneca's Truqap). **What could go wrong:** Weekly intravenous (IV) infusion logistics create community oncology adoption barriers against oral tablets, or VIKTORIA-1 delivers modest PFS gains without significant overall survival (OS) advantage. With $754.4M in total debt obligations, any commercial disappointment leaves the equity severely vulnerable to restructuring.

## 1. Executive Summary & Expected Value
- **Current Price:** $64.38 USD · **12-mo change:** +36.8% (52-wk range $46.20–$144.98).
- **Valuation Scenarios (rNPV):**
  - **Bear Case (30%):** **$10.31 USD** (-84.0% downside) — Peak sales $0.7B, 28% margin, WACC 11.0%.
  - **Base Case (50%):** **$33.79 USD** (-47.5% downside) — Peak sales $1.8B, 35% margin, WACC 10.2%.
  - **Bull Case (20%):** **$75.29 USD** (+16.9% upside) — Peak sales $3.2B, 42% margin, WACC 9.5%.
- **Probability-Weighted Expected Value:** **$35.04 USD** (Margin of Safety: **-83.7%**, Upside: **-45.6%**).
- **Reverse-DCF & Market Implication:** Today's price already discounts a **~$3.0B peak sales run-rate**, pricing in near-complete commercial execution and discounting the Bull Case almost entirely.
- **Portfolio Verdict:** **TRIM** (Conviction: **HIGH**). Spot price ($64.38) trades 41.3% above the Exit Above threshold ($45.56).

## 2. Business Quality (Buffett)
- **Economic Moat:** Rated **None (Clinical Potential Only)**. As a pre-revenue biotechnology company with $0 commercial revenue, Celcuity has no established economic moat today. Exclusivity rests on formulation and composition of matter patents extending through ~2039.
- **Circle of Competence:** Single-asset Phase 3 oncology biopharma carries clinical and commercial binary risks that sit outside the core circle of competence.
- **ROIC vs WACC:** Trailing ROIC is negative due to clinical trial development costs (-$208.7M TTM operating loss) against a WACC hurdle rate of 10.20%.
- **Runway & Solvency:** $754.0M in liquid assets balances $754.4M in total debt (**net cash is -$0.3M / -$0.01/share**). The liquid balance provides ~3.5 years of cash runway, completely insulating the company from dilutive equity financing before VIKTORIA-1 data readouts.

## 3. GARP & Valuation Matrix
| Metric | Current / TTM | FY24 | FY25 | Peer Median (EXEL, INSM, BMRN) |
| :--- | :--- | :--- | :--- | :--- |
| Price / Book | n/m (distorted equity) | 1.9x | 3.2x | 3.5x |
| P / E (trailing / forward) | n/m / n/m | n/m | n/m | 24.0x |
| Commercial Revenue | $0 | $0 | $0 | $650M |
| Operating Cash Flow | -$191.7M | -$98.7M | -$153.5M | +$180M |
| PEG (or VOID + reason) | VOID: negative trailing earnings base | n/a | n/a | n/a |
| Net Cash / Share | -$0.01 | $1.27 | $2.86 | $6.50 |
| ROIC vs WACC | Negative (-208M loss) | Negative | Negative | 13.0% vs 8.5% |
| Net Debt / EBITDA | Neutral ($0.3M Net Debt) | Net Cash | Net Cash | Net Cash |

*Data Layer Audit Notes:*  
- `institutional_pct=1.1010 outside 0..1`: Reported as a vendor artifact, not factual ownership.  
- `roe=-1433.70%`: Equity base is distorted by -$580.6M accumulated deficit; ROCE/ROIC evaluated instead.  
- `debt_to_equity is MISSING (null)`: Treated as absent/null per FIX-4, never asserted as zero.  
- `owner earnings negative`: Confirmed against negative operating cash flows (-$191.7M TTM).

## 4. DCF Scenarios (rNPV)
Executed via explicit rNPV cash flows in `02_model.py`. Terminal value is set strictly to **0.0%** post-2039 patent expiration (Hatch-Waxman LOE cliff). Cost of capital build incorporates 10-yr US Treasury 5.22% (FRED DGS10), oncology beta 1.00, ERP 5.00% (WACC 10.20%).
- **Bear Case ($10.31):** Peak sales $0.7B; VIKTORIA-1 shows modest PFS (1.5–2 mo); IV infusion limits community oncology adoption against oral capivasertib; operating margin 28.0%; WACC 11.00%.
- **Base Case ($33.79):** Peak sales $1.8B; VIKTORIA-1 succeeds across mutant and WT cohorts; preferred 2L backbone regimen; operating margin 35.0%; WACC 10.20%.
- **Bull Case ($75.29):** Peak sales $3.2B; proven overall survival advantage; expansion into 1L combinations and solid tumors; operating margin 42.0%; WACC 9.50%.
- **Reverse DCF Check:** At $64.38 spot, the market price requires peak annual sales of ~$2.8B to $3.0B worldwide, an aggressive target that leaves zero room for commercial route-of-administration friction.

## 5. The Skeptic's Audit
- **Number audit:** 9 primary balance sheet, share count, and debt variables verified against SEC 10-Q Q2-26 filings; 0 failed. Spot price ($64.38), share count (48.93M), liquid investments ($754.0M), total debt ($754.4M), and net cash (-$0.3M) audited.
- **Capital Allocation Grade: C**
  - Opportunistic licensing of gedatolisib from Pfizer created substantial clinical pipeline value.
  - Dilution has been significant: shares grew from 10.2M to 48.9M over 5 years.
  - Financial leverage: Carrying $754.4M in debt on a pre-revenue asset creates structural downside vulnerability if commercial execution falls short.
- **Quality of Earnings:** TTM operating cash burn was -$191.7M. Stock-based compensation was $28.5M TTM (14.9% of cash burn).
- **Primary Downside Catalysts:**
  1. VIKTORIA-1 fails to demonstrate clinically meaningful progression-free survival extension over standard fulvestrant.
  2. Oncologists favor oral AKT inhibitors (Truqap) over weekly IV infusions in community settings.
  3. Debt debt service obligations become onerous if commercialization cash flows are delayed past 2027.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency & Withholding:** Quoted in USD. No dividend payments, so 30% US dividend withholding tax is not an active drag.
- **Estate Tax Exposure:** US-situs asset subject to US federal estate tax over the US$60,000 threshold (26 USC §2104).
- **Capital Gains:** Singapore's 0% capital gains tax allows tax-free execution of portfolio trims.
- **Portfolio Overlap:** Sizing must be reduced given correlated biotech exposure across the book (MDGL, RVMD, INSM, PRAX, ACAD).

## 7. Sources
1. SEC EDGAR: Celcuity Inc. 10-Q Q2 2026 (accn `0001193125-26-349608`) and 10-K FY2025 (`0001193125-26-068340`).
2. ClinicalTrials.gov: NCT05501886 (Phase 3 VIKTORIA-1 study of Gedatolisib in HR+/HER2- Advanced Breast Cancer).
3. Federal Reserve Bank of St. Louis (FRED): 10-Year Treasury Constant Maturity Rate (DGS10).
4. Run Artifacts: `01_research.md`, `facts.json`, `02_model.py`, `02_quant.md`, `03_skeptic.md`.

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          64.38 USD
FAIR_VALUE:     35.04 USD
UPSIDE:         -45.6%
ENTRY_BELOW:    24.53 USD
EXIT_ABOVE:     45.56 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts ~$3.0B peak sales; IV infusion logistics vs oral AKT competitors cap real-world share
DATA_WARNINGS:  4
