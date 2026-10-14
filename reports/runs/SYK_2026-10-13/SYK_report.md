# Equity Analysis: SYK — Stryker Corporation
As of 2026-10-13 · Price 283.71 USD · Template FULL · Run: `reports/runs/SYK_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**An elite medical-technology Stalwart priced as an infallible high-growth compounder.** Stryker has grown reported revenue at 11.8% annualized from FY20 to FY25 (approximately 9.0% organic), driven by its market-leading Mako surgical robotics and orthopedic implants. **Why own it:** Stryker holds durable #1 and #2 positions across joint replacement, neurotechnology, and hospital capital equipment, supported by deep surgeon switching costs, proprietary robotics workflows, and consistent mid-teens adjusted EPS growth. **What has to happen:** to justify its current $283.71 price tag, Stryker must sustain a constant 10.2% revenue CAGR for a full decade at 24% EBITDA margins while successfully scaling its $4.8B Inari Medical acquisition and managing a major CEO transition at year-end 2026. **What could go wrong:** serial acquisitions ($14.1B spent in FY20–FY25) have yielded $1.7B in cumulative impairments and pushed net debt to $11.5B; if peripheral vascular manufacturing issues linger or robotic competitors (Zimmer's ROSA, J&J's VELYS) slow Mako's momentum, organic growth will fade toward 5%, triggering an overdue multiple contraction from 29x trailing GAAP P/E toward mature medtech norms.

## 1. Executive Summary & Expected Value
- **Current Price:** $283.71 USD · **12-mo change:** -22.3% (down from $365.10; 52-week range $269.75 to $388.35).
- **Bear / Base / Bull:** $131.41 (20%) / $209.13 (65%) / $304.40 (15%). Scenarios reflect explicit 10-year DCF projections fading organic growth from ~9% toward terminal rates.
- **Expected Value (probability-weighted):** **$207.87 USD** → margin of safety **-36.5%** (downside **-26.7%**).
- **SBC-adjusted Expected Value:** **$205.50 USD** (deducting ~$200M annual SBC dilution).
- **Price implies (reverse DCF):** a constant 10.20% revenue CAGR for 10 years at base margins/capex (reaching $68.3B in revenue by Year 10), or a flat EBITDA margin of 30.3% (vs 5-year average of 23.8%). Implied IRR at spot is just 7.54% against an 8.9% cost of capital.
- **Asymmetry (upside to Bull : downside to Bear):** 0.14 : 1 ($20.69 upside to Bull vs $152.30 downside to Bear).
- **Recommendation:** **TRIM** (HIGH conviction). The current stock price ($283.71) exceeds the sell discipline exit threshold of $270.23 (EV × 1.30).

## 2. Business Quality (Buffett)
**Moat: Wide, stable.** High surgeon switching costs (training, procedural habits, instrument ergonomics), hospital procurement contracts, and proprietary robotic lock-in (Mako software and cutting guides) create exceptional customer stickiness. **ROIC vs WACC:** Underlying return on invested capital of 12.9%–14.3% comfortably exceeds the 8.9% cost of capital. However, heavy acquisition goodwill ($18.8B on balance sheet) depresses reported balance-sheet capital turnover. **Circle of competence:** high predictability in non-discretionary surgical procedures and orthopedic demographics; medium predictability regarding serial M&A capital deployment.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median (ZBH, MDT, BSX) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 18.0x (TTM segment EBITDA) | 20.5x | 14.5x |
| P/E (ttm / fwd) | 29.4x GAAP / 18.9x adj. fwd | 32.0x GAAP | 22.0x / 16.5x |
| P/FCF (SBC-adjusted) | 24.5x (TTM FCF $4.45B) | 26.2x | 18.5x |
| FCF Yield / Owner-Earnings Yield | 4.1% / 4.0% | 3.8% | 5.2% |
| PEG Gate & PEG | Valid; PEG = 1.77 (fwd adj P/E 18.9 / 10.7% growth) | 2.10 | 1.85 |
| Lynch Ratio (g + yield) / P/E | 0.63 (poor; dividend yield 1.24% + 10.7% growth) | 0.55 | 0.60 |
| ROIC vs WACC | 12.9% vs 8.90% | 12.5% | 9.8% |
| Net debt / Owner earnings | 2.6x ($11.47B net debt / $4.45B owner earnings) | 2.4x | 2.1x |

## 4. DCF Scenarios
Valuation executed via `02_model.py`. WACC is 8.90% (US 10y Treasury yield 5.22%, Blume-adjusted beta 0.736, 5.0% ERP). Terminal growth rate is 3.5%, terminal ROIC is 12.9%, and terminal value constitutes 56% of enterprise value in Base.
- **Bear (20%): $131.41 USD.** Organic growth slows to 4.7% CAGR; Inari and vascular disruptions persist; EBITDA margin compresses to 22.0%; terminal growth 3.0%; equity value $50.7B.
- **Base (65%): $209.13 USD.** Organic growth fades from 8.8% to 3.5% (10-yr revenue CAGR 6.1%); EBITDA margin holds at 23.8%; tax rate 17.3%; equity value $80.7B.
- **Bull (15%): $304.40 USD.** Inari scales successfully; 10-yr revenue CAGR 8.0%; EBITDA margin expands to 27.4%; terminal growth 4.0%; equity value $117.5B.

## 5. The Skeptic's Audit
- **Number audit:** 12 financial statement items audited against SEC filings (10-K accn 0000310764-26-000017 and 10-Q Q2-26). Key confirmations:
  1. *Loaner Instrument D&A:* Confirmed that cash-flow D&A ($3,678M) was properly used rather than the larger SEC facts tag ($4,055M), which included ~$377M of loaner instrument amortisation whose replacement spend is already embedded in OCF.
  2. *Net Debt Reconciliation:* Net debt established at $11,466M (total debt $14,942M less cash $3,391M and short-term investments $85M).
  3. *Capex Verification:* Confirmed that an SEC facts capex warning was a false positive resulting from a $750M short-term investment purchase.
- **Capital Allocation Grade: C+**
  - Serial M&A deployed $14.1B across FY20–FY25, consuming 76% of cumulative free cash flow.
  - While acquisitions expanded MedSurg capabilities, cumulative impairments reached $1.72B (17.4% of deal capital), including the severe write-down and sale of Spinal Implants.
  - Share repurchases were zero over the 5-year period while gross debt expanded to $14.9B.
- **Quality of Earnings:** Moderate. A persistent 55% spread exists between GAAP EPS ($9.66) and guided adjusted EPS ($15.025), driven by perpetual amortization of acquisition intangibles.
- **Bear thesis:** The serial acquisition treadmill stalls as integration friction and regulatory scrutiny increase. As hospital robotics competition closes the gap on Mako and peripheral vascular manufacturing issues drag into 2027, organic growth slows toward 4%–5%, deflating Stryker's premium valuation multiple toward 15x–16x.
- **Primary Downside Catalysts:**
  1. *Peripheral Vascular Remediation (Q3/Q4 2026 Results):* Continued manufacturing headwinds or supply constraints in peripheral vascular lines.
  2. *CEO Transition (Year-End 2026):* New management resetting long-term financial targets or taking restructuring/goodwill impairments.
- **Unresolved disagreements (Quant vs Skeptic):** None; Skeptic highlighted tax rate sensitivity (Base falls to $194.46 under a normalized 22.5% effective tax rate).

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-denominated US large-cap equity; direct exposure to USD/SGD fluctuations.
- **Dividends:** Dividend yield is modest (1.24%); subject to 30% US dividend withholding tax for Singapore tax residents.
- **Estate Tax:** US-domiciled equity; subject to US federal estate tax under 26 USC §2104 above the US$60k statutory threshold.
- **Portfolio Weight:** Currently held in active portfolio. Recommended action is to trim exposure, locking in gains given the 36.5% valuation premium over Expected Value.

## 7. Sources
1. Stryker Corporation FY2025 Form 10-K Annual Report (SEC accn 0000310764-26-000017).
2. Stryker Corporation Q2 2026 Form 10-Q Quarterly Report (SEC accn 0000310764-26-000045).
3. Stryker Q2 2026 Earnings Release and Guidance Presentation (July 2026).
4. FRED US 10-Year Treasury Constant Maturity Yield (DGS10, October 2026).
5. Quantitative valuation model and DCF run file (`reports/runs/SYK_2026-10-13/02_model.py`).

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          283.71 USD
FAIR_VALUE:     207.87 USD
UPSIDE:         -26.7%
ENTRY_BELOW:    166.30 USD
EXIT_ABOVE:     270.23 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts ~10% revenue CAGR for a decade while M&A returns lag and peripheral vascular issues persist
DATA_WARNINGS:  0
