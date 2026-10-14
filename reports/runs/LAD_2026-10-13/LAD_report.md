# Equity Analysis: LAD — Lithia Motors, Inc.
As of 2026-10-13 · Price 287.94 USD · Template FULL · Run: `reports/runs/LAD_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**An aggressive automotive dealership consolidator and share cannibal trading at mid-cycle valuation multiples.** Lithia expanded revenue from $13.1B in FY20 to $37.6B in FY25 through relentless dealership acquisitions across the United States and the United Kingdom. **Why own it:** Lithia is the largest automotive retailer in North America, generating high-margin, recession-resilient recurring cash flow from Parts & Service (fixed operations) while management ruthlessly repurchases shares (diluted share count retired by >24% since 2021). **What has to happen:** Lithia must sustain normalized mid-cycle dealership operating margins of 4.0%–4.5% while using its $800M+ in annual free cash flow to pay down corporate debt and opportunistically repurchase undervalued shares. **What could go wrong:** sustained high consumer auto loan interest rates (7%–9%) and declining used vehicle valuations could compress gross profit per unit (GPU) below pre-pandemic levels, squeezing operating cash flows against $5.0B in corporate net debt.

## 1. Executive Summary & Expected Value
- **Current Price:** $287.94 USD · **12-mo change:** +5.2% (52-week range: $242.10 to $348.60).
- **Bear / Base / Bull:** $103.46 (20%) / $323.53 (60%) / $649.93 (20%). Scenarios model explicit 10-year DCF projections isolating floor plan financing from corporate leverage.
- **Expected Value (probability-weighted):** **$344.79 USD** → margin of safety **+16.5%** (upside **+19.7%**).
- **SBC-adjusted Expected Value:** **$341.50 USD** (deducting ~$70M annual stock-based compensation).
- **Price implies (reverse DCF):** a constant 10-year revenue CAGR of just ~2.5% at mid-cycle 4.2% operating margins. The market has fully absorbed post-COVID margin normalization.
- **Asymmetry (upside to Bull : downside to Bear):** 1.96 : 1 ($361.99 upside to Bull vs $184.48 downside to Bear).
- **Recommendation:** **HOLD** (HIGH conviction). As an existing holding, the market price ($287.94) sits between the required 25% margin-of-safety entry threshold ($258.59) and Expected Value ($344.79).

## 2. Business Quality (Buffett)
**Moat: Narrow, widening via procurement and software scale.** While individual vehicle sales are price-competitive, Lithia's massive nationwide retail network creates significant economies of scale in finance and insurance (F&I) commissions, nationwide parts distribution, and customer acquisition. Crucially, **Fixed Operations (parts, maintenance, warranty, and collision repair) generates >45% of total gross profit at 50%+ gross margins**, providing an indispensable cash flow annuity during retail vehicle sales downcycles. **ROIC vs WACC:** Mid-cycle ROIC of 10.7%–12.0% covers its 10.75% cost of capital. **Circle of competence:** high predictability in automotive dealership economics and consumer service behavior.

## 3. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (AN, PAG, ABG, GPI) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA (ex-floor plan) | 6.8x | 7.5x | 6.5x |
| P/E (ttm / fwd) | 9.5x / 6.9x | 7.8x | 8.2x / 7.5x |
| PEG Ratio | **0.54** (attractive under GARP) | 0.65 | 0.75 |
| Normalized FCF Yield | 13.5% (on $850M mid-cycle FCF) | 12.0% | 11.5% |
| Operating Margin | 4.2% (mid-cycle baseline) | 5.4% | 4.5% |
| ROIC vs WACC | 10.7% vs 10.75% | 15.2% | 11.0% |
| Net Corporate Debt / EBITDA | 2.5x ($5.0B debt / $2.0B EBITDA) | 2.2x | 2.4x |
*Note on Ownership: Data layer vendor report of 116.2% institutional ownership is an acknowledged vendor data artifact resulting from overlapping 13F filing aggregations.*

## 4. DCF Scenarios
Valuation executed via `02_model.py`. The model isolates ~$4.8B in floor plan notes payable (treated as operating working capital collateralized 1:1 by vehicle inventory) and evaluates the equity against $5.00B in net corporate debt ($227.45/share). WACC is 10.75% (US 10y Treasury yield 5.22%, Blume-adjusted beta 1.180, 5.0% ERP). Terminal growth rate is 2.5%, terminal ROIC is 12.0%, and terminal value represents 41.6% of enterprise value in Base.
- **Bear (20%): $103.46 USD.** Affordability pressures deepen; GPU contracts; operating margin compresses to 3.5%; 10-year revenue CAGR 1.0%; WACC 11.75%; equity value $2.27B.
- **Base (60%): $323.53 USD.** Mid-cycle operating margins hold at 4.2%; network consolidation CAGR 3.5%; fixed ops cash flow cushions cycles; WACC 10.75%; equity value $7.11B.
- **Bull (20%): $649.93 USD.** Fixed operations expand rapidly; UK Pendragon synergies exceed expectations; operating margin expands to 4.8%; 10-year revenue CAGR 5.5%; WACC 9.75%; equity value $14.29B.

## 5. The Skeptic's Audit
- **Number audit:** 10 financial items audited against SEC filings (10-K accn 0001023128-26-000018 and 10-Q Q2-26). Key confirmations:
  1. *Floor Plan Debt Isolation:* Confirmed floor plan notes payable (~$4.8B) are directly collateralized by vehicle inventory. Non-floor-plan corporate funded debt is $5.45B less $0.45B cash = $5.00B net corporate debt.
  2. *Cannibal Share Retirement:* Verified that diluted share count fell from 29.0M (FY21) to 21.98M (Q2-26), a massive 24.2% reduction. Over $960M in share repurchases was executed in FY25 alone.
  3. *Vendor Ownership Artifact:* Confirmed vendor institutional ownership flag is a vendor double-counting artifact.
- **Capital Allocation Grade: A-**
  - Buffett $1 test generated $1.19 in market value per $1 retained over FY20–FY25 despite severe post-COVID multiple compression.
  - Exemplary counter-cyclical share repurchases retiring nearly a quarter of company shares at depressed valuations.
  - Highly disciplined bolt-on dealership M&A executed at 3x–5x normalized EBITDA.
- **Quality of Earnings:** High. Fixed operations gross profit covers more than 70% of total dealership SG&A costs.
- **Bear thesis:** Sustained high auto loan interest rates and tighter lender credit standards squeeze consumer vehicle purchasing power, driving gross profit per unit (GPU) down toward pre-pandemic troughs while $5.0B in corporate debt requires steady cash servicing.
- **Primary Downside Catalysts:**
  1. *Automotive GPU Deterioration:* Combined new and used vehicle GPU falling below $1,900 in quarterly reports.
  2. *Subprime Auto Loan Delinquency Spikes:* Industry-wide credit tightening restricting dealership customer financing approvals.
- **Unresolved disagreements (Quant vs Skeptic):** None; Skeptic validated the corporate vs floor plan debt separation.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-denominated US domestic equity; direct exposure to USD/SGD exchange rate fluctuations.
- **Dividends:** Dividend yield is low (~0.8%), limiting drag from 30% US dividend withholding tax.
- **Estate Tax:** US-domiciled equity; subject to US federal estate tax under 26 USC §2104 above the US$60k threshold.
- **Portfolio Weight:** Currently held in active portfolio. Recommendation is to hold the position to capture ongoing cannibal share accretion and consolidation cash flows.

## 7. Sources
1. Lithia Motors, Inc. FY2025 Form 10-K Annual Report (SEC accn 0001023128-26-000018).
2. Lithia Motors, Inc. Q2 2026 Form 10-Q Quarterly Report (SEC accn 0001023128-26-000051).
3. Lithia Motors Q2 2026 Investor Presentation and Earnings Release (July 2026).
4. FRED US 10-Year Treasury Yield (DGS10, October 2026).
5. Quantitative valuation model and DCF run script (`reports/runs/LAD_2026-10-13/02_model.py`).

VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          287.94 USD
FAIR_VALUE:     344.79 USD
UPSIDE:         19.7%
ENTRY_BELOW:    258.59 USD
EXIT_ABOVE:     448.23 USD
CONVICTION:     HIGH
KEY_RISK:       High-interest rate environment tightens consumer auto affordability while $5.0B corporate debt requires steady cash flow
DATA_WARNINGS:  1
