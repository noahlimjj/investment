# Quant Model: ACAD (ACADIA Pharmaceuticals Inc.) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/ACAD_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._
_Template: **FULL (Commercial CNS Biopharma)**. Data layer: `fundamentals.json` ACAD warnings: 1._

**Price basis:** $18.815 USD close on 2026-10-13 ($18.82). Market capitalization is **$3.24B USD** across 172.305M diluted shares outstanding (10-Q Q2-26). Net cash is **$0.498B USD ($2.89/share)** with zero funded debt. Enterprise Value is **$2.74B USD**.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Stalwart / Fast Grower transitioning to Commercial Maturity**.
- **Evidence:** 
  - Revenue expanded at a **19.4% CAGR** from FY20 ($441.8M) to FY25 ($1,071.5M), crossing the $1B threshold following the launch of Daybue (trofinetide).
  - The business reached sustained GAAP operating profitability in FY24 ($230.8M) and FY25 ($104.8M).
  - Lynch Growth Metrics:
    - Trailing GAAP P/E: **8.44x** (artificially depressed by a deferred tax asset valuation allowance release in FY25).
    - Forward P/E: **20.82x** (reflecting normalized income taxes and stepped-up R&D).
    - Ratio check: Forward P/E (20.8) > Trailing P/E (8.4); data layer officially voided PEG.
    - Net Cash Cushion: **$2.89/share** (cash covers 15.4% of market cap).

---

## B. Commercial Franchise Architecture
- **Nuplazid (pimavanserin):** Generating ~$580M–$600M annually for Parkinson's disease psychosis. High gross margins (~90%) provide stable cash generation through 2030 patent expiry.
- **Daybue (trofinetide):** The sole approved treatment for Rett syndrome. Generated ~$350M+ in initial full commercial year. Facing real-world gastrointestinal discontinuation rates (~20%–25%), but expanding internationally into Europe and Canada.
- **Operating Margin Profile:** Gross margin is 92%–94%; normalized mid-cycle operating margin settles around 18.0% after ongoing Phase 3 pipeline spend.

---

## C. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (JAZZ, BMRN, NBIX, ITCI) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 12.5x | 18.0x | 13.5x |
| P/E (ttm / fwd) | 8.4x / 20.8x | n/m (past losses) | 18.5x / 16.0x |
| FCF Yield (Normalized) | 4.8% ($155M mid-cycle FCF) | negative | 5.2% |
| Net Cash / Market Cap | 15.4% ($498M net cash) | 12.0% | 9.0% |
| ROIC vs WACC | 15.2% vs 8.50% | negative | 12.5% |
| Net Debt / EBITDA | Net Cash ($0 Funded Debt) | Net Cash | Net Cash |

---

## D. Discount Rate Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (DGS10).
- Blume-Adjusted Beta: **0.650** (raw beta 0.480).
- Equity Risk Premium (ERP): **5.00%**.
- WACC / Cost of Equity: $5.22\% + (0.650 \times 5.00\%) = \mathbf{8.47\%} \rightarrow \mathbf{8.50\%}$.

---

## E. DCF Scenarios (Executed via 02_model.py)
Explicit 10-year DCF modeling from base revenue of $1.0715B and net cash of $0.498B.

1. **BEAR Case: $8.72 USD (-53.7% vs $18.82)**
   - Daybue GI discontinuations restrict persistence; Nuplazid generic erosion post-2030; operating margin 12.0%; 10-yr rev CAGR 1.0%; WACC 9.25%, g_term 1.5%; equity value $1.50B.
2. **BASE Case: $15.51 USD (-17.6% vs $18.82)**
   - Daybue ex-US launches succeed; Nuplazid stable through 2030; mid-cycle operating margin 18.0%; 10-yr rev CAGR 3.5%; WACC 8.50%, g_term 2.5%, terminal ROIC 12.0%; equity value $2.67B.
3. **BULL Case: $28.22 USD (+50.0% vs $18.82)**
   - Daybue global peak exceeds $700M; ACP-101 approved in Prader-Willi; operating margin expands to 24.0%; 10-yr rev CAGR 6.0%; WACC 7.75%, g_term 3.0%; equity value $4.86B.

---

## F. Reverse DCF: What Must Be True at $18.82?
- Today's market price of $18.82 discounts a constant **10-year revenue CAGR of ~5.2%** at mid-cycle 18.0% operating margins.
- The tape is balanced: it reflects moderate Daybue international growth and stability in Nuplazid, without baking in excessive pipeline speculation.
