<!-- pipeline:value-quant -->
# Quant Model & Fundamental Analysis: BATS.L (British American Tobacco p.l.c.)
**As of Date:** 2026-10-14  
**Primary Listing:** London Stock Exchange (LSE) · Currency: GBP  
**Template:** FULL (Operating Company, Profitable)  
**Model:** `reports/runs/BATS.L_2026-10-14/02_model.py`  

---

## 0. Tape Check & Data Integrity (RULE 0 & RULE 1)

### Tape Check (RULE 0)
- **Official Raw Close:** **£41.94** (4,194 pence, yfinance history auto_adjust=False)
- **Vendor Spot Price:** £42.25
- **Trailing P/E:** 14.5x (reported) / 11.6x (diluted TTM EPS £3.61) / ~8.5x on adjusted operating EPS (£3.80+)
- **Forward P/E:** 10.9x
- **52-Week High:** £53.30 · **Drawdown:** -21.3% from 52w peak.
- **Tape / Narrative Alignment:** The tape reflects an established consumer stalwart trading at a deep cyclical/regulatory discount. Market sentiment has been weighed down by the US combustible volume decline, litigation fears around a prospective US FDA menthol ban, and illicit Chinese disposable vapor penetration. The tape is pricing in terminal decay, while the underlying financial statements show £5.64B FCF and >83% gross margins.

### Data Layer Warnings (RULE 1)
`data/fundamentals.json` reports **0 warnings** and **0 errors** for `BATS.L`.
- `quote_currency`: GBP · `financial_currency`: GBP · `fx_to_usd`: 1.3267
- `peg_valid`: True (PEG: 1.4x)
- Note on historical accounting: In FY2023, BAT booked a £27.3B non-cash impairment against its US acquired combustible trademarks (*Newport, Camel*), resetting carrying value to a 30-year amortizable basis. This caused statutory operating profit and GAAP EPS to turn negative in FY2023, but operating cash flow (£10.75B) and dividend capacity were completely unaffected.

---

## 1. Enterprise Value Bridge & Capital Structure
*All figures in GBP Millions unless stated.*

```
EV Bridge:
Market Capitalisation:  £90,189m  (2,150.425m shares @ £41.94)
Total Debt:            £35,063m  (Current borrowings + Long-term bonds)
Less Cash:             -£2,533m  (Cash & cash equivalents)
-----------------------------------------------------------
Net Debt:              £32,530m  (£15.13 per share)
Enterprise Value:     £122,719m
```
- Net Debt covers 36.1% of spot price (£15.13 net debt per share).
- Net Debt / Adjusted EBITDA sits at **~2.45x**, inside management's target corridor of 2.0x–2.5x.

---

## A. Lynch Classification & Category Checks

### Classification: **Stalwart / Cash Cow in Structural Transition**
- **Revenue CAGR (FY21–FY25):** +1.3% (steady low-single digit net revenue growth in constant currency).
- **Combustible vs Smokeless Mix:** Combustibles generate ~81% of group net revenues and ~88% of group operating profit. New Categories (Vuse, glo, Velo) generate £3.4B+ and reached profitability ahead of schedule.
- **Lynch Metrics:**
  - **Lynch Ratio:** `(EPS Growth 2.0% + Dividend Yield 5.84%) / Forward P/E 10.9x` = **0.72**. (Reflects mature low-growth stalwart dynamics).
  - **Net-Cash-Adjusted P/E:** `(£41.94 - (-£15.13)) / £3.61` = **15.8x**.
  - **Inventory & Receivables Check:** Inventory growth is strictly matched to leaf purchasing cycles; receivables turnover is rapid (>12x annually) with negligible credit loss.
  - **PEG Gate:** Forward P/E 10.9x / 8.0% expected earnings growth = 1.36x. `peg_is_valid()` returns `(True, 'ok')`.

---

## B. Business Quality & Buffett Economic Moat

### Moat: **Wide (Stable to Slowly Eroding in Combustibles, Widening in Modern Oral)**
1. **Gross Margin Stability (Pricing Power):**
   - Gross margins across FY21–FY25: **83.5%, 82.9%, 83.0%, 83.5%, 83.5%**.
   - An 83.5% gross margin across economic cycles demonstrates pricing power. When combustible volumes fall 6-8%, BAT raises pack prices 7-10%, driving operating profit higher.
2. **Regulatory Barriers to Entry:**
   - Advertising bans and FDA Premarket Tobacco Application (PMTA) requirements completely prevent new combustible cigarette competitors from ever entering the market.
3. **Owner Earnings & Cash Conversion:**
   - **Net Income:** £7,765m
   - **D&A:** £2,270m
   - **CapEx:** £704m (Capital-light: capex is only 2.6% of revenue)
   - **Owner Earnings:** `£7,765m + £2,270m - £704m` = **£9,331m** ($12.38B USD).
   - **Owner Earnings Yield:** **10.35%** on current market cap!
   - **Free Cash Flow:** **£5,638m** (FCF Yield: **6.25%**).

---

## C. Capital Allocation ($1 Test, Buybacks & Deleveraging)
1. **Buffett $1 Test:** Cumulative retained earnings over 5 years divided into market cap change yields ~1.12x, supported by £2.45/share progressive dividend distributions.
2. **Deleveraging Discipline:**
   - Net debt reduced from peak post-Reynolds acquisition (>£45B) to £32.53B.
   - Successful monetization of partial ITC Limited (India) stake yielded £1.57B net proceeds, dedicated to debt retirement and funding share buybacks.
3. **Share Repurchases:**
   - Resumed £700m program in 2024, expanding into £900m–£1.6B annual buybacks.
   - Repurchases at <11x Forward P/E retire shares at an earnings yield >9.2%, creating per-share intrinsic value accretion.

---

## D. Financial Health & Balance Sheet Resilience
- **Net Debt:** £32.53B.
- **Interest Coverage:** Operating profit £12.55B / Net finance costs ~£1.45B = **8.6x**.
- **Maturity Profile:** Average debt maturity >9.5 years; >85% fixed-rate borrowing, shielding the company from interest rate shocks.
- **Dividend Coverage:** FCF £5.64B comfortably covers annual dividend requirements (~£4.9B) with surplus cash flow funding buybacks and debt paydown.

---

## E. Valuation Model Results (from `02_model.py`)

### 1. DCF Scenario Analysis (10-Year Horizon)
- **Base Revenue:** £27,100m · **Statutory Tax Rate:** 25.0% · **Terminal ROIC:** 15.0%

| Scenario | WACC | Term g | Rev CAGR | EBITDA Margin | Intrinsic / Share | Upside vs £41.94 | Probability | Weighted |
|---|---|---|---|---|---|---|---|---|
| **Bear** | 9.0% | 0.5% | -1.3% | 44.0% | **£24.17** | -42.4% | 25% | £6.04 |
| **Trough** | 8.5% | 1.0% | 0.0% | 46.0% | **£33.89** | -19.2% | 30% | £10.17 |
| **Base** | 8.2% | 1.5% | +1.1% | 48.5% | **£44.33** | +5.7% | 35% | £15.51 |
| **Bull** | 7.8% | 2.0% | +2.2% | 51.0% | **£58.93** | +40.5% | 10% | £5.89 |

- **Probability-Weighted Expected Value:** **£37.62**
- **Margin of Safety at Current Price (£41.94):** **-10.3%**

### 2. Reverse DCF ("What Must Be True?")
At today's price of **£41.94**, running `reverse_dcf()` with WACC 8.2% and terminal growth 1.5% reveals that the market discounts a **10-year revenue CAGR of: +0.54%**.
This is a low bar: if BAT merely achieves flat revenue (+0.5%) via pricing power offsetting combustible volume loss, the stock is fairly valued.

### 3. Sensitivity Grid (WACC × Terminal Growth)
*Intrinsic Value per Share (£)*

| WACC \ g_term | 0.5% | 1.0% | 1.5% | 2.0% |
|---|---|---|---|---|
| **7.5%** | £47.57 | £48.86 | £50.35 | £52.10 |
| **8.0%** | £43.75 | £44.76 | £45.92 | £47.26 |
| **8.2%** | £42.36 | £43.28 | **£44.33** | £45.53 |
| **8.5%** | £40.40 | £41.20 | £42.10 | £43.14 |
| **9.0%** | £37.44 | £38.07 | £38.78 | £39.59 |

---

## F. Singapore Tax Resident Fit (SGD Base)
1. **0% Dividend Withholding Tax:** Unlike US dividend payers (which suffer 30% statutory withholding drag), UK-domiciled ordinary shares incur **0% withholding tax** at source. The full 5.84% dividend yield is retained by a Singapore resident.
2. **0% US Estate Tax Risk:** LSE ordinary shares (`BATS.L`) are non-US situs assets, carrying zero exposure to the US federal estate tax threshold (26 USC §2104).
3. **ADR Fee Avoidance:** Buying ordinary shares on LSE avoids the $0.02–$0.05 per share depositary bank fee charged on `BTI` ADRs.
4. **Currency:** GBP exposure against SGD base.

---

## G. Handoff to Value Skeptic
The quantitative model shows a high owner earnings yield (10.35%) and substantial dividend return (5.84%), but a weighted Expected Value of £37.62 sits -10.3% below spot price due to the heavy net debt burden (£32.53B) and conservative terminal growth assumptions.

**Questions for the Skeptic:**
1. Does the 25% Bear probability adequately capture the regulatory risks of a US menthol ban and illicit disposable vape saturation?
2. Is the capital allocation grade constrained by the historic £45B+ Reynolds acquisition debt?
3. What is the single variable that flips the thesis from HOLD to BUY or PASS?
