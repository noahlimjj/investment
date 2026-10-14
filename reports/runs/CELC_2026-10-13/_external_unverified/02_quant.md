# Quant Model: CELC (Celcuity Inc.) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/CELC_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._  
_Template: **rNPV (Clinical Oncology: Gedatolisib in HR+/HER2- Breast Cancer)**. Data layer: `fundamentals.json` CELC warnings: 4._

**Price basis:** $64.38 USD spot (00_inputs.json). Market capitalization is **$3.15B USD** across 48.932M diluted shares outstanding (10-Q Q2-26). Net cash is **-$0.000B USD (-$0.01/share)** ($754.0M liquid cash/investments vs $754.4M debt). Enterprise Value is **$3.15B USD**.

**Tape check (RULE 0):** Spot price $64.38 USD, 12-month change +36.8% (52-week range $46.20 to $144.98). Under our probability-weighted rNPV model, Base Fair Value is **$33.79** and Bull Fair Value is **$75.29**. The current market price trades at a 90.5% premium to the Base Case and only breaks even if the Bull Case ($3.2B peak sales) is largely achieved. The tape and fundamental valuation disagree: the market is pricing in near-flawless Phase 3 VIKTORIA-1 data and rapid multi-billion commercialization without accounting for weekly IV administration logistics competing against oral AKT inhibitors.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Pre-Revenue / Clinical-Stage Oncology Biotech**.
- **Evidence:**
  - Commercial product revenue is $0.
  - Diluted shares expanded from 10.2M (FY20) to 48.9M (FY26) as Celcuity pivoted from diagnostics to drug development by licensing gedatolisib from Pfizer.
  - TTM Operating Loss is -$208.7M; TTM Operating Cash Flow burn is -$191.7M.
  - Stockholders' equity is -$12.8M (accumulated deficit -$580.6M), making trailing ROE mathematically distorted (-1433.7%) and debt-to-equity null per data layer warnings.
  - Lynch Growth Metrics:
    - Trailing P/E: n/m (pre-revenue losses).
    - Forward P/E: n/m.
    - PEG: VOID (negative trailing earnings base).
    - Net Cash per Share: **-$0.01** (cash balances balance total debt obligations).
    - Balance Sheet Runway: Liquid cash reserves of $754.0M vs ~$190M annual cash burn provide ~3.5 years of runway, completely funding VIKTORIA-1 Phase 3 completion and commercial launch prep.

---

## B. Product & Clinical Architecture (Gedatolisib)
- **Gedatolisib (pan-PI3K and dual mTORC1/mTORC2 inhibitor):**
  - Targets endocrine-resistant HR+/HER2- metastatic breast cancer post-CDK4/6 progression.
  - Dual inhibition achieves profound pathway shutdown while avoiding the severe hyperglycemia and rash that crippled Novartis' Piqray (alpelisib).
  - Main commercial competitor: AstraZeneca's Truqap (capivasertib), an oral AKT inhibitor approved in combination with fulvestrant.
- **Pivotal Phase 3 Trial (VIKTORIA-1):**
  - Testing gedatolisib + fulvestrant ± palbociclib in both PIK3CA-mutant and wild-type cohorts.
  - Primary endpoint: Progression-free survival (PFS). Readouts anticipated in 2025/2026.
- **Terminal Value Policy:** Set strictly to **0.0%** post-2039 patent expiration per rNPV biopharma guidelines.

---

## C. Cost of Capital Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (FRED DGS10).
- Oncology Biotech Beta: **1.00**.
- Equity Risk Premium (ERP): **5.00%**.
- WACC Build:
  - Base Case WACC: $5.22\% + (1.00 \times 5.00\%) = \mathbf{10.20\%}$.
  - Bear Case WACC: **11.00%**.
  - Bull Case WACC: **9.50%**.
- Corporate Tax Rate: **21.0%**.

---

## D. Explicit Valuation Scenarios (from `02_model.py`)

### 1. BEAR CASE: $10.31 USD (-84.0% vs $64.38)
- **Clinical/Commercial Thesis:** VIKTORIA-1 shows modest PFS improvement (1.5–2 months); IV weekly infusion logistics limit adoption in community oncology compared to oral capivasertib; peak sales plateau at **$0.7B** by 2032; operating margin settles at **28.0%**; WACC 11.00%.
- PV of explicit cash flows through 2039 LOE: $0.50B + Net Cash -$0.00B = Equity Value $0.50B ($10.31/share). Terminal value share: **0.0%**.

### 2. BASE CASE: $33.79 USD (-47.5% vs $64.38)
- **Clinical/Commercial Thesis:** VIKTORIA-1 meets primary PFS endpoint in both PIK3CA-mutant and wild-type cohorts; establishes gedatolisib as preferred 2L backbone regimen; peak sales reach **$1.8B** by 2032; commercial operating margin expands to **35.0%**; WACC 10.20%.
- PV of explicit cash flows through 2039 LOE: $1.65B + Net Cash -$0.00B = Equity Value $1.65B ($33.79/share). Terminal value share: **0.0%**.

### 3. BULL CASE: $75.29 USD (+16.9% vs $64.38)
- **Clinical/Commercial Thesis:** VIKTORIA-1 demonstrates statistically significant overall survival (OS) advantage; expands into 1L combinations and prostate cancer; peak sales reach **$3.2B** by 2033; operating margin reaches **42.0%**; WACC 9.50%.
- PV of explicit cash flows through 2039 LOE: $3.68B + Net Cash -$0.00B = Equity Value $3.68B ($75.29/share). Terminal value share: **0.0%**.

---

## E. Probability-Weighted Expected Value

| Case | Peak Sales (2032/33) | Operating Margin | WACC | Per Share Value | Weight | Weighted Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear** | $0.7B | 28.0% | 11.0% | $10.31 | 30% | $3.09 |
| **Base** | $1.8B | 35.0% | 10.2% | $33.79 | 50% | $16.89 |
| **Bull** | $3.2B | 42.0% | 9.5% | $75.29 | 20% | $15.06 |
| **Total**| — | — | — | — | **100%** | **$35.04 USD** |

- **Probability-Weighted Expected Value:** **$35.04 USD**
- **Margin of Safety at Spot ($64.38):** **-83.7%** (Upside: **-45.6%**)
- **Entry Price (< 30% MoS):** **$24.53 USD**
- **Exit Above (> 30% Premium to EV):** **$45.56 USD**

---

## F. Reverse DCF: What Must Be True?
To justify the current market price of **$64.38 USD** ($3.15B Market Cap / $3.15B Enterprise Value):
- At a 10.2% WACC and 35% operating margin, explicit cash flows through 2039 LOE must generate **~$2.8B to $3.0B in peak annual sales**.
- This requires gedatolisib to capture over 60% of all 2L/3L post-CDK4/6 metastatic breast cancer patients globally, completely overcoming the clinical convenience advantage of oral agents like Truqap (capivasertib).
- The tape discounts almost entirely the Bull Case, leaving substantial downside risk if trial readouts or commercial adoption encounter real-world friction.
