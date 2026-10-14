# Quant Model: 000660.KS (SK Hynix Inc.) — as of 2026-10-13

## A. Lynch Classification & Category Checks
- **Classification:** **Cyclical at Peak Margins**.
- **Evidence:** 
  - Revenue expanded +144% YoY in FY24 and is on an annualized run-rate of KRW 317.3T in Q2-26, driven by an unprecedented High Bandwidth Memory (HBM) supply bottleneck for AI accelerators (Nvidia H100/H200/B200).
  - Operating margin reached **76.3% in Q2-26** and **68.0% TTM**, up from a devastating -34.0% loss in FY23 (KRW -7.7T operating loss).
  - This is a textbook Peter Lynch Cyclical: Memory semiconductors (DRAM and NAND) are commoditized capital-intensive components that experience severe boom-bust cycles driven by fab capex additions, customer inventory hoarding, and rapid pricing collapses.
- **Lynch Cyclical Trap Warning:**
  - Trailing P/E sits at a headline ~3.2x–3.8x (further distorted by non-operating gains). Peter Lynch explicitly warns: *"A low P/E during peak margins is a value trap. Value cyclicals on mid-cycle earnings, not peak earnings."*

---

## B. Business Quality & Earnings Adjustments
- **Moat:** **Narrow to Wide in HBM packaging (MR-MUF); None in Commodity DRAM/NAND.**
  - SK Hynix established temporary technological supremacy over Samsung and Micron in HBM3 and HBM3E via its proprietary Mass Reflow Molded Underfill (MR-MUF) process, securing sole-source or primary supplier status to Nvidia.
  - However, Samsung and Micron are committing massive capex into HBM3E/HBM4 qualification. Historical memory moats never sustain 70%+ EBIT margins indefinitely.
- **Distortions in Reported Net Income:**
  - In Q2 2026, SK Hynix recorded a **KRW 63.3T non-operating gain** (KRW 53.2T fair-value gain + KRW 10.0T dividend income related to its Kioxia investment).
  - This gain is entirely non-operational and must be excluded from sustainable earnings power.
  - Non-operating assets (remaining Kioxia/LT investment assets of KRW 85.3T) are treated separately in the EV bridge at a 30% haircut (KRW 59.7T).
- **Balance Sheet & EV Bridge (KRW Trillions):**
  - Market Cap: 728.87M shares × KRW 1,443,000 = **KRW 1,051.8T**.
  - Net Cash (Jun 30, 2026): Cash & equivalents + ST instruments (KRW 88.0T) less borrowings (KRW 18.6T) = **KRW 69.4T net cash**.
  - Post-Jun 30 ADS Offering Net Proceeds: ~US$26.2B = **KRW 35.1T**.
  - Current Unpaid Tax Liability: **KRW -32.0T**.
  - Non-operating LT investments (at 30% haircut): **KRW +59.7T**.
  - Net Asset Value Bridge to Enterprise Value: **KRW +136.3T** net non-operating assets.

---

## C. GARP & Valuation Matrix
| Metric | Current Peak (TTM) | 5-Yr History / Mid-Cycle | Peer Comparison (Samsung, Micron) |
| :--- | :--- | :--- | :--- |
| Trailing P/E | 3.5x (distorted by Kioxia gain) | 12.0x–16.0x (ex-loss years) | 9.5x / 14.2x |
| Mid-Cycle Normalized P/E | **30.1x** (at KRW 1,443,000 vs Y4 NOPAT) | 10.0x–12.0x mid-cycle | ~11.0x |
| EV / Mid-Cycle EBIT | **17.3x** (vs Y4 EBIT KRW 60.7T) | 6.0x–8.0x | ~7.5x |
| Operating Margin | 76.3% (Q2-26) / 68.0% (TTM) | 29.0% (5-yr weighted avg) | ~25.0% |
| ROIC vs WACC | 48.6% (peak) vs 13.83% | 15.0% mid-cycle | 12.0% |
| Lynch Ratio (g + yield) / P/E | VOID (cyclical peak) | — | — |

---

## D. Discount Rate Build (KRW Base)
- 10-Year Korea Treasury Bond (KTB): **4.369%** (dated KOFIA close Oct 6, 2026).
- Adjusted Beta: **1.892** (Blume adjustment on raw beta 2.391).
- Equity Risk Premium (ERP): **5.00%**.
- Cost of Equity / WACC: $4.369\% + (1.892 \times 5.00\%) = \mathbf{13.83\%}$.
- Note: Korea tech cyclicals carry high betas; even at beta 1.0 (WACC 9.27%), Base value would be KRW 1,003,655, still far below the current price of KRW 1,443,000.

---

## E. DCF Scenarios (Executed via 02_model.py)
The model incorporates explicit memory cycle modeling: a 2-year peak fade followed by a mid-cycle downturn (Y3-Y4) and long-term trend growth (Y5-Y10).

1. **BEAR Case: KRW 411,148 (-71.5% vs KRW 1,443,000)**
   - Peak collapses rapidly: Y1 rev KRW 270T, Y2 drops -30% to KRW 189T, Y3 drops to KRW 120T; mid-cycle EBIT margin compresses to 21.0%; trend growth 5.0%.
   - Equity Value: KRW 299.7T (EV KRW 163.4T + net assets KRW 136.3T).
2. **BASE Case: KRW 727,950 (-49.6% vs KRW 1,443,000)**
   - HBM strength persists for 1 year (Y1 rev KRW 317.3T, 70% EBIT margin), fades in Y2 (-20% rev, 55% EBIT), troughs in Y3 (KRW 156.2T, 32% EBIT), and recovers to mid-cycle EBIT margin of 29.0% with trend growth fading from 10% to 4%. Capex averages 27–30% of revenue.
   - Equity Value: KRW 530.6T (EV KRW 394.3T + net assets KRW 136.3T).
3. **BULL Case: KRW 1,267,426 (-12.2% vs KRW 1,443,000)**
   - Supercycle persists: Y1 rev KRW 383.9T (+21%), Y2 KRW 340.3T, mid-cycle EBIT margin settles at an elevated 42.0%, Y5–Y10 growth 9–15%.
   - Equity Value: KRW 923.8T (EV KRW 787.5T + net assets KRW 136.3T).

---

## F. Reverse DCF: What Must Be True at KRW 1,443,000?
- **Duration of Peak Margins:** At current price of KRW 1,443,000, peak conditions (KRW 317T+ revenue and 70%+ EBIT margins) must persist uninterrupted for **5 FULL YEARS** before any downturn to cover intrinsic value.
- **Required 10-Year Revenue Growth:** Implies a constant **11.4% CAGR** from the already-doubled Q2 run-rate for 10 consecutive years (reaching KRW 936T revenue by Year 10), or **19.6% CAGR** from TTM revenue.
- **Required Mid-Cycle Margin:** If base revenue is held, the required mid-cycle EBIT margin is **95.0%** (physically impossible in semiconductor hardware).
- **Implied IRR:** 6.79% (against a cost of capital of 13.83%).

---

## G. Load-Bearing Inputs & Sensitivity
- Sensitivity across WACC and Terminal Growth:
  - At WACC 11.83% and g 4.0%, Base value is KRW 821,922.
  - At WACC 13.83% and g 3.0%, Base value is KRW 727,950.
  - At WACC 15.83% and g 2.0%, Base value is KRW 670,372.
- Top load-bearing inputs: WACC hurdle (±7.5%), mid-cycle EBIT margin (±3.7%), and peak fade velocity.
