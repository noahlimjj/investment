<!-- pipeline:value-researcher -->
# Research dossier: MC.PA (as of 2026-10-13)

Units: EUR millions unless stated. Quote ccy EUR, reporting ccy EUR (IFRS). Not an SEC filer. No ADR ratio applies to the Paris line (OTC ADR LVMUY exists, not used). Source IDs [S#] are listed at the end; machine-readable copy in `facts.json`.

## 0. Routing
**FULL.** Profitable operating company. LVMH is a conglomerate of five business groups under one operating model, not a holding company, so SOTP is not required. A segment cross-check is warranted because Fashion & Leather Goods (FLG) is 74% of group profit from recurring operations (PRO) (13,209 / 17,755, FY2025 [S1]) while the groups have different peer multiples (Hermès/Richemont-type for FLG and Watches & Jewelry, Sephora/retail for Selective Retailing, spirits for Wines & Spirits). Suggest the Quant runs consolidated DCF as primary and a segment-multiple cross-check as secondary.

## 1. Snapshot
- Price: EUR 381.65 (yfinance last/close 2026-10-13 [S7]; fundamentals.json 381.7 [S6]). L&S indication 377.60 at 10:05 CEST vs Xetra prior close 384.65 [S13].
- **12-month change: -27.6%** (527.18 on 2025-10-13 -> 381.65 [S7]).
- 52-week range (daily closes): 378.55 (2026-10-02) to 641.64 (2026-01-09); intraday 375.65 to 643.80 [S7]. Conflict: Yahoo `info` field and the Investing.com article cite a 52-week high of 654.70, which does not appear in the price history. Stock is at the bottom of its range.
- Market cap (own build): 381.65 x 495,811,080 shares issued at 30 Jun 2026 [S3] = EUR 189,226m. Treasury shares at 30 Jun 2026 UNKNOWN (1,295,928 at 31 Dec 2025 [S1]). Yahoo: 188,091m on 492,965,227 shares [S7].
- Shares: issued 497,686,940 at 31 Dec 2025 [S1], 495,811,080 at 30 Jun 2026 [S3]. Weighted average basic 494,587,155, diluted 494,957,592 (H1 2026 [S3]).
- EV build at 30 Jun 2026 balance sheet [S3]: market cap 189,226 + net financial debt 8,245 + IFRS 16 lease liabilities 16,261 (13,509 + 2,752) + minority interests (book) 1,599 + purchase commitments for minority interests' shares 6,416 = **221,747 incl. leases and puts** (205,486 excluding leases). Assets/liabilities held for sale (DFS: 2,074 / 1,025) not netted. The puts partly overlap with minority-interest book value; treatment left to the Quant. Yahoo EV: 216,133 [S7].
- Trailing P/E 17.6, forward 15.7 (fundamentals.json [S6]). Own TTM diluted EPS 21.94 (21.85 + 11.51 - 11.42) gives 17.4x. Dividend EUR 13.00/yr = 3.4% yield.
- France 10-year OAT: ~4.75% on 7 Oct 2026, after a >5% peak the prior week (TradingEconomics snippet [S11], secondary, not verified for 13 Oct). Treat as approximate.
- fundamentals.json (re-fetched 13:24Z after data-layer fix): `errors` empty; one warning about cash-flow vs income-statement net income (see Section 10, item 1) [S6].

## 2. Financial history (EUR m; FY to 31 Dec)
Sources: FY2023-FY2025 from FD2025 [S1] (FY2023 also cross-checked in [S2]); FY2021-FY2022 from FD2023 [S2]. All fiscal-year figures are reported IFRS.

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | TTM (Jun-26) |
|---|---|---|---|---|---|---|---|---|
| Revenue | 64,215 | 79,184 | 86,153 | 84,683 | 80,807 | 39,810 | 38,644 | 79,641 |
| Gross profit | 43,860 | 54,196 | 59,277 | 56,765 | 53,528 | 26,610 | 25,936 | 52,854 |
| Gross margin | 68.3% | 68.4% | 68.8% | 67.0% | 66.2% | 66.8% | 67.1% | 66.4% |
| Profit from recurring ops (PRO, = EBIT) | 17,151 | 21,055 | 22,802 | 19,571 | 17,755 | 9,012 | 8,691 | 17,434 |
| PRO margin | 26.7% | 26.6% | 26.5% | 23.1% | 22.0% | 22.6% | 22.5% | 21.9% |
| Operating profit (after other op. items) | 17,155 | 21,001 | 22,560 | 18,907 | 17,099 | 8,998 | 8,714 | 16,815 |
| Net profit before minorities | 12,698 | 14,751 | 15,952 | 12,958 | 11,222 | 5,915 | 6,019 | 11,326 |
| Net profit, Group share | 12,036 | 14,084 | 15,174 | 12,550 | 10,878 | 5,698 | 5,697 | 10,877 |
| Diluted EPS (EUR) | 23.89 | 28.03 | 30.33 | 25.12 | 21.85 | 11.42 | 11.51 | 21.94 |
| D&A incl. provisions + ROU depreciation (a) | 5,830 | 6,226 | 7,177 | 7,796 | 8,001 | 3,461 | 3,317 | 7,857 |
| SBC (bonus-share plan expense) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 159 | 69 | 97 | 187 |
| Net cash from operating activities | 18,648 | 17,833 | 18,400 | 18,924 | 18,874 | 7,881 | 7,647 | 18,640 |
| Operating investments (capex) | -2,664 | -4,969 | -7,478 | -5,531 | -4,567 | -2,360 | -2,061 | -4,268 |
| Repayment of lease liabilities | -2,453 | -2,751 | -2,818 | -2,915 | -2,974 | -1,489 | -1,486 | -2,971 |
| **Operating FCF (company def., after capex AND lease principal)** | 13,531 | 10,113 | 8,104 | 10,478 | 11,333 | 4,032 | 4,100 | 11,401 |
| OCF - capex only (Yahoo-style, ignores lease principal) | 15,984 | 12,864 | 10,922 | 13,393 | 14,307 | 5,521 | 5,586 | 14,372 |
| Dividends paid (incl. minorities) | -4,161 | -6,774 | -7,159 | -7,322 | -7,123 | -4,060 | -3,991 | -7,054 |
| Buybacks ("other equity-related transactions") | -552 | -1,604 | -1,569 | -224 | -1,634 | -1,239 | -1,658 | -2,053 |
| Cash & equivalents (balance sheet) | 8,021 | 7,300 | 7,774 | 9,631 | 8,794 | 8,176 | 6,803 | 6,803 |
| Cash + current AFS financial assets | UNKNOWN | 10,852 | 11,264 | 13,587 | 13,502 | UNKNOWN | 12,202 | 12,202 |
| Borrowings (LT + ST) | 20,240 | 19,739 | 21,907 | 22,942 | 20,343 | 22,381 | 20,485 | 20,485 |
| Net financial debt (excl. leases, excl. minority puts) | 9,607 | 9,201 | 10,746 | 9,228 | 6,857 | 10,176 | 8,245 | 8,245 |
| **IFRS 16 lease liabilities (non-current + current)** | 14,274 | 15,408 | 16,538 | 17,832 | 16,018 (b) | 16,912 | 16,261 | 16,261 |
| Purchase commitments, minority interests' shares | UNKNOWN | UNKNOWN | 11,919 | 8,056 | 6,331 | 7,015 | 6,416 | 6,416 |
| Total equity (incl. minorities) | 48,909 | 56,604 | 62,701 | 69,287 | 68,949 | 66,875 | 69,694 | 69,694 |
| Equity, Group share | 47,119 | 55,111 | 61,017 | 67,517 | 67,472 | 65,295 | 68,095 | 68,095 |
| Dividend per share for the year (EUR) | 10.00 | 12.00 | 13.00 | 13.00 | 13.00 | - | interim 5.50 | - |
| Diluted weighted-avg shares (m) | 503.90 | 502.48 | 500.30 | 499.68 | 497.98 | 498.74 | 494.96 | - |

TTM = FY2025 + H1 2026 - H1 2025 (own arithmetic). (a) D&A = "net increase in depreciation, amortization and provisions" + "depreciation of right-of-use assets" from the cash-flow statement; it includes provision movements, and equals Yahoo's 8,001 for FY2025. (b) FY2025 excludes c.1.0bn of DFS lease liabilities reclassified to liabilities held for sale [S1], so it is not like-for-like with FY2024. H1 2025 lease total = 14,128 + 2,784 [S3]. H1 2025 gross profit/borrowings and FY2021 borrowings are sums of sourced lines. Debt (incl. leases) at 30 Jun 2026 = 20,485 + 16,261 = 36,746; Yahoo totalDebt 37,151 [S7].

Growth (own arithmetic): revenue +23.3% (FY22), +8.8% (FY23), -1.7% (FY24), -4.6% (FY25). Diluted EPS FY2021 -> FY2025 is 23.89 -> 21.85, i.e. about -2% a year, with a peak of 30.33 in FY2023. FY2025 EPS is 28% below the FY2023 peak.

Segment data (revenue / PRO, EUR m) [S1][S2]:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Wines & Spirits | 5,974 / 1,863 | 7,099 / 2,155 | 6,602 / 2,109 | 5,862 / 1,356 | 5,358 / 1,016 |
| Fashion & Leather | 30,896 / 12,842 | 38,648 / 15,709 | 42,169 / 16,836 | 41,060 / 15,230 | 37,770 / 13,209 |
| Perfumes & Cosmetics | 6,608 / 684 | 7,722 / 660 | 8,271 / 713 | 8,418 / 671 | 8,174 / 727 |
| Watches & Jewelry | 8,964 / 1,679 | 10,581 / 2,017 | 10,902 / 2,162 | 10,577 / 1,546 | 10,486 / 1,514 |
| Selective Retailing | 11,754 / 534 | 14,852 / 788 | 17,885 / 1,391 | 18,262 / 1,385 | 18,348 / 1,780 |
| Other + elims | 19 / -451 | 282 / -274 | 324 / -409 | 503 / -617 | 671 / -491 |

FLG PRO margin: 41.6% (FY21), 40.6%, 39.9%, 37.1% (FY24), 35.0% (FY25). FY2021 and FY2022 "Other + elims" are derived as total minus the five groups. H1 2026 PRO by group: W&S 582, FLG 6,195 (34.1% margin), P&C 417, W&J 831, SR 893, Other -228 [S3].

FY2025 revenue by region of delivery: France 8%, Europe ex-France 18%, US 26%, Japan 8%, Asia ex-Japan 26%, Other 14%. By invoicing currency: EUR 21%, USD 29%, JPY 8%, HKD 3%, other 39% [S1].

## 3. Latest quarter & guidance
**Q3 2026 revenue was published 2026-10-12 (before this run) [S4].** Q3 revenue 18,504 vs 18,280 in Q3 2025; 9M revenue 57,148 vs 58,090 (-2% reported, +2% organic; FX -3%, scope -1%). Q3 organic +1% (scope -2%, FX +2%).

| Organic growth | Q1 26 | Q2 26 | Q3 26 | 9M 26 | 9M revenue 26 |
|---|---|---|---|---|---|
| Wines & Spirits | +5% | +5% | +6% | +5% | 4,027 |
| Fashion & Leather | -2% | +1% | **-5%** | -2% | 26,391 |
| Perfumes & Cosmetics | 0% | -1% | +1% | 0% | 5,922 |
| Watches & Jewelry | +7% | +11% | +6% | +8% | 7,725 |
| Selective Retailing | +4% | +6% | +8% | +6% | 12,476 |
| Group | +1% | +3% | +1% | +2% | 57,148 |

Q3 release verbatim: "In the third quarter, organic revenue growth reflected the impact on business activity of a less buoyant environment in China, while the United States, Europe and Japan saw good growth." And: "The Fashion & Leather Goods business group continued to benefit from the buoyant US market but was affected in the third quarter by the slowdown in demand in China." Marc Jacobs was sold to WHP Global on 1 Sep 2026; "Most of DFS' businesses were sold." [S4]

Outlook (Q3 release, verbatim): "Despite an economic and geopolitical environment that remains uncertain, the Group remains confident and will maintain a strategy focused on continuously enhancing the desirability of its brands... LVMH will draw on its powerful brands and the talent of its teams to reinforce its global leadership position in luxury goods once again in 2026." [S4] No numeric guidance. LVMH has not given numeric revenue or margin guidance in these releases.

**H1 2026 (27 Jul 2026) [S3]:** revenue 38,644 (-3% reported, +2% organic; FX -5%, scope -1%); PRO 8,691 (-4%), margin 22.5%; Group-share net profit 5,697 (flat); operating FCF 4,100 (+2%); net financial debt 8,245 (-19% vs H1 2025's 10,176); equity 69,694. Q2 organic +3% (+4% excluding Middle East conflict). Interim dividend EUR 5.50 payable 3 Dec 2026. Verbatim: "While continuing to pay very close attention to margins, we are entering the second half of the year with renewed confidence in the long-term potential of our Maisons". Currency effect on PRO H1: EUR 686m (secondary, trbusiness snippet; not verified in primary).

Q3 2026 earnings/not-yet-released items: the Q3 release carries no profit data. The next profit print is FY2026 results (date UNKNOWN; MarketScreener projects late Jan 2027 [secondary]).

## 4. Earnings-call takeaways
Primary transcripts not obtained (WebFetch of transcript sites returned nothing usable). The following is from an AI-assisted secondary article on the Q3 2026 call [S9]; treat as unverified and check against the transcript:
- CFO Cecile Cabanis: "a more macro-led challenging consumer backdrop among Chinese clientele"; near-term China challenges, no recovery timeline given.
- Price cuts not part of strategy: "hitting the sweet spot between desirability on one hand and perceived value on the other hand."
- Q3 FLG decline attributed partly to "a one-off logistic and transportation disruption" at Louis Vuitton costing more than 1 point of growth.
- Regional organic: US +5% in Q3 (+4% 9M); Japan +6% Q3; Asia ex-Japan -5% Q3 (after +7% Q1, +4% Q2); Europe +4% Q3.
- FX headwind on margin about 70 bps in H2 2026 similar to H1, easing in 2027. Management expects continued W&S growth (mid-single digit) and W&J growth in Q4.
- 9M buybacks "EUR 2.3bn" (article) - H1 primary figure is 1,658-1,659 [S3], so a further ~0.6bn in Q3 is implied but unverified.
Not obtained: analyst Q&A, what was dodged, and comparison with prior-call topics. Marked UNKNOWN.

## 5. Capital allocation record
- **Buybacks (company programmes) [S1]:** 2023: EUR 1,500m for 1,791,189 shares (avg ~EUR 837). 2025: EUR 1,000m for 1,899,397 shares (avg ~EUR 527), approved Feb 2025. Total 2025 purchases (incl. bonus-share and liquidity): 3,525,467 shares for EUR 1,863m (avg ~EUR 528); 2,654,760 shares retired in 2025. H1 2026: LVMH-share acquisitions 1,659; 1,875,860 shares retired [S3]. No 2024 programme (cash line 224). Averages are own arithmetic from sourced amounts and share counts. Buybacks 2023 were bought near the cycle top; 2025-26 near lows.
- **Share count:** issued 500,341,700 (Dec 2024) -> 497,686,940 (Dec 2025) -> 495,811,080 (Jun 2026). Diluted weighted average 503.9m (FY21) -> 498.0m (FY25).
- **Dividends:** EUR 10 / 12 / 13 / 13 / 13 for FY2021-25. FY2025: interim 5.50 (paid Dec 2025) + 7.50 balance (paid Apr 2026) [S1,S7]. Cash paid FY2025 7,123 incl. minorities; Group-share 6,463 [S1]. Payout on FY2025 EPS 21.85 = 59.5% (own arithmetic). FCF after dividends (operating FCF 11,333 - dividends 7,123) = 4,210; after buybacks (1,634) = 2,576 (own arithmetic).
- **M&A:** 2021 cash for consolidated investments 13,226 (the year of the Tiffany acquisition; deal price not read from a primary document in this run, so purchase price UNKNOWN). Net cash for acquisitions/disposals: 2022 -809, 2023 -721, 2024 -438, 2025 +149. Minority buyouts: 2025 1,091 (incl. an additional 9% of Loro Piana [S1]). Minority puts liability falling: 11,919 (2023) -> 8,056 -> 6,331 (2025) -> 6,416 (Jun 2026).
- **Writedowns and disposals:** "Other operating income and expenses" -656 in FY2025, -664 in FY2024, -242 in FY2023, mainly impairment of brands/goodwill and fixed assets, "primarily related to DFS" in 2025 [S1]. DFS: January 2026 sale of a significant portion to China Tourism Group Duty Free; net assets of 1.2bn reclassified to held-for-sale; estimated loss c.0.5bn recognised; DFS 2025 revenue 1,494 [S1]. Goodwill fell from 24,022 (2023) to 18,315 (2025) per Yahoo balance sheet [S7]. Marc Jacobs sold 1 Sep 2026 (price UNKNOWN).
- **Debt maturities (gross borrowings after derivatives, 31 Dec 2025) [S1 Note 19.2]:** 2026 7,923; 2027 1,986; 2028 1,767; 2029 2,107; 2030 863; 2031 1,505; thereafter 4,206; total 20,358. Against cash + current AFS assets of 13,502. Lease payments schedule (undiscounted): 2026 2,990; 2027 2,702; 2028 2,295; 2029 1,974; 2030 1,635; 2031-35 4,847; 2036-40 1,041; later 680; total 18,163, PV 16,018 [S1 Note 7.2].
- Interest: cost of net financial debt -348 and interest on lease liabilities -553 (FY2025); -442 and -510 (FY2024) [S1]. Lease interest is shown separately from financial-debt interest.

## 6. Insider transactions
- Holding (not activity): Arnault family group 247,694,473 shares = 49.77% of capital, 65.89% of voting rights at 31 Dec 2025 [S1]; reported at 50.01% of capital / 65.94% of votes on 24 Feb 2026 [S12].
- Transactions (secondary: abcbourse listing and AMF notices via search snippet, not verifiable at primary level [S10]): Arnault family entities were net buyers in 2026, with reports of more than 1.1 million shares bought from the start of 2026 up to 19 Feb 2026 (248,874,567 shares held after). Examples: Financiere Agache 20,288 shares at EUR 492.89 (12 Mar 2026); Christian Dior SE 20,197 at EUR 495.11 (9 Mar) and 9,803 at EUR 499.68 (11 Mar); director Ariane Gorin 500 shares at EUR 480.09 (23 Apr 2026, declared 27 May).
- Sales by insiders in the last 12 months: UNKNOWN. Purchases after April 2026 by family entities: UNKNOWN. Full AMF register not accessed.

## 7. Peers & sector multiples
Single vendor (Yahoo Finance via yfinance, 2026-10-13), each in its own currency. Vendor EV includes lease liabilities and EBITDA is post-IFRS 16; FCF yield = Yahoo `freeCashflow` / market cap, which for LVMH is OCF - capex and does NOT deduct lease principal (LVMH company FCF is 20% lower).

| Name | Ccy | Trailing P/E | Forward P/E | EV/EBITDA | FCF yield (Yahoo) |
|---|---|---|---|---|---|
| LVMH | EUR | 17.6 | 15.7 | 10.8 | 6.1% (11.5bn / 188.1bn) |
| Hermes (RMS.PA) | EUR | 30.3 | 26.1 | 18.0 | 3.7% |
| Kering (KER.PA) | EUR | n/a | 21.4 | 14.5 | 10.0% |
| Richemont (CFR.SW) | CHF | 31.5 | 21.2 | 18.2 | 2.6% |
| Prada (1929.HK) | HKD | 11.4 | 9.7 | 6.6 | 1.9% |

Burberry excluded (price reported in GBp, distorted). Christian Dior SE excluded (LVMH holding vehicle). Peer financial-year ends and reporting differ; Prada's low multiples look unusual and were not cross-checked. LVMH trades at roughly a 40% discount to Hermes and Richemont on forward P/E and EV/EBITDA, and at 1.2-1.3x the Kering forward multiple discount (own arithmetic).

## 8. Business facts (two-minute-drill inputs)
- What it sells: 75 Maisons in 6 segments: Wines & Spirits (Moet & Chandon, Dom Perignon, Veuve Clicquot, Hennessy, etc.), Fashion & Leather Goods (Louis Vuitton, Dior, Celine, Loewe, Fendi, Loro Piana, Rimowa, Berluti, Givenchy), Perfumes & Cosmetics (Dior, Guerlain, Benefit, Fenty), Watches & Jewelry (Tiffany, Bvlgari, TAG Heuer, Hublot, Chaumet), Selective Retailing (Sephora, Le Bon Marche, DFS being sold), other (Les Echos, Belmond, Cheval Blanc) [S3][S5]. 6,283 stores, 211,552 employees at 31 Dec 2025 [S5].
- Mix FY2025 revenue: FLG 47% (37,770), Selective Retailing 23%, W&J 13%, P&C 10%, W&S 6%, other 1% [S1]. PRO mix: FLG 13,209 (74% of group PRO).
- Customers: global consumers, no single-customer concentration disclosed. Geography per Section 2. Asia ex-Japan share fell from 31% (2023) to 26% (2025).
- Market share: not disclosed by LVMH in these documents; Sephora described as "world leader in beauty retail" and LVMH as "the only group that operates simultaneously in all the major luxury sectors" [S1][S5].
- Recent events with dates: Jan 2026 DFS Greater China sale to China Tourism Group Duty Free; Jonathan Anderson's first Dior designs credited with H1 acceleration (H1 release, 27 Jul 2026); new Louis Vuitton flagships Beijing and Seoul; Marc Jacobs sold 1 Sep 2026; Q3 2026 China slowdown (12 Oct 2026); Middle East conflict cost ~1 point of Q2 growth [S3]; Arnault family crossed 50% of capital in Feb 2026.
- Tape vs narrative: stock down 27.6% over 12 months and at the bottom of its 52-week range while H1 2026 showed a growth re-acceleration (organic +3% Q2). The Q3 slowdown (Group +1%, FLG -5%, Asia ex-Japan -5%) is consistent with the weak tape. PRO margin has fallen from 26.5% (FY2023) to 21.9% (TTM).

## 9. Consensus growth estimates
CONSENSUS (Yahoo Finance, 2026-10-13, vendor aggregate; no price targets or ratings collected):
- EPS FY2026 avg EUR 22.18 (range 21.59-22.88, 17 analysts), +1.5% vs FY2025 actual 21.85. EPS FY2027 avg EUR 24.43 (22.72-30.52, 18 analysts), +10.2%.
- Revenue FY2026 avg EUR 80.74bn (-0.1% vs FY2025 80.81bn); FY2027 avg EUR 84.45bn (+4.6%).
- Company's own history for comparison: revenue CAGR FY2021-FY2025 +5.9% (64,215 -> 80,807), but -1.7% and -4.6% in the last two years; diluted EPS -2% a year over FY2021-25 and -28% from the FY2023 peak. These estimates predate or only partly reflect the 12 Oct Q3 release. Estimate dates for the individual analysts are UNKNOWN.

## 10. Data warnings & conflicts
1. **Data-layer correction (orchestrator, re-fetch 2026-10-13T13:24Z).** The earlier MC.PA record took `net_income` from the cash-flow statement (17,099 = operating profit, the IFRS cash-flow starting line), which overstated owner earnings by about 44%. Re-fetched record now uses income-statement net income 10,878 (verified against FD2025: Net profit, Group share 10,878 [S1]) and carries the warning "cash-flow net income 17,099,000,000 differs from income-statement 10,878,000,000 by +57% (IFRS pre-tax start?) - income statement used". Current owner_earnings = EUR 14,209m (USD 15.92bn) = 10,878 + 8,001 - 4,670 [S6]. The superseded figure is not used anywhere. Caveat that remains: D&A 8,001 includes 3,143 of right-of-use depreciation while lease principal (2,974) is not deducted, so lease-adjusted owner earnings are about 11,235 (own arithmetic). Group-share profit, not pre-minority (11,222), is the basis.
2. `fcf` 14,205 in fundamentals.json = OCF - capex; it ignores lease principal of 2,974. Company operating FCF is 11,333.
3. D&A 8,001 includes right-of-use depreciation of 3,143; owner earnings built from it without subtracting lease cash costs flatter the business.
4. fundamentals.json `debt_to_equity` 0.533 (Yahoo) includes leases; company gearing (net financial debt / equity) is 9.9% at Dec 2025 and 11.8% at Jun 2026 (Quartr, secondary) [S1].
5. Net financial debt excludes leases (16,261) and minority puts (6,416). Lease interest (553) sits in "net financial income/expense", not in PRO.
6. 52-week high conflict: 641.64 (close) / 643.80 (intraday) from price history vs 654.70 in Yahoo info and an article.
7. Share-count conflict: Yahoo 492,965,227 outstanding vs 495,811,080 issued at 30 Jun 2026 (the former likely nets treasury shares; difference 0.6%, under 2%).
8. FY2024 revenue: Yahoo 84,682 vs LVMH 84,683 (rounding). Gross profit FY2022: Yahoo 54,195 vs LVMH 54,196. Not material.
9. FY2025 lease liabilities exclude c.1.0bn DFS leases (held for sale); FY2025 gross borrowings and balance sheet include held-for-sale reclassification effects.
10. 10-year OAT 4.75% is a secondary-source snippet for 7 Oct; other snippets cite "below 4.75%/4.8%" late September. Approximate.
11. The Q3 2026 call commentary comes from an AI-assisted article; the Q3 call Q&A transcript was not obtained.
12. **French dividend withholding tax for a Singapore-resident individual: 12.8%** (PwC Worldwide Tax Summaries: domestic rate 12.8% where the beneficiary is an individual; France-Singapore treaty dividends 5%/15%, the 5% rate needing a corporate shareholding of at least 10%, so the 15% treaty cap sits above the domestic 12.8% [S8]). Non-treaty non-resident companies: 25%. Caveat: secondary source; the rate actually deducted depends on the broker/custodian chain and on residence documentation, and a higher default rate at source with later reclaim is possible. The 0.4% French financial transaction tax on LVMH purchases and Singapore tax treatment of the dividend were not sourced here: UNKNOWN.
13. UNKNOWN count: SBC FY2021-FY2024 (4), FY2021 cash+AFS, H1 2025 cash+AFS, minority puts FY2021-22 (2), Tiffany price, Marc Jacobs price, treasury shares at 30 Jun 2026, insider sales and post-April purchases, Q3 call Q&A, prior-call comparison, FY2026 results date, individual consensus dates. Source disagreements above 2%: none. Blocking issues: none; the net_income issue was corrected in the data layer (item 1).

## Sources
[S1] https://lvmh-com.cdn.prismic.io/lvmh-com/aXjqHgIvOtkhB_8I_Financialdocuments-December31%2C2025.pdf (Financial Documents, 31 Dec 2025)
[S2] https://cdn.luxe.digital/download/financial-documents-lvmh-december-31-2023.pdf (English translation of LVMH Financial Documents, 31 Dec 2023; third-party host)
[S3] https://lvmh-com.cdn.prismic.io/lvmh-com/HpVUWE8YyscbnlXI_LVMH2026HalfYearResults_Pressrelease.pdf (H1 2026 results, 27 Jul 2026; page: https://www.lvmh.com/en/publications/accelerating-growth-in-the-second-quarter---solid-first-half-results)
[S4] https://lvmh-com.cdn.prismic.io/lvmh-com/Y6AfTE0Y7WFnyftQ_LVMH2026ThirdQuarterRevenue.pdf (Q3 2026 revenue, 12 Oct 2026; page: https://www.lvmh.com/en/publications/continued-growth-in-the-third-quarter-of-2026)
[S5] https://lvmh-com.cdn.prismic.io/lvmh-com/aczo-pGXnQHGZKQ5_UniversalRegistrationDocument2025.pdf (URD 2025)
[S6] data/fundamentals.json, MC.PA record, 2026-10-13T13:18:26Z
[S7] yfinance / Yahoo Finance, pulled 2026-10-13 (prices, peers, consensus, Yahoo statements)
[S8] https://taxsummaries.pwc.com/france/corporate/withholding-taxes
[S9] https://www.investing.com/news/company-news/lvmh-q3-2026-slides-1-growth-as-us-europe-offset-china-slump-93CH-4945011 (AI-assisted, secondary)
[S10] abcbourse.com transactions_dirigeants LVMH (via search snippet; fetch returned 403)
[S11] tradingeconomics.com/france/government-bond-yield/news (via search snippet)
[S12] https://www.lalibre.be/economie/entreprises-startup/2026/02/24/la-famille-arnault-detient-desormais-plus-de-50-du-capital-lvmh-MEV3FIQR7FDMJPXYEBNPNVFZGE/
[S13] https://www.ad-hoc-news.de/boerse/news/corporate-news/lvmh-reports-1-percent-third-quarter-growth-and-lvmh-stock-loses-1-83-percent/70311764
