<!-- pipeline:value-skeptic -->
# Skeptic audit: TSM (as of 2026-10-13)

Price US$444.35/ADS. This is the 2026-10-12 close, labelled 2026-10-13 in facts.json; yfinance printed 439.57 on 2026-10-13. Financials are in NT$ millions, 1 ADS = 5 shares, USDTWD 32.133. CURRENT HOLDING (SG resident, SGD base). Corrected model: `03_rerun.py` (executed; output quoted below).

## 1. Pre-mortem (written before reading the model)
I wrote this to the scratchpad from `01_research.md` and `facts.json` only, before opening `02_quant.md` or `02_model.py`. It is reproduced verbatim.

> **The most likely structural reason TSM is worth materially less in 5 years: peak-cycle margins are being capitalised at a peak multiple while capital intensity is locked in.**
> - TTM GM is 64.2% (2Q26 67.7%), against a FY21–25 range of 51.6–59.9%. TTM OM is 56%, against 41–51%.
> - FY23 showed the cycle: revenue −4.5%, NI −14%. AI/HPC is 58–66% of revenue, the top-2 customers are 36%, and the top-10 are 78%.
> - Capex is being raised: US$60–64B in 2026, "even more significantly higher" over the next 3 years, and US$265B pledged in Arizona at 2–4 pts of GM dilution. If AI capex digests in 2027–29, TSMC will have committed capacity and depreciation into a downturn. GM would fall back to the mid-50s and FCF conversion would drop (FCF/NI has historically been about 0.5–0.6). A 33x trailing P/E would then re-rate to about 15–20x on lower earnings.
> - Cross-strait risk is the tail (low probability, catastrophic), not the modal path.
> - Watch for a model that holds 55%+ OM in perpetuity, or a terminal value that assumes the AI growth rate persists.

## 2. Number audit
I recomputed every derived figure with python3 against facts.json. There were 5 web spot-checks: the 6-K for 4Q25 (2026-01-15), the 6-K for 1Q26 (2026-04-16), the September 2026 monthly revenue 6-K (2026-10-08, accn 0001046179-26-000680), the long-term targets (secondary), and the base-rate literature (secondary). Price, ^TNX, FX and beta were checked against yfinance.

| # | Input | Quant value | Verified value | Source | Status | Δ FV (base) |
|---|---|---|---|---|---|---|
| 1 | Price | US$444.35 | 444.35 = **2026-10-12 close**; 10-13 print 439.57 | yfinance history | PASS (temporal label only) | none (MoS −1%) |
| 2 | Shares / ADS ratio | 25,932.5M / 5 | 5,186.47M ADS-eq × 5 = 25,932.4M; mcap/ADS = 444.350 | 20-F cover; yfinance | PASS | 0 |
| 3 | USDTWD | 32.133 | 32.142 (10-13) | yfinance TWD=X | PASS | 0 |
| 4 | Net debt for DCF (incl. NCI) | −2,407,278 | cash 3,517,786.9; debt 1,068,556.0; NCI 41,952.6, all components sum | 6-K 2Q26 FS | PASS | 0 |
| 5 | Base revenue (TTM) | 4,440,492.5 | FY25 + 1H26 − 1H25 = 4,440,492.5; 1Q+2Q = 1H26 ✓ | facts | PASS | 0 |
| 6 | Risk-free | 5.277% "^TNX 2026-10-13" | ^TNX closes: **5.277 = 10-07**, 5.240 = 10-12, 5.208 = 10-13; FRED DGS10 5.22% (10-08) | yfinance ^TNX; orchestrator | **FAIL: Temporal** (stale, mislabelled) | **+0.9%** |
| 7 | Beta | 1.0 ("no sourced beta") | yfinance 1.239 (5y monthly); Blume-adjusted 1.16 | yfinance info | **FAIL: Source fidelity** (unsourced, contradicted by data) | **−11.0%** (kept as a disagreement, §7) |
| 8 | ERP | 5.0% | assumption, stated | — | PASS (judgement) | — |
| 9 | WACC arithmetic | 10.192% | 10.192% recomputed from their inputs | 03_rerun | PASS (inputs: see 6, 7) | — |
| 10 | EBITDA margin path, 68% mid-cycle | FY23–25 67.2/68.6/68.9% | 67.24/68.58/68.89% | facts | PASS | 0 |
| 11 | Y1 revenue: 3Q26 | guide mid NT$1,446,400 | **3Q26 actual NT$1,494,243** (Jan–Sep 3,898,727 − 1H26 2,404,483.7); US$46.73B at 3Q average FX 31.974, **above the top of the guide (US$45.8B)** | 6-K 2026-10-08 | **FAIL: Temporal** (published 5 days before the run; dossier had it as UNKNOWN) | +1.9% (with #12) |
| 12 | FY26 growth +40% | applied to **NT$** FY25 revenue | guide is "+40% in **US dollars**". FY25 US$122.43B = 1Q25 25.53 + 2Q25 30.07 + 3Q25 33.10 + 4Q25 33.73 (derived from releases). 4Q26 implied US$48.57B × 32 = NT$1,554B, vs Quant NT$1,482B | 6-K 4Q25, 1Q26, 2Q26 | **FAIL: Comparability** (currency basis) | (in #11) |
| 13 | Capex 37% of FY26 revenue | 37.2% | 36.4% on a USD-basis FY26 revenue | facts guidance | PASS (<1 pt; left unchanged) | ~0 |
| 14 | Tax 18% | 18% | 2Q26 18.05%; FY25 16.97% | facts | PASS | 0 |
| 15 | D&A rule k | 0.675 | 0.6746 | facts | PASS | 0 |
| 16 | Terminal g 3% / ROIC 25% | — | Y10 reinvestment 23.4% of NOPAT vs terminal 12% (FCF margin jumps from 32.3% to 37.1%). The Quant flagged it, effect <1% | 02_model | PASS (noted) | <1% |
| 17 | Discounting convention / valuation date | end-of-year from 30 Jun 2026, compared with a 13 Oct price | mid-year convention (×(1+WACC)^0.5), roll-forward 105 days, less NT$13.0/share of dividends a 13-Oct buyer no longer receives (2026 plan 24 − 1H26 paid 11.0) | 03_rerun | **FAIL: Model fidelity / temporal** | **+7.0%** |
| 18 | SBC treatment | deducted from EBITDA, shares flat | SBC 683.5 TTM = 0.015% of revenue; no double count | facts | PASS | 0 |
| 19 | TV share | 58/65/70% | 55/62/67% (Skeptic WACC) | 03_rerun | PASS (<75%) | — |
| 20 | Accounting identities | — | FCF = OCF − capex holds for all 5 yrs; EV = mcap − cash + debt + NCI ✓; TTM OCF/capex/OI/EPS ✓ | facts | PASS | 0 |

**Result: 20 checked, 5 failed.** Four are errors and are corrected in `03_rerun.py`: #6, #11, #12, #17. One is a disagreement kept separate: #7. No arithmetic, identity, ADR or unit errors were found in the Researcher's or Quant's work.

`03_rerun.py` step-by-step (US$/ADS):
```
                                                          BEAR     BASE     BULL   base vs prior step
Q0 Quant as published                                     131.23   289.71   484.70
C1 + rf 5.22%                                             132.19   292.36   489.91   +0.9%
C2+C3 + 3Q26 actual, FY26 growth in USD                   133.66   297.90   499.14   +1.9%
C4 + mid-year, roll-fwd, less divs (AUDITED, beta 1.0)    141.47   318.68   535.82   +7.0%
C5 + beta 1.16 (SKEPTIC CENTRAL)                          128.81   283.62   467.48   -11.0%
    alt: raw beta 1.239                                   123.39   268.89   439.40   -5.2%
WACC: Quant 10.192% | C1 10.136% | C5 (beta 1.16) 10.925% | raw beta 11.314%
Reverse DCF (BASE margins, same conventions): implied 10-yr revenue CAGR 17.6% (beta 1.0) / 19.3% (beta 1.16)
Implied IRR on corrected BASE cash flows: 8.28%; on BULL cash flows: 11.24%
```
The audited Quant base is **US$318.68 (+10.0% vs the published 289.71)**. The Skeptic central base is **US$283.62 (−2.1%)**. The error corrections push the value up; the beta disagreement pulls it down by about the same amount.

**Discount-rate decision (orchestrator Q1).** I keep a USD-built rate on the NT$ flows. This is not an inconsistency here. Revenue is priced and guided in USD, and every growth input is a USD guide converted at a constant 32.0–32.13. The model is therefore valuing USD cash flows at constant FX, and a USD rate is the right match. FX is an unmodelled risk leg (±10% USDTWD moves value by ∓9–11%, per Quant §G). I put **no Taiwan country premium in the rate**. Cross-strait risk enters only as an explicit 5% tail scenario in §5, so it is not counted twice. The +2 pp "Taiwan" row in the Quant's grid should not be used together with §5. Beta is market-cycle risk, not geopolitical risk, and a historical beta contains no realised cross-strait event, so raising it to 1.16 does not double-count Taiwan.

## 3. Quality of earnings
- **SBC:** 683.5 TTM = **0.026% of OCF and 0.015% of revenue**. FY21–25 SBC/OCF ranged from 0.0007% to 0.068%. The Quant already treats SBC as a cash cost, so the SBC-adjusted and unadjusted values differ by <0.1%. SBC-adjusted FCF TTM is 1,133,466 vs 1,134,150. **SBC-adjusted fair value is the same as reported: base US$283.62 (Skeptic) / 318.68 (audited); EV in §5 is unchanged.**
- **Accruals (NT$M):**

| | FY21 | FY22 | FY23 | FY24 | FY25 | TTM |
|---|---|---|---|---|---|---|
| OCF / NI | 1.88 | 1.62 | 1.46 | 1.58 | 1.34 | 1.19 |
| OCF − NI − D&A (working capital and other) | UNK | UNK | −141,964 | +5,000 | −110,725 | −270,690 |
| FCF / NI | 0.46 | 0.53 | 0.34 | 0.75 | 0.59 | 0.51 |

  OCF is **not** flattered by working capital. The residual is negative in 3 of 4 measurable periods, meaning working capital absorbed cash. The TTM residual also removes the non-cash NT$63B VIS gain. Unverified: customer prepayments ("temporary receipts"), which flattered OCF in earlier cycles, are not in facts.json (UNKNOWN). Inventory days are 87, up 7 on the N2 ramp. AR and inventory growth series are UNKNOWN, so the receivables/inventory-vs-sales test cannot be run.
- **The real QoE issue is depreciation lag, not accruals.** Cumulative FY21–25 FCF was NT$2.97T on NI of 5.29T: **56% conversion**. TTM owner earnings (normalised) are 1,346,751 against NI of 2,158,392, so **OE/NI = 0.62 and P/OE = 55x**. Capex/D&A is 2.16x TTM and about 2.9x on the FY26 guide. Reported EPS will overstate distributable cash until depreciation catches up, and the 33x P/E understates how expensive the stock is on Buffett's metric.
- **Adjusted vs GAAP:** TSMC reports IFRS only, with no "adjusted" add-backs. That is clean. The one non-recurring item is the 2Q26 VIS disposal gain (NT$63B pre-tax, EPS +2.24), which the Quant normalised out. Government grants (FY25 NT$76.3B, about 6% of capex) sit in investing flows. They fell to NT$0.6B in 1H26 vs 67.1B in 1H25, so FCF that relied on grants is a fading tailwind (the Quant excluded them, which is conservative).

## 4. Capital allocation: **Grade A−**
- **Share count:** 25,930M (FY21) → 25,932.5M (2Q26). **Zero net dilution in 5 years.** The only buyback was 3.2M shares / NT$3,089M in 2024 (about NT$965/share, 0.01% of shares, purpose UNKNOWN). It is irrelevant to value, and there is no buying back at peak prices. Buyback price discipline: not applicable.
- **Buffett's $1 test:** market value 31 Dec 2020 = US$109.04 (yfinance close) × 5,186M ADS-eq = **US$565.5B**; 31 Dec 2025 = 303.89 × 5,186.5M = **US$1,576.1B**; Δ = **US$1,010.6B**. Retained earnings FY21–25 (NI parent − dividends paid) = NT$3,620,430M = **US$117.8B**, converting each year at its yfinance average USDTWD. **US$8.58 of market value per US$1 retained** (calendar 5 yrs). Dec 2020 → today: (2,304.6 − 565.5) / (117.8 + 1H26 31.5) = **US$11.6 per $1**. The test passes by a wide margin. Caveat: part of this is multiple expansion, not retention alone.
- **Reinvestment returns:** ROIC FY24 34.7%, FY25 44.0%, TTM 46.8% vs WACC 10.1–10.9%. Incremental ROIC FY24 → TTM = ΔNOPAT 945,444 / ΔIC 1,203,174 = **79%**, helped by utilisation and pricing.
- **M&A:** no acquisition above 5% of mcap. The VIS stake was sold at a NT$63B gain. The Sony image-sensor JV (≤JPY282B) is small. Goodwill: UNKNOWN (not in facts). No diworsification.
- **The minus:** Arizona (US$265B total pledge), JASM and ESMC are politically driven capacity at 2–4 pts of GM dilution. Their stand-alone ROIC is UNKNOWN. This is the one large allocation decision that may be made below TSMC's own hurdle.
- **Payouts:** FY25 dividends were 27.5% of NI and 46.6% of FCF; the 2026 plan (NT$24) is 54.9% of TTM FCF. Payouts are funded from FCF with debt flat at about NT$1.05–1.07T, so leverage is not funding them.
- **Insider activity: UNKNOWN** (foreign private issuer, no Form 4s; MOPS not checked). **Candour:** good. Wei on double-ordering: "Might not be correct, but we did carefully". The CFO quantified the 2H26 N2 (3–4 pts) and overseas (2–4 pts) GM dilution in advance.
- Rubric: ROIC ≫ WACC sustained, disciplined reinvestment, no dilution → A, with a minus for the unproven returns on overseas fabs.

## 5. Probabilities & expected value
**Outside view first.** The reverse DCF (corrected conventions) says US$444.35 requires a **17.6% (beta 1.0) to 19.3% (beta 1.16) 10-yr revenue CAGR** at 68% EBITDA margins, from a US$138B TTM base, to about 5x today's revenue. Base rate (Mauboussin, *The Base Rate Book* and "A new world of accelerating growth", via secondary summaries, 1950–2015 data): **about 0% of companies starting above US$50B (real) revenue sustained a >20% 10-yr CAGR, and none starting above US$100B sustained mid-teens for a decade.** For reference, the Bull path is 17.1% including the half-booked Y1 (Y2–10 = 14.5%), so it sits at the outer edge of the historical distribution. Outside-view prior: Bull ≤10%.

**Inside-view adjustments.** Pushing up: 3Q26 revenue beat the top of the guide (US$46.7B vs 45.8B); Jan–Sep is +41.1%; leading-edge dominance (2nm/3nm/5nm = 66% of wafer revenue); management's ~25% 2024–29 USD CAGR target (secondary source; the Base path already matches it through 2029, at about US$277B in CY29). Pushing down: top-2 customers 36% and rising; management's own double-ordering caveat; capex at about 2.9x D&A; a downturn in at least one year of the next ten is near-certain for a foundry. Separate tail: cross-strait disruption, valued at net cash per ADS of US$14.70 (generous, since the cash is mostly held in Taiwan).

| Scenario | p | Skeptic value (beta 1.16) | Audited Quant (beta 1.0) |
|---|---|---|---|
| Bear (AI digestion, EBITDA 62–63%, 5.1% CAGR) | 25% | 128.81 | 141.47 |
| Base (FY26 +40%, fade to 4%, 13.0% CAGR) | 50% | 283.62 | 318.68 |
| Bull (17.1% CAGR, EBITDA 71%) | 20% | 467.48 | 535.82 |
| Taiwan tail (≈ net cash) | 5% | 14.70 | 14.70 |
| **Expected value** | | **US$268.24** | **US$302.61** |
| **Margin of safety** = 1 − 444.35/EV | | **−65.7%** | −46.8% |
| **Asymmetry** = (EV − P)/(P − bear) | | **−0.56** (negative: downside to EV, no upside) | −0.47 |

Robustness: holding the bear at 20% and the tail at 5%, EV reaches the HOLD threshold (EV × 1.3 ≥ price, i.e. EV ≥ US$341.81) only if Bull probability is ≥34% on audited values or ≥56% on Skeptic values. The bull case would have to be 3–5x the outside-view prior.

## 6. Bear thesis & downside catalysts
**Bear thesis (unchanged by the model; the Quant's bear path is my pre-mortem):** AI-capex digestion hits while TSMC's capex and overseas commitments are locked in. Margins revert toward the 56% GM floor management itself targets, and the multiple compresses together with earnings. The model confirms the price already sits at about the Bull value. It does not need the bear case to be overvalued.

1. **AI demand digestion / double-ordering.** Signpost: monthly revenue (6-K around the 10th) and quarterly HPC revenue. **Confirmation threshold:** two consecutive quarters of q/q USD revenue decline, or monthly y/y growth below +10% for 3 consecutive months, *while* capex guidance is held or raised. Supporting signal: inventory days above 95 (87 now).
2. **Structural margin erosion from N2 ramp, overseas fabs and the depreciation wave.** Signpost: quarterly GM/OM vs guide, and capex/D&A. **Confirmation threshold:** GM below 56% (management's own long-term floor, secondary source) or OM below 50% in a quarter *without* a revenue decline, or FY27 capex above 40% of revenue with revenue growth below 15%.

**The single variable that flips the thesis:** FY27 USD revenue growth (the year after the guided +40%). At **≥25% with GM ≥60%**, the Bull path becomes the base and EV moves toward the US$400s. At **below 15%**, the Base/Bear split is confirmed and price would sit about 1.6x EV. Close second: the discount rate. The price equals the corrected Base at an **8.28% IRR**, only about 3 pp over the US 10y.

## 7. Disagreements with the Quant (kept, not averaged)
| # | Issue | Quant view | Skeptic view | Evidence | Effect on base FV |
|---|---|---|---|---|---|
| 1 | Risk-free | 5.277% | 5.22% | ^TNX 5.277 is the 10-07 close; FRED DGS10 5.22% | +0.9% (corrected) |
| 2 | 3Q26 revenue | guide mid NT$1,446,400 | actual NT$1,494,243 | 6-K 2026-10-08 | +1.9% with #3 (corrected) |
| 3 | FY26 +40% basis | NT$ | USD (FY25 US$122.43B) | 6-K 4Q25/1Q26/2Q26 | (in #2) |
| 4 | Discounting conventions | end-year from 30 Jun, a "conservative choice" | mid-year + roll-forward to the price date, less NT$13/sh dividends | a price dated 13 Oct must be compared with a value dated 13 Oct | +7.0% (corrected) |
| 5 | Beta | 1.0 (unsourced) | 1.16 (Blume-adjusted from yfinance 1.239) | data layer; a cyclical semi with beta <1 is unsupported | −11.0% (**unresolved**; both shown) |
| 6 | Taiwan risk | flagged; offered +2 pp WACC row or a probability | 5% explicit tail at net cash; no CRP in WACC | avoids double count | −US$13 on EV |
| 7 | 1H27 = 1H26 × 1.25 | base | after the 3Q beat this implies 1H27 (3,006) **below** 2H26 (3,048): a sequential decline built into the base. Mildly conservative; left unchanged | 03_rerun | about +1–3% if flat-to-up (not applied) |
| 8 | Required MoS | n/a | 30% (Wide moat but cyclical, not "predictable"); 40% shown as an alternative | SKILL verdict rules | entry level only |
| 9 | Terminal reinvestment step | flagged | agree; immaterial | Quant §H4 | <1% |

Net: Audited Quant EV US$302.61 vs Skeptic EV US$268.24, a gap of 11.4%. That is below the 15% threshold for a conviction drop. **Both imply TRIM.**

## 8. Verdict recommendation
Held position. Price US$444.35 > EV × 1.3 under both value sets (Skeptic 348.72; audited 393.39) → **TRIM**. Capital allocation A− (thesis intact, not SELL). The bear thesis is **not** yet visible in the numbers (3Q26 beat), so this is a valuation trim, not a thesis break.

- **VERDICT:** TRIM
- **CONVICTION:** MEDIUM. HIGH drops one level because 4 load-bearing inputs were corrected (>2). TV share is <75%, the unresolved disagreement is 11.4% (<15%), and the financials are primary (20-F/6-K).
- **FAIR_VALUE (EV):** US$268.24 (audited-Quant alternative US$302.61)
- **ENTRY_BELOW:** US$187.77 (EV × 0.70; at a 40% cyclical MoS: 160.95)
- **EXIT_ABOVE:** US$348.72 (EV × 1.3; audited alternative 393.39)
- **Reason:** the price equals roughly the Bull-case value and needs a ~18–19% 10-yr revenue CAGR from a US$138B base, which no company that size has historically sustained. A wonderful business (A− allocator, ROIC ~47%) is priced for its best case, so trim the position and keep a core holding.
- KEY_RISK (to the trim): AI demand keeps compounding at 25%+ through FY27–28 (the Bull path becomes the base).

Sources: [6-K Sep-2026 revenue](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000680/tsm-revenue20261008.htm) · [6-K 4Q25 release](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000008/a4q25e_withguidancexfinal.htm) · [6-K 1Q26 release](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm) · [TSMC Sep-2026 PR](https://pr.tsmc.com/english/news/3343) · LT targets (secondary): [SemiVision](https://tspasemiconductor.substack.com/p/from-tsmcs-earnings-to-the-ustaiwan), [KGI note](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_15012026e.pdf), [VanEck](https://www.vaneck.com/mx/en/news-and-insights/blogs/thematic-investing/tsmc-q1-earnings-call-what-it-means-for-smh/) · Base rates (secondary): [MOI Global, Mauboussin](https://moiglobal.com/a-world-of-accelerating-growth-202201/), [HedgeFundAlpha](https://hedgefundalpha.com/education/michael-mauboussin-the-base-rate-book/) · yfinance (TSM history/beta, ^TNX, TWD=X), 2026-10-13 · facts.json S1–S9.
