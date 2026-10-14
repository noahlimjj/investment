# Quant Model: INCY (Incyte Corporation) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/INCY_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._
_Template: **FULL (Commercial Biopharma with Patent Cliff)**. Data layer: `fundamentals.json` INCY warnings: 1._

**Price basis:** $108.95 USD close on 2026-10-13. Market capitalization is **$21.77B USD** across 199.782M diluted shares outstanding (10-Q Q1-26). Net cash is **$3.10B USD ($15.51/share)** with zero funded debt. Enterprise Value is **$18.67B USD**.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Stalwart facing a Structural Patent Cliff**.
- **Evidence:** 
  - Revenue grew at an impressive **14.0% CAGR** from FY20 ($2.67B) to FY25 ($5.14B), driven by US Jakafi expansion and the rapid launch trajectory of Opzelura.
  - Operating margin expanded to **29.5% in FY25** (operating income $1.51B).
  - However, the business faces an imminent structural disruption: **Jakafi (ruxolitinib), which represents over 60% of total revenue, loses US patent protection in late 2028**.
- **Lynch Metrics:**
  - Trailing GAAP P/E: **13.88x**; Forward P/E: **12.51x**.
  - PEG Gate: Valid; **PEG = 0.95** (based on historical growth). However, per Rule FIX-6, PEG is deceptive when a major patent cliff sits within the 3-year investment horizon.
  - Net Cash per Share: **$15.51 USD** (cash covers 14.2% of market cap).

---

## B. The Jakafi LOE Replacement Dynamics
- **Jakafi Revenue Base:** ~$3.2B total contribution (US net sales ~$2.8B + Novartis ex-US royalties ~$400M). Generic entry in 2029 will trigger a standard -30% to -40% annual erosion curve.
- **Opzelura (ruxolitinib cream):** Currently generating ~$700M annualized. Expected to reach peak sales of $1.8B–$2.2B by 2030 across atopic dermatitis and vitiligo.
- **Pipeline & Expansion:** Niktimvo (axatilimab), Pemazyre, Monjuvi, and mutant CALR antibody (INCA33989) must generate >$1.5B in incremental revenue to offset Jakafi's decline.

---

## C. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (BIIB, GILD, REGN, VRTX) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 11.2x | 13.5x | 12.0x |
| P/E (ttm / fwd) | 13.9x / 12.5x | 18.0x | 14.5x / 13.2x |
| P/FCF (Normalized) | 18.1x (on $1.2B FCF) | 17.5x | 16.0x |
| FCF Yield | 5.5% | 5.7% | 6.2% |
| Net Cash / Market Cap | 14.2% ($3.10B net cash) | 12.5% | 8.5% |
| ROIC vs WACC | 16.5% vs 8.50% | 12.2% | 15.0% |

---

## D. Discount Rate Build (USD Basis)
- 10-Year US Treasury Yield: **5.22%** (DGS10).
- Blume-Adjusted Beta: **0.650** (raw beta 0.475).
- Equity Risk Premium (ERP): **5.00%**.
- WACC / Cost of Equity: $5.22\% + (0.650 \times 5.00\%) = \mathbf{8.47\%} \rightarrow \mathbf{8.50\%}$.

---

## E. DCF Scenarios (Executed via 02_model.py)
Explicit 10-year DCF modeling from base revenue of $5.14B, explicitly embedding the 2029–2030 Jakafi generic revenue contraction.

1. **BEAR Case: $44.31 USD (-59.3% vs $108.95)**
   - Opzelura plateaus at $1.4B peak; Jakafi generic erosion is severe (-25% Y4, -18% Y5); operating margin drops to 14%–16%; WACC 9.25%, g_term 1.5%; equity value $8.85B.
2. **BASE Case: $71.42 USD (-34.5% vs $108.95)**
   - Opzelura reaches $2.0B peak; pipeline adds $1.2B; Jakafi contracts to $400M by 2035; operating margin stabilizes at 22%; WACC 8.50%, g_term 2.5%, terminal ROIC 12.0%; equity value $14.27B.
3. **BULL Case: $128.66 USD (+18.1% vs $108.95)**
   - Opzelura expands to $2.8B; CALR antibody becomes a $2.0B blockbuster; operating margin holds >25%; WACC 7.75%, g_term 3.0%; equity value $25.70B.

---

## F. Reverse DCF: What Must Be True at $108.95?
- Today's market price of $108.95 requires the **BULL CASE** to materialize in full: non-Jakafi products must generate >$3.5B in peak revenue by 2031 to completely offset the patent cliff without experiencing operating margin compression.
- The tape has priced in near-flawless pipeline commercialization, leaving no margin of safety for clinical or commercial stumbles.
