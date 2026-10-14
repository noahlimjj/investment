<!-- pipeline:value-quant -->
# Value Quant Report: ASML.AS (ASML Holding N.V.)
As of: 2026-10-14 · Official Raw Close: €1,575.80 · Spot Price: €1,509.60

## A. Peter Lynch Classification
- **Lynch Category:** **Fast Grower transitioning to Stalwart.**
- **Classification Evidence:** 5-year revenue CAGR is +18.5% (from €13,978M in FY20 to €32,667M in FY25), driven by EUV adoption. However, law of large numbers and semiconductor cycle fab additions are moderating trend growth toward 10–12%.
- **Lynch Checks:**
  - **Lynch Ratio:** `(EPS Growth % + Dividend Yield %) / Trailing P/E = (22.0% + 0.5%) / 57.2x = 0.39` (Poor; below 1.0 hurdle).
  - **Net-Cash-Adjusted P/E:** `(Price €1,509.60 - Net Cash per share €22.96) / EPS €24.70 = 60.2x`.
  - **Inventory vs Sales Check:** In FY25, revenue grew +15.6% while inventory grew +11.2% (healthy inventory discipline; no discounting glut).

## B. Warren Buffett Business Quality
- **Economic Moat: Wide (Monopoly status in EUV, Pricing Power intact).**
  - Gross margins have held remarkably steady: 48.6%, 52.7%, 50.5%, 51.3%, 51.3%, 52.8% (FY20–FY25).
  - ASML possesses a 100% global monopoly on EUV lithography systems. Competitors (Canon, Nikon) cannot produce sub-7nm commercial scanners.
- **Owner Earnings vs Capex:**
  - OCF: €12,658M | PP&E Capex: €1,574M.
  - **Owner Earnings:** €9,004M (€10,094M USD).
  - Owner Earnings Yield on Market Cap (€580B): **1.55%** (Extremely compressed).
- **ROIC vs WACC:**
  - ROIC is **87.1%** vs WACC of **9.50%** (Economic value added spread is +77.6 percentage points).

## C. GARP & Valuation Multiples Matrix
| Metric | Current (ASML.AS) | 5-Yr Own Avg | Peer Median (AMAT, LRCX, KLAC) |
|---|---|---|---|
| **EV / EBITDA** | **42.6x** | 33.5x | 22.1x |
| **P/E (Trailing / Forward)** | **57.2x / 28.7x** | 41.0x / 31.0x | 23.5x / 24.1x |
| **P/FCF (SBC-Adjusted)** | **53.6x** | 42.0x | 26.5x |
| **FCF Yield** | **1.90%** | 2.50% | 3.90% |
| **Owner Earnings Yield** | **1.55%** | 2.10% | 4.20% |
| **PEG Ratio** | **1.12** (`peg_is_valid`: True) | 1.45 | 1.55 |
| **Lynch Ratio** | **0.39** | 0.65 | 0.85 |
| **Net Cash / (Debt)** | **+€8,931M Net Cash** | +€3,500M | Net Cash |

## D. Executed DCF Valuation Scenarios (from `02_model.py`)
- **Model Details:** 10-year explicit forecast, mid-year discounting, corporate tax 18.0%, Netherlands 10y risk-free rate 3.564%, Blume-adjusted beta 1.202, WACC 9.50%. Net cash €8,931M added to equity bridge.

| Scenario | 10-Yr Rev CAGR | EBIT Margin | WACC | Term. Growth | Fair Value per Share | Enterprise Value | Terminal Value Share |
|---|---|---|---|---|---|---|---|
| **Bear Case** | +4.4% | 29.0% | 10.0% | 2.0% | **€316.64** | €114,243M | 46.6% |
| **Trough Case** | +6.6% | 32.0% | 9.5% | 2.5% | **€444.87** | €164,123M | 52.5% |
| **Base Case** | +9.5% | 34.5% | 9.5% | 3.0% | **€614.44** | €230,087M | 56.7% |
| **Bull Case** | +12.0% | 37.0% | 9.0% | 3.5% | **€881.61** | €334,014M | 62.7% |

## E. Reverse DCF Analysis
- **At Spot Price (€1,509.60):** The stock prices in a constant 10-year revenue CAGR of **22.28%** at 34.5% EBIT margins.
- **At Official Raw Close (€1,575.80):** The stock prices in a constant 10-year revenue CAGR of **22.88%**.
- **Reality Check:** To justify today's valuation, ASML's revenue must compound from €32.7B to over **€244.0B** by 2035—more than the entire global wafer fab equipment market today.
