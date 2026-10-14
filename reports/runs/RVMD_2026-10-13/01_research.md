<!-- pipeline:value-researcher -->
# Research dossier: RVMD (as of 2026-10-13)

## 0. Routing
**rNPV** (late-stage oncology biotech, first product approved 2026-08-26, no product revenue yet reported: Q2 2026 revenue $0). Moat/PEG/owner-earnings not meaningful. Status: CURRENT HOLDING (SG resident, SGD base; US-listed USD security, so US estate-tax and dividend-WHT considerations are the user's profile matters, not researched here).

## 1. Snapshot
- Price $193.95 USD (close 2026-10-12; yfinance via methodologies/fundamentals.py, pulled 2026-10-13). Quote and reporting currency both USD; figures in USD millions unless stated. No ADR.
- 12m change: +297.8% (from $48.75 close 2025-10-13; yfinance). Since all-time-high close $221.15 (2026-08-27): -12.3%. Recent path: $207.68 (10-05) -> $188.12 (10-08, -6.3% day, cause UNKNOWN) -> $193.95 (10-12).
- 52-week range (yfinance daily high/low, 1y to 2026-10-12): $47.45 - $224.31. CONFLICT: prior deep dive quoted a 52w low of $35.62; the 1y window now excludes it (price 12m ago was $48.75). Not an error of the current figure.
- Market cap $41,570.5M (yfinance, 2026-10-13) = 214,336,418 shs (10-Q cover, 2026-07-31) x ~$193.95.
- EV build: mcap 41,570.5 - cash+marketable securities 3,938.0 (30 Jun 2026) + convertible notes principal 500.0 + royalty-sale liability carrying 548.5 (treated as debt-like, analyst judgement for Quant) = see Quant. Plain version: 41,570.5 - 3,938.0 + 500.0 = ~38,132.5. (yfinance EV $38,823M uses totalDebt $1,190M.)
- Shares: basic outstanding 214,336,418 (2026-07-31); Q2 weighted avg basic=diluted 210,893,604 (loss-making). Warrants (EQRx, 0.1112 sh each, expiring 2026) carried as $185.3M liability; count UNKNOWN. Convert 0.50% 2033 notes: conversion price UNKNOWN (not extracted).
- 10y UST yield 5.20% (yfinance ^TNX, 2026-10-13); sanity-check against Treasury.gov before use.

## 2. Financial history (USD M; sec_facts.py from SEC XBRL, retrieved 2026-10-13)
| FY | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM to 2026-06-30 |
|---|---|---|---|---|---|---|---|
| Revenue (collaboration) | 43 | 29 | 35 | 12 | 0 | 0 | 0 (Q2 and H1 2026: none) |
| Gross profit | n/a (pre-revenue) | | | | | | |
| Operating income | -111 | -188 | -258 | -487 | -690 | -1,182 | -1,627 |
| Net income | -108 | -187 | -249 | -436 | -600 | -1,131 | -1,768 |
| D&A | 3 | 3 | 4 | 5 | 7 | 8 | 9 |
| SBC | 9 | 21 | 31 | 62 | 79 | 118 | 219 |
| OCF | -100 | -147 | -224 | -351 | -557 | -898 | -1,223 |
| Capex | 3 | 7 | 11 | 8 | 10 | 16 | 9 |
| FCF | -103 | -154 | -235 | -358 | -568 | -914 | n/a |
| Buybacks / dividends | none | | | | | | |
| Cash and equivalents only | 104 | 108 | 161 | 696 | 543 | 384 | 815 (30 Jun 26) |
| Equity | 475 | 603 | 685 | 1,826 | 2,265 | 1,631 | 2,606 (30 Jun 26) |
| Diluted shares (M) | 55 | 73 | 81 | 113 | 168 | 190 | 210.9 (Q2 26) |

Cash caution: the XBRL "cash" row is cash equivalents only. Cash + marketable securities was $2,025.7M at 31 Dec 2025 and $3,937.97M at 30 Jun 2026 (10-Q accn 0001193125-26-335104; 8-K ex99.1 accn 0001193125-26-335039). Debt for the 2020-25 columns is not tagged; 30 Jun 2026: converts principal $500.0M (carrying $487.4M), royalty-sale liability $548.5M, op lease ROU asset $127.8M (lease liability UNKNOWN), term loan undrawn at 30 Jun.

Q2 2026 vs Q2 2025: R&D 394.9 vs 224.1; G&A 110.2 vs 40.6; opex 505.1 vs 264.7; net loss 644.4 vs 247.8, including $151.0M non-cash EQRx warrant remeasurement. H1 2026 opex 950.4; H1 2026 net cash used in operations -741.5 (10-Q). Interest income Q2 35.6; interest expense Q2 23.8 (mostly non-cash royalty-liability accretion).

## 3. Latest quarter and guidance
Only the Q2 2026 report (2026-08-05) exists; Q3 2026 has not been reported. Next earnings date: 2026-11-05 per yfinance calendar (UNCONFIRMED by company). yfinance consensus (CONSENSUS, 2026-10-13) for that quarter: EPS avg -2.39, revenue avg $24.1M (range 0 to $55.9M). Note an RBC Q3 revenue figure of $28M cited in the prior dive is not re-verified.

Verbatim guidance (8-K ex99.1, 2026-08-05): "Revolution Medicines is updating its full year 2026 GAAP operating expense guidance to a range of $2.1 to $2.2 billion, which includes estimated non-cash stock-based compensation expense of between $270 and $290 million."
Funding: "There remains up to an additional $1.5 billion in committed, flexible capital under the Royalty Pharma funding arrangements, subject to the achievement of specific milestones." 10-Q: "existing cash, cash equivalents and marketable securities will enable us to fund our planned operations for at least 12 months" (standard going-concern language; no longer runway stated).
Breakdown of the $1.5B (10-Q Notes 8-9): up to $750M further royalty purchases (tranches 3-5, milestone triggered) plus up to $750M senior secured term loan (3 x $250M; SOFR with 3.5% floor + 5.75%; 2% upfront fee; matures earlier of 6 yrs after first draw or 2032-12-31). Tranche 1 of the loan ($250M) "is required to be drawn in full ... within 45 days following receipt of FDA marketing approval ... if such approval occurs on or before January 1, 2028". Approval 2026-08-26 implies draw due by ~2026-10-10. No 8-K on a draw found as of 2026-10-13 (EDGAR filings list through 2026-10-01): draw status UNKNOWN. Prior dive called all $1.5B "undrawn, committed" without noting this mandatory draw; and it is debt, not royalty.
Royalty burden (10-Q): after tranches 1-2, 4.55% of annual net sales to $2B, 2.50% $2-4B, 1.00% $4-8B, 0% above $8B; if all optional tranches drawn: higher rates (text shows 4.55%/2.40% tiers variants for later purchases). Rates may rise in 2030-2041 if annual net sales fall below a threshold (0-2B tier only, stays single digit).

## 4. Earnings-call takeaways
Transcript NOT obtained (webcast 2026-08-05, 4:30pm ET; IR site returned 403). Q&A items: UNKNOWN. Prepared-remarks content taken from the press release only. Things the Aug-5 release emphasised: launch readiness, EAP >2,000 patients, NSCLC 1L combination data, CRC update in Q4.

## 5. Capital allocation record
- No buybacks, no dividends. Share count: diluted 55M (2020) -> 190M (2025) -> 214.3M (Jul 2026); diluted CAGR 28.2%.
- 2026 financing: April 2026 concurrent offerings $1,725.0M common + $500.0M 0.50% converts due 2033 (gross $2,225.0M; net convert proceeds ~$487.1M; first coupon 2026-11-01). Royalty Pharma: $250M upfront (Jun 2025) + $250M Tranche 2 (May 2026).
- M&A: EQRx (2023); impairment history not extracted (goodwill $14.6M, intangibles $55.8M at 30 Jun 2026). Prior-year offerings pre-2026: UNKNOWN (not re-sourced).
- Leases (8-K 2026-08-27/09-01, accn 0001193125-26-377362): 4 buildings, ~672,000 sq ft Redwood City HQ, 15-year terms ending Sep 2042, starting rent ~$2.7M/month at full commencement (+3%/yr, ~$32M/yr), commencements 2027-09-26 to 2028-09-01, TI allowance ~$115.9M (+ up to $40.3M), conditional on landlord acquisition closing (terminable if no close by 2026-12-31 notice window; auto-terminates 2027-04-29). Landlord affiliates of Farallon, which reported ~6.4% beneficial ownership of RVMD (related-party flag).
- Debt maturities: converts May 2033; term loan per above. No maturities in next 5 yrs.

## 6. Insider transactions (SEC Form 4, parsed from EDGAR, 2025-10-13 to 2026-10-01)
- Open-market purchases (code P): 0 in 12 months.
- Sales (code S, many via 10b5-1 / option exercise-and-sell): ~1,100,414 shares, ~$156.7M over 12 months. Since approval (2026-08-26): ~237,816 shares, ~$48.1M. Largest since 8-26: S. Kelsey ~$19.8M (2026-09-11 and 09-16), L. Kim (director) ~$15.0M (08-31 and 09-08), A. Mancini ~$4.6M, M. Goldsmith (CEO) ~$2.8M, E. Anderson (director) ~$2.0M, A. Sandler ~$1.3M, M. Horn ~$1.0M, J. Cislini ~$0.8M, J. Anders (CFO) ~$0.8M. Pre-approval: Goldsmith exercised and sold 80,000 options on 2026-08-21 at ~$207-212; CEO adopted 10b5-1 plan 2026-05-22 (10-Q).
- Several 2026-09-16 sales are small and consistent with tax-withholding-style sales on vesting (price $199.30). 
- insider_pct (static holding) 1.85% (yfinance). Institutional_pct 1.0127 flagged vendor artifact: not quoted. Large holders include Farallon ~6.4% (8-K 2026-08-27).

## 7. Peers and sector multiples
UNKNOWN. No revenue/earnings; EV/EBITDA, P/E, FCF yield not meaningful. No consistent single-vendor peer set sourced. Competitor context (Lilly olomorasib, Roche divarasib, Amgen sotorasib, BMS adagrasib, Immuneering IMM-1-104) is taken from the prior dive only and not re-verified.

## 8. Business facts
- Late-stage clinical oncology company; RAS(ON) inhibitors (tri-complex with cyclophilin A). Revenue now only via product sales to come; Royalty Pharma holds tiered royalty on daraxonrasib (and RMC-9805 if approved in same indication).
- **RASONQUE (daraxonrasib) FDA approved 2026-08-26** (8-K accn 0001193125-26-366931) for "adult patients with metastatic pancreatic adenocarcinoma who have received at least one prior systemic therapy or who are not candidates for multiagent systemic therapy". WAC $39,800 per 30-day supply. Tablets available in the US since approval. (NDA acceptance and CNPV voucher; approval ahead of PDUFA date per the prior dive: PDUFA date itself not re-verified.)
- RASolute 302 (Ph3, 2L PDAC; NEJM and ASCO 2026 plenary; 10-Q): median OS 13.2 vs 6.7 mo, HR 0.40, p<0.0001. Other trial details in prior dive (n=500, PFS 7.2 vs 3.6, ORR) not re-verified.
- Customer concentration: none (no sales). Market share: n/a.
- EMA: phased review under Cancer Medicines Pathfinder; Swissmedic orphan status. EU approval date UNKNOWN.

### Pipeline (sources: 10-Q 2026-08-05, 8-K ex99.1 2026-08-05, press 2026-09)
| Asset | Indication / study | Phase | Next event |
|---|---|---|---|
| Daraxonrasib (RASONQUE) | 2L+/unfit mPDAC | Approved (US 2026-08-26) | Q3'26 first sales; EMA phased review |
| Daraxonrasib | 1L mPDAC, RASolute 303 (+/- chemo vs chemo) | Ph3 | Readout date UNKNOWN. BTD (+gem/nab-pac, 1L) announced 2026-09-14 |
| Daraxonrasib | Adjuvant PDAC, RASolute 304 | Ph3 | UNKNOWN |
| Daraxonrasib | 2L RAS-mut NSCLC vs docetaxel, RASolve 301 | Ph3 | Enrollment complete 2026; "initial readout in 2027" |
| Zoldonrasib (G12D) | 1L PDAC + chemo, RASolute 305 | Ph3 | UNKNOWN |
| Zoldonrasib + daraxonrasib | 2L G12D PDAC, RASolute 309 | Ph3 | "recently initiated" (Aug); patient dosing announced ~early Oct 2026 |
| Zoldonrasib | 1L G12D NSCLC + SOC, RASolve 308 | Ph3 | "recently initiated"; readout UNKNOWN |
| Elironrasib (G12C) | 1L G12C NSCLC + SOC, RASolve 307 | Ph3 start | Initiate Q4 2026 |
| RMC-5127 (G12V) | solid tumors | Ph1 | RP2D 2H26; initial data 2027 |
| RM-055 (novel class) | - | IND-stage | FIH Q4 2026 |
| CRC combos | CRC | Ph1/2 | Data and strategy update Q4 2026 |
Preclinical: RMC-0708 (Q61H), RMC-8839 (G13C). Collaborations: Summit (PD-1/VEGF), Tango (PRMT5), BMS.
Early NSCLC data (cutoff 2026-05-11, press 2026-08-05): elironrasib+pembro+platinum 1L G12C: n=39, confirmed ORR 85%, DCR 97%, 95% PFS at 6 mo, median f/u 8.7 mo. Zoldonrasib+SOC 1L G12D: 38 treated, 28 efficacy-evaluable, ORR (confirmed+pending) 82%, DCR 100%, median f/u 3.4 mo.
BTDs: daraxonrasib previously treated KRAS G12 PDAC, previously treated non-G12C KRAS NSCLC; 1L PDAC with GnP (2026-09-14, company says third RASONQUE BTD, fifth in portfolio; secondary source).

### Events since the 28 Aug deep dive
- 2026-09-01: 8-K lease for ~672k sq ft HQ (see section 5).
- 2026-09-14: FDA BTD for RASONQUE + gem/nab-paclitaxel in 1L mPDAC (secondary sources: finviz/rttnews/pharmacally; company PR not fetched, IR 403).
- ~Early Oct 2026: first patients dosed in Ph3 RASolute 309 (Yahoo Finance headline, date approximate).
- Heavy insider selling post-approval (section 6); stock -12% from ATH close.
- No new efficacy readout, no safety communication, no financing found since 28 Aug. Mandatory $250M term-loan draw likely due ~2026-10-10: status UNKNOWN.

## 9. Consensus growth estimates
CONSENSUS (yfinance, 2026-10-13): next quarter revenue avg $24.1M, EPS avg -$2.39. Longer-dated peak-sales/consensus not re-sourced (prior dive's "$5.0-7.6B PDAC consensus" and "RBC $11.5B" are unverified; price targets banned). Historical growth: revenue $0 in FY2024-25; no meaningful growth series.

## 10. Data warnings and conflicts
fundamentals.json warnings (2): (a) institutional_pct=1.0127 outside 0..1, vendor artifact; (b) owner earnings negative (-$1,130.7M, confirmed by CF statement: NI -1,131 + D&A ~17 - capex 16).
Conflicts: 52w low $35.62 (prior dive) vs $47.45 (now): window roll-off. yfinance totalDebt $1,190M vs filing converts $500M + royalty liability $549M (+ leases) – definitional. fundamentals.json record shows operating_margins array of -inf; ignore.
UNKNOWN (count 10): earnings-call Q&A; Q3 report date confirmation; term-loan draw status; RASolute 303/304/305/308 readout dates; convert conversion price and warrant count; peers/multiples; EU approval timing; cause of 2026-10-08 -6.3% drop; PDUFA original date; consensus peak sales.
Also: sec_facts.py flagged 53 gaps (gross profit etc. n/a for pre-revenue) and TTM uses 10-Q; `stale` flag false.

## Sources
1. SEC EDGAR submissions CIK 1628171 (retrieved 2026-10-13).
2. 10-Q for 2026-06-30, accn 0001193125-26-335104.
3. 8-K 2026-08-05 (Q2 results), accn 0001193125-26-335039, ex99.1 rvmd-ex99_1.htm.
4. 8-K 2026-08-26 (FDA approval), accn 0001193125-26-366931.
5. 8-K 2026-09-01 (lease), accn 0001193125-26-377362.
6. Form 4 filings (72 filings 2025-10-13..2026-10-01), parsed from EDGAR XML.
7. methodologies/fundamentals.py and sec_facts.py outputs, data/fundamentals.json (2026-10-13).
8. yfinance price history, calendar, ^TNX (2026-10-13).
9. Secondary news for BTD and RASolute 309: finviz.com/news/391787, rttnews.com/3690926, Yahoo Finance RVMD press releases page (web search results, 2026-10-13).
10. Prior deep dive reports/detailed/RVMD_deep_dive_aug2026.md (pointer only).
