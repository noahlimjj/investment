<!-- pipeline:value-researcher -->
# Research dossier: 402340.KS (SK Square, KRX, KRW) (as of 2026-10-13)

Provenance key: [IR-NAV] = https://www.sksquare.com/kor/ir/nav.do (read 2026-10-14 SGT, NAV as of 2026-10-12); [Q2deck] = SK Square "Q2'26 Portfolio Update" PDF (IR fidx=729, 2026-08-14); [Q1deck] = Q1'26 deck (fidx=712, 2026-05-14); [BR25] = FY2025 business report (사업보고서 제5기, IR fidx=686, filed 2026-03-17); [SA25] = FY2025 separate-FS audit report (IR fidx=683, DART rcpNo 20260311800910, 2026-03-11); [RET] = IR shareholder-return page https://www.sksquare.com/kor/ir/return.do; [NAVER] = Naver Finance mobile API / WiseReport (secondary). DART's own search is not scriptable here and there is no API key. The IR site hosts the same DART-filed PDFs, so they are used as the primary source. Units: KRW billion (bn) / trillion (tn) as printed in decks; "mn" = KRW million as in DART statements.

## 0. Routing
SOTP. Investment holding company (spun out of SK Telecom Nov 2021). SK hynix is 234.49tn of 239.30tn NAV (98.0%) on 2026-10-12 [IR-NAV]. The user also holds SK hynix directly, so exposure overlaps. Because SK hynix is accounted for under the equity method, consolidated earnings are mostly hynix profit, not cash earnings of SK Square. The cash-earning layer is the holdco's dividend income.

## 1. Snapshot
- Quote ccy KRW. Reporting ccy KRW (K-IFRS). No ADR. 10y yield KRW 4.286% (OECD IRLTLT01KRM156N, 2026-08-01, from 00_inputs.json). USD 10y 5.22% (DGS10, 2026-10-08).
- PRICE CONFLICT (see s10): yfinance raw close 2026-10-13 = 857,000 (00_inputs.json). KRX regular-session close per NAVER = 867,000 (-117,000, -11.89% vs 984,000 on 2026-10-12). After-market (NXT) 20:00 = 868,000. Gap 1.2%. The 2026-10-12 official close of 984,000 is confirmed by [IR-NAV] and WiseReport. yfinance has no row for 2026-10-12.
- 12m price change (yfinance raw closes): 245,500 (2025-10-13) -> 857,000 (2026-10-13) = +249.1%. Using the NAVER 867,000 close = +253.1%. [WiseReport 2026-10-12 shows 1Y +298% on adjusted prices, not used.]
- 52w range (yfinance raw close): 195,300 (2025-09-26) to 1,970,000 (2026-06-22). Intraday NAVER range 229,000 to 2,338,000. Price is -56.5% from the closing high (857,000 vs 1,970,000). Month-end closes: 2026-04 841,000; 05 1,233,000; 06 1,697,000; 07 1,038,000; 09 1,139,000. Last three sessions: 1,050,000 (10-08, yfinance) -> 984,000 (10-12) -> 867,000 (10-13).
- SK hynix (000660.KS) tape: 415,000 (2025-10-13) -> 1,443,000 yfinance / 1,456,000 NAVER (2026-10-13), 52w close high 2,919,000 (2026-06-22), 10-13 move -9.3% (NAVER). Both stocks sold off together; SK Square fell more (-11.9% vs -9.3%).
- Market cap: 857,000 x 131,774,099 shares = 112.93tn KRW (yfinance marketCap 112,930,402,074,624). At 867,000 x 131,774,099 = 114.25tn (DERIVED; NAVER integration page showed 114.3781tn, an intraday value).
- Shares: issued 131,923,998; treasury 149,899 (0.11%); outstanding 131,774,099 ([NAVER WiseReport 2026-10-12]; yfinance sharesOutstanding 131,774,099 matches). Diluted: derivative/PRS items are not share-settled; stock options immaterial (stock-option reserve 16,199mn at FY25 [SA25]). Diluted EPS FY25 66,476 KRW vs basic 66,713 [BR25].
- EV: not meaningful for a holdco. Holdco net cash 0.80tn, 0 borrowings [Q2deck, IR-NAV]. yfinance enterpriseValue 111.80tn is a consolidated figure that nets 1.40tn cash; the Quant should use SOTP, not EV.
- NAV and discount (company-reported) [IR-NAV, as of 2026-10-12]: total NAV 239.3tn, NAV/share 1,813,952 KRW, price used 984,000, discount 45.8%.
- Researcher arithmetic on the 2026-10-13 tape (label: DERIVED, not company-reported): SK hynix 146,100,000 shares x 1,456,000 (NAVER close) = 212.72tn. Adding other portfolio 4.01tn (carried from 10-12 table) and net cash 0.80tn gives about 217.5tn NAV, or about 1,649,000 KRW/share on 131,923,998. At 867,000 that is a 47.4% discount. At 857,000 it is 48.0%. The Quant should rebuild this. The non-hynix lines are last-deal or book values and did not change.

## 2. Financial history
Consolidated (K-IFRS, KRW mn) [BR25 pp.55-59]. FY2021 and FY2022 not collected (UNKNOWN). Note NAVER's "revenue" line includes equity-method income (FY25 104,556 x 100mn = 10.46tn) and is NOT comparable to DART operating revenue.

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating revenue (excl. equity method) | 2,008,116 | 1,649,858 | 1,411,521 |
| Equity-method gain/(loss) | (2,050,020) | 4,106,802 | 8,930,435 |
| of which SK hynix equity gain | UNKNOWN | 4,193,866 | 9,037,459 |
| Operating income | (2,333,631) | 3,920,647 | 8,797,421 |
| Pre-tax income | (2,596,012) | 3,853,402 | 9,507,267 |
| Net income | (1,314,834) | 3,650,515 | 8,818,695 |
| NI to owners | (1,287,048) | 3,713,971 | 8,824,131 |
| Diluted EPS (KRW) | (9,259) | 27,716 | 66,476 |
| Gross profit | n/a (holdco; no COGS line) | n/a | n/a |
| D&A | 82,353 | 89,011 | 74,572 |
| SBC | UNKNOWN (standalone stock comp: 2,031 FY24; nil FY25 [SA25]) | | |
| OCF (consolidated) | UNKNOWN | UNKNOWN | 387,202 (yfinance via data/fundamentals.json, not DART-verified) |
| Capex | UNKNOWN | UNKNOWN | 38,634 (yfinance, same caveat) |
| Buybacks (cash, consolidated CF) | 265,607 | 154,602 | 190,033 |
| Dividends paid | 38,024 | 2,388 | 1,800 |
| Cash & equivalents (consolidated) | 1,270,893 | 1,368,298 | 1,310,718 (plus ST financial instruments 317,762) |
| Borrowings | 47,699 (ST 46,894 + LTD current 146 + LT 659) | 16,214 | 0 |
| Lease liabilities | 98,839 (33,799+65,040) | 55,298 | 112,827 (26,166+86,661) |
| Total equity | 15,816,517 | 19,585,415 | 27,983,163 (owners 27,636,531) |
| Issued shares (year-end) | 138,981,036 | 134,749,960 | 132,087,115 |

Consolidated FY25 notes: deferred tax liability 1,142,557mn; derivative financial liabilities 283,978mn (see s5); held-for-sale assets 284,637mn and liabilities 164,742mn [BR25 p.57-58].

Standalone holdco (the cash-earning layer) [SA25; BR25 p.56]:

| KRW mn | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating revenue | 177,597 | 177,465 | 357,572 |
| of which dividend income | UNKNOWN | 176,807 | 355,998 |
| Operating costs (head-office cost) | UNKNOWN | 64,932 | 56,920 |
| Operating income | 94,005 | 112,533 | 300,652 |
| Net loss (after investment impairments) | (314,171) | (179,595) | (105,572) |
| OCF | UNKNOWN | 72,916 | 368,496 |
| Cash + ST fin. instruments | UNKNOWN | 536,287 (456,287+80,000) | 769,014 (534,014+235,000) |

Head-office cost FY2025: 56,920mn = employee 30,223 + fees 17,171 + depreciation 4,255 + advertising 297 + other 4,974 [SA25 income statement]. Interest paid 101mn; no borrowings. Hynix dividend received FY25: 354,877mn (cash dividend on 146.1M shares; equals ~2,429 KRW/share) [BR25 note 10].

2026 interim (KRW bn) [Q1deck, Q2deck]: Q1 revenue 300.3, equity-method gain 8,312.6, operating income 8,278.3, NI 8,374.7, holdco dividend income 273.9. Q2 revenue 328.5, equity-method gain 19,267.2, operating income 19,235.4, pre-tax 19,667.8, NI 18,675.0; holdco dividend income 54.8; holdco cash 801.2, borrowings 0.0; consolidated assets 58,651.0, liabilities 3,639.2, equity 55,011.8. Consolidated cash and equivalents 1,319.5; current borrowings 4.3; no long-term borrowings. Q2 figures are management estimates pre-final audit ("외부감사인의 회계감사가 완료되지 않은 상태" disclaimer in deck); the auditor review cover was filed 2026-08-14. [NAVER Q2 NI 186,750 x 100mn = 18.675tn agrees.] H1 2026 NI 27.05tn (8,374.7 + 18,675.0 = 27,049.7bn; Asiae reports 27.0498tn).
Note: Q1 deck says dividend income was "834억 higher YoY" because subsidiaries raised shareholder returns, but Q2 holdco dividend income was only 54.8bn. Hynix's June payment is the likely driver; hynix's own Q3 return decision is pending (see s3).

Share count trajectory (issued): 138,981,036 (FY23) -> 134,749,960 (FY24) -> 132,087,115 (FY25) -> 131,958,386 (after 2026-04-01 cancellation, per Q1/Q2 NAV tables) -> 131,923,998 (after 2026-07-31 cancellation of 34,388 shares, per IR-NAV 2026-10-12). Treasury shares at FY25: 210,802 [SA25 note 14]; 149,899 on 2026-10-12 [NAVER].

## 3. Latest quarter & guidance
Latest reported quarter: 2Q26 (Apr-Jun 2026), published 2026-08-14. Next: 3Q26 (expected mid-Nov 2026; date UNKNOWN). Nothing newer is on IR as of 2026-10-14.

SK Square 2Q26 [Q2deck, KRW bn]: see s2. Verbatim/translated deck lines:
- "SK하이닉스 실적 호조 및 포트폴리오사들의 수익성 개선으로 연결 기준 영업이익은 전년 比 17.8조원 증가한 19.2조원 기록".
- "'26.2Q NAV는 SK하이닉스의 지분 가치 상승 등으로 '26.1Q比 268.9조 증가한 392.0조원 기록". NAV 391.98tn: SK hynix 387.17, TMAP 1.46, SK Shieldus 1.02, SK Planet 0.61, Wavve 0.26, other 0.66, net cash 0.80. Shares 131,958,386; NAV/share 2,970,469 KRW.
- Shareholder return: "'26년 주주환원(총 3,100억원 규모) 실행경과 ... 2,400억원 현금 배당 및 자사주 매입/소각 완료 ※ 잔여 금액(700억원)은 '27년 실행 예정".
- ICT portfolio operating loss of the 4 main consolidated subsidiaries: -28.2bn (2Q26) vs -11.7bn (2Q25); H1 cumulative -28.5bn. Small-company results (KRW bn, 2Q26): TMAP revenue 74.4, NI 0.1; SK Planet revenue 61.7, NI -2.2; FSK L&S revenue 72.8, NI 4.2; 11st revenue 97.0, NI -9.0 [Q2deck p.8].
- SK hynix (investee) 2Q26 per deck: revenue 79.3tn (+51% QoQ, +257% YoY), operating profit 60.5tn (+61% QoQ, +557% YoY, margin 76%). The deck also states "추가 주주환원 방안을 적극 검토 중이며, 구체적인 사항은 3분기 중 확정하여 발표 예정임" (hynix to announce additional shareholder returns in 3Q) and "10여개 고객사와 LTA(장기공급계약) 협상 마무리".
Numeric company guidance for SK Square earnings: none (holdco). Policy targets: see s5.
Filings in last 30 days (2026-09-14 to 2026-10-13): the NAVER/KOSCOM feed lists only a futures price-limit notice (2026-10-13, "주식선물 2단계 가격제한폭 확대요건 도달(하락)"). The most recent substantive items: 2026-08-19 SK hynix treasury-share acquisition/cancellation decisions and 2026-08-07 hynix cash-dividend decision (listed as "자회사의 주요경영사항"); 2026-08-13 change of listing for share cancellation; 2026-08-14 2Q results and review reports. DART's own list could not be queried (see header), so absence of other filings is UNVERIFIED.
Hynix events that load on NAV: ADR listing on Nasdaq 2026-07-10 at $149, first-day close $168.49 (press, daum 2026-07-13) [SNIPPET-grade, not confirmed in filing]; new-share issuance of up to 17.79M shares raising ~40tn KRW; total hynix shares 712,702,365 -> 730,492,365 [same press].

## 4. Earnings-call takeaways
No transcript found (Quartr page is an AI summary with no transcript; SK Square IR hosts decks only). Q&A: UNKNOWN. Tone from deck text: management's 2Q deck leads with record profit and NAV; it adds NAV-discount targets in other materials (see s5). Not collected: what was dropped versus prior call.
What the decks stopped saying: the Q1 deck contained "배당, 자사주 매입 · 소각 등 추가 주주환원 적극 검토해 연내 실행 방안 마련 계획" (hynix: additional returns by year-end); the Q2 deck tightened it to "3분기 중 확정하여 발표" (during 3Q). The Q1 NAV table listed Onestore (last deal value 2024Q1); the Q2 table drops Onestore (sale of the stake, see s8).
Press items on discount targets [Asiae English 2026-08-14, WebFetch summary, verify]: target "reduce the NAV discount rate below 30% by 2028"; NAV discount "38%" vs 50.1% a year earlier. [SNIPPET-grade; the company IR series shows 36.1% minimum on 2026-06-23, 45.8% on 2026-10-12, so the "38%" is a point-in-time figure.] A March 2026 itwiki item cites a 50% 2027 target already met [SNIPPET].

## 5. Capital allocation record
Shareholder-return policy [RET; Mar-25-2026 IR deck fidx=687]: 2026-28 "향후 3년간 경상 배당수입의 30% 이상" plus "투자 성과의 일부"; method "자사주 매입 후 전량 소각 또는 현금배당". 2026 plan: 310bn total = cash dividend 200bn + buyback 110bn (40bn in 2026, 70bn in 2027). Caveat in deck: details may change under Commercial Act limits, large investment, or major change in business environment. The policy ties returns to dividend income, not explicitly to a NAV-discount trigger (the discount targets are in separate press/valuation-plan material; the Nov-24-2025 "기업가치 제고 계획 (2025)" deck, IR fidx=?, was not read).
Execution [RET]: buyback board approval / executed (bn): 2023 310/267; 2024 200/155; 2025 200/190; return as % of dividend income 30.7% (2023), 56.5% (2024), 56.6% (2025). Each buyback was cancelled in full: 110bn done 2023-06-14, cancelled 2023-10-04; 200bn done 2024-02-08, cancelled 2024-04-02; 100bn done 2024-04-26, cancelled 2025-01-06; 100bn done 2025-02-24, cancelled 2025-04-01; 100bn done 2025-09-26, cancelled 2025-11-24; 100bn done 2026-02-09, cancelled 2026-04-01; 40bn done 2026-05-13, cancelled 2026-07-31. Cumulative buyback 750bn; cumulative cancelled shares 9,509,185 (6.7% of initial issue).
Average price paid (DERIVED from [SA25] cash outflow / shares): FY2024 154,602mn / 2,261,904 shares = about 68,347 KRW; FY2025 190,033mn / 1,440,941 shares = about 131,885 KRW (acquired for "주가 안정을 통한 주주가치제고" via trust). FY2023 shares acquired UNKNOWN. Spot price now 857,000-867,000, so all 750bn of buybacks were executed at prices far below today's, though today's price is 5-6x the 2025 average buyback price.
Dividends: first cash dividend 2026 interim DPS 1,550 KRW, total 204,302,634,050 KRW, record date 2026-05-15, paid 2026-06-05, board 2026-04-30; funded from capital reserve reduced into retained earnings, so "과세소득에 해당하지 않습니다" (not taxable income) [Q1-dividend deck fidx=710]. No dividends 2021-2025 (return page shows 0). Naver lists DPS 1,544/1,550; Edaily says 1,500 [SNIPPET]. Use 1,550 (company document).
M&A and disposals (BR25, SA25): 2025 sold ID Quantique to IonQ for 2,797,720 IonQ shares valued 110,513mn at acquisition; sold Dreamus 17.3% for 30,349mn then lost control; sold Incross 36.1% to SK Networks; sold Carrot Insurance 10% for 36,000mn; collected 450,000mn deferred proceeds (earlier stake sale); injected 390,000mn cash into SK Planet to buy 11st stakes (2025-11); recognised 274,708mn impairment on 11st; impairments also on Dreamus (34,225mn), Incross (19,960mn), Sparkplus (18,069mn), Wavve Americas (25,496mn). 11st had a 500bn FI put (drag-along) settled 2025: SK Planet paid 467,294mn, all distributed to the investor; derivative liability of 380,995mn extinguished.
Debt maturities: none. Holdco borrowings 0.0; consolidated long-term borrowings 0 at FY25 and 2Q26 (current 4.3bn) [BR25, Q2deck]. Contingent derivative-type liabilities at FY25 (mn): TMAP drag-along put 122,487; Onestore PRS 120,863; Wavve CJ ENM put on convertible bond (up to 125,000mn face) 40,628; total 283,978 [SA25 note 12]. Onestore PRS exposure after the 2026-06 stake sale: UNKNOWN. Guarantee: performance guarantee on TMAP navigation-software supply contract (amount UNKNOWN) [SA25 note 26].
Regulatory constraint on the SK hynix stake: Fair Trade Act Art. 18 requires a holding company to hold at least 20% of listed subsidiaries (press, daum 2026-07-13). SK Square holds 146,100,000 shares: 20.1% FY25 [BR25], 20.5% end of 1Q26, about 20.0002% if 730,492,365 hynix shares are outstanding (press). Headroom: 0.0002%. The press says falling below 20% would end its holding-company status for hynix. SK hynix buybacks/cancellations raise the ratio automatically. Whether SK Square can ever sell hynix shares or must buy more is unverified. Independent note: effective equity-method ratio 20.82% at FY25 because hynix holds treasury shares [BR25 note 10].

## 6. Insider transactions
Insider activity: UNKNOWN (no transaction data available). DART officer/major-holder reports could not be queried. Holdings only (not activity): SK Inc and 10 related persons own 42,502,379 shares = 32.22%; National Pension Service 11,662,940 = 8.84%; BlackRock Fund Advisors and 13 others 6,607,143 = 5.01% [WiseReport, as of 2026-10-12]. The BR25 table shows SK Inc stake at 32.05-32.16% in 2025 (rises only because of cancellations). Foreign ownership 46.2-46.5% [NAVER].
Company's own repurchases are in s5.

## 7. Peers & sector multiples
UNKNOWN. A consistent peer set (SK Inc 034730, LG Corp 003550, Samsung C&T 028260) with NAV discount, P/E, EV/EBITDA and FCF yield from one vendor and date was not sourced. yfinance returned market caps only (trailing PE/PB null for all), so no multiples are given. Peer NAV discounts are a Quant/Skeptic follow-up. Own-history comparator is in the table below.

NAV discount history, SK Square (company series [IR-NAV]):
- Quarterly (period end): 2021Q4 63.9%; 2022 Q1-Q4 66.6/72.8/74.1/74.5; 2023 Q1-Q4 72.8/74.4/75.6/73.0; 2024 Q1-Q4 66.9/67.1/65.8/65.7; 2025 Q1-Q4 62.8/50.1/52.6/51.5; 2026Q1 50.0%. (2026Q2 on IR: not listed in the quarterly string; daily series 2026-06-30 = 42.92%.)
- Daily series 2025-01-02 to 2026-10-12 (429 observations, in facts.json): mean 52.9%, median 52.1%, max 66.77% (2025-04-09), min 36.12% (2026-06-23). By period (min/mean/max): 2025H1 46.6/62.3/66.8; 2025H2 48.0/54.4/61.6; 2026Q1 44.2/48.0/53.6; 2026Q2 36.1/46.7/53.0; 2026Q3 37.9/43.6/48.8; Oct 1-12 2026 41.3/43.7/45.8.
- Latest 45.8% (2026-10-12). DERIVED estimate on 2026-10-13 tape about 47-48% (s1).
- NAV method per company: listed holdings at market; unlisted at last deal value or book value (TMAP 2022Q3; Shieldus 2023Q3; Wavve 2025Q3; SK Planet net assets 2025Q4). Deferred tax liability (1,142,557mn consolidated at FY25) and holdco running costs are not deducted in the company NAV; net cash is added.

## 8. Business facts (two-minute-drill inputs)
What it is: holding company created 2021-11-01 by human split from SK Telecom to manage "반도체 및 New ICT" investee stakes [BR25]. Listed on KRX 2021-11-29. Largest shareholder SK Inc 32.2%. It earns (a) dividends from SK hynix (FY25: 356.0bn cash; the only material cash inflow), (b) equity-method profit (non-cash), and (c) small operating revenue from ICT subsidiaries (consolidated operating revenue 1,411.5bn FY25 versus 1,649.9bn FY24 as holdings were sold). Standalone head-office cost 56.9bn FY25.

Holdings (stake %, shares or value, basis):
- SK hynix (listed, KRX 000660): 146,100,000 shares, 20.1% FY25 (about 20.0002% post-issuance, press). Book 26,181,548mn; market 95,111,100mn at 651,000 KRW on 2025-12-31 [BR25]. NAV value 234.49tn on 2026-10-12 at 1,605,000 KRW/share [IR-NAV]; DERIVED 212.7tn at 1,456,000 on 2026-10-13. Investee financials FY25: revenue 97,146,675mn, operating income 47,206,319mn, NI 42,947,902mn, equity 120,666,751mn [BR25 note 10]. 2Q26 revenue 79.3tn, OP 60.5tn [Q2deck].
- TMAP Mobility (unlisted): 63.2% (60.1% prior, rose via cancellation); NAV 1.46tn at last deal value (2022Q3); book 317,576mn standalone. 2Q26 revenue 74.4bn, NI 0.1bn; Mobility Data revenue +14% YoY [Q2deck].
- SK Shieldus (unlisted JV): 32.0% (43,614,686 shares from the merger with Korea Security Holdings 2025-12-30); NAV 1.02tn at last deal value (2023Q3); equity-method book 826,781mn. FY25 Shieldus revenue 2,201,306mn, operating income 111,524mn, net loss 130,329mn, long-term debt 2,353,376mn [BR25].
- SK Planet (unlisted): 99.5% after 390,000mn cash injection; NAV 0.61tn at net asset value (2025Q4); owns 100% of 11st (11st 2Q26 revenue 97.0bn, NI -9.0bn). Book 668,624mn standalone.
- Wavve (Contents Wavve, unlisted): 40.5% consolidated view (36.7% in standalone); NAV 0.26tn at last deal value (2025Q3); also holds a convertible bond (face 175,000mn before partial sale/purchase; CJ ENM put described in s5). Wavve Americas 14.4% carried at 1,282mn after impairment.
- Onestore: 45.8% (consolidated, control via shareholder agreement). Press says the whole stake was sold ~2026-06-29; KOSCOM title "지주회사의 자회사 탈퇴" on 2026-06-29 is consistent. Sale price and any residual PRS obligation: UNKNOWN. Q2 NAV table no longer lists Onestore.
- Listed small holdings: Dreamus Company 22.2%, 16,430,038 shares, market value 23,511mn at 2025-12-31. IonQ common: 2,797,720 shares received in 2025 (1,490,000 shares reclassified to a variable-consideration instrument); residual position UNKNOWN.
- Others at FY25 book (mn): SK Square Americas 100% 267,859; FSK L&S 60% 17,757; Korbit 31.5% 8,515; SPARKPLUS 19.0% 10,112; SAPEON 12.5% 27,758; Airport Limousine 40% 67,110; Veritas 6.4% 6,390; SK Telecom CST1 55.4% 31,218; TGC Square 34.8% 11,940. In the company NAV table they sit inside "기타" 0.66tn.
Customer concentration: not applicable at holdco; hynix is 98% of NAV.
Recent events with dates: hynix ADR/new shares (July 2026); hynix 2Q26 record results (2026-07/08); SK Square 2Q results 2026-08-14; buyback cancellations 2026-07-31 (34,388 shares, board 2026-07-22); Onestore sale 2026-06; KOSPI circuit breaker on 2026-07-13 (SK Square -17.6%, hynix -15.4%, press). 2026-10-13 sharp fall (-11.9%) on heavy volume (1.55M shares); cause not established (news search found no article).

## 9. Consensus growth estimates
CONSENSUS (NAVER Finance / FnGuide-sourced, retrieved 2026-10-14 from m.stock.naver.com finance/annual): FY2026E revenue 346,724 x 100mn = 34.67tn, operating income 51.15tn, net income 48.92tn, EPS 371,946 KRW, BPS 549,806. These include equity-method income, so they are mostly hynix profit. Not independent. Company's own history for comparison: net income -1.31tn FY23 -> 3.65tn FY24 -> 8.82tn FY25; H1 2026 actual 27.05tn already 55% of the FY26E figure (consensus is stale relative to H1 actuals; do not rely). Quarterly consensus 3Q26E operating income 126,340 x 100mn = 12.63tn versus 2Q26 actual 19.24tn. Number of analysts and date of consensus snapshot: UNKNOWN. No target prices or ratings collected (RULE 2).

## 10. Data warnings & conflicts
fundamentals.json record for 402340.KS: warnings = [] ; errors = [] (as_of 2026-10-13T18:32:32Z). Note: it is a consolidated snapshot, and yfinance "forward_pe 2.0", ROE 0.85 and owner earnings 8.86tn KRW are driven by equity-method income that is not cash; do not use owner earnings for a holdco. Gross margins in that file (0.96, 0.90, -0.28, 0.71) are meaningless for a holdco. yfinance sector says "Technology / Semiconductors" while the company is a holding company.
Conflicts:
1. Price: yfinance 857,000 vs KRX/NAVER close 867,000 for 2026-10-13 (1.2%); 2026-10-08 yfinance 1,050,000 vs NAVER listed 1,059,000 (the NAVER price list is internally inconsistent: 2026-10-08 shows 1,059,000 but 2026-10-12 shows a -68,000 change from 1,050,000). yfinance also lacks 2026-10-12. Orchestrator instruction is to keep the 857,000 pipeline price; 867,000 is the official KRX close. Effect on the NAV discount is under 1 point.
2. SK hynix stake %: 20.1% (BR25 FY25) vs 20.5% (1Q26 press) vs 20.0%/20.7% (press snippets) vs 20.0002% post-issuance (computed from 146,100,000 / 730,492,365). Cause: hynix share count changes (treasury cancellations, EB exchanges, ADR new issuance). 146,100,000 shares held is stable across BR25 and press. Which is right at 2026-10-13 requires hynix's cover-page share count; hynix 730.49M shares is consistent with NAVER market cap (1,063.6tn / 1,456,000 = 730.5M). Treat 20.0002% as likely but not filing-verified.
3. Dividend: DPS 1,550 (company) vs 1,544 (NAVER consensus column) vs 1,500 (Edaily snippet). Company document wins.
4. NAV: company NAV/share 932,398 (1Q26), 2,970,469 (2Q26), 1,813,952 (2026-10-12); NH Investment June estimate 3.58m/share, Yuanta 347tn NAV and DB Securities 278tn (Oct 6) are broker estimates [SNIPPET, not used]. Company numbers use hynix market price on each date.
5. Buyback amounts: Quartr summary shows 1,100bn buyback and 2,000bn dividend (units error x10); company deck says 110bn and 200bn. Edaily's 204.3bn dividend agrees with the company filing.
6. Quartr "H1 net income 27,055,747mn" is NI attributable to owners; company's total NI is 27,049.7bn. Immaterial difference (non-controlling interest).
7. Revenue definitions: DART operating revenue 1,411.5bn vs NAVER "revenue" 10.46tn (includes equity-method gains). Not a data error.
8. Market cap: NAVER integration page showed 114.38tn on 2026-10-13 at an intraday print; yfinance 112.93tn at 857,000. Both fine.
UNKNOWN list: insider open-market transactions; FY2021-22 financials; FY2023-24 OCF/capex (DART cash-flow statement not extracted); holdco FY2023 cost line; hynix quote of treasury share count; IonQ residual holding; Onestore sale price and residual PRS liability; guarantee amount for TMAP; earnings-call transcript and Q&A; peer multiples and peer NAV discounts; consensus analyst count and date; 2025 value-up plan targets read directly (only via press); cause of the 2026-10-13 sell-off; whether DART shows any filing between 2026-09-14 and 2026-10-13 (DART list not reachable); IR page listing of an NAV quarterly discount for 2026Q2.

## Sources
1. SK Square IR NAV page https://www.sksquare.com/kor/ir/nav.do (NAV table, daily/quarterly discount; read 2026-10-14)
2. SK Square IR shareholder return page https://www.sksquare.com/kor/ir/return.do
3. Q2'26 Portfolio Update, https://www.sksquare.com/download/down.do?bidx=&fidx=729
4. Q1'26 Portfolio Update, ...fidx=712
5. 2026 interim dividend decision (2026-04-30), ...fidx=710
6. Shareholder return policy and execution deck (2026-03-25), ...fidx=687
7. FY2025 business report (제5기 사업보고서, 2026-03-17), ...fidx=686
8. FY2025 separate-FS audit report, ...fidx=683 (DART https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260311800910&dcmNo=11107949)
9. FY2025 consolidated audit report, ...fidx=682 (cover and notes only parsed)
10. Q2 2026 review report covers, ...fidx=731 and 732 (cover pages only)
11. https://m.stock.naver.com/api/stock/402340/{integration,price,basic,finance/annual,finance/quarter,disclosure} and /000660/{integration,price} (retrieved 2026-10-14)
12. https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=402340 (shareholder table as of 2026-10-12)
13. yfinance raw closes (402340.KS, 000660.KS) and data/fundamentals.json (as_of 2026-10-13T18:32:32Z)
14. /Users/User/Desktop/Projects/Investment/reports/runs/402340.KS_2026-10-13/00_inputs.json (risk-free, FX)
15. [SNIPPET/prose only] https://view.asiae.co.kr/en/article/2026081416082138479 ; https://v.daum.net/v/20260713000210966 (Fair Trade Act 20%, ADR) ; https://quartr.com/events/sk-square-co-ltd-402340-q2-2026_FRDdpkDv (AI summary, no transcript); https://v.daum.net/v/20260710061018077 ; Edaily/Newsis search results
