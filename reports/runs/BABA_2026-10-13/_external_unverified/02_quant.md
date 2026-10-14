# Quant Model: BABA (Alibaba Group Holding Limited) — as of 2026-10-13

_Status: COMPLETE. Model: `reports/runs/BABA_2026-10-13/02_model.py` (executed 2026-10-14, exit 0)._
_Template: **FULL**. Data layer: `fundamentals.json` BABA warnings `[]`, errors `[]`._

**Price basis:** $110.53 USD close on 2026-10-13 (yfinance/fundamentals.json). Intraday was $109.64. Market capitalization is **$265.76B USD** across 2,404.375M ADS (19,235.0M ordinary shares, 8 shares per ADS). Net cash is **$4.94B USD** (CNY 33.0B; $2.05/ADS). Enterprise Value is **$260.82B USD**.

---

## A. Lynch Classification & Category Checks
- **Classification:** **Stalwart facing Cyclical/Structural Headwinds**.
- **Evidence:** 
  - Reported revenue CAGR over FY21–FY26 was **7.4%** (CNY 717.3B to CNY 1,023.7B).
  - Operating profit, however, dropped from CNY 89.7B (FY21) and peak CNY 140.9B (FY25) down to CNY 50.2B in FY26 as Taobao/Tmall sacrificed margins to defend market share against PDD and ByteDance.
  - While historically an elite Fast Grower, domestic e-commerce saturation and relentless competitor price wars have demoted Alibaba to a low-to-mid single-digit grower.
- **Lynch Metrics:**
  - Forward P/E: **11.9x** (on normalized adjusted earnings); Trailing GAAP P/E: **26.8x** (distorted by non-operating impairment charges).
  - Lynch Ratio: $(4.5\% \text{ growth} + 3.0\% \text{ dividend yield}) / 11.9 = \mathbf{0.63}$ (poor; below 1.0 threshold).
  - Net Cash per ADS: **$2.05 USD** (net cash represents only ~2% of market cap; cash pile of $43B is substantially offset by $38B in total debt).
  - Inventory Check: Minimal inventory risk (Alibaba operates primarily as a platform marketplace).

---

## B. Business Quality & Moat
- **Moat: Wide, but Narrowing under multi-front assault.**
  - *Taobao & Tmall:* Massive consumer network effects (>1 billion annual active consumers) and merchant logistics lock-in. However, pricing power has visibly eroded: take-rates have stagnated as merchants allocate ad budgets to Douyin livestreaming and Pinduoduo.
  - *Cloud Intelligence:* #1 public cloud provider in China with high enterprise switching costs and expanding AI model training workloads. However, aggressive cloud price cuts restrict EBITA margins to mid-single digits (6–8%).
- **ROIC vs WACC:** FY26 reported ROIC was ~6.4% (burdened by impairments), well below its 10.5% cost of capital. Mid-cycle normalized ROIC is ~12.0%, providing narrow excess economic spread.

---

## C. GARP & Valuation Matrix
| Metric | Current (TTM/FY26) | 5-Yr Own Avg | Peer Median (Tencent, PDD, JD) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 8.5x | 11.5x | 12.2x |
| P/E (ttm / fwd) | 26.8x GAAP / 11.9x fwd | 18.5x | 15.4x |
| P/FCF | 14.8x (normalized FCF $18B) | 14.0x | 13.5x |
| FCF Yield | 6.8% | 7.1% | 7.4% |
| Lynch Ratio (g + yield) / P/E | 0.63 | 1.15 | 1.40 |
| ROIC vs WACC | 6.4% (FY26) / 12.0% mid-cycle vs 10.5% | 14.5% | 18.0% |
| Net debt / Owner earnings | Net Cash ($4.94B net cash) | Net Cash | Net Cash |

---

## D. Discount Rate Build (USD / China Risk Hurdle)
- 10-Year US Treasury Yield: **5.22%** (DGS10).
- China Geopolitical / Country Risk Premium: **2.00%** (reflecting regulatory, VIE, and trade sanctions risk).
- Blume-Adjusted Beta: **0.642** (raw beta 0.463).
- Equity Risk Premium (ERP): **5.00%**.
- WACC / Cost of Equity: $5.22\% + 2.00\% + (0.642 \times 5.00\%) = \mathbf{10.43\%} \rightarrow \mathbf{10.50\%}$.
- Sensitivity bounds: Bear 11.50%, Bull 9.50%.

---

## E. DCF Scenarios (Executed via 02_model.py)
Explicit 10-year DCF modeling from base FY2026 revenue ($153.23B USD) and net cash ($4.94B USD).

1. **BEAR Case: $35.78 USD (-67.6% vs $110.53)**
   - Stagnant domestic consumption; PDD and Douyin continue taking share; group 10-year revenue CAGR 1.5%; operating margin settles at 8.0%; WACC 11.5%, g_term 1.5%; equity value $86.0B.
2. **BASE Case: $69.58 USD (-37.1% vs $110.53)**
   - Taobao/Tmall GMV stabilizes (+3% CAGR); Cloud AI accelerates (+12%–15%); group 10-year revenue CAGR 4.5%; operating margin stabilizes at 12.0%; WACC 10.5%, g_term 2.5%, terminal ROIC 12.0%; equity value $167.3B.
3. **BULL Case: $126.77 USD (+14.7% vs $110.53)**
   - Macro stimulus triggers consumer recovery; Cloud margins expand to 15.0%; group 10-year revenue CAGR 7.5%; operating margin 15.0%; WACC 9.5%, g_term 3.5%, terminal ROIC 16.0%; equity value $304.8B.

---

## F. Reverse DCF: What Must Be True at $110.53?
- **Implied 10-Year Revenue Growth:** At Base operating margins (12.0%), current price of $110.53 discounts a constant **11.5% revenue CAGR for 10 consecutive years** (group revenue reaching $455B by Year 10).
- **Implied Operating Margin:** At Base revenue growth (4.5% CAGR), today's price requires an immediate, permanent operating margin expansion to **19.5%** (compared to 5.0% reported in FY26 and 12.0% mid-cycle).
- **Conclusion:** The tape is pricing in a dramatic, uninterrupted fundamental boom that far exceeds China's macroeconomic reality and platform competitive dynamics.

---

## G. Sensitivity Grid (Base Value / ADS by WACC × Terminal Growth)
```
WACC / g       1.5%      2.0%      2.5%      3.0%      3.5%
  9.5%      $ 77.17   $ 77.90   $ 78.71   $ 79.63   $ 80.68
 10.0%      $ 72.73   $ 73.26   $ 73.85   $ 74.50   $ 75.23
 10.5%      $ 68.79   $ 69.17   $ 69.58   $ 70.03   $ 70.52
 11.0%      $ 65.25   $ 65.52   $ 65.80   $ 66.10   $ 66.42
 11.5%      $ 62.07   $ 62.24   $ 62.42   $ 62.61   $ 62.81
```
Across the entire sensitivity matrix (even at 9.5% WACC and 3.5% terminal growth), intrinsic value does not exceed **$80.68**, well below the current market price of **$110.53**.
