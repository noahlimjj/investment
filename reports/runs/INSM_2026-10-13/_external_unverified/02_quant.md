# Quant Model: INSM (Insmed Incorporated) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/INSM_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._  
_Template: **rNPV (Commercial Biopharma: Arikayce + Brensocatib + TPIP)**. Data layer: `fundamentals.json` INSM warnings: 2._

**Price basis:** $98.50 USD spot (00_inputs.json). Market capitalization is **$21.51B USD** across 218.380M diluted shares outstanding (10-Q Q2-26). Net cash is **$0.580B USD ($2.66/share)** ($1.160B liquid cash/investments vs $0.580B total debt). Enterprise Value is **$20.93B USD**.

**Tape check (RULE 0):** Spot price $98.50 USD, 12-month change -40.0% (retracing from an all-time high of $211.41 following the euphoria of the Phase 3 ASPEN data readout in mid-2024). Under our probability-weighted rNPV model, Base Fair Value is **$27.36** and Bull Fair Value is **$50.53**. Even under the Bull case ($7.5B peak company sales), the current market price sits at nearly double intrinsic value (+95.0% premium). The tape and fundamental valuation disagree sharply: the market is pricing Insmed as if brensocatib will achieve >$14.5B in peak sales across multiple unproven indications with zero competitive friction.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Fast Grower transitioning from Clinical to Commercial Scale**.
- **Evidence:**
  - Revenue expanded from $164.4M (FY20) to $606.4M (FY25), and reached $1,137.6M on a TTM basis (10-Q Q2-26).
  - Diluted shares rose from 98.4M (FY20) to 218.4M (FY26), a 15.3% CAGR, reflecting substantial equity dilution to fund Phase 3 trials and pre-launch commercial prep.
  - TTM Operating Loss stands at -$840.6M; TTM Operating Cash Flow burn is -$778.9M.
  - Lynch Growth Metrics:
    - Trailing GAAP P/E: n/m (GAAP net losses).
    - Forward P/E: n/m (heavy ongoing pre-launch commercial build-out).
    - PEG: VOID (negative trailing earnings base).
    - Net Cash per Share: **$2.66** (covers 2.7% of current share price).
    - Liquidity Runway: Liquid reserves of $1.16B against ~$600M annual cash burn provide ~1.8–2.0 years of runway before brensocatib commercial launch cash flows materialize.

---

## B. Commercial Franchise Architecture
- **Arikayce (liposomal amikacin):** Generating ~$450M–$500M baseline in refractory MAC lung disease. Exclusivity extends to 2033. Frontline Phase 3 ARISE and ENCORE trials offer modest label expansion.
- **Brensocatib (DPP1 inhibitor):** Landmark Phase 3 ASPEN trial met primary endpoints in non-cystic fibrosis bronchiectasis (NCFB), reducing pulmonary exacerbations by 20%–25% (p<0.01). Commercial launch targeted for 2025/2026. Composition of matter patent exclusivity extends to ~2039.
- **TPIP (inhaled treprostinil palmitil):** Phase 2 prostanoid in PAH and PH-ILD, offering potential convenient once-daily dry powder dosing.
- **Terminal Value Policy:** Set strictly to **0.0%** post-2039 patent expiration per rNPV biopharma guidelines.

---

## C. Cost of Capital Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (FRED DGS10).
- Biopharma Equity Beta: **1.00**.
- Equity Risk Premium (ERP): **5.00%**.
- WACC Build:
  - Base Case WACC: $5.22\% + (1.00 \times 5.00\%) = \mathbf{10.20\%}$.
  - Bear Case WACC: **11.00%**.
  - Bull Case WACC: **9.50%**.
- Corporate Tax Rate: **21.0%**.

---

## D. Explicit Valuation Scenarios (from `02_model.py`)

### 1. BEAR CASE: $14.52 USD (-85.3% vs $98.50)
- **Clinical/Commercial Thesis:** Brensocatib approval is restricted by payors to severe, hospital-exacerbating patients (strict prior auth); physician uptake is sluggish; TPIP fails Phase 3. Peak company sales reach **$2.5B** by 2030; commercial operating margin settles at **30.0%**; WACC 11.00%.
- PV of explicit cash flows through 2039 LOE: $2.59B + Net Cash $0.580B = Equity Value $3.17B ($14.52/share). Terminal value share: **0.0%**.

### 2. BASE CASE: $27.36 USD (-72.2% vs $98.50)
- **Clinical/Commercial Thesis:** Brensocatib becomes standard-of-care in NCFB ($3.2B peak); Arikayce expands into frontline MAC ($0.8B peak); TPIP contributes niche PAH revenue ($0.5B peak). Peak company sales reach **$4.5B** by 2031; commercial operating margin expands to **36.0%**; WACC 10.20%.
- PV of explicit cash flows through 2039 LOE: $5.39B + Net Cash $0.580B = Equity Value $5.97B ($27.36/share). Terminal value share: **0.0%**.

### 3. BULL CASE: $50.53 USD (-48.7% vs $98.50)
- **Clinical/Commercial Thesis:** Brensocatib becomes a multi-indication blockbuster in NCFB and CRSwNP ($5.5B peak); TPIP displaces Tyvaso in PAH ($1.5B peak); Arikayce sustains through 2033 ($0.8B peak). Peak company sales reach **$7.5B** by 2032; operating margin reaches **42.0%**; WACC 9.50%.
- PV of explicit cash flows through 2039 LOE: $10.45B + Net Cash $0.580B = Equity Value $11.03B ($50.53/share). Terminal value share: **0.0%**.

---

## E. Probability-Weighted Expected Value

| Case | Peak Sales (2031/32) | Operating Margin | WACC | Per Share Value | Weight | Weighted Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear** | $2.5B | 30.0% | 11.0% | $14.52 | 25% | $3.63 |
| **Base** | $4.5B | 36.0% | 10.2% | $27.36 | 55% | $15.05 |
| **Bull** | $7.5B | 42.0% | 9.5% | $50.53 | 20% | $10.11 |
| **Total**| — | — | — | — | **100%** | **$28.78 USD** |

- **Probability-Weighted Expected Value:** **$28.78 USD**
- **Margin of Safety at Spot ($98.50):** **-242.2%** (Upside: **-70.8%**)
- **Entry Price (< 30% MoS):** **$20.15 USD**
- **Exit Above (> 30% Premium to EV):** **$37.42 USD**

---

## F. Reverse DCF: What Must Be True?
To justify the current market price of **$98.50 USD** ($21.51B Market Cap / $20.93B Enterprise Value):
- At a 10.2% WACC and 36% operating margin, explicit cash flows through 2039 LOE must generate **>$14.5B in peak worldwide sales**.
- This requires brensocatib to not only capture the entire bronchiectasis market but to expand into multiple massive autoimmune/inflammatory indications with zero failure, making it one of the largest blockbuster drugs in pharmaceutical history.
- The market has capitalized a speculative blue-sky clinical pipeline while ignoring the substantial commercial launch friction, commercial SG&A costs, and ongoing cash burn.
