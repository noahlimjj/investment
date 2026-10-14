<!-- pipeline:value-quant -->
# Quant model: VWRA.L (as of 2026-10-13)

Template: **FUND** (dossier §0). Price 193.34 USD (facts: price, yfinance close 2026-10-13). Index trailing P/E 21.0x (facts: index_valuation.pe, Vanguard 31 Aug 2026; yfinance 20.97x agrees). 12m price change +18.1% (facts: price_change_pct.1y). Model: `reports/runs/VWRA.L_2026-10-13/02_model.py`, executed, output pasted in E/F.

Tape check (RULE 0): a cap-weighted index at 21x trailing earnings after +18.1% in 12 months and +81.0% over 3 years (facts) is priced on above-trend earnings and multiples. Nothing below assumes otherwise.

Data warnings (fundamentals.json, 1): `fund/ETF: operating-company metrics do not apply`. Conflicts carried from dossier §10: TER 0.14% vs 0.19% (stale); US weight 61.68% vs 59.77%; holdings 3,784 vs 3,759; 52w range; justETF returns are a different currency.

No DCF of a fund (AGENTS.md routing). Three executable substitutes are used instead:
- **M1**: earnings-yield and CAPE-yield real-return anchors.
- **M2**: 10-yr Bogle decomposition with bear/base/bull inputs. Net return = dividend yield + per-share EPS growth + annualised P/E change − TER − US dividend-WHT leakage − tracking residual.
- **M3**: value-driver justified P/E of the underlying index. Payout = 1 − g/ROE, the same steady-state formula as the `valuation.dcf()` terminal. Used for the reverse solve and the sensitivity grid.

Labels: **ASSUMPTION** means I chose the number and it is not sourced. **PROXY** means a different index or vendor. The Skeptic should attack ASSUMPTIONs first.

## A. Lynch classification & category checks
- **Category: not assigned.** AGENTS.md routing says "FUND ... Do not assign a Lynch category". The fund holds about 3,784 companies (facts: holdings_count), which span every category, so the aggregate has no single category.
- **Category checks:** none apply (no runway, no diworsification, no turnaround plan, no cycle position for the vehicle).
- **PEG:** VOID. Model output: `peg_is_valid(PE=21.0, fwd=None, growth=None) -> False`. No index EPS growth history or forward P/E is in the dossier (facts: forward_pe null), so PEG is not cited anywhere.
- **Lynch ratio** (EPS growth % + dividend yield %) / P/E: **UNKNOWN**. Index EPS growth is not in the dossier, and the dividend yield is a proxy only.
- **Net-cash-adjusted P/E:** not applicable (fund).
- **Inventory/receivables vs sales:** not applicable (fund).
- **Debt structure:** fund-level borrowing is not reported in the dossier, so UNKNOWN. Look-through index leverage is also UNKNOWN.

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)
**Circle of competence / predictability: partly.**
- **Vehicle: yes.** It is mechanical physical optimised sampling (facts: replication). TER is 0.14% (facts) and tracking error is 0.07% / 0.07% / 0.08% over 1/3/5y (facts: tracking_error_pct). This is volatility, not tracking difference.
- **Underlying aggregate earnings 10 years out: no, beyond broad bounds.** The index is 36.04% Technology (facts: sector_pct, justETF only). The top 10 are 23.6% (facts: top10_total_pct), led by NVIDIA 4.77%, Apple 4.24% and Microsoft 3.49%. Alphabet is 3.31% across two lines (dossier §3). Future earnings depend on a handful of AI-capex beneficiaries whose margins cannot be sketched with confidence.

**Moat:** not rated. A fund has no moat (FUND template). Look-through quality, from vendor aggregates:
- **Look-through ROE = P/B ÷ P/E = 3.6 / 21.0 = 17.14%.** Same vendor and same date (facts: index_valuation.pb, .pe). Compare cost of equity 8.00% (§D): spread +9.14 pts. The P/B of 3.6x is the market's capitalisation of that spread.
- **Margin/ROIC 5-yr series:** UNKNOWN. No history is in the dossier, so trend (widening / stable / eroding) is UNKNOWN.
- **CAPE (PROXY) vs trailing P/E:** CAPE 29.12 (facts: proxy_global_cape_siblis) / trailing P/E 21.0 = 1.39x (1.25x against the MSCI P/E of 23.24). This cross-vendor ratio suggests current earnings sit about 25–39% above their 10-yr real average. Earnings are elevated vs trend, which is a bear input, not a moat signal.

**Owner earnings:** not applicable (NI/D&A/capex are null in fundamentals.json). Look-through **earnings yield is 1/21.0 = 4.76%**, or 4.47% net of TER and US WHT leakage. The **CAPE yield (PROXY) is 3.43%**, or 3.15% net. Both are real-return anchors. Nominal = these + inflation, and inflation is UNKNOWN.

**SBC:** index EPS is vendor-defined, and whether it is before or after SBC is UNKNOWN. The M2 growth input is **per-share** EPS growth, so dilution (and buybacks) is carried through share count only. No separate SBC deduction is made, so there is no double count.

## C. GARP & valuation matrix
| Metric | Current | 5-yr own avg | Peer median |
| :--- | :--- | :--- | :--- |
| P/E trailing | 21.0x (Vanguard, 31 Aug); 20.97x yfinance | UNKNOWN (no history in dossier) | UNKNOWN. iShares ACWI 25.18x, MSCI ACWI 23.24x: different vendor definitions, NOT comparable (dossier §8) |
| P/E forward | UNKNOWN | UNKNOWN | PROXY MSCI ACWI 17.13x (31 Jul; flagged unverified, dossier §8) |
| P/B | 3.6x | UNKNOWN | UNKNOWN |
| Earnings yield | 4.76% | UNKNOWN | n/a |
| CAPE | UNKNOWN (PROXY global 29.12x, 1 Jul) | UNKNOWN | n/a |
| Dividend yield | UNKNOWN (PROXY 1.59% MSCI ACWI / 1.40% iShares ACWI) | UNKNOWN | n/a |
| EV/EBITDA, P/FCF, SBC-adj P/FCF, FCF yield | n/a (fund) | n/a | n/a |
| Owner-earnings yield | n/a; look-through earnings yield 4.76% | UNKNOWN | n/a |
| PEG | VOID (no growth input) | – | – |
| Lynch ratio | UNKNOWN (no growth input) | – | – |
| Look-through ROE vs k | 17.14% vs 8.00% | UNKNOWN | UNKNOWN |
| TER | 0.14% (conflict: 0.19% stale) | – | UNKNOWN (no peer TERs in dossier) |
| Tracking difference 1/3/5y | **UNKNOWN** (indicative 0.02%/yr, low reliability) | – | UNKNOWN |
| Tracking error 1/3/5y | 0.07 / 0.07 / 0.08% | – | UNKNOWN |
| Price vs NAV | −0.15% (193.34 on 13 Oct vs NAV 193.64 on 12 Oct; dates differ, indicative only) | – | – |
| Spread | about 0.01% (snapshot) | UNKNOWN | UNKNOWN |

**Exposure and role:**
- US 61.68% (facts; justETF 59.77%), Japan 6.00%, Taiwan 3.31%, UK 3.25%. Non-US total 38.32%.
- Overlap with other lines in the user's book (investor-profile memory, not re-verified):
  - The US sleeve overlaps VOO if VOO is still held (status unconfirmed).
  - The ex-US sleeve overlaps VXUS.
  - TSM is 1.70% of the fund and also a direct holding.
  - NVIDIA at 4.77% is the largest single look-through exposure.
- Holding VWRA + VXUS + VOO together re-weights the portfolio away from market cap, while charging for three wrappers.

## D. Discount rate build
| Component | Value | Source |
| :--- | :--- | :--- |
| Risk-free (10y) | **UNKNOWN** | dossier §1: not collected |
| ERP | 5.0% | stated (Quant instruction) |
| Beta | 1.0 | a cap-weighted all-world index is the market proxy; no sourced beta |
| Cost of debt / weights | n/a | fund. Look-through index leverage UNKNOWN; equity-only rate used |
| CAPM k | rf + 5.0% | – |
| Floor (USD) | 8.0% | Buffett opportunity-cost floor |
| **k used** | **8.00%** | The floor binds for any rf ≤ 3.0%. If rf = 4% then k = 9% (base hurdle-equivalent value 150.49); if rf = 5% then k = 10% (137.36). Output §6 |

SGD-base note: k and all returns are in USD. USD/SGD drift is UNKNOWN. Each ±1%/yr of USD move changes the SGD 10-yr outcome by ×1.105 / ×0.904 (output §6).

## E. Scenarios (M2, 10-yr, nominal USD, net of costs)
| Input | Bear | Base | Bull | Source / rationale |
| :--- | :--- | :--- | :--- | :--- |
| Dividend yield | 1.40% | 1.59% | 1.59% | PROXY, iShares ACWI / MSCI ACWI (dossier §8). FTSE All-World yield UNKNOWN |
| Per-share EPS growth | 3.0% | 5.0% | 7.5% | **ASSUMPTION.** Bounded by computed envelope 3.17% (all retained earnings on buybacks at E/P) to 11.42% (all reinvested at 17.1% ROE). Bear sits at the floor. Bull: no sourced reason for margin expansion exists in the dossier |
| Start P/E | 21.0x | 21.0x | 21.0x | facts |
| Exit P/E yr 10 | 15.0x | 21.0x | 24.0x | **ASSUMPTION.** Bear 15.0x = M3 justified P/E at k 8% / g 2%. Base = no re-rating. Bull 24.0x ≈ M3 justified at k 8% / g 5% (24.8x, above the 4% cap), near MSCI's 23.24x (cross-vendor) |
| TER | 0.14% | 0.14% | 0.14% | facts |
| US WHT leakage | DY × 61.68% × 15% | same | same | 15% is user-stated, unverified (dossier §9). Assumes the US dividend yield equals the index yield (ASSUMPTION) |
| Tracking residual beyond TER | 0 | 0 | 0 | UNKNOWN, swept in §6 of output |
| **Net return / yr** | **0.72%** | **6.30%** | **10.25%** | output §2 |
| Price in yr 10 (USD) | 207.77 | 356.26 | 512.89 | output §2 |
| **Hurdle-equivalent value/share** (price at which the scenario earns exactly k = 8%) | **96.24** (−50.2%) | **165.02** (−14.6%) | **237.57** (+22.9%) | output §2 |

How to read these:
- **Hurdle-equivalent value is not a fair value of the fund.** NAV is that. It is the scenario-consistent equivalent of a DCF per-share value at the 8% hurdle.
- **Terminal share:** in M2, 100% of the value comes from the year-10 exit price, because the fund accumulates and makes no interim distributions. The exit P/E carries the terminal assumption, so this is flagged as above 75% by construction. M3 is a perpetuity (100% terminal).
- **Base composition:** 1.59% yield + 5.00% growth + 0.00% re-rating − 0.29% costs.

### Model output (verbatim)
```

==============================================================================
0. INPUTS
==============================================================================
Price (13 Oct close)              193.34 USD   [facts: price]
NAV (2026-10-12)                 193.64 USD   [facts: nav]
Price vs NAV (dates differ)       -0.15%       indicative only, 1-day date mismatch
Index trailing P/E (Vanguard)      21.00x      [facts]; yfinance 20.97x [fundamentals.json]
Index P/B (Vanguard)                3.60x      [facts]
TER                                0.14%       [facts]
US weight                         61.68%       [facts]
Dividend yield (PROXY MSCI ACWI)   1.59%       [facts proxy]; alt iShares ACWI 1.40% [dossier §8]
CAPE (PROXY Siblis global)         29.12x      [facts proxy]
10y yield                        UNKNOWN   -> cost of equity = floor 8.00%
data warnings (fundamentals.json): ['fund/ETF: operating-company metrics do not apply']

==============================================================================
1. LOOK-THROUGH QUALITY & YIELDS (M1)
==============================================================================
Earnings yield 1/PE                4.76%
CAPE yield 1/CAPE (proxy)          3.43%
Look-through ROE = PB/PE          17.14%   vs cost of equity 8.00%  spread +9.14%
Payout = DY x PE (mixed vendor)   33.39%
Sustainable g, all reinvested     11.42%   (upper envelope, constant ROE)
Sustainable g, all bought back     3.17%   (lower envelope, zero organic growth)
Trailing PE / CAPE gap (cross-vendor): CAPE/PE = 1.39x (FTSE PE), 1.25x (MSCI PE)
Real-return anchor 1/PE         : gross  4.76%  net of TER+US WHT  4.47%   nominal = this + inflation (UNKNOWN)
Real-return anchor 1/CAPE proxy : gross  3.43%  net of TER+US WHT  3.15%   nominal = this + inflation (UNKNOWN)
peg_is_valid(PE=21.0, fwd=None, growth=None) -> False, 'missing growth or P/E'  => PEG VOID, not cited

==============================================================================
2. 10-YEAR SCENARIOS (M2, nominal USD, net of TER and US dividend WHT)
==============================================================================
           DY   EPS g    PE0   PE10 val chg/yr    WHT    TER   gross     NET price yr10 hurdle-eq val   vs px
Bear    1.40%   3.00%   21.0   15.0     -3.31%  0.13%  0.14%   0.99%   0.72%     207.77         96.24  -50.2%
Base    1.59%   5.00%   21.0   21.0      0.00%  0.15%  0.14%   6.59%   6.30%     356.26        165.02  -14.6%
Bull    1.59%   7.50%   21.0   24.0      1.34%  0.15%  0.14%  10.54%  10.25%     512.89        237.57  +22.9%
hurdle k = 8.00% (floor; 10y UNKNOWN). 'hurdle-eq val' = price at which scenario returns exactly k.
No terminal value in M2: 100% of return is earned inside the 10-yr window; exit P/E carries the terminal assumption.
Base return composition: DY 1.59% + EPS g 5.00% + re-rating 0.00% - costs 0.29%

==============================================================================
3. REVERSE SOLVES ('what must be true?')
==============================================================================
(a) 10-yr per-share EPS growth needed to earn the hurdle, base dividend yield & costs
    exit P/E  15.0x -> needed EPS g 10.35%/yr
    exit P/E  18.0x -> needed EPS g  8.35%/yr
    exit P/E  21.0x -> needed EPS g  6.70%/yr
    exit P/E  24.0x -> needed EPS g  5.28%/yr
(b) perpetual nominal growth implied by trailing P/E 21.0x (value-driver, payout = 1 - g/ROE)
    k=7%: ROE 10.0% -> g  4.05%  ROE 13.0% -> g  3.35%  ROE 17.1% -> g  2.94%  ROE 25.0% -> g  2.63%
    k=8%: ROE 10.0% -> g  5.96%  ROE 13.0% -> g  4.88%  ROE 17.1% -> g  4.27%  ROE 25.0% -> g  3.81%
    k=9%: ROE 10.0% -> g  7.94%  ROE 13.0% -> g  6.44%  ROE 17.1% -> g  5.62%  ROE 25.0% -> g  5.00%
    k=10%: ROE 10.0% -> g  9.99%  ROE 13.0% -> g  8.04%  ROE 17.1% -> g  6.98%  ROE 25.0% -> g  6.20%
    terminal-growth cap = min(4%, 10y yield UNKNOWN) -> 4% used as cap

==============================================================================
4. SENSITIVITY: value per share = price x justified PE / 21.0  (ROE held at look-through 17.1%)
==============================================================================
k \ g              2%        3%        4%        5%    (5% column exceeds the 4% cap; shown for reference)
7%             165.90    195.58    244.69    342.37
8%             138.25    156.47    183.52    228.25
9%             118.50    130.39    146.82    171.19
justified trailing P/E:
7%              18.0x     21.2x     26.6x     37.2x
8%              15.0x     17.0x     19.9x     24.8x
9%              12.9x     14.2x     15.9x     18.6x

==============================================================================
5. 10-YR NET RETURN GRID (M2): exit P/E x per-share EPS growth, base DY & costs
==============================================================================
g \ exitPE        15x       18x       21x       24x       27x
2.0%           -0.07%     1.74%     3.30%     4.67%     5.90%
3.0%            0.89%     2.73%     4.30%     5.69%     6.92%
4.0%            1.86%     3.71%     5.30%     6.70%     7.95%
5.0%            2.83%     4.70%     6.30%     7.71%     8.98%
6.0%            3.80%     5.68%     7.30%     8.73%    10.00%
7.5%            5.25%     7.16%     8.80%    10.25%    11.54%

==============================================================================
6. COST & UNKNOWN SWEEPS on base (annual net return; hurdle-eq value)
==============================================================================
  TER 0.14% (base)                             net  6.30%   hurdle-eq  165.02
  drag = indicative TD 0.02% instead of TER    net  6.42%   hurdle-eq  166.89
  stale TER 0.19% (conflict)                   net  6.25%   hurdle-eq  164.24
  +0.30% unexplained tracking residual         net  6.00%   hurdle-eq  160.42
  US WHT 30% (US-domiciled equivalent)         net  6.16%   hurdle-eq  162.75
  US WHT 0%                                    net  6.45%   hurdle-eq  167.32
  DY 1.40% (iShares proxy)                     net  6.13%   hurdle-eq  162.36
  SGD investor: USD/SGD drift UNKNOWN; each +/-1%/yr of USD move = +/-1%/yr SGD return, i.e. 10-yr x1.105 / x0.904
  HYPOTHETICAL 10y = 2%: k = 8.00%  base hurdle-eq value  165.02
  HYPOTHETICAL 10y = 3%: k = 8.00%  base hurdle-eq value  165.02
  HYPOTHETICAL 10y = 4%: k = 9.00%  base hurdle-eq value  150.49
  HYPOTHETICAL 10y = 5%: k = 10.00%  base hurdle-eq value  137.36

==============================================================================
7. LOAD-BEARING INPUTS: +/-10% of each input, base case
==============================================================================
base: net 6.30%/yr, hurdle-eq value 165.02, perpetual value 183.52 (k 8%, g 4%)
  starting P/E (measurement)   -10%: net  7.42% val  183.12 (+11.0%)   +10%: net  5.31% val  150.19 ( -9.0%)
  exit P/E (yr 10)             -10%: net  5.20% val  148.71 ( -9.9%)   +10%: net  7.31% val  181.31 ( +9.9%)
  per-share EPS growth         -10%: net  5.80% val  157.42 ( -4.6%)   +10%: net  6.80% val  172.95 ( +4.8%)
  dividend yield               -10%: net  6.16% val  162.79 ( -1.3%)   +10%: net  6.45% val  167.27 ( +1.4%)
  US WHT rate                  -10%: net  6.32% val  165.25 ( +0.1%)   +10%: net  6.29% val  164.79 ( -0.1%)
  US weight                    -10%: net  6.32% val  165.25 ( +0.1%)   +10%: net  6.29% val  164.79 ( -0.1%)
  TER                          -10%: net  6.32% val  165.24 ( +0.1%)   +10%: net  6.29% val  164.80 ( -0.1%)
  hurdle k 7.20%           value  177.76 ( +7.7%)
  hurdle k 8.80%           value  153.28 ( -7.1%)
  ROE -10% (perpetual M3)      perpetual value  177.31 ( -3.4%)
  ROE +10% (perpetual M3)      perpetual value  188.60 ( +2.8%)
  terminal g -10% (3.6%)       perpetual value  171.25 ( -6.7%)
  terminal g +10% (4.4%)       perpetual value  198.47 ( +8.1%)
```

## F. Reverse solve & sensitivity
From the output above (§3–§5):

**Reverse, 10-yr (output §3a).** The per-share EPS growth needed to earn the 8% hurdle at today's price depends on the exit P/E:

| Exit P/E | Required EPS growth |
| :--- | :--- |
| 15x | 10.35%/yr |
| 18x | 8.35%/yr |
| 21x (no re-rating) | 6.70%/yr |
| 24x | 5.28%/yr |

**Reverse, perpetual (output §3b).** At k = 8% and look-through ROE 17.1%, the 21.0x trailing P/E implies **4.27% perpetual nominal per-share growth**. That is just above the 4% terminal cap.
- ROE 13%: 4.88%.
- k = 7%: 2.94%.
- k = 9%: 5.62%.

**What must be true:** to earn 8% in USD from here, index per-share EPS must compound at about 6.7%/yr with no de-rating. Equivalently, the market must hold about 21x while growing faster than the 4% perpetual cap allows.

**Sensitivity (output §4).** The k ±1% × g grid (ROE 17.1%) runs from 118.50 (k 9%, g 2%) to 244.69 (k 7%, g 4%). The centre (k 8%, g 4%) is 183.52. The 5% column breaches the cap and is shown for reference only.

**10-yr return grid (output §5).** Net returns range from −0.07% (g 2%, exit 15x) to 11.54% (g 7.5%, exit 27x).

## G. Load-bearing inputs (±10%, base case; output §7)
| # | Input | Base value | Source | −10% → value | +10% → value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Starting P/E (measurement/definition) | 21.0x | facts (Vanguard); vendors disagree 21.0–25.2x | 183.12 (+11.0%) | 150.19 (−9.0%) |
| 2 | Exit P/E yr 10 | 21.0x | ASSUMPTION | 148.71 (−9.9%) | 181.31 (+9.9%) |
| 3 | Hurdle k (10y yield UNKNOWN) | 8.0% | floor | 177.76 (+7.7%) at 7.2% | 153.28 (−7.1%) at 8.8% |
| 4 | Perpetual g (M3) | 4.0% | cap | 171.25 (−6.7%) | 198.47 (+8.1%) |
| 5 | Per-share EPS growth | 5.0% | ASSUMPTION | 157.42 (−4.6%) | 172.95 (+4.8%) |
| 6 | Look-through ROE (M3) | 17.14% | P/B ÷ P/E, facts | 177.31 (−3.4%) | 188.60 (+2.8%) |
| 7 | USD/SGD drift (SGD investor) | UNKNOWN | – | ±1%/yr = ×0.904 / ×1.105 on 10-yr SGD outcome | – |
| 8 | Dividend yield | 1.59% | PROXY (MSCI ACWI) | 162.79 (−1.3%) | 167.27 (+1.4%) |
| 9 | Tracking difference beyond TER | UNKNOWN (0) | – | +0.30%/yr residual → 160.42 (−2.8%) | indicative 0.02% TD → 166.89 (+1.1%) |
| 10 | TER / US WHT rate / US weight | 0.14% / 15% / 61.68% | facts / user-stated / facts | each about ±0.1% | – |

Costs are not load-bearing for valuation. Even US WHT at 30% (the US-domiciled equivalent) costs only 0.14%/yr (6.16% vs 6.30%). Valuation level (start and exit P/E) and the discount rate dominate.

## H. Open questions for the Skeptic
1. **Which trailing P/E is real?** Vanguard 21.0x, MSCI ACWI 23.24x and iShares 25.18x differ by up to 20%, and input #1 moves value about 10%. The FTSE vendor definition (GAAP vs operating, ex-negative earners or not) is UNKNOWN.
2. **Earnings above trend.** CAPE (PROXY 29.12) / trailing P/E of 1.25–1.39x suggests trailing EPS is well above its 10-yr real average. The base case grows from that elevated base with no reset. Should the base include a partial earnings normalisation? The bear already proxies this through the 15x exit.
3. **Base growth of 5% is my ASSUMPTION**, with no sourced index EPS history. The computed envelope (3.17–11.42%) is wide. The 10-yr reverse needs 6.7% at a constant 21x.
4. **The 8% floor binds only because the 10y yield is UNKNOWN.** If rf exceeds 3%, k rises and every hurdle-equivalent value falls (rf 4% → base 150.49).
5. **Tracking difference is UNKNOWN.** Tracking error of 0.07% says nothing about the level. Tracking difference is the actual cost metric for a core holding.
6. **The WHT 15% treaty premise is unverified** (dossier §9), and so is whether the FTSE benchmark used is net or gross of WHT. Non-US WHT leakage is UNKNOWN and not modelled.
7. **Dividend yield is a PROXY** (MSCI ACWI). The 1.32% unlabeled Vanguard figure was correctly excluded.
8. **Concentration:** top 10 = 23.6%, Technology 36.04% (single non-issuer source). Does that make a "diversified core" premise weaker than the 3,784-name count suggests?
9. **Portfolio overlap with VXUS (and VOO, if held)** is a role question for the Skeptic and orchestrator, not a valuation input.
