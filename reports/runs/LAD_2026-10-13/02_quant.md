# Quant Model: LAD (Lithia Motors, Inc.) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/LAD_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._
_Template: **FULL (Auto Dealership Retailer)**. Data layer: `fundamentals.json` LAD warnings: 1._

**Price basis:** $287.94 USD close on 2026-10-13. Market capitalization is **$6.33B USD** across 21.983M diluted shares outstanding (10-Q Q2-26).

---

## A. Lynch Classification & Category Checks
- **Classification:** **Cyclical at Trough-to-Mid-Cycle Margins**.
- **Evidence:** 
  - Revenue expanded at an extraordinary **23.5% CAGR** from FY20 ($13.1B) to FY25 ($37.6B), driven by dealership M&A (The Suburban Collection, Jardine Motors, Pendragon UK).
  - Operating margin peaked at **7.3% in FY21** and **6.9% in FY22** during severe pandemic vehicle shortages, then compressed to a normalized **4.2% in FY25** as vehicle inventory normalized.
  - Peter Lynch Cyclical Timing: Unlike cyclicals trading at peak margins, Lithia has already absorbed the post-pandemic margin compression (GPU normalization). Operating margins are back at their 10-year historical baseline (4.0%–4.3%).
- **Lynch Metrics:**
  - Trailing P/E: **9.54x**; Forward P/E: **6.92x**.
  - PEG Gate: **VALID** (`peg_is_valid()` returns True); **PEG = 0.54** (attractive under Lynch's GARP framework).
  - Cannibal Stock Dynamics: Management repurchased >24% of shares outstanding between FY21 and FY26 (shares down from 29.0M to 21.98M), with $960.9M repurchased in FY25 alone.

---

## B. Balance Sheet & Floor Plan Debt Treatment
- **Floor Plan Notes Payable (~$4.8B):**
  - Automotive dealership inventory is financed via floor-plan lines collateralized 1:1 by new and used vehicles on dealer lots. Under GAAP and rating agency frameworks, floor plan debt is an operational working capital mechanism, not funded corporate leverage.
- **Corporate Funded Debt:**
  - Mortgages, senior unsecured notes, and corporate credit lines total ~$5.45B.
  - Cash & equivalents: ~$0.45B.
  - Net Corporate Debt: **$5.00B USD ($227.45/share)**.
  - Enterprise Value (Industrial Corporate Basis): $6.33B market cap + $5.00B net debt = **$11.33B USD**.

---

## C. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (AN, PAG, ABG, GPI) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA (ex-floor plan) | 6.8x | 7.5x | 6.5x |
| P/E (ttm / fwd) | 9.5x / 6.9x | 7.8x | 8.2x / 7.5x |
| PEG Ratio | **0.54** | 0.65 | 0.75 |
| FCF Yield (Normalized) | 13.5% ($850M mid-cycle FCF) | 12.0% | 11.5% |
| Operating Margin | 4.2% (mid-cycle) | 5.4% | 4.5% |
| ROIC vs WACC | 10.7% (FY25) vs 10.75% | 15.2% | 11.0% |
| Net Corporate Debt / EBITDA | 2.5x ($5.0B corporate debt / $2.0B EBITDA) | 2.2x | 2.4x |

---

## D. Discount Rate Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (DGS10).
- Blume-Adjusted Beta: **1.180** (raw beta 1.264).
- Equity Risk Premium (ERP): **5.00%**.
- WACC / Cost of Equity: $5.22\% + (1.180 \times 5.00\%) = \mathbf{11.12\%} \rightarrow \mathbf{10.75\%}$ (modeled at 10.75% Base, 11.75% Bear, 9.75% Bull).

---

## E. DCF Scenarios (Executed via 02_model.py)
Explicit 10-year DCF modeling from base revenue of $37.64B and net corporate debt of $5.00B.

1. **BEAR Case: $103.46 USD (-64.1% vs $287.94)**
   - Used vehicle prices slump; financing rates constrain retail buyers; operating margin compresses to 3.5%; 10-yr rev CAGR 1.0%; WACC 11.75%, g_term 1.5%; equity value $2.27B.
2. **BASE Case: $323.53 USD (+12.4% vs $287.94)**
   - Mid-cycle operating margins hold at 4.2%; network consolidation CAGR 3.5%; fixed ops cash flow cushions cycles; WACC 10.75%, g_term 2.5%, terminal ROIC 12.0%; equity value $7.11B.
3. **BULL Case: $649.93 USD (+125.7% vs $287.94)**
   - UK Pendragon synergies exceed targets; fixed operations expand; operating margin expands to 4.8%; 10-yr rev CAGR 5.5%; WACC 9.75%, g_term 3.0%; equity value $14.29B.

---

## F. Reverse DCF: What Must Be True at $287.94?
- At mid-cycle 4.2% operating margin and 10.75% WACC, today's price discounts a constant **10-year revenue CAGR of just ~2.5%**.
- The tape has fully priced in cyclical margin normalization and assumes low future dealership consolidation.
