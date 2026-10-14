<!-- pipeline:value-skeptic -->
# Skeptic audit: SYK (as of 2026-10-13)

## 1. Pre-mortem (written before reading the model)
Written from `01_research.md` + `facts.json` only, before opening `02_quant.md` / `02_model.py`.

**Most likely structural reason SYK is worth materially less in 5 years: capital misallocation in an acquire-to-grow model, priced at a quality premium that assumes the organic core keeps compounding at ~10%.**
- Stryker spent $14,102M on acquisitions FY20-25, equal to 76.4% of the period's FCF ($18,470M, OCF − PP&E capex). Goodwill went from $12.8B to $19.3B (40.3% of total assets at FY25). Interest expense nearly doubled ($315M → $607M) and there have been no buybacks since 2019. The growth "engine" is cash out the door for premium-priced assets, not internal reinvestment.
- The largest deal (Inari, $4.81B net, Feb 2025) now sits in the segment with a manufacturing and backorder problem: Q2'26 Vascular −0.7% reported, US Vascular −6.7% (primary 8-K). The Sept-8 −8.8% day says the market is already testing this.
- Crude FY25 ROIC on total invested capital, including goodwill, is ~10-12% (NOPAT at a 16-28% tax rate over ~$34.7B IC). That is only ~2-3 points above an 8-9% WACC with a 10y UST at 5.22%. The organic franchises (Mako/knees, Instruments, Endoscopy, Medical) almost certainly earn far more. The bought growth is what drags the group return toward WACC.
- Failure path: organic growth slips from ~10% to mid-single digits (Q1'26 was 2.4%, cyber-hit; peripheral vascular is backordered) while acquired assets under-earn. Then the market stops paying ~17x adjusted forward earnings, and both the "E" and the multiple fall. Two things amplify it: (a) adjusted EPS is ~38% above GAAP (FY25 $13.63 vs $8.40), so the "cheap" 17x forward P/E depends on add-backs (intangible amortisation, impairments in 5 of 5 years, recall and restructuring costs) that recur; (b) the GAAP tax rate stepped from 12-14% to 28.1% in FY25 (27.6% TTM). If that rate is structural (Pillar Two or IP relocation), owner earnings reset ~15% lower.
- Secondary candidates, noted but ranked lower: terminal-rate risk (a 5.22% risk-free compresses any premium multiple) and the CEO transition 2026-12-31 (it changes the capital allocator just after the largest deal in company history has stumbled).

## 2. Number audit
**Result: 15 inputs checked, 2 failed (both corrected in `03_rerun.py`, exit 0). Base FV unchanged at $209.13. Bear $131.41 → $148.08 (+12.7%). Probability-weighted EV +$4.17 (+2.0%, below the 5% re-run threshold; re-run done anyway because the bear moved more than 5%).** Identity checks pass, and SBC is counted once.

Primary-source spot-checks (5):
1. 10-K FY25 MD&A, tax note and XBRL rate reconciliation (accn 0000310764-26-000010)
2. 10-K FY25 cash-flow statement (same accn)
3. 10-Q Q2-26 XBRL balance sheet (accn 0000310764-26-000050)
4. The final 2026-10-13 close (yfinance raw bar, re-pulled 23:09 UTC after the 20:00 UTC close)
5. Ronda E. Stryker's Form 4 filed 2026-08-20 (accn 0001242914-26-000010)

All EDGAR requests used the generic contact UA.

| # | Input | Quant value | Verified value | Source | Status | Δ FV |
|---|---|---|---|---|---|---|
| 1 | Price | $283.71 "close" | **$282.55** final close. The $283.71 was an intraday pull (dossier written 02:44 SGT = 18:44 UTC, before the 20:00 UTC close) | yfinance raw bar 2026-10-13 (vol 2.07M) | **FAIL: Temporal.** Corrected (C1) | FV 0 (WACC still rounds to 8.9%); MoS −0.4pt |
| 2 | Shares | 383.573M basic (mcap), 386.0M diluted (per share) | 383,573,046 | 10-Q XBRL dei:EntityCommonStockSharesOutstanding | PASS | 0 |
| 3 | Net debt | $11,466M = 14,942 − 3,391 − 85 | 14,942 / 3,391 / 85 (current debt 750 + noncurrent 14,192) | 10-Q XBRL DebtLongtermAndShorttermCombinedAmount, cash, AFS securities | PASS. Note: debt fair value is **$14,024M** (−$918M vs book) | +1.1% if FV used (not applied) |
| 4 | Equity bridge | $12,218.5M (adds AVS 271, product liability 144, Q2 dividend 337.5) | Arithmetic OK. **Omitted:** German FCTO assessments for 2010-17 of $754M (+$11M expected). Company will appeal and seek foreign tax credits; the related UTB is "unchanged from 2024" (amount not split out) | 10-K FY25 critical accounting estimates / Note 11 | Minor omission (not a fail): not in dossier | −0.9% at full $765M (not applied) |
| 5 | Base revenue (TTM) | $25,837M | 25,116 + 12,609 − 11,888 = 25,837 (H1 +6.06%) | facts ttm, dossier §3 | PASS | 0 |
| 6 | WACC | 8.9% (raw 8.86%) | rf 5.22%, ERP 5.0%, β 0.781 → Blume 0.853, Ke 9.49%, Kd 5.22%, E/D 87.9/12.1 → 8.862% | 00_inputs, fundamentals.json | PASS. Kd = rf is a floor; +100bp → 8.96% | 0 |
| 7 | EBITDA margin (ex-imp, CF D&A) | 23.81% (FY21-25 mean) | 22.43 / 22.27 / 24.16 / 25.30 / 24.89 → 23.81% | facts + 10-K CF stmt (dep 461, amort 732 verified) | PASS (arithmetic). Judgment disagreement in §7 | (+5.4% at FY23-25 mean; not applied) |
| 8 | Growth path | 8.8% → 3.5% (10-yr CAGR 6.1%) | Guide midpoint (8.3+9.3)/2 = 8.8%, verbatim (dossier §3) | 8-K Ex 99.1 | PASS. Note: year 1 sits on a cyber-depressed TTM base; the guide implies H2-26 organic ≈ 11.5% | (+2.7%; not applied) |
| 9 | Terminal ROIC | 12.9% | EBITA ex-imp at pooled tax: 11.77 / 11.14 / 13.21 / 14.34 / 14.00 → 12.89% | facts + Item 6 equity | PASS | 0 |
| 10a | Tax, base | 17.3% (FY21-25 pooled GAAP) | 17.35% | facts | PASS. Evidence range 16.3–21.4% (§7) | −2.4% at 19.1% (not applied) |
| 10b | **Tax, bear** | **27.6%** ("TTM GAAP ETR persists"; cause unsourced) | **21.4%.** The TTM rate includes a one-off. 10-K FY25 MD&A: "The effective income tax rate for 2025 increased from 2024 due to the 2025 tax effect of **transfers of intellectual property between tax jurisdictions**". Rate reconciliation "disposition of assets" +$405M (+9.0pt). It was non-cash: deferred tax +$392M (FY24 −$370M), current tax $876M vs $869M. Q4-25 alone: tax $856M on pretax $1,705M. **H1-26 ETR 16.3%** (Q1 12.4%, Q2 18.4%; 10-Q). Bear now uses the highest evidenced recurring rate: FY25 cash taxes paid $1,002M / pretax ex-impairment $4,684M = 21.4%; bear terminal ROIC recomputed (9.8% → 10.6%) | 10-K XBRL IncomeTaxReconciliationDispositionOfAssets, DeferredIncomeTaxExpenseBenefit, IncomeTaxesPaidNet; 10-Q EffectiveIncomeTaxRateContinuingOperations | **FAIL: Temporal / source fidelity** (a one-off period used as the persistent rate). Corrected (C2) | **Bear +12.7%** ($131.41 → $148.08); EV +2.0% |
| 11 | Terminal growth | 3.5% | Assumption, within the 4% cap | policy | PASS | 0 |
| 12 | D&A % revenue | 4.75% | (461 + 732) / 25,116 = 4.750% | 10-K CF statement | PASS | 0 |
| 13 | Capex % revenue | 3.09% | FY21-25 mean 3.086% | facts | PASS | 0 |
| 14 | acq_amort_pct | 2.91% | 732 / 25,116 = 2.914%. 10-Q schedule: next-12-month amortisation $715M, then $634M / $617M / $599M, i.e. slowly declining, consistent with no fade | 10-Q XBRL FiniteLivedIntangibleAssetsAmortizationExpense* | PASS | 0 |
| 15 | WC intensity w | 19.4% (calibrated plug) | Reproduced. The FY24 (−370) and FY25 (+392) deferred-tax swings inside the calibration roughly offset | 02_model output | PASS | 0 |

**Accounting identities:**
- FCF = OCF − capex: FY25 5,044 − 761 = 4,283 ✓; TTM 5,525 − 823 = 4,702 ✓.
- EV = mcap + net debt: 108,824 + 11,466 = 120,290 ✓ (at the corrected price: 108,379 + 11,466 = 119,845).
- Owner earnings FY25 = 3,246 + 1,193 − 761 = 3,678 ✓ (= fundamentals.json).

**Model fidelity:**
- SBC is expensed inside EBITDA and the share count is held flat. It is counted once ✓.
- TV share is 51–61% ✓ (below 75%).
- **Library issue (not a Quant error, not corrected, below the 5% threshold).** `valuation.dcf()` discounts explicit flows at t−0.5 when `mid_year=True`, but discounts the terminal value at n. That understates TV by (1.089^0.5 − 1) = 4.4%: bear +2.7%, base +2.8%, bull +2.9%. Flag to the orchestrator to fix `methodologies/valuation.py`.

**Corrected scenario values (03_rerun.py):** Bear **$148.08** · Base **$209.13** · Bull **$304.40** (TV 52 / 56 / 61%). The reverse DCF at $282.55 implies a **10.15%** 10-yr revenue CAGR at base margins (9.51% at FY23-25 margins; 7.34% at bull margins). The base-case IRR at the price is **7.56%**, against rf 5.22% and WACC 8.9%.

## 3. Quality of earnings
**SBC: modest and stable, but not offset by buybacks.**
- SBC was 4.3–6.4% of OCF FY20-25 (FY25 4.8%, TTM 4.5%) and 0.91–1.01% of revenue (TTM 0.97%).
- FCF FY25 $4,283M → **SBC-adjusted $4,040M**. TTM $4,702M → **$4,451M**.
- Diluted shares rose 380.3M → 386.5M FY20-25 (+0.32%/yr) with zero buybacks, so the dilution is real.
- The Quant's DCF already treats SBC as a cash cost: it is expensed in EBITDA and shares are held flat. That makes the scenario values SBC-adjusted.

| Basis | Bear | Base | Bull | EV (25/50/25) |
|---|---|---|---|---|
| **SBC as cash (primary, corrected)** | $148.08 | $209.13 | $304.40 | **$217.69** |
| SBC as non-cash (reference only: adds back 0.97% of revenue) | $157.01 | $220.28 | $317.87 | $228.86 |

**Accruals: clean on the headline test, but one OCF line deserves attention.**
- OCF/NI was 1.64 / 1.11 / 1.17 / 1.42 / 1.55 for FY21-25. Cumulative OCF was $18,884M against NI of $13,756M (1.37x).
- The Sloan accrual ratio was negative every year (−0.7% to −4.0% of average assets). Cash earnings exceed accounting earnings. The gap comes mostly from non-cash amortisation ($623–732M), impairments, the inventory step-up ($173M FY25) and FY25's non-cash $392M deferred tax charge.
- **Working capital:**
  - Inventory grew faster than sales in FY22 (+12.7pp) and FY23 (+10.1pp). That unwound in FY24.
  - FY25 OCF was **flattered by receivables**: AR was a +$127M inflow on +11.2% sales, and DSO fell from 64 to 59 days.
  - The H1-26 AR fall (−7.3%) is largely seasonal (Q4 is the peak quarter), so TTM cash conversion (18.9% unlevered SBC-adjusted margin) overstates run-rate. I agree with the Quant's choice not to anchor on TTM.
- **"Other, net" in OCF is the biggest earnings-quality unknown.** It moved from +$2M (FY20) to −$47M, −$107M, −$134M, −$306M and **−$470M (FY25)**.
  - The FY25 10-K cash-flow statement has **no separate add-back for loaner-instrument amortisation**: only depreciation 461 and intangible amortisation 732. So the ~$377M of inferred loaner amortisation (segment D&A minus CF D&A) must sit inside "Other, net". That is an inference, consistent with the dossier.
  - If so, other operating outflows, most plausibly loaner-set additions, were about −$847M in FY25, up from −$262M in FY20. That is well above amortisation and growing faster than revenue.
  - The Quant's calibrated w absorbs the historical average, so this is **not a model error**. It is a risk that instrument intensity keeps rising with Mako and implant placements. Each $100M/yr above the calibrated level costs about 1.2% of FV (Quant §E).

**Adjusted vs GAAP: the add-back share is large and rising.**

| | Adj EPS | GAAP EPS | Add-back $/sh | % of adj EPS | ~$M after tax |
|---|---|---|---|---|---|
| FY23 | 10.60 | 8.25 | 2.35 | 22.2% | ~902 |
| FY24 | 12.19 | 7.76 | 4.43 | 36.3% | ~1,708 |
| FY25 | 13.63 | 8.40 | 5.23 | 38.4% | ~2,021 |

- **Components visible in primary docs:**
  - Intangible amortisation, $635M / $623M / $732M pre-tax.
  - Goodwill and other impairments, in **every** year: $264M / $270M / $36M / $977M / $170M (FY21-25). These are recurring "non-recurring" items, i.e. the running cost of an acquisition model.
  - Inventory step-up, $173M (FY25).
  - The FY25 IP-transfer tax charge, $405M. This one is genuinely one-off and non-cash.
- Restructuring, recall, MDR and integration add-backs: UNKNOWN (no reconciliation in the dossier).
- **The DCF is not exposed to this.** It runs on GAAP operating income plus impairments plus D&A, so restructuring, recall, integration and step-up costs stay in as costs. But the market's ~18.9x forward P/E is on adjusted EPS, and that multiple does lean on the add-backs.

**Tax (resolves Quant open question #1).**
- The 28.1% FY25 / 27.6% TTM GAAP rate is a **one-off, non-cash IP-transfer charge** (+$405M, +9.0pt; see §2 row 10b).
- FY23's rate was pushed the other way by an earlier IP transfer, and FY24's by the spine sale. **IP transfers make the GAAP rate noisy in both directions.**
- **Evidence for the recurring rate:**
  - H1-26 GAAP ETR: 16.3%.
  - FY25 ETR excluding the one-off: 19.1%.
  - Current-tax / pretax ex-impairment: 19.3% / 19.4% / 18.7% (FY23-25).
  - Cash taxes paid / pretax ex-impairment: 18.7% / 22.1% / 21.4% (FY23-25). Some of this may be final TCJA transition-tax instalments (UNKNOWN).
- That range is 16.3–21.4%. The base 17.3% is at the low end of the evidence; ~18–19% would be central (−1% to −2.4% FV).
- The Quant's "27.6% persists → $179.79 (−14%)" case is **not supported** by the filings.

## 4. Capital allocation
**Grade: C (upper end).**
- **Why above C:** the organic franchise earns well above its cost of capital, and dividends are disciplined.
- **Why not B:** the capital management actually deploys (76% of FCF into M&A) earns only ~1–2pt above an 8.9% WACC at group level. The two largest recent M&A outcomes are a ~$1B spine write-down and exit, and a backordered Inari. And the next buyback programme is set to run at prices above our value.

**Share count and buyback discipline**
- **Diluted shares (XBRL, 10-K):** 382.8M (2014) → 379.9M (2019) → 380.3M (2020) → 386.5M (2025). That is +0.09%/yr over 11 years and **+0.32%/yr since 2020**.
- **Buybacks:**
  - 2014-19 total $1,650M: $100M, $700M, $13M, $230M, $300M and $307M.
  - Yearly mean closes 2015-19 were $93 / $111 / $140 / $167 / $198 (yfinance). Those are far below today's EV of ~$218–230, so in hindsight they were bought below value. But they were small, and they roughly **offset SBC** (shares −0.8% over 2014-19).
  - None since 2020. $1,033M of authorisation remains.
- **Forward test (signpost).** The Q2 call says buybacks resume in Q3-26 ([SNIPPET], unverified). At $275–300 that is **1.26–1.38x the corrected EV ($217.69)**, which would be value-destroying on these numbers. Check the Q3 10-Q repurchase table.

**Buffett $1 test (both windows shown; the window is the whole answer)**

| Window | Start mcap | End mcap | Δ mcap | Retained (NI − dividends) | $ per $1 retained |
|---|---|---|---|---|---|
| A: FY-end 2020 → 2025 | $93,189M (245.04 x 380.3M) | $135,843M (351.47 x 386.5M) | $42,654M | $8,113M (NI 13,756 − div 5,643, FY21-25) | **5.26** |
| B: as-of 2021-10-13 → 2026-10-13 | $98,060M (256.50 x 382.3M) | $109,064M (282.55 x 386.0M) | $11,004M | $9,041M (NI 14,883 − div 5,842, Jul-21 to Jun-26; H1 figures from XBRL 10-Qs) | **1.22** (1.14 on basic end shares) |

- Sources: yfinance raw closes; diluted shares from facts.json; NI and dividends from SEC XBRL.
- Both windows are above 1. But the as-of window is only just above 1, even though it was helped by ~$1.9B of net new debt (debt rose from $13,991M to $15,859M) that went into M&A.
- Window A ends near a peak multiple. Window B is the honest read today: each retained dollar has bought about $1.2 of market value.

**M&A (main capital-allocation lever)**
- **Scale:** acquisitions FY14-25 totalled **$23,587M** (XBRL PaymentsToAcquireBusinessesNetOfCashAcquired). FY20-25 was $14,102M, or 76.4% of FCF.
- **Goodwill:** $19,584M = **40.9% of total assets** at 6/30/26 (10-Q).
- **Impairments:** goodwill & other impairments FY21-25 were $1,717M, or 17.4% of FY21-25 acquisition spend. The XBRL goodwill-only impairments were $216M (2022) and $456M (2024).
- **Documented failure: Spinal Implants.** It took $977M of FY24 impairments and was then sold for $165M.
- **Largest deal: Inari ($4.81B net, Feb-25).** In Q2-26 Vascular was −0.7% reported (US −6.7%) on a manufacturing and backorder issue (primary 8-K). Continuation into Q3 is [SNIPPET] only. Inari's gross revenue and acquired returns are UNKNOWN.
- **Returns:**
  - Group ROIC including goodwill: 10.1% (FY21-25 mean), 11.3% TTM, against WACC 8.9% (+1.2 to +2.4pt).
  - Ex-goodwill ROIC: 21.9%.
  - Acquisition returns are bounded between ≤2.9% first-year pre-tax and ≤19.4% incremental (Quant §A). Neither bound is tight.
- **Diworsification:** no. The deals are hospital-medtech adjacencies (I agree with the Quant).
- **Leverage:** rising but moderate. Net debt / EBITDA is 1.83x. Interest expense went from $315M to $607M (cash interest $582M in FY25).
- **Dividends:** DPS CAGR 7.1% over 2021-25, ~30% of FCF. Disciplined.

**Insider transactions (Form 4s, dossier §6 plus my check of the 2026-08-20 filing)**
- **Ronda E. Stryker (director, founding family):**
  - Sold 1.68M shares (~$581M at ~$332–344) in four quarterly tranches. She also gifted 655,800 shares in Feb-26.
  - **The 2026-08-20 Form 4 has the Rule 10b5-1 box unchecked (`aff10b5One` = 0),** so these were **discretionary sales, not a pre-set plan.**
  - Holdings after the sale: ~14.47M shares across a revocable trust (2.25M), the L. Lee Stryker Trust (12.18M), the Johnston trust (37.6K) and direct (762). That is ~$4.1B at $282.55. Over 12 months she sold ~10% of her position.
  - **Read:** family diversification on a regular quarterly cadence is the most likely explanation, and she remains heavily aligned. But the sales were discretionary, at prices 17–22% above today and above our EV x 1.3. Her price discipline beat the company's planned buybacks. This is a **weak negative, not thesis-changing.**
- **Executives:** small sales only (CLO, CHRO, CAO, CFO). There were **zero open-market purchases** by any executive through a −22% year and the 2026-09-08 −8.8% day. The Brainerd 131-share "P" entry is immaterial.

**Candour**
- The Q1 cyber incident was disclosed promptly, with "material impact" language (8-K, then 8-K/A Item 1.05). That is candid.
- The vascular manufacturing issue appeared in release text and conference remarks, with no 8-K. Law-firm "investigations" exist ([SNIPPET]).
- Without call transcripts, management's candour about M&A misses (spine, Inari) is UNKNOWN.
- The CEO handover (Lobo → Stiles, 2027-01-01) changes the capital allocator just as the largest deal in company history is stumbling.

## 5. Probabilities & expected value
**Outside view first.**
- **Source:** Mauboussin, Callahan & Majd, *The Base Rate Book* (Credit Suisse, 26 Sep 2016), Exhibit 4. It covers the top 1,000 global companies, 1950-2015, with sales growth **inflation-adjusted** to 2015 dollars and unadjusted for M&A.
- SYK's $25.8B of TTM sales falls in the $12–25B decile or the bottom of the >$25B decile in 2015 dollars, depending on the deflator. Both are shown.

| 10-yr real sales CAGR | $12–25B decile | >$25B decile |
|---|---|---|
| ≥10% | **9.7%** | 7.3% |
| ≥5% | **30.5%** | 27.5% |
| <0% | 27.9% | 35.5%* |
| Median | 2.7% | 1.8% |

\*Sum of the six negative rows: 0.1 + 0.2 + 0.8 + 2.5 + 9.0 + 22.9.

- **Anchor: the reverse DCF.** The price needs a **10.15% nominal** 10-yr CAGR at base margins (9.51% at FY23-25 margins). In real terms that falls in the 5–10% bucket for any inflation between 0.15% and 5.15%. So the outside-view probability of meeting it is **between ~10% and ~30%**.
- **Inside view, for:** FY21-25 organic growth of 9.7–12.6% (mean 10.9%), the FY26 organic guide of 8.3–9.3% held through a cyber incident, Q2-26 organic 9.0%, Q2 adjusted operating margin +170bp, and an ex-impairment EBITDA margin trend of +61bp/yr.
- **Inside view, against:**
  - Part of that "organic" growth was bought: acquired fast-growers roll into organic after 12 months.
  - The largest acquisition is backordered.
  - A CEO change.
  - Net debt is up, which limits the next round of bought growth.

**Assignment and reasoning**
- **Bull (8.0% nominal CAGR plus margin expansion to 27.4%): 25%.** The ≥5%-real bucket (~30%) is the ceiling, before also requiring margin expansion. SYK's record keeps it near that ceiling rather than below.
- **Bear (4.7% CAGR, margin to the FY22 low, 21.4% tax): 25%.** The bear's growth alone is close to the size-class median, so growth by itself is not unlikely. But the bear also needs margins to fall to the 5-yr low against a rising trend.
- **Base: 50%.** The base's 6.1% nominal is already above the size-class real median.

| Scenario | Quant value | Corrected value (03_rerun.py) | p | p x value |
|---|---|---|---|---|
| Bear | $131.41 | **$148.08** | 25% | $37.02 |
| Base | $209.13 | **$209.13** | 50% | $104.57 |
| Bull | $304.40 | **$304.40** | 25% | $76.10 |
| **EV** | $213.52 (Quant values at my p) | **$217.69** | | |

- **Price:** $282.55 (final 2026-10-13 close; the Quant used $283.71).
- **Expected value:** **$217.69**. SBC is already treated as cash. Treating SBC as non-cash would give $228.86 (reference only).
- **Margin of safety:** 1 − 282.55 / 217.69 = **−29.8%**. Price / EV = **1.298**.
- **Asymmetry:** (217.69 − 282.55) / (282.55 − 148.08) = **−0.48**. EV is below price, so there is no upside to EV; the downside to the bear is −47.6%.
- **IRR at the price:** 7.56% on base cash flows and 9.26% on bull cash flows, against rf 5.22% and WACC 8.9%.

**Sensitivity of the verdict line (EV x 1.3 = $282.99 vs price $282.55).**
- With p(base) fixed at 50%, the break-even p(bear) is **25.2%**. Above that, price > EV x 1.3.

| p(bear / base / bull) | EV | EV x 1.3 | Rule outcome (held) |
|---|---|---|---|
| 25 / 50 / 25 (mine) | $217.69 | $282.99 | HOLD by $0.44 |
| 30 / 50 / 20 | $209.87 | $272.83 | TRIM |
| 30 / 45 / 25 | $214.63 | $279.02 | TRIM |
| 20 / 55 / 25 | $220.74 | $286.96 | HOLD |
| 20 / 50 / 30 | $225.50 | $293.15 | HOLD |
| Skeptic-judgment set, 25/50/25 (TV mid-year fix on all three + FY23-25 base margin; §7) | $229.57 | $298.44 | HOLD (MoS −23.1%) |
| Quant's uncorrected values, 25/50/25 | $213.52 | $277.57 | TRIM |

## 6. Bear thesis & downside catalysts
**The pre-mortem, revisited after seeing the model.**
- **Confirmed: the core failure path.** The price discounts ~10% revenue growth for a decade (reverse DCF 10.15%). That is SYK's own blended organic-plus-M&A record. Only ~10–30% of companies this size achieve it (§5). The shareholder's return on capital actually deployed is only ~1–2pt above WACC.
  - If organic growth fades to mid-single digits while acquired assets (Inari) under-earn, the stock re-rates toward the bear ($148, −48%). It falls on both earnings and multiple.
- **Refuted: the tax amplifier.** The FY25 / TTM 27.6% rate was a one-off, non-cash IP-transfer charge. H1-26 is 16.3%.
- **Neutralised in the DCF, live in the market multiple: the GAAP/adjusted gap.** The model runs on GAAP-cost EBITDA, but the 18.9x forward P/E is on adjusted EPS, with 38% add-backs.
- **New, from the audit:** the instrument-set cash drain hidden in "Other, net" (−$470M FY25 and widening), and a German tax assessment ($765M) not in any bridge.

**Bear thesis (one line):** an acquire-to-grow medtech priced for a decade of ~10% growth. Its bought growth earns barely above WACC and its biggest deal is stumbling; an organic fade plus M&A under-earning takes it toward ~$150.

**Top 2 structural downside catalysts**

| # | Catalyst | Observable signpost | Confirming threshold |
|---|---|---|---|
| 1 | **Organic growth fade** (the base-rate pull: size, M&A-fed "organic" rolling off, a CEO transition) | Quarterly organic growth (8-K Ex 99.1); FY27 guidance (late Jan 2027) | Q3-26 organic below ~9% puts the FY guide at risk (the guide implies ~11.5% organic in H2-26). **Confirmed** if FY26 organic comes in below 8.3% (bottom of guide), or FY27 organic guidance is below 7%, or two consecutive 2027 quarters run below 7% |
| 2 | **Acquired-asset under-earning / capital misallocation** (Inari and vascular; the new CEO's first moves) | Vascular sales line each quarter; goodwill impairment notes; Q3/Q4 10-Q repurchase table; any >$3B deal announcement | **Confirmed** by any of: Vascular reported growth negative in both Q3 and Q4-26; any Vascular / Inari impairment; buybacks executed above ~$283 (EV x 1.3); or M&A plus buybacks pushing net debt / EBITDA above ~2.5x (now 1.83x) |

**The single variable that flips the thesis: how long ~9–10% organic growth lasts.**
- At base margins, the price needs ~10% for 10 years.
- The Quant's grid shows that 5 years at 8.8% before the fade gives only $227.82.
- If SYK sustains 9–10% organic growth through 2030 without buying it, the bull ($304) becomes the central case and the stock is fairly priced.
- If growth fades to ~6% by 2028, the base ($209) is generous.
- WACC is the second-largest lever: rf x 0.9 → base $234.

## 7. Disagreements with the Quant
Kept side by side, not averaged. "Applied" means the item is in the corrected values (`03_rerun.py`). Everything else is shown with its effect only.

| # | Issue | Quant view | Skeptic view | Evidence | Effect on FV | Status |
|---|---|---|---|---|---|---|
| 1 | Bear tax rate | 27.6% (TTM GAAP persists; cause unsourced) | 21.4% (FY25 cash taxes / pretax ex-impairment). The 27.6% contains a one-off, non-cash IP-transfer charge | 10-K FY25 MD&A quote; XBRL rate reconciliation +$405M / +9.0pt; deferred +$392M; H1-26 ETR 16.3% (10-Q) | Bear +12.7% ($131.41 → $148.08); EV +$4.17 | **Applied (C2)** |
| 2 | Price | $283.71 "close" | $282.55 final close | yfinance bar after 20:00 UTC | FV 0; MoS −0.4pt | **Applied (C1)** |
| 3 | Base EBITDA margin | 23.8% (FY21-25 mean) | ~24.8% (FY23-25 mean) is the better central case. FY21-22 carried COVID and supply-chain inflation (GM −1.3pt in 2022, fully recovered); the trend is +61bp/yr; Q2-26 adjusted op margin was +170bp. I concede shocks recur (tariffs), so my true central sits between the two | facts margins; 8-K Q2-26 | Base +5.4% ($220.33) at 24.8%; about +2.7% at the midpoint | Unresolved (judgment) |
| 4 | Terminal-value discounting (library `dcf()`) | TV discounted at n with mid-year explicit flows | Inconsistent. A mid-year-consistent TV is x(1+WACC)^0.5. This is a tool fix, not the Quant's error | `valuation.py` lines 75-79 | Bear +2.7%, base +2.8%, bull +2.9% (EV ≈ +$6) | Unresolved; flag to orchestrator to fix the tool |
| 5 | Year-1 growth base | 8.8% on a TTM that includes the cyber-hit Q1-26 | FY guide midpoint 8.8% with H1 at 5.8% implies H2-26 organic ≈ 11.5% (arithmetic). Year 1 is likely understated *if* the guide holds. Q3 results decide | dossier §3 verbatim guide | +2.7% if the guide is met | Unresolved until Q3-26 print |
| 6 | Base tax rate | 17.3% pooled | Evidence range 16.3–21.4%; central ~18–19% (current-tax rate FY23-25 18.7–19.4%; FY25 ex-one-off 19.1%) | 10-K / 10-Q XBRL | −1% to −2.4% (−5.6% at 21.4%) | Unresolved (minor) |
| 7 | Equity bridge | 12,218.5 (net debt at book + AVS + product liability + Q2 dividend) | Add the German FCTO assessment (up to $765M, partly reserved) and the Q3-26 dividend ($337.5M); debt at fair value ($14,024M) is the textbook basis | 10-K FY25; 10-Q XBRL DebtInstrumentFairValue | −0.9% / −0.4% / +1.1%; net ≈ −0.2% | Unresolved (immaterial) |
| 8 | Moat → required MoS | WIDE (organic), stable | Agree WIDE at the franchise level (ex-goodwill ROIC 19–25%, gross margin within 1.3pt). But the verdict's 20% MoS needs a "Wide moat **with predictable earnings**". The Quant's own predictability call is PARTLY: GAAP margin, tax and capital deployment are not predictable, and group ROIC is only WACC +1–2pt. So use **30%** | Quant §B; §3–4 above | ENTRY_BELOW $152.38 (30%) vs $174.15 (20%) | Unresolved (verdict parameter) |
| 9 | Loaner-instrument spend | Loaner amortisation (~$377M) kept in opex as the spend proxy; spend UNKNOWN; −1.2% per $100M/yr | The 10-K CF statement has no loaner add-back, so the amortisation sits inside "Other, net" (−$470M FY25). Implied other operating outflows ≈ −$847M FY25 (−$262M FY20): spend likely runs well above amortisation. The calibrated w absorbs the historical average, so there is no FV change; the risk is rising intensity | 10-K FY25 CF statement | 0 now; −1.2% per extra $100M/yr | Agree on treatment; flag as the top earnings-quality unknown |
| 10 | Tax open question ("−14% if 27.6% persists") | Biggest single judgment | Resolved: it does not persist (one-off). The −14% case is not supported | as #1 | Removes a −14% tail from the base | Resolved by evidence |

**Net effect of the unresolved items:**
- The judgment items (#3–#7) range from about **−4% to +12%** on the base. Adding the one-at-a-time effects, they net to roughly **+8% to +10%** if all apply, or **+6% to +7%** excluding the Q3-contingent #5.
- The Skeptic-judgment set (#3 + #4 only) gives EV **$229.57**, vs **$217.69** corrected.
- No single unresolved disagreement exceeds 15% of FV.

**Agreements (no manufactured dissent):**
- WACC build.
- SBC treatment (once, as cash).
- CF-basis D&A and the decision not to add back loaner amortisation.
- acq_amort_pct with no fade (the 10-Q amortisation schedule supports it).
- Leases excluded under US GAAP.
- Terminal ROIC at the group (not ex-goodwill) level, given 76% of FCF goes to M&A.
- Not diworsification.
- The reverse-DCF framing.

## 8. Verdict recommendation
**Rule application (held position).**
- Corrected EV is $217.69 and price is $282.55, so price / EV = 1.298.
- That sits inside the HOLD band (EV < price ≤ EV x 1.3 = $282.99), by $0.44.
- Is the bear thesis already in the numbers? Only in the acquired Vascular segment (Q2 −0.7%, US −6.7%). It is not in group organic growth (Q2 9.0%, FY guide narrowed upward). So the "bear thesis showing" TRIM trigger is **not yet** met.
- Capital allocation is C, not F, and there is no solvency issue, so SELL does not apply.

```
VERDICT:      HOLD
CONVICTION:   LOW
ENTRY_BELOW:  $152.38   (EV $217.69 x (1 − 30%); 30% MoS: wide franchise moat but earnings only partly predictable; §7 #8)
EXIT_ABOVE:   $282.99   (EV x 1.3), i.e. essentially at today's price
FAIR_VALUE:   $217.69   (probability-weighted, SBC as cash; Skeptic-judgment range up to $229.57)
UPSIDE:       −23.0%    (217.69 / 282.55 − 1)
```
**Reason (one line):** after correcting the bear tax rate (a one-off IP-transfer charge, not a new normal), the price is 1.30x EV. That is exactly on the HOLD/TRIM line, so hold but do not add, and trim into any strength above ~$283.

**Why LOW conviction:**
- None of the four mechanical drop triggers fires: 2 corrected inputs (not more than 2), TV 52–61%, no single disagreement above 15%, primary SEC financials.
- But the verdict sits on the boundary:
  - p(bear) above 25.2% flips it to TRIM.
  - The Quant's uncorrected values flip it to TRIM ($213.52 EV).
  - My judgment items (§7 #3–#5) move it further into HOLD ($229.57).
- A Quant-vs-Skeptic split this close is a coin-flip, and the conviction label should say so.

**What would change it (for the orchestrator):**
- **To TRIM:**
  - Q3-26 (late Oct; date UNKNOWN) organic growth below ~9%, or Vascular still negative, or an FY guide cut.
  - Buybacks executed above ~$283.
  - Any Inari impairment.
- **Toward ACCUMULATE:** only below EV ($217.69), and BUY only below $152.38. Neither is close.
- **Fix the tool regardless:** the `valuation.dcf()` mid-year TV inconsistency (+2.8%) should be repaired before the next run. It biases every pipeline FV slightly low.

**Investor fit (for the synthesis; facts only):**
- The 30% US withholding takes the 1.24% yield to ~0.87% net.
- SYK is US-situs for estate purposes (US$60k threshold applies at the portfolio level).
- **Overlap:** the user also holds ZBH (pipeline TRIM, capital allocation D), so hips, knees and trauma exposure is doubled. HOLD on SYK means do not add to combined orthopaedic exposure. If the user wants to cut ortho, SYK is the better of the two to keep: higher ROIC, better allocator grade (C vs D), and a wide franchise moat. But at 1.30x EV it is not cheap.
