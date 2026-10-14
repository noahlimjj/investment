<!-- pipeline:value-researcher -->
# Research dossier: NVO (as of 2026-10-13)
Status: CURRENT HOLDING (SG resident, SGD base; Danish dividend withholding relevant). Draft written at checkpoint; sections marked (TODO) were still open when written.

## 0. Routing
FULL. Profitable operating pharma, ADR (NYSE: NVO) = 1 Novo Nordisk B share (ADR ratio 1:1; check: $38.015 / 0.14973 USD per DKK = DKK 253.9 vs B share close DKK 256.65 on 2026-10-13 (yfinance NOVO-B.CO), within FX/timing noise). Quote ccy USD; reporting ccy DKK (IFRS, millions unless stated); 20-F filer, interim results on 6-K.

## 1. Snapshot (tape first)
- Price: $38.015 close 2026-10-13 (yfinance raw Close, auto_adjust=False; fundamentals.json shows 38.015). Orchestrator 00_inputs price 38.415 was intraday 13:52Z.
- 12m change (raw closes): $57.50 (2025-10-13) -> $38.015 = -33.9%. Price only; dividends excluded (ADR dividends in window: $1.275 on 2026-03-30, $0.579 on 2026-08-17 per yfinance; total-return not computed).
- 52w range (raw closes, 12m window): high $63.98 (2026-01-26), low $35.29 (2026-03-30). All-time raw close high in 2y history $119.78 (2024-10-14) => -68% from that peak.
- Path: $63.98 (26 Jan) -> $58.93 (2 Feb) -> $50.30 (3 Feb) -> $47.19 (4 Feb) after FY26 guidance of -5% to -13% -> low $35.29 (30 Mar) -> $45.76 (6 May) -> $47.09 (3 Aug) -> $44.28 (4 Aug, Q2) -> $45.33 (31 Aug) -> $43.24 (18 Sep) -> $39.80 (21 Sep, Capital Markets Day) -> $38.03 (13 Oct).
- Trailing P/E 9.29, forward P/E 11.47 (fundamentals.json, yfinance, as_of 2026-10-13T18:32Z). Beta 0.384.
- Market cap: 4,413.1M shares outstanding x $38.015 = $167.76B (fundamentals.json market_cap_usd $167,764M; matches).
- Shares: total A+B 4,465,000,000 incl. treasury; treasury 51,889,876 B shares = 1.2% (6-K accn 0001171843-26-006585, 2026-10-12, as of 9 Oct) => outstanding 4,413.1M basic. Diluted weighted avg H1 2026: UNKNOWN in text read (EPS 15.67 basic / 15.66 diluted implies ~same). yfinance sharesOutstanding 3,338M = B shares only (A shares excluded): do not use.
- EV build (my arithmetic, mixed sources): Net borrowings 30 Jun 2026 = borrowings 121,794 + 18,333 = 140,127 DKK M, less cash 44,482 less marketable securities 500 = 95,145 DKK M net debt (6-K accn 0000353278-26-000023, Appendix 3). x 0.14973 = $14.25B. EV = 167.76 + 14.25 = ~$182.0B. Whether the BS "Borrowings" line includes IFRS 16 lease liabilities: UNKNOWN (company net debt definition excludes lease liabilities per Q4 release, which implies leases sit inside Borrowings; not confirmed from the notes). Lease liabilities 31 Dec 2025 DKK 8,572M (XBRL ifrs-full:LeaseLiabilities, 20-F accn 0000353278-26-000012). 
- yfinance EV $265,980M and EV/EBITDA 1.5 are WRONG (DKK debt and EBITDA added to USD market cap without conversion). Do not use.
- 10y yields (00_inputs.json): USD 5.22% (DGS10, 2026-10-08); DKK 3.01% (OECD IRLTLT01DKM156N, monthly avg 2026-08-01, lags 1-2 months). FX DKKUSD 0.14973; SGDUSD 0.78121.
- Dividend: ADR yfinance dividendRate $1.80 [SNIPPET: vendor field]. Company: FY2025 total DKK 11.70/share (interim 3.75 + final 7.95); 2026 interim DKK 3.75 paid Aug 2026 (6-K 0000353278-26-000023).

### Narrative vs tape
The stock is -68% from the Oct-2024 peak and -34% on 12m with P/E 9.3 trailing / 11.5 forward. The 2023 "GLP-1 explosion" story is stale: revenue growth FY2025 was +6.4% DKK (+10% CER), 2026 guidance is adjusted sales -6% to 0% at CER, and consensus expects declining EPS. The tape is pricing a profit decline from price (US MFN, WAC cut), competition (Lilly) and semaglutide LOE. Note the trailing P/E is flattered by a one-off DKK 26.8B non-cash 340B provision reversal in Q1 2026 (see section 3).

## 2. Financial history (DKK millions; source SEC XBRL via sec_facts.py, 20-F accns 0001628280-23-001868 (FY20), -24-002635 (FY21), -25-003920 (FY22), 0000353278-26-000012 (FY23-25); H1 from 6-K 0000353278-26-000023)
| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Revenue | 126,946 | 140,800 | 176,954 | 232,261 | 290,403 | 309,064 |
| Gross profit | 106,014 | 117,142 | 148,506 | 196,496 | 245,881 | 250,276 |
| EBIT | 54,126 | 58,644 | 74,809 | 102,574 | 128,339 | 127,658 |
| Net income | 42,138 | 47,757 | 55,525 | 83,683 | 100,988 | 102,434 |
| D&A | UNKNOWN | UNKNOWN | 6,553 | 7,289 | 8,545 | 14,666 |
| D&A+impairment (CF add-back) | 5,753 | 6,025 | 7,362 | 9,413 | 19,107 | 21,982 |
| SBC | 823 | 1,040 | 1,539 | 2,149 | 2,289 | 1,435 |
| OCF | 51,951 | 55,000 | 78,887 | 108,908 | 120,968 | 119,102 |
| Capex PP&E | 5,825 | 6,335 | 12,146 | 25,806 | 47,164 | 60,140 |
| Purchase of intangibles | 16,256 | 1,050 | 2,607 | 13,090 | 4,145 | 29,973 |
| Acquisitions of businesses | 0 | 18,283 | 7,075 | 0 | 82,163 | 0 |
| Buybacks | 16,855 | 19,447 | 24,086 | 29,924 | 20,181 | 1,388 |
| Dividends paid | 20,121 | 21,517 | 25,303 | 31,767 | 44,140 | 51,763 |
| Cash | 12,226 | 10,719 | 12,653 | 14,392 | 15,655 | 26,464 |
| Borrowings (BS) | 10,356 | 26,645 | 25,784 | 27,006 | 102,787 | 130,958 |
| Lease liabilities | 3,672 | 4,129 | 4,529 | 5,726 | 6,766 | 8,572 |
| Equity | 63,325 | 70,746 | 83,486 | 106,561 | 143,486 | 194,047 |
| Inventories | 18,536 | 19,621 | 24,388 | 31,811 | 40,849 | 49,623 |
| Trade receivables (current) | 27,734 | 40,643 | 50,560 | 64,770 | 71,949 | 70,856 |
| Diluted shares (M, split-adjusted) | see conflict | 4,606.2 | 4,544.6 | 4,494.8 | 4,463.0 | 4,447.7 |
| Diluted EPS (DKK) | see conflict | 10.37 | 12.22 | 18.62 | 22.63 | 23.03 |
Gross margin: 83.5% / 83.2% / 83.9% / 84.6% / 84.7% / 81.0%. Operating margin FY2025 41.3% (fundamentals.json margins list shows 41.3%-44.2%).
Company-defined FY2025 FCF DKK 28,295M (FY2024 -14,707) = OCF less PP&E, intangibles, business acquisitions, other, lease repayment (Q4 release 6-K accn 0000353278-26-000006). Lease repayment FY2025 DKK 1,503M, FY2024 1,417M (same source). fundamentals.json FCF 28,989 = OCF 119,102 - (PP&E 60,140 + intangibles 29,973) and Capex -90,113: includes intangibles (Akero, see section 5).
Adjusted figures FY2025: adjusted net profit 116,407; adjusted diluted EPS 26.17 (Q4 release). FY2025 EBITDA (company) 149,640.
Inventory growth vs sales growth: inventories +21.5% FY2025 (40,849->49,623) vs revenue +6.4%; FY2025 inventory write-downs DKK 4,272M (FY2024 2,660; XBRL InventoryWritedown). Receivables flat/down in FY2025 (70,856 vs 71,949), but 30 Jun 2026 trade receivables 88,949 (+25.5% vs 31 Dec 2025) and inventories 51,352.

### Latest interim and TTM (DKK M)
H1 2026 / H1 2025 (6-K 0000353278-26-000023): Net sales 175,311 / 154,944; gross profit 144,613 / 129,208; EBIT 86,679 / 72,240; net profit 69,546 / 55,537; diluted EPS 15.66 / 12.49; OCF 79,283 / 66,504; PP&E capex 23,986 / 28,083; intangibles 854 / 2,778; buybacks 5,899 / 1,388; dividends 35,312 / 35,100; D&A+impairment 13,840 / 8,663.
Derived TTM to 30 Jun 2026 (arithmetic: FY2025 - H1'25 + H1'26): revenue 329,431; net profit 116,443; diluted EPS 26.20. These include the DKK 26,760M non-cash 340B provision reversal in Q1 2026 (net of Q2'25's 2,600M reversal within H1'25). TTM OCF/FCF: NOT COMPUTED, because from 1 Jan 2026 interest received/paid moved out of operating cash flow (note 1 to Appendix 2), so H1'26 OCF is not comparable with FY2025.
Balance sheet 30 Jun 2026: total equity 221,277; borrowings 121,794 non-current + 18,333 current; cash 44,482; marketable securities 500; tax payables 20,460 (vs 8,416 at Dec 2025); sales deductions and returns 140,201 current. Company H1 2026 FCF (redefined as OCF - PP&E capex) DKK 55.3B vs 38.4B.
Ratings Aa3 (Moody's) / AA (S&P); EUR 15.0B and CHF 1.09B bonds outstanding.

## 3. Latest quarter and guidance (Q2/H1 2026, released 2026-08-04, 6-K accn 0000353278-26-000023)
Why forward P/E > trailing P/E: trailing includes the one-off 340B reversal that boosted H1 reported EBIT; underlying (adjusted) numbers are shrinking on price. Verbatim/primary facts:
- "Q2 2026 reported sales increased by 3% at CER ... Q2 2026 adjusted sales increased by 7% at CER, driven by GLP-1 volume growth across geographies and favourable US rebate adjustments in the quarter."
- Q2 adjusted sales DKK 78,488M (+6% DKK, +7% CER); adjusted EBIT 33,389 (+11% CER); reported EBIT 27,061 (-19% DKK) after DKK 6.3B non-cash impairments (monlunabant DKK 4.0B).
- Adjusted gross margin 78.2% vs 82.7% Q2'25: "impacted by lower realised prices, one-time costs of around DKK 3 billion related to right-sizing of manufacturing capacity agreements, as well as a negative currency impact".
- H1 reported sales 175,311 includes "DKK 26.8 billion sales rebate provision reversal ... in Q1 2026, related to the US 340B Drug Pricing Program ... no cash impact." H1 adjusted sales 148,551 (+2% CER), adjusted EBIT 66,247 (+2% CER), adjusted EBIT margin 44.6%.
- US adjusted sales Q2 40,869 (+4% CER; H1 -4% CER): "reflecting volume growth ... partly offset by lower realised prices". Wegovy injectable US Q2 -22% CER. Wegovy pill Q2 DKK 3,218M; >265,000 weekly TRx (week to 17 Jul); self-pay USD 149-299/month. Insulin US market share declines.
- Intl Operations Q2 +10% CER; Obesity care +37%. Region China list-price cuts late Q4 2025. "In Canada, the loss of exclusivity for semaglutide has led to lower realised prices while volumes have remained broadly stable".
- Rare disease Q2 operating loss DKK 1,295M.
Guidance (as reported, 2026, CER unless noted), history: 3 Feb: adj. sales -5% to -13%, FCF 35-45 bDKK; 6 May: -4% to -12%, FCF 36-46; 4 Aug: "Adjusted sales growth for 2026 is now expected to be 0% to -6% at CER and adjusted operating profit growth is now expected to be 0% to -6% at CER." DKK reporting: sales ~1 pt lower than CER, EBIT ~2 pts lower. Capex (PP&E) "Around 55 bDKK" (2025: 60); "In the coming years, the capital expenditure investments are expected to decline." FCF now 45-55 bDKK (definition OCF less PP&E). Financial items net loss ~1.1 bDKK; tax rate 21-23%. Unadjusted midpoints: sales +5%, EBIT +12%.
Drivers cited by company: MFN agreement with US administration; "loss of exclusivity for the semaglutide molecule in certain markets in International Operations"; "intensifying competition"; reduced Medicaid obesity coverage; Wegovy pill cannibalisation assumptions.
Forward price events: "effective 1 January, 2027, Novo Nordisk will lower the list price, or wholesale acquisition cost (WAC), of Wegovy ... and Ozempic ... to USD 675, representing reductions from the current list price of approximately 50% and 35% ... The change in list prices is expected to impact Novo Nordisk's cash flow in 2027."
Capital Markets Day 21 Sep 2026 (GlobeNewswire text via Investegate; no 6-K carrying it found in the sweep): 2030 ambitions "from a 2026 baseline ... do not constitute Novo's financial outlook or guidance": "Deliver 2026-30 revenue CAGR in line with industry peers" (14-company peer list incl. Lilly), "Maintain a broadly stable operating margin", "Maintain an attractive dividend per share", ">5 multi-blockbusters by 2030", ">150 bDKK pipeline sales in 2035" (risk-adjusted), ">60m patients". No numeric growth rate. Stock -7.9% on the day (raw close $43.24 -> $39.80). Same-day reports (secondary, Yahoo/FT-syndicated, [SNIPPET]): ~13,000 staff cut over the year; Citi describes mid-single-digit growth ambition as in line with consensus; CEO did not rule out a large transaction/bolt-on M&A.
Other recent events: ziltivekimab ZEUS Phase 3 missed primary endpoint (July; may cause Q3 2026 non-cash impairment); CagriSema REIMAGINE 4 non-inferior to tirzepatide on weight, not on HbA1c; US decision on CagriSema obesity expected Q4 2026; denecimig US BLA delayed by FDA facility remediation (6-K 0001171843-26-006374, 2 Oct 2026; launch aim H1 2027, "no impact on Novo's financial outlook for 2026"); CHMP positive on denecimig 17 Sep (0001171843-26-006088).

## 4. Earnings-call takeaways (Q2 2026 call, 4-5 Aug 2026). Source: Investing.com transcript via WebFetch (IR/6-K exhibit does not include a transcript; Investing.com blocked direct curl, so quotes below are WebFetch output, tagged [SECONDARY, not verified verbatim]).
- Goldman (James Quigley) on 2027: CFO Knudsen: "the loss of exclusivity impact will annualize into next year"; H2 comps include sema LOE in "Canada and Brazil mainly" and DKK 5B favourable prior-year gross-to-net.
- BNP (Verdult) on 2027 growth: Knudsen: "We look forward to guide for 2027 come February next year." (no 2027 guide given; the Jan 2027 WAC cut cash-flow impact is flagged in the report).
- Danske (Madsen) on US Wegovy injectable -22%: Millar: "we were expecting volume growth but continued price pressure"; "No new price dynamic impacting it." Knudsen: "self-pay is to the tune of 35% of total Wegovy injectable" (10-15% a year earlier per Zacks summary).
- UBS (Weston) on cutting price of higher pill doses: Millar: "more of a targeted surgical solution" rather than "a universal wholesale change".
- Citi (Parry): US GTN: "About three quarters of the impact is Ozempic gross to net, and then the balance is insulin."
- Pill pace [SNIPPET, Zacks summary]: weekly pill Rx growth slowed; ~90% share of oral obesity market; ~60% of branded obesity new starts in July.
- Dodged/unspecified: 2027 guidance deferred to February; no figure on how much of 2027 profit the WAC cut and LOE take. Compounding was not a prominent topic in sources read: UNKNOWN whether raised.
Stopped talking about: ziltivekimab as a pipeline growth driver (failed); monlunabant terminated.

## 5. Capital allocation record
- Buybacks (DKK M, XBRL PurchaseOfTreasuryShares): 2020 16,855; 2021 19,447; 2022 24,086; 2023 29,924; 2024 20,181; 2025 1,388; H1 2026 5,899. Average price paid by year: UNKNOWN except 2026 programme: DKK 15B programme from 4 Feb 2026; as of 9 Oct 2026, 37,849,179 B shares repurchased at avg DKK 278.97 = DKK 10,558,876,422 (6-K 0001171843-26-006585). Recent weekly buys at DKK 245-255 (5-9 Oct). Programme ends 1 Feb 2027 (tranche of DKK 11.2B from 6 May).
- Dividends/share (DKK): 2020 9.10; 2021 10.40; 2022 (paid) 6.20 split-adj basis in XBRL; FY2025 total 11.70 (FY2024 11.40); payout 50.7% (Q4 release). Dividends paid DKK 51.8B 2025 vs FCF 28.3B: dividends plus capex exceed company FCF, funded with debt (borrowings 26.6B 2021 -> 131.0B 2025).
- Share count: NumberOfSharesOutstanding 4,620M (2021) -> 4,444M (2025): -3.8% over 4 years (XBRL, split-adjusted).
- Acquisitions: 2024: three Catalent manufacturing sites, USD 11.7B (DKK 82,163M cash, CF statement; Q4 release); 2025: Akero Therapeutics closed 9 Dec 2025, USD 54/share cash = USD 4.7B plus a CVR of USD 6/share (USD 0.5B aggregate) on US approval of EFX in compensated MASH cirrhosis (20-F accn 0000353278-26-000012). The 2025 "Purchase of intangible assets" of DKK 29,973M is consistent with Akero being booked as an asset acquisition (inference, not confirmed in note text). 2021 DKK 18.3B acquisitions (Emisphere/Dicerna, named in 20-F subsidiaries list; amounts by deal UNKNOWN). Lost bid for Metsera to Pfizer: not verified, omitted.
- Impairments (XBRL, intangibles other than goodwill): 2023 1,414; 2024 9,513; 2025 2,760; plus PP&E impairment 2025 4,556; Q2 2026 6,328 (monlunabant 4.0B); possible Q3 2026 ziltivekimab charge.
- Restructuring: ~DKK 8B transformation costs in 2025; headcount 76,302 (end 2024) -> 68,794 (end 2025).
- Debt: Aa3/AA; EUR 1.3B bond repaid 21 May 2026; CHF 1.09B issued 11 Jun 2026. Debt maturities over next 5 years: UNKNOWN (maturity ladder is in Annual Report note, not read). Current borrowings 18,333 at 30 Jun 2026.
- Governance: Novo Nordisk Foundation control (A shares): voting split UNKNOWN in sources read.

## 6. Insider transactions
Insider activity: UNKNOWN (no transaction data available). Novo is a foreign private issuer, so no Form 4; Danish MAR manager transactions are published by the company/Nasdaq Copenhagen but not retrieved. insider_pct 0.00003 (fundamentals.json) is a static holding, not activity. The 6-K sweep showed only weekly buyback reports (company repurchases, not insider trades).

## 7. Peers and sector multiples (yfinance .info, pulled 2026-10-13/14, one vendor; all USD-reporting except NVO)
| | Price | EV/EBITDA | Trailing P/E | Fwd P/E | FCF yield |
|---|---|---|---|---|---|
| LLY | 1162.22 | 26.4 | 39.0 | 24.4 | 1.1% |
| AZN | 156.48 | 13.5 | 23.4 | 13.8 | 2.1% |
| PFE | 28.26 | 8.4 | 37.2 | 9.7 | 7.8% |
| AMGN | 412.38 | 15.6 | 25.6 | 16.8 | 3.9% |
| MRK | 142.12 | 14.1 | 112.8 | 15.3 | 4.3% |
| NVO | 38.02 | UNKNOWN (vendor 1.5 is a DKK/USD error) | 9.3 | 11.5 | vendor 22.5% unusable (mixed ccy) |
NVO own-basis (arithmetic, mixed sources): EV ~$182.0B (section 1); EV/TTM EBITDA: UNKNOWN (TTM EBITDA not derivable: H1'25 EBITDA not read). Company EBITDA FY2025 DKK 149,640M x 0.14973 = $22.4B => EV/EBITDA FY2025 ~8.1x (ratio of my EV to FY2025 EBITDA; FY2025 is stale vs EV date). FCF yield (company FY2025 FCF DKK 28,295M / mcap DKK ~1,120B) ~2.5%; H1'26 FCF 55.3B is on a different (PP&E-only) definition. Peer multiples are vendor values, and trailing P/Es (MRK 112.8, PFE 37.2) are distorted by one-offs.

## 8. Business facts (two-minute drill)
- Sells: GLP-1 injectables and pills for diabetes (Ozempic, Rybelsus/Ozempic pill) and obesity (Wegovy injectable, Wegovy pill launched US 5 Jan 2026, Wegovy HD 7.2mg launched US 7 Apr 2026, Saxenda), insulin, and rare disease (haemophilia, growth hormone). Customers: payers/PBMs, wholesalers, increasingly direct-to-patient self-pay (NovoCare Pharmacy, telehealth). Makes money from patent-protected branded drug sales; ~81% gross margin FY2025.
- Segments H1 2026 reported: Obesity and Diabetes care 164,943 (sales), Rare disease 10,368. Geography H1 2026 adjusted: US Operations 76,254 (51%), International Operations 72,297 (EUCAN 37,124; Emerging Markets 15,274; APAC 10,155; China 9,744). Therapy Q2 adjusted: Obesity care 23,152; GLP-1 diabetes 36,784; insulin 12,941; rare disease 4,907. Ozempic 31,375 and Wegovy injectable 19,484 are the largest Q2 products.
- Customer concentration (wholesalers) : UNKNOWN (not read). Market share: US Wegovy franchise "market leader among branded obesity medications" by new patient starts (6-K). Global branded obesity market volume growth 81%, GLP-1 diabetes 29% (IQVIA May 2026, company table).
- Competition: Eli Lilly tirzepatide (Mounjaro/Zepbound) and Foundayo (orforglipron oral, US approval ~April 2026 per press search [SNIPPET]); Lilly weekly Rx data: UNKNOWN verified. Company states Novo's pill ~90% of oral obesity market [SNIPPET].
- Semaglutide exclusivity by market: loss of exclusivity already in Canada and Brazil (CFO on Q2 call [SECONDARY]); company 6-K: "compound patent expiry of the semaglutide molecule in certain markets in International Operations". China, India, and other-market expiry dates: UNKNOWN in sources read (2026 expiries reported in press are not verified). US: Cipla ANDA Paragraph IV suit pending in D.N.J.; Sandoz UPC revocation action filed 30 Jun 2026 against EP unitary patent for 1mg semaglutide (18 EU countries). Compounding: UNKNOWN (not addressed in 6-K).
- Policy: Nov 2025 MFN agreement; Medicare Bridge pilot from 1 Jul 2026; IRA litigation closed after SCOTUS denied cert 18 May 2026; 340B provision of USD 4.2B fully reversed in Q1 2026 (non-cash). CVS Caremark adds other weight-loss meds to template formularies from 1 Oct 2026.
- Legal/IT: US class actions over an IT security incident (press release 11 Jun 2026); false-advertising suit vs Lilly filed 21 Jul 2026.
- Pipeline: CagriSema US decision Q4 2026; oral semaglutide 25mg (Ozempic pill) US decision Q4 2026; zenagamtide Phase 3; efruxifermin (Akero) Phase 3; CagriSema high-dose Phase 3 reads H1 2028.

## 9. Consensus growth estimates (CONSENSUS (yfinance earnings_estimate, retrieved 2026-10-14, DKK); no price targets collected)
EPS (DKK): FY2026 avg 22.53 (8 analysts; range 21.01-24.25) vs FY2025 actual 23.03 = -2.2%; FY2027 avg 22.09 (range 16.88-23.74) = -1.9%. Revenue FY2026 avg DKK 300,978M (-2.6%; range 272,677-?), FY2027 304,688M (+1.2%). Company history to compare: revenue CAGR FY2020-25 19.5% (sec_facts, DKK, 2020 base); revenue growth FY2025 +6.4%; EPS FY2021 10.37 -> FY2025 23.03 (CAGR 22%); FY2025 EPS +1.8%. Management ambition: 2026-30 revenue CAGR in line with industry peers, broadly stable operating margin; Citi characterised as mid-single-digit [SNIPPET]. Note consensus FY2026 EPS is on a reported basis and should be read against H1'26 reported EPS of 15.66 which includes the 340B reversal; the yfinance period definition vs adjusted: UNKNOWN.

## 10. Data warnings and conflicts
Warnings (fundamentals.json, NVO): (1) "forward P/E (11.5) > trailing (9.3): earnings are declining, so PEG=4.36 is meaningless - VOID, use FCF yield / DCF". errors: none. Run writes 1 ticker, 0 errors.
Conflicts and UNKNOWNs:
1. yfinance EV ($265,980M) and EV/EBITDA (1.5x): currency mix (DKK balance sheet items against USD cap). Right figure: own build ~$182B. Resolved.
2. yfinance sharesOutstanding 3,338M vs 4,413M: B shares only vs A+B net of treasury. Right: 4,413.1M (6-K). Resolved.
3. Trailing EPS yfinance $4.09 vs my TTM diluted EPS DKK 26.20 x 0.14973 = $3.92 (4% gap; FX/period timing; and TTM includes one-off 340B). Not load-bearing but noted.
4. facts.json diluted shares/EPS FY2020 (2,340M; 18.01) are pre-2023 2:1 split (not restated) vs FY2021+ restated; diluted_share_cagr 13.7% in facts.json is an artefact. True FY2021-25 diluted share change: 4,606.2M -> 4,447.7M = -0.7% p.a. (inference: the 2:1 split date was not retrieved). Also FY2020 EPS comparable would be ~9.0.
5. Capex definition: fundamentals.json capex -90,113 (PP&E + intangibles) vs company capex 60,140 (PP&E). FCF 28,989 (vendor) vs company 28,295 (also deducts lease repayment, other). Difference = intangible purchases (Akero) and lease principal; right figure depends on the purpose (company FCF ex-M&A is OCF - PP&E = 58,962 FY2025).
6. H1 2026 OCF not comparable with FY2025 (interest reclassified from operating in 2026).
7. Interest expense XBRL FY2023 845 looks inconsistent with neighbours (2,451-7,346): not load-bearing; verify before use.
8. sec_facts gaps: debt_current, debt_noncurrent, equity tags empty in facts.json (equity filled from XBRL above), D&A FY2020-21, securities, TTM empty, shares_outstanding_latest null, stale null. Facts.json file edited to carry the above.
9. Reported figures contain non-cash 340B reversal (DKK 26.76B in Q1 2026; USD 400M in 2025); adjusted measures exclude them.
10. UNKNOWN list: insider activity; debt maturity ladder; average buyback price by year (pre-2026); 2027 guidance; compounding status; semaglutide LOE dates for China/India/other markets; customer concentration; TTM EBITDA; H1'25 adjusted EPS; lease-in-borrowings confirmation; Foundayo weekly Rx verified; Foundation voting control; verbatim call quotes (secondary). Tagged [SNIPPET] items are not load-bearing.

## Sources
1. data/fundamentals.json record NVO (yfinance), as_of 2026-10-13T18:32Z; yfinance raw closes NVO, NOVO-B.CO
2. reports/runs/NVO_2026-10-13/00_inputs.json; facts.json (sec_facts.py, companyfacts CIK0000353278)
3. SEC 6-K accn 0000353278-26-000023 (Q2/H1 2026 financial report, 2026-08-04)
4. SEC 6-K accn 0001171843-26-005184 (raised outlook, 2026-08-04); 0001171843-26-005172 (buyback)
5. SEC 6-K accn 0000353278-26-000018 (Q1 2026, 2026-05-06); 0000353278-26-000006 (FY2025 release, 2026-02-03)
6. SEC 20-F accn 0000353278-26-000012 (filed 2026-02-04)
7. SEC 6-Ks: 0001171843-26-006585 (buyback 12 Oct), -006374 (denecimig FDA 2 Oct), -006088 (CHMP 17 Sep), -006128/-006038/-005925/-005795/-006248/-006440 (weekly buyback reports)
8. https://www.investegate.co.uk/announcement/gnw/novo-nordisk-a-s-class-b--0qiu/highlights-to-be-presented-at-novo-s-capital-/9781878 (CMD release 21 Sep 2026)
9. https://in.investing.com/news/transcripts/earnings-call-transcript-novo-nordisk-beats-q2-2026-estimates-shares-rise-premarket-93CH-5536175 (Q2 call, via WebFetch, secondary)
10. https://finance.yahoo.com/healthcare/articles/novo-targets-blockbuster-heavy-2030-115948877.html and https://finance.yahoo.com/healthcare/articles/nvo-q2-earnings-call-centers-140000115.html (secondary summaries, [SNIPPET])
11. SEC submissions index https://data.sec.gov/submissions/CIK0000353278.json (filing sweep: only 6-Ks in last 30 days, none with results/guidance beyond those above)
