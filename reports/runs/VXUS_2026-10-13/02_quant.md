<!-- pipeline:value-quant -->
# Quant model: VXUS (as of 2026-10-13)

**Template: FUND** (dossier §0). Vanguard Total International Stock ETF, a US-domiciled RIC (Delaware statutory trust, dossier §8). Status: current holding alongside VWRA (the core).
- **Price:** 84.52 USD, the 2026-10-13 close (facts: price.close_raw). 00_inputs shows 84.405 intraday, which is −0.14%; the close is used, per dossier §1/§10.
- **Index P/E:** 18.3x for the fund, 18.2x for the index (factsheet, 2026-06-30, dossier §2). yfinance gives 16.14x on a different definition (fundamentals.json).
- **12-month change:** +15.35% on price, +18.30% total return (facts).
- **Model:** `reports/runs/VXUS_2026-10-13/02_model.py`, executed. The output is pasted verbatim in E.

**Tape check (RULE 0).** The ex-US index trades at 18.3x after +18.3% total return over 12 months. Its earnings yield is 1/18.3 = **5.46%** against a 10y UST of **5.22%**, a gap of +0.24 pp (output §0). The ex-US universe is cheaper than the world index; the VWRA run had an E/P of 4.76%, below the UST. Even so, it offers only a thin cushion over Treasuries. Nothing below calls it "cheap".

**Data warnings (fundamentals.json, 1):** `fund/ETF: operating-company metrics do not apply`. Errors: none. Conflicts carried from dossier §10:
- Price, intraday vs close: −0.14%.
- P/E: factsheet 18.3x vs yfinance 16.14x.
- Distribution yield: 2.35% vs stale third-party figures (discarded).

The dossier lists 8 UNKNOWNs, all of which are carried here.

**Method.** There is no DCF of a fund (AGENTS.md routing). The model reuses the VWRA run's structure (`VWRA.L_2026-10-13/03_rerun.py`), so the two are comparable:
- **M1:** earnings yield and look-through ROE (P/B ÷ P/E).
- **M2:** the 10-yr Bogle decomposition, net = yield + per-share EPS growth + re-rating − TER − source-country WHT − investor-level tax. It is run for **four holders of the same ex-US exposure**:
  1. VXUS with no investor-level tax;
  2. VXUS held by a Singapore resident;
  3. the ex-US sleeve inside VWRA;
  4. the Irish ex-US UCITS (IE0009A5ADV9).
- **M2b:** a year-by-year simulation in which the yield moves with the P/E path. This is a cross-check of the drag.
- **M3:** the value-driver justified P/E (payout = 1 − g/ROE), used for the reverse solve and the k × g grid.

**Key identity.** VXUS's observed cash distribution (TTM 1.985 USD = **2.349%**, facts) is already net of two things:
- the source-country WHT, paid at fund level and equal to 7.48% of the cash dividend (facts: 2024 FTC worksheet);
- the 0.05% TER. This is an ASSUMPTION (expenses paid from income); output §8 shows the drag gap is unchanged if it is false.

So the gross underlying yield, DY_gross = 2.349% × 1.0748 + 0.05% = **2.574%**, is a property of the exposure and common to every wrapper. Each wrapper then subtracts its own layers.

**Labels:** ASSUMPTION = I chose the number and it is not sourced. UNKNOWN = set to a neutral value and swept. There are no probabilities and no verdict in this file; those belong to the Skeptic.

### Headline (decisive quantity: after-tax return for a Singapore holder)
| Base case, same ex-US exposure | 10-yr net/yr | Implied ERP vs 5.22% | US$10,000 → yr 10 |
|---|---|---|---|
| VXUS, no investor-level tax | 7.35% | – | 20,322 |
| **VXUS, Singapore holder** | **6.64%** | **+1.42%** | **19,027** |
| VWRA ex-US sleeve (Irish, 0.14%) | 7.26% | +2.04% | 20,152 |
| Irish ex-US UCITS (0.12%) | 7.28% | – | 20,190 |

- **Annual drag difference, VXUS-SG minus the VWRA sleeve: 61.5 bp** (M2), or 65.0 bp on M2b. It is 63.5 bp vs the Irish ex-US UCITS. The 30% US WHT on the distribution (70.5 bp) is partly offset by VXUS's lower TER (−9.0 / −7.0 bp).
- **10-yr wealth difference: US$1,125 per US$10,000** in the base case (5.58% of the VWRA-sleeve outcome). The range across scenarios is US$764 (bear) to US$1,465 (bull); M2b gives US$923 to US$1,467.
- The drag consumes **30% of the ex-US equity premium** (output §3b).
- Effective total tax on the underlying dividends is **34.9% in VXUS** vs **7.0% in an Irish wrapper**, on equal source-country rates (output §2).

## A. Lynch classification & category checks
- **Category: not assigned.** AGENTS.md routing for FUND says "Do not assign a Lynch category". The fund holds 8,755 stocks (facts: n_stocks_fund), which span every category.
- **Category checks:** none apply to the vehicle.
- **PEG.** `peg_is_valid(PE=18.3, fwd=None, growth=0.126)` returns `True, 'ok'` (output §1). The only growth figure, however, is the factsheet's **backward-looking** 12.6% "EPS growth" (horizon unstated, dossier §2/§9). No consensus exists (RULE 2; dossier §9). **PEG is not used**: under the FUND template it is not a decision metric, and a trailing growth rate is not a forecast.
- **Lynch ratio** = (EPS growth % + dividend yield %) / P/E = (12.6 + 2.35) / 18.3 = **0.82** (output §1). This is **informational only**: the growth is trailing and the metric is not a FUND test. On Lynch's scale it would read "poor" (<1).
- **Net-cash-adjusted P/E, inventory and receivables vs sales:** not applicable (fund).
- **Debt structure:** fund-level borrowing is not reported, so UNKNOWN. Look-through index leverage is also UNKNOWN.
- **Distribution record (the FUND analogue of a dividend check; it drives the tax drag):**
  - The payout is lumpy and December-heavy (dossier §5).
  - Calendar 2025 = 2.399 USD, which is **2.84%** on today's price. TTM = 1.985 USD, which is 2.35%.
  - Q1–Q3 2026 paid 0.622 vs 1.036 in Q1–Q3 2025, **−40.0%** (output §0).
  - The cause is UNKNOWN: timing, lower foreign dividends, or FX. The drag scales 1:1 with the yield.

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)
**Circle of competence / predictability: partly.**
- **Vehicle: yes.** Passive, sampled, 4.4% turnover (dossier §2). The NAV return matched the index to within +0.13 / +0.14 / 0.00 pp over 3/5/10y (facts: tracking_difference_pp). Note that the comparison index is **net of the withholding a US RIC suffers** (dossier §2 caveat), so this TD says nothing about investor-level tax.
- **Wrapper tax for this holder: yes, mechanically.** The 30% statutory rate (26 USC 871(a)) applies to 100% of a domestic-corporation dividend. Singapore has no treaty (dossier §8).
- **Underlying earnings 10 years out: no, beyond broad bounds.** There are 8,755 stocks across Japan 15.4%, Taiwan 9.1%, UK 8.0%, Canada 7.7%, Korea 7.5% and China 6.7% (dossier §2). The top 10 total 15.0%, and **10.8% sits in four semiconductor names** (TSMC, Samsung, SK hynix, ASML; output §1). The ex-US index is more diversified than VWRA's top 10, but it carries its own memory/foundry cycle.

**Moat:** not rated (a fund has no moat). Look-through quality:
- **Look-through ROE = P/B ÷ P/E = 2.3 / 18.3 = 12.57%** (output §1; same vendor and date). The factsheet's ROE is 13.3% (definitions differ). Against k = 10.22% (§D) the spread is **+2.35 pts**, a much thinner quality spread than VWRA's 17.14% look-through (VWRA run, 02_quant.md).
- **5-yr margin/ROE trend:** UNKNOWN (no history in the dossier). Widening / stable / eroding: UNKNOWN.

**Owner earnings:** not applicable (NI, D&A and capex are null in fundamentals.json).
- Look-through **earnings yield is 5.46%**.
- The **payout** (DY_gross × P/E) is **47.11%**.
- The **sustainable per-share growth envelope** runs from **2.89%** (all retained earnings spent on buybacks at E/P) to **6.65%** (all reinvested at the 12.57% ROE). Using the factsheet ROE instead gives an upper bound of 7.03% (output §1).

**SBC:** index EPS is vendor-defined, and whether it is before or after SBC is UNKNOWN. M2 uses **per-share** EPS growth, so dilution and buybacks enter once, through the share count. No separate deduction is made, so there is no double count.

**Structure quality (the FUND substitute for moat), from the dossier:**
| Item | VXUS (SG holder) | Irish UCITS (VWRA / IE ex-US) | Source |
|---|---|---|---|
| Domicile / legal form | US Delaware statutory trust, taxed as a RIC | Ireland, UCITS | dossier §7–8 |
| Investor-level US WHT on distributions | 30% on the whole distribution | none (accumulating) | 26 USC 871(a), 861(a)(2)(A); dossier §8 |
| Source-country WHT on ex-US dividends | at fund level, 7.48% of cash dividends (2024); no credit usable by a SG holder | at fund level, rate UNKNOWN | facts: FTC worksheet |
| US estate-tax situs | **US-situs** (2104(a); 2105(d) look-through ended 2011). Form 706-NA above US$60,000; credit US$13,000; no SG death-tax treaty | not US-situs | facts: us_tax_nonresident |
| 871(k) exempt share of distributions | UNKNOWN (QSG list did not visibly include VXUS) | n/a | dossier §5 |
| Broker withholding practice | UNKNOWN (statute 30%) | n/a | dossier §8 |

**ROIC vs WACC (look-through):** 12.57% ROE vs 10.22% k = **+2.35 pts**. Goodwill is not applicable.

## C. GARP & valuation matrix
| Metric | Current | 5-yr own avg | Peer median |
|---|---|---|---|
| P/E trailing | 18.3x fund / 18.2x index (factsheet, 2026-06-30); 16.14x yfinance (definition differs) | UNKNOWN (no history in dossier) | UNKNOWN (dossier §7: multiples not collected for fund peers) |
| P/E forward | UNKNOWN | UNKNOWN | UNKNOWN |
| P/B | 2.3x | UNKNOWN | UNKNOWN |
| Earnings yield | 5.46% (6.19% on yfinance P/E) vs UST 5.22% | UNKNOWN | n/a |
| CAPE | UNKNOWN | UNKNOWN | n/a |
| Cash distribution yield | 2.35% TTM (2.84% CY2025 on today's price) | UNKNOWN | UNKNOWN |
| EV/EBITDA, P/FCF, SBC-adj P/FCF, FCF yield | n/a (fund) | n/a | n/a |
| Owner-earnings yield | n/a. Look-through earnings yield 5.46% | – | – |
| PEG | not used (FUND). Gate returned valid on backward growth only | – | – |
| Lynch ratio | 0.82 (informational, trailing growth) | – | – |
| Look-through ROE vs k | 12.57% vs 10.22% | UNKNOWN | VWRA 17.14% (VWRA run) |
| TER | **0.05%** | – | listed peers: VWRA 0.14%, IE ex-US 0.12% (Acc; Dist 0.12% [SNIPPET]), iShares World ex-USA 0.15%, iShares EM IMI 0.18% (facts). Median not computed: the peers are not like-for-like |
| Tracking difference | +0.68 / +0.13 / +0.14 / 0.00 pp (1/3/5/10y, vs a WHT-adjusted index) | – | VWRA calendar 2020–25 mean −0.023 pp (output §8). IE ex-US: UNKNOWN (launched 2026-08-18, TNA US$35M) |
| **All-in drag on the ex-US exposure, SG holder (TER + source WHT + US WHT)** | **93.0 bp/yr** | – | VWRA sleeve **31.6 bp**; IE ex-US **29.6 bp**; iShares pair 57.5–60.5 bp better than VXUS (output §2) |
| Price vs NAV | −0.07% (NAV date unstated; indicative) | – | – |

**Role / exposure.**
- VWRA's ex-US share is 38.32%. Getting US$1 of ex-US exposure through VWRA needs US$2.61 of VWRA and brings **US$1.61 of US equity** with it (output §1).
- So VWRA is a cheaper wrapper for the same ex-US *stocks*, but **not a substitute for an ex-US *tilt***. Only a dedicated Irish ex-US fund keeps the tilt: the Vanguard UCITS (0.12%), or the iShares developed + EM pair.
- VXUS also adds small caps (8,755 stocks vs VWRA's 3,784). Their return contribution is UNKNOWN; output §8 shows ±0.10%/yr moves the gap by ∓10 bp.
- Holding VXUS on top of VWRA raises ex-US weight above market cap. This is a tilt, not diversification (dossier §8). The exact holdings overlap is UNKNOWN.

## D. Discount rate build
| Component | Value | Source |
|---|---|---|
| Risk-free (10y UST) | 5.22% | 00_inputs (FRED DGS10, 2026-10-08; dossier re-verified) |
| ERP | 5.0% | 00_inputs |
| Beta | **1.0** | fundamentals.json `beta` is null, so no vendor beta exists. 1.0 is used by default, stated. A broad cap-weighted index is close to its own market, but its beta to a global or US market proxy is UNKNOWN |
| Cost of debt / weights | n/a | fund. Equity-only rate |
| CAPM k = rf + β × ERP | **10.22%** | output §0 |
| Floor (USD) | 8.0% | 00_inputs. Does not bind |
| SGD floor (local 10y + 4%) | UNKNOWN | SG 10y is not in 00_inputs. All work is in USD |

Staleness: rf is dated 5 days before AS_OF, so it is not stale. k only affects the HEV and M3 figures, not the 10-yr return (FAIR_VALUE under FUND). k ±1% is in the M3 grid, and k ±10% moves the base HEV by +9.8% / −8.8% (output §10a).

## E. Scenarios (FUND: 10-yr decomposition; pre-tax and after-tax for a Singapore holder)
| Input | Bear | Base | Bull | Source / rationale |
|---|---|---|---|---|
| Cash distribution yield | 2.35% | 2.35% | 2.35% | facts (TTM). Swept at 2.84% and 2.11% in §8 |
| Gross underlying yield | 2.57% | 2.57% | 2.57% | identity above (f = 7.48%, facts) |
| Per-share EPS growth | 3.0% | 5.0% | 6.65% | **ASSUMPTION.** Bear ≈ lower envelope (2.89%). Base = VWRA-run base. Bull = computed upper envelope (all retained earnings reinvested at 12.57% ROE). VWRA's bull used 7.5%, which here would exceed the envelope with no sourced reason |
| Start P/E | 18.3x | 18.3x | 18.3x | dossier §2 |
| Exit P/E yr 10 | 14.3x | 18.3x | 21.1x | **ASSUMPTION, same rule as the VWRA run:** bear = M3 justified at k 8% / g 2% (14.29x); bull = M3 justified at k 8% / g 5% (21.08x). At the sourced k of 10.22%, justified P/E is only 10.4–11.4x for g 2–4% (output §6), so the base's no re-rating is not conservative |
| TER | 0.05% / 0.14% / 0.12% | same | same | facts (VXUS / VWRA / IE ex-US) |
| Source-country WHT | 17.6 bp in every wrapper | same | same | facts. Irish rate UNKNOWN, set equal, swept ±50% |
| US investor-level WHT | 30% × 2.35% = 70.5 bp (VXUS-SG only) | same | same | facts (871(a)). 871(k) exempt share UNKNOWN, set to 0 |
| Tracking residual beyond TER | 0 | 0 | 0 | UNKNOWN. TD-based rows in §8 |

| Result | Bear | Base | Bull |
|---|---|---|---|
| Pre-investor-tax net (VXUS) | 2.84% | 7.35% | 10.53% |
| **VXUS, Singapore holder, after-tax** | **2.13%** | **6.64%** | **9.82%** |
| VWRA ex-US sleeve | 2.75% | 7.26% | 10.44% |
| Irish ex-US UCITS | 2.77% | 7.28% | 10.46% |
| Drag gap vs VWRA sleeve, M2 / M2b | 61.5 / 72.3 bp | 61.5 / 65.0 bp | 61.5 / 61.5 bp |
| Implied ERP, VXUS-SG / VWRA sleeve | −3.09% / −2.47% | +1.42% / +2.04% | +4.60% / +5.22% |
| US$10k → yr 10, VXUS-SG / VWRA sleeve | 12,352 / 13,116 | 19,027 / 20,152 | 25,524 / 26,988 |
| **10-yr wealth gap per US$10k (and per S$10k at constant FX)**, M2 (M2b) | **764 (923)** | **1,125 (1,200)** | **1,465 (1,467)** |
| HEV/share at k 10.22%, VXUS-SG / VWRA sleeve (price 84.52) | 39.45 / 41.89 | 60.77 / 64.37 | 81.53 / 86.21 |

How to read these:
- **HEV** (hurdle-equivalent value) is the price at which the scenario earns exactly k. It is **not** a fair value; NAV is that. It is shown only for comparability with the VWRA run.
- **Terminal share: 100% by construction,** above the 75% flag. The exit P/E carries the terminal assumption, as in the VWRA run.
- The VWRA run's whole-fund base was 6.30%/yr (VWRA run, 03_skeptic.md). The ex-US sleeve's higher 7.26% comes from the lower starting P/E and the higher yield, not from a different growth input.
- **In a de-rating (bear), the yield rises, so the US-WHT drag widens** (M2b: 72.3 bp).

### Model output (verbatim, `python3 reports/runs/VXUS_2026-10-13/02_model.py`)
```

======================================================================================
0. INPUTS & TAPE CHECK
======================================================================================
Price 2026-10-13 close              84.52 USD  [facts]; 00_inputs intraday 84.405 (-0.14%) -> close used
NAV (date unstated)                 84.58 USD  price/NAV -0.07% indicative only
12m price / total return          +15.35% / +18.30%  [facts]
Fund P/E (factsheet 2026-06-30)     18.30x  index 18.2x; yfinance 16.14x [fundamentals.json]
P/B 2.3x  factsheet ROE 13.3%  factsheet EPS growth 12.6% (backward-looking)
TTM distributions                   1.985 USD -> yield 2.349%  [facts]
CY2025 distributions                2.399 USD -> 2.838% on today's price
Q1-Q3 distributions 2026 vs 2025    0.622 vs 1.036 (-40.0%)
TER VXUS / VWRA / IE ex-US UCITS 0.05% / 0.14% / 0.12%  [facts]
Foreign tax paid (2024)             7.48% of cash dividends; foreign-source 88.66% of Box 1a [facts]
US NRA WHT (s.871(a))                 30%  on 100% of the RIC dividend (US-source, dossier §8)
rf 10y 5.22% (FRED DGS10 2026-10-08); ERP 5%; beta raw None -> beta used 1.00 (no vendor beta); k = max(8%, rf + beta*ERP) = 10.22%
SGDUSD 0.7812 [00_inputs]; data warnings: ['fund/ETF: operating-company metrics do not apply']; errors: []
Tape: earnings yield 1/PE 5.46% vs 10y UST 5.22% -> gap +0.24% (yfinance P/E basis 6.19%, gap +0.97%)

======================================================================================
1. LOOK-THROUGH (M1)
======================================================================================
Earnings yield 1/PE                 5.46%
Look-through ROE = PB/PE           12.57%  (factsheet ROE 13.3%); vs k 10.22% spread +2.35%
Gross underlying DY = DYdist*(1+f)+TER   2.574%  (DYdist 2.349%, f 7.48%, TER 0.05%)
Source-country WHT, % of NAV       0.176%  = f x DYdist
Payout = DY_gross x PE             47.11%
Sustainable g envelope              2.89% (all buybacks at E/P)  to 6.65% (all reinvested at ROE_LT)
  with factsheet ROE 13.3%: upper 7.03%
peg_is_valid(PE=18.3, fwd=None, growth=0.126) -> True, 'ok'  [FUND: PEG not used; growth is backward-looking]
Lynch ratio (informational, backward growth): (12.6 + 2.35) / 18.3 = 0.82
CAPE of ex-US index: UNKNOWN (not in dossier)
Top-10 sum 15.0% (factsheet 15.0%); of which semis/semicap (TSMC, Samsung, SK hynix, ASML) 10.8%
VWRA ex-US share 38.32% -> US$ of VWRA needed per US$1 of ex-US exposure 2.61 (brings US$1.61 of US equity with it): VWRA does NOT replicate an ex-US tilt

======================================================================================
2. COST & TAX WATERFALL on the same ex-US exposure (bp/yr of NAV)
======================================================================================
vehicle                        TER  src WHT   US WHT   TOTAL  vs VXUS-SG
VXUS, pre-investor-tax         5.0     17.6      0.0    22.6        70.5
VXUS, Singapore holder         5.0     17.6     70.5    93.0         0.0
VWRA ex-US sleeve             14.0     17.6      0.0    31.6        61.5
IE ex-US UCITS (0.12%)        12.0     17.6      0.0    29.6        63.5
Annual drag difference: VXUS-SG minus VWRA sleeve = 61.5 bp; minus IE ex-US UCITS = 63.5 bp
Of which US 30% WHT 70.5 bp, TER advantage of VXUS -9.0 bp (vs VWRA) / -7.0 bp (vs IE ex-US)
Source-country WHT (17.6 bp) is unusable for a SG holder in EVERY wrapper; base assumes the Irish funds suffer the same rate (UNKNOWN) -> 0 bp differential. A US taxpayer recovers it via the FTC.
Effective total tax on underlying dividends (pre-TER): VXUS-SG 34.9% vs Irish wrapper 7.0%
Breakevens: VXUS-SG = VWRA sleeve if effective US WHT <= 3.83% or distribution yield <= 0.300%; vs IE ex-US: WHT <= 2.98% or yield <= 0.233%
iShares two-fund (World ex-USA 0.15% + EM IMI 0.18%): blended TER 0.15%-0.18% (weights UNKNOWN) -> drag diff 57.5-60.5 bp

======================================================================================
3. 10-YEAR SCENARIOS (M2, nominal USD, additive decomposition as in the VWRA run)
======================================================================================
Exit P/E rule (VWRA-comparable): bear = justified(k 8%, g 2%, ROE 12.57%) = 14.29x; bull = justified(k 8%, g 5%) = 21.08x; base = no re-rating
      DYdist  EPS g  PE10   v/yr DYgross  gross |  pre-tax VXUS-SG VWRAslv  IE xUS | diff bp ERP SG ERP VW
Bear   2.35%  3.00%  14.3 -2.44%   2.57%  3.06% |    2.84%   2.13%   2.75%   2.77% |    61.5 -3.09% -2.47%
Base   2.35%  5.00%  18.3  0.00%   2.57%  7.57% |    7.35%   6.64%   7.26%   7.28% |    61.5 +1.42% +2.04%
Bull   2.35%  6.65%  21.1  1.43%   2.57% 10.75% |   10.53%   9.82%  10.44%  10.46% |    61.5 +4.60% +5.22%
Base composition (VXUS-SG): DYgross 2.57% + EPS g 5.00% + re-rating 0.00% - TER 0.05% - source WHT 0.18% - US WHT 0.70% = 6.64%
Base composition (VWRA sleeve): DYgross 2.57% + 5.00% + 0.00% - TER 0.14% - source WHT 0.18% = 7.26%

======================================================================================
3b. 10-YR WEALTH per US$10,000 (and per S$10,000 at constant spot FX 0.7812)
======================================================================================
        VXUS-SG  VWRA slv    IE xUS   pre-tax |  VW-SG $ IE-SG $ VW-SG % |  VW-SG S$ |  HEV SG HEV VW
Bear     12,352    13,116    13,141    13,231 |      764     789   6.18% |       764 |   39.45  41.89
Base     19,027    20,152    20,190    20,322 |    1,125   1,163   5.91% |     1,125 |   60.77  64.37
Bull     25,524    26,988    27,037    27,209 |    1,465   1,514   5.74% |     1,465 |   81.53  86.21
S$ column: a S$10,000 stake = US$7,812; at constant FX the S$ gap equals the US$ gap per 10,000 units (FX drift UNKNOWN, identical for both USD wrappers, so the DIFFERENCE is FX-neutral).
SGD holder: USD/SGD drift UNKNOWN; each +/-1%/yr of USD move scales the absolute 10-yr SGD outcome by x1.105 / x0.904 for BOTH wrappers
Lost wealth from the drag alone (base): 5.58% of the VWRA-sleeve outcome over 10y; 6.37% vs a holder with no investor-level tax
HEV = price at which the scenario earns exactly k 10.22%; NOT a fair value (NAV is). Terminal share 100% by construction.
Base implied ERP: VWRA sleeve +2.04%, VXUS-SG +1.42% -> the 61.5 bp drag consumes 30% of the ex-US equity premium

======================================================================================
4. CROSS-CHECK (M2b): year-by-year, yield moves with the P/E path, dividends grow with EPS
======================================================================================
Bear  VXUS-SG  2.39%  VWRA sleeve  3.11%  IE xUS  3.13%  diff  72.3 bp /  74.3 bp   10y wealth gap per US$10k    923 /    949
Base  VXUS-SG  6.73%  VWRA sleeve  7.38%  IE xUS  7.40%  diff  65.0 bp /  67.0 bp   10y wealth gap per US$10k  1,200 /  1,238
Bull  VXUS-SG  9.83%  VWRA sleeve 10.44%  IE xUS 10.46%  diff  61.5 bp /  63.5 bp   10y wealth gap per US$10k  1,467 /  1,516

======================================================================================
5. REVERSE SOLVES ('what must be true?')
======================================================================================
(a) per-share EPS growth needed for the after-tax net return to hit a target (base yield, costs)
  UST 5.22% (ERP 0) :  14.3x SG 6.16% VW 5.53% |  16.1x SG 4.88% VW 4.26% |  18.3x SG 3.58% VW 2.96% |  21.1x SG 2.11% VW 1.51%
  UST + 3%          :  14.3x SG 9.24% VW 8.61% |  16.1x SG 7.92% VW 7.30% |  18.3x SG 6.58% VW 5.96% |  21.1x SG 5.07% VW 4.46%
  UST + 4%          :  14.3x SG 10.26% VW 9.63% |  16.1x SG 8.93% VW 8.31% |  18.3x SG 7.58% VW 6.96% |  21.1x SG 6.06% VW 5.45%
  CAPM k 10.22%     :  14.3x SG 11.29% VW 10.66% |  16.1x SG 9.95% VW 9.32% |  18.3x SG 8.58% VW 7.96% |  21.1x SG 7.04% VW 6.44%
  -> holding VXUS instead of the VWRA sleeve needs ~0.61%/yr more EPS growth for the same outcome
(b) perpetual nominal growth implied by P/E 18.3x (value-driver, payout = 1 - g/ROE)
  k= 8.00%: ROE 10.00% -> g  5.29%  ROE 12.57% -> g  4.22%  ROE 13.30% -> g  4.04%  ROE 16.00% -> g  3.62%
  k= 9.22%: ROE 10.00% -> g  8.09%  ROE 12.57% -> g  6.34%  ROE 13.30% -> g  6.07%  ROE 16.00% -> g  5.41%
  k=10.22%: ROE 10.00% -> g 10.21%  ROE 12.57% -> g  8.14%  ROE 13.30% -> g  7.77%  ROE 16.00% -> g  6.90%
  k=11.22%: ROE 10.00% -> g 11.21%  ROE 12.57% -> g  9.98%  ROE 13.30% -> g  9.52%  ROE 16.00% -> g  8.41%
  terminal-growth cap = min(4%, 10y 5.22%) = 4%
(c) market-implied perpetual k at 18.3x (ROE_LT 12.57%): g 3% -> k  7.28% (ERP +2.06%)  g 4% -> k  7.87% (ERP +2.65%)

======================================================================================
6. SENSITIVITY (M3, index level, pre-investor-tax): value/share = price x justified PE / 18.3  (ROE 12.57%)
======================================================================================
k \ g                2%        3%        4%        5%    (5% column exceeds the 4% cap; reference only)
8.00%             66.02     72.43     81.87     97.34 (VWRA-run comparability)
9.22%             54.87     58.23     62.73     69.20
10.22%            48.19     50.16     52.65     55.94
11.22%            42.96     44.06     45.35     46.95
justified P/E:
8.00%             14.3x     15.7x     17.7x     21.1x
9.22%             11.9x     12.6x     13.6x     15.0x
10.22%            10.4x     10.9x     11.4x     12.1x
11.22%             9.3x      9.5x      9.8x     10.2x

======================================================================================
7. 10-YR AFTER-TAX NET RETURN GRID, VXUS-SG (M2): exit P/E x per-share EPS growth; [VWRA-sleeve = +diff]
======================================================================================
g \ exitPE       14.3x     16.1x     18.3x     21.1x     24.0x
2.00%            1.16%     2.37%     3.64%     5.11%     6.45%
3.00%            2.13%     3.36%     4.64%     6.12%     7.48%
4.00%            3.11%     4.35%     5.64%     7.14%     8.50%
5.00%            4.09%     5.34%     6.64%     8.15%     9.53%
6.00%            5.06%     6.32%     7.64%     9.16%    10.56%
6.65%            5.70%     6.96%     8.29%     9.82%    11.23%

======================================================================================
8. SWEEPS on the DRAG DIFFERENTIAL (VXUS-SG minus VWRA sleeve, base) and VXUS-SG base net
======================================================================================
  base                                                    diff   61.5 bp   VXUS-SG net  6.64%   10y gap/US$10k  1,125
  yield 2.84% (CY2025 dists on today's price)             diff   76.2 bp   VXUS-SG net  6.99%   10y gap/US$10k  1,444
  yield -10% (2.11%)                                      diff   54.4 bp   VXUS-SG net  6.48%   10y gap/US$10k    980
  10% of payout s.871(k)-exempt (HYPOTHETICAL)            diff   54.4 bp   VXUS-SG net  6.71%   10y gap/US$10k    999
  25% of payout s.871(k)-exempt (HYPOTHETICAL)            diff   43.8 bp   VXUS-SG net  6.82%   10y gap/US$10k    809
  30% also withheld on s.853 FTC gross-up (UNKNOWN)       diff   66.7 bp   VXUS-SG net  6.59%   10y gap/US$10k  1,219
  Irish source WHT 50% higher than VXUS's (UNKNOWN)       diff   52.7 bp   VXUS-SG net  6.64%   10y gap/US$10k    961
  Irish source WHT 50% lower than VXUS's (UNKNOWN)        diff   70.2 bp   VXUS-SG net  6.64%   10y gap/US$10k  1,291
  VXUS expenses NOT paid from income                      diff   61.5 bp   VXUS-SG net  6.59%   10y gap/US$10k  1,121
  vehicle cost = TD: VXUS 10y TD 0.00, VWRA mean cal. TD  diff   68.1 bp   VXUS-SG net  6.69%   10y gap/US$10k  1,256
  vehicle cost = TD: VXUS 5y TD +0.14 (beat index)        diff   54.1 bp   VXUS-SG net  6.83%   10y gap/US$10k  1,004
  vs IE ex-US UCITS 0.12% instead of VWRA                 diff   63.5 bp   VXUS-SG net  6.64%   10y gap/US$10k  1,163
  vs IE ex-US + 0.10% unknown TD residual                 diff   53.5 bp   VXUS-SG net  6.64%   10y gap/US$10k    976
  small-cap return gap +/-0.10%/yr (UNKNOWN), per 0.10    diff   51.5 bp   VXUS-SG net  6.64%   10y gap/US$10k    938
  VWRA calendar TD mean 2020-25 = -0.023 pp (fund-benchmark); VXUS TD 1/3/5/10y = +0.68/+0.13/+0.14/+0.00 pp vs a WHT-adjusted index. Benchmarks' WHT bases differ, so TD rows are indicative only.

======================================================================================
9. ONE-OFF SWITCH COST PAYBACK and $ drag (switch costs UNKNOWN; HYPOTHETICAL grid)
======================================================================================
  one-off cost    10 bp -> payback  0.16 yrs vs VWRA sleeve,  0.16 yrs vs IE ex-US
  one-off cost    25 bp -> payback  0.41 yrs vs VWRA sleeve,  0.39 yrs vs IE ex-US
  one-off cost    50 bp -> payback  0.81 yrs vs VWRA sleeve,  0.79 yrs vs IE ex-US
  one-off cost   100 bp -> payback  1.63 yrs vs VWRA sleeve,  1.58 yrs vs IE ex-US
  annual US WHT paid per US$10,000 of VXUS at today's yield: US$70.46; net drag vs VWRA sleeve: US$61.46
  Estate: VXUS is US-situs (dossier §8). Form 706-NA if US-situs > US$60,000; credit US$13,000. Rate schedule UNKNOWN, position size UNKNOWN, aggregate US-situs holdings UNKNOWN -> not in the bp figures.

======================================================================================
10. LOAD-BEARING INPUTS (+/-10%, one at a time, everything else fixed)
======================================================================================
(a) on VXUS-SG base after-tax net 6.64% and HEV 60.77 (k 10.22%)
  exit P/E (yr 10)         -10%: net  5.54% HEV  54.79 ( -9.9%)   +10%: net  7.65% HEV  66.75 ( +9.8%)
  per-share EPS growth     -10%: net  6.14% HEV  57.98 ( -4.6%)   +10%: net  7.14% HEV  63.68 ( +4.8%)
  distribution yield       -10%: net  6.48% HEV  59.84 ( -1.5%)   +10%: net  6.81% HEV  61.72 ( +1.6%)
  US WHT rate              -10%: net  6.71% HEV  61.18 ( +0.7%)   +10%: net  6.57% HEV  60.37 ( -0.7%)
  TER (VXUS)               -10%: net  6.65% HEV  60.80 ( +0.0%)   +10%: net  6.64% HEV  60.75 ( -0.0%)
  hurdle k  9.20%            HEV  66.71 ( +9.8%)  net unchanged
  hurdle k 11.24%            HEV  55.42 ( -8.8%)  net unchanged
  starting P/E measurement 18.3x -> 16.14x (exit follows definition): base  6.64% (unchanged); bear (absolute 14.3x exit)  3.40% vs  2.13%
  ROE_LT -10% (M3)         M3 value  49.92 ( -5.2%) vs centre 52.65 (k 10.22%, g 4%)
  ROE_LT +10% (M3)         M3 value  54.88 ( +4.2%) vs centre 52.65 (k 10.22%, g 4%)
  terminal g 3.6% (M3)     M3 value  51.58 ( -2.0%) vs centre 52.65 (k 10.22%, g 4%)
  terminal g 4.4% (M3)     M3 value  53.84 ( +2.3%) vs centre 52.65 (k 10.22%, g 4%)
(b) on the DRAG DIFFERENTIAL, base 61.5 bp (vs VWRA sleeve)
  distribution yield       -10%:   54.4 bp   +10%:   68.5 bp
  US WHT rate              -10%:   54.4 bp   +10%:   68.5 bp
  TER VWRA                 -10%:   62.9 bp   +10%:   60.1 bp
  TER VXUS                 -10%:   61.0 bp   +10%:   62.0 bp
  Irish source-WHT ratio   -10%:   63.2 bp   +10%:   59.7 bp
  EPS growth               -10%:   61.5 bp   +10%:   61.5 bp
  exit P/E                 -10%:   61.5 bp   +10%:   61.5 bp
  (additive M2 holds the yield constant, so exit P/E and EPS growth leave the bp gap unchanged; M2b §4 shows the de-rating path raises the gap)
```

## F. Reverse solve & sensitivity grid
**Reverse, 10-yr (output §5a):** the per-share EPS growth needed for the **after-tax** return to reach a target.

| Target | Exit 14.3x | Exit 16.1x | Exit 18.3x (no re-rating) | Exit 21.1x |
|---|---|---|---|---|
| = UST 5.22% (ERP 0) | SG 6.16% / VW 5.53% | 4.88% / 4.26% | **3.58% / 2.96%** | 2.11% / 1.51% |
| = UST + 4% | 10.26% / 9.63% | 8.93% / 8.31% | **7.58% / 6.96%** | 6.06% / 5.45% |
| = CAPM k 10.22% | 11.29% / 10.66% | 9.95% / 9.32% | **8.58% / 7.96%** | 7.04% / 6.44% |

- **What must be true:** at a constant 18.3x, ex-US per-share EPS must compound at **3.58%/yr** just for a Singapore holder of VXUS to match a 10y Treasury. The same exposure inside an Irish wrapper needs 2.96%.
- Earning a 4% premium needs 7.58%, which is **above the computed sustainable envelope of 6.65%**. Through VWRA's wrapper it needs 6.96%.
- Holding VXUS rather than the VWRA sleeve needs about **0.61 pp/yr more EPS growth** for the same outcome.

**Tax "what must be true" (output §2).** VXUS-SG matches the VWRA sleeve only if one of these holds:
- the effective US WHT is **≤ 3.83%** (statute: 30%); or
- the distribution yield is **≤ 0.300%** (actual: 2.35%).

Against the Irish ex-US UCITS the thresholds are ≤ 2.98% and ≤ 0.233%. Neither is close.

**Reverse, perpetual (output §5b–c), index level:**
- At 18.3x with the look-through ROE of 12.57%, the implied perpetual nominal growth is 4.22% at k 8% and **8.14% at k 10.22%**. The k 10.22% figure is far above the 4% cap = min(4%, 5.22%).
- The market-implied perpetual k at g 3–4% is **7.28–7.87%**, an implied ERP of **+2.06% to +2.65%** before investor tax. The VWRA run gave +2.58% at g 4% (VWRA run, 03_skeptic.md).

**Sensitivity grid (M3, output §6), value per share at ROE 12.57%:**
- At k 10.22% / g 4%: **52.65** (justified P/E 11.4x).
- Across k 9.22–11.22% × g 2–4%, values run from 42.96 to 62.73.
- The k = 8% row is shown for VWRA comparability: 66.02 to 81.87 at g 2–4%.
- Every value within the 4% cap (g ≤ 4%) is below the 84.52 price. As in the VWRA run, the index is priced for a lower k than CAPM's 10.22%.
- This grid is pre-investor-tax, at index level. It is not an argument about the wrapper.

**After-tax return grid (output §7), VXUS-SG:** from 1.16% (g 2%, exit 14.3x) to 11.23% (g 6.65%, exit 24x). The VWRA sleeve is the same cell plus about 61.5 bp.

## G. Load-bearing inputs
**(a) On the VXUS-SG base after-tax return (6.64%) and HEV (60.77), ±10% one at a time (output §10a):**
| # | Input | Base | Source | −10% | +10% |
|---|---|---|---|---|---|
| 1 | Exit P/E yr 10 | 18.3x | ASSUMPTION (no re-rating) | 5.54%, HEV 54.79 (−9.9%) | 7.65%, HEV 66.75 (+9.8%) |
| 2 | Hurdle k (HEV only) | 10.22% | CAPM, 00_inputs | HEV +9.8% | HEV −8.8% |
| 3 | Per-share EPS growth | 5.0% | ASSUMPTION | 6.14% (−4.6%) | 7.14% (+4.8%) |
| 4 | Distribution yield | 2.35% | facts (TTM) | 6.48% (−1.5%) | 6.81% (+1.6%) |
| 5 | US WHT rate | 30% | facts (871(a)) | 6.71% (+0.7%) | 6.57% (−0.7%) |
| 6 | Look-through ROE (M3) | 12.57% | P/B ÷ P/E, dossier §2 | M3 −5.2% | M3 +4.2% |
| 7 | Terminal g (M3) | 4% | cap | M3 −2.0% | M3 +2.3% |
| 8 | Starting P/E *measurement* (18.3x → 16.14x yfinance; exit follows the definition) | 18.3x | dossier vs fundamentals.json | base unchanged (6.64%) | bear 2.13% → 3.40% (the absolute 14.3x exit becomes a smaller de-rating) |
| 9 | TER (VXUS) | 0.05% | facts | ±0.0% | – |
| 10 | USD/SGD drift | UNKNOWN | – | same for both wrappers. The gap is FX-neutral; absolute SGD outcome ×1.105 / ×0.904 per ±1%/yr (output §3b) | – |

**(b) On the decisive quantity, the drag gap vs the VWRA sleeve (61.5 bp, output §8 and §10b):**
| # | Input | Base | Source | Effect |
|---|---|---|---|---|
| 1 | Distribution yield | 2.35% | facts | ±10% → 54.4 / 68.5 bp. At the CY2025 level of 2.84%: **76.2 bp** |
| 2 | US WHT rate / 871(k)-exempt share | 30% / 0% | facts / UNKNOWN | ±10% rate → 54.4 / 68.5 bp. 10% exempt → 54.4 bp. 25% exempt → 43.8 bp |
| 3 | Irish vs US source-country WHT | equal | UNKNOWN | Irish +50% → 52.7 bp. Irish −50% → 70.2 bp |
| 4 | Path / de-rating (M2b) | – | ASSUMPTION | bear 72.3 bp, base 65.0, bull 61.5 |
| 5 | 30% also applied to the §853 FTC gross-up | no | UNKNOWN | 66.7 bp |
| 6 | Vehicle cost as TD instead of TER | TER | facts | VXUS 10y TD 0.00 → 68.1 bp. VXUS 5y TD +0.14 → 54.1 bp (benchmarks' WHT bases differ, indicative only) |
| 7 | Comparator | VWRA 0.14% | facts | IE ex-US 0.12% → 63.5 bp. With +0.10% unknown TD → 53.5 bp. iShares pair → 57.5–60.5 bp |
| 8 | Small-cap return gap (all-cap vs large+mid) | 0 | UNKNOWN | each 0.10 pp/yr → ∓10 bp |
| 9 | TER VWRA / TER VXUS | 0.14% / 0.05% | facts | ±10% → about ±1.4 / ±0.5 bp |
| 10 | Exit P/E, EPS growth | – | ASSUMPTION | 0 bp in M2 (the gap does not depend on market outcomes, except through the yield path) |

**Bottom line of G.**
- Market inputs (exit P/E, growth, k) dominate the *level* of return.
- The *wrapper gap* depends almost entirely on **yield × effective WHT rate**. Across every swept UNKNOWN, the gap stays between **43.8 and 76.2 bp/yr** in favour of the Irish wrapper.
- **No swept case comes close to the 0 bp breakeven.**
- One-off switching costs (UNKNOWN; hypothetical grid in output §9) pay back in **0.16 years at 10 bp** and **1.63 years at 100 bp**.

## H. Open questions for the Skeptic
1. **Actual withholding by IBKR on VXUS distributions for a Singapore W-8BEN holder** (dossier UNKNOWN #6). The statute says 30% on the whole RIC dividend, and that is the single largest input to the gap. Any 871(k) short-term-gain or interest-related designation (UNKNOWN #5) lowers it: 25% exempt still leaves 43.8 bp.
2. **Is the 2.35% TTM yield representative?** CY2025 was 2.84% on today's price, while Q1–Q3 2026 payouts were 40% below Q1–Q3 2025. The gap scales 1:1 (54–76 bp across 2.11–2.84%). The cause of the 2026 drop is UNKNOWN.
3. **Source-country WHT parity.** I assumed an Irish UCITS suffers the same source-country rates on Japanese, Taiwanese, Korean, Swiss and other dividends as a US RIC (UNKNOWN). ±50% moves the gap 52.7–70.2 bp. Is any treaty asymmetry large enough to matter? The 7.48% is a 2024 figure, applied to 2025–26 payouts.
4. **§853 pass-through for a non-US holder.** Does the withholding agent apply 30% to the grossed-up dividend (including the foreign tax passed through)? If so, the gap rises to 66.7 bp (output §8). Not in the dossier.
5. **Estate tax is outside the bp figures.** VXUS is US-situs (2104(a); 2105(d) look-through ended 2011). The threshold is US$60,000 and the credit US$13,000 (facts). The rate schedule, the position size, and the user's **aggregate** US-situs holdings are all UNKNOWN. The investor-profile memory, not re-verified, lists several US-domiciled direct stocks, so the threshold test is portfolio-wide, not VXUS-only. This is an unquantified tail cost that may be larger than the 10-yr drag, and it should be sized.
6. **The substitute is new.** IE0009A5ADV9 launched 2026-08-18 with US$35M TNA, TD UNKNOWN, and large+mid only (2,340 stocks vs 8,755). Closure, spread and liquidity risk are UNKNOWN. The Dist class and its OCF are [SNIPPET] only. Is the iShares developed + EM pair (57.5–60.5 bp better) the more robust substitute despite a different index family?
7. **Role:** is the ex-US tilt intended? If not, the choice isn't "VXUS vs an Irish ex-US fund" but "VXUS vs more VWRA", which changes the exposure (US$1.61 of US per US$1 ex-US). That is an allocation question for the orchestrator, not a valuation input.
8. **P/E definition.** Factsheet 18.3x (dated 2026-06-30; price drift since then UNKNOWN) vs yfinance 16.14x. This moves only the bear case (2.13% → 3.40%). The base is unchanged because the exit follows the same definition.
9. **Base exit at 18.3x with no re-rating** sits well above the M3 justified 10.4–11.4x (g 2–4%) at the sourced k of 10.22%. This is the same tension the VWRA Skeptic raised (rf above E/P there; here E/P is only 0.24 pp above rf).
10. **Singapore tax on the net VXUS distribution** is assumed to be 0 (not in the dossier). Any SG tax would add to the VXUS-SG drag only.
11. **Switching frictions** (commission, spread, any tax on disposal) are UNKNOWN. The payback grid is hypothetical.
