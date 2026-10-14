<!-- pipeline:value-skeptic -->
# Skeptic audit: NVO (as of 2026-10-13)

## 1. Pre-mortem (written before reading the model)
_Written from 01_research.md and facts.json only, before opening 02_quant.md or 02_model.py._

**The most likely structural reason NVO is worth materially less in 2031 is that semaglutide turns into a priced-down commodity before a successor is proven.** This is terminal-value and moat-erosion risk, not a cyclical dip.
- **Concentration.** GLP-1 lines were 76% of Q2-26 adjusted sales: obesity 23,152 + GLP-1 diabetes 36,784 of 78,488 DKK M (6-K 0000353278-26-000023). Almost all of that is one molecule.
- **Price is falling on every front.** US WAC cuts of about 50% (Wegovy) and 35% (Ozempic) start 2027-01-01. The MFN agreement, self-pay at USD 149-299 a month, and loss of exclusivity in Canada and Brazil (where "lower realised prices" are already showing) add to it. The US and EU compound-patent expiry dates are UNKNOWN in the dossier, so the cliff may fall inside or just past the 5-year window.
- **Share loss and weak pipeline.** US Wegovy injectable fell 22% at CER in Q2. CagriSema was non-inferior to tirzepatide on weight, not superior. Ziltivekimab failed and monlunabant was terminated, so no proven successor exists.
- **The erosion already shows in the margins.** Gross margin was 84.7% (FY24), then 81.0% (FY25), then 78.2% adjusted in Q2-26. Operating margin went from 44.2% to 41.3%. Inventory grew 21.5% in FY25 against sales growth of 6.4%, with write-downs of DKK 4.3B.
- **Second-order capital misallocation.** Management built capacity at peak: Catalent sites for USD 11.7B and PP&E capex of 60 bDKK in 2025. It is now "right-sizing manufacturing capacity agreements" (about DKK 3B in one-time costs). That capex was funded with debt: borrowings rose from 27 to 131 bDKK while dividends (51.8 bDKK) exceeded company FCF (28.3 bDKK) in FY25.

**What the model has to survive:** revenue flat to down through 2028, then operating margin drifting from about 41-44% toward big-pharma levels (about 30-35%) instead of the "broadly stable" margin management targets, plus a terminal value that assumes no semaglutide cliff. **What would prove me wrong:** global volume growth (branded obesity volume +81% per IQVIA, May 2026) outrunning price deflation, with the oral pill holding about 90% of its segment.

## 2. Number audit
**Method.** Every recomputation is printed by `03_rerun.py` §1, which loads `02_model.py` unchanged and reproduces the Quant exactly: 156.6 / 347.3 / 554.1 DKK. Primary documents were fetched fresh from EDGAR using the generic SEC contact string: the 20-F (accn 0000353278-26-000012), the FY25 release 6-K (0000353278-26-000006), the Q2-26 6-K (0000353278-26-000023) and the buyback 6-K (0001171843-26-006585). Five figures were spot-checked on the web: DKK 10y, LOE dates, the FY25 adjusted base, the treaty WHT rate and the share count.

| # | Input | Quant value | Verified value | Source | Status | Δ FV (BASE) |
|---|---|---|---|---|---|---|
| 1 | Price | USD 38.415 (00_inputs, 13:52Z intraday) | USD 38.015 per orchestrator (fj, stamped 18:32Z, which is also intraday). Final 2026-10-13 close was **38.06** (yfinance daily history, pulled 2026-10-14). | fj; yfinance | **FAIL: Temporal** | 0 on FV (DKK model). Base upside moves +35.4% to +36.8%. |
| 2 | Shares | 4,413.1m | 4,413.110m = 4,465,000,000 - 51,889,876 treasury | 6-K 0001171843-26-006585 | PASS | 0 |
| 3 | Net debt Dec-25 / claims | 104,494 / 166,914 | Both recomputed exactly. Dec-25 marketable securities were UNKNOWN; they are **498**, giving claims of 166,416. | facts (XBRL); Q2-26 6-K balance-sheet comparative | PASS (one gap filled) | +0.11 DKK/share |
| 4 | Leases inside Borrowings | assumed, "UNCONFIRMED" | **Confirmed.** The company defines net debt as Borrowings "excluding lease liabilities", with an "Add-back of lease liabilities 8,572". | FY25 release 6-K, Appendix 7 | PASS | 0 (the -1.94 sensitivity case is retired) |
| 5 | Net debt Jun-26 | 95,145 | 121,794 + 18,333 - 44,482 - 500 = 95,145 | Q2-26 6-K | PASS | n/a |
| 6 | Base revenue FY25 (adjusted) | 306,464 (340B 2,600) | 306,415. The FY25 340B exclusion is **2,649**. | Q2-26 6-K, Appendix 7 reconciliation | PASS (0.02%, minor source-fidelity) | ~0 |
| 7 | Base EBIT FY25 (adjusted) | 132,374 (adds back 7,316 of impairments) | The company's FY25 adjusted-OP base is **not published**. The H1-25 comparative strips only the 340B (72,240 - 2,649 = 69,591). If FY25 impairments are not stripped, the base is 125,009 and the guide-implied FY26 margin is about 40.4%, not 42.7%. | Q2-26 6-K | UNVERIFIABLE | 0 in the DCF (FY26 is calibrated to the FCF guide). The margin-anchor risk is downside (§7). |
| 8 | "Unexplained" 10,272 FY25 adjusted NP add-back (Quant H4) | open | **Resolved.** Adjusted *net profit* excludes intangible impairments, intangible amortisation and "major restructuring costs" (~DKK 8bn). It is a different measure from adjusted *operating profit*, which excludes 340B, major legal matters and major impairments. The Quant's 47% alternative base is not supported. | FY25 release, Appendix 7 | RESOLVED, in the Quant's favour | 0 |
| 9 | **WACC 7.01%** (load-bearing #1) | DKK 10y 3.01% + 4% floor | (i) 3.01% is the OECD **August** monthly average, and FRED has nothing later as of 2026-10-14. The latest print found is **3.17% on 1 Sep 2026** (Trading Economics, secondary), giving a floor of 7.17%. (ii) The model holds FX flat on DKK cash flows of which **51.3%** of sales are US (76,254 / 148,551 H1-26 adjusted), so USD-earned flows are discounted at a DKK rate. Blending 51.3% x USD floor 8.00% with 48.7% x 7.17% gives **7.60%**. | 00_inputs; FRED csv; tradingeconomics.com; Q2-26 6-K | **FAIL: Temporal + Comparability** | **-12.1%** (347.3 to 305.5 DKK; USD 52.01 to 45.74). Rate (i) alone: -3.5%. Blend on the stale rf (7.52%): -10.6%. |
| 10 | EBIT margin path (#2) | FY26 42.7%, FY27-35 39.5-41% | FY26 recomputed as 125,755 / 294,205 = 42.74%. H1-26 adjusted margin 44.6%; Q2 42.5% including ~3bn one-offs. FY27+ is an ASSUMPTION. | Q2-26 6-K | PASS (arithmetic) | 0 |
| 11 | FY27+ revenue level (#3) | FY27 -3% | ASSUMPTION (no 2027 guidance). Reasonable. | n/a | n/a | 0 |
| 12 | Tax 22% | 22% | Guidance 21-23% | Q2-26 6-K | PASS | 0 |
| 13 | Terminal growth | 2.5% | Below the DKK 10y | n/a | PASS | 0 |
| 14 | FY26 capex / FCF guide | 55bn / 45-55bn | "Around 55 bDKK"; "Between 45 and 55 bDKK", where FCF = OCF less PP&E | Q2-26 6-K | PASS | 0 |
| 15 | Terminal ROIC / FY25 ROIC | 20% / 33.6% | 33.55% recomputed | facts | PASS | 0 |
| 16 | D&A FY26 | 15,024 | (13,840 - 6,328) x 2 | dossier / 6-K | PASS | 0 |
| 17 | BD allowance | 1.45% | Arithmetic is right (median FY21-24 intangibles / revenue), but the definition omits business acquisitions. See J3. | facts | PASS (arithmetic); model-fidelity concern | -2.0% at 3% (§7) |
| 18 | Semaglutide share of sales | at least 68.9% (Q2 floor) | **73.9% of FY25 sales** (Ozempic 127,089 + Wegovy 79,106 + Rybelsus 22,093). US + EUCAN semaglutide alone is 62.6%. | 20-F (key-products table) | FAIL: source fidelity (understated, but labelled a floor) | context for J1 |
| 19 | Semaglutide LOE dates | UNKNOWN | Compound patent including extensions: **US 2032; Europe 2031; Japan 2031; China 2026**. The 20-F text says: "Compound patent expiry in the US for the semaglutide branded products - Ozempic, Rybelsus, and Wegovy - is 2032". | 20-F, Annual Report patent table | RESOLVED. The Quant's FY32-33 timing is consistent. | depth: J1 |
| 20 | Sales-deduction provision | 140,201 | Jun-26 140,201; Dec-25 133,349 | Q2-26 6-K | PASS | n/a |
| 21 | Identities | FCF = OCF - PP&E; EV = mcap + ND; IC | All recomputed exactly (58,962; 1,227,354; 298,541) | facts | PASS | 0 |
| 22 | TV share | 55 / 63 / 68% | Same. Below 75%, no flag. Skeptic scenarios: 57 / 59 / 66%. | model | PASS | 0 |
| 23 | IFRS 16 in explicit FCF | lease principal not deducted | D&A includes ROU depreciation, but future lease cash is never deducted in FY26-35. That overstates FCF by about the lease principal (FY25 1,503), roughly -2.4 DKK/share. The terminal value is unaffected (NOPAT bears ROU depreciation). | FY25 release | minor model-fidelity issue | about -0.7%, below threshold, not corrected |
| 24 | SBC treatment | deduct method (IFRS 2 inside EBIT) | Correct. Never added back. | model | PASS | 0 |

**Result.** 24 items checked: 4 FAIL (#1 price, #9 discount rate, #18 semaglutide share, #23 lease cash), 1 UNVERIFIABLE (#7), 3 Quant UNKNOWNs resolved (#4, #8, #19). Only #9 moves fair value by more than 5%, so `03_rerun.py` re-runs the model with corrections A1-A3 (price, securities, rate).
- **Audit-corrected values: BEAR / BASE / BULL = DKK 139.8 / 305.5 / 480.5 = USD 20.93 / 45.74 / 71.95**, against the Quant's 23.44 / 52.01 / 82.97.
- Variants: pure DKK at the current rf (7.17%) gives BASE 335.0 (USD 50.16); pure USD (8.00%) gives 282.1 (USD 42.24).
- **Why the blend:** NVO's cash flows are not DKK cash flows. Holding the USD/DKK rate flat at spot while discounting at a DKK rate implicitly assumes the USD will not depreciate against DKK, despite a 2.2-point rate gap. Weighting by the US sales share is the minimum correction. Weighting by profit would push the rate closer to 8%: guidance puts the FX effect on EBIT at about twice the effect on sales.

## 3. Quality of earnings
**SBC.**
- FY25 SBC was 1,435 = **0.47% of revenue and 1.20% of OCF** (FY21-25 average 0.74% of revenue). Under IFRS 2 it is expensed inside EBIT, and the model never adds it back, so the fair value is already SBC-burdened.
- FCF FY25 (OCF - PP&E) was 58,962. Treating SBC as cash gives 57,527.
- Fair value, Quant BASE: **DKK 347.3 (USD 52.01)** with SBC as a cash cost, which is the model as built. Adding SBC back would raise it by about 1.5%.
- Fair value, Skeptic BASE: **DKK 254.4 (USD 38.09)** with SBC as a cash cost, against DKK 258.2 (USD 38.67) if SBC were added back as non-cash (`03_rerun.py` §4).
- SBC is immaterial here.

**Accruals.**
- OCF/NI was 1.23 / 1.15 / 1.42 / 1.30 / 1.20 / 1.16 for FY20-25. Cumulative FY21-25 OCF was 482,865 against NI of 390,387 (1.24x). On the surface, cash conversion is good.
- However, a US pharma's OCF includes growth in its **sales-deduction (rebate) provision**. That provision becomes a cash outflow when gross-to-net narrows.
- **H1-26 OCF is not representative**, per the Q2-26 6-K balance sheet:
  - The current sales-deduction provision rose from 133,349 to 140,201 *after* a 26,760 non-cash 340B reversal, so the underlying accrual build was **+33.6bn**.
  - Tax payables rose 8,416 to 20,460 (**+12.0bn**).
  - Partly offsetting: trade receivables -18.1bn, trade payables -5.2bn, inventories -1.7bn.
  - Net working-capital tailwind: about **+19.3bn**.
  - That is why H1 FCF (55.3bn) already exceeds the full-year guide (45-55bn), which implies **H2 FCF of -10 to 0bn**. The FY27 WAC cut converts part of the 140bn provision into a cash outflow (company: "expected to impact Novo Nordisk's cash flow in 2027"). See J2.
- **Receivables (Quant H7): +25.5% in H1-26 is a partly benign flag.** DSO was 105 / 104 / 102 / 90 / 84 days for FY21-25, and **109** at Jun-26 on annualised adjusted sales (93 on reported sales, which include the 340B reversal).
  - H1-26 is a reversion to the FY21-23 norm.
  - The flattering happened in FY24-25, when DSO compression added about 15bn to OCF ((102 - 84)/365 x 309bn).
  - The cause of the H1 build is UNKNOWN; possible drivers are wholesaler timing ahead of the WAC cut and the Medicare Bridge pilot from 1 Jul. Flag kept as moderate.
- **Inventory: a real red flag.** FY25 inventory grew +21.5% against sales +6.4%, and inventory days went 51 to 59. Write-downs rose to 4,272 (FY24: 2,660). Q2-26 adjusted GM carried about DKK 3bn of "right-sizing of manufacturing capacity agreements". This is consistent with capacity built for a volume-at-price path that did not happen.

**Adjusted vs GAAP.**
- Adjusted NP minus reported NP was 9,569 in FY24 (9.5% of NP) and **13,973 in FY25 (13.6%)**. The add-backs are rising.
- "Non-recurring" items recur. Impairments: FY23 1,414; FY24 10,562 (incl. ocedurenone 5.7bn); FY25 7,316; H1-26 6,328 (monlunabant 4.0bn); a probable Q3-26 ziltivekimab charge. Restructuring: about 8bn in FY25; about 3bn of one-offs in Q2-26; 13,000 job cuts announced at the CMD.
- Per this audit's rule, they count as costs. In a DCF the impairments are non-cash, but they are the visible trace of BD spending that failed. That is why the BD cash allowance must reflect actual BD intensity (J3), not the low-intangibles median.
- The 2026 adjusted-OP measure (ex-340B, ex-major impairment) keeps restructuring in. That is the stricter definition, and the one the Quant's base uses.
- **The trailing P/E of 9.3 is flattered** by the 26.8bn non-cash 340B reversal. The Quant's normalised 11.9x is the right read.

## 4. Capital allocation
**Grade: D.** Management is judged only as capital allocators. Rubric mapping:
- **A** needs ROIC well above WACC sustained *and* buybacks below value. NVO fails the second limb.
- **F triggers present:** buybacks at peak prices (2023-24) and rising leverage funding payouts (FY24-26 distributions > FCF while borrowings rose 5.3x).
- **Kept above F by:** ROIC still about 34% (well above a 7-8% WACC), leverage still modest (company net debt/EBITDA 0.64x, Aa3/AA), and M&A mostly core. **D blocks BUY**, which requires at least C.

**Share count.** Diluted shares went 4,680m (FY20, split-adjusted) to 4,447.7m (FY25), -5.0% or about -1.0% a year. Outstanding is 4,413.1m (Oct-26). SBC (1,435) is tiny next to buybacks (FY20-24 average 22,099 a year), so buybacks were not merely offsetting dilution.

**Buyback price discipline.** Proxy: the annual mean NOVO-B.CO close (yfinance, split-adjusted). Novo does not disclose the average price by year in the sources read; 2026 is the actual from the 6-K.

| Year | Spent (DKK m) | ~Avg price (DKK) | x today's DKK 253.88 | x Skeptic EV (DKK 258) |
|---|---|---|---|---|
| 2020 | 16,855 | 212 | 0.83 | 0.82 |
| 2021 | 19,447 | 281 | 1.11 | 1.09 |
| 2022 | 24,086 | 387 | 1.53 | 1.50 |
| 2023 | 29,924 | 584 | 2.30 | 2.27 |
| 2024 | 20,181 | 851 | 3.35 | 3.30 |
| 2025 | 1,388 | 434 | 1.71 | 1.68 |
| 2026 (to 9 Oct) | 10,559 | 278.97 (actual) | 1.10 | 1.08 |

- In total, about DKK 122.4bn bought about 327m shares (average about DKK 374). They are worth about 83.0bn today (**-32%**).
- 2023-24 alone: 50.1bn at about DKK 669, worth about 19.0bn today (**-62%**).
- The pattern is pro-cyclical: spending peaked near the price top (29.9bn in 2023) and was cut to 1.4bn in 2025 after the price halved.
- The 2026 programme (DKK 15bn, average 278.97) is roughly at my value, but it is **debt-funded**: 2026E distributions are 66.9bn against a guided FCF of 45-55bn.

**Buffett $1 test.** Sources: NOVO-B.CO closes (yfinance, split-adjusted) x XBRL diluted shares; the end of Window B uses the ADR close in DKK x 4,413.1m. Retained = NI - dividends, from facts and the H1-26 6-K.

| Window | Market cap start -> end (DKK bn) | Δ | Retained (NI - div) | Value per DKK retained |
|---|---|---|---|---|
| A: fiscal, Dec-20 -> Dec-25 | 998 -> 1,447 | +448 | 215.9 | **+2.08** (pass) |
| B: to date, Oct-21 -> Oct-26 | 1,483 -> 1,120 | -363 | 223.9 (FY22-25 + H1-26) | **-1.62** (fail) |

The result depends on the window because the stock rose 4x and then fell 75%. Window B is the decision-relevant one. Every DKK retained since late 2021 (plus 81.5bn of buybacks) sits against a lower market value today. I treat it as a **fail, with low precision**.

**Returns on reinvestment.**
- ROIC (EBIT x (1-ETR) / (equity + borrowings - cash)) went **70% (FY20) to 34% (FY25)**.
- Incremental ROIC FY20 to FY25 was 24.1% (ΔNOPAT 57,245 / ΔIC 237,086), but **FY24 to FY25 it was -2.5%**: IC rose 67.9bn while NOPAT fell 1.7bn.
- Invested capital rose 4.9x while NOPAT rose 2.3x. Much of that IC is pre-productive capacity, and some of it is now being right-sized.

**M&A.**
- **Emisphere (2020):** the SNAC oral platform underpinning Rybelsus and the Wegovy pill. A good deal (qualitative; deal size UNKNOWN by deal).
- **Dicerna (2021) and Forma (2022):** together part of the 18.3bn and 7.1bn business acquisitions. Returns UNKNOWN.
- **Inversago (2023):** monlunabant terminated, impaired DKK 4.0bn in Q2-26. A write-off.
- **Catalent sites (2024):** DKK 82.2bn. Their D&A pulled down FY25 gross margin (company), and capacity agreements are now being "right-sized". Bought at the cycle peak.
- **Akero (2025):** USD 4.7bn plus a USD 0.5bn CVR, for a Phase 3 MASH asset. Too early to judge.
- Goodwill is 3.7% of assets, because M&A sits in intangibles and PP&E. Little diworsification: everything is metabolic, manufacturing or rare disease. But Rare disease ran a Q2 operating loss of DKK 1,295m.

**Leverage funding payouts.** Borrowings went 26.6bn (FY21) to 140.1bn (Jun-26). Distributions against company FCF:
- FY24: 64.3bn against -14.7bn.
- FY25: 53.2bn against 28.3bn.
- 2026E: 66.9bn against 45-55bn.

The CMD keeps "an attractive dividend per share" as an ambition.

**Insider activity: UNKNOWN (no transaction data available).** Novo is a foreign private issuer, so there are no Form 4s, and the Danish MAR manager filings were not retrieved.

**Candour: mixed.**
- The Annual Report 2025 letter calls the semaglutide LOE "an opportunity, not a threat" (20-F). That is spin about a molecule that is 74% of sales.
- The CMD gave no numeric growth target, and 2027 guidance was deferred.
- In fairness, the 2026 guidance was set low and raised twice, and the restructuring was announced plainly.

## 5. Probabilities & expected value
**Anchor: the reverse DCF at the corrected price and rate.** All figures are from `03_rerun.py` §5.
- At USD 38.015 and 7.60%, with the Quant's BASE margins and capex, the price implies a constant 10-yr revenue CAGR of **-1.67%**. The Quant's figure was -2.88%, at 7.01% and USD 38.415.
- Including my J2/J3 costs, the implied CAGR is -1.14%.
- My BASE path is -1.16% a year: FY35 revenue 272,712 against 306,464.
- The price-implied IRR on my BASE cash flows is 7.61%, essentially equal to my discount rate. **The market is pricing my base case.**

**Base rate (outside view, stated before adjusting).** No sourced cross-company statistic was retrieved in this run, so this is a qualitative base rate.
- A large-cap pharma whose lead molecule is about 74% of sales and loses US and EU exclusivity inside the forecast decade usually shows revenue declines in the two to three years after LOE.
- Novo's own in-house analogue: liraglutide (Victoza) sales fell **-44.9% in 2025** (5,482 to 3,020, 20-F), after the US compound patent expired in 2023.
- Holding revenue at about -1% a year across the decade therefore needs an above-base-rate pipeline replacement. I put that at roughly even odds, which sets BASE at 50%.

**Inside-view adjustments.** The tails skew to the bear.
- Bear-side evidence: the 2026 pipeline readouts were net negative (ZEUS missed its primary endpoint; monlunabant terminated; CagriSema non-inferior to tirzepatide on weight, not superior). US injectable pricing is visibly breaking (US Wegovy injectable -22% at CER in Q2; 35-50% WAC cuts from 2027).
- Bull-side evidence: volume growth is real (IQVIA branded obesity volume +81%; International Operations obesity +37% at CER), the oral pill leads its category, guidance was raised twice in 2026, and Q2 adjusted EBIT grew 11% at CER.
- Result: BEAR 30%, BULL 20%.

| Scenario | Quant value (USD/ADR) | Audit-corrected A1-A3 | **Skeptic A1-A3 + J1-J3** | Probability |
|---|---|---|---|---|
| BEAR | 23.44 | 20.93 | **18.40** (DKK 122.9) | 30% |
| BASE | 52.01 | 45.74 | **38.09** (DKK 254.4) | 50% |
| BULL | 82.97 | 71.95 | **70.25** (DKK 469.2) | 20% |
| **EV** | 49.63 | 43.54 | **38.62** (DKK 257.9) | |
| MoS vs USD 38.015 | +23.4% | +12.7% | **+1.6%** | |
| Asymmetry | 0.80 | 0.32 | **0.03** | |

The Quant's column applies my probabilities to the Quant's own values, for comparison only; the Quant assigned none.
- **Expected value:** EV = 0.30 x 18.40 + 0.50 x 38.09 + 0.20 x 70.25 = **USD 38.62**.
- **Margin of safety:** 1 - 38.015 / 38.62 = **+1.6%**. At the verified final close of 38.06 it is +1.4%.
- **Asymmetry:** (38.62 - 38.015) / (38.015 - 18.40) = **0.03**. The upside to EV is negligible against a -52% path to the bear.
- **Sensitivity:**
  - Probabilities 40/45/15 give EV USD 35.04 (MoS -8.5%); 20/55/25 give 42.20 (+9.9%).
  - Rate: pure DKK (7.17%) gives EV 42.57 (+10.7%); pure USD (8.00%) gives 35.51 (-7.1%).
  - LOE depth (BASE, FY32-33 each year): +2.5% gives USD 46.48; -1% gives 43.82; -5% gives 40.90; -9% gives 38.09; -13% gives 35.41; -18% gives 32.21.
  - FX: USD values move one-for-one with DKKUSD (00_inputs 0.149734).

## 6. Bear thesis & downside catalysts
**Pre-mortem revisited: confirmed and sharpened.** The model did not change my structural view; the sourcing made it more specific.
- **Patents.** Semaglutide is 73.9% of FY25 sales. Its compound patents expire in **2031 (EU, Japan) and 2032 (US)**, inside the DCF window, and in China in 2026.
- **Price.** It is eroding *before* the patents go: the WAC cut from 1 Jan 2027, MFN, self-pay at USD 149-299, and LOE pricing in Canada and Brazil.
- **Margins and capital.** The erosion is already visible: gross margin went 84.7% (FY24) to 81.0% (FY25) to 78.2% adjusted (Q2-26), and incremental ROIC turned negative in FY25.
- **Capital misallocation (secondary).** Capacity was bought at the peak, and payouts are now debt-funded.

**Downside catalyst 1: the US net-price reset outruns volume after the 2027 WAC cut.**
- *Signposts:* FY2027 guidance (early Feb 2027), Q1-27 US Operations adjusted sales at CER, adjusted gross margin, and the FY27 FCF guide (the provision unwind).
- *Confirmation thresholds (any one):*
  - FY27 adjusted sales guide midpoint at or below **-5% CER**.
  - US Operations below **-10% CER** in any 2027 quarter.
  - Adjusted gross margin **below 76%** for two consecutive quarters.
  - FY27 FCF guide **below DKK 30bn**.
- At those levels the BEAR path (FY27 -10%, margin 37%) is the operative case.

**Downside catalyst 2: no successor before the 2031-32 cliff, or the cliff arrives early.**
- *Signposts:* the CagriSema US decision (Q4-26) and launch share; zenagamtide Phase 3; the Cipla Paragraph IV suit (D.N.J.); the Sandoz UPC revocation action (EP unitary patent, 18 countries).
- *Confirmation thresholds (any one):*
  - A CagriSema CRL.
  - Any ruling that invalidates or narrows the US or EP semaglutide patents ahead of 2031-32.
  - Semaglutide still **above 65% of sales in FY2029** (73.9% in FY25), meaning no diversification ahead of the cliff.

**The single variable that flips the thesis:** the **depth of the FY32-33 revenue loss at the US/EU semaglutide LOE, net of pipeline**. It is worth about DKK 4.6 per share per point of annual decline. Full offset (-1%/-1%) gives USD 43.82 (+15%). No offset (-18%/-18%) gives USD 32.21 (-15%). The discount-rate currency is second, at about ±USD 3.5.

## 7. Disagreements with the Quant
Kept, not averaged. Effects are on BASE, in DKK per share, run in `03_rerun.py` §2-3. Changes are cumulative in the order shown; single-change effects on the Quant's own BASE are in brackets.

| # | Issue | Quant view | Skeptic view | Evidence | Δ FV (BASE) |
|---|---|---|---|---|---|
| D1 | Discount rate (audit A3) | 7.01%: DKK floor on a 3.01% rf; DKK cash flows at a DKK rate | **7.60%**: DKK rf 3.17% (floor 7.17%), blended with the USD floor of 8.00% on the 51.3% US sales weight | 00_inputs (Aug-26 OECD average); Trading Economics 3.17% on 1 Sep 2026; Q2-26 6-K geographic split | 347.3 to 305.5 (**-12.1%**; USD 52.01 to 45.74) |
| D2 | LOE depth, FY32-33 (J1) | -1% / -1%: pipeline offsets about 95% of the loss | **-9% / -9%**: about half offset | 20-F: US 2032 and EU/JP 2031 expiry; semaglutide 73.9% of sales; US + EUCAN semaglutide 62.6%; Victoza -44.9% in 2025; 2026 pipeline setbacks | 305.5 to 266.8 (-38.6) [Quant BASE alone: -12.9%] |
| D3 | 2027 WAC-cut cash (J2) | FY27 cash gap of 2.76% of revenue (~7.9bn); unwind only as a stress test | **25% of the 140,201 provision paid out net in FY27**, *replacing* the gap (bear 50%, bull 10%) | Company: the WAC cut is "expected to impact Novo Nordisk's cash flow in 2027"; H1-26 underlying provision build of +33.6bn | -5.8 [-1.7%] |
| D4 | BD / bolt-on M&A allowance (J3) | 1.45% (median FY21-24 intangibles only) | **3.0%** | FY20-25 intangibles + acquisitions ex-Catalent = 7.25% of revenue (4.90% also ex-Akero); impairments every year 2023-26; the CEO "will not shy away from business development" (20-F letter) | -6.6 [-2.0%] |
| D5 | Price of record | USD 38.415 (intraday) | USD 38.015 (orchestrator); the true final close was 38.06 | yfinance daily history | MoS only |
| D6 | Capital allocation | not graded | **D**, which blocks BUY | §4 | verdict gate |
| D7 | FY26 margin anchor (not modelled) | 42.7%; the 47% alternative judged implausible | Agree that 47% is wrong (H4 resolved). The risk runs the **other** way: if FY25 impairments are not in the company's adjusted base, the FY26 guide-implied margin is about 40.4% | Q2-26 6-K reconciliation (H1-25 comparative strips 340B only) | 0 (FY26 calibrated); a downside flag for FY27+ margins |

**Net effect.** Skeptic BASE is **DKK 254.4 = USD 38.09**, 26.8% below the Quant's 52.01. The audit-only correction (D1) accounts for USD 6.27 of the gap; judgement (D2-D4) accounts for USD 7.65. Probability-weighted EV is USD 38.62 (Skeptic) against 49.63 (Quant values at my probabilities). **The gap exceeds 15% of fair value and is unresolved.**

**Agreements:**
- The Lynch reclassification (Fast Grower to Slow Grower) and the moat rating (NARROW, eroding).
- LOE timing (FY32-33, now sourced).
- FY26 calibration to the FCF guide.
- Leases in Borrowings (now confirmed).
- SBC treatment.
- The deeper bear margins (34-37%): Q2 adjusted GM is already below its 5-yr low.
- PEG void.
- The FY27 revenue of -3%.
- Terminal assumptions; TV share below 75%.

## 8. Verdict recommendation
**Rule trace** (`analyse` skill, Verdict rules; position held):
- **Required margin of safety.** Moat NARROW and eroding, so the required MoS is **30%**.
- **Price band.** EV is USD 38.62. EV x 0.70 = 27.03 < price 38.015 <= EV 38.62, which falls in the ACCUMULATE / HOLD band for a held position.
- **Why not ACCUMULATE.** The MoS is +1.6% against the 30% required, and capital allocation is D. That leaves **HOLD**.
- **Why not TRIM.** Price is not above EV x 1.3 (50.20). The bear thesis is *partly* visible (gross margin, US injectable pricing), but the data that defines the bear path is not yet in: FY27 net price after the WAC cut, and the FY27 guide in Feb 2027. Meanwhile 2026 guidance was raised twice and Q2 adjusted EBIT grew 11% at CER. If either catalyst in §6 hits its threshold, the verdict moves to **TRIM**.
- **Why not SELL.** Capital allocation is D, not F; there is no solvency risk (Aa3/AA, 0.64x net debt/EBITDA); the moat is eroding, not gone.
- **Circle of competence.** The Quant judged a 10-year forecast "NO". Per the rules this flags the position **for review at the FY27 guidance (early Feb 2027)** or on any semaglutide patent ruling.
- **Conviction.** It drops for an unresolved Quant/Skeptic disagreement above 15% of fair value, and again for more than 2 corrected load-bearing inputs (discount rate plus J1-J3), so **LOW**.

```
VERDICT:      HOLD
CONVICTION:   LOW
FAIR_VALUE:   USD 38.62 (probability-weighted EV; BASE USD 38.09; Quant BASE 52.01 shown alongside)
ENTRY_BELOW:  USD 27.03   (EV x 0.70)
EXIT_ABOVE:   USD 50.20   (EV x 1.30)
KEY_RISK:     US net-price reset from 1 Jan 2027 WAC cut, then semaglutide LOE (US 2032, EU/JP 2031) without a proven successor
```
**One line:** At USD 38 the market already prices my base case: a stable volume franchise whose price and patent cliff are only half offset by the pipeline. So there's no margin of safety to add on, no evidence yet to sell, and D-grade capital allocation rules out a BUY even on a dip until payouts are funded from FCF.

**Holder notes (SG resident):**
- **Danish dividend withholding.** The Denmark-Singapore DTA (2000, effective 1 Jan 2001) caps it at **10% of the gross amount** for a Singapore resident. Singapore MOF release of 21 Dec 2000: "The withholding tax in Denmark on Danish dividends derived by a Singapore resident remains at 10% of the gross amount". Clearstream's current Danish treaty table also lists 10%.
- **What is actually withheld.** The rate withheld at source on the NVO ADR via the depositary and IBKR is **UNKNOWN**. Anything above 10% has to be reclaimed from the Danish tax authority, which needs proof of Singapore residence.
- **Yield.** The gross yield is 4.6% (DKK 11.70 / 253.88), or about 4.1% net of 10%.
- **Not verified in this run:** the Singapore-side treatment of foreign dividends and the US estate-tax situs of a foreign-issuer ADR.
