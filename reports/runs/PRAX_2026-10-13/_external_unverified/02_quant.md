# Quant Model: PRAX (Praxis Precision Medicines, Inc.) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/PRAX_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._  
_Template: **rNPV (Clinical Neuroscience: Ulixacaltamide + PRAX-628)**. Data layer: `fundamentals.json` PRAX warnings: 2._

**Price basis:** $248.69 USD spot (00_inputs.json). Market capitalization is **$6.94B USD** across 27.920M diluted shares outstanding (10-Q Q2-26). Net cash is **$0.757B USD ($27.11/share)** ($758.6M liquid cash/investments vs $1.1M lease obligations; $0 funded bank/convertible debt). Enterprise Value is **$6.19B USD**.

**Tape check (RULE 0):** Spot price $248.69 USD, 12-month change +363.3% (surging from 52-week lows of $52.52 following the Essential1 Phase 2b data and PRAX-628 PPR trial results). Under our probability-weighted rNPV model, Base Fair Value is **$117.96** and Bull Fair Value is **$233.36**. Even under our optimistic Bull case ($5.0B peak global sales), the current market price trades at a premium. The tape and fundamental clinical probabilities disagree: the market has capitalized a speculative best-case scenario with zero discount for Phase 3 clinical trial failure or neurology commercialization headwinds.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Pre-Revenue / Clinical-Stage Biotech (Transitioning to Commercial)**.
- **Evidence:**
  - Commercial revenue is $0. The company is clinical-stage.
  - Diluted shares rose from 4.8M (FY20) to 27.9M (FY26) (split-adjusted), reflecting continuous equity issuance to finance clinical operations.
  - TTM Operating Loss is -$378.2M; TTM Operating Cash Flow burn is -$305.1M.
  - Lynch Growth Metrics:
    - Trailing P/E: n/m (pre-revenue losses).
    - Forward P/E: n/m.
    - PEG: VOID (negative trailing earnings base).
    - Net Cash per Share: **$27.11** (covers 10.9% of current share price).
    - Balance Sheet Runway: Liquid cash reserves of $758.6M vs ~$300M annual cash burn provide ~2.5 years of runway, comfortably funding operations through pivotal Phase 3 readouts.

---

## B. Product & Clinical Architecture
- **Ulixacaltamide (PRAX-944):** T-type calcium channel blocker in registrational Phase 3 Essential3 study for essential tremor (ET). ET affects ~7M US individuals with zero new approved therapies in 50 years. First-in-class potential.
- **PRAX-628:** Functionally selective Nav channel blocker for focal epilepsy. Demonstrated 100% complete response in Phase 2a photo-paroxysmal response (PPR) proof-of-concept.
- **Relutrigine (PRAX-562):** Nav blocker in Phase 2 for SCN2A/SCN8A developmental epileptic encephalopathies.
- **Terminal Value Policy:** Set strictly to **0.0%** post-2039 patent expiration per rNPV biopharma methodology.

---

## C. Cost of Capital Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (FRED DGS10).
- Neuroscience Biotech Beta: **1.00**.
- Equity Risk Premium (ERP): **5.00%**.
- WACC Build:
  - Base Case WACC: $5.22\% + (1.00 \times 5.00\%) = \mathbf{10.20\%}$.
  - Bear Case WACC: **11.00%**.
  - Bull Case WACC: **9.50%**.
- Corporate Tax Rate: **21.0%**.

---

## D. Explicit Valuation Scenarios (from `02_model.py`)

### 1. BEAR CASE: $47.77 USD (-80.8% vs $248.69)
- **Clinical/Commercial Thesis:** Ulixacaltamide Phase 3 misses secondary endpoints; tolerability concerns (dizziness/fatigue) limit adoption; PRAX-628 Phase 3 suffers safety/efficacy attrition in broader focal epilepsy. Peak sales reach **$0.8B** by 2032; operating margin settles at **28.0%**; WACC 11.00%.
- PV of explicit cash flows through 2039 LOE: $0.58B + Net Cash $0.757B = Equity Value $1.33B ($47.77/share). Terminal value share: **0.0%**.

### 2. BASE CASE: $117.96 USD (-52.6% vs $248.69)
- **Clinical/Commercial Thesis:** Ulixacaltamide succeeds in Phase 3 and achieves approval in essential tremor ($1.5B peak); PRAX-628 demonstrates strong anti-seizure efficacy and gains approval in refractory focal epilepsy ($1.2B peak). Peak company sales reach **$2.7B** by 2033; commercial operating margin expands to **36.0%**; WACC 10.20%.
- PV of explicit cash flows through 2039 LOE: $2.54B + Net Cash $0.757B = Equity Value $3.29B ($117.96/share). Terminal value share: **0.0%**.

### 3. BULL CASE: $233.36 USD (-6.2% vs $248.69)
- **Clinical/Commercial Thesis:** Ulixacaltamide becomes standard-of-care across US/EU in essential tremor ($2.5B peak); PRAX-628 achieves best-in-class multi-billion status in epilepsy ($2.5B peak). Total peak sales reach **$5.0B**; operating margin expands to **42.0%**; WACC 9.50%.
- PV of explicit cash flows through 2039 LOE: $5.76B + Net Cash $0.757B = Equity Value $6.51B ($233.36/share). Terminal value share: **0.0%**.

---

## E. Probability-Weighted Expected Value

| Case | Peak Sales (2032/33) | Operating Margin | WACC | Per Share Value | Weight | Weighted Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear** | $0.8B | 28.0% | 11.0% | $47.77 | 30% | $14.33 |
| **Base** | $2.7B | 36.0% | 10.2% | $117.96 | 50% | $58.98 |
| **Bull** | $5.0B | 42.0% | 9.5% | $233.36 | 20% | $46.67 |
| **Total**| — | — | — | — | **100%** | **$119.98 USD** |

- **Probability-Weighted Expected Value:** **$119.98 USD**
- **Margin of Safety at Spot ($248.69):** **-107.3%** (Upside: **-51.8%**)
- **Entry Price (< 30% MoS):** **$83.99 USD**
- **Exit Above (> 30% Premium to EV):** **$155.98 USD**

---

## F. Reverse DCF: What Must Be True?
To justify the current market price of **$248.69 USD** ($6.94B Market Cap / $6.19B Enterprise Value):
- At a 10.2% WACC and 36% operating margin, explicit cash flows through 2039 LOE must generate **>$5.5B to $6.0B in peak annual sales**.
- This requires 100% Phase 3 registrational success across both ulixacaltamide and PRAX-628, followed by rapid multi-billion commercialization in two highly competitive CNS indications with zero commercial friction.
- The tape leaves zero room for regulatory delay, clinical endpoint ambiguity, or generic antiepileptic pricing pressure.
