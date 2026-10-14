# Equity Analysis: VXUS — Vanguard Total International Stock ETF (US-domiciled)
As of 2026-10-13 · Price 84.52 USD · Template FUND · Run: `reports/runs/VXUS_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
No Lynch category: this is an index fund. **Why own it:** cheap (0.05% expense ratio), broad ex-US equity exposure, including small caps. **The problem is the wrapper, not the index:** for a Singapore resident, a US-domiciled fund's distributions carry 30% US withholding, and the fund is US-situs for estate tax. The same stocks held through an Irish UCITS fund (VWRA's ex-US sleeve, or an Irish ex-US fund) avoid both. **What it costs:** about **62bp a year**, or roughly **US$1,100 per US$10,000 over 10 years**. That holds in every scenario modelled, so switching has no modelled downside.

## 1. Executive Summary & Expected Value
- **Current Price:** $84.52 · **12-mo change:** +15.4% (raw closes; total return +18.3%)
- **Bear / Base / Bull (10-yr net annual return, Singapore holder):** 2.13% (25%) / 6.64% (55%) / 9.82% (20%)
- **Same stocks in an Irish wrapper (VWRA ex-US sleeve):** 2.75% / 7.26% / 10.44%
- **Expected Value (probability-weighted):** 6.15%/yr in VXUS vs 6.77%/yr in the Irish wrapper. Margin of safety: n/a under the FUND rules.
- **SBC-adjusted Expected Value:** n/a (fund).
- **Price implies:** ex-US per-share EPS must compound at 3.58%/yr at a constant 18.3x just for VXUS to match the 5.22% 10-yr Treasury (2.96%/yr inside an Irish wrapper).
- **Asymmetry of the decision:** the Irish wrapper wins in every scenario, by 61.5–74.3bp a year.
- **Recommendation:** **SELL** and move the exposure (MEDIUM conviction). On the wrapper economics alone the Skeptic rates it HIGH. Conviction drops one level mechanically because the model's value comes entirely from the year-10 exit price, as with any fund.

## 2. Business Quality (Buffett)
n/a for a fund. Look-through ROE is 12.6% (P/B 2.3 ÷ P/E 18.3) against a 10.22% CAPM hurdle, a weaker spread than VWRA's 17.1%. **Circle of competence:** a broad index is the classic know-nothing holding. The decision here is about tax structure, not business quality.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | n/a (fund) | n/a | n/a |
| P/E (ttm / fwd) | 18.3x (Vanguard factsheet, 30 Jun 2026) / UNKNOWN | UNKNOWN | VWRA 21.0x |
| P/FCF (SBC-adjusted) | n/a | n/a | n/a |
| FCF Yield / Earnings Yield | earnings yield 5.46%; distribution yield 2.35% TTM | 5-yr avg DPS on today's price 2.33% | UNKNOWN |
| PEG (or VOID + reason) | VOID: fund, no forward growth input | n/a | n/a |
| Lynch ratio (g + yield) / PE | n/a (fund) | n/a | n/a |
| ROIC vs WACC | look-through ROE 12.6% vs CAPM 10.22% | UNKNOWN | VWRA 17.1% |
| Expense ratio / all-in drag (Singapore holder) | 0.05% / **~93bp** | — | Irish wrapper ~30bp |

## 4. DCF Scenarios
No DCF of a fund. This is the 10-yr return decomposition used for VWRA (yield + EPS growth + P/E change − costs − tax drag), run in `02_model.py`. Risk-free rate: 10-yr US Treasury 5.22% (FRED). CAPM hurdle 10.22%. The decisive quantity is the after-tax gap between wrappers, and it barely moves under different probability weights (US$1,084–1,158 per US$10k).
- **Bear (25%): 2.13%/yr.** Semiconductor and memory earnings revert (EPS growth 3%) and the multiple compresses to 14.3x.
- **Base (55%): 6.64%/yr.** EPS growth 5%, no re-rating at 18.3x.
- **Bull (20%): 9.82%/yr.** EPS growth 6.65%, re-rating to 21.1x.

## 5. The Skeptic's Audit
- **Number audit:** 17 checked, 0 failed, 3 flags; fair value unchanged. The Skeptic's independent code reproduced the Quant's scenario returns to 0.01pp.
  - **Yield:** Q1–Q3 2026 distributions were the lowest of 2021–26, cause unknown. The plausible gap range is 61–76bp.
  - **Irish substitute's size:** it has grown to about US$117M (undated, two vendors), from US$35M.
  - **Trading spread:** UNKNOWN.
- **Structure Grade: D** for a Singapore holder. It would grade A for a US taxpayer.
  - **30% withholding:** verified against §871(a) and IRS Pub. 901 (Singapore has no US income-tax treaty). VXUS is absent from Vanguard's short-term-gain exemption lists for 2023 and 2025.
  - **US-situs for estate tax:** verified. §2104(a) counts shares issued by a domestic corporation; §851(a) treats a fund like this as a domestic corporation; the §2105(d) look-through for such funds ended for deaths after 2011.
  - **Estate-tax cost:** each US$10k of VXUS adds US$2,600–3,000 of estate tax if total US-situs holdings are US$60–150k (§2101(b), §2001(c)).
  - **Foreign tax credits:** VXUS passes them through, but a non-US holder can't use them.
- **Quality of Earnings (index level):** trailing ex-US earnings are cyclically lifted by semiconductors and memory. That's in the bear weight.
- **Bear thesis:** semiconductor and memory earnings revert while the multiple compresses. On top of that the wrapper leaks about 62bp/yr for certain, and **the leak is the only part of the downside you can remove.**
- **Primary Downside Catalysts:**
  1. **The December distribution.** December carries 39–57% of yearly payouts. Withholding on that one payout costs about 36–48bp of the position. **Signpost: the ex-date** (2024-12-20 and 2025-12-19 in prior years), so switch before it.
  2. **Cyclical earnings reversal in Asian semiconductors and memory.** Signpost: the TSMC and SK Hynix results the pipeline covers separately.
- **Unresolved disagreements (Quant vs Skeptic):** none on numbers. The Skeptic made five refinements:
  - a range for the exemption share;
  - estate-tax sizing;
  - the substitute's size;
  - December timing;
  - the yield trend.
  All are kept separate in its §7.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-quoted with global ex-US exposure.
- **Dividends:** **30% US withholding on distributions.** That's the core defect.
- **Estate tax:** **US-situs**, so it counts toward the US$60k threshold together with ZBH, RVMD and your other US listings.
- **Overlap with VWRA:** this exposure largely duplicates VWRA's ex-US sleeve (38% of VWRA), plus small caps.
- **Tax on switching:** no capital-gains tax, so a switch costs only the trading spread.
- **Where to move the money** is an allocation choice:
  - **VWRA**, if the ex-US overweight wasn't deliberate. Each US$1 of ex-US exposure also brings US$1.61 of US stocks.
  - **The Irish ex-US UCITS (IE0009A5ADV9)**, if you want the tilt. Use limit orders. It's young (launched 2026-08-18), but it only loses if it trails its index by more than 63.5bp/yr beyond its fee.
  - **An iShares developed ex-US + EM pair**, for a longer track record.

## 7. Sources
1. Vanguard VXUS product page, factsheet (30 Jun 2026) and distribution history; Vanguard short-term capital-gain exemption lists 2023/2025
2. 26 USC §2104(a), §851(a), §2105(d), §2101(b), §2001(c), §871(a)/(k): https://www.law.cornell.edu/uscode/text/26/2104
3. IRS Publication 901 (US tax treaties); IRS nonresident estate tax guidance: https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
4. Vanguard FTSE All-World ex-U.S. UCITS ETF (IE0009A5ADV9), Vanguard and justETF pages; iShares MSCI World ex-USA (IE000R4ZNTN3) and Core MSCI EM IMI (IE00BKM4GZ66)
5. FRED DGS10: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
6. yfinance raw price history; `data/fundamentals.json` (2026-10-13)
7. Run files: `01_research.md`, `facts.json`, `02_quant.md`, `02_model.py`, `03_skeptic.md`; VWRA comparison in `reports/runs/VWRA.L_2026-10-13/`

VERDICT:        SELL
AS_OF:          2026-10-13
PRICE:          84.52 USD
FAIR_VALUE:     6.64%/yr base 10-yr net return for a Singapore holder (probability-weighted 6.15%/yr; same exposure in an Irish wrapper 6.77%/yr)
UPSIDE:         n/a (FUND)
ENTRY_BELOW:    n/a
EXIT_ABOVE:     n/a
CONVICTION:     MEDIUM
KEY_RISK:       Structural: 30% US withholding (~62 bp/yr) and US-situs estate exposure; switch before the December ex-date
DATA_WARNINGS:  1
