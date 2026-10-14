# Equity Analysis: BABA — Alibaba Group Holding Limited
As of 2026-10-13 · Price 110.53 USD · Template FULL · Run: `reports/runs/BABA_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**A former Fast Grower turned low-growth Stalwart enjoying a sentiment-driven stimulus rebound.** Alibaba recently rallied +38% from its 52-week lows to $110.53 following aggressive Chinese central bank monetary stimulus announcements. **Why own it:** Alibaba remains China's dominant digital commerce ecosystem (>1 billion active consumers across Taobao and Tmall), the country's #1 enterprise cloud provider, and a shareholder-friendly capital allocator that retired 12.5% of its share count via buybacks alongside a ~3.0% dividend yield. **What has to happen:** to justify today's $110.53 price tag, Alibaba must generate an 11.5% constant revenue CAGR for ten consecutive years at 12% operating margins while expanding Cloud Intelligence margins to 15% and halting domestic e-commerce market share erosion. **What could go wrong:** domestic commerce is structurally pressured by PDD Holdings' manufacturer-direct pricing and ByteDance's Douyin livestreaming; group operating income fell from peak CNY 140.9B (FY25) to CNY 50.2B in FY26 as Taobao sacrificed merchant fees to defend volume, while gross cash ($43B) is substantially offset by total debt ($38B), leaving a modest net cash cushion of just $4.94B ($2.05/ADS).

## 1. Executive Summary & Expected Value
- **Current Price:** $110.53 USD · **12-mo change:** +38.2% (from $79.98; down -65.2% from all-time peak of $317.14).
- **Bear / Base / Bull:** $35.78 (25%) / $69.58 (55%) / $126.77 (20%). Scenarios reflect explicit 10-year DCF modeling incorporating realistic Chinese macroeconomic growth and competitive platform pressures.
- **Expected Value (probability-weighted):** **$72.57 USD** → margin of safety **-52.3%** (downside **-34.3%**).
- **SBC-adjusted Expected Value:** **$70.80 USD** (deducting ~$1.67B annual SBC cash drag).
- **Price implies (reverse DCF):** a constant 11.5% revenue CAGR for 10 years at base operating margins (12.0%), or an immediate, permanent expansion in group operating margin to 19.5% on base growth (vs 5.0% reported in FY26). The tape is discounting an uninterrupted fundamental boom unsupported by competitive data.
- **Asymmetry (upside to Bull : downside to Bear):** 0.22 : 1 ($16.24 upside to Bull vs $74.75 downside to Bear).
- **Recommendation:** **TRIM** (HIGH conviction). The market price ($110.53) trades 17% above the sell discipline exit threshold of $94.34 (EV × 1.30).

## 2. Business Quality (Buffett)
**Moat: Wide, but Narrowing under intense competitor siege.** Alibaba retains formidable consumer network effects in Taobao/Tmall and mission-critical cloud infrastructure lock-in. However, pricing power in digital advertising and merchant take-rates has degraded as merchants diversify marketing budgets to Douyin and low-cost sellers migrate to Pinduoduo. **ROIC vs WACC:** FY26 reported ROIC was ~6.4% (burdened by impairments), well below its 10.5% cost of capital; mid-cycle normalized ROIC is ~12.0%, providing only a modest spread above cost of capital. **Circle of competence:** understandable digital commerce and cloud computing; high geopolitical and regulatory complexity surrounding Cayman Islands Variable Interest Entity (VIE) structures.

## 3. GARP & Valuation Matrix
| Metric | Current (TTM/FY26) | 5-Yr Own Avg | Peer Median (Tencent, PDD, JD) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 8.5x | 11.5x | 12.2x |
| P/E (ttm / fwd) | 26.8x GAAP / 11.9x fwd | 18.5x | 15.4x |
| P/FCF (SBC-adjusted) | 16.2x (on normalized FCF $16.5B) | 14.0x | 13.5x |
| FCF Yield / Owner-Earnings Yield | 6.2% / 6.0% (normalized) | 7.1% | 7.4% |
| PEG Gate & PEG | Valid; PEG = 1.11 (fwd adj P/E 11.9 / 10.7% growth) | 1.35 | 1.25 |
| Lynch Ratio (g + yield) / P/E | 0.63 (poor; 4.5% growth + 3.0% yield) | 1.15 | 1.40 |
| ROIC vs WACC | 6.4% (FY26) / 12.0% mid-cycle vs 10.5% | 14.5% | 18.0% |
| Net debt / Owner earnings | Net Cash ($4.94B net cash / $16.5B owner earnings) | Net Cash | Net Cash |

## 4. DCF Scenarios
Valuation executed via `02_model.py`. WACC is 10.50% (US 10y Treasury yield 5.22%, China country risk premium 2.0%, Blume-adjusted beta 0.642, 5.0% ERP). Terminal growth rate is 2.5%, terminal ROIC is 12.0%, and terminal value constitutes 43.1% of enterprise value in Base.
- **Bear (25%): $35.78 USD.** Domestic consumption remains depressed; PDD and Douyin take additional share; 10-year revenue CAGR 1.5%; operating margin 8.0%; WACC 11.5%, g_term 1.5%; equity value $86.0B.
- **Base (55%): $69.58 USD.** Taobao/Tmall GMV stabilizes (+3% CAGR); Cloud AI expands at +12%–15%; group 10-year revenue CAGR 4.5%; operating margin 12.0%; WACC 10.5%, g_term 2.5%; equity value $167.3B.
- **Bull (20%): $126.77 USD.** Stimulus reignites broad consumer spending; Cloud margins expand to 15.0%; group 10-year revenue CAGR 7.5%; operating margin 15.0%; WACC 9.5%, g_term 3.5%; equity value $304.8B.

## 5. The Skeptic's Audit
- **Number audit:** 12 balance sheet and P&L items audited against SEC 20-F filings (accn 0001193125-26-231755). Key discoveries:
  1. *Net Cash Demystification:* Audited gross cash and short-term investments ($42.94B USD) against total bank debt and senior notes ($38.00B USD), proving true net cash is only $4.94B USD ($2.05/ADS). Net cash does not provide the massive valuation floor often claimed in retail commentary.
  2. *Operating Cash Flow Contraction:* Confirmed FY26 OCF dropped 53% YoY to CNY 76.2B ($11.4B USD), reflecting platform fee waivers and customer subsidy outlays.
  3. *Share Repurchase Count:* Verified that management repurchased and cancelled 343.4M ADS equivalents over FY22–FY26, reducing share count by 12.5%.
- **Capital Allocation Grade: B-**
  - Buffett $1 test is negative over 5 years due to broad market de-rating.
  - Share repurchase execution was highly disciplined, repurchasing stock well below intrinsic value ($75–$95/ADS).
  - Past venture acquisitions (Sun Art, Intime, Youku) resulted in multi-billion-dollar goodwill impairments.
- **Quality of Earnings:** Moderate. FY26 operating margins compressed to 5.0% due to aggressive reinvestment, while GAAP net income remains volatile due to equity investment revaluations.
- **Bear thesis:** Competitive margin erosion. PDD's manufacturer-direct pricing power and ByteDance's short-video attention dominance permanently break Taobao's advertising monopoly. Platform subsidies become permanent operating costs, anchoring group operating margins in the single digits while US chip sanctions cap Alibaba Cloud's AI potential.
- **Primary Downside Catalysts:**
  1. *Singles' Day (Double 11) Market Share Data (November 2026):* Further GMV share loss to Douyin livestreaming.
  2. *Macro Stimulus Disappointment:* Lack of direct fiscal consumer cash transfers in China leading to renewed retail sales weakness.
- **Unresolved disagreements (Quant vs Skeptic):** None; both confirm that recent stimulus-driven multiple expansion has carried the stock far above fundamental fair value.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency & Listing:** USD-denominated ADR on NYSE (BABA) or HKD-denominated shares on HKEX (9988.HK); exposed to USD/SGD or HKD/SGD currency fluctuations.
- **Dividends:** Cayman Islands corporate domicile; 0% dividend withholding tax for Singapore tax residents.
- **Estate Tax:** Foreign Cayman issuer; exempt from US federal estate tax under 26 USC §2104.
- **Portfolio Weight:** Currently held in active portfolio. Recommendation is to capitalize on the recent 38% stimulus liquidity surge to trim the position back to disciplined risk limits.

## 7. Sources
1. Alibaba Group Holding Limited FY2026 Form 20-F Annual Report (SEC accn 0001193125-26-231755).
2. Alibaba Group Holding Limited FY2021–FY2025 Form 20-F Filings.
3. Alibaba Group Q1 FY2027 Earnings Release (August 2026).
4. FRED US 10-Year Treasury Yield (DGS10, October 2026).
5. Quantitative valuation model and DCF run script (`reports/runs/BABA_2026-10-13/02_model.py`).

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          110.53 USD
FAIR_VALUE:     72.57 USD
UPSIDE:         -34.3%
ENTRY_BELOW:    58.05 USD
EXIT_ABOVE:     94.34 USD
CONVICTION:     HIGH
KEY_RISK:       Price discounts ~11.5% revenue CAGR for a decade while PDD and Douyin squeeze domestic commerce margins
DATA_WARNINGS:  0
