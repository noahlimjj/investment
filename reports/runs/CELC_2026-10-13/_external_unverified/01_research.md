# Research Dossier: CELC (Celcuity Inc.) — as of 2026-10-13

Status: CURRENT HOLDING (Singapore tax resident, SGD base). US clinical-stage oncology biopharma (NASDAQ: CELC).

## 0. Routing
rNPV (Clinical-stage oncology biopharma with pivotal Phase 3 registration trial: Gedatolisib in HR+/HER2- Advanced Breast Cancer). Quote ccy USD; reporting ccy USD.

## 1. Snapshot (Tape First)
- **Current Price:** $64.38 USD ($64.375 in 00_inputs.json; 52-week range: $46.20 to $144.98).
- **12-Month Change:** +36.8% (down from 52-week highs of $144.98 following anticipation and enrollment completion of pivotal Phase 3 VIKTORIA-1 trial).
- **Shares Outstanding:** 48,931,908 shares (10-Q Q2-26 accn 0001193125-26-349608, cover date 2026-08-05).
- **Market Capitalization:** 48.93M shares × $64.38 = **$3.15B USD**.
- **Balance Sheet & Liquidity (as of 2026-06-30):**
  - Cash and cash equivalents: $182.0M USD.
  - Marketable securities (short-term investments): $572.0M USD.
  - Total Liquid Cash & Investments: **$754.0M USD ($0.754B)**.
  - Total Debt: **$754.4M USD ($0.754B)** (convertible debt and term loan credit facility).
  - Net Cash Position: **-$0.3M USD (-$0.00B, net cash neutral / -$0.01/share)**.
  - Operating cash flow burn: TTM OCF is -$191.7M; FY25 OCF was -$153.5M. The $754.0M liquid cash cushion provides ~3.5 years of cash runway, funding the company through Phase 3 VIKTORIA-1 data readouts and initial commercial launch preparations.
- **Multiples:** Trailing P/E negative (net loss -$226.5M TTM); Pre-revenue ($0 commercial product revenue); Stockholders' Equity is -$12.8M (distorted equity base due to cumulative R&D losses).
- **Data Layer Warnings (4):**
  1. `institutional_pct=1.1010 outside 0..1 - vendor artifact, do not quote as a fact` (Vendor artifact per Rule FIX-6).
  2. `roe=-1433.70% implies a distorted equity base - use ROCE/ROIC instead` (Stockholders' equity distorted by -$580.6M accumulated deficit per Rule FIX-5).
  3. `debt_to_equity is MISSING (null) - absent, not zero; do not assert a value` (Negative equity base leaves D/E mathematically null per Rule FIX-4).
  4. `owner earnings negative - confirm against the cash flow statement before use` (Verified: Pre-revenue oncology biotech; OCF -$191.7M TTM, SBC $28.5M).

## 2. Financial History (USD Thousands; Source SEC 10-K Filings FY2020–FY2025)
| Metric | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| **Revenue** | 0 | 0 | 0 | 0 | 0 | 0 |
| **Gross Margin** | n/a | n/a | n/a | n/a | n/a | n/a |
| **Operating Income** | -10,031 | -38,103 | -44,380 | -63,497 | -108,124 | -165,820 |
| **Net Income** | -9,820 | -42,540 | -43,210 | -60,180 | -104,230 | -182,450 |
| **Operating Cash Flow** | -8,450 | -28,210 | -38,150 | -55,420 | -98,650 | -153,529 |
| **Cash & ST Investments** | 22,410 | 114,350 | 85,120 | 185,420 | 148,600 | 452,540 |
| **Total Debt** | 0 | 0 | 18,500 | 18,200 | 99,415 | 323,441 (754M now) |
| **Diluted Shares (M)** | 10.2 | 14.8 | 15.2 | 22.4 | 38.6 | 45.2 (48.9 now) |

## 3. Product Architecture & Oncology Pipeline
- **Gedatolisib (PF-05212384):**
  - First-in-class, highly potent dual pan-PI3K (p110α, β, γ, δ) and mTOR (mTORC1 and mTORC2) inhibitor licensed globally from Pfizer in April 2021.
  - Indication: HR+/HER2- metastatic breast cancer (MBC) in patients who progressed on CDK4/6 inhibitor therapy.
  - Scientific Rationale: Hyperactivation of the PI3K/AKT/mTOR signaling pathway is the primary mechanism of endocrine and CDK4/6 resistance. By simultaneously targeting all class I PI3K isoforms and both mTOR complexes, gedatolisib achieves deep pathway suppression without activating feedback feedback loops.
  - Favorable Safety Profile: Unlike isoform-specific PI3K inhibitors (Novartis' Piqray / alpelisib, which has ~30% Grade 3/4 hyperglycemia and severe rash), gedatolisib's intermittent weekly IV dosing produces significantly lower rates of severe metabolic toxicity.
- **Pivotal Phase 3 Trial (VIKTORIA-1):**
  - Evaluating gedatolisib + fulvestrant ± palbociclib vs standard fulvestrant in two distinct cohorts:
    - Cohort A: PIK3CA-mutated patients.
    - Cohort B: PIK3CA-wild-type patients.
  - Primary endpoint is progression-free survival (PFS). Registrational data readouts expected in 2025/2026.
- **Secondary Pipeline Programs:**
  - CELC-G-201: Phase 1/2 clinical study in metastatic castration-resistant prostate cancer (mCRPC) and other advanced solid tumors.
- **Exclusivity & Patents:** Formulation and composition of matter patents extend through ~2039. Terminal value post-2039 is set strictly to **0.0%**.

## 4. Capital Allocation Assessment
- **License-to-Registrational Model:** Management opportunistically acquired Pfizer's clinical asset gedatolisib for $5M upfront plus milestones, transforming Celcuity from a diagnostics company into a Phase 3 oncology biopharma.
- **Balance Sheet Expansion:** The company raised $754M in convertible debt and term loan financing to fully fund VIKTORIA-1 and commercial pre-launch activities.
- **Cash Runway:** With $754.0M in liquid assets against ~$190M annual cash burn, the company has ~3.5 years of runway, completely insulated from emergency dilutive equity issuance before Phase 3 readouts.
