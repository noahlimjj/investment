<!-- pipeline:value-quant -->
# Quant model: NVO (as of 2026-10-13)

Template: **FULL** (profitable operating pharma; ADR, 1 ADR = 1 B share). Model: `02_model.py` (executed; every number below is printed by it unless tagged with a source).
Price of record **USD 38.415** (00_inputs, intraday 13:52Z) = **DKK 256.56** per ADR at DKKUSD 0.149734 (00_inputs). Close USD 38.015 (fj) = DKK 253.88; both are shown where it matters.
Model currency DKK (IFRS reporter); USD per ADR = DKK x 0.149734.
Data-layer warnings (fj, 1): "forward P/E (11.5) > trailing (9.3): earnings are declining, so PEG=4.36 is meaningless - VOID, use FCF yield / DCF". Errors: none.
Tape: -33.9% over 12 months, -68% from the Oct-2024 peak (dossier S1). Trailing P/E is 9.3 on the vendor number, but that number is flattered by the DKK 26.8bn non-cash 340B reversal. Normalised P/E is 11.9; forward is 11.5. The tape is pricing flat-to-falling earnings, and the model below agrees: the question is how far they fall and for how long.

Treatments (stated once, applied throughout):
- **Base period** FY2025 (31 Dec 2025), put on an "adjusted-equivalent" basis: reported minus the 340B reversal plus impairments. This is exactly the definition the company's H1-26 adjusted EBIT reconciles to: 86,679 - 26,760 + 6,328 = 66,247 (MATCH). Adjusted FY2025: revenue 306,464; EBIT 132,374 (43.2%); EBITDA 147,040.
- **Valuation date** `dcf(mid_year=True, stub_years=0.7830)` (31 Dec 2025 to 13 Oct 2026). Because the rolled-forward EV contains all FY2026 FCF, the bridge deducts Dec-25 net debt (104,494) **plus every distribution paid since** (FY25 final dividend 35,312, 2026 interim 16,549, 2026 buybacks 10,559), giving claims of 166,914 = DKK 37.82/share. Share count is the current 4,413.1m (6-K, 9 Oct 2026). Reconciliation: Dec-25 ND + H1 distributions (145,705) - Jun-26 ND (95,145) = 50,560 of H1 cash generation, against company H1 FCF of 55.3bn.
- **IFRS 16**: leases are kept **in** net debt, using the reported Borrowings line, which dossier S1 infers includes leases (UNCONFIRMED). FCF is pre-lease, so lease principal (FY25 1,503) is never deducted. If leases sit outside Borrowings: -1.94 DKK/share.
- **SBC**: deduct method. IFRS 2 expenses SBC inside EBIT, the model never adds it back, and the share count is held flat. SBC is 0.46% of FY25 revenue.
- **Acquired intangibles**: Akero (FY25 purchase of intangibles 29,973) is treated as **M&A, not maintenance capex** (orchestrator note). Instead, every year carries a recurring BD/in-licensing charge of **1.45% of revenue**, the median of FY21-24 intangibles purchased / revenue. `acq_amort_pct` is **not** used: D&A is 0.24x capex, the opposite of the acquisition-heavy case.
- **FY2026 cash** is calibrated to the FY26 FCF guidance (OCF - PP&E capex, 45-55bn) through an explicit "cash gap" line (base 8,113 = 2.76% of revenue). It covers WC, cash-tax timing and restructuring. Guidance implies H2-26 FCF of -10.3 to -0.3bn after the 55.3bn earned in H1.

## A. Lynch classification & category checks

**Actual growth.** Revenue CAGR FY20-25 was **19.5%** (facts `revenue_cagr`); FY25 revenue grew +6.4%. Diluted EPS CAGR FY21-25 was **22.1%** = (23.03/10.37)^(1/4) - 1 (facts `eps_diluted`). On a split-adjusted basis FY20-25 it was 20.7% (FY20 EPS 18.01 is pre-split; dossier S10.4). FY25 EPS growth was **+1.8%**. FY26 guidance is adjusted operating profit 0% to -6% at CER (dossier S3). CONSENSUS EPS CAGR FY25-27 is **-2.06%** (dossier S9, labelled).

**Classification: former Fast Grower, now a Slow Grower on forward evidence. The category is changing.** Five years of 20%+ EPS growth put it squarely in Fast Grower. The forward evidence (FY25 EPS +1.8%, FY26 guided profit decline, the 1 Jan 2027 WAC cut of ~35-50%, semaglutide LOE already in Canada/Brazil) puts near-term EPS growth below 5% and negative. Lynch's warning applies: the fast-to-slow transition is when the multiple de-rates, and the -68% from peak is that de-rate. It is **not Cyclical**, because the price reset is structural (policy, patents, competition) and not demand-cyclical. It is **not a Turnaround**, because the company is rated Aa3/AA, interest cover is 18.8x and ROIC is 34%. It could re-qualify as a Stalwart if the CMD ambition is met ("2026-30 revenue CAGR in line with industry peers", "broadly stable operating margin"), but that ambition has no number attached and is not guidance.

**Slow-grower checks (dividend):**
- FY25 DPS DKK 11.70 (interim 3.75 + final 7.95). Payout 50.7% (company). EPS cover **1.97x**.
- FY25 cash cover: dividends paid 51,763 vs OCF - PP&E capex 58,962 = **1.14x**; vs company FCF 28,295 = **0.55x**.
- 2026 cash cover: dividends paid 51,861 vs guided FCF midpoint 50,000 = **0.96x**. Adding the DKK 15bn buyback programme gives distributions of 66,861 against FCF of 50,000, a **shortfall of 16,861 that is funded with debt**. Borrowings went 26,645 (FY21) to 130,958 (FY25) to 140,127 (Jun-26).
- Record: FY24 DPS 11.40 to FY25 11.70 (+2.6%). The longer split-consistent DPS record is UNKNOWN (dossier S5 mixes pre- and post-split bases). CMD: "Maintain an attractive dividend per share".

**Fast-grower checks (to explain the transition):**
- Runway still exists in volume: IQVIA branded obesity market volume +81%, International Operations obesity +37% CER in Q2.
- But price is falling faster than volume grows: US Wegovy injectable -22% CER in Q2, US adjusted sales -4% CER in H1, LOE price erosion in Canada.
- Growth was **not internally funded** in FY24-25. Capex, M&A and dividends exceeded OCF (dossier S5), and borrowings went from 26,645 (FY21) to 130,958 (FY25).

**Stalwart checks:** P/E vs its own 5-yr range is UNKNOWN (the dossier has no FX-matched historical price series). On diworsification: Catalent sites (DKK 82,163m, manufacturing, core) and Akero (USD 4.7bn plus a USD 0.5bn CVR, MASH, an adjacent metabolic Phase 3 asset) are both in or near the core. The Rare disease segment ran a Q2 operating loss of DKK 1,295m.

**Lynch metrics (formulas shown):**

| Metric | Formula / inputs | Value |
|---|---|---|
| EPS used | TTM 26.20 - 26,760 x (1-22%) / 4,441m (340B reversal stripped; reversal assumed taxed at 22%, its tax treatment is UNKNOWN) | **21.50** |
| P/E (normalised) | 256.56 / 21.50 | **11.93x** |
| PEG | `peg_is_valid(11.93, 11.47, -2.06%)` uses the lower of historical 22.1% and CONSENSUS -2.06% | **VOID** (growth <= 0). Not cited. |
| Lynch ratio | (EPS growth % + div yield %) / P/E = (-2.1 + 4.56) / 11.93 | **0.21** (poor; < 1). Historical growth would give 2.23, but the rule takes the lower growth. |
| Dividend yield | (7.95 + 3.75) / 256.56 | 4.56% (vendor ADR rate USD 1.80 gives 4.69%) |
| Net-cash-adj P/E | (P - net cash/share) / EPS = (256.56 - (-21.56)) / 21.50 | **12.94x** (Jun-26 ND 95,145); 13.16x on the Oct-26 ND estimate of 116,354 |
| Inventory vs sales | facts derived | FY25 **+15.1pt** (inventories +21.5% vs sales +6.4%; write-downs 4,272 vs 2,660, dossier S2). **Red flag.** FY24 +3.4pt. |
| Receivables vs sales | trade receivables growth - sales growth | FY25 -7.9pt (fine). **H1-26 receivables +25.5% vs Dec-25** (88,949 vs 70,856) against H1 adjusted sales +2% CER. **Red flag**; cause UNKNOWN. |
| Debt | ND / owner earnings | Jun-26 ND / OE ex-M&A = **1.67x**; vs fj OE 3.53x; ND / FY25 adj EBITDA 0.65x; current borrowings 18,333 vs cash 44,482 (2.4x cover). **Maturity wall UNKNOWN.** Aa3/AA. |

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence / predictability: NO for a 10-year sketch; PARTLY for FY2026 only.** Reasons:
1. At least **68.9%** of Q2-26 adjusted sales come from one molecule: Ozempic 31,375 + Wegovy injectable 19,484 + Wegovy pill 3,218 = 54,077 of 78,488. Rybelsus is not broken out, so this is a floor.
2. Semaglutide LOE dates for the US, EU, China and India are **UNKNOWN** in the dossier. A US Paragraph IV suit is pending and an EU UPC revocation action has been filed.
3. The US net price after the 2027 WAC cut is UNKNOWN, and 2027 guidance is not given until Feb 2027.
4. The pipeline is binary (CagriSema US decision Q4-26; ziltivekimab ZEUS failed).

The model's own dispersion confirms it: FY2035 revenue is **2.06x** apart between bull (414,842) and bear (201,753). This belongs in the "too hard" pile for point estimates. The valuation leans on ranges and on the reverse DCF.

**Moat evidence (facts.json series):**
- Gross margin FY20-25: 83.5 / 83.2 / 83.9 / 84.6 / 84.7 / **81.0%**. Q2-26 adjusted **78.2%** vs 82.7% a year earlier, now below the 5-yr low of 81.0%. Stable through FY24 and **eroding since FY25**.
- EBIT margin FY20-25: 42.6 / 41.7 / 42.3 / 44.2 / 44.2 / 41.3%. 5-yr average 42.7%, low 41.3%.
- ROIC FY20-25: **70 / 55 / 62 / 69 / 44 / 34%**, 5-yr average 52.7%. It has always been far above WACC, but it is falling: invested capital rose **4.86x** FY20-25 while NOPAT rose only **2.33x** (42,928 to 100,173).
- Capital intensity: PP&E capex / revenue went 4.6% to **19.5%**; capex / D&A was 1.85 / 3.54 / 5.52 / 4.10 for FY22-25. A capex super-cycle on top of the Catalent purchase (FY24 DKK 82,163m).
- Market share: US "market leader among branded obesity medications" by new patient starts (6-K). Still, US Wegovy injectable is -22% CER and US insulin share is declining (dossier S3/S8). Mixed, and eroding in the US injectables franchise.
- **Rating: NARROW, trend ERODING.** Today's returns are still at wide-moat level (ROIC 33.6% even at the FY25 low; GM 81.0% in FY25). What is missing is evidence of durability, and that evidence points the other way: pricing power is visibly breaking (company-initiated 35-50% WAC cuts, MFN, China list-price cuts, LOE price erosion in Canada), gross margin is below its 5-yr low, and the moat's main source is the patent estate on a single molecule, which has a finite life.

**Owner earnings (FY2025, DKK m):**

| Version | Computation | OE | Yield on mcap 1,132,209 |
|---|---|---|---|
| AGENTS.md / fj | NI 102,434 + D&A 14,666 - capex incl. Akero 90,113 | 26,987 | 2.38% (distorted by Akero) |
| Ex-M&A intangibles | 102,434 + 14,666 - PP&E 60,140 | **56,960** | **5.03%** |
| Ex-M&A, less BD allowance | 56,960 - 1.45% x revenue | 52,478 | 4.63% |
| SBC-adjusted (FCF basis) | OCF - PP&E 58,962 - SBC 1,435 | 57,527 | 5.08% |

SBC is already expensed in NI under IFRS 2, so the NI-based versions are SBC-burdened. Lease principal is not deducted because leases are in net debt. FY25 owner earnings are themselves depressed by peak capex (19.5% of revenue). On a steady-state capex of 6% + BD, the FY26 guided FCF would be a **7.34%** yield (model line, ASSUMPTION-driven).

**ROIC vs WACC.**
- FY25 ROIC **33.6%** = EBIT 127,658 x (1 - 21.5%) / (equity 194,047 + borrowings 130,958 - cash 26,464 = 298,541). Adjusted-equivalent: **34.8%**.
- WACC **7.01%** (section D), a spread of about 27 points.
- Goodwill is 6.6% of IC (19,845). That is below the 30% trigger, so ex-goodwill ROIC is not needed (it would be 35.9%).
- Caveats: R&D is expensed, so IC omits the R&D asset and accounting ROIC overstates economic ROIC. ROIC also counts leases inside Borrowings, which is inferred rather than confirmed.
- What matters for the thesis is the trend (70% to 34%) and the terminal ROIC on new money (base 20%), not the level.

## C. GARP & valuation matrix

DKK basis. Market EV = mcap 1,132,209 + Jun-26 ND 95,145 = **1,227,354** (USD 183.8bn). The vendor EV (USD 266bn) and EV/EBITDA (1.5x) mix currencies and are **not used** (dossier S10.1). Peer medians are computed from the dossier S7 vendor values (LLY, AZN, PFE, AMGN, MRK).

| Multiple | Current | 5-yr own average | Peer median |
|---|---|---|---|
| EV/EBITDA (FY25 adjusted EBITDA 147,040) | **8.3x** (8.2x on company EBITDA 149,640) | UNKNOWN | 14.1x |
| P/E trailing, normalised (TTM ex-340B EPS 21.50) | **11.9x** | UNKNOWN | 37.2x (distorted by MRK 112.8 / PFE 37.2 one-offs) |
| P/E trailing, vendor (flattered by 340B) | 9.3x | UNKNOWN | n/a |
| P/E forward (fj) | 11.5x | UNKNOWN | 15.3x |
| P/E on CONSENSUS FY26 / FY27 EPS | 11.4x / 11.6x | UNKNOWN | n/a |
| P/FCF FY25 (OCF - PP&E 58,962) | 19.2x | UNKNOWN | 25.6x (1 / median FCF yield) |
| P/FCF FY25 (company FCF 28,295) | 40.0x | UNKNOWN | n/a |
| P/FCF FY26 (guidance midpoint 50bn) | 22.6x | UNKNOWN | n/a |
| P/FCF SBC-adjusted (FY26 midpoint - FY25 SBC) | 23.3x | UNKNOWN | n/a |
| FCF yield FY26 (guidance midpoint) | **4.42%** | UNKNOWN | 3.9% |
| FCF yield FY26 at steady-state capex (6% + BD) | 7.34% | UNKNOWN | n/a |
| Owner-earnings yield (fj / ex-M&A) | 2.38% / **5.03%** | UNKNOWN | UNKNOWN |
| PEG | **VOID** (not cited) | n/a | n/a |
| Lynch ratio (lower growth) | **0.21** | UNKNOWN | UNKNOWN |
| Dividend yield | 4.56% | UNKNOWN | UNKNOWN |

5-yr own-average column: UNKNOWN throughout, because the dossier has no FX-matched historical price series.

Read: NVO trades well below the peer medians on EV/EBITDA (8.3x vs 14.1x) and forward P/E (11.5x vs 15.3x). On FCF yield it is close to the peer median (4.42% vs 3.9%), because FY26 PP&E capex is still guided at about 55bn. The discount is on earnings, not on cash, until capex normalises.

## D. Discount rate build

| Component | Value | Source |
|---|---|---|
| Risk-free (DKK 10y) | 3.01% | 00_inputs (OECD IRLTLT01DKM156N, monthly average for Aug-26) |
| Beta | raw 0.384; Blume 0.67 x 0.384 + 0.33 = **0.587** | fj `beta` (vendor) |
| ERP | 5.0% | 00_inputs |
| Cost of equity | 3.01% + 0.587 x 5% = **5.95%** | computed |
| Cost of debt, pre-tax | **5.80%** = FY25 interest expense 6,778 / average borrowings 116,872 | facts. The tag may include other finance costs, so this is conservative vs the DKK 10y of 3.01%. Novo's actual bond spread is UNKNOWN. |
| Cost of debt, after tax (22%) | 4.52% | computed |
| Weights (market value; debt at book) | equity 1,132,209 (89.0%); gross borrowings Jun-26 140,127 (11.0%) | computed |
| WACC (CAPM) | **5.79%** | computed |
| Floor (local 10y + 4%) | **7.01%** | 00_inputs rule |
| **WACC used** | **7.01%** (the floor binds) | |

Why DKK: the cash flows are modelled in DKK, and discounting DKK flows at a DKK rate before converting at spot keeps the currency consistent. Translation risk (US sales were 51% of H1-26 adjusted sales) is shown as the DKKUSD sensitivity in G, not loaded into the rate.

Flags:
1. The DKK 10y is **stale-prone**: it is an OECD monthly average that lags 1-2 months. A move of -50bp / +50bp in it shifts the floor to 6.51% / 7.51%, and base value to DKK 392.5 / 311.1 (USD 58.78 / 46.58).
2. If the USD-name floor of 8.00% is applied instead, base value is **DKK 282.0 = USD 42.22**.
3. Because the floor binds, beta and the cost of debt are **not** load-bearing. The floor is.

## E. DCF scenarios

10-year FCFF DCF (FY2026-FY2035) in DKK via `valuation.dcf(mid_year=True, stub_years=0.7830)`, WACC 7.01% in every scenario. Scenarios differ in cash flows, not in the discount rate. No probabilities are assigned; that is the Skeptic's job.

**Inputs per scenario** (printed by the model as `[SCENARIO inputs]`):

| Input | BEAR | BASE | BULL | Source / basis |
|---|---|---|---|---|
| FY26 revenue growth (DKK) | -7.0% | -4.0% | -1.0% | FY26 guidance of -6% / -3% / 0% CER (low / mid / top), less 1pt DKK effect (dossier S3) |
| FY27 | -10.0% | -3.0% | +2.0% | ASSUMPTION. 1 Jan 2027 WAC cut (list ~-50% Wegovy, ~-35% Ozempic) plus LOE annualising. No 2027 guidance (dossier S3/S4). |
| FY28-30 | -4 / 0 / +1% | +2 / +3 / +3% | +6 / +6 / +6% | ASSUMPTION. Bull's sourced drivers: IQVIA branded obesity volume +81%, Intl Ops obesity +37% CER, Wegovy pill >265k weekly TRx (dossier S3/S8). |
| FY31-35 | -8 / -10 / -3 / 0 / +1% | +2 / -1 / -1 / +2 / +2.5% | +4 / +1 / +1 / +3 / +3% | ASSUMPTION. Semaglutide LOE in major markets (date UNKNOWN), offset by the pipeline (CMD ">150 bDKK pipeline sales in 2035", risk-adjusted). |
| 10-yr revenue CAGR / FY35 revenue | -4.09% / 201,753 | +0.52% / 322,769 | +3.07% / 414,842 | computed |
| EBIT margin FY26 | 42.7% | 42.7% | 42.8% | Guidance-implied: adjusted EBIT growth (CER - 2pt) applied to the FY25 adjusted base of 132,374 |
| EBIT margin FY27-35 | 37 -> 34 (LOE) -> 35% | 40 -> 41 -> 39.5 (LOE) -> 40% | 42 -> 44 -> 42.5 (LOE) -> 44% | ASSUMPTION. Anchors: 5-yr avg 42.7%, low 41.3%, FY23-24 44.2%, Q2-26 adj GM 78.2%. Bull's reason: headcount 76,302 -> 68,794 (dossier S5). |
| Tax | 23% | 22% | 21% | FY26 guidance 21-23% (dossier S3) |
| D&A % revenue | 5.3 -> 7.0% | 5.1 -> 7.0% | 5.0 -> 7.0% | FY26 = H1-26 D&A ex-impairment x2 = 15,024. Ramp is an ASSUMPTION (FY25-26 capex entering service). |
| PP&E capex % revenue | 19.3 / 15 / 12 / 9 / 7% | 18.7 / 14 / 10 / 8 / 6% | 18.1 / 14 / 10 / 8 / 6% | FY26 = guided "around 55 bDKK"; "expected to decline" (dossier S3). Path is an ASSUMPTION. |
| BD / in-licensing | 0.60% FY26, then 1.45% | 0.58%, then 1.45% | 0.56%, then 1.45% | FY26 = H1 854 x2; thereafter the FY21-24 median (facts) |
| Cash gap (WC / tax / restructuring) | 3.09% FY26, 6.17% FY27 | 2.76%, 2.76% | 2.47%, 0 | FY26 calibrated to the FCF guide of 45 / 50 / 55bn. FY27 is an ASSUMPTION (company: WAC cut "expected to impact Novo Nordisk's cash flow in 2027"). |
| Working capital | 0 | 0 | 0 | ASSUMPTION (see H7) |
| Terminal growth | 1.5% | 2.5% | 3.0% | <= min(4%, DKK 10y 3.01%) |
| Terminal ROIC | 12% | 20% | 30% | ASSUMPTION; FY25 ROIC is 33.6% |
| Claims (ND Dec-25 + 2026 distributions) | 166,914 | 166,914 | 166,914 | facts additions; dossier S1/S2/S5 |

**Results:**

| | BEAR | BASE | BULL |
|---|---|---|---|
| Value, DKK per share | **156.6** | **347.3** | **554.1** |
| Value, USD per ADR (x 0.149734) | **23.44** | **52.01** | **82.97** |
| vs price of record USD 38.415 | -39.0% | +35.4% | +116.0% |
| vs close USD 38.015 | -38.3% | +36.8% | +118.3% |
| PV explicit / PV terminal (DKK m) | 388,512 / 469,352 | 627,203 / 1,072,502 | 827,173 / 1,785,231 |
| TV share of EV | 55% | 63% | 68% |
| TV > 75% flag | no | no | no |

Cross-checks:
- **FCF-margin anchor.** BASE FY30-35 FCF margin is 30.9%, against a 5-yr average of 30.5% (OCF - PP&E) or 26.7% (facts definition, which includes Akero).
- **The terminal is stricter than the explicit years.** g/ROIC reinvestment implies gross capex + dWC of 10.9% of revenue in the BASE terminal, vs 7.45% capex + BD in explicit FY35. This is also why the capex path barely moves value (G).
- **Instruction-literal bear** (margin only falls to the 5-yr low of 41.3%, with BEAR growth): DKK 190.2 = USD 28.49. The bear above goes below that low because Q2-26 adjusted GM (78.2%) is already below its own 5-yr low (81.0%) before the WAC cut lands.
- **CMD "broadly stable operating margin" taken literally** (42.7% flat, BASE growth): DKK 372.4 = USD 55.77.

Executed output (`python3 reports/runs/NVO_2026-10-13/02_model.py`, sections 2, 3, 7):
```
================================================================================================
2. ADJUSTED BASE (FY2025) AND FY2026 GUIDANCE TRANSLATION
================================================================================================
Definition check: H1-26 reported EBIT 86,679 - 340B 26,760 + Q2 impairment 6,328 = 66,247 vs company H1-26 adjusted EBIT 66,247 -> MATCH
FY2025 adjusted-equivalent: revenue 309,064 - 2,600 = 306,464 | EBIT 127,658 - 2,600 + impairments 7,316 = 132,374 (43.2%) | EBITDA 147,040 (company EBITDA 149,640 incl. 340B)
  (FY2025 transformation costs ~DKK 8bn stay IN the adjusted EBIT: the H1-26 definition does not remove restructuring.)
FY25 company adjusted NP 116,407 - reported 102,434 = 13,973; our adjustments explain 3,701 after tax -> 10,272 UNEXPLAINED (likely incl. ~8bn transformation costs). If the company's FY25 adjusted EBIT base includes it: 145,465 (47.5%) -> FY26 BASE guide-implied margin 47.0% instead of 42.7%
  implied H2-26 adjusted EBIT margin (our base): (125,755 - H1 66,247) / (294,205 - H1 148,551) = 40.9% vs H1-26 actual 44.6%
  implied H2-26 adjusted EBIT margin (alt base): (138,192 - H1 66,247) / (294,205 - H1 148,551) = 49.4% vs H1-26 actual 44.6%
BEAR  FY26 sales -6% CER -7% DKK -> 285,012 | adj EBIT -8% DKK -> 121,784 (42.73%) | NOPAT@23% + D&A 15,024 - capex 55,000 = 53,798 vs guided FCF 45,000 -> cash gap 8,798 (3.09% of rev)
BASE  FY26 sales -3% CER -4% DKK -> 294,205 | adj EBIT -5% DKK -> 125,755 (42.74%) | NOPAT@22% + D&A 15,024 - capex 55,000 = 58,113 vs guided FCF 50,000 -> cash gap 8,113 (2.76% of rev)
BULL  FY26 sales +0% CER -1% DKK -> 303,399 | adj EBIT -2% DKK -> 129,727 (42.76%) | NOPAT@21% + D&A 15,024 - capex 55,000 = 62,508 vs guided FCF 55,000 -> cash gap 7,508 (2.47% of rev)
Cross-check FY2025: adj EBIT x (1-ETR 21.5%) + D&A - PP&E capex = 58,399 vs actual OCF - PP&E capex 58,962
H2-26 implied company FCF = FY guide 45-55bn - H1 actual 55.3bn = -10.3 to -0.3bn (dossier S2/S3)
================================================================================================
3. EV -> EQUITY BRIDGE (valuation date 2026-10-13)
================================================================================================
Stub: 2025-12-31 -> 2026-10-13 = 0.7830 yrs (mid-year discounting on)
Net debt Dec-25 (borrowings 130,958 - cash 26,464) = 104,494; marketable securities Dec-25 UNKNOWN (500 at Jun-26)
+ FY25 final dividend paid 2026 35,312 + 2026 interim (3.75 x 4,413.1m) 16,549 + 2026 buybacks to 9 Oct 10,559
= claims deducted from rolled-forward EV: 166,914 (37.82 DKK/share)
Reconciliation: Jun-26 net debt 95,145 vs Dec-25 ND + H1 distributions 145,705 -> H1-26 cash generated before distributions 50,560 (company H1 FCF 55.3bn)
Estimated Oct-26 net debt (Jun ND + interim div + Jul-Oct buybacks, no H2 op cash) 116,354
Market EV (mcap 1,132,209 + Jun-26 ND 95,145) = 1,227,354 DKK m = USD 183.8bn | with Oct-26 ND estimate 1,248,563
================================================================================================
7. DCF SCENARIOS (10 yr FY2026-FY2035, FCFF, DKK; mid-year; stub-dated to 2026-10-13)
================================================================================================

[BEAR inputs] growth: -7.0% -10.0% -4.0% +0.0% +1.0% -8.0% -10.0% -3.0% +0.0% +1.0%
  EBIT margin: 42.7% 37.0% 37.0% 37.0% 37.0% 34.0% 34.0% 34.0% 35.0% 35.0%
  PP&E capex%: 19.3% 15.0% 12.0% 9.0% 7.0% 7.0% 7.0% 7.0% 7.0% 7.0%
  BD%:         0.60% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45%
  D&A%:        5.3% 5.8% 6.4% 6.8% 7.0% 7.0% 7.0% 7.0% 7.0% 7.0%
  cash gap%:   3.09% 6.17% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%
  terminal: NOPAT margin 26.9%; reinvestment g/ROIC = 12.5% of NOPAT = 3.4% of revenue -> implied gross capex+dWC = D&A 7.0% + 3.4% = 10.4% of revenue (explicit FY35 capex+BD 8.45%)

--- BEAR: WACC 7.01% | g_T 1.5% | ROIC_T 12% | tax 23% | BD 1.45% | 10-yr rev CAGR -4.09% | FY35 rev 201,753
FY          g   Revenue  EBIT%   EBITDA     EBIT     D&A Cpx+BD+gap      FCF   FCF%       PV
2026    -7.0%   285,012  42.7%  136,808  121,784  15,024     65,506   43,292  15.2%   41,850
2027   -10.0%   256,510  37.0%  109,786   94,909  14,878     58,033   29,925  11.7%   27,033
2028    -4.0%   246,250  37.0%  106,872   91,112  15,760     33,121   52,795  21.4%   44,569
2029    +0.0%   246,250  37.0%  107,857   91,112  16,745     25,734   61,168  24.8%   48,254
2030    +1.0%   248,712  37.0%  109,433   92,024  17,410     21,017   67,251  27.0%   49,578
2031    -8.0%   228,815  34.0%   93,814   77,797  16,017     19,336   56,585  24.7%   38,983
2032   -10.0%   205,934  34.0%   84,433   70,018  14,415     17,402   50,927  24.7%   32,786
2033    -3.0%   199,756  34.0%   81,900   67,917  13,983     16,880   49,399  24.7%   29,719
2034    +0.0%   199,756  35.0%   83,897   69,915  13,983     16,880   50,937  25.5%   28,637
2035    +1.0%   201,753  35.0%   84,736   70,614  14,123     17,049   51,447  25.5%   27,029
PV explicit 388,512 | PV terminal 469,352 (55% of EV)
EV 857,864 - claims 166,914 = equity 690,950 -> DKK 156.6/share = USD 23.44/ADR vs USD 38.415 (-39.0%); vs close 38.015: -38.3%

[BASE inputs] growth: -4.0% -3.0% +2.0% +3.0% +3.0% +2.0% -1.0% -1.0% +2.0% +2.5%
  EBIT margin: 42.7% 40.0% 41.0% 41.0% 41.0% 41.0% 39.5% 39.5% 40.0% 40.0%
  PP&E capex%: 18.7% 14.0% 10.0% 8.0% 6.0% 6.0% 6.0% 6.0% 6.0% 6.0%
  BD%:         0.58% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45%
  D&A%:        5.1% 5.8% 6.4% 6.8% 7.0% 7.0% 7.0% 7.0% 7.0% 7.0%
  cash gap%:   2.76% 2.76% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%
  terminal: NOPAT margin 31.2%; reinvestment g/ROIC = 12.5% of NOPAT = 3.9% of revenue -> implied gross capex+dWC = D&A 7.0% + 3.9% = 10.9% of revenue (explicit FY35 capex+BD 7.45%)

--- BASE: WACC 7.01% | g_T 2.5% | ROIC_T 20% | tax 22% | BD 1.45% | 10-yr rev CAGR +0.52% | FY35 rev 322,769
FY          g   Revenue  EBIT%   EBITDA     EBIT     D&A Cpx+BD+gap      FCF   FCF%       PV
2026    -4.0%   294,205  42.7%  140,779  125,755  15,024     64,821   48,292  16.4%   46,683
2027    -3.0%   285,379  40.0%  130,704  114,152  16,552     51,962   53,629  18.8%   48,446
2028    +2.0%   291,087  41.0%  137,975  119,346  18,630     33,330   78,389  26.9%   66,175
2029    +3.0%   299,819  41.0%  143,314  122,926  20,388     28,334   87,936  29.3%   69,372
2030    +3.0%   308,814  41.0%  148,231  126,614  21,617     23,008   97,368  31.5%   71,781
2031    +2.0%   314,990  41.0%  151,195  129,146  22,049     23,468   99,316  31.5%   68,420
2032    -1.0%   311,840  39.5%  145,006  123,177  21,829     23,233   94,674  30.4%   60,950
2033    -1.0%   308,722  39.5%  143,556  121,945  21,611     23,001   93,727  30.4%   56,387
2034    +2.0%   314,896  40.0%  148,001  125,959  22,043     23,461   96,830  30.7%   54,438
2035    +2.5%   322,769  40.0%  151,701  129,108  22,594     24,047   99,250  30.7%   52,144
PV explicit 627,203 | PV terminal 1,072,502 (63% of EV)
EV 1,699,704 - claims 166,914 = equity 1,532,790 -> DKK 347.3/share = USD 52.01/ADR vs USD 38.415 (+35.4%); vs close 38.015: +36.8%

[BULL inputs] growth: -1.0% +2.0% +6.0% +6.0% +6.0% +4.0% +1.0% +1.0% +3.0% +3.0%
  EBIT margin: 42.8% 42.0% 44.0% 44.0% 44.0% 44.0% 42.5% 42.5% 44.0% 44.0%
  PP&E capex%: 18.1% 14.0% 10.0% 8.0% 6.0% 6.0% 6.0% 6.0% 6.0% 6.0%
  BD%:         0.56% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45% 1.45%
  D&A%:        5.0% 5.8% 6.4% 6.8% 7.0% 7.0% 7.0% 7.0% 7.0% 7.0%
  cash gap%:   2.47% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%
  terminal: NOPAT margin 34.8%; reinvestment g/ROIC = 10.0% of NOPAT = 3.5% of revenue -> implied gross capex+dWC = D&A 7.0% + 3.5% = 10.5% of revenue (explicit FY35 capex+BD 7.45%)

--- BULL: WACC 7.01% | g_T 3.0% | ROIC_T 30% | tax 21% | BD 1.45% | 10-yr rev CAGR +3.07% | FY35 rev 414,842
FY          g   Revenue  EBIT%   EBITDA     EBIT     D&A Cpx+BD+gap      FCF   FCF%       PV
2026    -1.0%   303,399  42.8%  144,751  129,727  15,024     64,216   53,292  17.6%   51,517
2027    +2.0%   309,467  42.0%  147,925  129,976  17,949     47,814   72,817  23.5%   65,780
2028    +6.0%   328,035  44.0%  165,330  144,336  20,994     37,561   97,458  29.7%   82,273
2029    +6.0%   347,718  44.0%  176,640  152,996  23,645     32,860  111,651  32.1%   88,080
2030    +6.0%   368,581  44.0%  187,976  162,175  25,801     27,460  126,459  34.3%   93,227
2031    +4.0%   383,324  44.0%  195,495  168,662  26,833     28,559  131,517  34.3%   90,604
2032    +1.0%   387,157  42.5%  191,643  164,542  27,101     28,844  128,245  33.1%   82,562
2033    +1.0%   391,029  42.5%  193,559  166,187  27,372     29,133  129,527  33.1%   77,925
2034    +3.0%   402,759  44.0%  205,407  177,214  28,193     30,007  138,186  34.3%   77,688
2035    +3.0%   414,842  44.0%  211,570  182,531  29,039     30,907  142,331  34.3%   74,777
PV explicit 827,173 | PV terminal 1,785,231 (68% of EV)
EV 2,612,404 - claims 166,914 = equity 2,445,490 -> DKK 554.1/share = USD 82.97/ADR vs USD 38.415 (+116.0%); vs close 38.015: +118.3%

FCF-margin anchor: BASE FY30-35 FCF margin 30.9% vs 5-yr avg 30.5% (OCF-PP&E) / 26.7% (facts def, incl. Akero)
BASE terminal-year FCF margin implied by g/ROIC: 27.3% of FY35 revenue
BASE FY2027 revenue 285,379 vs CONSENSUS FY2027 304,688 (dossier S9; comparison only, not an input): -6.3%
```

## F. Reverse DCF & sensitivity grid

**What must be true at USD 38.415 (DKK 256.56):**
- With BASE margins, capex and terminal assumptions at WACC 7.01%, the price implies a constant 10-yr revenue CAGR of **-2.88%** (FY35 revenue 228,705 vs FY25 adjusted 306,464). At the close it is -2.99%.
- The same solve under BEAR margins gives +0.73%; under BULL margins, -5.23%. At the USD-name floor of 8%, -0.70%.
- With BASE growth, the price implies a flat FY27-35 **EBIT margin of 30.7%**, vs the 5-yr low of 41.3% and the FY26 guide-implied 42.7%.
- With the BASE operating case, the price implies an **IRR of 8.51%**.
- Explicit FY26-35 FCF less claims is worth DKK 104.3/share. The price therefore needs DKK 152.3/share (59% of price) from the terminal, against a BASE terminal value of 243.0.
- **Equivalences found:**
  - BASE with a deep LOE (-18% / -18% in FY32-33, no pipeline offset) gives DKK 256.3, which is the price.
  - Zero growth with maintenance capex = D&A at a 40% EBIT margin on FY27 BASE revenue gives an EPV of DKK 261.5, roughly the price.

  In plain terms, the market is paying for no growth at a margin just below the 5-yr low, or for the base case with an un-offset semaglutide cliff.

`reverse_dcf()` caveat: not applicable here. The company is profitable, so there are no early losses to scale.

Executed output (sections 8, 9, 11, 12):
```
================================================================================================
8. REVERSE DCF (what must be true at USD 38.415 = DKK 256.56)
================================================================================================
BASE margins/capex, WACC 7.01%, g 2.5%, ROIC 20%: implied constant 10-yr revenue CAGR -2.88% (FY35 revenue 228,705); at close price -2.99%
  at BEAR margins/capex/terminal: implied CAGR +0.73%
  at BULL margins/capex/terminal: implied CAGR -5.23%
  BASE operating inputs at WACC 8.00% (USD-name floor): implied CAGR -0.70%
At BASE growth path: price implies flat FY27-35 EBIT margin 30.74% (5-yr avg 42.7%, low 41.3%; FY26 guide-implied 42.7%)
BASE operating case: price implies a discount rate (IRR) of 8.51%
BASE PV of FY26-35 explicit FCF less claims = DKK 104.3/share; price needs DKK 152.3/share (59% of price) from the terminal (BASE TV gives 243.0)
================================================================================================
9. SENSITIVITY (BASE): WACC x terminal growth, DKK/share (USD/ADR in brackets)
================================================================================================
WACC / g              1.5%            2.0%            2.5%            3.0%            3.5%   (g 3.5% > DKK 10y cap 3.01%)
6.01%          388 (58.02)     415 (62.16)     451 (67.47)     498 (74.52)     563 (84.36)
6.51%          346 (51.85)     367 (54.93)     393 (58.78)     425 (63.70)     469 (70.24)
7.01%          313 (46.80)     328 (49.15)     347 (52.01)     371 (55.57)     402 (60.13)
7.51%          284 (42.59)     297 (44.41)     311 (46.58)     329 (49.23)     351 (52.53)
8.01%          261 (39.03)     270 (40.46)     281 (42.14)     295 (44.15)     311 (46.60)

BASE: WACC x terminal ROIC (g 2.5%), DKK/share
WACC/ROIC       12%      15%      20%      25%      30%
6.01%           418      434      451      460      467
6.51%           365      379      393      401      406
7.01%           324      336      347      354      359
7.51%           291      301      311      317      321
8.01%           264      273      281      287      290

BASE: flat FY27-35 EBIT margin x WACC, DKK/share
WACC/EBIT%    34.0%    37.0%    41.3%    42.7%    44.2%
6.01%           376      412      465      482      501
6.51%           326      359      405      420      436
7.01%           288      317      359      372      386
7.51%           257      284      321      334      346
8.01%           232      256      291      302      314
================================================================================================
11. STRESS TESTS ON BASE (one change each)
================================================================================================
No major-market LOE in horizon (FY32-33 at +2.5%)    DKK   368.1  USD  55.12  (+43%)
LOE early: FY30-31 -1%/-1%, FY32-33 +2%              DKK   342.3  USD  51.25  (+33%)
LOE base timing FY32-33 -1%/-1% (BASE)               DKK   347.3  USD  52.01  (+35%)
LOE late: FY34-35 -1%/-1%                            DKK   350.6  USD  52.49  (+37%)
Deep LOE FY32-33 -18%/-18%, no pipeline offset       DKK   256.3  USD  38.38  (-0%)
WAC-cut cash unwind: 10% of sales-deduction provision (14,020) paid out in FY27 (pre-tax, no offset): -3.0 DKK/share -> 344.3 (USD 51.55)
WAC-cut cash unwind: 25% of sales-deduction provision (35,050) paid out in FY27 (pre-tax, no offset): -7.6 DKK/share -> 339.8 (USD 50.87)
WAC-cut cash unwind: 50% of sales-deduction provision (70,100) paid out in FY27 (pre-tax, no offset): -15.1 DKK/share -> 332.2 (USD 49.74)
WACC 8.00% (USD-name floor instead of DKK floor): DKK 282.0 (USD 42.22)
DKK 10y 2.51% (stale input -50bp) -> floor 6.51%: DKK 392.5 (USD 58.78)
DKK 10y 3.51% (stale input +50bp) -> floor 7.51%: DKK 311.1 (USD 46.58)
Steady-state PP&E capex FY30-35 4.5% instead of 6.0% (FY20-21 level 4.5%; FY22-23 avg 9.0%): DKK 351.5 (USD 52.64)
Steady-state PP&E capex FY30-35 9.0% instead of 6.0% (FY20-21 level 4.5%; FY22-23 avg 9.0%): DKK 338.9 (USD 50.74)
Capex stays high (FY27-28 14%, FY29 12%, FY30-35 9%): DKK 334.3 (USD 50.05)
Leases outside Borrowings (+8,572 Dec-25 leases to claims): 345.4 (-1.94)
Akero CVR USD 0.5bn paid: 346.6 (-0.76)
BEAR growth with EBIT margin held at the 5-yr low 41.3% (instead of 34-37%): DKK 190.2 (USD 28.49)
BASE growth with CMD 'broadly stable margin' taken literally (42.7% flat): DKK 372.4 (USD 55.77)
Price check: USD 38.415 (record) vs 38.015 (close): base upside +35.4% vs +36.8%
================================================================================================
12. EARNINGS-POWER CROSS-CHECK (no growth, maintenance capex = D&A; Oct-26 ND estimate)
================================================================================================
FY26 BASE revenue 294,205 x EBIT 34.0% x (1-22%) / 7.01% = EPV 1,113,028 -> DKK 225.8 (USD 33.82)
FY26 BASE revenue 294,205 x EBIT 37.0% x (1-22%) / 7.01% = EPV 1,211,237 -> DKK 248.1 (USD 37.15)
FY26 BASE revenue 294,205 x EBIT 40.0% x (1-22%) / 7.01% = EPV 1,309,445 -> DKK 270.4 (USD 40.48)
FY26 BASE revenue 294,205 x EBIT 42.7% x (1-22%) / 7.01% = EPV 1,399,274 -> DKK 290.7 (USD 43.53)
FY27 BASE revenue 285,379 x EBIT 34.0% x (1-22%) / 7.01% = EPV 1,079,637 -> DKK 218.3 (USD 32.68)
FY27 BASE revenue 285,379 x EBIT 37.0% x (1-22%) / 7.01% = EPV 1,174,900 -> DKK 239.9 (USD 35.92)
FY27 BASE revenue 285,379 x EBIT 40.0% x (1-22%) / 7.01% = EPV 1,270,162 -> DKK 261.5 (USD 39.15)
FY27 BASE revenue 285,379 x EBIT 42.7% x (1-22%) / 7.01% = EPV 1,357,296 -> DKK 281.2 (USD 42.10)
```

## G. Load-bearing inputs

Each input is moved +/-10% relative, one at a time, everything else fixed (BASE = DKK 347.3 = USD 52.01). Ranked by swing:

| # | Input (BASE value) | Source | -10% -> DKK (USD) | +10% -> DKK (USD) | Swing (DKK) |
|---|---|---|---|---|---|
| 1 | **WACC** 7.01% | Floor = DKK 10y 3.01% (00_inputs) + 4%. CAPM is only 5.79%. | 414.1 (62.00) | 298.5 (44.70) | **115.6** |
| 2 | **EBIT margin**, all years (42.7% FY26; 39.5-41% after) | FY26 guidance-implied; FY27+ ASSUMPTION | 306.3 (45.87) | 388.3 (58.15) | **82.0** |
| 3 | **FY27+ revenue level** (WAC-cut year -3%) | ASSUMPTION (no 2027 guidance) | 309.9 (46.41) | 384.7 (57.61) | **74.8** |
| 4 | DKKUSD 0.149734 (USD value only) | 00_inputs | (46.81) | (57.21) | DKK unchanged |
| 5 | Tax 22% | FY26 guidance 21-23% | 358.9 (53.74) | 335.8 (50.27) | 23.1 |
| 6 | Terminal growth 2.5% | ASSUMPTION, <= DKK 10y | 337.3 (50.50) | 358.5 (53.68) | 21.2 |
| 7 | PP&E capex path (18.7% -> 6%) | FY26 guided 55bn; path ASSUMPTION | 352.2 (52.73) | 342.5 (51.28) | 9.7 |
| 8 | Claims 166,914 | facts additions / dossier S1, S2, S5 | 351.1 (52.57) | 343.5 (51.44) | 7.6 |
| 9 | Terminal ROIC 20% | ASSUMPTION (FY25 33.6%) | 343.5 (51.43) | 350.5 (52.48) | 7.0 |
| 10 | D&A % revenue (EBITDA fixed) | H1-26 annualised; ramp ASSUMPTION | 350.8 (52.53) | 343.8 (51.48) | 7.0 |
| 11 | BD allowance 1.45% | facts, FY21-24 median | 348.0 (52.11) | 346.6 (51.90) | 1.4 |
| 12 | FY26-27 cash gap | calibrated to FY26 FCF guide | 347.7 (52.06) | 347.0 (51.95) | 0.7 |

**Inputs that cannot be expressed as +/-10% but move value more** (section 11):
- Revenue growth FY27-35 -1pt / +1pt: 320.3 / 376.4.
- Deep un-offset LOE: 256.3.
- WACC at the USD floor of 8%: 282.0.
- DKK 10y -50bp / +50bp: 392.5 / 311.1.
- Bear-growth path at the 5-yr-low margin: 190.2.

**Top 3:**
1. The discount-rate floor, set by a stale-prone DKK 10y.
2. The post-WAC-cut EBIT margin.
3. The FY27+ revenue level, i.e. the net-price pass-through of the WAC cut.

Behind all three sits the depth of the semaglutide LOE, which is what separates base from price.

```
================================================================================================
10. LOAD-BEARING INPUTS: +/-10% (relative, one at a time) on BASE, DKK/share
================================================================================================
BASE = DKK 347.3/share = USD 52.01/ADR
Input                                      -10%     +10%   swing  -10% USD  +10% USD
WACC (7.01%)                              414.1    298.5   115.6     62.00     44.70
EBIT margin, all years                    306.3    388.3    82.0     45.87     58.15
FY27+ revenue level (WAC-cut yr)          309.9    384.7    74.8     46.41     57.61
Tax rate (22%)                            358.9    335.8    23.1     53.74     50.27
Terminal growth (2.5%)                    337.3    358.5    21.2     50.50     53.68
PP&E capex / revenue                      352.2    342.5     9.7     52.73     51.28
Claims (ND Dec-25 + 2026 distrib.)        351.1    343.5     7.6     52.57     51.44
Terminal ROIC (20%)                       343.5    350.5     7.0     51.43     52.48
D&A / revenue (EBITDA fixed)              350.8    343.8     7.0     52.53     51.48
BD/in-licensing allowance                 348.0    346.6     1.4     52.11     51.90
FY26-27 cash gap                          347.7    347.0     0.7     52.06     51.95
DKKUSD FX (USD value only)                                  46.81     57.21  (DKK value unchanged)
Revenue growth FY27-35 -1pt / +1pt (absolute, not 10%): 320.3 / 376.4
```

## H. Open questions for the Skeptic

1. **Which currency's floor?** Base value is DKK 347.3 (USD 52.01) under the DKK floor of 7.01%, vs DKK 282.0 (USD 42.22) under the USD floor of 8.00%. CAPM gives only 5.79% (Blume beta 0.587 from the vendor's raw 0.384), so the floor does all the work. The DKK 10y is an Aug-26 OECD monthly average and stale-prone (+/-50bp gives 311.1 / 392.5). For an SGD-based holder of a USD ADR on DKK cash flows, which opportunity cost is right?
2. **FY27 WAC cut.** There is no 2027 guidance until Feb 2027. Base has FY27 revenue -3% and EBIT margin 40%. BASE FY2027 revenue (285,379) is 6.3% below the CONSENSUS FY2027 figure of 304,688 (comparison only, never an input). Is the base too harsh or too soft on how much of a 35-50% list cut reaches net price?
3. **Semaglutide LOE dates are UNKNOWN** for the US, EU, China and India, and the molecule is at least 68.9% of Q2-26 adjusted sales. Timing barely matters (342.3 to 368.1 across the sweep), but depth does: -18% / -18% with no pipeline offset gives DKK 256.3, i.e. the price. Sourcing the US/EU compound-patent expiry and the probability-adjusted pipeline offset is the single highest-value piece of research left.
4. **FY25 adjusted base definition.** The company's FY25 adjusted net profit (116,407) implies 10,272 of after-tax adjustments that my definition (340B plus impairments, the one H1-26 reconciles to) does not explain. That gap probably includes about 8bn of transformation costs. If the company's base includes them, the FY26 guide-implied margin is 47.0%, not 42.7%. But that would require an H2-26 adjusted EBIT margin of 49.4% against H1's 44.6% while prices are falling. I judged that implausible and kept 42.7% (implied H2 margin 40.9%). FY26 value is calibrated to FCF guidance either way, so what this changes is the level that "broadly stable margin" anchors to.
5. **Bear margin floor.** The bear uses 34-37%, below the 5-yr low of 41.3%. The instruction-literal bear (5-yr low) gives 190.2 (USD 28.49). Is the deeper bear justified by Q2-26 GM of 78.2% and the WAC cut, or over-punitive?
6. **The 2027 cash hit from the WAC cut.** The current sales-deduction provision is 140,201 (Jun-26). In base the 2027 hit is only a 2.76%-of-revenue FY27 cash gap. If 10% / 25% / 50% of the provision unwinds in FY27, value falls by 3.0 / 7.6 / 15.1 DKK/share. Small against the margin and WACC effects, but it is explicitly flagged by the company.
7. **Working-capital quality.** Inventories +21.5% vs sales +6.4% in FY25 (write-downs 4,272), and trade receivables +25.5% in H1-26. WC is modelled at 0% of incremental revenue. A write-down wave or a slower collection cycle would cut FY26-27 cash below the guidance calibration.
8. **Tax on the 340B reversal.** Tax payables were 20,460 at Jun-26 vs 8,416 at Dec-25. Whether the DKK 26.8bn non-cash reversal triggers cash tax is UNKNOWN. In the DCF it is absorbed by the FY26 FCF calibration. It does change the normalised EPS (21.50 assumes the reversal is taxed at 22%), and therefore P/E and the Lynch ratio.
9. **Bridge items not confirmed:**
   - Leases inside Borrowings: -1.94 DKK/share if they sit outside.
   - Akero CVR USD 0.5bn: -0.76 if paid, excluded.
   - Marketable securities at Dec-25: UNKNOWN.
   - Pensions, other provisions, minorities: not in the dossier, treated as zero.
   - Debt maturity ladder: UNKNOWN.
10. **Distributions exceed cash.** In 2026, dividends plus the 15bn buyback exceed guided FCF by 16,861. Borrowings went from 26,645 (FY21) to 140,127 (Jun-26). The unexecuted remainder of the buyback programme is not deducted (value-neutral if bought at fair value; value-destroying above it). The CMD keeps "an attractive dividend per share" as an ambition.
11. **Terminal assumptions.** TV is 55-68% of EV, below the 75% flag. Terminal ROIC is 20% vs a reported 34%, and expensed R&D flatters the reported figure. The ROIC grid at 7.01% runs from 324 (12%) to 359 (30%), so terminal ROIC is a second-order input here.
12. **Price of record.** The 00_inputs intraday price (USD 38.415) is used, vs the close (38.015, also in fj). Base upside is +35.4% vs +36.8%.
13. **Vendor beta 0.384** is low for a single-molecule pharma facing policy risk. It is irrelevant while the floor binds, and decisive if anyone removes the floor.
