<!-- pipeline:value-researcher -->
# Stage 1: Value Researcher Dossier — Insmed Incorporated (INSM)
**As of Date:** 2026-10-14  
**Quote Currency:** USD | **Financial Currency:** USD | **Exchange:** NASDAQ  
**Template:** rNPV (Commercial / Clinical-Stage Biopharma)  
**Holding Status:** Active Holding (40 shares @ $96.79 USD, Market Value $3,871.60 USD)

---

## 1. Company Profile & Commercial Pipeline
Insmed Incorporated (`INSM`) is a biopharmaceutical company focused on serious, rare diseases in pulmonology and inflammatory conditions.

1. **Arikayce (Amikacin Liposome Inhalation Suspension):**
   - Approved in the US, Europe, and Japan for refractory *Mycobacterium avium* complex (MAC) lung disease as part of a combination antibacterial regimen.
   - Core commercial cash generator: FY2025 revenue reached $606M, and TTM revenue reached $1,138M (up from $164M in FY2020).
   - Expanding into frontline MAC clinical trials (ENCORE trial).

2. **Brensocatib (DPP1 / Cathepsin C Inhibitor) — The Load-Bearing Asset:**
   - First-in-class, oral reversible inhibitor of dipeptidyl peptidase 1 (DPP1), which activates neutrophil serine proteases (NSPs).
   - **ASPEN Phase 3 Trial:** Successfully met primary endpoint in non-cystic fibrosis bronchiectasis (NCFB), demonstrating a statistically significant reduction in annualized rate of pulmonary exacerbations versus placebo (p=0.004).
   - **Epidemiology:** NCFB affects >450,000 diagnosed patients in the US, with >1M across the G7. Zero currently approved pharmacotherapies.
   - **Regulatory Timeline:** NDA submission under review; PDUFA and commercial launch expected in 2025–2026.
   - **Lifecycle Extension:** Phase 2 exploratory studies in Chronic Rhinosinusitis without Nasal Polyps (CRSwNP) and Hidradenitis Suppurativa (HS).

3. **Treprostinil Palmitil Inhalation Powder (TPIP):**
   - Dry powder pro-drug formulation of treprostinil administered once daily via small inhaler for Pulmonary Arterial Hypertension (PAH) and Pulmonary Hypertension associated with Interstitial Lung Disease (PH-ILD).
   - Competing against United Therapeutics' Tyvaso DPI (treprostinil) and Liquidia's Yutrepia.

---

## 2. Audited Historical Financials (SEC Form 10-K & 10-Q)

| Metric (USD Millions) | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (Q2-26) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Revenue** | $164 | $188 | $245 | $305 | $364 | $606 | $1,138 |
| **Gross Margin** | 75.7% | 76.6% | 77.5% | 78.5% | 76.4% | 79.7% | 83.5% |
| **Operating Income** | -$265 | -$375 | -$457 | -$710 | -$878 | -$1,247 | -$841 |
| **Net Income** | -$294 | -$435 | -$482 | -$750 | -$914 | -$1,277 | -$875 |
| **Operating Cash Flow (OCF)** | -$219 | -$363 | -$400 | -$536 | -$684 | -$935 | -$779 |
| **CapEx** | $6 | $7 | $10 | $13 | $22 | $33 | $29 |
| **Free Cash Flow (FCF)** | -$226 | -$371 | -$410 | -$550 | -$706 | -$968 | -$808 |
| **Stock-Based Comp (SBC)** | $36 | $46 | $58 | $75 | $97 | $153 | $157 |
| **Diluted Shares (M)** | 98 | 112 | 123 | 140 | 164 | 199 | 218.4 |

### Load-Bearing Financial Observations:
- **Revenue 5-Yr CAGR:** 29.8% (driven by commercial expansion of Arikayce).
- **Share Dilution 5-Yr CAGR:** 15.3% (share count doubled from 98M to 199M to fund clinical trials).
- **Cumulative Retained Deficit:** -$4.85 Billion.
- **Stock-Based Compensation:** $157.5M TTM (constituting 20.2% of total operational cash burn).

---

## 3. Balance Sheet, Solvency & Cash Runway
- **Total Cash, Equivalents & Marketable Securities:** $1,160.3M (as of Q2 2026).
- **Long-Term Debt:** $579.9M (convertible notes).
- **Net Cash:** **+$580.4M ($2.66 / share)**.
- **Current Run-Rate Operating Burn:** -$779M annually.
- **Solvency & Runway:** Total liquidity of $1.16B provides approximately **1.5 to 1.8 years of operational runway**. Breakeven depends directly on a successful, non-discounted launch of brensocatib by FY2026/2027; otherwise, further secondary equity offerings will be required.

---

## 4. Benchmark Inputs (from `00_inputs.json`)
- **Spot Price:** $96.79 USD (as of 2026-10-14).
- **10-Year US Treasury Benchmark:** 5.22% (FRED DGS10).
- **Equity Risk Premium:** 5.0%.
- **Biopharma Beta:** ~1.00.
- **Base Biopharma WACC:** 10.20% (Cost of Equity 5.22% + 5.00%).

---

## 5. Data Warnings & Primary Sources
- **Warnings in Data Layer:**
  - `institutional_pct = 1.0506` (vendor artifact outside 0..1, do not quote as >100%).
  - `owner_earnings negative` (standard for pre-commercial / Phase 3 biotech; rNPV template required).
- **Primary Sources:**
  - SEC EDGAR Form 10-Q (accn `0001104506-26-000041`) and Form 10-K (accn `0001104506-26-000009`).
  - Phase 3 ASPEN Clinical Trial Publication (NEJM, 2024).
  - FRED Federal Reserve Economic Data (Series DGS10).
