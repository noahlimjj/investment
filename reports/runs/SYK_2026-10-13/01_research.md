<!-- pipeline:value-researcher -->
# Research dossier: SYK (as of 2026-10-13)

## 0. Routing
FULL (acquisitive medtech compounder, profitable operating company). User holds SYK (SG resident, SGD base). Focus: (a) instrument-set capex check (ZBH analogue), (b) FY2024 capex-completeness flag, (c) acquisition spend vs acquired revenue by year.

## 1. Snapshot
- Price: $283.71 raw close 2026-10-13 (yfinance auto_adjust=False). fundamentals.json shows $283.61 (18:32 UTC intraday pull); 00_inputs.json $282.70 (13:52 UTC intraday). Use the 283.71 close. USD quote, USD reporting, no ADR.
- 12m change (raw closes): $364.92 (2025-10-13) -> $283.71 = -22.3% (price only, excludes ~$3.5/yr dividend).
- 52w closing range $269.75 (2026-09-24) to $388.35 (2025-10-22); intraday $267.00 to $392.55.
- Tape: -8.8% on 2026-09-08 ($303.13 -> $276.43, volume 6.3M vs ~2.2M norm). Cause per [SNIPPET] web summary: CFO at Wells Fargo conference said a peripheral-vascular manufacturing issue continues into Q3 (not yet verified from primary doc; no 8-K filed that day).
- Shares: 383,573,046 basic outstanding (10-Q Q2 2026, accn 0000310764-26-000050, cover/6-30-2026); diluted weighted 386.0M Q2 2026.
- Mcap = 383.573M x $283.71 = ~$108.8B (fundamentals.json mcap $108.785B at $283.61).
- EV build (6-30-2026 balance sheet): total debt $14,942M (10-Q) + lease liabilities $501M (FY2025 10-K: 153+348; Q2 lease figure UNKNOWN) - cash $3,391M - marketable securities $85M = net debt = 14,942+501-3,391-85 = $11,967M. EV ~ $108.8B + $12.0B = ~$120.8B. (ex-leases: $11,466M net debt, EV ~$120.2B.)
- 10y UST: 5.22% (FRED DGS10, 2026-10-08, per 00_inputs.json). SGDUSD 0.7812.
- fundamentals.json: warnings [] ; errors []. trailing P/E 29.39, forward P/E 16.99, beta 0.781.

## 2. Financial history  (USD millions; FY Dec; source 10-K accns below)
| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM 6/2026 |
|---|---|---|---|---|---|---|---|
| Revenue | 14,351 | 17,108 | 18,449 | 20,498 | 22,595 | 25,116 | 25,837 |
| Gross profit | 9,057 | 10,968 | 11,578 | 13,058 | 14,440 | 16,065 | 16,788 |
| Op income | 2,223 | 2,584 | 2,841 | 3,888 | 3,689 | 4,889 | 5,534 |
| Net income | 1,599 | 1,994 | 2,358 | 3,165 | 2,993 | 3,246 | 3,729 |
| Diluted EPS ($) | 4.20 | 5.21 | 6.17 | 8.25 | 7.76 | 8.40 | (H1'26 5.23 vs 3.98) |
| Adj. diluted EPS ($) | UNKNOWN | UNKNOWN | UNKNOWN | 10.60 | 12.19 | 13.63 | H1'26 6.29 |
| Depreciation (CF stmt) | 340 | 371 | 371 | 393 | 427 | 461 | |
| Amort. intangibles (CF) | 472 | 619 | 627 | 635 | 623 | 732 | |
| "Total D&A" per segment note / XBRL tag | 1,076 | 1,272 | 1,278 | 1,341 | 1,426 | 1,570 | 1,618 |
| Gap (segment D&A - CF dep - CF amort) | 264 | 282 | 280 | 313 | 376 | 377 | |
| SBC | 142 | 171 | 168 | 205 | 229 | 243 | 251 |
| OCF | 3,277 | 3,263 | 2,624 | 3,711 | 4,242 | 5,044 | 5,525 |
| PP&E capex | 487 | 525 | 588 | 575 | 755 | 761 | 823 |
| FCF (OCF - PP&E capex) | 2,790 | 2,738 | 2,036 | 3,136 | 3,487 | 4,283 | 4,702 |
| Acquisitions (net cash) | 4,222 | 339 | 2,563 | 390 | 1,628 | 4,960 | 605 |
| Dividends paid | 863 | 950 | 1,051 | 1,139 | 1,219 | 1,284 | 1,317 |
| Buybacks | 0 | 0 | 0 | 0 | 0 | 0 | 0 (H1'26: none; 10-Q) |
| Cash & equivalents | 2,943 | 2,944 | 1,844 | 2,971 | 3,652 | 4,011 | 3,391 (6/30/26) |
| Total debt (ex leases) | 13,991 (761+13,230) | 12,479 | 13,048 | 12,995 | 13,597 | 15,859 | 14,942 (6/30/26) |
| Equity | UNKNOWN | 14,877 | 16,616 | 18,593 | 20,634 | 22,420 | 23,988 (6/30/26) |
| Diluted shares (M) | 380 | 382 | 382 | 384 | 386 | 386 | 386.0 (Q2'26) |
| Inventory | 3,494 | 3,314 | 3,995 | 4,843 | 4,774 | 5,310 | 5,521 |
| Receivables | 2,701 | 3,022 | 3,565 | 3,765 | 3,987 | 4,039 | 3,743 |
Notes: FY2021-FY2025 equity, total debt, PP&E, inventories, receivables from 10-K FY2025 Item 6 (accn 0000310764-26-000010). FY2020 equity UNKNOWN (sec_facts gap; not in Item 6 five-year table of FY2025 10-K). Debt FY2020 from sec_facts (761+13,230). Other rows: sec_facts via facts.json (XBRL, accns in facts.json).
TTM = FY2025 + H1 2026 - H1 2025 (10-Q accn 0000310764-26-000050). TTM D&A 1,618 is on the segment/XBRL basis (see section 10).
Buybacks: last repurchases $300M (2018) and $307M (2019) per FY2020 10-K (accn 0000310764-21-000027); none 2020-H1 2026. $1,033M authorization remains (10-Q).
Margins: gross 63.1/64.1/62.8/63.7/63.9/64.0% (FY20-25); op margin 15.5/15.1/15.4/19.0/16.3/19.5%.

### FY2024 capex-completeness flag - RESOLVED
sec_facts "unexplained investing outflow" FY2024 $608M. 10-K FY2025 cash-flow statement (accn 0000310764-26-000010): FY2024 investing = acquisitions (1,628) + purchases of short-term investments (750) + PP&E (755) + other investing +133 = (3,000). The residual is the $750M purchase of short-term investments (balance sheet 12/31/24: short-term investments $750M; $0 at 12/31/25), reversed +$750M in FY2025. It is treasury cash parking, NOT capex. FY2025 residual (855): +750 ST-investment redemption... + $165M proceeds from sale of Spinal Implants - $60M other investing. FY2024 PP&E capex $755M is complete. Segment capex split (10-K FY2025 Note 14): Orthopaedics 296/230/179, MedSurg 220/276/183, Corporate 245/249/213 (FY25/24/23).

### Instrument-set capex check (ZBH analogue)
- No separate instruments capex line in investing. Investing shows only "Purchases of property, plant and equipment".
- 10-K policy text (every year FY2017-FY2025): SG&A includes "amortization of loaner instrumentation". FY2020 10-K (accn 0000310764-21-000027): "$302 of loaner instrumentation not intended to be sold [2019] reclassified from inventories to other noncurrent assets". So loaner/instrument sets live in OTHER NONCURRENT ASSETS (not PP&E) and are amortised through SG&A.
- Segment note total D&A ($1,570M FY25) exceeds cash-flow depreciation+amortization of intangibles ($1,193M) by $377M ($376M FY24, $313M FY23, $280M FY22). The 10-K does not label the gap. INFERENCE (not stated in the filing): the gap is largely loaner-instrument amortization. The cash outlay for new instrument sets is not shown on any labelled line; it is inside operating cash flow (candidates: "Other, net" -470/-306/-134/-107/-47/+2 for FY25..FY20, or "Inventories"). Amount of instrument additions: UNKNOWN.
- Implication (facts): OCF is already net of whatever cash goes into loaner sets (not in investing), so FCF = OCF - PP&E capex = $4,283M FY25 does not omit that outflow; BUT sec_facts.py "owner_earnings" (FY25 $4,055M) uses D&A of 1,570 incl. the ~$377M and therefore overstates vs fundamentals.json owner_earnings $3,678M (uses 1,193). Quant should not add back the 377 gap to NI without deducting instrument spend.
- Unlike ZBH, Stryker's investing section has no hidden capex line; the exposure is on the OCF side.

## 3. Latest quarter & guidance
Q2 2026 (6-30-2026), 8-K accn 0000310764-26-000048 (Ex 99.1, 2026-07-30):
- Net sales $6,589M vs $6,022M, +9.4% reported, +9.0% organic (all unit volume). Op margin 25.2%; adj op margin 27.4% (+170bp). Reported EPS $3.30 (+44.1%); adj EPS $3.69 (+17.9%). Reported gross margin 68.3% vs 63.8% (adj 66.0%) - Q2 includes tariff refunds per [SNIPPET] summary of call; unverified.
- H1 2026: sales $12,609M (+6.1%, +5.8% organic); adj EPS $6.29 (+5.4%). Q1 2026 derived: sales $6,020M vs $5,866M (+2.6%), hit by cyber incident (arithmetic from H1 less Q2).
- Verbatim guidance: "We are narrowing our full year 2026 guidance and now expect organic net sales growth in the range of 8.3% to 9.3% and adjusted net earnings per diluted share in the range of $14.95 to $15.10. Our sales guidance includes a modestly positive pricing impact. Additionally, foreign exchange is expected to have a slightly favorable impact on both sales and adjusted net earnings per diluted share should rates hold near current levels."
- Cyber incident: 8-K 2026-03-11 (accn 0001193125-26-102460) identified incident, "global disruption to the Company's Microsoft environment". 8-K/A Item 1.05 2026-04-09 (accn 0001193125-26-149607): "the incident had a material impact on its operations, with resulting impact to the Company's financial results for the first quarter of 2026" and "has not had, and is not reasonably likely to have, a material impact on the Company's 2026 full-year guidance." Fully operational by then.
- Guidance history (8-K Ex 99.1): Q4'25 release (accn 0000310764-26-000006, 2026-01-29) and Q1'26 release (accn 0000310764-26-000025, 2026-04-30) both: "organic net sales growth in the range of 8.0% to 9.5% and adjusted net earnings per diluted share in the range of $14.90 to $15.10". Q2 narrowed to 8.3%-9.3% / $14.95-$15.10 (midpoint EPS 15.025 vs 15.00; sales midpoint 8.8% vs 8.75%).
- Q1 2026: sales +2.6% reported, +2.4% organic; adj op margin 21.1% (-180bp); adj EPS $2.60 (-8.5%); reported EPS $1.93. Q4 2025: sales $7.2B +11.4%, organic +11.0%, adj EPS $4.47 (+11.5%).
- Implied H2 2026 (arithmetic from guide midpoints, not company-stated): adj EPS guide $14.95-15.10 less H1 $6.29 = $8.66-$8.81 for H2.
- Q3 2026 results not yet reported (date UNKNOWN; last year late Oct).

## 4. Earnings-call takeaways
Verbatim Q&A not obtained. [SNIPPET]-only (WebSearch summaries, unconfirmed): Primary-doc facts first: Q2 organic growth 9.0%, MedSurg 9.2%, Ortho 8.6%; Q2 Vascular -0.7% reported/-1.8% cc (US -6.7%) after H1 +11.9%; Lobo (release): "We made significant progress in our recovery from the cyber incident... we enter the second half of 2026 with regained momentum". Q2 call: CFO Wells said Q2 EPS included tariff refunds, offset in H2 by cyber-related absorption/idle/remediation/IT costs; plan to resume share repurchases in Q3 (~$1B left on authorization); July 30 text "supply disruption resulted in a meaningful backorder situation with lost sales in the quarter" (peripheral vascular). 2026-09-08 Wells Fargo conf: manufacturing issue in peripheral vascular continuing into Q3, still limiting full customer inventory coverage. Q2 Vascular sales -0.7% reported (-1.8% cc), US Vascular -6.7% (10-Q/Ex 99.1; H1 +11.9%) - this confirms a vascular slowdown from primary doc. Transcript hosts: gurufocus 403, nasdaq highlights timeout; no verbatim transcript obtained => Q&A section UNKNOWN (3-5 exchanges not captured). Stopped-talking-about: not assessable without transcripts.

## 5. Capital allocation record
- Buybacks: $300M (2018), $307M (2019), none 2020-H1 2026 (cash flow statements). Auth remaining $1,033M (10-Q 6/30/26; program announced March 2015, $2,000M).
- Dividends declared/share: 2021 2.585, 2022 2.835, 2023 3.050, 2024 3.240, 2025 3.400; 2026 quarterly $0.88 (10-K Item 6; 10-Q).
- Share count: shares outstanding 378.7M (start 2023) -> 380.1 -> 381.4 -> 382.5 (end 2025) -> 383.5 (6/30/26); creeping UP ~0.3%/yr (SBC issuance, no buybacks).
- Acquisitions (cash net of cash acquired): 2020 $4,222M (deal names not read from filing here: UNKNOWN), 2021 $339M, 2022 $2,563M, 2023 $390M, 2024 $1,628M (+ $400M contingent milestones, FV $208M), 2025 $4,960M (Inari Medical $4,810M net of cash, $80/share, Feb 2025), H1 2026 $459M cash (AVS closed May 2026: $435M net cash + up to $400M milestones, FV $271M; 10-Q Note 7). 6-year cumulative FY20-FY25: $14,102M = 4,222+339+2,563+390+1,628+4,960 = $14,102M.
- Impairments: goodwill & other impairments FY25 $170M, FY24 $977M (Spinal Implants held-for-sale / product exits), FY23 $36M, FY22 $270M, FY21 $264M (10-K Item 6). Spinal Implants business sold (proceeds $165M FY25); spinal sales 713 (23) -> 707 (24) -> 185 (25).
- Organic vs acquired growth (10-K MD&A, accn 0000310764-26-000010): FY2025 reported +11.2%, cc +10.7%, ex acquisitions/divestitures +10.3% cc (9.9% volume + 0.4% price); MedSurg ex-M&A impact 4.7pts => 10.0% organic; Ortho ex 5.7pts (net of spine divestiture) => 9.6% organic. FY2024 reported +10.2%, cc 10.7%, organic 10.2% (9.1% vol + 1.1% price). Inari revenue contribution: not disclosed in 10-K (no pro forma found); Vascular sales 1,308->1,968 (+$661M, +50.6%; includes legacy neurovascular? and Inari). Organic cc growth (derived = cc growth minus acquisitions/divestitures impact, from 10-K MD&A): FY2020 -4.8% (cc -3.6%, acq +1.2pt; text "-4.1% unit, -0.7% price"); FY2021 12.6% (cc 18.1%, acq 5.5pt; Wright Medical-driven); FY2022 9.7% (cc 11.0%, acq 1.3pt); FY2023 11.5% (cc 11.6%, acq 0.1pt); FY2024 10.2%; FY2025 10.3% (acq/div net +0.4pt); Q1'26 organic 2.4% (acq/div -1.4pt, spine divestiture); Q2'26 9.0%.
Acquired revenue in $ (derived = pts x prior-year sales; approximate): FY2021 ~5.5% x 14,351 = ~$790M on $339M FY21 cash plus FY20's $4,222M spend (Wright annualisation); FY2022 ~1.3% x 17,108 = ~$222M; FY2023 ~$18M; FY2024 ~0.5% x 20,498 = ~$100M (MD&A text); FY2025 net +0.4pt = ~$90M net, i.e. Inari + others offset by spinal divestiture (spinal -$522M: 707->185). Gross Inari revenue UNKNOWN. Cash spent FY20-25 $14.1B bought at most ~5.5+1.3+0.1+0.5pt of growth plus Inari; Vascular +$661M FY25 is the upper bound for Inari-related contribution.
- Debt maturities (10-K Note 7): 2026 $1,000M; 2027 $1,382M; 2028 $2,606M; 2029 $1,691M; 2030 $2,565M; thereafter $6,729M. At 6/30/26 total debt $14,942M incl. $250M CP; $750M current. Revolver $3,000M to Feb 2030, $2,910M capacity.
- Lease liabilities FY25: $153M current + $348M noncurrent; op lease expense $205M.

## 6. Insider transactions
Form 4s filed 2025-10-13 to 2026-10-13 (65 filings, parsed from EDGAR XML; codes: S open-market/plan sale, P purchase, F tax withholding, M option exercise, A award, G gift):
- Open-market sales (code S) total 1,697,124 shares, ~$586M: director Ronda E. Stryker 1,680,000 sh ~$581M (2025-11-07; 2026-02-06; 2026-05-28; 2026-08-20 at ~$332-344); Fletcher (CLO) 4,544 sh ~$1.4M (2026-05-29); Fink (CHRO) 8,720 sh ~$2.5M (2026-05-12); Berry (CAO) 1,953 sh ~$0.7M (2025-11-17); King 826 sh; Crotty 441 sh; Pierce 475 sh; Wells (CFO) 165 sh (2025-11-20 at $365.88).
- Open-market purchases (code P): director Mary K. Brainerd, 131 shares total ~$26.7K on 2026-09-02, reported prices $185.65-$225.20, which are far below the ~$312 market that day (anomalous: possibly a plan/fund-related entry; not verified). Otherwise ZERO insider open-market buys; no purchases after the 2026-09-08 drop.
- Lobo exercised 206,955 options at $96.64 on 2026-02-06 and had 132,410 shares withheld for tax (F), no S recorded. Wells code J dispositions 2026-09-24/28 (non-sale). Ronda Stryker gifts (G) 2026-02: 55,600+377,900+222,300 sh.
- Note: Ronda Stryker sales are a family-director holder; sale volume (1.68M sh) is ~0.44% of shares outstanding.
Form 3 filings 2026-01-09 and 2026-09-08 seen (new insiders). insider_pct 5.36% is a holding (yfinance, vendor).
Management change: 8-K 2026-10-06 (accn 0001193125-26-414956): CEO Kevin Lobo resigns as CEO 12/31/2026, becomes Executive Chair 1/1/2027; Spencer Stiles (age 50, President & COO since Jan 2026) becomes CEO 1/1/2027, base salary $1,320,000, bonus target 150%. CAO Berry retires 9/1/2026 (8-K 2026-05-20).

## 7. Peers & sector multiples
Single vendor (yfinance .info, pulled 2026-10-13/14, TTM basis; EV/EBITDA = vendor enterpriseToEbitda; FCF yield = vendor freeCashflow / marketCap; vendor figures not re-verified to filings except SYK):
| Ticker | Mcap $B | EV $B | EV/EBITDA | Trailing P/E | Fwd P/E | FCF yield % |
|---|---|---|---|---|---|---|
| SYK | 109.0 | 120.4 | 16.3 | 29.4 | 17.0 | 3.77 |
| BSX | 63.3 | 75.9 | 13.3 | 17.7 | 12.9 | 3.87 |
| MDT | 118.1 | 137.5 | 13.2 | 22.7 | 14.4 | 4.58 |
| ABT | 178.0 | 204.0 | 17.5 | 33.2 | 17.0 | 4.05 |
| ZBH | 17.7 | 24.7 | 9.8 | 22.6 | 10.3 | 6.05 |
| ISRG | 149.7 | 146.0 | 34.9 | 48.6 | 35.0 | 1.75 |
| EW | 49.4 | 46.4 | 23.2 | 51.1 | 25.4 | 2.49 |
SYK trailing P/E is inflated by GAAP items (FY25 tax 28% and impairments); forward P/E 17.0 is on adjusted EPS.

## 8. Business facts
FY2025 sales mix (10-K): MedSurg & Neurotech $15,647M (62%): Instruments 3,183, Endoscopy 3,807, Medical 4,204, Vascular 1,968, Neuro Cranial 2,485. Orthopaedics $9,469M (38%): Knees 2,656, Hips 1,865, Trauma & Extremities 3,948, Spinal Implants 185, Other 815. Geography: US $19,006M (75.7%), Intl $6,110M. ~56,000 employees. Mako robotic >45 countries. Q1 2026 reorg created "Ortho Tech" (orthopaedic instruments + other ortho) - segments recast (8-K 2026-06-26, accn 0000310764-26-000041). Customer concentration: not disclosed in text read (UNKNOWN; hospitals/ASCs, no >10% customer found in 10-K sections read - not exhaustively searched). Market share: 10-K states 'one of four leading global competitors for joint replacement and trauma and extremities products and robotics'. Recent events: Inari acquired Feb 2025; AVS (IVL, peripheral) May 2026; cyber incident 2026-03-11; peripheral vascular supply/backorder issue (Q2 release Vascular -0.7%); CEO transition announced 2026-10-06; SEC/DOJ FCPA inquiries closed 2025 (10-K Note 7); product-liability accrual $144M (hip recalls, Rejuvenate/ABG II).

## 9. Consensus growth estimates
CONSENSUS (yfinance analyst estimates, pulled 2026-10-13): FY2026 EPS avg $14.97 (low 14.89, high 15.05, 28 analysts), +9.8% vs FY25 adj $13.63; FY2027 EPS avg $16.69 (+11.5%); FY2026 revenue avg $27.19B (+8.3% vs $25.116B), FY2027 $29.53B (+8.6%); next quarter (0q) revenue $6.62B, EPS $3.56 vs $3.19 yr ago, +11.5%). (Consensus EPS basis is adjusted; no price targets/ratings collected.)
Company history: revenue CAGR FY20-25 11.8% (sec_facts) incl. acquisitions; organic 10.2-11.5% FY23-25; adj EPS 10.60 -> 13.63 (FY23-25, ~13.4% CAGR); GAAP EPS 4.20 -> 8.40. Company: revenue CAGR FY20-25 11.8% (sec_facts); diluted EPS 4.20 -> 8.40; adj EPS 10.60 -> 13.63 FY23-25. Company guide FY26 adj EPS $14.95-15.10 (+9.7% to +10.8% vs 13.63).

## 10. Data warnings & conflicts
- fundamentals.json SYK: warnings none, errors none.
- Conflict A (resolved): fundamentals.json NI $3,246M (FY2025) vs facts.json ttm NI $3,729M: different periods (FY vs TTM through 6/2026). Both correct.
- Conflict B (resolved): sec_facts owner_earnings FY25 $4,055M vs fundamentals.json $3,678M (10%): D&A basis 1,570 (segment note, incl. ~377 non-labelled, likely loaner-instrument amortization) vs 1,193 (cash flow dep+amort). Use 1,193 basis.
- Price: 283.71 close vs 283.61/282.70 intraday pulls (0.03-0.4%).
- FY2024 $608M unexplained investing: resolved (short-term investment purchase).
- sec_facts gaps: capex_intangibles none (no separate line), buybacks FY22-25 = none (true zero repurchases, verified in equity statement), equity filled from Item 6.
- Brainerd Form 4 'P' prices ($185-225 vs ~$312 market) anomalous; flagged.
- Search-snippet items ([SNIPPET], not confirmed in source docs): reason for 2026-09-08 drop; tariff-refund commentary; buyback-resumption plan; 'meaningful backorder' quote.
- Possible legal overhang [SNIPPET]: law firms (Hagens Berman, Glancy) announced investigations re disclosure of the manufacturing issue.
- UNKNOWN list: Inari gross revenue; instrument-set cash spend; adj EPS FY20-22; FY2020 equity; verbatim call Q&A (5 exchanges); Q2 lease liabilities; customer concentration; acquisition names FY20/FY22; Q3 earnings date.

## Sources
1. https://data.sec.gov/api/xbrl/companyfacts/CIK0000310764.json (facts.json)
2. 10-K FY2025 accn 0000310764-26-000010; FY2024 0000310764-25-000023; FY2023 0000310764-24-000024; FY2022 0000310764-23-000017; FY2021 0000310764-22-000028; FY2020 0000310764-21-000027
3. 10-Q Q2 2026 accn 0000310764-26-000050; 8-K Q2 earnings 0000310764-26-000048 (Ex 99.1)
4. 8-Ks: 0001193125-26-102460, 0001193125-26-104431, 0001193125-26-149607, 0001193125-26-232643, 0000310764-26-000041, 0001193125-26-414956
5. yfinance raw closes (pulled 2026-10-13/14)
6. EDGAR Form 4 XML (65 filings); yfinance info/estimates (peers, consensus)
7. [SNIPPET] WebSearch summaries (financialmodelingprep, tikr, marketbeat, nasdaq, gurufocus) - unverified
