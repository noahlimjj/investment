<!-- pipeline:value-skeptic -->
# Skeptic audit: MC.PA (as of 2026-10-13)

LVMH, Euronext Paris, EUR. EUR millions unless stated. Price EUR 381.65 (facts; yfinance raw close 13 Oct 380.45, −0.3%). Status: **CURRENT HOLDING** (SG resident, SGD base). Template FULL. Quant category: Cyclical-at-trough on a former Stalwart.
Inputs audited: `facts.json`, `01_research.md`, `02_quant.md`, `02_model.py` (re-executed, reproduces 213 / 309 / 355 / 486). Skeptic script: `03_rerun.py`. It loads `02_model.py` unchanged through `runpy` and adds the variants below. No Quant number was overwritten.

Primary sources the Skeptic added (read 2026-10-13):
- [K1] LVMH H1-2026 release with condensed statements (S3)
- [K2] LVMH Financial Documents FY2025 (S1): Notes 11, 12, 15.2, segment note, ETR note
- [K3] LVMH Financial Documents FY2023 (S2): inventories FY21–23
- [K4] lvmh.com, "Record results for LVMH in 2019" (28 Jan 2020)
- [K5] ECB Data Portal: IRS FR/DE long-term rates, monthly; euro AAA 10y spot, daily
- [K6] AMF BDIF declarations 2026DD1092911 and 2026DD1116814
- [K7] yfinance MC.PA raw daily closes
- [K8] Mauboussin et al., *The Base Rate Book* (Credit Suisse, 2016), sales-growth table for sales > $50bn

## 1. Pre-mortem (written before reading the model)
Written at 21:36 SGT from `01_research.md` + `facts.json` only, and reproduced verbatim:

> Most likely structural reason LVMH is worth materially less in 5 years: **moat erosion visible in the margins of Fashion & Leather Goods** (74% of PRO). FLG PRO margin has fallen every year: 41.6% (FY21) → 40.6 → 39.9 → 37.1 → 35.0% (FY25) → 34.1% (H1-26), and FLG revenue fell −2.7%/−8.0% in FY24/FY25 with Q3-26 organic −5% even as W&J/SR grow. The 2021–23 margin peak was built on repeated price increases to an aspirational (heavily Chinese) clientele; management now says price is at "the sweet spot between desirability and perceived value", so the price lever is spent. If FLG settles at ~30–32% (operating deleverage on a fixed-cost network of ~6.3k stores, rising marketing), group PRO margin is ~19–20%, not a mean-reversion to 26%. A DCF that fades margins back toward 24–26% would capitalise a peak that was cyclical/price-driven, not structural. Secondary: China wealth effect plus the onshoring of Chinese spend means a smaller volume base for a decade. Not a debt wall (2026 maturities 7.9bn vs 13.5bn cash+AFS). Capital-allocation risk: family control (66% of votes) means minority holders cannot discipline M&A, and the 2023 buyback at ~EUR 837 average was at the peak.

The Quant independently raised the same concern as its top open question (H.1). §5 and §7 test it against primary pre-COVID data.

## 2. Number audit
Every derived figure was recomputed in python from `facts.json` and the primary PDFs ([K1]–[K3]). Δ FV is the effect on the Quant BASE of EUR 354.8.

| # | Input | Quant value | Verified value | Source | Status | Δ FV |
|---|---|---|---|---|---|---|
| 1 | Price | 381.65 | 380.45 (raw close 13 Oct) | [K7] | PASS (−0.3%, intraday vs close) | 0 |
| 2 | Shares | 495.811m issued | 495,811,080 issued, verified. Outstanding ≈ 492.97m (treasury carried at EUR 1,417m) | [K1] equity statement | PASS; using issued shares is conservative | +0.6% if outstanding used |
| 3 | Net financial debt | 8,245 | 8,245 | [K1] p.2 table | PASS | 0 |
| 4 | Minority puts / minorities (book) | 6,416 / 1,599 | 6,416 / 1,599. No double count: puts are a separate liability line | [K1] balance sheet | PASS | 0 |
| 5 | Non-operating assets | not credited | JV/associates 1,225 + non-current AFS 1,967 + DFS held-for-sale net 1,049 = 4,241 | [K1] | WARN: conservative, disclosed | +8.6/share (+2.4%) |
| 6 | Base revenue (TTM to 9M-26) | 79,865 | 80,807 + 57,148 − 58,090 = 79,865; Q3 tables tie | [K2], Q3 PDF (S4) | PASS | 0 |
| 7 | Risk-free (France 10y OAT) | 4.75% (secondary, 7 Oct) | ECB primary: FR monthly average Aug 4.00%, **Sep 4.44%**; FR−DE spread 0.97pt in Sep and widening late in the month; euro AAA 10y **3.50% on 12 Oct**. AFT TEC10 4.48% on 14 Sep (secondary). 4.75% on 7 Oct is consistent with the AAA level plus a ~1.2pt late-Sep spread. **FRED's 4.00% is the stale August average, so it fails on temporal grounds and is rejected.** | [K5] | PASS (±30bp band 4.45–5.00%) | 4.44%: +20 (+5.7%); 5.00%: −14 (−3.9%) |
| 8 | WACC | 9.50% | Recomputed 9.50% (Ke 9.75%, Kd 3.42% after tax, 96/4 weights). Beta 1.0 is the instruction (Yahoo beta 0.88 would give 8.92% → 394) | model | PASS | none applied |
| 9 | Steady-state PRO margin | 24.97% (5-yr average) | Arithmetic 24.97% ✓. **The anchor is disputed:** FY2018 21.4% and FY2019 21.4% [K4]; FY2019 segment margins on the FY2025 mix give 22.2% | facts, [K4] | Arithmetic PASS; anchor DISPUTED (§7 D1) | 23.5%: −21.9 (−6.2%) |
| 10 | Tax rate | 28.07% (5-yr average) | 26.2 / 26.7 / 26.2 / 28.5 / 32.8%. FY25 is inflated by the French "additional tax" for 2025 (661 paid) | [K2] ETR note | PASS | — |
| 11 | Capex / revenue | 6.26% | 6.257% | facts | PASS | — |
| 12 | D&A ex-ROU / revenue | 5.03% | 5.034%. Includes provision movements, absorbed by the gap calibration | facts | PASS | — |
| 13 | Lease adjustment | 0.48% | (2,974 + 553 − 3,143) / 80,807 = 0.475% | facts | PASS | — |
| 14 | Cash-conversion gap / lease interest location | 1.49%; Quant unsure whether lease interest is in OCF | **Lease interest paid sits inside OCF** (FY25 (545), H1-26 (252)). The calibration is correct and the Quant's −7 to −8/share contingency does not apply. FCF identity OCF − capex − lease principal = company FCF holds in all 5 years | [K1] cash-flow statement | PASS (closes Quant H.3) | 0 |
| 15 | SBC treatment | "SBC-burdened" | Partly re-credited. Reported OCF adds back non-cash bonus-share expense, and the gap is calibrated to reported FCF, so about 0.23% of revenue of SBC is credited back | [K1] "other adjustments and computed expenses" | FAIL, model fidelity (minor) | −2.8/share (−0.8%) |
| 16 | Discounting convention | end-of-year | Mid-year convention would give 372.8 | `valuation.py` | WARN: disclosed, pipeline-wide convention, conservative | +5.1% (not applied) |
| 17 | TV share | 53–58% | Recomputed | model | PASS (< 75%) | — |
| 18 | 12-m change / 52-w high / P/E 12m ago | −27.6% / 641.64 / 21.0x | Raw closes: 540.40 → 380.45 = **−29.6%**; 52-w closing high **652.10** (which explains the dossier conflict with Yahoo's 654.70); P/E 12m ago 540.40/25.12 = **21.5x**. The facts used dividend-adjusted closes | [K7] | FAIL, comparability (not load-bearing) | 0 |
| 19 | Inventory / receivables vs sales | UNKNOWN | Closed. See §3 | [K1][K2][K3] | Closed; red flag (moderate) | — |
| 20 | "One-off LV logistics disruption, >1pt" (Q3) | used in the cyclical reading | Not in the primary Q3 release; no 2026 coverage found | S4, web search | FAIL, source fidelity (UNVERIFIED) | qualitative |

**Result: 20 checked. 0 load-bearing errors above 5%. 3 minor failures (#15, #18, #20) and 3 disclosed conservative conventions (#2, #5, #16).** Netting the factual items (#2, #5, #15) gives about +2%, so no correction to fair value is applied and the Quant's scenario values stand. Two variants are each worth more than 5%: risk-free at the ECB September average (+5.7%) and mid-year discounting (+5.1%). Neither is an error. The first rests on a temporally older figure, and the second is a library convention. Both are shown as sensitivities and cut against a too-bearish reading.

## 3. Quality of earnings
**SBC.** FY25 SBC is 159, or 0.84% of OCF and 0.20% of revenue. TTM SBC is 187, or 1.00% of OCF and 0.23% of revenue. It is immaterial. Treating SBC as a cash cost (closing the calibration re-credit in #15) gives:

| | Bear | Trough | Base | Bull | EV (§5 weights) |
|---|---|---|---|---|---|
| Quant (as built) | 212.9 | 308.8 | 354.8 | 486.0 | **332.3** |
| SBC as cash | 210.5 | 306.0 | 352.0 | 482.9 | **329.5** |

SBC-adjusted TTM company FCF is 11,214, a yield of 5.93%.

**Accruals.**
- Over FY21–25, net income (pre-MI) was 67,581 and OCF was 92,679 (1.37x). After deducting lease principal, OCF is 78,768 (1.17x NI), so cash backs earnings.
- Working capital consumed cash in every period: FY23 −4,577, FY24 −1,925, FY25 −576, H1-25 −1,990, H1-26 −2,446. OCF is not flattered by WC.
- This confirms the Quant's hypothesis that the FY24 cash gap was an inventory build: inventories moved −1,114 and payables −664 that year [K2].

**Inventory: the Lynch check, now closed. Moderate red flag.**

| | FY21 | FY22 | FY23 | FY24 | FY25 | Jun-26 |
|---|---|---|---|---|---|---|
| Inventory | 16,549 | 20,319 | 22,952 | 23,669 | 22,659 | 24,184 |
| Inventory growth | — | +22.8% | **+13.0%** | **+3.1%** | −4.3% | **+4.7% YoY** |
| Revenue growth | — | +23.3% | +8.8% | −1.7% | −4.6% | −2.9% (H1) |
| Inventory / revenue | 25.8% | 25.7% | 26.6% | 28.0% | 28.0% | (seasonal; not comparable) |

- Inventory has grown faster than sales in FY23, FY24 and H1-26.
- FY25's reported −4.3% hides **gross additions of +1,315**, offset by FX translation (−1,306) and the DFS held-for-sale reclassification (−182 net). Underlying, the build continued while revenue fell [K2 Note 11].
- Impairment charges on inventory are large and steady: 986 / 834 / 803 a year, against a provision stock of 3,644, or 21% of gross finished goods. LVMH protects its brands by provisioning and destroying stock rather than discounting it, so stress shows up in provisions and gross margin rather than in price cuts. Gross margin is not yet showing it: H1-26 67.1% vs 66.8% in H1-25.
- By segment, the build is concentrated in **Wines & Spirits**: inventory/revenue went from 105% in FY21 to **158%** in FY25 (inventory +35%, revenue −10%), which reads as a cognac glut. Next is W&J: 44% → 52%.
- FLG went from 11% to 14%, flat since FY23. SR fell from 21% to 15%.
- **Receivables** were 4,728 / 4,730 / 4,332, and at Jun-26 3,941 (−7.4% YoY) against revenue −2.9%. No channel-stuffing signal.

**Adjusted vs GAAP.** PRO excludes "other operating income and expenses", mostly impairments of brands, goodwill and fixed assets:

| | FY21 | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|---|
| Other operating items | +4 | −54 | −242 | −664 | −656 |
| As % of PRO | 0.0% | −0.3% | −1.1% | −3.4% | −3.7% |

- The 5-year total is −1,612, or −1.6% of PRO, and the trend is rising. These are "recurring non-recurring" items and should count as costs.
- They are largely non-cash write-downs of acquired capital (DFS in 2025), so they are not double-counted in the FCF-based DCF. Their economic meaning is that past M&A earned less than its price.
- The DCF models no future M&A, so it implicitly assumes future deals are NPV-neutral. LVMH's record suggests that assumption is mildly generous. This is not quantified.

## 4. Capital allocation: grade **C+**
**Rubric position.** Group ROIC is 15.7% against a 9.5% WACC, which is well above (A-like). The *marginal* capital deployed since FY21, however, has earned below WACC so far, and buyback timing has been poor. There is no leverage-funded payout: NFD fell from 10,176 to 8,245 YoY, and the dividend is covered 1.59x by FCF. That combination is C+, not B and not F.

**Buffett's $1 test.** Inputs:
- Start market caps use [K7] raw closes × FY21 diluted weighted-average shares of 503.9m, a proxy for the share count at the start date.
- Retained earnings = NI pre-MI minus dividends including minorities: 35,042 for FY21–25, and 37,070 including H1-26.

| Window | MV start → end (EUR m) | ΔMV | Per EUR retained |
|---|---|---|---|
| 31 Dec 2020 → 31 Dec 2025 (fiscal) | 257,440 → 321,008 | +63,568 | **+1.81** (pass) |
| 13 Oct 2021 → 13 Oct 2026 (trailing 5 yrs) | 329,497 → 188,631 | −140,866 | **−3.80** (fail) |
| 31 Dec 2020 → 13 Oct 2026 | 257,440 → 188,631 | −68,809 | **−1.86** (fail) |

The test is dominated by the luxury multiple cycle: FY21 EPS 23.89 against an end-2021 price of 727 is ~30x, against 17.4x today. The same retained capital passes or fails depending on the endpoint. The economic version is clearer:
- **Incremental ROIC FY21→FY25 = −724 NOPAT on +17,290 of added invested capital = −4.2%.**
- That capital went into the FY22–23 capex boom (7.5bn in FY23 alone, 8.7% of revenue, including flagship real estate) and into Tiffany integration. It has produced no incremental profit yet. This is cycle-distorted, but it is not evidence of discipline.

**Buybacks vs value.**

| Tranche | Average price | Context |
|---|---|---|
| 2023 programme | ~EUR 837 | 2023 average close 788, range 661–902: bought near the top |
| 2025 purchases | ~EUR 528 | |
| H1-26 (1,659 spent) | ~EUR 510 (proxy: H1 average close) | |

- Every tranche was bought **above today's price, above the Skeptic EV (332) and above the Quant's bull value (486)**.
- Net share count fell 0.40% a year (503.9m to 494.96m diluted), so buybacks did more than offset SBC (~0.3m shares a year). Size is modest at 7.24bn cumulative over FY21 to H1-26.
- Verdict on buybacks: a capital return made at prices that, on current evidence, exceeded intrinsic value. Not disciplined.

**M&A.**
- 2021 cash for consolidated investments was 13,226 (the Tiffany year; the purchase price itself is UNKNOWN in this run).
- **W&J (Tiffany era) FY25 NOPAT of 1,089 on segment assets ex-ROU of 29,890 is ~3.6%**, gross of payables and well below WACC. W&J PRO margin fell from 18.7% (FY21) to 14.4% (FY25). For contrast, FLG earns 31.1% on the same basis.
- DFS was sold in Jan 2026 at an estimated loss of ~0.5bn after impairments, and Marc Jacobs was sold on 1 Sep 2026. Goodwill fell from 24,022 (FY23) to 18,315 (FY25).
- Goodwill + brands are 41,892, or **29.5% of total assets** (Jun-26).
- Lynch diworsification: Selective Retailing is 23% of revenue but 10% of PRO. The 2026 pruning (DFS, Marc Jacobs) is a belated correction.

**Insiders (actual declarations).**
- Verified at the primary source [K6]: **Financière Agache** (Arnault-linked) bought **96,773 shares at EUR 547.60 on 30 Jan 2026** (~EUR 53m), and director **Ariane Gorin** bought **500 at EUR 480.09 on 23 Apr 2026**.
- Further March 2026 family purchases (20,288 at 492.89 and 20,197 at 495.11) are secondary only (abcbourse).
- Insider sales are UNKNOWN.
- Caveat: the family purchases also served to cross 50% of capital (AMF threshold filing, early Mar 2026), so they signal control as much as valuation.

**Candour.** The primary releases disclose the DFS impairment and loss factually. The H1 release concedes "very close attention to margins". In the documents read, there is no explicit admission that Tiffany or the 2022–23 capex wave underperformed. Call Q&A is UNKNOWN (no primary transcript).

## 5. Probabilities & expected value
**Outside view first.**
- *Growth.* Base rate from [K8] for companies with sales > $50bn (inflation-adjusted 10-yr CAGR, 1950–2015): mean 0.8%, median 1.1%; 37.8% grew 0–5% real and 21.1% grew more than 5% real.
  - The price implies a 4.81% nominal CAGR (≈2.8% real at 2% inflation) **with** margins back to 25%. Base rate of achieving it: **~38%**.
  - At trough margins, the implied 6.5% nominal is achieved **~25%** of the time.
  - The Quant BASE path (3.94% nominal, ~1.9% real) sits at about the 56th percentile, so it is achievable 44% of the time.
- *Margin.* The 25% "mid-cycle" margin was reached only in the FY21–23 boom. Both pre-boom years were 21.4% [K4], and FY19 segment margins on today's mix give 22.2%.
- Combined: the outside view says the Quant BASE (growth at the 56th percentile **and** a return to boom-average margins) is no better than a coin flip, and margin recovery is the weaker leg.
- *Evidence adjustments.*
  - Upward: 9M organic +2%, gross margin stabilising, NFD falling, insiders buying.
  - Downward: Q3 FLG −5%, inventory outgrowing sales, Asia ex-Japan −5% (secondary).

| Scenario | Value (Quant, verified) | Probability | p × v |
|---|---|---|---|
| Bear (revenue −1%/−3%, margin to 20.5% then 22%) | 212.9 | 20% | 42.6 |
| Trough (21.9% margin flat, base growth) | 308.8 | 30% | 92.7 |
| Base (margin to 25.0% by yr 5) | 354.8 | 35% | 124.2 |
| Bull (26.5% margin, 6–7% growth) | 486.0 | 15% | 72.9 |
| **Expected value** | | | **EUR 332.3** |

- The probability-weighted steady-state margin is **23.7%**, which matches the Skeptic's independent mid-cycle view (§7 D1). The margin disagreement is therefore expressed through the weights, not by also cutting BASE, which would double-count. With BASE recut at 23.5% and the same weights, EV would be 324.6.
- **SBC-adjusted EV: EUR 329.5.**
- **Margin of safety = 1 − 381.65 / 332.3 = −14.8%** (price above EV).
- **Asymmetry = (332.3 − 381.65) / (381.65 − 212.9) = −0.29.** Downside to the bear is −44% against "upside" to EV of −13%; upside to the bull is +27%.

Weight sensitivity:

| Weights (bear/trough/base/bull) | EV | EV × 1.3 |
|---|---|---|
| Quant-friendly 10/25/45/20 | 355.4 | 462 |
| Harsh 30/30/30/10 | 311.6 | 405 |
| Skeptic 20/30/35/15, OAT at ECB Sep avg 4.44% | ≈351 | — |
| Skeptic 20/30/35/15, AAA Rf with OAT floor | ≈381 | — |

The price sits between EV and EV × 1.3 under every weighting above. That is why the verdict below is robust.

## 6. Bear thesis & downside catalysts
**Pre-mortem revisited.** The primary data strengthens it, with one correction. FLG margin at 34–35% is *still above* its FY2019 level of 33.0%, and group TTM margin of 21.9% is *above* FY2019's 21.4%. Today is therefore not an obvious trough; it looks like a return to pre-boom normal. The bear case is not "margins collapse". It is "**margins don't come back, and the price needs them to**": the price needs 26.8% on the base growth path. The second leg is the inventory build (W&S 158% of revenue), which carries provision and discount risk.

**Bear thesis (one line):** the 2021–23 margins were a price-hike boom, not mid-cycle. FLG keeps de-leveraging toward its pre-COVID 33% while China stays soft, so value converges on the trough case (~309) or below, not the 355 base.

| # | Downside catalyst | Observable signpost | Confirming threshold |
|---|---|---|---|
| 1 | Structural FLG margin compression | FLG PRO margin in FY2026 results (late Jan 2027, date UNKNOWN) and H1-27 | **FLG margin < 33.0%** (below FY2019) **and** FLG organic growth ≤ 0 for FY2026; group PRO margin ≤ 21.0% |
| 2 | China/Asia demand reset forcing inventory clearance | Asia ex-Japan organic (Q3-26 −5%, secondary); inventories in FY2026 accounts; gross margin; W&S margin | Asia ex-Japan negative for **3 consecutive quarters** (Q3-26, Q4-26, Q1-27); **Dec-26 inventory > 23,669** (FY24 peak) with FY26 revenue down; **gross margin < 66.0%**; W&S PRO margin < 15% (FY25 19.0%, H1-26 22.4%) |

**The single variable that flips the thesis: the steady-state group PRO margin (driven by FLG).** Each 1pt is worth ≈ EUR 15/share. At 26.8% the price is fair; at 22% value is ~310 [Quant grid]. A return of FLG margin above 37% (FY24 level) on positive FLG growth would flip the Skeptic toward the Quant base/bull.

## 7. Disagreements with the Quant
These are kept and not averaged. The Quant's numbers are left as published.

| # | Issue | Quant view | Skeptic view | Evidence | Effect on FV |
|---|---|---|---|---|---|
| D1 | Mid-cycle PRO margin | 5-yr average 25.0% is mid-cycle (flagged as the most uncertain input) | It is a boom average. Mid-cycle is ≈ 23.5%, between FY19 segment margins on today's mix (22.2%) and the 7-verified-year average (23.9%, which omits COVID FY20 and so is biased up) | FY18 21.4%, FY19 21.4%, FY19 FLG 33.0% [K4] | BASE 355 → 333 (−6.2%); at 22.2% → 313 (−11.6%). Expressed through probabilities, not double-counted |
| D2 | Cyclical reading: "one-off LV logistics hit >1pt" | Cited as partial explanation of Q3 FLG −5% | Unverified; not in the primary Q3 release. Give it no weight | S4 text; search | Qualitative; supports trough/bear weight |
| D3 | SBC | Fully burdened | Re-credited through the gap calibration (~0.23% of revenue) | [K1] OCF add-backs | −2.8/share (−0.8%) |
| D4 | Non-operating assets | Not credited (disclosed) | Credit 4,241 (associates, AFS, DFS held-for-sale net) | [K1] | +8.6/share (+2.4%) |
| D5 | Risk-free | 4.75% (secondary) | Agree on level (ECB Sep avg 4.44%, spread widening into Oct). FRED 4.00% rejected as stale. If anything, the OAT embeds ~1.2pt of French sovereign spread on a business that is 92% non-French; an AAA-based Rf with the OAT floor gives 406 | [K5] | None applied; sensitivity +20 / +51 |
| D6 | Inventory / WC | UNKNOWN; FY24 gap "consistent with inventory build" | Confirmed: inventory outgrowing sales FY23, FY24, H1-26; W&S 158% of revenue | [K1][K2][K3] | Qualitative; raises bear weight |
| D7 | Lease interest location (Quant H.3) | Unverified; possible −7 to −8/share | Inside OCF, so the Quant's calibration is right | [K1] | 0 (resolves in the Quant's favour) |
| D8 | Price-history figures | −27.6%, 52-w high 641.64, P/E 12m ago 21.0x | −29.6%, 652.10, 21.5x (raw closes; facts used dividend-adjusted closes) | [K7] | 0 |
| D9 | Consensus FY27 +4.6% in BASE year 2 (Quant H.10) | Labelled growth estimate | Acceptable under RULE 2 (it is a revenue estimate, not a target or rating); BASE growth sits at the ~56th percentile of the base rate | [K8] | 0 |

None of these is worth more than 15% of fair value. D1 is the largest, at −6% to −12% on BASE.

## 8. Verdict recommendation
- **Required MoS: 40%.** The Quant's category is Cyclical. Earnings are not predictable even though the brand moat is Wide but eroding. At 30% MoS, ENTRY_BELOW would be 233.
- **Position: EV 332 < price 381.65 ≤ EV × 1.3 = 432.** For a held position that is **HOLD**.
- **TRIM check: is the bear thesis already showing?** Not yet confirmed. 9M organic growth is +2%, H1 gross margin rose, and the FLG margin (34.1%) is still above its FY19 level of 33.0%. Early signals are present (Q3 FLG −5%, the inventory build), so the §6 thresholds are the TRIM triggers.
- **Capital allocation C+** (≥ C), so a BUY would be permissible only below 199.
- **Conviction:** no automatic downgrades apply. There are 0 corrected load-bearing inputs, TV share is 55%, no disagreement exceeds 15%, and the financials are primary (only the OAT and the call commentary are secondary). The verdict holds across all weightings tested. MEDIUM rather than HIGH because predictability is only partial.

Capital Allocation Grade: C+

```
VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          EUR 381.65
FAIR_VALUE:     EUR 332.3 (probability-weighted EV; SBC-adjusted 329.5; Quant BASE 354.8 shown alongside)
UPSIDE:         -12.9%
ENTRY_BELOW:    EUR 199 (EV x 0.60; Cyclical 40% MoS)
EXIT_ABOVE:     EUR 432 (EV x 1.3)
CONVICTION:     MEDIUM
KEY_RISK:       2021-23 margins were a boom, not mid-cycle; price needs 26.8% PRO margin vs 21.9% TTM and 21.4% pre-COVID
DATA_WARNINGS:  1
```
TRIM triggers: FY26 FLG margin < 33% with FLG organic <= 0; or Dec-26 inventory > 23,669 with revenue down and gross margin < 66%.
**Reason:** the price already discounts a return to roughly boom-era margins (26.8% on the base path) that only happened in 2021–23. That leaves no margin of safety, though the price is not far enough above value to force a trim while the margin-erosion thesis is unconfirmed.

Investor-fit notes for the orchestrator: EUR/SGD translation is not modelled, and 79% of revenue is invoiced outside EUR. French dividend WHT of 12.8% for an SG individual is secondary-sourced (dossier §10.12).

Sources (web): [ECB Data Portal](https://data-api.ecb.europa.eu/), [FRED IRLTLT01FRM156N](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IRLTLT01FRM156N), [TradingEconomics FR OAT news](https://fr.tradingeconomics.com/france/government-bond-yield/news/590139), [abcbourse on French debt](https://www.abcbourse.com/analyses/chronique-dette_francaise_pourquoi_les_marches_commencent_a_sinquieter-1618), [LVMH 2019 results](https://www.lvmh.com/en/publications/record-results-for-lvmh-in-2019), [AMF 2026DD1092911](https://bdif.amf-france.org/back/api/v1/documents/2026/2026DD1092911/FFA65D63B6E8288B02C60E8073DA4A10CBFCB44B9728271567094BE5E9284A12.pdf), [AMF 2026DD1116814](https://bdif.amf-france.org/back/api/v1/documents/2026/2026DD1116814/F0E118A90AD6CAB4A70BAADD26C5F36CC33C20D17F2133315D1E81F597EBAFD1.pdf), [abcbourse insider list](https://www.abcbourse.com/marches/transactions_dirigeants/FR0000121014p), [The Base Rate Book (third-party host)](https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf), LVMH PDFs S1/S2/S3/S4 as listed in `01_research.md`.
