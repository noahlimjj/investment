# Quant Model: MDGL (Madrigal Pharmaceuticals, Inc.) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/MDGL_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._  
_Template: **rNPV (Commercial Single-Asset Biopharma: Rezdiffra in MASH)**. Data layer: `fundamentals.json` MDGL warnings: 2._

**Price basis:** $455.53 USD close on 2026-10-13. Market capitalization is **$10.52B USD** across 23.104M diluted shares outstanding (10-Q Q2-26). Net cash is **$0.510B USD ($22.07/share)** ($850M cash/investments vs $340M Hercules term loan). Enterprise Value is **$10.01B USD**.

**Tape check (RULE 0):** Spot price $455.53 USD, 12-month change +195.4% following Rezdiffra's accelerated FDA approval (March 2024) and rapid commercial launch. The stock has de-coupled from fundamental DCF value: under our rNPV model, Base Fair Value is **$239.36** and Bull is **$374.18**. Even under the Bull case ($5.2B peak sales), the current market price sits at an 18% premium. The tape and the fundamental model disagree, and **that disagreement is the core finding**: the market is pricing Rezdiffra as an undisputed monopoly blockbuster reaching >$6.5B–$7.0B peak sales with zero competitive margin erosion.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Fast Grower transitioning from Clinical to Commercial Stage**.
- **Evidence:**
  - Revenue went from $0 in FY23 to $180.1M in FY24, and reached $958.4M in FY25.
  - Diluted shares rose modestly from 18.2M (FY23) to 23.1M (FY26), reflecting discipline in using debt/royalties rather than dilutive equity at bottoms.
  - GAAP Operating Income was -$300.1M in FY25 (narrowing from -$497.9M in FY24); operating cash flow burn narrowed to -$189.6M in FY25.
  - Lynch Growth Metrics:
    - Trailing P/E: n/m (GAAP net losses).
    - Forward P/E: **47.3x** (reflecting rapid earnings inflection as Rezdiffra covers fixed SG&A/R&D overhead).
    - PEG: VOID (negative trailing earnings base).
    - Net Cash per Share: **$22.07** (covers 4.8% of current share price).
    - Balance Sheet Runway: Cash & equivalents of ~$850M vs ~$150M annual cash burn rate implies >5.0 years runway, easily carrying the company to self-funded cash generation in H1 2027.

---

## B. Product & Commercial Architecture (Rezdiffra)
- **Rezdiffra (resmetirom):** Once-daily oral THR-beta selective agonist approved for noncirrhotic MASH with moderate-to-advanced fibrosis (F2–F3).
- **First-Mover Formulary Moat:** Madrigal achieved broad commercial coverage without requiring liver biopsy for reimbursement across major US commercial payors (UnitedHealthcare, Cigna, CVS Caremark).
- **Patent Runway:** Composition of matter and formulation patents extend to **2038** (with potential Hatch-Waxman patent term extension). Terminal value post-2038 is set explicitly to **0.0%** per standard biotech rNPV discipline.

---

## C. Cost of Capital Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (FRED DGS10 as of 2026-10-13).
- Biotech Equity Beta: **1.00** (reflecting single-product regulatory/commercial risk).
- Equity Risk Premium (ERP): **5.00%**.
- WACC Build:
  - Base Case WACC: $5.22\% + (1.00 \times 5.00\%) = \mathbf{10.20\%}$.
  - Bear Case WACC: **11.00%** (incorporating financing/refinancing spread on Hercules loan).
  - Bull Case WACC: **9.50%** (reflecting rapid de-risking as cash generation turns positive).
- US Federal + State Corporate Tax Rate: **21.0%**.

---

## D. Explicit Valuation Scenarios (from `02_model.py`)

### 1. BEAR CASE: $128.54 USD (-71.8% vs $455.53)
- **Clinical/Commercial Thesis:** GLP-1/GIP agonists (tirzepatide, semaglutide) and emerging oral THR-beta/FGF21 competitors compress Rezdiffra's adoption. Peak annual sales plateau at **$2.2B** by 2030; commercial operating margin limited to **32.0%** due to aggressive rebating; WACC 11.00%.
- PV of explicit cash flows through 2038 LOE: $2.46B + Net Cash $0.510B = Equity Value $2.97B ($128.54/share). Terminal value share: **0.0%**.

### 2. BASE CASE: $239.36 USD (-47.5% vs $455.53)
- **Clinical/Commercial Thesis:** Rezdiffra establishes itself as the standard-of-care oral backbone for MASH fibrosis regression, used in combination with GLP-1s. European launch adds incremental volume from 2026. Peak annual sales reach **$3.8B** by 2031; commercial operating margin expands to **38.0%**; WACC 10.20%.
- PV of explicit cash flows through 2038 LOE: $5.02B + Net Cash $0.510B = Equity Value $5.53B ($239.36/share). Terminal value share: **0.0%**.

### 3. BULL CASE: $374.18 USD (-17.9% vs $455.53)
- **Clinical/Commercial Thesis:** Full commercial dominance; global expansion (EU, Japan) accelerates; Rezdiffra demonstrates hard clinical outcome benefits in post-marketing trials. Peak annual sales reach **$5.2B** by 2031; operating margins reach best-in-class **44.0%**; WACC 9.50%.
- PV of explicit cash flows through 2038 LOE: $8.13B + Net Cash $0.510B = Equity Value $8.64B ($374.18/share). Terminal value share: **0.0%**.

---

## E. Probability-Weighted Expected Value & Sensitivity

| Case | Peak Sales (2031) | Operating Margin | WACC | Per Share Value | Weight | Weighted Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear** | $2.2B | 32.0% | 11.0% | $128.54 | 25% | $32.14 |
| **Base** | $3.8B | 38.0% | 10.2% | $239.36 | 55% | $131.65 |
| **Bull** | $5.2B | 44.0% | 9.5% | $374.18 | 20% | $74.84 |
| **Total**| — | — | — | — | **100%** | **$238.62 USD** |

- **Probability-Weighted Expected Value:** **$238.62 USD**
- **Margin of Safety at Spot ($455.53):** **-90.9%** (Upside: **-47.6%**)
- **Entry Price (< 30% MoS):** **$167.03 USD**
- **Exit Above (> 30% Premium to EV):** **$310.21 USD**

---

## F. Reverse DCF: What Must Be True?
To justify the current market price of **$455.53 USD** ($10.52B Market Cap / $10.01B Enterprise Value):
- At a 10.2% WACC and 38% operating margin, explicit cash flows through 2038 LOE must deliver **~$6.8B to $7.0B in peak worldwide sales**.
- This requires Madrigal to treat >150,000 US patients annually at current net realized prices (~$45k/year net), capturing virtually the entire addressable diagnosed F2–F3 noncirrhotic population with zero formulary degradation or competitive erosion from big pharma competitors.
- This expectation leaves zero margin for clinical or competitive surprises.
