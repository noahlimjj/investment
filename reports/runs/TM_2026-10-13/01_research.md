<!-- pipeline:value-researcher -->
# Research dossier: TM (as of 2026-10-13)

Conventions: JPY unless stated. "bn" = billions, "M" = millions. FY2026 = year ended 2026-03-31 (Toyota's naming; "FY2027" ends 2027-03-31). Source numbers in [brackets] refer to the Sources list. "derived" = arithmetic on cited figures, no external input. `[SNIPPET]` = seen only in a search or fetch summary, not load-bearing.

## 0. Routing
**FULL**, with an industrial / financial-services split. TM is a profitable operating company (autos). Toyota Financial Services (about half of group assets and about 95% of group debt) must not be read as industrial leverage. Section 2B gives the split. Reporting currency JPY (IFRS), quote currency USD, 1 ADS = 10 ordinary shares [1].

## 1. Snapshot
Tape first (RULE 0). All prices are raw closes (`auto_adjust=False`), yfinance, run 2026-10-14.

| Item | Value |
|---|---|
| TM ADS close 2026-10-13 | **USD 188.71** (fundamentals.json 2026-10-13; 00_inputs showed 188.38 intraday at 13:52 UTC) |
| 12-month price change (raw close) | **+0.44%** (187.88 on 2025-10-13 to 188.71). Price only, excludes dividends. |
| 52-week range | close low 166.50 (2026-06-25), close high 248.29 (2026-02-13). Intraday 166.10 to 248.90. Now 24.0% below the closing high (derived). |
| Path (month-end closes) | Sep-25 191.09; Dec-25 214.06; Feb-26 242.38; Mar-26 206.09; Jun-26 168.42; Aug-26 196.54; Sep-26 183.10 |
| Tokyo line 7203.T | JPY 2,984 close 2026-10-13; 12m change +2.95% (2,898.5 on 2025-10-10, last close before 10-13 anniversary); 52w close range 2,686 to 3,944 (yfinance) |
| ADS to share | 1 ADS = 10 ordinary shares [1]. USD 188.71 / 10 = USD 18.871 per share = JPY 2,991 at 158.52 (derived), vs 7203.T JPY 2,984. Consistent. |
| FX | 00_inputs: JPYUSD 0.006314 (about JPY 158.38 per USD). yfinance JPY=X 158.52 on 2026-10-13. Both used as given; difference 0.1%. |
| Trailing / forward P/E (vendor) | 8.29 / 11.96 (yfinance via fundamentals.json). **Forward > trailing: see Section 3 and 10.** |
| Shares outstanding | 2026-03-31: 13,033,931,974 [1]. 2026-06-30: issued 14,594,987,460 less treasury 2,753,153,800 = 11,841,833,660 (derived from [2]). After Aug-Sep buybacks of 63,766,500 [3][4]: about **11,778,067,160** (derived, ignores treasury reissuances). In ADS terms about 1,177.8M. Diluted = basic (Toyota reports "basic and diluted" identical; FY2026 weighted 13,033,274k [1]). |
| Market cap | 11,778.07M sh x USD 18.871 = **USD 222.3bn**; x JPY 2,984 = JPY 35,146bn (derived). yfinance market cap USD 223.5bn (uses 11,841.8M sh). |
| Book value | Equity attributable to TMC JPY 37,308.8bn at 2026-06-30 [2] = JPY 3,151/share on 11,841.8M sh. P/B about 0.95x at JPY 2,984 (derived). Note yfinance priceToBook 15.19 is a vendor artifact. |
| 10y yield USD | 5.22% (DGS10, 2026-10-08, from 00_inputs) |
| 10y yield JPY | 00_inputs: 2.94% (OECD Aug-2026 monthly average, stale). **Fresher: MoF JGB 10y = 3.027% on 2026-10-09** (2026-10-12 Japanese holiday; 10-13 not yet published). MoF table, dated: 10-01 3.092, 10-05 3.085, 10-06 3.103, 10-07 3.111, 10-08 3.089, 10-09 3.027 [17]. The gap is 9bp (derived). Small but nonzero. I did not silently substitute. |

**EV build (industrial EV, not the vendor EV).** Vendor EV of JPY 35.0tn (yfinance) loads in about JPY 41tn of finance-arm debt and is not an industrial EV.
- Market cap JPY 35,146bn (above)
- plus non-controlling interests JPY 920.1bn (2026-06-30 [2])
- plus non-financial-services debt JPY 2,800.1bn incl. leases (2026-03-31 [1]; June figure UNKNOWN, date mismatch)
- less non-FS liquid assets JPY 14,727.6bn (cash, time deposits, bonds, monetary trusts; 2026-06-30 [2], Supplemental p.3 note 8)
- = about **JPY 24,139bn** (derived; mixed dates). Not deducted: equity-method investments JPY 5,539.5bn and FVOCI stock portfolio JPY 3,554.4bn (2026-03-31 [1]). Financial-services equity (book JPY 6,644.2bn derived, 2026-03-31) is valued as part of the group, not netted. The Quant should decide how to treat the captive-finance arm (value at book/earnings, or look through).

## 2. Financial history
Source: Toyota 20-F filings [1][5][6]. JPY bn, IFRS, FYE 31 March. The prior `sec_facts.py` output was stale (latest annual period 2025-03-31) and its FY2020 data is US GAAP and pre-split, so I rebuilt from the filings. Old file kept as `facts_sec_facts_script_stale_FY2025.json`. Full-precision values with per-value source URLs are in `facts.json`.

### 2A. Consolidated 5-year table (JPY bn)
| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | TTM to 2026-06-30 |
|---|---|---|---|---|---|---|
| Revenue | 31,379.5 | 37,154.3 | 45,095.3 | 48,036.7 | 50,684.9 | 51,957.0 |
| Gross profit (derived: rev - cost of products - cost of fin. services) | 5,971.7 | 6,313.0 | 9,368.3 | 9,578.0 | 8,463.7 | 8,706.2 |
| Gross margin | 19.0% | 17.0% | 20.8% | 19.9% | 16.7% | 16.8% |
| Operating income | 2,995.7 | 2,725.0 | 5,352.9 | 4,795.6 | 3,766.2 | 3,663.5 |
| Pre-tax income | 3,990.5 | 3,668.7 | 6,965.1 | 6,414.6 | 5,153.0 | 5,865.0 (derived: 5,153.0-1,252.2+1,963.9) |
| Net income attrib. to TMC | 2,850.1 | 2,451.3 | 4,944.9 | 4,765.1 | 3,848.1 | **4,483.8** (inflated by Q1 FY27 one-offs) |
| Net income incl. NCI | 2,874.6 | 2,493.0 | 5,071.4 | 4,789.8 | 3,985.8 | n/a |
| EPS basic=diluted (yen) | 205.23 | 179.47 | 365.94 | 359.56 | 295.25 | Q1 FY27 120.69 vs 64.56 |
| Weighted shares (M) | 13,887.3 | 13,658.4 | 13,512.8 | 13,252.5 | 13,033.3 | Q1 FY27 12,238.8 |
| D&A | 1,821.9 | 2,039.9 | 2,087.1 | 2,251.2 | 2,392.5 | 2,482.8 |
| SBC | UNKNOWN as expense line (liability JPY 0.195bn at 2026-03-31 [1]); immaterial | | | | | |
| OCF | 3,722.6 | 2,955.1 | 4,206.4 | 3,696.9 | 5,472.9 | 4,133.0 |
| Capex: PP&E ex leased equipment | 1,197.3 | 1,450.2 | 1,846.4 | 1,906.8 | 2,148.2 | 2,141.8 |
| Capex: intangibles | 346.1 | 348.3 | 334.3 | 354.2 | 378.8 | 380.7 |
| Additions to equipment leased to others (finance arm) | 2,286.9 | 1,907.4 | 2,867.7 | 2,996.9 | 2,766.4 | 2,833.5 |
| Proceeds from sale of leased equipment | 1,542.1 | 1,659.2 | 2,008.6 | 1,707.9 | 1,355.6 | n/a |
| FCF as vendors compute (OCF - all additions) | 3,722.6-1,197.3-2,286.9-346.1 = -107.7 | -750.4 | -842.4 | -3,561.5? see note | 179.6 | -1,223 (derived) |

Correction to the last row: arithmetic, derived. FY2022 = 3,722.6-1,197.3-2,286.9-346.1 = **-107.7**; FY2023 = 2,955.1-1,450.2-1,907.4-348.3 = **-750.8**; FY2024 = 4,206.4-1,846.4-2,867.7-334.3 = **-842.0**; FY2025 = 3,696.9-1,906.8-2,996.9-354.2 = **-1,561.0**; FY2026 = 5,472.9-2,148.2-2,766.4-378.8 = **+179.6** (matches fundamentals.json fcf JPY 179,572M); TTM = 4,133.0-2,141.8-2,833.5-380.7 = **-1,223.0**. The "FCF" a screener shows is distorted by two things, both caused by the captive-finance arm: gross additions to leased vehicles (rental fleet bought with debt, partly recovered via sale proceeds) and growth in finance receivables sitting inside OCF (FY2026: -2,017.2bn "receivables related to financial services" [1]). Alternative definitions for FY2026, all derived from [1]:
- OCF - PP&E - intangibles = **2,945.9**
- ... less net leased-equipment outflow (2,766.4-1,355.6 = 1,410.8) = **1,535.2**
- Non-financial-services only: OCF 5,479.4 - capex (2,119.2 + 33.2 + 365.8) = **2,961.2** (this OCF includes dividends from affiliates of 424.8 and is before the ~JPY 4tn of bond and stock purchases in investing)

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Q1 FY27 (2026-06-30) |
|---|---|---|---|---|---|---|
| Dividends paid to TMC holders | 709.9 | 728.0 | 880.2 | 1,132.3 | 1,239.0 | 651.7 |
| Buybacks (cash, net of reissuance) | 404.7 | 431.1 | 231.1 | 1,179.0 | 40.0 | **3,656.9** (Toyota Industries self-tender) |
| DPS (yen, split-adjusted) | 52 | 60 | 75 | 90 | 95 | FY27 forecast 100 |
| Cash & equivalents (consolidated) | 6,113.7 | 7,517.0 | 9,412.1 | 8,982.4 | 12,659.6 | 10,343.1 |
| Debt incl. IFRS 16 leases, consolidated (ST + LT) | 26,496.4 | 29,380.3 | 36,561.8 | 38,792.9 | 43,205.5 | 43,953.2 (17,868.7+26,084.5) |
| Equity attrib. to TMC | 26,246.0 | 28,338.7 | 34,221.0 | 35,924.8 | 39,918.9 | 37,308.8 |
| Inventories | 3,821.4 | 4,255.6 | 4,605.4 | 4,598.2 | 5,135.0 | 5,469.8 |
| Trade receivables | 3,142.8 | 3,586.1 | 3,789.4 | 3,679.7 | 3,796.0 | 4,019.6 |

Debt note: consolidated debt includes lease liabilities (FY2026 JPY 711.0bn: current 163.4, non-current 547.6 [1]). IFRS 16 lease principal sits in financing "payments of long-term debt"; total lessee-lease cash outflow JPY 484.9bn FY2026 (208.4 FY2025) includes interest of 5.0 [1]. FY2022-23 balance-sheet debt lines: lease inclusion confirmed from FY2024 only.

Lynch inventory check (derived from the table): FY2026 inventory +11.7% vs sales +5.5% vs receivables +3.2%. Inventory grew faster than sales by 6.2 points. 20-F attributes it "mainly" to exchange rates [1]. FY2025: inventory -0.2% vs sales +6.5%. Management says US inventory days are low [Q&A Q8, [7]].

Growth, company's own: revenue CAGR FY2022-26 **12.7%**; EPS CAGR FY2022-26 **9.5%**, but EPS FY2026 vs FY2024 **-19.3%**; operating income FY2026 vs FY2024 **-29.6%** (derived).

### 2B. Industrial vs financial-services split (2026-03-31, JPY bn) [1] Item 5.B
| | Non-financial services (industrial) | Financial services (TFS) | Eliminations | Consolidated |
|---|---|---|---|---|
| Total assets | 53,395.2 | 53,741.7 | -1,614.6 | 105,522.3 |
| Total liabilities | 19,022.9 | 47,097.5 | -1,618.1 | 64,502.3 |
| Equity (derived: assets - liabilities) | 34,372.4 | 6,644.2 | +3.5 | 41,020.1 incl. NCI |
| Cash & equivalents | 9,885.1 | 2,774.5 | | 12,659.6 (check: 12,659.6 OK) |
| ST + current LT debt | 976.2 | 17,042.9 | | 17,581.1 (sum is 18,019.1, see gap) |
| LT debt | 1,823.8 | 23,904.8 | | 25,624.4 (sum is 25,728.7) |
| **Total debt** | **2,800.1** | **40,947.7** | | 43,205.5 (segments sum 43,747.8; gap 542.3 = intercompany eliminations, inferred not itemised) |
| FY2026 operating cash flow | 5,479.4 | -33.7 | | 5,472.9 |
| FY2026 net income | 3,376.4 | 625.3 | | 3,985.8 |
| Interest paid FY2026 | 90.5 | 1,620.6 | | 1,685.0 |
| Segment operating income FY2026 (Q1 FY27 Supplemental) | Automotive 2,777.0, other 132.0 | 851.7 | elim 5.3 | 3,766.2 |

- Industrial debt/equity = 2,800.1 / 34,372.4 = **8.1%**; FS debt/equity = 40,947.7 / 6,644.2 = **6.2x** (both derived). Consolidated yfinance debt_to_equity 1.15 mixes the two.
- Finance receivables JPY 38,966.6bn (+15.9% in FY2026): North America 52.2%, Europe 15.4%, Asia 11.4%, Japan 10.0%, Other 11.0% [1].
- FS debt is largely secured/ABS and MTNs: secured loans (mostly receivables securitisation) JPY 8,737.8bn; unsecured bonds/MTNs of subsidiaries JPY 17,989.7bn; parent unsecured bonds JPY 1,099.5bn (2026-03-31 [1] Note 18). Assets pledged JPY 11,000bn.
- Ratings (2026-05-31, [1]): S&P A+ / A-1+, Moody's A1 / P-1, R&I AAA (long-term).
- Industrial liquidity: IR "total liquid assets excluding FS" JPY 17,418.0bn (2026-03-31) and **14,727.6bn (2026-06-30)** [2]. The fall of about JPY 2.7tn reflects the JPY 3.66tn self-tender (settled 2026-05-25) net of Toyota Industries share-sale proceeds and other flows (proceeds amount UNKNOWN). Management said after the tender it "will still be able to maintain net liquid assets of approximately 11 trillion yen" [7, Q12]. Not reconciled to my 14,727.6 - 2,800.1 = 11,927.5 (derived; date mismatch).
- Consolidated "liquid assets" (including FS) JPY 22,117.9bn at 2026-03-31 [1].

### 2C. Debt maturities, consolidated contractual (2026-03-31, JPY bn) [1] Item 5.B
Short-term debt 5,699.1 (all <1y). Long-term debt principal: total 37,506.4; <1y 11,882.0; 1-3y 15,000.0 (14,999.7); 3-5y 8,093.9; >5y 2,530.7. These are group (mostly FS) maturities, matched by finance receivables, not an industrial refinancing wall. Industrial maturities UNKNOWN as a separate schedule. Purchase commitments 2,570.9; guarantees 1,553.3.

## 3. Latest quarter & guidance
Latest reported: **Q1 FY2027 (Apr-Jun 2026), reported 2026-08-04** [2], filed 6-K accn 0001193125-26-331392. No later results. Next: Q2 expected early Nov 2026 (date not confirmed, UNKNOWN). Last 30 days of filings (2026-09-13 to 2026-10-13): 6-K 2026-10-05 (September buyback status), 6-K 2026-09-03 (August buyback status; filed 2026-09-03, just outside window), SC 13G/A 2026-09-14 (holder not read), Form 4s 2026-09-29 (all code A, below). Nothing carrying results, guidance changes or financing in the window.

| JPY bn | Q1 FY27 | Q1 FY26 | Change |
|---|---|---|---|
| Revenue | 13,525.4 | 12,253.3 | +10.4% |
| Operating income | 1,063.5 | 1,166.1 | -8.8% (margin 7.9% vs 9.5%) |
| Other finance income | 850.6 | 153.7 | +696.9 |
| Other finance costs | -285.6 | -6.2 | |
| FX gain (loss) | +112.4 | -212.4 | |
| Equity-method income | 210.7 | 141.0 | +49.4% |
| Pre-tax income | 1,963.9 | 1,252.2 | +56.8% |
| Net income attrib. | **1,477.0** | 841.3 | +75.6% (EPS 120.69 vs 64.56) |
| OCF | 536.6 | 1,876.5 | -71.4% |
| Vehicle sales (k units) | 2,395 | 2,411 | -0.7% (Japan +8.9%, overseas -3.1%) |
| Toyota+Lexus retail (k) | 2,552 | 2,643 | -3.4%; electrified 1,410 (55.3%) |
| Segments: Automotive op. inc. | 719.9 | 911.4 | -21.0% |
| Financial services op. inc. | 275.6 | 222.3 | +24.0% (loan balance) |
| North America op. inc. | +185.4 | -21.2 (loss) | swing +206.6 |

Company OI bridge Q1 (bn): FX +345.0; marketing +70.0; cost reduction -85.0 (materials/suppliers -140.0 incl. Middle East -25.0; cost reduction +55.0); expenses -190.0; other -242.6 (of which unrealised-profit adjustment -248.3). Per management: "The impact of unrealized gains and losses was approximately -250 billion yen" [7, Q1].

**Why net income jumped while operating income fell (one-offs).** Per management Q&A: "total other income amounts to 900.3 billion yen. Of this, approximately 600 billion yen relates to the sale of Toyota Industries shares. In addition, approximately 300 billion yen reflects foreign exchange gains on U.S. dollar-denominated assets held by overseas subsidiaries." Hino deconsolidation and gain on ARCHION sale "largely offset each other" [7, Q10]. Separately, 6-K 2026-06-15: gain on sale of Toyota Industries shares JPY 1,206.3bn in non-consolidated accounts (final) and JPY 576.9bn (estimate) in consolidated accounts [8]. A BEV development-project review provision is inside the "Other -190bn" expense line, amount undisclosed ("we would prefer not to disclose the specific amount") [7, Q1].

**FY2027 guidance (revised up 2026-08-04)** [2] Ex 99.1/99.2:
- Revenue JPY 54,000bn (prior 51,000; FY26 actual 50,684.9), +6.5%
- Operating income JPY 3,400bn (prior 3,000; FY26 3,766.2), **-9.7%**, margin 6.3%
- Pre-tax JPY 4,570bn; **net income attrib. JPY 3,250bn (prior 3,000), -15.5%**; EPS yen 272.17
- Equity-method income 580; DPS yen 100 (FY26 95)
- FX assumptions: 160 yen/USD (prior 150), 181 yen/EUR. FY26 actual averages 151 and 175.
- Vehicle sales 9,700k consolidated (prior 9,600k; FY26 9,595k, which included Hino 104k); Toyota+Lexus retail 10,500k (unchanged); total retail incl. Daihatsu/Hino 11,180k.
- "The impact of the 2026 Kumamoto Earthquake is currently under assessment and has not been reflected in the forecast" (verbatim, Ex 99.2 p.3). Management says it believes the quake "is covered by the risk allowance for potential production stoppages" [7, Q4].
- Verbatim summary line (Ex 99.2 p.3): "Operating income: 3.4 trillion yen (+0.4 trillion yen from the previous forecast) - Revised forecast upward, reflecting changes in the external environment such as foreign exchange assumptions, as well as marketing efforts including the establishment of alternative logistics routes to the Middle East".
- Bridge FY27 guidance vs FY26 actual, OI (bn): FX +560.0; marketing +715.0; cost reduction **-1,105.0** (materials prices/supplier-base strengthening -1,325.0 incl. Middle East -345.0; cost-reduction efforts +220.0); expenses -240.0 (labour -235.0, depreciation -180.0, R&D -70.0, other +245.0); other -296.2 (swaps -95.0, unrealised-profit -165.0, other -36.2). Ex-FX/swap total -785.0. Total -366.2 [2] Ex 99.2 p.18.

**Why forward P/E (11.96) is above trailing P/E (8.29)** (RULE 1 warning; sourced):
1. Trailing EPS (yfinance USD 22.76/ADS) is built on TTM net income of JPY 4,483.8bn (derived), which includes the Q1 FY27 non-operating gain of about JPY 900bn (Toyota Industries share sale ~600bn, USD-asset FX gain ~300bn per management). It is flattered by non-recurring items, not a sign of rising earnings.
2. Company guidance is for lower earnings: FY27 net income -15.5% and operating income -9.7% vs FY26. Given Q1 NI already booked (1,477.0), implied Q2-Q4 NI = 3,250.0 - 1,477.0 = **1,773.0 vs 3,006.6 in Q2-Q4 FY26 (-41%)**; implied Q2-Q4 operating income = 3,400.0 - 1,063.5 = **2,336.5 vs 2,599.9 (-10%)** (derived; Q2-Q4 FY26 from Supplemental: 839.5+1,191.0+569.4 and 932.0+1,257.4+817.2).
3. Drivers named by the company: US tariffs (FY26 cost JPY 1,380.0bn; North America FY26 operating loss -192.5bn; FY27 now expected about 70bn lower than the initial 1.38tn, including IEEPA refunds [7, Q2]); Middle East situation (exports about 500-600k vehicles/yr; materials cost inflation; "rising material prices... particularly for memory and aluminum"; impact "expected to continue into the second half"); higher labour, depreciation and R&D; partly offset by a weaker yen (160 vs 151). Management: material-cost impact about 1.3tn (1.2tn materials alone), "recover roughly half of that through price revisions" [7, Q6]. Management also cites underlying earning power "approximately 5 trillion yen, excluding the impacts of the Middle East situation and U.S. tariffs" (May explanation, restated Q4 [7]).
4. Vendor forward EPS (USD 15.78/ADS = about JPY 250/share at 158.4) is below company guidance EPS of JPY 272.17, so part of the gap is vendor-estimate staleness or consensus conservatism (3 analysts). Not resolved.

## 4. Earnings-call takeaways
Toyota held an online investor briefing 2026-08-04 (speakers Takanori Azuma, Chief Officer Accounting; Hiroyuki Ueda, External & Public Affairs). Source used: the company's own **Q&A summary (translated, edited, in summary form) filed on TDnet 2026-08-04** [7]. No verbatim transcript exists on SEC; I did not use third-party transcript sites. Quotes below are from that document.

1. **Quality of Q1 earnings (Q1, Q10).** Unrealised-profit adjustment about -250bn; BEV project review provision "recognized the full amount as a provision at this stage... We will subsequently reverse portions of the provision as appropriate"; amount withheld. Analysts tried to size one-offs; management declined to itemise ("avoid figures being taken out of context"). **Dodged:** the size of the BEV provision, the Q1 tariff figure ("refrain from disclosing the specific first-quarter figure").
2. **Tariffs (Q2).** "At the beginning of the fiscal year, we projected the annual impact of U.S. tariffs at 1.38 trillion yen. We now expect that impact to be reduced by 70 billion yen." Q1 includes IEEPA refunds ("Yes").
3. **Middle East (Q4).** Export volume hit now assumed -25% from September (was -50%) after rerouting; "rising material prices... have had a significant impact on earnings."
4. **Buyback and policy-held shares (Q5, Q9, Q12).** "We have recently been accelerating the sale of policy-held shares, and we determined that the proceeds should be returned to shareholders through share repurchases." "we have substantially reduced our policy-held shares over the past several years. As we continue to review our policy-held shareholdings, we will also consider the appropriate balance of share repurchases and dividends." ROE 20% target described as a "North Star" (no timeline).
5. **China (Q3, Q11).** Passenger market "approximately 80% of the previous year's level"; Toyota "approximately 72%"; equity-method profit down (GAC Toyota, FAW Toyota); production revised down about 100k.
6. **Pricing (Q6, Q8).** Intends to recover about half of the 1.2-1.3tn material-cost hit via price revisions, "not... all at once." US incentives lower than competitors; inventory days low.
7. **North America structure (Q13).** Local production, local procurement, local sales; Tacoma moves to Texas (production from 2030, 150k/yr) and a fourth India plant announced.

Prior call (FY2026, 2026-05-08): CFO Miyazaki per a machine-generated summary of press conference: "We were not able to fully offset the impact of U.S. tariffs amounting to 1.38 trillion yen"; President Kon said break-even volume increase cannot be braked ("We are not able to apply the brakes") [SNIPPET, BigGo summary, not verified against a transcript]. Tone shift vs May: the 2026-05-08 narrative led with tariffs and a Middle East hit to FY27 forecast (guided OI JPY 3.0tn); in August the lead is raised guidance, FX, alternative logistics routes, and buyback. Tariffs are now "reduced by 70bn". Not discussed at length in August: BEV targets (BEV forecast cut from 598k to 533k retail units, -10.9% [2] Ex 99.2 p.11), and the LF-ZC cancellation (decided late May 2026, disclosed in 20-F subsequent events [1]).

## 5. Capital allocation record
**Buybacks (price paid disclosed).**
- Programme resolved 2026-08-04: up to 500M shares / **JPY 1,000bn**, open-market, 2026-08-05 to 2027-08-04; plus cancellation of 200M treasury shares (1.37% of issued) [3]. Reason stated: "improve capital efficiency by carrying out flexible share repurchases in light of the market's valuations and current price level."
- Progress: Aug 28,211,700 sh for JPY 86,494,175,900 (avg JPY 3,066) [4]; Sep 35,554,800 sh for JPY 108,506,196,300 (avg JPY 3,052) [3]; cumulative to 2026-09-30 63,766,500 sh / JPY 195,000,372,200 (avg JPY 3,058, 19.5% of the cap; avg derived). October status due about 2026-11-05. Current price JPY 2,984 is 2.4% below the Sept average (derived).
- **Toyota Industries self-tender** (cross-shareholding unwind): 1,192,330,962 shares (9.17% of outstanding) bought at JPY **3,067**, total about JPY 3.657tn, tender period 2026-03-31 to 2026-04-27, settled 2026-05-25 [1][9]. Priced at a 10% discount to the lower of the prior close and 1-month average [10]. Toyota Industries was then left holding 1,242,720 TMC shares. Retirement of treasury shares: 1.2bn shares cancelled (retirement date 2026-06-30 [9]; Q1 issued shares 14,594,987,460 vs 15,794,987,460).
- History (market purchases unless noted; yen; pre-2021 amounts shown as announced) [10]: FY-by-programme totals: Nov 2015 to Mar 2016 JPY 139.3bn; May-Sep 2016 500.0bn; 2016-17 200.0bn; 2017 250.0bn; 2017-18 250.0bn; 2018 300.0bn; 2018-19 250.0bn; 2019 300.0bn; 2019-20 200.0bn; 2021 250.0bn (25.8M sh); Nov 2021-Mar 2022 150.0bn (70.4M sh); Mar-May 2022 100.0bn (46.2M); Jun-Nov 2022 185.7bn (90.3M sh); Nov 2022-Mar 2023 150.0bn (79.2M sh); May-Oct 2023 150.0bn (64.6M sh); Nov 2023-Apr 2024 100.0bn (32.1M sh); May 2024-Apr 2025 315.5bn (117.1M sh, avg about JPY 2,695, derived); tender Jul-Aug 2024 806.8bn (290.1M sh, JPY 2,781); ToSTNeT-3 Sep 2024 77.7bn (29.7M sh, JPY 2,617).
- Cash flow statement view: net repurchase FY2022 404.7bn; FY2023 431.1; FY2024 231.1; FY2025 1,179.0; FY2026 40.0 (JPY bn).

**Share count trajectory (weighted, M):** FY2022 13,887; FY2023 13,658; FY2024 13,513; FY2025 13,252; FY2026 13,033; Q1 FY27 12,239 (tender shares leave from 2026-04); about 11,778 at 2026-09-30 (derived). Share count down about 15.2% from FY2022 weighted to Sep-2026 (derived). Dilution: employee ESOP-trust and restricted-stock plans use treasury shares (6-Ks 2026-08-04, 2026-08-07); amounts small, not quantified.

**Dividends:** DPS (yen, split-adjusted) 52 / 60 / 75 / 90 / 95 for FY2022-26; FY2027 forecast 100 (interim 50, year-end 50). Payout ratio FY2026 32.1% [2]; forecast 36.7%. FY2027 forecast dividend about 3.35% of JPY 2,984 (derived). Total cash dividends FY2026 JPY 1,238.2bn [2].

**Cross-shareholding (policy-held shares) unwind** (primary [1][7][8]):
- Toyota Industries: Toyota's own 24.66% stake (74,100,604 sh) sold back to Toyota Industries in the squeeze-out step; non-consolidated gain JPY 1,206.3bn (final), consolidated gain estimate JPY 576.9bn, booked in Q1 FY27 [8]. Toyota Industries shares reclassified to held-for-sale at 2026-03-31: carrying value JPY 788.9bn [1].
- Toyota also **invested JPY 800bn in non-voting preferred shares** of the Toyota Industries offeror's parent (Toyota Fudosan group vehicle); preferred dividend 8.6% p.a. compounded; Toyota Fudosan separately invested JPY 200bn in common [10]. This is cash the buyback did not fund and an illiquid asset: terms and redemption date should be read in [10].
- FVOCI listed stocks held at 2026-03-31: JPY **3,554.4bn** (2025: 3,246.9bn). Top holdings: KDDI 989.6bn, NTT 317.5bn, MS&AD 283.8bn, MUFG 267.3bn, Suzuki 180.0bn [1] Note 9. Disposals (fair value derecognised): JPY 277.3bn in FY2026, 681.3bn in FY2025.
- Planned Q2+ items: partial sale of ARCHION shares (assets held for sale at 2026-06-30, JPY 130.9bn) [2].
- `[SNIPPET]` Reports (Angel One, 2026-02-27, citing Bloomberg-type sources) said financial institutions (SMFG, MUFG, MS&AD named as major holders) would sell about USD 19bn (about JPY 3tn) of Toyota stock with Toyota possibly buying back part: unverified in primary documents; possible supply overhang to be checked. Earlier unwinds (Denso 2023, Aisin 2024 stake cuts) are also [SNIPPET] only.
- Management quote on the 20% ROE target: denominator side "we have substantially reduced our policy-held shares" [7].

**M&A / disposals over about 5% of market cap (about JPY 1.76tn):** None as acquirer in the period. Disposals: Hino Motors business integration with Mitsubishi Fuso (MFTBC), effective 2026-04-01 (Hino deconsolidated; Hino certification-issue costs JPY 281.1bn in FY2025 [1]; JPY 3.0bn land writedown on held-for-sale assets FY2026 [1]); Toyota Industries stake (above). Q1 FY27 "equity transactions and other" included acquisition of Toyota Motor Hamura (Hino plant) shares. Impairment: BEV project review provision in Q1 FY27 (amount undisclosed); LF-ZC BEV development discontinued late May 2026, effect "not possible at this time to reasonably estimate" [1].

**Japanese withholding tax (investor fit).** Per 20-F: dividends to non-residents of listed Japanese shares are generally withheld at 15.315% through 2047 (20.42% otherwise, 3%+ individual holders excluded); Singapore treaty portfolio-investor rate 15% (treaty reductions require a filing via the withholding agent / standing proxy) [1] Item 10.E. ADS holders: depositary is Bank of New York Mellon [1]. No US withholding statement was read by me (Skeptic/Quant domain).

## 6. Insider transactions
Source: SEC Form 4s filed by TM insiders, issuer CIK 1094517 (parsed from EDGAR XML; transaction rows 106 across about 100 filings, 2026-03-27 to 2026-09-29). Form 4 reporting for TM officers and directors appears to begin only in March 2026 (earliest filing in the 12-month window is 2026-03-27); the reason (likely the foreign-insider reporting rule) is not verified. **Oct 2025 to mid-Mar 2026: Insider activity: UNKNOWN (no Form 4 data; Japanese insider filings not accessed).**

Open-market transactions (code P or S) in the window, per share prices as reported in USD per ordinary share:
- **Buy:** Kenta Kon (President, Director), 2026-08-05, **85,000 sh at USD 18.41** (about USD 1.56M; holdings after 148,100) [Form 4 accn 0000947871-26-000750]
- **Sell:** Koji Sato (Vice Chairman, formerly President), 2026-06-17, **88,600 sh at USD 17.83** (about USD 1.58M; holdings after 567,600); filed late, 2026-07-20 [accn 0000947871-26-000712]
- All other rows are code A (awards/plan acquisitions) or J (other), not open-market: e.g. 2026-06-30 awards of 368,400 sh (Toyoda), 71,500 each (Nakajima, Miyazaki), 22,800 (Kon) at USD 18.31 (consistent with the restricted-stock plan 6-K of 2026-05-08); recurring small monthly acquisitions of 3 to 500 shares (shareholding-association style purchases, pattern inferred) by about 11 officers/directors at USD 16.71-21.28.
- Net open-market 12m: one purchase, one sale, roughly offsetting in USD. `insider_pct` (vendor 0.004%) is a holding artifact, not activity; Akio Toyoda holds 24,459,675 shares after the 2026-06-30 award (Form 4, derived about 0.2% of shares).

## 7. Peers & sector multiples
One vendor (yfinance `.info`), one date (2026-10-14). Captive-finance consolidation differs by company, so EV/EBITDA and FCF yield are **not comparable across this set** and I report them as UNKNOWN for use; vendor figures shown only for the audit trail.

| Peer | Quote ccy / fin ccy | Mkt cap (USD bn) | Trailing P/E | Forward P/E | Vendor EV/EBITDA (not comparable) |
|---|---|---|---|---|---|
| TM | USD / JPY | 223.5 | 8.29 | 11.96 | 6.25 |
| Honda (HMC) | USD / JPY | 43.3 | none (n/a) | 6.72 | 7.16 |
| Ford (F) | USD / USD | 48.2 | none | 6.30 | 24.79 |
| GM | USD / USD | 73.7 | 37.67 | 5.56 | 10.90 |
| Stellantis (STLA) | USD / EUR | 16.8 | none | 3.71 | negative (artifact) |
| Nissan (NSANY) | USD / JPY | 6.3 | none | 4.22 | 15.32 |

- Excluded: Volkswagen (VWAGY forward P/E 0.33 is a vendor artifact), Hyundai (US OTC quote not found).
- Several peers show no trailing P/E (negative or missing TTM earnings), so the peer trailing column is nearly empty.
- FCF yield: UNKNOWN for all (yfinance FCF for TM -JPY 3.6tn conflicts with my derived TTM -1.2tn and FY +0.18tn; see Section 10).
- Sector multiples beyond this set: UNKNOWN.

## 8. Business facts (two-minute-drill inputs)
**What it sells and how it earns.** Toyota designs, makes and sells passenger cars, minivans, SUVs, trucks (Toyota, Lexus, Daihatsu; Hino deconsolidated 2026-04-01), through independent dealers/distributors worldwide, and earns finance and leasing margin through Toyota Financial Services (retail loans, dealer floorplan, vehicle leasing) [1]. Group strategy "best in town" regional management; hybrid-heavy mix.

**Revenue mix FY2026 (external customers) [1]:** Automotive JPY 45,201.9bn (89.2%), Financial services 4,819.0bn (9.5%), All other 664.0bn (1.3%) (derived %). Segment operating income: automotive 2,777.0bn, financial services 851.7bn (22.6% of group OI; FS is 9.5% of revenue), all other 132.0bn. By customer location: Japan 10,985.6bn, United States 18,494.0bn, other 21,205.4bn (derived by subtraction). US is 36.5% of revenue (derived).
**Units FY2026 (consolidated, k):** 9,595 total: Japan 2,082 (21.7%), North America 2,934 (30.6%), Europe 1,183 (12.3%), Asia 1,759 (18.3%), other 1,637 (17.1%). Toyota+Lexus retail 10,477k, electrified 48.1% (HEV 4,620k, PHEV 175k, BEV 243k); total retail incl. Daihatsu/Hino 11,283k [1][2].
**Market share (retail) [1]:** Japan ex-mini 50.9% (FY2026); North America 15.1% (CY2025; 14.4% CY2024); Europe 6.6%; Asia ex-China 13.0%; China sales 1.78M units CY2025 (market 27.73M).
**Customer concentration:** no single customer disclosed; dealers/distributors, fleet customers not itemised: UNKNOWN. Related-party: purchases from associates/JVs JPY 14,239.5bn FY2026, sales to them 4,095.3bn [1].
**Operating leverage / profitability series (derived):** operating margin FY2022-26 9.5%, 7.3%, 11.9%, 10.0%, 7.4%; TTM 7.1%; FY27 guide 6.3%. Company says break-even volume has risen "due to... increases in investments in human resources and future-oriented investments and the impact of U.S. tariffs" [1].
**Dated events:** US tariffs elevated since 2025, cost JPY 1,380.0bn FY2026 [1]; Middle East situation raising material costs and cutting regional exports (2026); Kumamoto earthquake (about late July 2026; Toyota's three Kyushu plants halted to 2026-08-05; Aisin Kumamoto the main supply issue) [SNIPPET: Adnkronos/S&P-type reports]; Hino-MFTBC integration effective 2026-04-01 [1]; Toyota Industries squeeze-out completed (delisted 2026-06-01, share consolidation effective 2026-06-03) [1]; LF-ZC BEV cancelled late May 2026 [1]; management change: Kenta Kon President/CEO from 2026-04-01 (Koji Sato to Vice Chairman, Chief Industry Officer), Akio Toyoda remains Chairman, Yoichi Miyazaki CFO [11][12]; Tacoma Texas production from 2030 and India fourth plant (2026-07-07 / 2026-05-11) [2]; RAV4 launch delay mentioned in an analyst's question only (unverified).
**Employees:** 367,990 at 2026-06-30 (390,927 at 2026-03-31, drop from Hino deconsolidation) [2].
**Capital intensity:** R&D JPY 1,522.8bn FY2026 (guided 1,600.0); capex (ex leased, ex rights-of-use) 2,390.6bn FY2026, guided 2,300.0bn; depreciation 1,418.9bn, guided 1,650.0bn [2].

## 9. Consensus growth estimates
CONSENSUS (yfinance, 2026-10-14, 3 analysts for annual EPS, USD per ADS; currency conversion done by vendor, treat as approximate):
- FY ending 2027-03 (0y): EPS USD 18.33 (low 16.91, high 19.53) vs year-ago USD 18.85, **-2.8%**
- FY ending 2028-03 (+1y): EPS USD 20.51 (low 20.38, high 20.58), **+11.9%** (only 2-3 analysts)
- Revenue (JPY): FY2027 JPY 53.97tn (company guide 54.0tn), FY2028 JPY 55.66tn (+3.1%). Vendor's 0y revenue growth field shows 195.6%: artifact, ignore.
- Vendor "stockTrend/LTG" fields empty or index-level (LTG 12.2% is an index value, not TM).
Company's own history beside it: EPS growth FY2022-26 CAGR 9.5% but -19.3% FY2024 to FY2026; revenue CAGR 12.7%. Company guidance FY27 EPS JPY 272.17 (-7.8% vs FY26 295.25, derived) while FY27 net income -15.5%: EPS decline is smaller than NI decline because of the lower share count (derived: 3,250.0/272.17 = 11,942M average shares implied).
No sell-side price targets or ratings collected (RULE 2).

## 10. Data warnings & conflicts
**fundamentals.json warnings (TM record, as_of 2026-10-13T23:07Z): 1 warning, 0 errors.**
1. "forward P/E (12.0) > trailing (8.3): earnings are declining, so PEG=1.56 is meaningless - VOID, use FCF yield / DCF". PEG must not be cited. Explanation in Section 3 (TTM flattered by about JPY 900bn Q1 one-offs; FY27 NI guided -15.5%).

**Conflicts and artifacts (each with cause and which figure is right):**
2. **FCF.** fundamentals.json FCF JPY 179.6bn (FY2026) vs yfinance `freeCashflow` -JPY 3.6tn (TTM) vs my derived TTM -1.2tn vs non-FS FCF +2.96tn. Cause: leased-equipment additions (2,766bn) counted as capex while sale proceeds (1,356bn) are ignored; finance-receivable growth inside OCF; the -3.6tn vendor figure is not reproducible from the filings (UNKNOWN cause). Right figure for industrial economics: Section 2A/2B definitions. Do not use consolidated FCF.
3. **Net income.** fundamentals.json net_income 3,985.8bn is net income incl. NCI; attributable to TMC is 3,848.1bn (3.6% difference, below 5% but it flows into owner earnings). owner_earnings JPY 1,084.9bn (= 3,985.8 + 2,392.5 - 5,293.3) subtracts gross leased-equipment capex; same distortion as item 2.
4. **P/B.** yfinance priceToBook 15.19 and bookValue 12.42: vendor mixes ADS/share/currency; computed P/B about 0.95x (Section 1).
5. **EV and debt-to-equity.** yfinance EV JPY 35.0tn and D/E 1.15 consolidate TFS; use the industrial figures in Section 1/2B.
6. **Debt segments vs consolidated.** Segment debt sums to 43,747.8bn vs consolidated 43,205.5bn (1.3%); gap 542.3bn attributed to intercompany eliminations (inferred; the filing gives liability eliminations of 1,618.1bn but does not itemise the loan portion).
7. **Share count.** Company's Aug-4 notice gives 11,842,234,260 outstanding ex-treasury (ex-ESOP) at 2026-06-30 vs 11,841,833,660 derived from Q1 summary (difference 0.003%); yfinance sharesOutstanding 1,184,183,366 ADS-equivalents consistent with the latter.
8. **sec_facts.py output stale.** Latest annual period 2025-03-31; FY2020 US GAAP pre-split; `diluted_share_cagr` 0.36 is a split artifact. Replaced by filing-derived `facts.json`.
9. **Rates.** 00_inputs JPY 10y 2.94% (OECD monthly, Aug) vs MoF 3.027% (2026-10-09). Gap 9bp. Fresher figure shown; per rule not substituted.
10. **Price.** 00_inputs 188.38 (intraday) vs close 188.71 (0.17%).
11. **Corrected filing.** 6-K/A (accn 0001193125-26-339000, 2026-08-07) fixed a sign/figure error in Ex 99.1: "Income tax expense, Net Income Attributable to Non-controlling Interests" changed from 760.1 to -76.0 in the Q1 net-income bridge. I used the corrected figure; the Q1 net income itself (1,477.0bn) is unchanged.
12. **Ownership artifacts.** yfinance `institutional_pct` 2.23% and `insider_pct` 0.004% reflect the ADS float only; not facts.
13. **Dividend history in yfinance** stops at 2025-03-31 (ADS USD amounts); used 20-F yen DPS instead. Trailing annual dividend rate 95 is in yen.
14. **Currency traps.** All filings in JPY millions; Form 4 prices in USD per ordinary share (about ADS/10); yfinance consensus EPS in USD per ADS; guidance EPS in JPY per share. Never mix.
15. **FY2022-23 debt lines**: lease inclusion confirmed from FY2024 (via Note 18) only.

**UNKNOWNs (count 14):** (a) SBC expense line; (b) industrial debt at 2026-06-30; (c) industrial-only maturity schedule; (d) Toyota Industries share-sale cash proceeds; (e) size of BEV-review provision; (f) Q1 tariff figure; (g) customer concentration; (h) insider activity before March 2026; (i) EV/EBITDA and FCF yield peers (not comparable); (j) cause of yfinance -3.6tn FCF; (k) Q2 earnings date; (l) holder behind 2026-09-14 SC 13G/A; (m) quantified earthquake impact; (n) unverified RAV4 delay. **Conflicts/artifacts logged: 15.** Items tagged [SNIPPET]: Bloomberg-type quotes from BigGo May summary; Kumamoto quake plant halts; 2026-02 bank share-sale report; Denso/Aisin earlier unwinds.

## Sources
1. Toyota 20-F FY2026 (FYE 2026-03-31), accn 0001193125-26-264811, filed 2026-06-10: https://www.sec.gov/Archives/edgar/data/1094517/000119312526264811/d101983d20f.htm
2. 6-K accn 0001193125-26-331392 (2026-08-04) Q1 FY2027 results: Ex 99.1 https://www.sec.gov/Archives/edgar/data/1094517/000119312526331392/d258414dex991.htm ; Ex 99.2 (presentation) .../d258414dex992.htm ; also https://global.toyota/pages/global_toyota/ir/financial-results/2027_1q_presentation_en.pdf
3. 6-K accn 0001193125-26-413029 (2026-10-05), September repurchase status: .../000119312526413029/d147797dex991.htm; and Ex 99.3 of [2] (repurchase resolution 2026-08-04)
4. 6-K accn 0001193125-26-380869 (2026-09-03), August repurchase status: .../000119312526380869/d126654dex991.htm
5. 20-F FY2025, accn 0001193125-25-142326: https://www.sec.gov/Archives/edgar/data/1094517/000119312525142326/d925022d20f.htm
6. 20-F FY2023, accn 0001193125-23-179181: https://www.sec.gov/Archives/edgar/data/1094517/000119312523179181/d360541d20f.htm
7. Toyota Q&A Summary of Q1 FY2027 investor briefing (2026-08-04, TDnet): https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260804/20260804507923.pdf
8. 6-K accn 0001193125-26-270230 (2026-06-15), gains on sale of shares: .../000119312526270230/d166826dex991.htm
9. 6-K accn 0001193125-26-183369 (2026-04-28), tender offer results: .../000119312526183369/d132275dex991.htm
10. 6-K accn 0001193125-26-130284 (2026-03-30), tender offer notice (incl. buyback history, JPY 800bn preferred): .../000119312526130284/d12865dex991.htm ; amendment 6-K accn 0001193125-26-094985
11. 6-K accn 0001193125-26-092421 (2026-03-05), executive changes: .../d115770dex991.htm
12. 6-K accn 0001193125-26-273360 (2026-06-17), board and executive structure
13. 6-K/A accn 0001193125-26-339000 (2026-08-07), correction to [2]
14. 6-K accn 0001193125-26-232785 (2026-05-20) and 0001193125-26-243215 (2026-05-28), Hino/company-split notices; 6-K accn 0001193125-26-213363 (2026-05-08) FY2026 results incl. Ex 99.2 presentation
15. Form 4 filings, issuer CIK 1094517, accn prefix 0000947871-26-; EDGAR submissions JSON https://data.sec.gov/submissions/CIK0001094517.json (retrieved 2026-10-14)
16. yfinance (raw closes, .info peers, consensus), run 2026-10-14; `data/fundamentals.json` as_of 2026-10-13T23:07Z
17. MoF Japan JGB yields CSV: https://www.mof.go.jp/jgbs/reference/interest_rate/jgbcm.csv (rows to R8.10.9 = 2026-10-09)
18. [SNIPPET] BigGo Finance summary of FY2026 press conference https://finance.biggo.com/news/US_TM_2026-05-08 ; Angel One 2026-02-27 https://www.angelone.in/news/global-market/toyota-plans-19-billion-share-sale-as-part-of-cross-holding-unwind ; Adnkronos 2026-08-03 Kumamoto quake https://english.adnkronos.com/2026/08/03/japan-auto-plant-halt-prolonged-after-kumamoto-quake/
