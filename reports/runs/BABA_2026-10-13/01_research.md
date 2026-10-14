<!-- pipeline:value-researcher -->
# Research dossier: BABA (as of 2026-10-13)

Conventions: CNY millions unless stated. FY ends 31 Mar (FY26 = year to 2026-03-31; Q1 FY27 = quarter to 2026-06-30). US GAAP, filer of 20-F/6-K. `[DERIVED]` = my arithmetic from cited figures. `[FETCH]` = seen via a summarising fetch, not the primary document. Dossier written 2026-10-14; price data 2026-10-13 close.

## 0. Routing
**FULL** (operating company; a profit-making but currently FCF-negative business). **SOTP as a cross-check overlay, not the primary template.** Reason: it is an operating company, but ~RMB 457bn of book-value investments (equity-method + non-treasury securities, see s.8) and a large net cash pile sit beside loss-making AI/new-retail units; segment data below allow a SOTP. Current holding of a Singapore-resident (SGD base) investor.

## 1. Snapshot
- **Price (raw close, 2026-10-13): US$110.535 per ADS** (yfinance history auto_adjust=False; fundamentals.json 110.53). In SGD: S$141.49 [DERIVED at SGDUSD 0.78120732, 00_inputs.json].
- **12m change (raw closes): -33.7%** (US$166.81 on 2025-10-13 -> 110.535) [DERIVED]. 52w closing range 94.81 (2026-06-26) to 179.97 (2025-10-29); intraday 91.99 to 182.50. Dividend not included (price only; FY26 regular dividend US$1.05/ADS = 0.95% of price [DERIVED]).
- Tape events: 2026-08-20 close 130.53 -> 2026-08-21 close 119.34 (-8.6%, day after June-quarter results); 2026-06-09 DoD CMC-list inclusion (s.8); low 2026-06-26.
- **Currency/units:** quote USD per ADS; reporting CNY. **1 ADS = 8 ordinary shares** (6-K accn 0001104659-26-099220). Companyfacts also contains USD "convenience translation" units (at RMB6.8980 for Mar-26); I used CNY only. Form 4 prices are per ORDINARY share (about US$14), not per ADS.
- **Listings:** NYSE BABA (ADS); HKEX 9988 (HKD) and 89988 (RMB counter); Cayman Islands company; WVR structure (Alibaba Partnership nominates directors); one vote per share (6-K accn 0001104659-26-096226). HK close 2026-10-13 HK$107.20 per ordinary share (yfinance 9988.HK) = US$109.3 per ADS-equivalent at HKD 7.8476 [DERIVED]; ADS about 1.1% above parity.
- **Share count:**
  - HKEX issued shares 19,901,959,514 at 2026-09-29 (accn 0001104659-26-111915) = **2,487.74m ADS-equivalents** [DERIVED]; this equals yfinance sharesOutstanding exactly. Includes the 710m placing shares (below).
  - US GAAP weighted Q1 FY27: basic 18,671m, diluted 19,324m ordinary (accn 0001104659-26-099220). Plus 710m placing -> basic 2,422.6m ADS, diluted 2,504.3m ADS [DERIVED].
  - US GAAP outstanding at 2026-03-31: 18,580,374,278 ordinary (XBRL CommonStockSharesOutstanding, accn 0001193125-26-231755) = 2,322.5m ADS.
  - HKEX issued (19.2bn at Jun-26) is ~0.6bn higher than US GAAP outstanding. Likely shares issued to the depositary for award vesting (treasury shares at cost RMB 37.2bn at Jun-26) - **inference, unverified**.
  - Dilutive securities: May-2024 US$5.0bn convertible, conversion price US$12.5222/share (= US$100.18/ADS, in the money; 519.1m shares); Sep-2025 US$3.168bn convertible, US$23.9244/share (US$191.4/ADS; 173.8m shares) (accn 0001104659-26-091990); HK$12.023bn zero-coupon exchangeable bonds due 2032 on Alibaba Health shares (not Alibaba shares), exchange price HK$5.92 (accn 0001104659-26-096226).
- **Market cap [DERIVED]:** 2,487.745m ADS x 110.535 = **US$274.98bn** (basic-GAAP basis US$267.8bn; diluted basis US$276.8bn).
- **EV build [DERIVED], FX CNYUSD 0.14968715 (00_inputs.json):**
  - Cash and other liquid investments RMB 474,505 (2026-06-30, unrestricted; includes cash 142,914 + ST investments 154,653 + ~176,938 other treasury investments carried in equity securities).
  - Financial debt RMB 266,530 = current bank 30,614 + non-current bank 56,007 + senior notes 115,716 + convertibles 54,905 + exchangeable 9,288 (balance sheet, accn 0001104659-26-099220). Matches yfinance totalDebt 266.53bn.
  - Net cash RMB 207,975 = **US$31.1bn** (company rate 6.7851: US$30.65bn; management says "approximately $30.7 billion in net cash" in the call, consistent).
  - Placing net proceeds HK$79,785m (= 47,871 + 31,914, accn 0001193125-26-365894) = US$10.2bn at 7.8476 arrived AFTER 30 June.
  - EV (mcap - net cash) = **US$243.9bn**; pro forma for placing cash = **US$233.7bn**.
  - Optional lines for the Quant: operating lease liabilities RMB 21,726 (Mar-26) = US$3.25bn; noncontrolling interests RMB 57,272 (Jun-26 book) = US$8.6bn; mezzanine equity RMB 7,584 = US$1.1bn; equity-method investments RMB 203,207 (book) = US$30.4bn; non-treasury equity securities and other ~RMB 254,210 [DERIVED: 431,148 total equity securities & other investments less 176,938 treasury] = US$38.1bn (book).
  - yfinance EV of US$204.2bn differs by 16%: it appears to subtract ~US$71bn of cash/liquid investments without deducting debt (my inference). Do not use it. yfinance EV/EBITDA 2.05x mixes USD EV with CNY EBITDA and is invalid.
- **Risk-free (00_inputs.json):** USD 10y 5.22% (DGS10, 2026-10-08). **CNY 10y 1.67%** (ChinaBond MOF curve, 2026-10-13 [FETCH]); corroborated by AsianBondsOnline close 1.664% on 2026-10-12 [FETCH]. Both fetched via summariser from live tables; consistent with each other (HTML table of yield.chinabond.com.cn confirmed to contain the 2026-10-13 row, but I did not machine-parse the 10Yr cell).

## 2. Financial history
CNY millions. Sources: sec_facts.py (XBRL companyfacts, 20-F accn 0001193125-26-231755 and earlier) plus my additions in `facts.json` -> `researcher_additions`. Gross profit = revenue - cost of revenue [DERIVED] (not a tagged line).

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | TTM Jun-26 [DERIVED] |
|---|---|---|---|---|---|---|---|
| Revenue | 717,289 | 853,062 | 868,687 | 941,168 | 996,347 | 1,023,670 | 1,044,971 |
| Cost of revenue | 421,205 | 539,450 | 549,695 | 586,323 | 598,285 | 616,136 | n/a |
| Gross profit | 296,084 | 313,612 | 318,992 | 354,845 | 398,062 | 407,534 | n/a |
| Gross margin | 41.3% | 36.8% | 36.7% | 37.7% | 40.0% | 39.8% | n/a |
| Income from operations (EBIT) | 89,678 | 69,638 | 100,351 | 113,350 | 140,905 | 50,150 | 30,323 |
| Adj. EBITA (company non-GAAP) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 173,065 | 76,416 | 64,901 |
| Net income, NetIncomeLoss (attrib.) | 150,578 | 62,249 | 72,783 | 80,009 | 130,109 | 103,592 | n/a |
| Net income incl. NCI | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 125,976 | 102,127 | 70,189 |
| NI to ordinary shareholders | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 129,470 | 105,904 | 73,325 |
| Non-GAAP net income | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 158,122 | 60,658 | 47,863 |
| D&A (XBRL) | 25,550 | 25,470 | 24,654 | 23,344 | 24,515 | 34,963 | see s.10 |
| SBC | 50,120 | 23,971 | 30,831 | 18,546 | 13,970 | 11,180 | 10,948 |
| OCF | 231,786 | 142,759 | 199,752 | 182,593 | 163,509 | 76,213 | 78,486 |
| Capex incl. intangibles | 43,185 | 53,324 | 34,352 | 32,929 | 85,972 | 126,937 | 155,065 (ex-intangibles) |
| OCF minus capex | 188,601 | 89,435 | 165,400 | 149,664 | 77,537 | -50,724 | -76,579 |
| Company FCF definition | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 73,870 | -46,609 | -72,464 |
| Buybacks (cash) | 773 | 61,225 | 74,746 | 88,745 | 86,662 | 7,638 | n/a |
| Dividends (cash) | 0 | 0 | 0 | 17,946 | 29,077 | 33,732 | n/a |
| Cash and equivalents | 321,262 | 189,898 | 193,086 | 248,125 | 145,487 | 131,530 | 142,914 (Jun-26) |
| Short-term investments | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 228,826 | 155,310 | 154,653 |
| Financial debt (ex-leases) | 149,153 | 141,344 | 161,354 | 170,776 | 230,703 | 259,996 | 266,530 (Jun-26) |
| Operating lease liabilities | 32,286 | 35,253 | 34,215 | 34,838 | 17,407 | 21,726 | UNKNOWN |
| Shareholders' equity (parent) | 937,470 | 948,479 | 989,657 | 986,544 | 1,009,858 | 1,060,886 | 1,049,038 (Jun-26) |
| Diluted shares (m ordinary) | 21,982 | 21,787 | 21,114 | 20,359 | 19,318 | 19,235 | 19,324 (Q1 FY27) |
| Diluted EPS (RMB/share) | 6.84 | 2.84 | 3.43 | 3.91 | 6.70 | 5.50 | n/a |
| Inventories | 27,858 | 30,087 | 28,547 | 25,460 | 18,887 | UNKNOWN | UNKNOWN |
| Accounts receivable | 27,076 | 32,813 | 32,134 | 30,686 | 31,172 | 36,020 | n/a |
| Goodwill | 292,771 | 269,581 | 268,091 | 259,679 | 255,501 | 247,378 | 242,456 |

Notes:
- Capex: FY21 to FY25 from cash-flow statements of 20-Fs (accn 0001104659-22-082622, 0000950170-24-063767, 0000950170-25-090161). FY26 126,063 (land use rights and PP&E) + 874 intangibles (6-K accn 0001104659-26-060224). TTM capex = FY26 126,063 - Q1FY26 38,676 + Q1FY27 67,678 [DERIVED]. Capitalised intangibles are included in FY columns; sec_facts reports capex as a gap.
- Net income: three definitions, all valid; see s.10.
- Debt includes convertibles and exchangeable. Operating leases are US GAAP (no finance-lease principal in financing).
- Debt maturities (senior notes principal, RMB m, **as of 31 Mar 2025, FY25 20-F**): Y1 0, Y2 0, Y3 18,492, Y4 8,400, Y5 5,000, thereafter 91,344 (total 123,236). The FY26 20-F note is unreachable (see s.10), so the schedule is not refreshed. May-2024 US$5.0bn 0.5% convertible due 2031 with holder put on 1 Jun 2029. Current bank borrowings RMB 30,614 (Jun-26); bank loan maturity ladder UNKNOWN.
- Supplier finance obligation RMB 15,361 at Mar-26 (XBRL SupplierFinanceProgramObligation).
- Restricted cash and escrow receivables RMB 42,585 (Jun-26) is excluded from "liquid" cash.
- Tag note: fundamentals.json reports FY26 (Mar-26) figures, not TTM: OCF 76,213, capex 126,937, FCF -50,724, NI 102,127, trailing P/E 26.76, forward P/E 11.9, beta 0.463, institutional_pct 0.1013, insider_pct 0.0177 (static holdings, not activity). Warnings: none. Errors: none.

## 3. Latest quarter & guidance
**Q1 FY27 (quarter to 2026-06-30), 6-K accn 0001104659-26-099220, released 2026-08-20** (primary document, read in full):
- Revenue 268,953 (+9% y/y vs 247,652). Customer management revenue (CMR) -7% reported; "+1%" like-for-like excluding contra revenue from the new business development program.
- Income from operations 15,161 (-57%), after goodwill impairment 4,458 and a provision for a EUR550m European Commission DSA fine. Adj. EBITA 27,329 (-30%); adj. EBITDA 39,143 (-14%). Net income 10,444 (-75%); NI to ordinary 10,537; non-GAAP NI 20,715 (-38%). Diluted EPS RMB 3.71/ADS (RMB 0.46/share); non-GAAP RMB 8.52/ADS (-42%). Revenue estimate beat: 268.88bn avg (LSEG) per Reuters [FETCH]; Reuters says adj. EPS 8.52 vs 10.53 est. [FETCH].
- OCF 22,945 (+11%). Capex 67,678 (+75% y/y), "fluctuations in procurement cycles, increase in CPU-compute capacity... and higher pricing of a broad range of chip components". Company FCF -44,670 (vs -18,815).
- Cash and other liquid investments 474,505 (vs 520,824 at 31 Mar); net bank borrowing proceeds 11,005 in the quarter.
- **Segments (new structure from this quarter; prior-year recast, revenue / adj. EBITA, RMB m):**

| Segment | Rev Q1 FY27 | y/y | Adj. EBITA Q1 FY27 | Q1 FY26 |
|---|---|---|---|---|
| Alibaba E-commerce Group | 205,862 | +4% | 39,749 | 39,988 |
| - China E-commerce | 110,900 | -8% (CMR 82,547, -7%) | | |
| - China Quick Commerce | 53,295 | +45% | | |
| - International E-commerce | 27,761 | -1% | | |
| - Global Wholesale | 13,906 | +7% | | |
| AI Cloud and Compute Services | 48,437 | +45% | 5,628 (11.6% margin) | 2,419 |
| AI Labs and Applications | 3,338 | +16% | -13,861 | -3,224 |
| All others | 28,803 | +1% | -3,343 | +687 |
| Unallocated / eliminations | 783 / -18,270 | | -163 / -681 | |

- AI-related product revenue RMB 12,376 (12th straight quarter of triple-digit growth). Cloud external revenue growth 45%. Annual run-rate of AI-related products ~RMB 49.5bn per call.
- Buyback: 13.4m ordinary shares (~1.7m ADS) for US$162m (avg US$12.09/share = US$96.7/ADS) [DERIVED]. 88VIP members ~64m. Employees 132,165.
- **Numeric guidance:** the release contains **no** formal revenue/EPS/capex guidance. Management statements (verbatim from the Benzinga/Webull automated transcript, 2026-08-20; ASR errors possible):
  - "our own forecast is that that same annualized revenue for AI next quarter will approach US$10 billion." (Eddie Wu; vs RMB 49.5bn = US$7.3bn now)
  - "we remain confident that we will achieve our year-end target of 30 billion ARR by the end of the year." (MaaS ARR; "surpassed 16 billion RMB" in August)
  - "we're highly confident in our ability to achieve our goal of 100 billion in external cloud revenue by 2030, and we have good visibility into achieving gross margin of 20%."
  - "The Quick Commerce business is expected to achieve overall profitability in FY29."
  - "We expect the segment loss to narrow over the coming quarters" (AI Labs and Applications) (Toby Xu).
  - "Based on average gross margins today, roughly we can break even on AI-related capex in three years... shorten that payback period, say to 2.5 years."
  - "theoretically keeping our growth rate below 33% would already enable positive cash flow. However, that is not our strategic choice at this time."
  - Capex plan: analyst cited "this 380 billion" three-year capex budget; management did not restate or update it. Reuters says Wu said the company has spent about half of the RMB 380bn 2026-29 AI plan [FETCH, bnnbloomberg.ca].

**Recent filings sweep (last 30 days, 2026-09-13 to 2026-10-13):** 6-K 2026-09-22 (AGM voting results; content not read, see s.10); 6-K 2026-09-29 (HKEX next-day return: RSU/option issuances, shares to 19,901,959,514); 6-K 2026-10-07 (September monthly return); Form 4s 2026-09-14 to 2026-10-05 (s.6); Schedule 13D/A 2026-09-22 (Alibaba's 6.1% holding in ZTO Express, 46,941,287 Class A shares). Nothing in the window carries results, guidance or financing. **Most important events just outside the window:**
- 2026-08-23/26: HK$80bn placing of 710,000,000 new ordinary shares at HK$112.70 (= US$114.98/ADS-equivalent at 7.8412 [DERIVED]), non-US persons, Reg S; closed 2026-08-26. 100% of net proceeds to "full-stack AI": ~60% (HK$47,871m) global computing infrastructure, ~40% (HK$31,914m) hyperscale AI data centres and cloud upgrade (accn 0001193125-26-361715 and -365894). Dilution: 710m / 19,175m pre-placing issued = 3.7% [DERIVED]. Not mentioned in the 08-20 call (it came 3 days later).
- 2026-06-09: Alibaba added to US DoD list of Chinese Military Companies ("CMC List"); company says it is a mistake and will "take all available legal action" (accn 0001104659-26-071542).
- 2026-08-14: exchangeable bond adjustment (above).

## 4. Earnings-call takeaways
Source: Benzinga automated transcript hosted on Webull (webull.com/news/15435452986795008). It is an automated transcript with errors (examples in s.10). Primary results numbers above come from the 6-K, not the transcript.
- **Alicia Yap (Citi) - capex and ROIC.** She asked about the capex increase, any update to the three-year RMB 380bn budget, a breakdown by use, and ROIC. Xu answered on payback (about 3 years, aiming 2.5, "industry-wide shortage in AI compute will not be resolved until at least 2030", A100/V100 still at full capacity as proof of asset life, proprietary T-Head chips, co-building data centres and customer prepayments). **Dodged:** no update to the 380bn budget, no training/inference/other breakdown given in the transcript.
- **Charlene Liu (HSBC) - e-commerce reorg.** Wu: China e-commerce faces "short-term macroeconomic challenges", 6.18 festival "aligned with our expectations"; Taobao Instant Commerce unit economics improved, non-food orders to exceed food within the next fiscal year, quick commerce profitable in FY29, potential 30% of platform GMV; international hit by "tariff policies and the geopolitical environment".
- **Yang Bai (CICC) - cloud growth.** Wu: 9 straight quarters of accelerating external cloud growth; growth to keep accelerating; EBITDA margin to improve sequentially; new-customer and renewal pricing "healthy" (price rises); US$100bn external cloud revenue by 2030, ~20% gross margin visibility.
- **Yuanli - MaaS.** Own models are the majority of MaaS revenue; third-party gross margin "highly comparable"; year-end ARR target RMB 30bn reiterated.
- **Alex Yao (JPM) - where value accrues.** Wu: near term mostly chips and AI cloud infrastructure; API monetisation of LLMs is "a short-term transitional approach"; >500,000 prior-generation T-Head chips shipped; next generation development starts in H2 2026.
- **Tone shifts and gaps (observed in the sources I read; the prior-quarter call transcript was NOT read, so "stopped talking about" is incomplete):**
  - Core e-commerce language is defensive: CMR like-for-like +1% (vs +8% like-for-like in the March quarter, release accn 0001104659-26-060224) with "weaker transaction activities"; no analyst question on CMR decline or on negative free cash flow.
  - The call framed buybacks in one sentence ("We will adjust our priorities as market conditions and strategic needs evolve"); actual repurchases were nil from Sep 2025 to Mar 2026 (6-K accn 0001104659-26-060224 shows repurchases only Apr-Aug 2025) and US$162m in Q1 FY27.
  - CMC-list inclusion, EU DSA fine and the placing were not discussed in the Q&A transcript.
  - Transcript says "EBITDA decreased 30%" while the release says adjusted **EBITA** -30% (EBITDA -14%).

## 5. Capital allocation record
- **Buybacks (ordinary shares, US$, avg per ADS = 8 x per-share) - sources: results 6-Ks:**

| Year | Shares | US$ | Avg per ADS | Source accn |
|---|---|---|---|---|
| FY22 | 480.3m | 9.6bn | ~US$160 | 0001104659-22-065269 |
| FY23 | UNKNOWN | UNKNOWN (cash RMB 74,746m) | UNKNOWN | (Q4 FY23: 172.4m sh, US$1.9bn; 0001104659-23-062243) |
| FY24 | 1,249m | 12.5bn | ~US$80 | 0001104659-24-061145 |
| FY25 | 1,197m | 11.9bn | ~US$79.5 | 0001104659-25-049400 |
| FY26 | 72.7m | 1.046bn | ~US$115 | 0001104659-26-060224 |
| Q1 FY27 | 13.4m | 0.162bn | ~US$96.7 | 0001104659-26-099220 |

  - FY25 detail: NYSE 735.2m sh for US$7,417m; HK 343.1m sh for HK$25,294m; plus 118.6m sh at US$10.10 bought privately alongside the May 2024 convertible. All FY26 repurchases were cancelled.
  - July 2026: HKEX return shows 31.3m shares repurchased and cancelled (29.79m at US$12.17 on 9 Jul; 1.54m at US$13.61 on 22 Jul; accn 0001104659-26-091990) - includes Q1 purchases. None reported in Aug-Sep.
  - Program: Feb 2024 board added US$25bn, effective through March 2027 (20-F FY24). Remaining authorisation UNKNOWN.
  - Buyback pace collapsed from ~US$12bn/yr (FY24, FY25 at ~US$80/ADS) to ~US$1bn (FY26 at ~US$115/ADS), then Aug 2026 issued 710m shares at ~US$115/ADS-equivalent.
- **Share count (US GAAP ordinary, m):** 21,699 (Mar-21), 21,357 (Mar-22), 20,526 (Mar-23), 19,469 (Mar-24), 18,474 (Mar-25), 18,580 (Mar-26; increased in FY26 despite 73m repurchased). Company stated FY25 net reduction 5.1% and FY24 5.1%. HKEX issued shares 19,901m at Sep-26 after the 710m placing.
- **Dividends:** FY24 US$4.0bn annual+special; FY25 US$4.6bn (US$1.05 regular + one-time special = US$2.00/ADS); FY26 US$1.05/ADS regular only, ~US$2.5bn, record 11 Jun 2026, payable ~13 Jul 2026 (accn 0001104659-26-060224). Cash paid RMB 17,946 / 29,077 / 33,732 (FY24/25/26).
- **Financing flow, last 15 months:** US$5.0bn convertible (May 2024, 0.5%, due 2031); HK$12.023bn exchangeable on Alibaba Health (Jul 2025); US$3.168bn convertible (Sep 2025, due 2032); HK$80bn equity placing (Aug 2026). Net proceeds of convertibles and capped calls FY26 RMB 20,967m; exchangeable RMB 10,986m. Debt up from RMB 141bn (Mar-22) to 267bn (Jun-26).
- **M&A / disposals:** nothing exceeding ~5% of market cap in the window. FY26: acquisition of additional NCI in subsidiaries RMB 16,768m (financing outflow); Trendyol local consumer services disposal gain. FY25: Sun Art (73.66% stake) sold Dec 2024 for HK$9,698m (RMB 9,054m) with **loss on disposal RMB 13,123m**; Intime also disposed (loss amount UNKNOWN); original Sun Art and Intime purchase prices UNKNOWN (not extracted). Goodwill impairments: FY26 RMB 9,515m (XBRL); Q1 FY27 RMB 4,458m (All others). Goodwill RMB 292.8bn (Mar-21) -> 242.5bn (Jun-26).
- **Investment portfolio (reported separately, book values only):**
  - Equity-method investments RMB 206,803m (Mar-26) / 203,207m (Jun-26). Ant Group: 33% equity interest at 2019 closing (20-F FY25); Ant share of profit RMB 1,563m in Q1 FY27 (1,547 a year earlier). Ant carrying value UNKNOWN.
  - Equity securities and other investments RMB 479,996m (Mar-26) / 431,148m (Jun-26), of which ~RMB 234bn / ~177bn is treasury investments counted in "liquid" cash [DERIVED]. Remaining ~RMB 246bn / ~254bn = listed + private equity stakes + debt investments [DERIVED].
  - Mar-25 split (20-F FY25): listed equity 77,630; private companies 96,167; debt securities/loans 8,785; other treasury 228,016 = 410,598. FY26 split UNKNOWN. Mar-26 XBRL: equity securities without readily determinable fair value 124,979; equity subject to contractual sale restriction 41,800.
  - Known listed holdings: ZTO Express 46,941,287 Class A shares = 6.1% (13D/A, 2026-09-22); Alibaba Health (consolidated subsidiary; exchangeable bonds reference it). Net investment gains were RMB ~74bn in FY26 non-GAAP bridge (gain on revaluation/disposals 74,416), which flatters GAAP NI.

## 6. Insider transactions
Source: all Form 4s in the EDGAR submissions feed, parsed from XML (accessions in Sources). **Coverage starts March 2026**: Form 3s were filed 2026-03-18, the earliest Form 4 is 2026-03-26. Insider activity before March 2026: **UNKNOWN** (apparently not Section 16 filers earlier; HKEX disclosure-of-interest data not checked). `insider_pct` 1.77% (fundamentals.json) is a holding, not activity.

Open-market / private purchases (code P):
| Date | Insider | Shares (ordinary) | Price/sh | US$ |
|---|---|---|---|---|
| 2026-08-24 | Joseph C. Tsai (director, chairman) | 720,000 | 14.29 (HK$ converted at 7.8412) | 10.29m |
| 2026-08-25 | Joseph C. Tsai | 720,000 | 14.47 | 10.42m |
| 2026-08-24 | Yongming (Eddie) Wu (CEO) | 350,000 | 14.24 (HK$110.70-112.40) | 4.98m |
Total purchases ~US$25.7m [DERIVED]. Tsai post-holding 114,979,168 ordinary; Wu 1,364,418 (before later RSU vesting). Purchases came 4-5 days after results and on the day the HK$112.70 placing was priced.

Sales (code S), RMB-unit caveat none; prices per ordinary share unless noted:
- Jiang Fang (Chief People Officer): 885,272 sh on 2026-09-30 at ~US$13.55 (HK$105.70-107.00) = US$12.0m; plus small sales 16,848 (Mar), 4,898 (Jun), 4,889 (Sep) = US$12.4m total.
- J. Michael Evans (President/director): Form 4 shows 720,000 "shares" at US$94.92-95.59 on 2026-06-29 (naive product US$68m). **Form 144 (accn 0001958244-26-000412) shows 90,000 ADS (=720,000 ordinary) with aggregate market value US$8,595,900.** Correct value ~US$8.6m; the Form 4 mixes share count in ordinary shares with a per-ADS price. Remaining holding 55,008 after sale.
- Xu Hong (CFO): 54,450 (Mar, US$16.07), 175,054 (Jun, US$12.15), 103,046 (Sep, US$13.68) = 332,550 sh, US$4.4m. Yu Siying (GC): 35,008 sh, US$0.5m. Jiang Fan (CEO of business group): 13,579 sh, US$0.16m.
- Total sales ~US$26m after correcting Evans [DERIVED]. Whether any are 10b5-1 or tax-related sales is not stated in the filings I read (most coincide with RSU vesting dates).
- Non-market: RSU vestings (e.g. 2026-04-01, 06-25, 09-25, 10-01), RSU grants 2026-05-29 (Wu 448,000; Xu 160,000; Tsai 120,000; Yu 120,000; Jiang Fan 248,000; Jiang Fang 60,000), director share awards 32,000 each on 2026-09-23.

## 7. Peers & sector multiples
Single vendor (yfinance via methodologies/fundamentals.py, snapshot 2026-10-13, USD market caps, CNY financials converted by the tool). **EV/EBITDA: UNKNOWN for every Chinese peer** because yfinance divides a USD EV by CNY EBITDA (BABA shows 2.05x, PDD -3.4x - invalid). FCF yield = fcf_usd / market_cap_usd [DERIVED]; fcf is last fiscal year, not TTM.

| Ticker | Mcap US$bn | Trailing P/E | Forward P/E | FCF yield | Note |
|---|---|---|---|---|---|
| BABA | 275.0 | 26.8 | 11.9 | -2.8% | FY26 FCF basis; TTM company FCF is worse |
| PDD | 117.5 | 9.3 | 6.7 | 13.5% | |
| JD | 36.2 | 18.7 | 6.5 | 2.0% | IFRS pre-tax warning from tool |
| BIDU | 28.5 | n/a (loss) | 11.1 | -8.6% | |
| TCEHY | 487.0 | 14.9 | 12.9 | 5.8% | |
| AMZN (cloud comp) | 2,794.5 | 20.8 | 24.8 | 0.3% | USD reporter; forward > trailing flagged |
BABA trailing P/E is inflated/deflated by ~RMB 74bn of non-operating investment gains in FY26 and a RMB 13bn non-GAAP bridge in the quarter; use with the s.2 non-GAAP figures. Cloud-specific peer multiples (Tencent Cloud, Huawei) are not separately listed: UNKNOWN.

## 8. Business facts (two-minute-drill inputs)
**What it sells / how it makes money.** Operates Taobao, Tmall, AliExpress, Alibaba.com/1688 and Freshippo/Taobao Instant Commerce (quick commerce); merchants pay mainly customer management revenue (advertising and commissions on GMV), plus direct-sales revenue (Tmall Supermarket, Tmall Global) and logistics. Alibaba Cloud rents compute, storage and model access (MaaS "Bailian/Model Studio"); T-Head designs proprietary AI chips (Zhenwu PPU; M890 processor; >650 external customers per 6-K). Qwen is the LLM family (>3bn downloads per call). Strategic pivot: AI cloud and applications are being funded from e-commerce cash flows, equity and debt.

**Revenue mix, FY26 (old segment structure), RMB m, accn 0001104659-26-060224:** Alibaba China E-commerce Group 554,217 (customer management 343,867; direct sales/logistics 105,518; quick commerce 78,520; wholesale 26,312); International Digital Commerce 144,170 (international retail 117,731, wholesale 26,439); Cloud Intelligence 158,132; All others 254,367 (Freshippo, Cainiao, Alibaba Health, Amap, Hujing, DingTalk etc.; down 25% on Sun Art/Intime disposal); unallocated 2,340; eliminations -89,556; total 1,023,670. **Adj. EBITA FY26:** China E-com 107,509 (FY25 193,223, -44%); International -2,051; Cloud 14,265 (9.0% margin); All others -35,737; unallocated -5,150; eliminations -2,420; total 76,416 (FY25 173,065). Q1 FY27 on new structure in s.3. Recast FY26 full-year numbers on the new structure: UNKNOWN. TTM adj. EBITA 64,901 and quarterly path: Q1 FY26 38,844 -> Q4 FY26 5,102 -> Q1 FY27 27,329 [DERIVED from releases].

**Geography.** The FY25 20-F states "substantially all of the Company's revenue is derived from within the PRC" and presents no geographic split, while International Digital Commerce revenue is RMB 144,170m (14.1% of FY26 [DERIVED]) - the two are not reconciled; geographic split: UNKNOWN.

**Concentration/market share.** Customer concentration: none disclosed in what I read (UNKNOWN). Omdia: Alibaba Cloud 38.1% of China AI cloud market, ranked first (quoted in the 6-K; period "2025"). 88VIP ~64m members. Employees 132,165 (Jun-26).

**Structure.** Cayman holding company; PRC operations through subsidiaries and VIEs (value-added telecom licences). FY25 20-F consolidating schedule (accn 0000950170-25-090161): "Major VIEs and their subsidiaries" third-party revenue RMB 98,433m = 9.9% of consolidated 996,347 [DERIVED]; VIE total assets RMB 145,114m = 8.0% of 1,804,227 [DERIVED]; a further RMB 64,331m of third-party revenue sits in "Primary beneficiaries of major VIEs". FY26 equivalent UNKNOWN (20-F not retrievable). 20-F risk language: contractual arrangements "have not been tested in a court of law"; investors hold no equity in the VIEs. ADS = 8 ordinary shares; HK dual-primary listing (9988/89988).

**Recent events (dated):**
- 2026-06-09 CMC list (DoD) inclusion; 2026-06-26 stock closes at 52w low 94.81.
- 2026-08-20 results; 2026-08-21 stock -8.6%; 2026-08 Qwen3.8-Max released with open weights (2.4 trillion parameters, per release).
- EC Digital Services Act fine: EUR550m provision in Q1 FY27 G&A.
- Q4 FY26 (Mar-26) accounting change: some merchant subsidies now recorded as contra revenue instead of S&M, depressing reported CMR and revenue growth and flattering S&M.
- Quick commerce: "continued to narrow losses substantially" (call), profitability targeted FY29; AliExpress reached operating profit in Q1 FY27 (release).
- Cloud pricing/capacity: management says compute "will continue to outstrip supply"; price rises on renewals.

## 9. Consensus growth estimates
CONSENSUS (Yahoo Finance via yfinance earnings_estimate/revenue_estimate, retrieved 2026-10-13; no price targets or ratings collected). EPS is **non-GAAP diluted EPS per ADS, RMB**. 30 analysts for EPS, 43 for revenue.

| | Consensus | Company history (own filings) |
|---|---|---|
| FY27E non-GAAP EPS/ADS | RMB 44.35 (+65.5%); range 37.59-53.07 | FY25 65.41; FY26 26.80 (-59%) |
| FY28E non-GAAP EPS/ADS | RMB 62.15 (+40.1%); range 40.94-80.85 | FY27E still below FY25; FY28E just below FY25 |
| Current-quarter (Dec-26) EPS | RMB 10.90 (vs 4.36 year ago) | Q1 FY27 actual 8.52 vs 14.75 |
| FY27E revenue | RMB 1,118.3bn (+9.25%) | FY26 +2.7%; FY21-FY26 CAGR 7.4% [DERIVED]; Q1 FY27 +8.6% |
| FY28E revenue | RMB 1,264.0bn (+13.0%) | |
Consensus EPS was revised down over 90 days for FY27 (45.56 -> 44.35). The consensus expects a profit trough in FY26-Q2 FY27 then recovery; the company's own record is a 59% non-GAAP EPS fall in FY26 and -42% in Q1 FY27.

## 10. Data warnings & conflicts
**fundamentals.json BABA record:** warnings `[]`, errors `[]`. (It reflects FY26, not TTM - see s.2.)

**Source conflicts (resolved unless stated):**
1. **Share count 10x:** sec_facts `shares_outstanding_latest` 1,858,037,427 (dei:EntityCommonStockSharesOutstanding) is 1/10 of us-gaap CommonStockSharesOutstanding 18,580,374,278 ordinary (= 2,322.5m ADS). dei value wrong; use ordinary figures above. Override recorded in facts.json.
2. **Net income:** sec_facts FY26 103,592 (NetIncomeLoss, attributable before mezzanine accretion) vs fundamentals 102,127 (ProfitLoss, incl. NCI) vs 105,904 (to ordinary shareholders, EPS numerator). Difference = NCI loss 1,465 and mezzanine accretion. All consistent; the choice is the Quant's. FY25: 130,109 vs 125,976 vs 129,470.
3. **D&A:** XBRL DepreciationDepletionAndAmortization FY26 34,963 vs fundamentals 47,118 (+35%) vs company recon (depreciation/impairment of PP&E and land-use lease cost 37,067 + amortization/impairment of intangibles 5,079 = 42,146). Cause not resolved. fundamentals owner earnings (22,308 RMB m) used 47,118; with 34,963 it is 10,153. Also NI includes ~RMB 74bn investment gains, so owner earnings from NI are unreliable.
4. **Capex vs FCF:** fundamentals capex 126,937 (FY26) vs TTM 155,065 (+22%); FY26 OCF-capex -50,724 vs company FCF -46,609 (company excludes campus construction and buyer-protection deposits). Not an error; definitional.
5. **EV:** yfinance US$204.2bn vs my build US$243.9bn (16%); cause likely debt omission (inference). yfinance EV/EBITDA invalid (currency mix).
6. **Q1 FY27 operating income:** yfinance 19,619 vs release 15,161: yfinance adds back the 4,458 goodwill impairment (15,161 + 4,458 = 19,619).
7. **Transcript vs release:** transcript says "US$162 billion" repurchased (release: US$162 million), "EBITDA decreased 30%" (release: adj. EBITA -30%), mangles net cash after "46 point". The Reuters/BNN statements (half of RMB 380bn spent; "break even... within the next three years") are [FETCH]. Chairman named "Zhu Cai" (= Joseph Tsai, transliteration) - trivial.
8. **Evans Form 4:** unit mismatch (ordinary share count, per-ADS price); resolved with Form 144 (90,000 ADS, US$8.6m).
9. **Shares HKEX issued vs US GAAP outstanding:** 19.2bn vs 18.6bn-ish; cause inferred (depositary/treasury), not verified.
10. **Geography:** "substantially all revenue from the PRC" vs International Digital Commerce 14.1% of revenue - unresolved.

**UNKNOWN list (13):**
(a) FY26 20-F main document and exhibits return HTTP 404 on EDGAR (accn 0001193125-26-231755; only XBRL via companyfacts works) -> FY26 inventories, equity securities breakdown, VIE schedule, bank-loan and senior-note maturity ladder, geographic data;
(b) FY23 buyback shares/US$/average price;
(c) remaining buyback authorisation;
(d) EV/EBITDA for all peers;
(e) insider transactions before March 2026;
(f) Sun Art/Intime purchase prices and Intime loss;
(g) customer concentration;
(h) Ant Group carrying value;
(i) prior (May 2026) call transcript - so "what management stopped saying" is partial;
(j) geographic revenue split;
(k) FY26 full-year recast on the new segment structure;
(l) contents of 6-K 2026-06-18 (accn 0001193125-26-274928), 2026-08-06 (AGM notice, 0001193125-26-336936; 404), and 2026-09-22 AGM voting results (not read);
(m) company adj. EBITA FY21-FY24 and non-GAAP NI FY21-FY24 (not collected).

**Other warnings:** (i) The currency of every Form 4 price is per ordinary share, not per ADS (except Evans); (ii) OECD/FRED USD 10y 5.22% dated 2026-10-08 is 5 days older than the price; (iii) CNY 10y sourced via fetch summaries (see s.1); (iv) a coordinator note said an outside agent wrote files into this folder; I did not read or use `_external_unverified/`.

## Sources
1. SEC submissions JSON, CIK 1577552: https://data.sec.gov/submissions/CIK0001577552.json
2. SEC XBRL companyfacts: https://data.sec.gov/api/xbrl/companyfacts/CIK0001577552.json (20-F FY26 accn 0001193125-26-231755)
3. 20-F FY22 accn 0001104659-22-082622; FY24 accn 0000950170-24-063767; FY25 accn 0000950170-25-090161 (baba-20250331.htm)
4. 6-K Q1 FY27 results (2026-08-20): accn 0001104659-26-099220, tm2623667d1_ex99-1.htm
5. 6-K FY26 / Mar-quarter results (2026-05-13): accn 0001104659-26-060224; dividend announcement 0001104659-26-060229
6. 6-K placing: accn 0001193125-26-361715 (launch/pricing), 0001193125-26-365894 (completion); 6-K HKEX returns: 0001104659-26-091990 (Jul), -101020, -105208 (Aug), -111915, -114191 (Sep), -082647, -078252 (Jun)
7. 6-K exchangeable bond adjustment 0001104659-26-096226; conversion rate adjustments 0001104659-26-075717; CMC list 0001104659-26-071542; AGM record date 0001104659-26-085556
8. 6-K prior results: FY25 0001104659-25-049400; FY24 0001104659-24-061145; FY23 0001104659-23-062243; FY22 0001104659-22-065269
9. Form 4s (38, 2026-03-26 to 2026-10-05), e.g. 0001193125-26-361902, -361711, -364044, -291402, -411206, -405899; Form 144 0001958244-26-000412; Schedule 13D/A 0001104659-26-109479
10. Transcript: https://www.webull.com/news/15435452986795008 (Benzinga automated transcript, 2026-08-20)
11. Reuters via BNN Bloomberg [FETCH]: https://www.bnnbloomberg.ca/business/company-news/2026/08/20/alibabas-quarterly-revenue-up-9-misses-adjusted-profit-due-to-heavy-ai-spend/
12. China 10y: https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=en_US&nameType=1 (2026-10-13) [FETCH]; https://asianbondsonline.adb.org/china/ (2026-10-12) [FETCH]
13. yfinance (history auto_adjust=False, estimates, info) retrieved 2026-10-13/14; data/fundamentals.json (as_of 2026-10-13T18:47Z BABA; peers 18:57Z)
14. /Users/User/Desktop/Projects/Investment/reports/runs/BABA_2026-10-13/00_inputs.json and facts.json (`researcher_additions`)
