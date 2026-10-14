<!-- pipeline:value-researcher -->
# Research dossier: 000660.KS (SK hynix Inc.) (as of 2026-10-13)

Prepared 2026-10-14 (SGT). Price data = 2026-10-13 KRX close. All figures K-IFRS consolidated, KRW, **millions of KRW unless stated** (trillion = T, billion = B). Tags: `[SNIPPET]` = seen only in a search/WebFetch summary, not confirmed in a primary document; `[WF]` = WebFetch-summarised quote from a transcript host, not checked against the raw transcript.

## 0. Routing
**FULL** (profitable operating company), Lynch category candidate **Cyclical** (DRAM/HBM/NAND). Current holding. Not a bank/biotech/fund. Note for later stages: reported net income is dominated by non-operating fair-value gains (Section 2/10), so Owner-Earnings and P/E built on net income are unreliable without adjustment.

**Corporate-status finding:** SK hynix IPO'd ADSs on Nasdaq (ticker SKHY) on 2026-07-10 and is now an SEC foreign private issuer (CIK 0002120882, files 6-K; first 20-F not yet due). `sec_facts.py 000660.KS` returns NOT AN SEC FILER (ticker map), so facts were taken from the SEC-filed 6-K / 424B4 documents (accession numbers below). That gives a primary K-IFRS source with accession numbers for FY2023-FY2025 (audited, KPMG) and H1 2026 (unaudited).

## 1. Snapshot
| Item | Value (source, date) |
|---|---|
| Price | **KRW 1,443,000** (KRX raw close, yfinance auto_adjust=False, 2026-10-13). Quote ccy KRW, reporting ccy KRW. |
| 12m change (raw closes) | +247.7%: 415,000 (2025-10-13) -> 1,443,000. Dividends over the 12m: KRW 375 + 1,875 + 375 + 375 = 3,000 (ex-dates 2025-11-27, 2026-02-26, 2026-05-28, 2026-08-28; yfinance dividend history) = ~0.2% of price, separate from the price change. |
| 52w range (raw closes) | low 411,500 (2025-10-14); high 2,919,000 (2026-06-22). Price is **-50.6% below the 52w high**. |
| Recent tape | 2026-10-02 1,841,000; 10-06 1,773,000; 10-07 1,723,000; 10-08 1,681,000; 10-12 1,605,000; **10-13 1,443,000 (-10.1% on the day, -21.6% in 6 sessions)**. Samsung Electronics (005930.KS) 262,000 -> 232,000 (10-08 -> 10-13, -11.5%); SK Square 1,050,000 -> 857,000. KOSPI 6,625.9 (10-08) -> 6,384.2 (10-12). I found no article explaining 10-13 (searches returned only July/June episodes: 2026-07-13 -15.4% day tied to MSCI EM weight + profit-taking after ADR listing; 2026-06-23 -12.5%). Cause of the 10-13 fall: UNKNOWN. |
| Shares | Issued **730,492,365** (6-K accn 0001193125-26-356141, 2026-08-19) less treasury **1,625,769** (6-K accn 0001193125-26-359825, as of 2026-08-21) = **728,866,596 outstanding**. Dividend cross-check: Q2 dividend KRW 273,324,801,750 / KRW 375 = 728,866,138 entitled shares (6-K accn 0001193125-26-339031). Increase of 17,790,000 shares vs 712,702,365 at 2026-06-30 = ADR primary issue (6-K accn 0001193125-26-303972). Buyback of up to 24,070,000 shares began 2026-08-20; **shares bought to date UNKNOWN** so true count is somewhat lower. |
| Diluted shares (weighted) | H1 2026: 711,615,569; Q2 2026: 711,647,617 (6-K accn 0001193125-26-354777, note 27). FY2025 711,266,733; FY2024 709,834,641 (424B4). These pre-date the ADR issue: **post-ADR diluted count is about 17.8M higher**. Exchangeable bonds fully exchanged (no dilution remaining). |
| Market cap | 728,866,596 x 1,443,000 = **KRW 1,051,754B (~KRW 1,051.8T)** = ~US$784B at KRWUSD 0.00074539 (00_inputs.json; 1 USD = KRW 1,341.6; 1 SGD = KRW 1,048.1). yfinance/fundamentals.json shows KRW 1,026.1T (US$765.4B) because it uses the stale 711,075,500 share count (-2.4% vs mine). |
| EV build (simple, 6/30/2026 balance sheet) | mcap 1,051,754,498 - cash & equivalents 26,835,986 - ST financial instruments 22,397,559 - ST investment assets 38,724,378 (= 87,957,923; company says "KRW 88T") + borrowings 18,586,634 + lease liabilities 2,526,505 (526,461 current + 2,000,044 non-current) = **KRW 984,909,714M (~984.9T)**. Net cash ex-leases 69,371,289M (company: "69.4 trillion won"). **Not in the build** (Quant must decide): LT investment assets 85,309,524 (FV; Kioxia-related share not separable, UNKNOWN), LT financial instruments 7,101,803, ADR net proceeds received after 6/30 (company-estimated US$26.2B net; gross KRW 39,890,534,790,000 issuance amount at KRW 1,504.9/USD), current tax liabilities 31,958,025 (unpaid), KRW 40.0T buyback authorisation. |
| ADR | 1 SKHY ADS = **1/10** common share (424B4). SKHY close US$155.93 (2026-10-13 US) = US$1,559/share-equivalent vs KRX US$1,076: **ADS trades ~45% above the KRX line** (30-45% premium since late July, computed from yfinance SKHY, 000660.KS and KRW=X closes; US session closes after KRX, so same-day timing is not synchronous). Cause UNKNOWN. IPO price US$149.00 vs KRX US$1,421 on 2026-07-09 (~5% premium then). |
| 10y yield (KRW) | 00_inputs.json uses OECD monthly 4.286% (Aug 2026). Fresher: **4.369%, KTB 10y close 2026-10-06 (KOFIA basis, SBS Biz https://biz.sbs.co.kr/amp/article/20000338551, WebFetch-confirmed)**; 4.436% on 2026-10-01 (SBS Biz 20000337916). OECD Sept monthly average 4.45% (statisticsoftheworld.com). Oct 7-13 closes not found. Per 00_inputs rule, I show the effect but do not silently substitute: the delta vs the 00_inputs figure is +8bp. USD 10y 5.22% (DGS10, 2026-10-08) per 00_inputs. |
| Beta | 2.391 (yfinance). |

## 2. Financial history
Source for FY2023-FY2025: 424B4 accn 0001193125-26-299963 (audited K-IFRS). H1 2026 and H1 2025: 6-K accn 0001193125-26-354777 (unaudited). FY2021-FY2022: company results release mirror (rounded to KRW B).
K-IFRS cash flow starts from profit for the year (not pre-tax), so the "IFRS pre-tax start" caveat does **not** apply here (fundamentals.json has no such warning for this ticker). Lease principal sits in financing (below). Capex = PP&E + intangibles acquisitions (this ties to fundamentals.json capex 28,579,343).

| KRW M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | **TTM (Jun-26)** |
|---|---|---|---|---|---|---|---|---|
| Revenue | 42,998,000 | 44,648,000 | 32,765,719 | 66,192,960 | 97,146,675 | 39,871,093 | 131,895,033 | **189,170,615** |
| Gross profit | UNKNOWN | UNKNOWN | -533,448 | 31,828,146 | 58,690,790 | 22,085,315 | 107,670,770 | 144,276,245 |
| Operating profit (EBIT) | 12,410,000 | 7,007,000 | -7,729,999* | 23,467,319* | 47,206,319* | 16,653,355 | 98,152,891 | **128,705,855** |
| Net income (profit for period) | 9,616,000 | 2,439,000 | -9,137,547 | 19,796,902 | 42,947,902 | 15,104,411 | 134,268,502 | **162,111,993** |
| NI attributable to owners | UNKNOWN | UNKNOWN | -9,112,428 | 19,788,681 | 42,919,287 | 15,104,309 | 134,150,412 | 161,965,390 |
| D&A (CF depreciation+amortisation) | UNKNOWN | UNKNOWN | 13,282,991 | 12,581,537 | 13,930,130 | 6,799,925 | 7,759,289 | 14,889,494 |
| SBC (CF add-back "share-based payments", includes cash-settled) | UNKNOWN | UNKNOWN | 28,793 | 104,110 | 414,114 | 206,308 | 74,639 | 282,445 |
| Operating cash flow | [SNIPPET] 19,797,648 | [SNIPPET] 14,780,517 | 4,278,191 | 29,795,885 | 53,373,126 | 18,189,841 | 91,742,501 | 126,925,786 |
| Capex (PP&E + intangibles) | [SNIPPET] 12,486,635 | [SNIPPET] 19,010,261 | 8,779,848 | 16,662,640 | 28,579,343 | 11,076,176 | 18,994,016 | 36,497,183 |
| FCF (OCF - capex) | UNKNOWN | UNKNOWN | -4,501,657 | 13,133,245 | 24,793,783 | 7,113,665 | 72,748,485 | 90,428,603 |
| Buybacks (cash) | none | none | none | none | none | none | none | none (KRW 40.0T programme began 2026-08-20) |
| Dividends paid | UNKNOWN | UNKNOWN | 825,575 | 826,323 | 1,681,166 | 1,159,114 | 1,594,365 | 2,116,417 |
| Lease principal repaid (financing) | UNKNOWN | UNKNOWN | 461,466 | 601,821 | 596,465 | 301,734 | 287,185 | 581,916 |
| Cash + ST fin. instr. + ST investment assets | UNKNOWN | UNKNOWN | ~8,921,000 | ~14,156,363 | 34,942,253 | n/a | 87,957,923 | (6/30/26) |
| Borrowings (current+non-current) | UNKNOWN | UNKNOWN | ~29,468,000 | 22,683,733 | 22,247,905 | n/a | 18,586,634 | (6/30/26) |
| Lease liabilities | UNKNOWN | UNKNOWN | ~3,029,000 | 2,768,376 | 2,509,943 | n/a | 2,526,505 | (6/30/26) |
| Total debt incl. leases | UNKNOWN | UNKNOWN | ~32,497,000 | 25,452,109 | 24,757,848 | n/a | 21,113,139 | (6/30/26) |
| Total equity | UNKNOWN | UNKNOWN | 53,504,000 (~) | 73,915,704 | 120,666,751 | n/a | 262,693,228 | (6/30/26) |
| Inventories | UNKNOWN | UNKNOWN | ~13,481,000 | 13,313,937 | 14,289,390 | n/a | 17,985,706 | (6/30/26) |
| Trade receivables, net | UNKNOWN | UNKNOWN | ~6,600,000 | 13,019,006 | 18,199,078 | n/a | 47,821,395 | (6/30/26) |
| Diluted shares (weighted) | UNKNOWN | UNKNOWN | 688,051,238 | 709,834,641 | 711,266,733 | 711,094,878 | 711,615,569 | pre-ADR basis |
| Diluted EPS (KRW) | UNKNOWN | UNKNOWN | -13,244 | 28,419 | 60,378 | 20,996 | 188,193 | |

`~` = from the 424B4 selected-data table in KRW billions (rounded). `*` = derived: GP - SG&A - R&D (424B4 does not print an operating-profit line for FY23-25; FY2025 EBIT 47,206,319 is derived). FY2021/22 revenue, operating profit, net income are from the company's FY2022 release (rounded KRW B: 2022 44,648 / 7,007 / 2,439; 2021 42,998 / 12,410 / 9,616). The FY2021-22 OCF/capex are aggregator figures seen in a search summary, tagged [SNIPPET] and not load-bearing. TTM = FY2025 - H1 2025 + H1 2026 (my arithmetic).

**Growth, company's own history:** revenue FY2023 -26.6% (44,648B -> 32,766B; FY2022 figure is the rounded release number), FY2024 +102.0%, FY2025 +46.8%, H1 2026 vs H1 2025 +230.8% (company release). Q2 2026 revenue +257% YoY, +51% QoQ. Revenue in 2019-2024 averaged below KRW 16T a quarter [SNIPPET, blocksandfiles].

**Quarterly path (company, K-IFRS):** Q2'25 revenue 22,231,952 / OP 9,212,851 / NI 6,996,216; Q1'26 52,576,287 / 37,610,283 / 40,345,909; **Q2'26 79,318,746 / 60,542,608 / 93,922,593** (GM 83.2% = 65,991,356/79,318,746; OPM 76.3%). Q2'26 split: DRAM 56,982,743 (71.8%), NAND 21,959,898 (27.7%), other 376,105 (6-K note 21). HBM is inside DRAM; **HBM revenue UNKNOWN**.

**Why NI (93.9T) > OP (60.5T) in Q2 and why this matters (K-IFRS net-income caveat):** Q2 finance income 65,858,814 = gain on valuation of financial instruments 53,237,425 + dividend income 10,027,945 + FX 2,149,342 + interest 304,478 + other 139,624; finance expense 3,640,903 incl. derivative loss 2,479,736 (exchangeable bonds; non-cash). Press reports tie the gain to SK hynix's Kioxia holding; the filing itself (note 24) does not name Kioxia. The "KRW 63.3T" the call and press call "gains from sale and valuation of investment assets" = 53,237,425 + 10,027,945 = 63,265,370, i.e. **fair-value gain plus dividend income, not sale proceeds** (some press, e.g. Blocks & Files, calls it "proceeds from sale"; the 6-K cash-flow shows only 10,695,241 proceeds from disposal of LT investment assets in H1). Tax: H1 income tax 40,056,711 on PBT 174,325,213 = 23.0%; **current tax liabilities 31,958,025** (vs 7,023,813 at 12/31/25), deferred tax liabilities 7,836,633. FY2025 NI (42.9T) was also flattered by 12.0T valuation gains and burdened by 8.4T derivative losses (424B4 note 33).
OCF H1 2026 91.7T includes 13,983,648 "dividends received" (vs 25,932 H1'25) and 23.3T of receivable build (trade receivables 18,199,078 -> 47,821,395; DSO on Q2 revenue ~55 days = 47.82T/79.32T x 91).

**Lease/IFRS 16:** lease principal is financing outflow (FY2025 596,465; H1'26 287,185) and not in capex or FCF above; total lease payments H1'26 316,646 (principal+interest 48,474 included). Lease liabilities 2,526,505 are included in "total debt incl. leases". No minority-interest put liabilities found (NCI is only 312,618). 5-year inventories/receivables: FY2021-22 UNKNOWN.

**Net cash:** company-stated, 6/30/26: cash & equivalents (incl. ST investments) KRW 88T, debt 18.6T, net cash 69.4T. My tie-out: 87,957,923 - 18,586,634 = 69,371,289. Caution: the "cash" includes 38.7T of short-term investment assets (Level 2 fair value), and 31.96T of current tax is unpaid.

## 3. Latest quarter & guidance
**Status of Q3 2026 results: NOT RELEASED.** No Q3 preliminary result is in SEC 6-K filings through 2026-09-18 (latest) or in any search. Date of the Q3 release/call is **not confirmed by the company**; third-party calendars say call 2026-10-29 09:00 KST / results 10-28 [SNIPPET: AJ Bell, Earnings Whispers estimates]. For Q2 the company filed its call notice 6-K two weeks ahead (2026-07-15 for 07-29), so a Q3 notice should appear ~mid-October. The company said it expects to unveil detailed additional shareholder-return plans "within the year" / with Q3 results [WF + press].
Sell-side Q3 operating-profit estimates quoted in a search summary (not collected as targets; flagged only as the "what the market expects" mark): DS Investment 70T, Daishin 78T, vs a 111T/78T consensus mentioned in the same piece [SNIPPET, internally inconsistent]. Yahoo consensus is in Section 9.

**Q2 2026 (K-IFRS, press release 2026-07-29 https://news.skhynix.co.kr/q2-2026-business-results/; 6-K accn 0001193125-26-321989; statements note "review by external auditor not complete"):**
- Revenue 79,318,746; operating profit 60,542,608 (OPM 76%); profit 93,922,593.
- Pricing (H1 report, section II.2.B): "DRAM shipment volume increased slightly as sales expanded centered on HBM3E and AI-oriented server DRAM products, and average selling price ('ASP') rose in the mid-30% range due to the continuation of strong pricing for general DRAM. NAND shipment volume increased in the mid-10% range ... and ASP rose in the mid-50% range compared to the previous quarter" (6-K accn 0001193125-26-354777).
- Utilisation: "average utilization rate of production facilities during the same period was maintained at 100%" (H1 report).
- Press release verbatim (English mirror, Placera/PR Newswire): "cash and cash equivalents reached 88 trillion won at the end of the second quarter ... Total debt decreased by 0.7 trillion won to 18.6 trillion won, expanding the net cash position to 69.4 trillion won."
- Press (Korean original): the company started HBM4 mass-production shipments in Q2 and will "본격 확대" in H2; HBM4E samples were supplied in H1; 321-layer NAND to ~50% of domestic capacity by year-end; LTAs concluded with around 10 customers, "고객 수요가 공급 역량을 상회하는 시장 환경" (customer demand exceeds supply capacity); "설비투자 원칙(CapEx Discipline)을 유지".
- Versus expectations: operating profit 60.54T vs FnGuide 63.99T and revenue 79.32T vs 83.94T (Korea JoongAng Daily, WF). The shares fell 9.6% on 2026-07-29 [WF].

**Management numeric guidance (transcript via Investing.com, `[WF]`, not verified against raw transcript):**
- Capex: "our 2026 CapEx is expected to reach the high KRW 40 trillion range" (Song Hyeon-jong, President Corporate Center); "we are pulling forward the mass production schedule for M15X". Reference: FY2025 cash capex was 28,579,343M and H1'26 cash capex 18,994,016M (cash basis; the guidance basis, accrual vs cash, is not stated: UNKNOWN).
- Q3 DRAM: "DRAM shipments are expected to increase by approximately 10% from that of Q2" (Park Seong-hwan, IR). Q3 NAND: "we plan bit shipment increase of low single-digit percent quarter-on-quarter."
- H2: "we expect bit growth in the second half to be higher than the level in the first half".
- Supply: "tight supply-demand conditions expected to persist for a considerable period"; "it appears difficult for the supply-demand balance to improve meaningfully in the near term"; Yongin phase-1 cleanroom opens "in early 2027"; HBM4E "aiming at volume production beginning in 2027".
- Fixed dividend: KRW 1,500/share per year for 2025-2027, paid in four KRW 375 instalments (H1 report section 2A).

**Capital-commitment 6-Ks (last ~10 weeks):** Y2 (Yongin Fab 2 phases 1-6) KRW 35,224,600,000,000, period to 2031-10-31 (6-K accn 0001193125-26-339024, 2026-08-07); M17 Cheongju KRW 19,100,000,000,000, to 2031-04-30 (accn 0001193125-26-339011, 2026-08-07); P&T7 packaging raised to KRW 7,093,100,000,000 (accn 0001193125-26-311230, 2026-07-22).

## 4. Earnings-call takeaways
Source: Investing.com transcript of the 2026-07-29 Q2 call, accessed via WebFetch (summarising model; quotes <= 125 chars, `[WF]`). Free hosts Yahoo/GuruFocus/Quartr were blocked or AI-summary only; no 6-K transcript exists (6-K carries only the call notice).
1. **2027 HBM pricing (UBS):** CFO Kim Woo-hyun: "Discussion is underway for 2027 HBM supply volume and pricing with our key customers"; "we cannot disclose the contractual terms or pricing details for individual customers"; "HBM pricing is not determined solely by conventional DRAM prices." No 2027 price direction was given (dodged). HBM market share was not disclosed on the call.
2. **Oversupply (Hana Securities):** "we do not believe our medium to long-term investment plans will lead to oversupply right away."
3. **Overseas capacity (CLSA):** "there are no further decisions made in addition to the investment that has already been announced." (Later 6-Ks show media rumours the company neither confirmed nor denied outright: Japan fab, Chongqing packaging stake sale ~KRW 4T, Solidigm pre-IPO raise ~KRW 5T; all answered "no matters have been determined"; further disclosure promised within three months of 2026-09-04/09/18.)
4. **HBM4 competitiveness (SK Securities):** yield and quality "nearing the levels of HBM3E".
5. **Shareholder returns (DS Investment):** "we are currently evaluating various options for additional shareholder returns"; format/size/timing not provided; "we do intend to communicate our plans to the market within the year". Followed by the 2026-08-19 KRW 40T buyback.
6. **Daiwa on DRAM ASP:** some high-value shipments "were pushed back into the second half" (revenue-timing explanation for the miss). A Reuters-attributed explanation that SK hynix prioritised DRAM bits for HBM [SNIPPET].
**Not discussed (per WF summary):** tax on the investment gain, inventory, and Kioxia (only named inside an analyst question; no answer). Tone vs prior call: UNKNOWN (Q1 call transcript not collected). Shares fell on "growth doubts" [WF] even as the print was a record.

## 5. Capital allocation record
- **Buybacks.** No cash buybacks in FY2023-FY2025 or H1 2026 (cash-flow statements: none; treasury share history lists open-market purchases only in 2015 and 2018, H1 report section I.3). 2026-02-09: cancelled 15,300,000 old treasury shares, carrying value KRW 872,236,935,000 (avg ~KRW 57,000/share; they were bought in 2018). **2026-08-19: board approved acquiring and cancelling up to 24,070,000 shares, aggregate KRW 40,004,340,000,000, open-market, 2026-08-20 to 2026-11-19** (6-K accn 0001193125-26-356133 and -356141). Implied ~KRW 1,662,000/share at the ceiling. Executed to date: UNKNOWN (no interim report found). Management stated "its recent share price [is] undervalued relative to the Company's intrinsic value" (6-K accn 0001193125-26-356139).
- **Return policy 2025-2027 (updated 2026-08-19):** "return over 50% of cumulative Free Cash Flow to its shareholders"; reviewing dividend expansion "including existing fixed dividends and special dividends" (6-K accn 0001193125-26-356139). Earlier policy was 5% of FCF.
- **Dividends per share declared:** FY2024 KRW 2,204; FY2025 KRW 3,000 (3 x 375 + year-end 1,875); 2026: Q1 375, Q2 375 (record 2026-08-31, total KRW 273.3B). Payout ratio FY2025 4.9% (company, consolidated). Cash paid FY2025 1,681,166M.
- **Share count trajectory:** issued 728,002,365 (12/31/25) -> 712,702,365 (after the 15.3M cancellation) -> 730,492,365 (after 17.79M ADR shares, 2026-07-14). Treasury 26,310,845 (12/31/25; includes shares reserved for the exchangeable bond) -> 1,625,769. Outstanding 12/31/25 = 701,691,520 (728,002,365 - 26,310,845); 2026-08-21 = 728,866,596. Weighted diluted FY2023 688.1M -> H1'26 711.6M (the increase is the exchangeable-bond exchange, 8,932,474 shares exchanged in H1 2026 for USD 738.4M of bonds; cumulative 20,560,302 shares for USD 1.7B).
- **Equity issuance:** 2026-07: 17,790,000 new shares via ADSs at US$149.00/ADS (US$1,490/share; USD 26,507,100,000 gross; est. net US$26.2B), "general corporate purposes, including capital expenditures" (424B4). That is ~2.4% dilution at about KRW 2.24M/share, issued 6 weeks before the company declared its own stock "undervalued" and began buying at ~KRW 1.4-1.7M (6-K 2026-08-19). Both are facts; the interpretation is for the Skeptic.
- **Acquisitions.** Intel NAND (NSG) business: phase 1 completed Dec 2021, final phase completed March 2025 (H1 report section I.2.D); FY2025 cash outflow from business combination 3,079,783M (424B4). Key Foundry acquired Aug 2022. The purchase price of the Intel deal is **UNKNOWN** (not extracted from a sourced document). Intel-related impairment history: UNKNOWN (not researched; Solidigm is now reported inside the single segment).
- **Debt (6/30/26):** current 5,858,873 (short-term borrowings 2,664,419; current long-term 1,945,289; current debentures 1,249,165); non-current 12,727,761 (long-term borrowings 2,183,825; debentures 10,543,936). The 2023 USD 1.7B exchangeable bonds (due 2030) were fully exchanged/redeemed (clean-up call completed 2026-05-28). **Maturity ladder by year 2027-2031 UNKNOWN** (not extracted). Covenants: debt ratio and LTV complied (H1 report).
- **Other uses:** KRW 35.2T Y2 + 19.1T M17 + 7.1T P&T7 board approvals (Section 3) with multi-year windows; Yongin cluster plan reported at 800T for Samsung+SK hynix combined [SNIPPET].
- **Tax cash call:** current tax liabilities 31,958,025 at 6/30/26.

## 6. Insider transactions
Form 4 does not apply (Korean issuer). Primary source: H1 2026 report, "changes in largest shareholder and related parties" table (accn 0001193125-26-354777).
- Related-party holdings of SK Square group (146,100,000 shares held by SK Square + ~24,531 by related persons) moved 146,115,103 (2025-04-25) -> 146,115,505 (2026-01-29) -> 146,113,730 (2026-03-26) -> 146,118,388 (2026-04-07) -> 146,124,531 (2026-05-06). Every change listed in the last 12 months to 2026-06-30 is a **treasury-share grant, stock-option exercise, or change of the related-party roster**, not an open-market trade. Open-market purchases appear in this table only earlier (e.g. Feb 2023, CEO Nohjung Kwak).
- 2026-08-19: 82 treasury shares granted to independent directors at KRW 1,500,000 (compensation, 6-K accn 0001193125-26-359825). Not a market transaction.
- **Open-market insider buys/sells after 2026-06-30: UNKNOWN** (DART officer-holding reports not accessed).
- Holdings (not activity): SK Square 20.50% as of 2026-06-30 (146,124,531 shares; ~20.0% on the post-ADR share count, my arithmetic), National Pension Service 8.06% (as of 2025-12-31), BlackRock Fund Advisors 5.11% (as of 2026-02-10). `insider_pct` in fundamentals.json is not used.
- SK Square (the user's other holding) sold or pledged its hynix stake? UNKNOWN; its stake is unchanged at 146,100,000 shares through 2026-06-30.

## 7. Peers & sector multiples
Single vendor: yfinance via `methodologies/fundamentals.py` / `Ticker.info`, snapshot 2026-10-13. **Caveat: the vendor's trailing figures are not synchronised.** For 000660.KS and 005930.KS trailing P/E is null and FCF/EBITDA reflect FY2025 or a stale mix, whereas the true TTM (Section 2) is 3-4x larger. Treat as a rough cross-section only, not for valuation.
| Name | Mcap (US$B) | EV/EBITDA (vendor) | Trailing P/E | Forward P/E | FCF yield (latest-FY FCF / mcap) |
|---|---|---|---|---|---|
| SK hynix 000660.KS | 765.4 (stale shares; 784 on my count) | 6.68 | null | 3.07 | 2.4% (FY2025 FCF; TTM FCF in Section 2 is ~3.6x higher) |
| Samsung Electronics 005930.KS | 1,126.5 | 6.03 | null | 3.21 | 2.2% |
| Micron MU | 1,061.0 | 9.93 | 12.6 | 4.55 | 0.2% |
| SanDisk SNDK | 209.2 | 16.90 | 19.6 | 5.43 | 5.5% |
| Kioxia 285A.T | 153.1 | 10.55 | 18.2 | null | 1.4% |
| Nanya 2408.TW | 52.3 | 12.86 | 18.2 | 4.07 | 0.3% |
Warnings from fundamentals.json for peers: Kioxia and Nanya "cash-flow net income differs from income-statement ... (IFRS pre-tax start?)". Samsung/SK hynix Korean-peer comparison also note: all of these are in a sharp drawdown the same week (Samsung -11.5%, SK Square -18.4% between 10-08 and 10-13). Forward P/Es of 3-5x imply forward EPS far above trailing; they are consensus-derived and shown for completeness only.

## 8. Business facts (two-minute-drill inputs)
- **What:** memory semiconductors. DRAM (incl. HBM, server DRAM, SOCAMM2, LPDDR) and NAND (eSSD via Solidigm, 321-layer), plus small foundry (SK hynix system ic, SK keyfoundry). Single reportable segment (6-K note 4). Fabs in Icheon, Cheongju (Korea) and Wuxi, Chongqing, Dalian (China); 100% utilisation H1 2026.
- **How it makes money:** sells chips to hyperscalers/GPU and device makers, mostly direct plus distributors. Q2 2026 revenue by type: DRAM 71.8%, NAND 27.7%, other 0.5%. H1 2026 revenue by selling entity: U.S.A. 84,564,776 (64.1%), China 32,478,276 (24.6%), Asia ex-China 11,387,227 (8.6%), Europe 2,804,146 (2.1%), Korea 660,608 (0.5%). Major raw materials: wafers (finished 300mm bought from outside), substrates, PCBs.
- **Customer concentration:** largest customer 23.9% of 2025 revenue; Q1 2026 two largest 14.8% and 12.4% (424B4); H1 2026 customers A 13.35% (17,608,702) and B 13.03% (17,187,421), (6-K note 4(2)). Named relationships: NVIDIA technology partnership announced June 2026 (424B4); ~10 customers on long-term agreements (3-5 year term, with deposits per JoongAng [WF]).
- **Market share (IDC via the 424B4, Q1 2026, revenue basis):** HBM #1 at **56.4%**; DRAM incl. HBM #2 at 29.1%; NAND #2 at 18.5%. Samsung began HBM4 supply in Feb 2026 per JoongAng [WF]; SK hynix began HBM4 mass shipments in Q2.
- **Industry size (Gartner via H1 report):** 2025 memory US$220.1B (DRAM US$146.9B, NAND US$68.1B) of US$809.0B total semis.
- **Pricing evidence:** Q2 ASP: DRAM mid-30% QoQ, NAND mid-50% QoQ (H1 report). HBM ASP and HBM revenue share: UNKNOWN.
- **Recent events (dated):** 2026-02-09 cancelled 15.3M treasury shares; 2026-03: Google "TurboQuant" compression named as a demand risk factor (424B4); 2026-06-24 board approved ADR issue; 2026-07-10 Nasdaq ADS listing at US$149; 2026-07-13 -15.4% single day; 2026-07-29 Q2 print (record, slight miss); 2026-08-07 Y2/M17 approvals; 2026-08-19 KRW 40T buyback; rumours disclaimed 2026-08-06/10/21/22 (Solidigm pre-IPO raise, Chongqing packaging stake sale, Japan fab, Intel Ohio site). China competitor CXMT listed on Shanghai STAR in July 2026, raising CNY 57.92B [SNIPPET, from storagenewsletter-hosted article].
- **Risks the company itself flags:** capacity allocation among customers and regulatory scrutiny of memory prices ("demand for our products has exceeded our available supply"), customer concentration (US, China), AI-capex dependence, technology migration (424B4 risk factors).
- **Employee profit-sharing:** "other long-term employee benefits" (non-current) rose 1,300,847 -> 2,881,930 and "other non-trade payables" (current) 6,283,111 -> 11,800,979 in H1 2026. The bonus formula is not stated in what I read: UNKNOWN.
- **Dividend withholding for a Singapore resident (not a tax opinion):** secondary sources (Orbitax/EY alerts on the 2019 revised Singapore-Korea treaty, in force 2019-12-31) give 15% dividend WHT for portfolio holders (10% for a company holding >=25%); Korean domestic non-treaty rate 20% + 10% local surtax = 22% (Clearstream list). Which rate applies via the user's broker and the Singapore-side treatment are **UNKNOWN / not researched**. Treaty claim normally needs a residency certificate and a beneficial-owner filing; ADS holders face the depositary's own withholding mechanics. These come from search summaries [SNIPPET]; confirm with the broker.

## 9. Consensus growth estimates
`CONSENSUS (Yahoo Finance via yfinance, 2026-10-13)`; sell-side price targets and ratings deliberately not collected.
| Period | EPS avg (KRW) | # analysts | Revenue avg (KRW) |
|---|---|---|---|
| Q3 2026 ("0q") | 86,241 (low 76,216 / high 94,256) | 13 | 99.67T |
| Q4 2026 ("+1q") | 100,524 (86,210 / 113,563) | 13 | 113.73T |
| FY2026 ("0y") | 355,219 (281,586 / 400,359) | 40 | 344.26T |
| FY2027 ("+1y") | 470,324 (325,173 / 610,284) | 40 | 531.44T |
Vendor-implied growth: FY2026 EPS +488% (vs FY2025 diluted EPS 60,378); FY2026 revenue +254% vs FY2025 97.15T; FY2027 EPS +32%, revenue +54%.
**Company's own history next to it:** revenue +102% (FY24), +46.8% (FY25), +230.8% (H1 2026 YoY); diluted EPS 28,419 (FY24), 60,378 (FY25), 188,193 (H1 2026 alone, boosted by non-operating gains). Consensus FY2026 EPS 355,219 less H1 actual basic EPS 189,546 leaves ~165,673 for H2; but Q3+Q4 estimates sum to 186,765. The vendor's period estimates are therefore **internally inconsistent by ~21k/share (~12%)** (different analyst sets / inclusion of the Kioxia gain are possible). Also, Q3 revenue consensus 99.67T vs a broker Q3 note of 89.5T (DS Investment, [SNIPPET]) and a KRW appreciation of ~11% QoQ cited as a headwind. Price check: the 52w tape (-50.6% from high, -21.6% in six sessions) says the market is not extrapolating these numbers.

## 10. Data warnings & conflicts
**fundamentals.json warnings for 000660.KS: none (`warnings: []`, `errors: []`).** Despite that, the record is stale relative to the filings:
1. **Stale financials (conflict, resolved).** fundamentals.json uses FY2025 net income 42,947,902M, OCF 53,373,126M, capex 28,579,343M, FCF 24,793,783M (ties exactly to the 424B4), ROE 92.7%, trailing P/E null. Filings now give TTM net income 162.1T, OCF 126.9T, capex 36.5T, FCF 90.4T. **Use the 6-K/424B4 figures; the vendor lags by half a year.** Its "owner earnings" (28.3T) and "peg 0.18" inherit the stale base.
2. **Share count (conflict, resolved, 2.4%).** yfinance 711,075,500 (= 30 June, pre-ADR) vs 728,866,596 (issued 730,492,365 less 1,625,769 treasury, 2026-08). Market cap therefore 1,026.1T (vendor) vs 1,051.8T (mine). I use mine; buybacks since 2026-08-20 are not reflected (UNKNOWN).
3. **Net income vs operating profit.** Q2 NI 93.9T vs OP 60.5T (explained in Section 2). The "63.3T" is fair-value gain 53.24T + dividend income 10.03T, not sale proceeds as some press say; the filing's cash flow shows only 10.70T disposal proceeds in H1.
4. **D&A.** CF depreciation+amortisation FY2025 13,930,130 vs 424B4 Adjusted-EBITDA table "13,890" bn (0.3% difference; table rounds/differs in definition). Not material.
5. **Equity/liabilities basis.** The 6-K "capital management" table (liabilities 80.3T, equity 252.1T, borrowings 15.7T) is the parent-only (separate) statement, not consolidated (liabilities 86.2T, equity 262.7T, borrowings 18.6T). Do not mix.
6. **ADS vs KRX price gap** ~45% (Section 1). Unexplained; do not use the ADS price for the KRW line.
7. **Interest rate.** 00_inputs.json KRW 10y 4.286% is OECD August monthly average; fresher KOFIA close 4.369% (2026-10-06) and OECD Sept 4.45%. Reported, not substituted.
8. **Currency.** FX moved: KRW per USD 1,538 (2026-07-02 NY noon rate used in 424B4) -> 1,504.9 (ADR issue date) -> 1,341.6 (00_inputs, 2026-10-13). A ~13% won appreciation reduces KRW revenue per USD of memory sold; the company's reporting is in KRW with USD-linked pricing. The Q2 press said FX fell ~11% vs end-Q2 [SNIPPET].
9. **Consensus internal inconsistency** (Section 9). Broker Q3 estimates vary widely (OP 70T-78T vs vendor-implied higher).
10. **Transcript reliability.** Call quotes are WebFetch-summarised from a third-party site (`[WF]`).
11. **Auditor status.** H1 2026 figures are unaudited ("review ... not completed" language on the press release); the KRW 134.3T H1 profit is not audited.

**UNKNOWNs (count 17):** FY2021-22 gross profit/D&A/SBC/balance sheet/inventories/receivables/diluted shares (1 bundle); FY2021-22 OCF & capex confirmed from a primary doc; HBM revenue and ASP; HBM share trend vs the prior quarter; Kioxia stake carrying value inside the 85.3T LT investment assets; debt maturity ladder 2027-31; buyback executed to date; insider transactions after 2026-06-30; cause of the 2026-10-13 -10% day; cause of the ADS premium; capex-guidance basis (cash vs accrual); Q3 2026 results and call date (unreleased); Intel NSG purchase price and impairment history; profit-sharing formula; tone shift vs Q1 call; Singapore-resident dividend tax treatment; Oct 7-13 KTB closes.
**Conflicts logged (>2%):** 3 resolved (stale financials, share count, press mis-description of the 63.3T), 1 unresolved (consensus EPS inconsistency), 1 unexplained (ADS premium).

## Sources
1. SEC EDGAR submissions index, SK hynix CIK 0002120882: https://data.sec.gov/submissions/CIK0002120882.json (6-K list through 2026-09-18).
2. 6-K accn 0001193125-26-354777, Semi-Annual Business Report H1 2026 (K-IFRS interim FS, unaudited), filed 2026-08-18: https://www.sec.gov/Archives/edgar/data/2120882/000119312526354777/d147827d6k.htm
3. 424B4 accn 0001193125-26-299963 (ADS prospectus; audited K-IFRS FY2023-25; IDC shares; customer concentration), filed 2026-07-10: https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm
4. 6-K accn 0001193125-26-321989 (Q2 2026 preliminary results), 2026-07-29; 6-K accn 0001193125-26-303983 (call notice, 2026-07-15); 6-K accn 0001193125-26-303972 (ADR share issue result, 2026-07-15).
5. 6-Ks: -356141 (cancellation, 730,492,365 issued), -356133 (acquisition of treasury shares, KRW 40.0T), -356139 (shareholder return policy), -359825 (treasury disposal, 1,625,769 held), -339031 (Q2 dividend KRW 375), -339024 (Y2 investment), -339011 (M17 investment), -311230 (P&T7), -350177 (derivative loss 3,977,121,095,025), -336490, -382688, -341163, -385841, -359830, -394998, -311226 (rumour/clarification notices), all under https://www.sec.gov/Archives/edgar/data/2120882/ (generic user agent).
6. SK hynix Q2 2026 press release (Korean): https://news.skhynix.co.kr/q2-2026-business-results/ ; English mirror: https://www.placera.se/pressmeddelanden/sk-hynix-announces-2q26-financial-results-20260729 ; https://www.storagenewsletter.com/2026/07/30/sk-hynix-fiscal-2q26-financial-results/
7. SK hynix FY2022 results release (mirror): https://en.startuprecipe.co.kr/archives/pr-newswire/sk-hynix-reports-2022-and-fourth-quarter-financial-results ; https://www.storagenewsletter.com/?p=258475
8. Call transcript (via WebFetch summary): https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q2-2026-results-as-shares-fall-93CH-4818480
9. Korea JoongAng Daily: https://www.koreajoongangdaily.com/business/sk-hynix-posts-record-q2-profit-on-ai-demand-but-shares-slide-on-growth-doubts/12796737 ; Blocks & Files: https://www.blocksandfiles.com/flash/2026/07/29/sk-hynix-announces-extraordinarily-high-revenues-but-misses-expectations/5280499
10. Market data: yfinance (Close, auto_adjust=False; dividends; estimates), `data/fundamentals.json` (as_of 2026-10-13), `reports/runs/000660.KS_2026-10-13/00_inputs.json`.
11. KTB yields: https://biz.sbs.co.kr/amp/article/20000338551 (2026-10-06), https://biz.sbs.co.kr/amp/article/20000337916 (2026-10-01); OECD Sept: https://statisticsoftheworld.com/news/2026-10-09
12. Withholding tax secondary sources: https://taxnews.ey.com/news/2019-1078 ; https://clearstream.com/clearstream-en/res-library/tax-announcements/drs-double-taxation-treaties-concluded-by-south-korea-and-currently-in-force-1281292
13. Q3 date calendars (estimates): AJ Bell key dates / Earnings Whispers (search summary only).
14. Aggregator FY2021-22 cash flow (search summary, [SNIPPET]): https://stockanalysis.com/quote/KRX/000660/financials/cash-flow-statement/
