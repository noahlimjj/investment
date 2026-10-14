# Equity Analysis: ASML.AS — ASML Holding N.V.
As of 2026-10-14 · Price 1509.60 EUR · Template FULL · Run: `reports/runs/ASML.AS_2026-10-14/`

## 0. Two-Minute Drill (Lynch)
**A world-monopoly Fast Grower now trading at euphoria multiples.** 
- **Why own it:** ASML is the undisputed sole global supplier of Extreme Ultraviolet (EUV) photolithography scanners, without which advanced microchips below 7nm cannot be commercially manufactured. The company earns an extraordinary 87.1% ROIC on a fortress balance sheet with €8.93B in net cash and €9.00B in annual Owner Earnings.
- **What has to happen:** Today's spot price of €1,509.60 requires an impossible **22.28% constant revenue CAGR for 10 straight years**, growing sales from €32.7B to over €244.0B by 2035 at elevated 34.6% operating margins.
- **What could go wrong:** Western export bans on immersion DUV tools to China threaten ~30–40% of recent tool shipments; customer concentration is extreme (TSMC, Samsung, Intel represent >80% of bookings); and TSMC is pushing out High-NA adoption due to exorbitant €350M+ tool costs.

---

## 1. Executive Summary & Expected Value
- **Current Price:** €1,509.60 (official raw close €1,575.80) · **12-Mo Change:** +68.5% (down -13.3% from 52-week peak of €1,818.00).
- **Bear / Trough / Base / Bull:** €316.64 (25%) / €444.87 (35%) / €614.44 (30%) / €881.61 (10%).
- **Expected Value (probability-weighted):** **€507.35** → margin of safety: **-197.5%** (downside: **-66.4%**).
- **SBC-adjusted Expected Value:** **€505.20** (SBC is minimal at 1.6% of OCF).
- **Price Implies (Reverse DCF):** At €1,509.60, the market discounts a 10-year revenue CAGR of **22.28%** at WACC 9.5% and 34.5% EBIT margins. Implausible outside of a prolonged multi-decade semiconductor hyper-bubble.
- **Asymmetry (Upside to Bull : Downside to Bear):** -0.53 : 1 (the stock sits 71% above even the most aggressive Bull case).
- **Recommendation:** **PASS** for new capital / **TRIM** for existing holders (HIGH conviction). The stock trades at nearly 3.0x intrinsic value.

---

## 2. Business Quality (Buffett)
- **Economic Moat: Wide (Monopoly status, Unassailable Pricing Power).**
  - Gross margins have held remarkably rock-solid: **48.6%, 52.7%, 50.5%, 51.3%, 51.3%, 52.8%** (FY20–FY25). No competitor exists on the planet capable of commercial EUV lithography.
- **ROIC vs WACC:** FY25 ROIC of **87.1%** vastly exceeds the 9.50% cost of capital.
- **Circle of Competence:** Understandable semiconductor manufacturing physics; highly unpredictable customer ordering panics and geopolitical export bans.

---

## 3. GARP & Valuation Matrix
| Metric | Current (ASML.AS) | 5-Yr Historical Avg | Peer Median (AMAT, LRCX, KLAC) |
|---|---|---|---|
| **EV / EBITDA** | **42.6x** | 33.5x | 22.1x |
| **P/E (Trailing / Forward)** | **57.2x / 28.7x** | 41.0x / 31.0x | 23.5x / 24.1x |
| **P/FCF (SBC-Adjusted)** | **53.6x** | 42.0x | 26.5x |
| **FCF Yield / Owner Earnings Yield** | **1.90% / 1.55%** | 2.50% / 2.10% | 3.90% / 4.20% |
| **PEG Ratio** | **1.12** (`peg_is_valid`: True) | 1.45 | 1.55 |
| **Lynch Ratio** | **0.39** (poor) | 0.65 | 0.85 |
| **ROIC vs WACC** | **87.1% vs 9.50%** | 73.0% vs 9.50% | 35.0% vs 9.0% |
| **Net Cash / (Debt)** | **+€8,931M Net Cash** | +€3,500M | Net Cash |

---

## 4. DCF Scenarios (Model: `02_model.py`)
Valuation executed using an explicit 10-year Free Cash Flow to Firm DCF model with terminal value linked to reinvestment rate (`g / ROIC` where ROIC = 20–35%). Corporate tax rate 18.0%, Netherlands 10y risk-free rate 3.564%, Blume-adjusted beta 1.202, WACC 9.50%, mid-year discounting.

- **Bear Case (25% prob): €316.64 (-79.0% upside).** China immersion DUV export ban enforced; foundry capex pauses; 10-yr revenue CAGR +4.4%; EBIT margin drops to 29.0%; WACC 10.0%, terminal growth 2.0%.
- **Trough Case (35% prob): €444.87 (-70.5% upside).** Normalized mid-cycle growth (+6.6% CAGR); EBIT margin 32.0%; WACC 9.5%, terminal growth 2.5%.
- **Base Case (30% prob): €614.44 (-59.3% upside).** High-NA ramp proceeds for A16/A14 logic nodes; revenue CAGR +9.5%; EBIT margin 34.5%; WACC 9.5%, terminal growth 3.0%.
- **Bull Case (10% prob): €881.61 (-41.6% upside).** Complete High-NA EUV supercycle across logic and advanced 3D DRAM; revenue CAGR +12.0%; EBIT margin 37.0%; WACC 9.0%, terminal growth 3.5%.

---

## 5. The Skeptic's Audit
- **Number Audit:** 16 core metrics verified against SEC Form 20-F XBRL and Euronext filings. Spot price €1,509.60, diluted shares 389.0M, net cash €8,931M, FCF €11,027M confirmed with zero load-bearing errors.
- **Capital Allocation Grade: A-**
  - Buffett $1 Test: Created **€12.97 in market cap per €1 retained** over 2020–2025.
  - Share Repurchases: Retired 30.0M shares (-7.2% share reduction) at favorable historical prices (€550–€750).
  - Balance Sheet: Fortress with €8.93B in net cash.
- **Primary Downside Catalysts & Bear Thesis:**
  1. **China DUV Export Revenue Cliff:** Dutch government licensing curbs and US export controls restrict advanced immersion tools and maintenance, hitting ~30–40% of shipments.
  2. **High-NA Customer Pushback:** TSMC stretching 0.33 NA tools via multi-patterning due to €350M+ tool costs.
  3. **Valuation De-rating:** 1.55% Owner Earnings yield offers zero margin of safety against potential semiconductor capex pauses.

---

## 6. Investor Fit (Singapore Resident, SGD Base)
- **Currency:** EUR-quoted Euronext Amsterdam ordinary shares (`ASML.AS`).
- **Dividend Withholding:** 15% Dutch statutory dividend withholding tax (yield is low at 0.5%, so tax leakage is negligible).
- **0% US Federal Estate Tax:** 100% exempt from US estate tax under 26 USC §2104 (Dutch corporate domicile).
- **Active Portfolio Overlap:** Not currently held in the user's active 19-stock portfolio.

---

## 7. Sources
1. ASML Holding N.V. Form 20-F Annual Report for FY2025 (SEC CIK 0000937966) and Interim 2026 Results (asml.com).
2. Euronext Amsterdam official closing price history for `ASML.AS`.
3. European Central Bank (ECB) 10-year Netherlands Government Bond Yield series (IRS/M.NL.L.L40.CI.0000.EUR.N.Z).
4. Data Layer: `data/fundamentals.json` (as of 2026-10-14, 0 warnings, 0 errors).
5. Executed Valuation Model: `reports/runs/ASML.AS_2026-10-14/02_model.py`.

---

VERDICT:        PASS
AS_OF:          2026-10-14
PRICE:          1509.60 EUR
FAIR_VALUE:     507.35 EUR
UPSIDE:         -66.4%
ENTRY_BELOW:    405.88 EUR
EXIT_ABOVE:     659.56 EUR
CONVICTION:     HIGH
KEY_RISK:       Current price trades at 3x intrinsic value requiring an impossible 22.3% revenue CAGR for a decade amidst China export restrictions
DATA_WARNINGS:  0
