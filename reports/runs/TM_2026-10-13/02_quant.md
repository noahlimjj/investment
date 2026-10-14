# Quant Model: TM (Toyota Motor Corporation) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/TM_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._
_Template: **FULL (Modified Auto Industrial + Captive Finance)**. Data layer: `fundamentals.json` TM warnings: 1._

**Price basis:** $188.38 USD close on 2026-10-13. Market capitalization is **$245.53B USD** across 1,303.39M ADS (13,033.9M common shares, 10 shares per ADS).

---

## A. Lynch Classification & Category Checks
- **Classification:** **Stalwart / Cyclical at Mid-to-Peak Margins**.
- **Evidence:** 
  - Toyota expanded revenue from JPY 29.9T (FY20) to JPY 48.0T (FY25), benefiting from a strong product cycle, hybrid leadership, and an ultra-weak yen.
  - Operating margin peaked at **11.9% in FY24** and settled at **10.0% in FY25**, well above the 5-year pre-boom average of ~7.5%–8.2%.
  - Lynch Cyclical Warning: Trailing P/E sits at a modest **8.3x**, but forward P/E is **11.9x** due to expected earnings contraction as yen tailwinds normalize and vehicle certification remediations are absorbed. The data layer explicitly voided PEG.
- **Mid-Cycle Valuation Principle:**
  - Automotive manufacturing must be valued on sustainable mid-cycle operating margins (7.5%–8.5%) rather than peak currency-windfall margins.

---

## B. Segment Architecture: Industrial Auto vs Captive Finance
- **Automotive Industrial Business:**
  - FY2025 Revenue: JPY 48.04T (~$303.3B USD).
  - Normalized Mid-Cycle EBIT: JPY 3.84T (8.0% margin).
  - Tax Rate: 29.0% effective rate -> NOPAT JPY 2.73T.
  - Automotive Capex (JPY ~2.25T) vs D&A (JPY ~1.90T) implies annual reinvestment drag of ~JPY 350B. Normalized industrial FCF = JPY ~2.18T ($13.8B USD).
- **Non-Operating Asset SOTP Bridge:**
  - *Net Industrial Cash:* Cash & liquid securities JPY 8.98T less industrial debt JPY ~4.50T = **JPY 4.48T ($28.3B USD)**.
  - *Toyota Financial Services (Captive Finance Equity):* JPY ~5.0T book equity, valued at 0.8x book = **JPY 4.00T ($25.3B USD)**.
  - Total non-operating asset cushion: **$53.54B USD ($41.08/ADS)**.

---

## C. GARP & Valuation Matrix
| Metric | Current Peak (FY25) | 5-Yr Own Avg | Peer Median (VW, Honda, GM, Stellantis) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA (Consolidated) | 6.5x (distorted by finance debt) | 7.2x | 5.8x |
| P/E (ttm / fwd) | 8.3x / 11.9x | 10.5x | 6.5x / 7.2x |
| FCF Yield (Consolidated) | 5.5% (distorted by finance cash flows) | 4.8% | 6.2% |
| Industrial Net Cash / Market Cap | 11.5% ($28.3B net cash) | 10.0% | 8.5% |
| ROIC vs WACC | 12.4% (FY25) / 10.5% mid-cycle vs 8.12% | 10.0% | 8.2% |
| Lynch Ratio (g + yield) / P/E | VOID (earnings contracting post-peak) | — | — |

---

## D. Discount Rate Build (USD ADS Basis)
- 10-Year US Treasury Yield: **5.22%** (DGS10).
- Blume-Adjusted Beta: **0.580** (raw beta 0.375).
- Equity Risk Premium (ERP): **5.00%**.
- Cost of Equity / WACC: $5.22\% + (0.580 \times 5.00\%) = \mathbf{8.12\%}$ (binds near 8.0% USD floor).

---

## E. DCF Scenarios (Executed via 02_model.py)
Explicit 10-year DCF modeling on automotive industrial cash flows plus $53.5B non-operating assets.

1. **BEAR Case: $135.14 USD (-28.3% vs $188.38)**
   - Yen appreciates to 120–125; China sales contract under intense BYD EV pressure; industrial EBIT margin slips to 6.0%; 10-year rev CAGR 1.0%; WACC 8.80%, g_term 1.5%; equity value $176.1B.
2. **BASE Case: $205.41 USD (+9.0% vs $188.38)**
   - Yen stabilizes around 140–145; hybrid volume holds steady; mid-cycle industrial EBIT margin 8.0%; 10-year rev CAGR 2.5%; WACC 8.12%, g_term 2.0%, terminal ROIC 11.0%; equity value $267.7B.
3. **BULL Case: $301.92 USD (+60.3% vs $188.38)**
   - Global hybrid hegemony widens; solid-state battery tech enters production; operating margin 9.5%; 10-year rev CAGR 4.0%; WACC 7.50%, g_term 2.5%, terminal ROIC 13.0%; equity value $393.5B.

---

## F. Reverse DCF: What Must Be True at $188.38?
- At mid-cycle 8.0% operating margin, current price of $188.38 implies a constant **10-year revenue CAGR of just ~1.0%**.
- Today's tape reflects conservative expectations, fully pricing in post-peak profit contraction without baking in catastrophic structural share loss.
