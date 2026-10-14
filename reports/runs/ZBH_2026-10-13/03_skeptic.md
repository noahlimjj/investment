<!-- pipeline:value-skeptic -->
# Skeptic audit: ZBH (as of 2026-10-13)

Zimmer Biomet, NYSE, USD. Price **$92.17** (fundamentals.json; this is the **2026-10-12 close**, and yfinance shows ~$93.49 intraday on 10-13).
Template FULL. Status: current holding (SG-resident, SGD-base investor).
Corrected model: `reports/runs/ZBH_2026-10-13/03_rerun.py`. It is 02_model.py with one load-bearing input fixed (C1) and one history-only fix (C2). Formulas and scenario structure are unchanged.

**Headline: the Quant's capex leaves out "Additions to instruments", a separate line in ZBH's cash-flow statement worth $300.5M in FY25 and $322.9M TTM.**
With it included:
- TTM FCF is **$1,079M**, not $1,402M.
- Base fair value is **$71.58**, not $95.27 (−24.9%).
- The reverse DCF changes from "price = status quo" to **"price needs 6.15% growth or a 30.8% EBITDA margin, above the FY23 peak."**

## 1. Pre-mortem (written before reading the model)
I wrote this to scratch before opening 02_quant.md or 02_model.py. It is reproduced verbatim:

> Most likely structural reason ZBH is worth materially less in 5 years: **moat erosion in large-joint reconstruction.**
> Knees (40% of sales) grew +0.4% in Q2-26 while the market grows mid-single-digit. Stryker's Mako installed base locks in surgeons, so the robot is a switching cost that now favours the competitor.
> The result is organic growth stuck at 2–3% (2026 guide 2.25–3.25%), plus pricing pressure (GPO, China VBP, ASC shift) that erodes adjusted operating margin (−210bp y/y in Q2).
> Management responds by buying growth (Paragon 28, Monogram: $1.39B in 2025) on a balance sheet where GAAP ROIC is already ~5% (< WACC) and goodwill is ~43% of assets. It also does debt-funded buybacks (debt +$1.3B in FY25).
> Failure mode for the model: a DCF that assumes ~18% FCF margins and ~3% terminal growth forever on a business that is a share donor in its core category.
> Secondary: the GAAP/adjusted gap (adjusted EPS ~2x GAAP). If "one-off" restructuring and integration charges are perennial, owner earnings are overstated.

(Two of the pre-mortem figures were wrong and are corrected here. Market share is UNKNOWN: no share data is in the dossier, and the Mako point is a hypothesis, not a sourced fact. FY25 debt rose $1.31B, from $6,204.6M to $7,519.1M.)

## 2. Number audit
Every value was traced to a primary filing and recomputed in python3. Primary sources fetched this session:
- 10-K FY2025 (accn 0001193125-26-059853)
- 10-K FY2022 (0000950170-23-004264)
- 10-Q Q2-2026 (0001193125-26-335044)
- 8-Ks dated 2026-06-29 and 2026-09-08
- SEC companyfacts XBRL
- 82 Form 4s
- FRED DGS10

| # | Input | Quant value | Verified value | Source | Status | Δ FV (base) |
|---|---|---|---|---|---|---|
| 1 | Price | $92.17 | $92.17 = 10-12 close; 10-13 intraday ~$93.49 | yfinance history; fundamentals.json as_of 13:18 UTC (pre-open) | PASS (temporal note: label as 10-12 close) | 0 |
| 2 | Shares | 190.74M | 190,737,689 at 2026-07-30; Q2 weighted diluted 192.8M | 10-Q cover; 10-Q EPS note | PASS | 0 (diluted 192.8 gives −$0.8) |
| 3 | Net debt | 7,068.9 | 1,201.5 + 6,277.5 − 410.0 = 7,068.9. Debt fair value 7,470.7 ≈ book | 10-Q balance sheet; XBRL LongTermDebtFairValue | PASS. Leases ($233.0M, Dec-25) and contingent consideration (current balance UNKNOWN; Monogram $201.6M at acquisition) are excluded | leases −$1.22 (shown, not applied) |
| 4 | Base revenue (TTM) | 8,508.8 | 8,231.5 + 4,263.7 − 3,986.4 = 8,508.8 | 10-K; 10-Q | PASS | 0 |
| 5 | 10y UST in WACC | 5.20% | DGS10 5.22% (2026-10-08); 5.17–5.31% over the last 2 weeks | FRED | PASS | ~0 |
| 6 | WACC 8.5% (beta 1.0, ERP 5%, Kd 5.5%) | 8.5% | Arithmetic reproduces 8.50%. Vendor beta is 0.485, which would push WACC under the 8% floor | 02_model.py; yfinance beta | PASS (assumption; see §7) | at 8.0%: +$9.84 |
| 7 | **Capex % revenue** | **4.0%** (PP&E 220.3 + intangibles 121.0) | **7.81%**: other PP&E 220.3 + **instruments 322.9** + intangibles 121.2 = 664.4 | 10-K FY25 CF: instruments 300.5 / 240.3 / 311.7 (FY25/24/23). 10-Q: H1-26 162.6, H1-25 140.2 | **FAIL: source fidelity + accounting identity.** FCF ≠ OCF − all capex. The company's own FCF definition deducts instruments: Q2 FCF $308.3M = OCF 447.9 − 139.6 | **−$23.69 (−24.9%)** |
| 8 | TTM FCF | 1,402 | **1,079** (company-defined, excluding intangibles: 1,200) | same | **FAIL** (same root cause as #7). Vendor FCF of $1,072M was approximately right | in #7 |
| 9 | D&A 13.0%, fading to capex by year 10 | 13.0% | 13.03% TTM. FY25 split: depreciation 427.9 + intangible amortisation 665.9 (61%) | XBRL Depreciation and AmortizationOfIntangibleAssets; 10-K segment note | PASS. The fade is supported (resolves Quant H2). Endpoint moves to 7.81% with #7 | in #7 |
| 10 | GAAP EBITDA margin | 27.2% | (1,205.0 + 1,108.4)/8,508.8 = 27.19% | facts TTM; 10-Q | PASS | 0 |
| 11 | Tax rate | 18% | Adjusted rate 18% (8-K). TTM GAAP ETR 13.6% | dossier §3; facts | PASS (assumption) | 0 |
| 12 | Terminal ROIC | 10% | 5-yr ex-GW ROIC 9.7% recomputed | 02_model / facts | PASS (see §7, reinvestment note) | 0 |
| 13 | Growth path | 4.4% → 3.0% | FY26 reported guide 3.9–4.9% | 8-K ex99.1 (dossier) | PASS | 0 |
| 14 | WC % of Δrevenue | 48.5% | (2,286.4 + 1,704.4)/8,231.5 = 48.48% | facts | PASS | 0 |
| 15 | FY20/FY21 OCF (history) | 1,204.5 / 1,499.2 | Continuing ops: **1,075.6 / 1,404.3** | 10-K FY2022 CF | **FAIL: comparability.** facts.json mixes pre-ZimVie-spin OCF with continuing-ops revenue | 0 (history and averages only) |
| 16 | Revolver status | "$1.5B to 2030; 364-day renewal UNKNOWN" | New $1.5B 5-yr to **2031-06-26** plus new **$1.25B 364-day**. Covenant: debt/EBITDA ≤ 4.5x | 8-K 2026-06-29 | **FAIL: temporal** (stale) | 0 (lowers refinancing risk) |

**Result: 16 checked, 3 failed, 1 of them load-bearing (#7/#8). Base fair value changes by −24.9%, so the input was corrected and the model re-run.**
Model fidelity: TV share is 47–56% in all scenarios (below 75%). SBC is expensed once, through GAAP EBIT, and not double-counted. The equity bridge identity holds.

Corrected scenarios (`03_rerun.py`; capex keeps the Quant's period mapping, bear = FY24 / base = TTM / bull = FY25 totals):

| | Bear | Base | Bull |
|---|---|---|---|
| Capex % revenue (incl. instruments) | 7.78% | 7.81% | 7.01% |
| Year-1 FCF margin | 15.0% | 14.8% | 15.6% |
| **Per share (Skeptic, corrected)** | **$41.97** | **$71.58** | **$106.57** |
| Per share (Quant, 02_model) | $59.25 | $95.27 | $131.74 |
| TV share | 47% | 52% | 56% |

Calibration check: the corrected historical unlevered FCF margin for FY23/24/25 is 14.5% / 14.2% / 16.6% (average 15.1%). That matches the corrected year-1 base of 14.8%.
The Quant's 18.6% matched a history that left out instruments.

**Reverse DCF, corrected.** $92.17 implies one of the following:
- a **6.15%** 10-year revenue CAGR at base margins;
- a flat **30.8%** GAAP EBITDA margin at base growth (FY23 peak 30.2%; TTM 27.2%);
- a **7.55%** IRR on base cash flows, below the 8.5% WACC.

The tape is pricing recovery, not stasis.

## 3. Quality of earnings
- **SBC:** $98.2M TTM = **5.6% of OCF** and **1.15% of revenue** (FY25: 5.3% / 1.10%). Low and stable at $74–105M a year.
  - FCF: TTM **$1,079M** as reported; **$981M** with SBC treated as cash (yield 6.1% / 5.6% on $17,580M).
  - Fair value: **$71.58** with SBC expensed (the model's base, via GAAP EBIT); **$78.22** with SBC added back (non-cash view).
- **Owner earnings (corrected, NI + D&A − all capex):** FY25 $1,221.5M, TTM $1,251M (7.1% yield; 6.6% after SBC). The Quant had $1,522M / 9.0%.
- **Accruals:**
  - FY21–25 NI totals $3,265.9M against continuing OCF of $7,538.6M (2.3x).
  - This is not an accrual red flag. GAAP NI is depressed by $530–666M a year of non-cash acquired-intangible amortisation. But the $240–312M a year of instrument spend is real cash that the Quant's FCF ignored.
  - Working capital is not systematically flattering OCF. FY25 got +$200M from inventory (+98.2) and payables (+101.8), offset by receivables (−127.3) and taxes (−166.6). FY24 payables were −322.0, and H1-26 WC was a drag of about −$220M.
- **Receivables (amber flag):**
  - FY25 receivables grew +15.1% against sales +7.2%.
  - Excluding acquired Paragon 28 receivables ($42.0M, 10-Q PPA table), growth is **+12.3%**.
  - DSO went from 70.4 to 75.6 days. Q2-26 annualised is about 74 days.
  - FX translation probably explains part of this, but the size of that effect is UNKNOWN.
- **Adjusted vs GAAP:**
  - "Restructuring and other cost reduction initiatives" plus "Acquisition, integration, divestiture" were $173.6M / $242.6M / $258.1M in FY23/24/25. That is **2.3% / 3.2% / 3.1% of sales, every year, and rising.** They are recurring and count as costs.
  - The 2025 Restructuring Plan adds about $155M more to 2027.
  - Q2-26 adjusted NI of $399.6M is about 2x GAAP $198.3M.
  - The Quant valued off GAAP EBITDA (these charges expensed). I agree.

## 4. Capital allocation: grade **D**
**Share count.** Diluted shares went 207.0 (FY20) → 210.4 → 210.3 → 209.7 → 203.9 → 198.7 (FY25) → **192.8 (Q2-26 weighted)**, which is −8.3% since FY22.
- Treasury shares rose 104.8M (Dec-22) to 128.8M (Jun-26): **24.0M shares bought for $2,532M**.
- About 6.5M of those (27%) were absorbed by employee issuance. So buybacks did more than offset SBC.

**Buyback price discipline.** Average price paid = treasury cost ÷ change in treasury shares (XBRL TreasuryStockValueAcquired; 10-K/10-Q balance sheets):
- FY23–24: **$113.5**
- FY25: **$100.9** (Q4-25 $92.21 per the 10-K table)
- H1-26: **$90.1** (Q2 $84.60 per the 10-Q table)
- All-in average: **$105.5**

That is about 48% above my probability-weighted value of $71.18, and above today's $92.17, so the program is about −$320M marked to market.
Payouts now exceed FCF:
- FY25 corrected FCF was $1,119.7M against buybacks + dividends + M&A + CVR of $2,095.5M.
- H1-26 FCF was $452.9M against buybacks + dividends + contingent payments of $663.4M.
- Net debt went $5,679M (Dec-24) → $6,927M (Dec-25) → $7,069M (Jun-26).
- The FY26 plan ($1B buyback + ~$190M dividends) exceeds TTM FCF of $1,079M.

**Buffett $1 test (fails decisively):**

| Window | Start mcap | End mcap | Δ | Retained (NI − div) | Δ per $1 retained |
|---|---|---|---|---|---|
| FY20 → FY25 | $149.60 × 207.0M = $30,967M | $89.92 × 198.7M = $17,867M | −$13,100M | $2,277M | **−$5.75** (−$4.80 if $2,174M of buybacks added back) |
| 2021-10-13 → 2026-10-13 | $138.61 × 210.4M = $29,164M | $92.17 × 190.74M = $17,580M | −$11,583M | $2,419M | **−$4.79** |

Sources and adjustments:
- Prices are yfinance closes. yfinance applies a 1.03 factor on 2022-03-01 for the ZimVie spin, so the start values exclude ZimVie, which was distributed.
- Shares are 10-K diluted counts and the 10-Q cover.
- NI and dividends are from facts / 10-Q.
- Part of the drop is P/E de-rating, but no plausible adjustment closes a gap of $11–13B.

**M&A:**
- 2025: Paragon 28 total consideration $1,276.5M (cash 1,241.5 + contingent 35.0); Monogram $377.5M incl. $211.3M contingent (10-K / 10-Q PPA notes). Earlier: 2023 $134.9M, 2024 $276.3M.
- Goodwill + intangible impairments (XBRL GoodwillAndIntangibleAssetImpairment) total **$1,862M** for 2018–2022: 2018 $979.7M, 2019 $70.1M, 2020 $503.0M, 2021 $16.3M, 2022 $292.8M. Plus a $116.6M loss on the ZimVie stake (2022).
- Goodwill is **43.5% of assets**; goodwill + intangibles are 63.1%.
- Group ROIC including goodwill is 4.7–6.9% against an 8.5% WACC, so acquired capital has not earned its cost.
- Acquisition-specific ROIC for Paragon 28 / Monogram is UNKNOWN.
- Recent deals are adjacent (foot & ankle, robotics), so this is not Lynch diworsification. But at 2025's scale (~1 year of FCF) and with these returns, the deals are value-destructive.

**Insider transactions (Form 4, 82 filings 2025-10-13 → 2026-10-13, parsed from SEC XML):**
- **Zero open-market purchases (code P).**
- Five open-market sales (code S), 17,341 shares, ≈ **$1.58M** in total:
  - Yi 1,000 @ $96.49 and 5,000 @ ~$82.65
  - Winkler 2,650 @ $94.66
  - Phipps 3,000 @ $98.35
  - Thornal 5,691 @ $92.95, three days after the 8-K notice that his role was "restructured"
- All CEO and CFO dispositions are code F (tax withholding on vesting), which is not informative.
- Two senior field leaders left within 6 weeks: the APAC president (Aug) and the Group President Americas/Global Businesses (8-K 2026-09-08).
- Candour on calls: UNKNOWN (no transcript).

**Grade D.**
- Not C: ROIC is well below WACC, not about equal to it. Buybacks ran about 48% above value. Leverage is rising while payouts exceed FCF.
- Not F: buybacks did shrink the count by more than SBC. There have been no impairments since 2022. Recent M&A is bolt-on. Leverage is serviceable: 3.06x GAAP EBITDA against a 4.5x covenant, with a revolver renewed to 2031.

## 5. Probabilities & expected value
**Outside view first.**
- At base margins the price needs a **6.15% revenue CAGR for 10 years**.
- ZBH's own record:
  - 2016 → 2019 revenue CAGR **1.3%** (XBRL, pre-spin basis: 7,668.4 → 7,982.2).
  - FY21 → FY25 **4.8%**, including acquisitions (~2.5pt of FY25's 7.2%).
  - FY26 organic cc guide **2.25–3.25%**.
- I did not verify a published cross-sectional base-rate table, so I use ZBH's own decade as the reference class. No 4-year window since 2016 delivered ≥6% organic growth.
- **Base rate used: P(≥6% organic CAGR for 10 years) ≤ 10%.**
- The alternative route to $92 is a 30.8% margin, above any year in the record. That is also a minority outcome.

**Evidence adjustments.**
- Against the bull case: Q2 adjusted operating margin −210bp, GAAP gross margin 71.8% → 69.7% (FY23 → FY25), knees flat, senior field turnover, payouts above FCF.
- For the bull case: FY26 revenue guide raised twice, GAAP operating margin up y/y in Q2, FY23–24 EBITDA margins of ~30% achieved on essentially this portfolio.

| Scenario | Value (corrected) | Probability | p × value |
|---|---|---|---|
| Bear (2% growth, margin to FY22 low 23.4%) | $41.97 | 25% | $10.49 |
| Base (guide → 3%, 27.2% flat) | $71.58 | 55% | $39.37 |
| Bull (4.5% growth, margin back to 30%) | $106.57 | 20% | $21.31 |
| **Expected value** | | | **$71.18** |

- **Margin of safety** = 1 − 92.17 / 71.18 = **−29.5%** (price is above EV).
- **Asymmetry** = (71.18 − 92.17) / (92.17 − 41.97) = **−0.42**.
- Sensitivity of EV to weights:
  - 30/50/20 → $69.69
  - 20/55/25 → $74.41
- The same weights on the Quant's uncorrected values would give $93.56. That is the size of the capex error at the EV level.

## 6. Bear thesis & downside catalysts
The pre-mortem survives the model and is sharper now. **The price already assumes a return to FY23-peak margins (30.8% needed vs 27.2% TTM), while the reported trend is the other way.** Capital is meanwhile being returned above value and partly on borrowed money.

1. **Margin squeeze in recon (pricing, mix, China VBP, knee share).**
   - Signposts: TTM GAAP EBITDA margin, (operating income + D&A)/revenue, now 27.2%; adjusted operating margin; US knee growth.
   - **Confirms if:** TTM GAAP EBITDA margin < **25.5%** for two consecutive quarters (halfway to the bear 23.4%), or FY adjusted operating margin < 25%, or US knees < +2% y/y for 4 straight quarters.
   - Each 1pp of EBITDA margin ≈ **$5.75/share**.
2. **Leverage-funded capital return / another large deal.**
   - Signposts: net debt / TTM GAAP EBITDA (now 3.06x); payouts vs corrected FCF; deal size.
   - **Confirms if:** net debt / EBITDA > **3.5x**, or an acquisition > $1B, or a second consecutive year of buybacks + dividends > FCF (FY26 plan $1.19B vs TTM FCF $1.08B is already on track to breach).
   - A watch item: instrument capex intensity above 4% of sales (TTM 3.8%), e.g. if robotics/ROSA placements need more sets.

**Single variable that flips the thesis:** the sustainable **GAAP EBITDA margin**, with capex fixed at ~7.8% including instruments. At **≥30.8%** the stock is fairly priced. At 27.2% (today) it is worth ~$72.

## 7. Disagreements with the Quant
| # | Issue | Quant view | Skeptic view | Evidence | Effect on FV |
|---|---|---|---|---|---|
| 1 | Capex completeness (Quant H1/S1) | 4.0% of revenue; TTM FCF $1,402M. Flagged as open | **7.81%**: "Additions to instruments" is a separate investing line every year | 10-K FY25 / FY22 and 10-Q Q2-26 cash-flow statements. Company FCF definition deducts it | Base **$95.27 → $71.58 (−24.9%)**; bear −$17.28; bull −$25.17 |
| 2 | Cash-metric cheapness | FCF yield 8.0%, OE yield 9.0%, P/FCF 12.5x; "cheap on every cash metric" | FCF yield **6.1%**, OE yield **7.1%**, P/FCF **16.3x**. Still cheaper than the 23.7x peer median, but ZBH is the slowest grower | Follows from #1 | n/a |
| 3 | Reading of the reverse DCF | Price = 2.9% growth, i.e. "today's business forever"; IRR 8.65% ≈ WACC | Price = **6.15%** growth or **30.8%** margin; IRR **7.55% < WACC**. Market prices recovery | 03_rerun.py §F | Verdict-relevant |
| 4 | Debt / refinancing | $1.5B revolver to 2030; 364-day renewal UNKNOWN; "FCF covers 2027 notes" | Revolvers renewed to 2031 plus $1.25B 364-day, so refinancing risk is lower. But corrected FCF of $1,079M < FY26 buyback + dividend of $1.19B, so 2027 notes and payouts are partly debt-funded | 8-K 2026-06-29; §4 | 0 |
| 5 | Net-debt completeness | Leases / CVR UNKNOWN | Leases $233.0M (Dec-25 XBRL); contingent consideration balance UNKNOWN (Monogram $201.6M at acquisition; $69.2M paid in H1-26) | XBRL; 10-Q | −$1.22 (leases), not applied |
| 6 | History comparability | FY20/21 FCF margins 17.8% / 19.7% | Pre-spin OCF mixed with continuing revenue. Corrected FY20/21 FCF margins 11.2% / 14.0% | 10-K FY2022 | 0 (history only) |
| 7 | WACC | 8.5% (beta 1.0 assumed) | **Agree, keep 8.5%.** Vendor beta 0.485 would put WACC under the 8% floor, but an 8% WACC with a 5.2% risk-free rate on a 3x-levered business leaves too thin a premium. Recorded, not applied | yfinance beta; FRED | If 8.0%: +$9.84 |
| 8 | Terminal reinvestment | ROIC 10% → terminal reinvestment 30% of NOPAT (~4.8% of revenue) | Mostly agree. Today's true net reinvestment is ~3.7% of revenue (capex 7.8% − depreciation ~5.2%, + WC ~1.4%). Year-10 explicit reinvestment is only 1.4%, so the model has a mild discontinuity that is conservative | §2 #12 | ROIC 12%: +$4.04 |
| 9 | Lynch category / moat | Slow Grower; Narrow, eroding at operating level | Agree | — | 0 |
| 10 | GAAP vs adjusted | Value off GAAP; restructuring treated as recurring | Agree. Charges are 2.3–3.2% of sales every year, rising | §3 | 0 |

## 8. Verdict recommendation
Rules applied (analyse skill §Verdict rules):
- Narrow moat → required MoS 30%.
- EV = **$71.18**.
- EV × 1.3 = **$92.53**.
- EV × 0.7 = **$49.82**.

At the $92.17 print the price is $0.36 inside the HOLD band. At the 10-13 intraday ~$93.49 it is in the TRIM band.
The second TRIM trigger, "bear thesis already showing in the numbers", is **partly met**:
- adjusted operating margin −210bp y/y;
- GAAP gross margin −2.1pp since FY23;
- knees flat;
- payouts above corrected FCF with leverage rising.

The full bear margin (23.4%) has not arrived: the TTM EBITDA margin is still at its 5-year average.
Capital allocation is D (≥ C is required only for BUY; it is not F, so this is not SELL).

```
VERDICT:      TRIM
CONVICTION:   MEDIUM   (one corrected load-bearing input; TV 52%; primary financials. Dropped from HIGH
                        because the verdict sits within 0.4% of the HOLD/TRIM boundary and moves with the weights)
ENTRY_BELOW:  $49.82   (EV $71.18 × 0.70)
EXIT_ABOVE:   $92.53   (EV $71.18 × 1.3)
FAIR_VALUE:   $71.18   (probability-weighted; base $71.58)
```
**Reason:** with instrument capex included, ZBH is worth about $71. The price needs FY23-peak-plus margins that the trend is moving away from, and management is buying back stock at about 1.5x value with partly borrowed money.
If the orchestrator applies the band mechanically at $92.17, the result is **HOLD (LOW)** with the same ENTRY/EXIT levels.
SGD note: the position is USD exposure. Dividend yield is 1.0%, subject to 30% US withholding for an SG resident, so the drag is ~0.3%/yr and not decision-relevant. There is no capital-gains tax, so trimming has no tax cost.
