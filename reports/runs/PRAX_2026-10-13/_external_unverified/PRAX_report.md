# Equity Analysis: PRAX — Praxis Precision Medicines, Inc.
As of 2026-10-13 · Price 248.69 USD · Template rNPV · Run: `reports/runs/PRAX_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**Pre-revenue clinical-stage biotech transitioning to registrational Phase 3 trials.** Praxis specializes in CNS ion-channel therapeutics, with its lead asset ulixacaltamide (PRAX-944) advancing through registrational Phase 3 Essential3 trials for essential tremor (ET), alongside PRAX-628 for focal epilepsy. **Why own it:** Essential tremor afflicts ~7 million Americans with no newly approved medical therapies in five decades; PRAX-628 demonstrated 100% complete response in Phase 2a photo-paroxysmal EEG studies, supported by $757.5M in net cash ($27.11/share) and $0 funded debt ($1.1M lease obligations). **What has to happen to justify today's tape:** Spot price of $248.69 USD ($6.94B market cap) requires **>$5.5B to $6.0B in peak annual sales**, demanding 100% Phase 3 success and multi-blockbuster adoption across both tremor and epilepsy indications with zero competitive friction. **What could go wrong:** Neuroscience Phase 3 trials suffer notorious clinical attrition due to subjective endpoint variability (TETRAS scale) and high placebo rates; a clinical miss or tolerability-driven dropouts would collapse the stock toward its net cash floor. Because the tape trades above even our optimistic Bull case ($233.36), risk/reward is heavily skewed to the downside.

## 1. Executive Summary & Expected Value
- **Current Price:** $248.69 USD · **12-mo change:** +363.3% (52-wk range $52.52–$386.33).
- **Valuation Scenarios (rNPV):**
  - **Bear Case (30%):** **$47.77 USD** (-80.8% downside) — Peak sales $0.8B, 28% margin, WACC 11.0%.
  - **Base Case (50%):** **$117.96 USD** (-52.6% downside) — Peak sales $2.7B, 36% margin, WACC 10.2%.
  - **Bull Case (20%):** **$233.36 USD** (-6.2% downside) — Peak sales $5.0B, 42% margin, WACC 9.5%.
- **Probability-Weighted Expected Value:** **$119.98 USD** (Margin of Safety: **-107.3%**, Upside: **-51.8%**).
- **Reverse-DCF & Market Implication:** Today's price already discounts a **>$5.5B to $6.0B peak sales run-rate**, which prices in flawless registrational trial outcomes and immediate commercial blockbuster status.
- **Portfolio Verdict:** **TRIM** (Conviction: **HIGH**). Spot price ($248.69) trades 59.4% above the Exit Above threshold ($155.98).

## 2. Business Quality (Buffett)
- **Economic Moat:** Rated **None (Clinical Potential Only)**. As a pre-revenue drug developer with $0 commercial revenue, Praxis currently possesses no operational economic moat. Composition of matter patents extend to ~2039–2040.
- **Circle of Competence:** Clinical-stage neuroscience biopharma carries acute binary regulatory and clinical risk, placing it outside the traditional Buffett/Lynch circle of competence.
- **ROIC vs WACC:** Trailing ROIC is negative due to clinical R&D spend (-$378.2M TTM operating loss) against a WACC hurdle rate of 10.20%.
- **Runway & Solvency:** $758.6M in liquid investments against $1.1M in lease debt provides **$757.5M in net cash ($27.11/share)**. The company has ~2.5 years of operational runway, fully funding all Phase 3 readouts through late 2027 without emergency dilutive financing.

## 3. GARP & Valuation Matrix
| Metric | Current / TTM | FY24 | FY25 | Peer Median (BMRN, NBIX, ITCI) |
| :--- | :--- | :--- | :--- | :--- |
| Price / Book | 5.2x | 1.8x | 3.5x | 4.2x |
| P / E (trailing / forward) | n/m / n/m | n/m | n/m | 22.0x |
| Commercial Revenue | $0 | $0 | $0 | $850M |
| Operating Cash Flow | -$305.1M | -$182.3M | -$249.1M | +$220M |
| PEG (or VOID + reason) | VOID: negative trailing earnings base | n/a | n/a | n/a |
| Net Cash / Share | $27.11 | $15.45 | $16.13 | $8.50 |
| ROIC vs WACC | Negative (-378M loss) | Negative | Negative | 12.0% vs 8.5% |
| Net Debt / EBITDA | Net Cash ($757M Net Cash) | Net Cash | Net Cash | Net Cash |

## 4. DCF Scenarios (rNPV)
Executed via explicit rNPV cash flows in `02_model.py`. Terminal value is set strictly to **0.0%** post-2039 patent expiration (LOE cliff). Cost of capital build incorporates 10-yr US Treasury 5.22% (FRED DGS10), biopharma beta 1.00, ERP 5.00% (WACC 10.20%).
- **Bear Case ($47.77):** Peak sales $0.8B; Phase 3 ET trial mixed/narrow; PRAX-628 suffers attrition in focal epilepsy; operating margin 28.0%; WACC 11.00%.
- **Base Case ($117.96):** Peak sales $2.7B; ulixacaltamide approved in ET ($1.5B peak); PRAX-628 approved in epilepsy ($1.2B peak); operating margin 36.0%; WACC 10.20%.
- **Bull Case ($233.36):** Peak sales $5.0B; ulixacaltamide standard-of-care in ET ($2.5B peak); PRAX-628 best-in-class epilepsy blockbuster ($2.5B peak); operating margin 42.0%; WACC 9.50%.
- **Reverse DCF Check:** At $248.69 spot, the market price requires peak sales of >$5.5B–$6.0B worldwide, an unrealistic threshold for early clinical-stage CNS molecules.

## 5. The Skeptic's Audit
- **Number audit:** 9 primary balance sheet and share count variables verified against SEC 10-Q Q2-26 filings; 0 failed. Spot price ($248.69), share count (27.92M), liquid investments ($758.6M), lease debt ($1.1M), and net cash ($757.5M) audited.
- **Capital Allocation Grade: C**
  - Dilution has been significant: shares grew from 4.8M to 27.9M over 5 years (split-adjusted). Management opportunistically raised equity during clinical rallies.
  - Accumulated deficit sits at -$1.32B with $0 in commercial revenues.
  - Balance sheet carries $0 funded debt ($1.1M lease obligations), providing $27.11/share in downside cash cushion.
- **Quality of Earnings:** TTM operating cash burn was -$305.1M. Stock-based compensation was $45.8M TTM (15.0% of cash burn).
- **Primary Downside Catalysts:**
  1. Primary endpoint miss in Phase 3 Essential3 trial for ulixacaltamide in essential tremor.
  2. Loss of efficacy or narrow therapeutic index in Phase 2b focal epilepsy trials for PRAX-628.
  3. Slow enrollment and prolonged clinical trial timeline pushing cash burn beyond 2027.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency & Withholding:** Quoted in USD. No dividend payments, so 30% US dividend withholding tax is not an active drag.
- **Estate Tax Exposure:** US-situs asset subject to US federal estate tax over the US$60,000 threshold (26 USC §2104).
- **Capital Gains:** Singapore's 0% capital gains tax allows tax-free harvesting of the spectacular +363% 12-month gain.
- **Portfolio Overlap:** Sizing must be reduced given correlated biotech exposure across the book (MDGL, RVMD, INSM, CELC, ACAD).

## 7. Sources
1. SEC EDGAR: Praxis Precision Medicines 10-Q Q2 2026 (accn `0001689548-26-000083`) and 10-K FY2025 (`0001689548-26-000018`).
2. ClinicalTrials.gov: NCT05021796 (Essential1) and NCT06240273 (Essential3) for Ulixacaltamide.
3. Federal Reserve Bank of St. Louis (FRED): 10-Year Treasury Constant Maturity Rate (DGS10).
4. Run Artifacts: `01_research.md`, `facts.json`, `02_model.py`, `02_quant.md`, `03_skeptic.md`.

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          248.69 USD
FAIR_VALUE:     119.98 USD
UPSIDE:         -51.8%
ENTRY_BELOW:    83.99 USD
EXIT_ABOVE:     155.98 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts >$5.5B peak sales; CNS Phase 3 endpoint subjectivity and clinical trial attrition
DATA_WARNINGS:  2
