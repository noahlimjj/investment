# Equity Analysis: INCY — Incyte Corporation
As of 2026-10-13 · Price 108.95 USD · Template FULL · Run: `reports/runs/INCY_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**A commercial biopharma Stalwart trading at peak pre-patent-cliff valuation multiples.** Incyte grew revenue at a 14.0% CAGR from FY20 to FY25 ($5.14B in FY25), driven by its core myelofibrosis therapy Jakafi and the dermatology launch of Opzelura cream. **Why own it:** Incyte is a highly profitable biopharma with unencumbered cash generation ($1.41B OCF in FY25), an unblemished fortress balance sheet with $3.10B in net cash ($15.51/share) and $0 funded debt, and commercial momentum in Opzelura. **What has to happen:** to justify today's $108.95 price tag, Incyte's non-Jakafi pipeline (Opzelura, Niktimvo, and mutant CALR antibodies) must generate over $3.5B in peak revenue by 2031 to completely offset the patent cliff. **What could go wrong:** Jakafi represents over 60% of total revenue ($3.2B) and loses primary US patent exclusivity in late 2028; generic erosion post-2028 will cut Jakafi revenue by 60%–70%, creating a multi-billion-dollar revenue gap that Opzelura alone cannot fill.

## 1. Executive Summary & Expected Value
- **Current Price:** $108.95 USD · **12-mo change:** +83.2% (52-week range: $58.10 to $112.45).
- **Bear / Base / Bull:** $44.31 (25%) / $71.42 (55%) / $128.66 (20%). Scenarios model explicit 10-year DCF projections directly incorporating post-2028 generic erosion curves.
- **Expected Value (probability-weighted):** **$76.09 USD** → margin of safety **-43.2%** (downside **-30.2%**).
- **SBC-adjusted Expected Value:** **$74.20 USD** (deducting ~$285M annual SBC dilution).
- **Price implies (reverse DCF):** flawless pipeline execution requiring non-Jakafi commercial products to reach >$3.5B in peak sales by 2031 while sustaining operating margins above 25% through the patent cliff.
- **Asymmetry (upside to Bull : downside to Bear):** 0.31 : 1 ($19.71 upside to Bull vs $64.64 downside to Bear).
- **Recommendation:** **PASS** (HIGH conviction). The stock trades at a 43.2% premium over Expected Value ($76.09) and offers zero margin of safety ahead of its 2028 patent cliff.

## 2. Business Quality (Buffett)
**Moat: Narrow, narrowing toward 2028 patent expiry.** Incyte holds strong regulatory and clinical moats in myeloproliferative neoplasms (Jakafi) and dermatology (Opzelura). However, pharmaceutical moats are legally finite: Jakafi's US composition-of-matter exclusivity expires in late 2028, after which generic ruxolitinib will enter the market. **ROIC vs WACC:** Current ROIC of 16.5% exceeds its 8.50% cost of capital, but ROIC will compress sharply in 2029 during generic onset. **Circle of competence:** high predictability in on-market commercial oncology/dermatology sales; medium predictability regarding Phase 3 pipeline replacement timing.

## 3. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (BIIB, GILD, REGN, VRTX) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 11.2x | 13.5x | 12.0x |
| P/E (ttm / fwd) | 13.9x / 12.5x | 18.0x | 14.5x / 13.2x |
| PEG Ratio | 0.95 (valid historically, but deceptive pre-LOE) | 1.30 | 1.20 |
| Normalized FCF Yield | 5.5% (on $1.2B FCF) | 5.7% | 6.2% |
| Net Cash / Market Cap | 14.2% ($3.10B net cash) | 12.5% | 8.5% |
| ROIC vs WACC | 16.5% vs 8.50% | 12.2% | 15.0% |
| Net Debt / EBITDA | Net Cash ($0 Funded Debt) | Net Cash | Net Cash |
*Note on Ownership: Data layer vendor report of 103.4% institutional ownership is an acknowledged vendor data artifact resulting from overlapping institutional filings.*

## 4. DCF Scenarios
Valuation executed via `02_model.py`. The model explicitly projects the late-2028 Jakafi patent cliff, modeling generic erosion in Years 4–5 (2029–2030) followed by pipeline recovery. WACC is 8.50% (US 10y Treasury yield 5.22%, Blume-adjusted beta 0.650, 5.0% ERP). Terminal growth rate is 2.5%, terminal ROIC is 12.0%, and terminal value represents 47.2% of enterprise value in Base.
- **Bear (25%): $44.31 USD.** Opzelura plateaus at $1.4B; Jakafi generic cliff is severe (-25% Y4, -18% Y5); operating margin drops to 14%–16%; WACC 9.25%; equity value $8.85B.
- **Base (55%): $71.42 USD.** Opzelura reaches $2.0B peak; pipeline adds $1.2B; Jakafi contracts to $400M by 2035; operating margin stabilizes at 22%; WACC 8.50%; equity value $14.27B.
- **Bull (20%): $128.66 USD.** Opzelura expands to $2.8B; CALR antibody becomes a $2.0B blockbuster; operating margin holds >25%; WACC 7.75%; equity value $25.70B.

## 5. The Skeptic's Audit
- **Number audit:** 10 financial items audited against SEC filings (10-K accn 0000879169-26-000014 and 10-Q Q1-26). Key confirmations:
  1. *Net Cash Reconciliation:* Confirmed $3,097.8M in cash and marketable securities with $0 in funded corporate debt, providing $15.51 per share in tangible liquidity.
  2. *ASR Share Reduction:* Verified management executed a $2.0B Accelerated Share Repurchase in 2024, retiring 15.4M shares at an attractive valuation.
  3. *Patent Expiry Timing:* Confirmed primary composition-of-matter patent protection for Jakafi expires in Q4 2028.
- **Capital Allocation Grade: B+**
  - Buffett $1 test generated $1.41 in market value per $1 retained over FY20–FY25.
  - Excellent balance sheet discipline with $0 in funded debt.
  - Highly opportunistic $2.0B buyback execution in 2024 retiring shares below intrinsic value.
- **Quality of Earnings:** High cash conversion, but FY25 net income ($1.29B) reflects peak pre-patent-cliff profitability.
- **Bear thesis:** The Jakafi replacement deficit. Jakafi represents over $3.2B of revenue. Payer utilization restrictions on topical JAK inhibitors cap Opzelura's commercial peak at $1.5B, leaving an unbridgeable revenue deficit that compresses operating profits by >50% post-2028.
- **Primary Downside Catalysts:**
  1. *Opzelura Quarterly Deceleration:* Sales growth slowing below 15% YoY in upcoming quarterly prints.
  2. *Jakafi Generic Patent Settlements:* Generic filers securing early entry dates ahead of Q4 2028.
- **Unresolved disagreements (Quant vs Skeptic):** None; Skeptic verified that the DCF model properly discounts the post-2028 LOE cliff.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-denominated US domestic equity; direct exposure to USD/SGD fluctuations.
- **Dividends:** Zero dividend payout (reinvesting cash into pipeline R&D), so no dividend withholding drag.
- **Estate Tax:** US-domiciled equity; subject to US federal estate tax under 26 USC §2104 above the US$60k threshold.
- **Portfolio Status:** Unheld. Recommendation is to PASS; avoid committing fresh capital at peak multiples ahead of a major patent cliff.

## 7. Sources
1. Incyte Corporation FY2025 Form 10-K Annual Report (SEC accn 0000879169-26-000014).
2. Incyte Corporation Q1 2026 Form 10-Q Quarterly Report (SEC accn 0000879169-26-000026).
3. Incyte Corporation Q2 2026 Earnings Presentation (July 2026).
4. FRED US 10-Year Treasury Yield (DGS10, October 2026).
5. Quantitative valuation model and DCF run script (`reports/runs/INCY_2026-10-13/02_model.py`).

VERDICT:        PASS
AS_OF:          2026-10-13
PRICE:          108.95 USD
FAIR_VALUE:     76.09 USD
UPSIDE:         -30.2%
ENTRY_BELOW:    60.87 USD
EXIT_ABOVE:     98.91 USD
CONVICTION:     HIGH
KEY_RISK:       Price requires flawless pipeline execution to offset the late-2028 Jakafi patent cliff (>60% of revenue)
DATA_WARNINGS:  1
