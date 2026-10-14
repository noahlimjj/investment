<!-- pipeline:value-researcher -->
# Research dossier: VXUS (as of 2026-10-13 US close; written 2026-10-14)

## 0. Routing
FUND. Vanguard Total International Stock ETF, US-domiciled, passive ex-US all-cap equity index ETF. Status: current holding; user's core is VWRA (Irish UCITS). No Lynch category, no DCF. Role question = "does a US-situs ex-US ETF belong beside VWRA, and if an ex-US sleeve is wanted, is there a better-structured vehicle".

## 1. Snapshot
- Price: $84.52 raw close (yfinance auto_adjust=False, 2026-10-13). 00_inputs.json shows 84.405 (intraday 13:52Z); the close is used. Quote ccy USD, reporting ccy USD. No ADR ratio (not applicable).
- 12m price change (raw closes): $73.27 (2025-10-13) to $84.52 = +15.35% price only. Total-return (dividend-adjusted closes, labelled separately): +18.30%.
- 52w range (raw closes): low $72.19 (2025-11-20), high $88.41 (2026-09-04). Close is 4.4% under the high (arithmetic from the above).
- NAV $84.58 (yfinance navPrice, date unstated). Premium/discount about -0.07%, [indicative only].
- Size: ETF share class TNA $156,510M; whole fund (all share classes) $651,036M, both as of 2026-06-30 (Vanguard factsheet F3369_062026). yfinance totalAssets $649,285M undated. No "mcap/EV/shares" for a fund; not applicable.
- 10y UST yield 5.22% (FRED DGS10, 2026-10-08, from 00_inputs; re-verified on FRED CSV: 2026-10-08 = 5.22).
- Fund trailing P/E 16.14 (yfinance), vs factsheet P/E 18.3x (fund) and 18.2x (index) at 2026-06-30 [differing definitions; factsheet is the issuer figure].
- fundamentals.py: errors = none. warnings = 1 ("fund/ETF: operating-company metrics do not apply"). Not blocked.

## 2. Financial history
Not applicable (FUND). sec_facts.py returned "NOT AN SEC FILER: VXUS not found in SEC ticker map". Fund-level facts instead (issuer factsheet 2026-06-30, https://institutional.vanguard.com/iippdf/pdfs/FS3369R.pdf):

| Item | Value |
|---|---|
| Expense ratio | 0.05% (most recent prospectus, per factsheet); management fee 0.06% / other 0.02% is the Institutional-class table in SEC 497K accn 0001683863-24-000918 (2024) and not this share class |
| Benchmark | FTSE Global All Cap ex US Index |
| Inception | 2011-01-26 |
| Number of stocks | 8,755 fund / 8,579 index |
| Median mkt cap | $57.1B fund / $57.0B index |
| P/E, P/B, ROE, EPS growth (factsheet, trailing) | 18.3x, 2.3x, 13.3%, 12.6% |
| Turnover | 4.4% |
| Std dev (3y monthly) | 12.90% fund / 13.92% index |
| Top 10 (15.0% total) | TSMC 4.3, Samsung 2.6, SK hynix 2.2, ASML 1.7, Tencent 0.8, HSBC 0.7, Roche 0.7, Novartis 0.7, Royal Bank of Canada 0.7, AstraZeneca 0.6 |
| Top country weights (% of common stock) | Japan 15.4, Taiwan 9.1, UK 8.0, Canada 7.7, Korea 7.5, China 6.7, Switzerland 5.1, France 5.1, Germany 4.6, India 4.4 |
| Sectors | Financials 22.2, Technology 19.7, Industrials 15.2, Cons. Disc. 8.9, Basic Materials 6.9, Health Care 6.7, Telecom 5.4 (rest cut off in extraction) |

Tracking difference (factsheet, periods to 2026-06-30, NAV return vs "Spliced Total International Stock Index", index returns adjusted for withholding taxes):

| Period | NAV | Index | Diff (pp) |
|---|---|---|---|
| 1y | 27.42% | 26.74% | +0.68 |
| 3y ann. | 18.73% | 18.60% | +0.13 |
| 5y ann. | 8.81% | 8.67% | +0.14 |
| 10y ann. | 9.97% | 9.97% | 0.00 |
| Since inception | 6.68% | 6.66% | +0.02 |

Caveat: the index is stated net of withholding for "U.S.-based mutual funds organized as Delaware statutory trusts" (SEC 497K accn 0001683863-24-000918), so the near-zero difference is against a withholding-adjusted index, not a gross index. Calendar-year fund-vs-index returns: UNKNOWN (not in the factsheet extract).

## 3. Latest quarter & guidance
Not applicable for a fund. Latest distribution: $0.156/share, ex-date 2026-09-18 (yfinance raw dividends; one third-party aggregator [SNIPPET] agrees at $0.1562). No guidance exists.

## 4. Earnings-call takeaways
Not applicable.

## 5. Capital allocation record (FUND analogue: distributions, flows, structure)
- Distribution frequency: quarterly (Vanguard factsheet 2026-06-30). Amounts are lumpy, December is large.
- Raw distributions per share (yfinance, ex-dates): 2025-03-21 0.191; 2025-06-20 0.485; 2025-09-19 0.360; 2025-12-19 1.363; 2026-03-20 0.080; 2026-06-18 0.386; 2026-09-18 0.156. Calendar 2025 sum = 2.399. Last four (Dec 2025 to Sep 2026) = 1.985 = 2.35% of the $84.52 close. yfinance "yield" field = 2.34%. Consistent. (Third-party sites quoted 0.55% to 2.55%; those are stale or wrong, discarded.)
- Foreign tax credit pass-through (Vanguard FTC worksheet, 2024 tax year, https://investor.vanguard.com/content/dam/retail/publicsite/en/documents/taxes/FTCWS_012025.pdf): VXUS foreign-source income 88.6575% of 1099-DIV Box 1a; qualified foreign dividend income 61.1496%; foreign tax paid 7.48% of ordinary cash dividends. Vanguard passes the credit to US taxpayers on 1099-DIV. A non-US holder files no US return claiming it and gets no benefit; the tax is a cost embedded in NAV (the benchmark is likewise net of withholding). That last point is my reading, not a quoted statement.
- Short-term capital gain dividends: Vanguard's 2025 QSG list (https://investor.vanguard.com/content/dam/retail/us/en/pdfs/taxes/1042sb-022026.pdf) states NRA exemption for such dividends; the visible list text did not show Total International Stock (grep for "international"/"total" found nothing in pages 1-2 after the first block; list may be truncated). Treat as UNKNOWN whether any VXUS payout was designated exempt.

## 6. Insider transactions
Insider activity: not applicable to an ETF (no Form 4 filers). Not UNKNOWN in the sense of a gap; no data exists.

## 7. Peers & sector multiples
Consistent vendor comparison of EV/EBITDA, P/E, FCF yield for peers: UNKNOWN (not applicable to funds). The relevant comparison is cost and structure. Sources and dates: Vanguard factsheets (fund-docs.vanguard.com) and justETF profiles, all fetched 2026-10-14.

| Fund | Domicile | Index | Cost | Tracking difference | Dist. |
|---|---|---|---|---|---|
| VXUS (current) | US (Delaware statutory trust per SEC 497K; RIC) | FTSE Global All Cap ex US (~8.6k stocks) | 0.05% | +0.68 / +0.13 / +0.14 / 0.00 pp (1/3/5/10y to 2026-06-30, vs withholding-adjusted index) | Quarterly cash |
| Vanguard FTSE All-World ex-U.S. UCITS ETF USD Acc, IE0009A5ADV9 (tickers VXUA USD / VXUS GBP on LSE) | Ireland, UCITS | FTSE All-World ex US (large+mid; 2,340 stocks) | OCF 0.12% | UNKNOWN: launched 2026-08-18, "performance data will be available after one year"; fund TNA $35M, class $26M at 2026-08-31 | Accumulating |
| Same, Dist class IE000G1H7OC0 | Ireland | same | OCF 0.12% [SNIPPET, search summary of factsheet, not opened] | UNKNOWN | Quarterly [SNIPPET] |
| iShares MSCI World ex-USA UCITS ETF USD Acc, IE000R4ZNTN3 | Ireland | MSCI World ex USA (developed only, 735 holdings) | TER 0.15% | UNKNOWN (launched 2025-01-24, justETF extract had no TD) | Accumulating; fund EUR 3,262M |
| iShares Core MSCI EM IMI UCITS ETF USD Acc, IE00BKM4GZ66 (EM only; pair with a developed ex-US fund) | Ireland | MSCI EM IMI (2,902 holdings) | TER 0.18% | UNKNOWN | Accumulating; EUR 40,259M |
| VWRA, Vanguard FTSE All-World UCITS ETF USD Acc, IE00BK5BQT80 (core, for reference) | Ireland | FTSE All-World (3,784 stocks) | OCF 0.14% (Vanguard factsheet 2026-08-31; justETF agrees 0.14%) | 2020 -0.02, 2021 -0.07, 2022 -0.01, 2023 +0.03, 2024 -0.01, 2025 -0.06 pp (fund minus benchmark, calendar years); 1y/3y/5y to 2026-08-31 22.29/20.45/10.90 vs 22.29/20.47/10.91 | Accumulating |

Cost note: VXUS 0.05% vs the new Irish ex-US UCITS 0.12% = 0.07 pp/yr (arithmetic). An earlier search snippet quoting VWRA at 0.19% is stale/wrong; the issuer shows 0.14%.
Two-fund substitutes for developed ex-US + EM exist but a blended TER depends on weights; not computed (weights would be an assumption).

## 8. Business facts (VWRA overlap and role)
- What it is: passive, sampled index fund of non-US developed and emerging equities, all-cap.
- VWRA FTSE All-World: US weight 61.68% (benchmark 61.71%) at 2026-08-31, so VWRA's ex-US sleeve is about 38.32% (arithmetic, fund-level). VXUS holds essentially the same non-US universe plus small caps (8,755 vs 3,784 stocks). Top holdings overlap (TSMC is VWRA #6 at 1.70%; Samsung, ASML etc. also in both). Adding VXUS to VWRA raises ex-US weight above the market-cap weight: it is a tilt, not diversification. Exact overlap percentage: UNKNOWN (no holdings-file comparison done).
- Both funds are USD; no currency difference.

### US tax facts for a Singapore-resident non-US-person holder (primary texts)
Estate:
- 26 USC 2104(a), verbatim: "shares of stock owned and held by a nonresident not a citizen of the United States shall be deemed property within the United States only if issued by a domestic corporation." (Cornell LII, fetched 2026-10-14).
- 26 USC 851(a), verbatim opening: "the term 'regulated investment company' means any domestic corporation" (Cornell LII, via WebFetch quote; not re-verified in raw HTML).
- VXUS is a Delaware statutory trust (SEC 497K accn 0001683863-24-000918; and Bloomberg LEI search result [SNIPPET]) taxed as a RIC under 851 [RIC status inferred from fund's 1099-DIV/FTC reporting, not directly quoted].
- 26 USC 2105(d) (look-through for RIC stock) "shall not apply to estates of decedents dying after December 31, 2011" (Cornell LII and GovInfo USCODE-2023 both). IRS Form 706-NA instructions (Rev. 08-2025) say the RIC portion rule applies to "an NRNC decedent who died after 2004 and before 2012", and "stock of corporations organized in or under U.S. law is property located in the United States".
- Filing threshold: Form 706-NA required if US-situs assets exceed $60,000 (IRS page). Maximum unified credit "in general ... $13,000" (Form 706-NA instructions Rev. 08-2025). Rates (top rate) not extracted: UNKNOWN.
- Treaty: Form 706-NA instructions list the death-tax treaty countries (Australia, Austria, Canada, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, South Africa, Switzerland, UK). Singapore is not on the list.
- Conclusion supported by the sources: VXUS shares owned by a Singapore-resident non-citizen are, on the statute text, US-situs for estate tax, exposed above $60,000 with only the $13,000 credit. Caveat: Treasury regs 20.2104-1 and any ETF-specific guidance were not retrieved. A third-party commentary [SNIPPET] says neither the Code nor regs specifically address ETFs; the domestic-corporation reading for a RIC is the standard one but this is not a legal opinion. Irish-domiciled UCITS (VWRA etc.) are shares of a non-US issuer, outside 2104(a).
Income:
- 26 USC 871(a)(1)(A): 30 percent tax on US-source dividends to a nonresident alien individual (Cornell LII). RIC dividends are paid by a domestic corporation (861(a)(2)(A): dividends from a domestic corporation are US-source), so the 30% applies to the entire ordinary dividend even though about 89% of the underlying income is foreign-source (FTC table).
- Exceptions under 871(k): interest-related dividends and short-term capital gain dividends are exempt. For an equity-only fund these are small; the Vanguard QSG list did not visibly include VXUS (see section 5). Vanguard's NRA percentage file (ICI layout) not opened: UNKNOWN.
- Treaty: Singapore does not appear in IRS Pub. 901 (text extracted: contains the treaty tables, countries such as Sweden and Switzerland present, "Singapore" absent), so no treaty-reduced rate. W-8BEN instructions: failure to supply may lead to withholding at 30%.
- Vanguard-specific statement that it withholds 30% on brokerage ETF dividends: not found. The Vanguard document located covers IRA withdrawals only. Users hold via a Singapore broker, whose withholding agent practice is UNKNOWN to me; statute rate is 30%.
- Compare Irish-domiciled UCITS holding US stocks: fund-level 15% US withholding under the US-Ireland treaty (Syfe article [SNIPPET]); not relevant to the ex-US stocks in an ex-US fund, where leakage occurs at source-country level in both structures.

## 9. Consensus growth estimates
Not applicable (RULE 2: none collected). Fund-level factsheet "earnings growth rate" 12.6% (2026-06-30) is a backward-looking issuer statistic, not consensus.

## 10. Data warnings & conflicts
Warnings:
1. fundamentals.json VXUS: "fund/ETF: operating-company metrics do not apply". errors: none.
Conflicts and resolutions:
- Price: 00_inputs 84.405 (intraday) vs close 84.52 (+0.14%). Close used. Below 2% threshold.
- Trailing yield: yfinance 2.34% vs my sum of raw distributions 2.35% (agree); third-party pages 0.55 to 2.55% (stale or using partial-year sums; discarded).
- VWRA TER: search snippet 0.19% vs Vanguard factsheet and justETF 0.14%. Issuer figure used.
- VXUS holdings count: factsheet 8,755 (2026-06-30) vs 8,561 (2025-06-30, older factsheet in snippet). Dates differ, not a conflict.
- VWRA holdings 3,784 (Vanguard, 2026-08-31) vs 3,759 (justETF, undated). Issuer used.
- Fund TNA: $651,036M (factsheet 2026-06-30) vs $649,285M (yfinance, undated). 0.3%, ignore.
- 10y yield 5.22% is high versus recent history but matches FRED DGS10 on 2026-10-08.
UNKNOWNs (count 8): (1) calendar-year VXUS vs index returns; (2) tracking difference of Vanguard ex-US UCITS (launched 2026-08-18); (3) tracking differences of iShares ex-US/EM UCITS; (4) exact VWRA/VXUS holdings overlap; (5) Vanguard NRA percentage file / whether any VXUS distribution is 871(k)-exempt; (6) Vanguard/broker actual withholding practice for a Singapore holder; (7) Reg. 20.2104-1 text and top NRA estate rate; (8) Dist-class OCF/ISIN confirmed only by [SNIPPET].
[SNIPPET] items: Delaware statutory trust via Bloomberg LEI listing; Dist-class IE000G1H7OC0 and its OCF; US-Ireland 15% dividend rate; ETF-guidance gap commentary.
Not legal or tax advice; confirm situs with a US-qualified adviser before relying on it.

## Sources
1. Yahoo Finance via yfinance (VXUS history auto_adjust=False; dividends; info), pulled 2026-10-14
2. /Users/User/Desktop/Projects/Investment/data/fundamentals.json (VXUS, as_of 2026-10-13T18:32Z)
3. https://institutional.vanguard.com/iippdf/pdfs/FS3369R.pdf (VXUS factsheet 2026-06-30, F3369_062026)
4. https://www.law.cornell.edu/uscode/text/26/2104 ; /2105 ; /851 ; /871 ; /861
5. https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleB-chap11-subchapB-sec2105.htm
6. https://www.irs.gov/pub/irs-pdf/i706na.pdf (Instructions Form 706-NA Rev. 08-2025)
7. https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
8. https://www.irs.gov/pub/irs-pdf/p901.pdf (US Tax Treaties)
9. https://investor.vanguard.com/content/dam/retail/publicsite/en/documents/taxes/FTCWS_012025.pdf
10. https://investor.vanguard.com/content/dam/retail/us/en/pdfs/taxes/1042sb-022026.pdf
11. https://www.sec.gov/Archives/edgar/data/736054/000168386324000918/f37634d1.htm (497K, accn 0001683863-24-000918)
12. https://fund-docs.vanguard.com/FTSE_All-World_UCITS_ETF_USD_Accumulating_9679_CH_RET_EN.pdf (VWRA factsheet 2026-08-31)
13. https://fund-docs.vanguard.com/FTSE_All-World_Ex-U.S._UCITS_ETF_USD_Acc_E165_EU_INT_EN.pdf (ex-US UCITS factsheet 2026-08-31)
14. https://www.justetf.com/en/etf-profile.html?isin=IE000R4ZNTN3 ; ...IE00BKM4GZ66 ; ...IE00BK5BQT80
15. https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
16. https://www.ch.vanguard/en/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating (VWRA page, WebFetch summary)
17. [SNIPPET] https://professionalparaplanner.co.uk/?p=24991 (fund-launch news, names only)
