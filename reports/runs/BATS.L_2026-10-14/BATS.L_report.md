# Equity Analysis: BATS.L — British American Tobacco p.l.c.
As of 2026-10-14 · Price 41.94 GBP (4,194 pence) · Template FULL · Run: `reports/runs/BATS.L_2026-10-14/`

## 0. Two-Minute Drill (Lynch)
**A high-yielding defensive Stalwart / Cash Cow transitioning from combustible cigarettes to smokeless New Categories.** 
- **Why own it:** BATS is a global consumer staple generating £5.64B in annual Free Cash Flow and £9.33B in Owner Earnings, backed by an unyielding 83.5% gross margin. It pays a secure, progressive annual dividend of **£2.45 per share (5.84% yield)** that incurs **0% dividend withholding tax** and **0% US estate tax risk** for a Singapore tax resident. Management has reduced net debt to £32.53B (~2.45x net debt/EBITDA) and expanded share repurchases to £900m–£1.6B annually at attractive sub-11x Forward P/E multiples.
- **What has to happen:** Pricing power (+6% to +8% per pack) must continue to offset combustible volume declines (-5% to -8%), while New Categories (Vuse vapor, glo heated tobacco, Velo modern oral pouches) continue to scale profitably to deliver ~1.0% consolidated net revenue CAGR.
- **What could go wrong:** Accelerated combustible volume decline in the US (Reynolds American), federal finalization of an FDA menthol cigarette ban threatening Newport (which generates ~50% of US profit), or persistent market share losses to illicit disposable vapes imported from China. With £32.53B in net debt, a severe cash flow shock could impair dividend growth.

---

## 1. Executive Summary & Expected Value
- **Current Price:** £41.94 (official raw close; vendor quote £42.25) · **52-Week High:** £53.30 (-21.3% drawdown).
- **Valuation Scenarios:** Bear £24.17 (25%) / Trough £33.89 (35%) / Base £44.33 (30%) / Bull £58.93 (10%).
- **Probability-Weighted Expected Value:** **£37.10** → margin of safety: **-11.5%** vs spot price.
- **Base Case Fair Value:** **£44.33** (+5.7% upside).
- **Price Implies (Reverse DCF):** At £41.94, the market discounts a 10-year revenue CAGR of just **+0.54%** at WACC 8.2% and terminal growth 1.5%.
- **Verdict:** **HOLD** (High conviction). The stock is fairly valued for current holders seeking a reliable 5.84% tax-free yield. New capital should await a wider margin of safety below **£35.00**.

---

## 2. Business Quality (Buffett)
- **Economic Moat: Wide (Stable to Slowly Eroding in Combustibles, Widening in Modern Oral).**
  - **Pricing Power:** Gross margins have held remarkably constant across economic cycles: **83.5%, 82.9%, 83.0%, 83.5%, 83.5%** (FY21–FY25 TTM). Inelastic consumer addiction and brand loyalty allow BAT to routinely raise pack prices by 7-10%, more than compensating for secular volume declines.
  - **Barriers to Entry:** Total global marketing bans and FDA PMTA regulatory requirements make it impossible for new combustible cigarette competitors to emerge.
- **Owner Earnings vs Capex:**
  - Highly capital-light operations: Capex of £704m represents only 2.6% of revenue.
  - **Owner Earnings:** £9,331m ($12.38B USD), translating to an **Owner Earnings Yield of 10.35%** on market cap.
  - Free Cash Flow: £5,638m (6.25% FCF yield).

---

## 3. GARP & Valuation Matrix

| Metric | BATS.L Current | 5-Yr Historical Avg | Industry Peer Median |
|---|---|---|---|
| **EV / EBITDA** | **7.2x** | 7.8x | 10.5x (PMI, MO, Imperial) |
| **P/E (Trailing / Forward)** | **14.5x / 10.9x** | 11.5x / 9.8x | 16.5x / 14.2x |
| **Owner Earnings Yield** | **10.35%** | 9.80% | 7.50% |
| **Free Cash Flow Yield** | **6.25%** | 7.10% | 6.80% |
| **Dividend Yield** | **5.84%** (£2.45/sh) | 6.80% | 5.20% |
| **Lynch Ratio** | **0.72** | 0.85 | n/a |
| **Net Cash / (Debt) per Share**| **-£15.13** (Net debt £32.53B) | -£18.50 | n/a |
| **Net-Cash-Adjusted P/E** | **15.8x** | 17.2x | n/a |
| **PEG Ratio** | **1.4x** (`peg_is_valid`: True) | 1.3x | 1.8x |

---

## 4. DCF Scenarios (Model: `02_model.py`)
Valuation is conducted using an explicit 10-year Free Cash Flow to Firm DCF model with terminal value linked to reinvestment rate (`g / ROIC` where ROIC = 15.0%). All scenarios incorporate UK corporate tax rate of 25.0% and mid-year discounting.

- **Bear Case (25% prob): £24.17 (-42.4% upside).** FDA enforces US menthol ban; US volume decay accelerates to -10%; illicit vapes persist. Revenue decays at -1.3% CAGR, EBITDA margin drops to 44.0%, WACC 9.0%, terminal growth 0.5%.
- **Trough Case (35% prob): £33.89 (-19.2% upside).** Combustible pricing perfectly neutralizes volume declines; revenue growth is 0.0% CAGR; EBITDA margin 46.0%, WACC 8.5%, terminal growth 1.0%.
- **Base Case (30% prob): £44.33 (+5.7% upside).** New Categories (Velo, Vuse) scale; pricing power intact; consolidated revenue grows at +1.1% CAGR; EBITDA margin 48.5%, WACC 8.2%, terminal growth 1.5%.
- **Bull Case (10% prob): £58.93 (+40.5% upside).** Federal crackdown seizes illicit Chinese disposable vapes, driving users to Vuse; Velo modern oral pouches expand rapidly; revenue grows at +2.2% CAGR; EBITDA margin 51.0%, WACC 7.8%, terminal growth 2.0%.

---

## 5. The Skeptic's Audit
- **Number Audit:** 18 distinct metrics verified from primary statements with zero discrepancies above 1%. Spot price £41.94, shares 2,150.4m, net debt £32.53B, FCF £5.64B, dividend £2.45/share confirmed.
- **Capital Allocation Grade: B+.**
  - Legacy Reynolds American acquisition in 2017 burdened the balance sheet, resulting in the non-cash £27.3B write-down in FY2023.
  - However, modern execution is disciplined: net debt reduced to 2.45x EBITDA, partial ITC India stake monetization yielded £1.57B dedicated to debt paydown, progressive dividend maintained for 25+ consecutive years, and buybacks resumed below 11x Forward P/E.
- **Quality of Earnings:** High cash conversion (FCF is ~73% of net income; Owner Earnings exceed net income by £1.57B due to low maintenance capex of £704m vs D&A of £2,270m).
- **Primary Downside Catalysts & Bear Thesis:**
  1. **FDA Menthol Ban Implementation:** Newport generates ~50% of Reynolds' profit. A sudden ban without grandfathering would trigger an immediate valuation de-rate toward £24/share.
  2. **Illicit Disposable Vape Proliferation:** Continued influx of cheap, flavored Chinese disposables evading US customs eroding youth recruitment into legal nicotine categories.
  3. **High Leverage in a Higher-for-Longer World:** £32.53B net debt limits capital allocation flexibility if combustible cash generation falters.

---

## 6. Investor Fit (Singapore Resident, SGD Base)
- **0% Dividend Withholding Tax:** UK-incorporated equities listed on the LSE incur **0% withholding tax** on dividends paid to non-resident individual investors. The full 5.84% yield flows directly to the Singapore investor without the 30% IRS tax drag incurred on US equities (like Altria or Philip Morris).
- **0% US Estate Tax Risk:** Unlike US-domiciled equities or ADRs which trigger US federal estate tax under 26 USC §2104(a) above US$60,000, LSE ordinary shares (`BATS.L`) are 100% exempt from US estate tax.
- **ADR Fee Elimination:** Holding primary LSE shares avoids the $0.02–$0.05 per share depositary bank fee levied on `BTI` ADR holders.
- **Currency:** GBP exposure vs SGD base.

---

## 7. Sources
1. British American Tobacco p.l.c. Annual Reports & Accounts (FY2021–FY2024) and 2025/2026 Interim Results (bat.com).
2. London Stock Exchange (LSE) official closing price history for ticker `BATS.L`: https://www.londonstockexchange.com/stock/BATS/british-american-tobacco-p-l-c/
3. US Food and Drug Administration (FDA) Center for Tobacco Products (CTP) regulatory filings and PMTA guidance: https://www.fda.gov/tobacco-products
4. Data Layer: `data/fundamentals.json` (as of 2026-10-14, 0 warnings, 0 errors).
5. Valuation Model: `reports/runs/BATS.L_2026-10-14/02_model.py` and methodologies library `methodologies/valuation.py`.

---

VERDICT:        HOLD
AS_OF:          2026-10-14
PRICE:          41.94 GBP
FAIR_VALUE:     37.10 GBP
UPSIDE:         -11.5%
ENTRY_BELOW:    35.00 GBP
EXIT_ABOVE:     52.00 GBP
CONVICTION:     HIGH
KEY_RISK:       US combustible volume decline acceleration and prospective FDA menthol ban on Newport
DATA_WARNINGS:  0
