<!-- pipeline:value-researcher -->
# Research dossier: ZBH (as of 2026-10-13)

## 0. Routing
FULL. Profitable operating company (orthopaedic / medtech devices), FY2025 revenue $8,232M, net income $705M.

## 1. Snapshot
- Price $92.17 USD (fundamentals.json/yfinance, 2026-10-13). Quote and reporting currency both USD, figures in USD millions. No ADR. (Also listed on SIX.)
- 12m price change: -2.0% ($94.08 close 2025-10-13 to $92.17; price only, dividends excluded). 52w range $79.12-$106.88 (yfinance info). Tape: flat over a year, about 14% below the 52w high.
- Market cap $17,580M (fundamentals.json). Shares outstanding 190.74M (yfinance); FY2025 diluted 199M (10-K via sec_facts); latest-quarter diluted count UNKNOWN (not extracted).
- EV build (Q2 2026 balance sheet, 8-K ex99.1, 2026-06-30): market cap 17,580 + current debt 1,201.5 + long-term debt 6,277.5 - cash 410.0 = ~$24,649M. yfinance EV $24,726M (0.3% diff). Operating lease liabilities not included: UNKNOWN. Noncontrolling interest negligible (FY2025 NCI result -$0.1M).
- Trailing P/E 22.4 (GAAP), forward P/E 10.2 (vendor, on adjusted EPS; GAAP vs adjusted gap is large). EV/EBITDA 9.8 (yfinance). Dividend $0.96/yr (yfinance dividendRate).
- 10-year US Treasury yield 5.20% (yfinance ^TNX close, 2026-10-13). Verify against Treasury.gov; value is high so worth a check.

## 2. Financial history (USD M; sec_facts.py from SEC XBRL, 10-K FY2025 accn 0001193125-26-059853)
| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | TTM to 2026-06-30 |
|---|---|---|---|---|---|---|---|
| Revenue | 6,128 | 6,827 | 6,940 | 7,394 | 7,679 | 8,232 | 8,509 |
| Gross profit | UNKNOWN (XBRL gap; gross margin series from fundamentals.json: 69.7%/71.5%/71.8%/70.9% for the 4 latest FYs, order per vendor) | | | | | | TTM cost of revenue 2,563 -> GP ~5,946 (derived) |
| Operating income | 83 | 860 | 696 | 1,278 | 1,286 | 1,098 | 1,205 |
| Net income | -139 | 402 | 231 | 1,024 | 904 | 705 | 807 |
| D&A | 898 | 938 | 926 | 952 | 996 | 1,094 | 1,108 |
| SBC | 74 | 76 | 105 | 100 | 101 | 90 | 98 |
| OCF | 1,204 | 1,499 | 1,356 | 1,582 | 1,499 | 1,697 | 1,743 |
| Capex | 112 | 144 | 188 | 291 | 204 | 224 | 220 |
| FCF (OCF-capex) | 1,093 | 1,356 | 1,168 | 1,290 | 1,296 | 1,473 | 1,523 (derived) |
| Buybacks | UNKNOWN | UNKNOWN | 126 | 692 | 868 | 487 | 751 |
| Dividends | 198 | 200 | 201 | 201 | 196 | 190 | 188 |
| Cash | 802 | 378 | 376 | 416 | 526 | 592 | 410 (Jun-26) |
| Non-current debt | 7,626 | 5,464 | 5,152 | 4,868 | 5,342 | 6,932 | 6,277.5 LT + 1,201.5 current |
| Equity | 12,194 | 12,661 | 12,020 | 12,480 | 12,468 | 12,698 | 12,632.5 (Jun-26) |
| Diluted shares | 207 | 210 | 210 | 210 | 204 | 199 | UNKNOWN |

Derived (sec_facts): operating margin 1.4/12.6/10.0/17.3/16.7/13.3%; FCF margin 17.8/19.9/16.8/17.5/16.9/17.9%; ROIC 0.3/4.0/2.9/6.9/6.2/4.7%. Revenue CAGR 6.1% (FY20-25); diluted share CAGR -0.8%.
Interest expense, net: FY2025 $292.8M, FY2024 $218.0M, FY2023 $201.2M (10-K income statement). FY2025 pre-tax earnings $830.8M, tax $125.7M (ETR 15.1%).
Total debt at 2025-12-31 incl. current: 6,932.0 + 587.1 = $7,519M; operating-lease liabilities UNKNOWN.
fundamentals.json: net income 705.1M, D&A 1,093.8M, capex -276.9M, OCF 1,697.1M, owner earnings 1,522M, FCF 1,420.2M, ROE 6.4%, D/E 0.60. Op margins (vendor, 4 FYs): 16.5/19.9/19.6/17.2%.
FY2025 GAAP operating profit fell to 1,098 from 1,286 (Paragon 28 deal/integration, restructuring).

## 3. Latest quarter and guidance (Q2 2026, reported 2026-08-05; 8-K ex99.1)
- Net sales $2,177.0M, +4.8% reported, +4.7% cc, +4.0% organic cc. US $1,239.9M (+5.6%; organic +4.6%); International $937.0M (+3.7%; organic +3.1%).
- Products: Knees $828.9M (+0.4% reported; US +1.4%, Intl -0.9%); Hips $562.7M (+5.0%; US +5.9%); S.E.T. $586.0M (+6.4%; organic +3.4%); Technology & Data, Bone Cement and Surgical $199.4M (+21.1%).
- GAAP diluted EPS $1.03 (+33.8%); adjusted diluted EPS $2.07 (flat y/y). Net earnings $198.3M; adjusted $399.6M.
- Adjusted operating margin 25.7% (Q2 2025 27.8%), H1 26.5% (H1 2025 27.1%). GAAP operating margin 15.0% (14.4%). So adjusted margin fell ~210bp y/y in the quarter. Adjusted tax rate 18.0%.
- OCF $447.9M, FCF $308.3M in Q2. H1 2026 share repurchases $500.8M (H1 2025 $237.0M).
- Balance sheet 2026-06-30: cash 410.0; current debt 1,201.5 (was 587.1 at Dec-25); long-term debt 6,277.5; equity 12,632.5; goodwill 9,919.5; intangibles 4,461.6.
- Guidance verbatim table: FY2026 reported revenue change 3.9%-4.9% (prior 2.5%-4.5%); FX +0.5%; constant currency 3.4%-4.4% (prior 2.0%-4.0%); organic cc 2.25%-3.25% (prior 1.0%-3.0%); adjusted diluted EPS $8.47-$8.59 (prior $8.40-$8.55). Footnote: organic excludes Paragon 28 through its one-year anniversary, "approximately 110bps".
- Highlight: "Announced increase to share repurchase expectations of up to $1 billion of its common stock during fiscal year 2026."
- CEO Ivan Tornos: "we are raising our revenue and adjusted EPS guidance for the year."
- Other: Sang Yi (Asia Pacific president) departed 2026-08-28, replaced by Chintan Desai. FDA 510(k) for next-gen ROSA Shoulder.

## 4. Earnings-call takeaways
Full Q&A transcript could not be retrieved (paywalled or cut off), so this section is limited. UNKNOWN: tone shifts, dodged questions.
- Knee international decline of 1.5% attributed by management to China and core emerging markets (Nasdaq/MarketBeat call summary via search snippet, not verified against transcript).
- First analyst question (Stifel, Frederick Wise): pace and implications of the US sales-force transition (StockStory summary). Other four questions not retrieved.
- US growth credited to sales-force transformation, Z1 hip stem, OrthoGrid navigation, Paragon 28 (secondary summaries).
- Observation from the numbers, not management: adjusted EPS flat in Q2 while revenue +4.8%; the EPS guide raise ($0.07 at the low end, $0.04 at the high end) is small next to the revenue raise.

## 5. Capital allocation record
- Buybacks: FY22 $126M, FY23 $692M, FY24 $868M, FY25 $487M (10-K), TTM to Jun-26 $751M, H1 2026 $500.8M, FY2026 plan up to $1B. Average price paid: UNKNOWN. Diluted shares 210M (FY22) to 199M (FY25), 190.7M outstanding now (yfinance).
- Dividends ~$190-200M/yr, $0.96/share annual (yfinance).
- M&A: Paragon 28 (closed 2025): $13.00/share cash, equity ~$1.1B, EV ~$1.2B, plus a CVR up to $1.00/share tied to FY2026 sales (search report of deal terms; g-medtech). 10-K: $1,393.2M paid net of cash for Paragon 28 and Monogram in 2025. Monogram Technologies (robotics, closed 2025-10) price UNKNOWN beyond that combined figure. Goodwill/intangible impairments: none found in 10-K FY2025 annual test (fair values exceeded carrying by >25% for the two reporting units quantitatively tested). Earlier large deals (Biomet 2015) are outside the scope of data pulled here: UNKNOWN.
- Restructuring: 2025 Restructuring Plan, ~$155M pre-tax charges by end-2027 (10-K).
- Debt 12/31/2025 (10-K Note 12), principal in $M: Euro 2.425% 2026 587.1; 4.700% 2027 600.0; Euro 1.164% 2027 587.1; 5.350% 2028 500.0; 3.550% 2030 257.5; 5.050% 2030 550.0; Swiss 0.930% 2030 (amount not captured); 2.600% 2031 750.0; Euro 3.518% 2032 822.0; 5.200% 2034 700.0; 4.250% 2035 253.4; 5.500% 2035 600.0; 5.750% 2039 317.8; 4.450% 2045 395.4. Next ~5 years' maturities therefore at least ~$2.3B by 2027 (587.1 repaid/refinanced by Jun-26: current debt now 1,201.5, consistent with the 2027 notes moving to current). Revolvers: $1.5B five-year to 2030-06-27; 364-day $1.0B matured 2026-06-26 (renewal status UNKNOWN).

## 6. Insider transactions (yfinance insider_transactions, 2026-10-13; not verified against Form 4)
- No open-market purchases listed in the last ~12 months.
- Sales with prices: K. Thornal 5,691 sh @ $92.95 (2026-09-11, ~$529K); C. Phipps 3,000 @ $98.35 (2026-09-04, ~$295K); S. Yi 5,000 @ $82.65 (2026-05-29, ~$413K); L. Winkler 2,650 @ $94.66 (2026-03-12, ~$251K).
- Many "D" dispositions without price (2026-02-25, 03-06, 04-01, 07-31, 10-01) incl. CEO Tornos 34,704 and 19,090 sh and CFO Upadhyay 14,776 sh: likely tax-withholding on vesting; unconfirmed. Treat as UNKNOWN nature.
- insider_pct holding 0.16% (static holding, not activity).

## 7. Peers and sector multiples (yfinance .info, all one vendor, 2026-10-13)
| | Price | EV/EBITDA | Trailing P/E | Forward P/E | FCF yield (FCF/mcap) |
|---|---|---|---|---|---|
| ZBH | 92.17 | 9.8 | 22.4 | 10.2 | 6.1% |
| SYK | 282.60 | 16.3 | 29.3 | 16.9 | 3.8% |
| MDT | 91.93 | 13.2 | 22.6 | 14.3 | 4.6% |
| BSX | 43.84 | 13.3 | 17.7 | 13.0 | 3.9% |
| SNN | 27.67 | 44.8 | 18.8 | 11.5 | 9.1% |
| EW | 86.39 | 23.2 | 51.4 | 25.5 | 2.5% |
| GMED | 76.24 | 9.7 | 19.5 | 14.1 | 5.4% |
Note: vendor FCF for ZBH is $1,072M, which differs from fundamentals.json ($1,420M) and SEC-derived TTM ($1,523M). Peer forward P/E bases (adjusted EPS) vary. SNN ADR-based EV/EBITDA looks distorted.

## 8. Business facts
- Sells orthopaedic reconstruction (knees, hips), sports medicine/extremities/trauma/CMFT/thoracic (S.E.T.), and technology/data (ROSA robots, OrthoGrid), bone cement and surgical products, mainly to hospitals and surgery centres via direct sales force (US sales agents converted to employees) and distributors; GPO contracts typically 3 years, hospital pricing pressure is a risk (10-K).
- FY2025 mix: Knees $3,322M (40%), Hips $2,094M (25%), S.E.T. $2,150M (26%), Tech/Data/Cement/Surgical $666M (8%). US $4,764M (58%), International $3,468M (42%). FY2025 growth +7.2% reported, Paragon 28 added ~2.5pts of volume growth (10-K).
- Segment geography: Americas Orthopedics, EMEA, Asia Pacific, CMFT reporting units. EMEA second largest.
- Customer concentration: no single customer disclosed in extracts reviewed: UNKNOWN. Market share: UNKNOWN.
- Recent events: Paragon 28 foot/ankle acquisition (2025); Monogram robotics acquisition (Oct 2025); Z1 hip stem; ROSA Shoulder clearance (2026); US sales-force transition; APAC leadership change (Aug 2026); China weakness in knees.

## 9. Consensus growth estimates (CONSENSUS, yfinance, 2026-10-13)
- Adj EPS FY2026 $8.53 (28 analysts; guide $8.47-$8.59); FY2027 $9.07 (+6.3%). Revenue FY2026 $8,596M (+4.4%); FY2027 $8,904M (+3.6%).
- Company history: revenue CAGR FY20-25 6.1% (flattered by Paragon 28 and COVID base); FY2025 +7.2%; organic cc 2026 guide 2.25-3.25%. GAAP net income fell from $1,024M (FY23) to $705M (FY25); adjusted EPS history not extracted: UNKNOWN beyond FY2025 year-ago consensus figure of $8.20.

## 10. Data warnings and conflicts
- fundamentals.json warning: institutional_pct=1.1137 outside 0..1, vendor artifact; not quoted.
- Conflict: FCF $1,420M (fundamentals.json) vs $1,072M (yfinance info) vs $1,523M (SEC TTM OCF 1,743 minus capex 220); >2%.
- Conflict: capex $276.9M (fundamentals.json) vs $224M FY2025 / $220M TTM (SEC). Possibly includes other investing items.
- Conflict: owner earnings 1,522M (fundamentals.json, uses 276.9 capex, 705 NI) vs 1,574M (sec_facts FY2025).
- Conflict: 52w high $106.88 (info) vs highest daily close ~$102.88 (history); intraday vs close.
- sec_facts gaps: gross profit and interest expense XBRL missing for all years (26 gaps); interest taken from 10-K text.
- UNKNOWN: lease-inclusive debt, latest diluted shares, buyback average prices, Swiss note amount, full call Q&A, customer concentration, market share, FY2020-21 buybacks, 364-day revolver renewal, pre-2025 M&A, 10y yield cross-check.
- Search-sourced facts (Paragon 28 deal terms, call summaries) come from secondary pages.

## Sources
1. data/fundamentals.json (methodologies/fundamentals.py run 2026-10-13)
2. methodologies/sec_facts.py output, reports/runs/ZBH_2026-10-13/facts.json
3. 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1136869/000119312526059853/zbh-20251231.htm
4. Q2 2026 release (8-K ex99.1) as hosted at https://investor.zimmerbiomet.com/news-and-events/news/2026/08-05-2026-113057327
5. yfinance (price history, info, insider_transactions, estimates, ^TNX), 2026-10-13
6. Call summaries via search: nasdaq.com/articles/zimmer-biomet-q2-earnings-call-highlights; stockstory.org Q2 questions
7. Paragon 28 terms: https://g-medtech.com/news/zimmer-biomet-to-acquire-paragon-28-for-1-2-billion-expanding-into-the-5-billion-foot-and-ankle-segment/
