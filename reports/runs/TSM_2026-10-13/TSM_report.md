# Equity Analysis: TSM — Taiwan Semiconductor Manufacturing (ADR)
As of 2026-10-13 · Price 444.35 USD/ADS (1 ADS = 5 shares; financials in NT$) · Template FULL · Run: `reports/runs/TSM_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**Fast Grower with a cyclical overlay.** Revenue grew 24.5% a year FY21–25, but FY23 fell 4.5%. **Why own it:** TSMC makes most of the world's leading-edge chips. Its return on invested capital is about 47%, there has been no dilution in 5 years, and AI demand has it guiding to roughly +40% USD revenue growth in FY26. **What has to happen:** at $444 the market needs about 18–19% a year revenue growth for 10 years. No company with over $50B of revenue has sustained 20%+ for a decade (Mauboussin base rates, secondary source). **What could go wrong:** AI capex pauses for digestion while TSMC's own capex (US$60–64B in FY26) and overseas fabs are locked in. Margins would then fall toward management's 56% gross-margin floor just as the multiple compresses. It's a great business at a price that already assumes the bull case.

## 1. Executive Summary & Expected Value
- **Current Price:** $444.35 · **12-mo change:** +48.3%
- **Bear / Base / Bull / Taiwan tail:** $128.81 (25%) / $283.62 (50%) / $467.48 (20%) / $14.70 (5%). These are the Skeptic's values with beta 1.16. The audited Quant values with beta 1.0 are $141 / $319 / $536.
- **Expected Value (probability-weighted):** **$268.24** (Quant basis: $302.61) → margin of safety **−65.7%** (−46.8%)
- **SBC-adjusted Expected Value:** $268.24. SBC is 0.03% of OCF and makes no difference.
- **Price implies (reverse DCF):** a 17.6–19.3% revenue CAGR for 10 years, about 5.5x TTM revenue. Plausible? Only in the bull case. The price equals the corrected base at an 8.28% implied return, about 3pp over the US 10-yr.
- **Asymmetry:** −0.56
- **Recommendation:** **TRIM** (MEDIUM conviction). This is a valuation trim; the thesis isn't broken. It flips to HOLD only if the bull probability is ≥34% (Quant values) or ≥56% (Skeptic's).

## 2. Business Quality (Buffett)
**Moat: Wide, widening on the evidence.** Gross margin was 64.2% TTM against a 5-yr range topping out at 59.9%. ROIC is 46.8% TTM against a 10.1–10.9% WACC, and incremental ROIC from FY24 to TTM was 79%. Margins are measured off the 2023 trough, though, and customer concentration is rising (top 10 = 78%, HPC = 58%). **Circle of competence:** the technology lead is understandable. Through-cycle earnings and Taiwan geopolitics are not predictable, which is why it carries the cyclical 40% margin of safety despite the wide moat.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 22.5x (TTM, NT$ basis) | UNKNOWN | UNKNOWN (vendor EV currency-mismatched) |
| P/E (ttm / fwd) | 33.4x (34.3x normalised, 40.6x mid-cycle) / 19.9x (unvalidated) | UNKNOWN | 37.8x / 19.4x (unvalidated) |
| P/FCF (SBC-adjusted) | 65.3x (65.3x) | UNKNOWN (5-yr avg FCF margin 22.1%) | UNKNOWN |
| FCF Yield / Owner-Earnings Yield | 1.53% / 1.82% | UNKNOWN | UNKNOWN |
| PEG (or VOID + reason) | 1.14 (passes the gate; historical growth only) | UNKNOWN | UNKNOWN |
| Lynch ratio (g + yield) / PE | 0.90 (0.76 mid-cycle): poor | UNKNOWN | UNKNOWN |
| ROIC vs WACC | 46.8% vs 10.9% | FY24–25 avg 39.3% | UNKNOWN |
| Net debt / Owner earnings | −1.82x (net cash) | UNKNOWN | UNKNOWN |
Only 56% of net income became free cash over FY21–25, because capex runs at 2.2–2.9x depreciation. On owner earnings the stock trades at about 55x.

## 4. DCF Scenarios
WACC is 10.9% (10-yr US Treasury 5.22% from FRED, ERP 5%, beta 1.16 Blume-adjusted from yfinance 1.239). The Quant's 10.2% used beta 1.0 (unsourced). The model uses USD cash flows from USD guidance at constant FX, converted from NT$ per share at ×5 ÷ 32.133. Terminal growth is 3% with terminal ROIC 25%, and terminal value is 55–67% of EV. Valuation uses mid-cycle margins (EBITDA 68%) because current margins are above the 5-yr range. Taiwan risk is an explicit 5% tail valued at net cash, not added to WACC, so it isn't counted twice.
- **Bear (25%): $128.81.** AI-capex digestion; gross margin falls toward 56% and the multiple compresses.
- **Base (50%): $283.62.** FY26 per guidance plus the actual 3Q26 (NT$1,494B), then fading growth at mid-cycle margins.
- **Bull (20%): $467.48.** AI demand stays strong into FY27+ (≥25% growth, gross margin ≥60%).
- **Taiwan tail (5%): $14.70.** Net cash only.

## 5. The Skeptic's Audit
- **Number audit:** 20 checked, 5 failed, with no arithmetic, identity, ADR or unit errors. Four corrections together raised the Quant base +10%:
  - **Risk-free rate:** 5.277% was the 7 Oct ^TNX close, mislabelled. FRED gives 5.22%.
  - **3Q26 revenue:** the actual NT$1,494B (filed in a 6-K on 8 Oct, above the guide) **was missed by the Researcher** and replaces the guide midpoint.
  - **FY26 growth:** the "+40%" guide is in USD but had been applied to NT$ revenue.
  - **Discounting date:** values now run mid-year and roll forward to 13 Oct, less the NT$13 of 2026 dividends a buyer today no longer receives (+7.0%).
  - **The one unresolved item is beta:** 1.0 unsourced vs 1.16 sourced, worth −11% of fair value and below the 15% conviction threshold.
- **Capital Allocation Grade: A−.** ROIC is about 47% against an ~11% hurdle, there has been no dilution in 5 years and no M&A. The $1 test gives **US$8.6 of market value per $1 retained** (end-2020 to end-2025). The minus is the ~US$265B Arizona build, whose returns are unproven. Insider activity: UNKNOWN (foreign private issuer, no Form 4s).
- **Quality of Earnings:** accruals are clean and SBC is negligible. The 2Q26 EPS included a ~NT$2.24 one-off gain from a Vanguard stake, normalised out. Heavy capex means owner earnings are only 0.62x net income.
- **Bear thesis:** AI-capex digestion hits while TSMC's capex and overseas commitments are locked in. Margins revert toward 56% and the multiple compresses at the same time.
- **Primary Downside Catalysts:**
  1. **AI demand digestion or double-ordering.** Signpost: two straight quarters of falling USD revenue q/q, or monthly revenue growth below +10% y/y for 3 months, while capex guidance holds. Inventory days above 95 (87 now) would support it.
  2. **Margin erosion** from the N2 ramp, overseas fabs and the depreciation wave. Signpost: gross margin below 56% or operating margin below 50% in a quarter without a revenue decline, or FY27 capex above 40% of revenue with growth below 15%.
- **Unresolved disagreements (Quant vs Skeptic):**

| Issue | Quant | Skeptic | Effect on base FV |
|---|---|---|---|
| Beta | 1.0 (unsourced) | 1.16 (Blume-adjusted yfinance) | −11.0%; both shown |
| Required MoS | n/a | 30% chosen, 40% alternative | **Orchestrator applies 40%** (new rule: when moat and cyclicality conflict, the higher MoS wins) |
| 1H27 base path | 1H26 × 1.25 | implies a sequential dip after the 3Q beat (mildly conservative) | +1–3% if flat-to-up; not applied |

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-quoted ADR on NT$ earnings, so USD/TWD is a load-bearing input (±10% FX ≈ ±10% value).
- **Dividends:** Taiwan withholding on dividends to a non-resident (rate UNKNOWN in this run; confirm with IBKR). Not US-domiciled, so no 30% US withholding.
- **Estate tax:** the NYSE ADR is issued by a non-US company, so it is likely not US-situs under 26 USC §2104(a). This wasn't verified for ADR depositary structures; confirm.
- **Overlap:** TSMC is also 1.70% of VWRA, and you hold SK Hynix and SK Square directly. Semiconductor/AI exposure is stacked across the portfolio.
- **Tax on selling:** no capital-gains tax, so a trim costs nothing in tax.

## 7. Sources
1. TSMC FY2025 Form 20-F (SEC EDGAR, accn 0001628280-26-025362); 6-K exhibits 1Q26/2Q26 and monthly revenue 6-K of 2026-10-08
2. investor.tsmc.com 2Q26 earnings conference transcript (guidance: 3Q26 US$44.6–45.8B, FY26 "slightly above 40%" USD growth, FY26 capex US$60–64B)
3. SEC XBRL companyfacts (stale, reference only): https://data.sec.gov/api/xbrl/companyfacts/CIK0001046179.json
4. FRED DGS10: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
5. yfinance price history and beta; `data/fundamentals.json` (2026-10-13, net income corrected to the income statement)
6. Mauboussin et al. base rates for sales growth (via secondary sources; flagged)
7. Run files: `01_research.md`, `facts.json`, `02_quant.md`, `02_model.py`, `03_skeptic.md`, `03_rerun.py`

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          444.35 USD
FAIR_VALUE:     268.24 USD
UPSIDE:         -39.6%
ENTRY_BELOW:    160.94 USD
EXIT_ABOVE:     348.71 USD
CONVICTION:     MEDIUM
KEY_RISK:       Price embeds ~18-19%/yr growth for 10 yrs (bull case) while capex and overseas fabs lock in costs before any AI digestion
DATA_WARNINGS:  1
