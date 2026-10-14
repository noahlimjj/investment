<!-- pipeline:value-skeptic -->
# Skeptic audit: RVMD (as of 2026-10-13)

Revolution Medicines, NASDAQ, USD. Price **$193.95** (close 2026-10-12, re-verified via yfinance; 2026-10-13
close $192.55, −0.7%, immaterial). Template rNPV. CURRENT HOLDING. Re-run: `03_rerun.py` (it reproduces the
Quant's $15.60 / $63.38 / $130.49 exactly before applying any change). Data warnings carried: 2
(institutional_pct vendor artifact; negative owner earnings, confirmed).

## 1. Pre-mortem (written before reading the model)

Recorded at 21:32 SGT, before `02_quant.md` / `02_model.py` were opened:

> The price ($41.6B market cap, ~$38B EV) already capitalises a multi-indication franchise (1L mPDAC plus
> RAS-mutant NSCLC). The only approved revenue stream is 2L+ mPDAC, a short-duration, small-population market.
> The most likely failure path: the 1L PDAC and NSCLC readouts are positive but commercially narrower than
> priced. Pan-RAS(ON) tolerability limits combination use and treatment duration, and mutant-selective
> competitors take NSCLC share. Peak revenue then lands well below the ~$8–12B the price needs, while
> ~$2.1–2.2B of annual opex, 28%/yr share dilution, a 4.55% top-line royalty to Royalty Pharma and secured
> debt keep compounding. Terminal kicker: the IRA small-molecule clock (~2033 selection) caps the tail.

## 2. Number audit

Reproduction: `02_model.py` re-executed and gives identical output. `03_rerun.py` replicates `run()` to $0.0000.
Primary-source spot-checks (5): the 10-Q on EDGAR (convert terms; option and RSU table), the patent expiry
search (not found, stays UNKNOWN), ACS 2026 epidemiology, and IRA/EPIC Act status. The 10y yield comes from
the orchestrator (FRED DGS10).

| Input | Quant value | Verified value | Source | Status | Δ base FV |
|---|---|---|---|---|---|
| Price | $193.95 | $193.95 (10-12 close) | yfinance history pulled 2026-10-13 | PASS | 0 |
| Shares | 214.336M basic | 214.336M basic (cover 07-31); 214.243M at 06-30. **Plus 9.74M vested options at $25.62 WAEP**, 8.62M unvested options, 5.08M RSUs (23.4M total = 10.9% of basic) | 10-Q accn 0001193125-26-335104, Note 12–13 | **FAIL – Model fidelity** (vested in-the-money options ignored; treasury-stock method at intrinsic value adds +2.5%) | **−2.6%** (−$1.64) |
| Cash + MS | 3,937.97 | 815.435 + 3,122.534 = 3,937.969 | 10-Q balance sheet | PASS | 0 |
| Converts | $500M par, conversion price UNKNOWN | $500M, 0.50%, conversion **$198.80** (5.0302 sh/$1,000), 2.515M shares if converted | 10-Q Note 10 | PASS: par treatment is correct (out of the money at $193.95, far above FV). Deducting at par rather than PV is ~$1/sh conservative and was not changed | 0 |
| Warrant liability | 185.253 deducted | 19.73M warrants × 0.1112 sh at $11.50 (= $103.42/sh), 2.19M shares, expire Dec 2026 | 10-Q Note 11 | PASS (conservative at FV < $103) | 0 |
| Royalty liability | 548.5 not deducted; tiers 4.55/2.50/1.00/0% modelled | Tiers verbatim; payable on RMC-6236 and same-indication RMC-9805 WW net sales | 10-Q Note 8 | PASS (no double count). Applying the royalty to all revenue is slightly conservative | 0 |
| Net debt / EV | EV 38,132.6 | 41,570.5 − 3,938.0 + 500 = 38,132.5 | identity | PASS | 0 |
| Base revenue H2-26 | $72M (Q3 consensus 24.1 × 3) | not reportable (Q3 not yet reported) | yfinance CONSENSUS (non-primary) | PASS with note (Temporal) | ±$0.1 |
| H2-26 opex | 1,199.6 | 2,150 − 950.4; H1 R&D 738.889 + G&A 211.5 recomputed; Q2 R&D 394.919, net loss 644.371 match | 10-Q P&L; 8-K guidance | PASS | 0 |
| rf / WACC | 5.20% / 10.177% | 5.22% (FRED DGS10 2026-10-08) / 10.196%; recomputed | orchestrator; python | **FAIL – Temporal (minor)** | −0.2% |
| IRA Medicare negotiation | not modelled | Current law: small molecules selected 7 yrs post-approval, price effective ~9 yrs. EPIC Act (13 yrs) still a proposal per Apr-2026 source. Daraxonrasib approved 2026-08-26 → negotiated price from 2036 | IRA statute; Public Citizen Apr-2026 (via Salud y Fármacos) | **FAIL – Model fidelity** (statutory cash-flow effect omitted). Haircut size is a Skeptic assumption: 65% US × 55% Medicare × 25% price cut = 8.9% of segment revenue, 2036→LOE (darax), 2040→LOE (later molecules) | **−6.5%** (−$4.09) |
| Segment peaks | 9,500 base | unsourced on both sides; see §7 #4 | — | UNSOURCED (judgement, not scored as a failure) | see §7 |
| LOE year | 2042 | patent expiry not found in 10-Q or by web search | — | UNKNOWN (stays an assumption; ±2 yrs = ±$5–6) | n/a |
| NOL | 3,967.3 (accumulated deficit) | accumulated deficit 3,967.289 matches. The 80% NOL-use limit and §382 (share count +89% since 2023) are ignored; NOL = 0 gives $61.44 | 10-Q | PASS with note (Model fidelity, −3% worst case) | ≤ −3% |
| SBC treatment | GAAP opex incl. SBC, shares not grown | correct: deducted once, not double counted | 02_model.py | PASS | 0 |
| FCF FY25 | −913.7 | −897.741 − 15.990 = −913.731 | facts | PASS | 0 |
| TV share | 0% (rNPV) / 74.9% going-concern base | recomputed | 02 output | PASS (under the 75% flag) | 0 |
| Discounting | mid-year from 30 Jun, rolled 105 days at WACC | correct. Rolling cash forward at WACC overstates by ~$0.4/sh | code read | PASS | ~0 |

**Result: 16 checked / 3 failed (2 material: IRA omission, vested-option dilution; 1 immaterial: rf).**
Combined, the corrections take the base from $63.38 to **$57.72 (−8.9%)**, the bull from $130.49 to **$119.53 (−8.4%)**, and leave the bear at $15.61 (floored)
or −$2.72 (unfloored). The change exceeds the 5% threshold, so the corrected values are used from here on (`03_rerun.py` §1).
Resolved UNKNOWNs: convert conversion price $198.80; EQRx warrant count 19.73M (2.19M shares). Still UNKNOWN: the
mandatory $250M term-loan draw (no 8-K through the EDGAR list top entry 2026-10-01), patent expiry, and the D&A
tag conflict (7.78 vs 16.56; immaterial).

## 3. Quality of earnings

- **SBC:** FY25 $118.4M = **13.2% of |OCF|**; TTM $218.8M = **17.9% of |OCF|**; FY26 guide $270–290M = 13.0%
  of the opex guide. SBC as a % of revenue is n/m (zero revenue). SBC grew 67.8%/yr over FY20–25 ($8.9M → $118.4M).
- **SBC-adjusted FCF:** FY25 −$1,032.1M; TTM −$1,450.9M.
- **Fair value, SBC as a cash cost (Quant and Skeptic):** base **$57.72**. With SBC added back and no dilution
  (the flattering view, for sizing only): $72.35. **SBC is worth ~$14.6/sh (25%) of base value.**
- **Accruals:** NI was below OCF in every year (gap +8 to +234), mostly SBC. The residual OCF − NI − SBC runs
  from −36.5 to +115.2; FY25's +115.2 includes non-cash royalty accretion (FY25 interest expense $24.2M). Accrued R&D rose
  137.2 → 170.1 in H1-26, which flatters OCF a little. H1-26 NI −1,098.2 vs CFO −741.5: the gap includes the Q2 $151.0M
  non-cash warrant remeasurement, which ends when the warrants expire in Dec 2026. Receivables and inventory: no sales, n/a.
- **Watch item:** per the 10-Q, pre-launch materials were "recorded as research and development expense prior to
  initial regulatory approval". Early RASONQUE gross margins will be **flattered by zero-cost inventory**,
  so do not extrapolate Q3/Q4-26 COGS.
- **Adjusted vs GAAP:** guidance is GAAP and includes SBC. No recurring "non-recurring" add-backs were found.

## 4. Capital allocation (financing discipline, R&D productivity, insiders)

**The Buffett $1 retained-earnings test does not apply.** Accumulated deficit $3.97B, no retained earnings, no dividends.
**Substitute: market value created per $1 of capital paid in, Oct-2021 → Oct-2026.**
Start market cap $27.82 (yfinance close 2021-10-13) × 72.81M (FY21 weighted diluted shares, an approximation
for the period-end count) = $2,025M. Now $41,570M; Δ $39,545M. Capital paid in: ΔAPIC $5,524M (APIC 1,055 at end-21
→ 6,579 at Jun-26, incl. SBC and EQRx stock) + converts $500M + royalty $500M = $6,524M.
**$6.06 per $1 at market; $1.78 at my corrected EV; $3.15 at the ALT EV.** All are > 1.

| Area | Evidence | Read |
|---|---|---|
| Dilution | diluted shares 54.9M (2020) → 190.1M (2025) → 214.3M (Jul-26): 28.2% CAGR | heavy, but normal for the stage |
| Issue prices | Apr-26 follow-on 12.15M sh at **$142.00**; ATM $226.7M in H1-26; converts at a **$198.80** conversion price (40% premium) and 0.50% coupon | 2026 raises were **above my intrinsic value** (EV $64–105), so they were accretive to holders. This is good discipline: selling dear paper |
| Royalty Pharma | $500M for 4.55/2.50/1.00% tiers; implied IRR to RP **21.3% base / 7.6% bear** (`03_rerun.py` §7) | expensive in success, cheap in failure (insurance-like) |
| Term loan | up to $750M, SOFR (3.5% floor) + 5.75%, 2% fee, secured; $250M draw mandatory within 45 days of approval; status **UNKNOWN** | expensive, secured claim ahead of equity |
| R&D productivity | ~$3.76B cumulative operating loss 2021–H1-26 bought an approved first-in-class drug (OS HR 0.40), 3 molecules in Ph3, 5 BTDs | high |
| M&A | EQRx 2023 (terms not verified). Goodwill $14.6M unchanged since 2020 (0.3% of assets); no impairments | no diworsification |
| Lease | 672k sq ft, 15-yr HQ at ~$32M/yr + 3%; landlord affiliates of Farallon (~6.4% holder) = **related party**; committed before revenue | yellow flag |
| Insiders (Form 4) | 0 open-market buys in 12m; ~1.10M sh / $156.7M sold; $48.1M since approval; CEO 80k options exercise-and-sell 2026-08-21 (10b5-1 adopted 05-22) | no insider conviction at these prices |
| Candor | call transcript not obtained | UNKNOWN |

**Capital Allocation Grade: B−.** Raises at rising prices above intrinsic value and strong R&D productivity are the case for B.
Expensive secured and royalty capital, 28%/yr dilution, zero insider buying against $157M of sales, and a large
related-party lease keep it below B. ROIC vs WACC is not measurable (no revenue).

## 5. Probabilities & expected value

**Outside view first.**
- **Reverse-DCF anchor:** $193.95 needs ~**$18.5B** peak WW net sales, 1.94× the Quant base, with 2027 revenue of $1.24B.
- **Phase 3 base rates** (Wong, Siah & Lo, *Biostatistics* 2019, 2000–15 data): oncology P3→approval is **35.5%**
  across all indications, 48.5% for lead indications, and **63.6% with biomarker selection** (RVMD's trials are
  RAS-defined). Corrigendum note: the published correction touched Table 1 P3→APP and Table 2 P2→3 only.
- **Launch base rates:** McKinsey (210 NMEs, 2003–09) found two-thirds of launches below year-1 consensus, and 78% of
  laggards still lagging in year 2. L.E.K. (450+ launches, 2004–19) found ~35% of oncology launches missed
  consensus by ≥20%.

**Adjusting for the evidence.**
- 1L mPDAC: 75%. Same molecule and tumour, OS HR 0.40 in 2L, BTD for the 1L combo.
- 2L RAS NSCLC vs docetaxel: 60%. KRAS-G12C precedents beat docetaxel on PFS, but OS is not assured.
- 1L G12C/G12D NSCLC: 50%. New molecules, combos, and large-pharma competition.
- Adjuvant/CRC: 30%.

The outcomes are correlated (same mechanism). That gives P(bear: 1L PDAC and all NSCLC fail) ≈ 0.25 × 0.5 ≈ 12–15%, and a bull
(everything plus upper-end peaks) at ~20%. That is generous against the launch base rates, but it partly reflects my view in §7 #4
that the Quant's PDAC peaks are conservative.

| Scenario | p | Value (corrected) | Quant 02 value | Skeptic ALT (PDAC re-anchor) |
|---|---|---|---|---|
| Bear | 0.15 | $15.61 (unfloored −$2.72) | $15.60 | $15.61 (unfloored $4.50) |
| Base | 0.65 | $57.72 | $63.38 | $95.21 |
| Bull | 0.20 | $119.53 | $130.49 | $205.76 |
| **EV** | | **$63.76** | $69.63 | $105.38 |
| MoS = 1 − P/EV | | **−204%** | −179% | −84% |
| Asymmetry (EV − P)/(P − bear) | | **−0.73** (−0.66 unfloored) | −0.70 | −0.50 |

**4-point check:** adding a MID state (1L PDAC works, all NSCLC fails, R&D held at $1.8B: **$29.71**) at
12/18/50/20 gives an EV of $59.99. **Robustness:** with bear fixed at 15%, no bull weight reaches the price on either the
corrected values or the ALT values. The price can only be reached if the bull case is close to certain *and* the PDAC peaks sit above my
epidemiology bracket.

## 6. Bear thesis & downside catalysts

The pre-mortem holds, and the model sharpens it. PDAC alone, even on my more generous bracket (~$8.4B base WW),
cannot carry $194. The price needs NSCLC to become a second multi-billion franchise, and that has not yet read out.

1. **NSCLC disappoints (RASolve 301, 2L RAS NSCLC vs docetaxel, "initial readout in 2027").**
   - Signpost: OS hazard ratio.
   - Confirming threshold: **OS HR ≥ 0.80, or a PFS-only win** (sotorasib-like). That removes ~$20/sh from the base and shuts the
     path to the price-implied peak.
2. **PDAC launch below the price-implied path.**
   - Signposts: quarterly RASONQUE net sales from the 2026-11-05 report (unconfirmed date), then the RASolute 303 (1L) readout.
   - Confirming threshold: **FY2027 net sales < $600M** (Quant base $637M vs $1.24B price-implied), or a **1L 303
     OS HR > 0.75 / failure**. 1L PDAC is the single largest value item (~$46/sh).

**Variable that flips the thesis:** aggregate franchise peak sales. The price needs ~$18–20B. That is only plausible
if 1L PDAC *and* NSCLC both succeed commercially at the top of the bracket.

## 7. Disagreements with the Quant (kept, not averaged)

| # | Issue | Quant | Skeptic | Evidence | Effect on FV |
|---|---|---|---|---|---|
| 1 | IRA negotiation | omitted | 8.9% haircut on affected revenue from 2036 (darax) / 2040 (later molecules) to LOE | current law; EPIC Act unenacted (Apr-26) | base −6.5% |
| 2 | Share count | 214.3M basic (+5% shown as a sensitivity only) | treasury-stock method on 9.74M vested options at $25.62 (10-Q). Unvested awards excluded because their expense is already in opex | 10-Q Note 13 | base −2.6%, bull −3.5% |
| 3 | rf | 5.20% (^TNX) | 5.22% (FRED) | orchestrator | −0.2% |
| 4 | **PDAC peak sales (judgement, UNRESOLVED)** | 2L+ 2.5B + 1L 3.5B = **$6.0B** WW base | bracket of **$4.0B + $4.4B = $8.4B**. Anchors: ACS 2026 US pancreatic deaths 52,740 (verified) and WAC $39,800/30d (dossier). ASSUMED: treated share 30%/45%, mean DoT 0.5/0.7 yr, GtN 80%, ex-US +30% | `03_rerun.py` §4 | base $57.72 → **$95.21 (+65%)**; EV $63.76 → $105.38 |
| 5 | Bear floor | floored $15.60; calls unfloored −$2.25 "more honest" | partial agreement: cutting R&D one year earlier (failures known 2027) gives +$2.81 unfloored; EV uses the floored value with the unfloored value shown | `03_rerun.py` §1 | EV −$2.7 if unfloored |
| 6 | Funding the 2028–29 gap "at intrinsic value, neutral" | neutral | raising $1.32B at market ($194) rather than intrinsic would be accretive by ~$4.3/sh; in a bear case it would be dilutive | arithmetic | not applied (timing unknowable) |
| 7 | Converts / royalty liability / warrants | par; not deducted; liability | agree. Conversion price now verified at $198.80 | 10-Q | 0 |
| 8 | 44% steady-state EBIT margin (Quant's own question) | flagged as possibly generous | agree it is high-end, but I have no verified peer margins. Early COGS will also be flattered by expensed pre-launch inventory | 10-Q | not changed |

## 8. Verdict recommendation

**Lynch two-minute drill:** RVMD has just launched the first RAS(ON) inhibitor (OS HR 0.40 in 2L pancreatic
cancer), but at $194 the stock already pays for success in 1L pancreatic *and* lung cancer, about an $18.5B franchise.
The probability-weighted value is $64 ($105 if pancreatic uptake is stronger than the Quant assumes), so the
price is the bull case. Hold a smaller position and let the 2027 readouts and launch numbers earn it back.


Rules (`analyse` § Verdict rules): rNPV requires 40% MoS. Held. Price $193.95 > EV × 1.3 = $82.89 (corrected)
and > $136.99 even on the ALT EV, so the result is **TRIM**. Separately, the outcome rests on unreported Ph3 readouts (the Quant
puts it in Buffett's "too hard" pile), so I also **flag it for review**. Conviction starts HIGH. The corrections count as 2 load-bearing ones (the rf
change is −0.2% and is not counted as load-bearing), so there is no drop for corrections. The unresolved PDAC-peak disagreement is worth > 15% of FV, so conviction drops one level to MEDIUM.

```
VERDICT:        TRIM  (+ flag for review: outcome rests on unreported Ph3 readouts)
AS_OF:          2026-10-13
PRICE:          $193.95 USD (close 2026-10-12)
FAIR_VALUE:     $63.76 (probability-weighted EV, corrected; Skeptic ALT $105.38)
UPSIDE:         -67.1% (ALT -45.7%)
ENTRY_BELOW:    $38.26 (EV x 0.60; ALT $63.23)
EXIT_ABOVE:     $82.89 (EV x 1.30; ALT $136.99) -> price already above
CONVICTION:     MEDIUM
KEY_RISK:       price needs ~$18.5B franchise peak; NSCLC (RASolve 301, 2027) and 1L PDAC (RASolute 303) must both win commercially
DATA_WARNINGS:  2
```
**Reason:** at $193.95 the market prices a ~$18.5B franchise. That is roughly my *bull* case even after re-anchoring
PDAC upward, so EV sits 46–67% below the price on every value set I can defend.

### Sources
- 10-Q Q2-2026, accn 0001193125-26-335104 (EDGAR, fetched 2026-10-13): Notes 8, 10, 11, 12, 13; MD&A liquidity
- EDGAR filing index CIK 1628171 (latest entry 2026-10-01; no 8-K on the term-loan draw)
- yfinance RVMD price history (2021-10-13 $27.82; 2026-10-12 $193.95; 2026-10-13 $192.55)
- FRED DGS10 5.22% on 2026-10-08 (orchestrator-supplied)
- [ACS Key Statistics for Pancreatic Cancer](https://www.cancer.org/cancer/types/pancreatic-cancer/about/key-statistics.html) (2026: 67,530 cases / 52,740 deaths; via search result)
- [Wong, Siah & Lo 2019, Biostatistics](https://www.Gwern.net/doc/biology/2018-wong-2.pdf); [corrigendum](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6409416/)
- [McKinsey, The secret of successful drug launches](https://mckinsey.com/~/media/McKinsey/Industries/Healthcare%20Systems%20and%20Services/Our%20Insights/The%20secret%20of%20successful%20drug%20launches/The_secret_of_successful_drug_launches.pdf); [L.E.K. Launch Monitor](https://www.lek.com/insights/ei/biopharma-launch-trends-lessons-learned-leks-launch-monitor)
- [Public Citizen on EPIC Act, Apr-2026 (Salud y Fármacos)](https://www.saludyfarmacos.org/?p=78126); [PharmaLive on EPIC Act](https://www.pharmalive.com/congress-re-introduces-epic-act-to-remove-iras-pill-penalty/)
