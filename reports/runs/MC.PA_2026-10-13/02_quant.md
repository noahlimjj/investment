<!-- pipeline:value-quant -->
# Quant model: MC.PA (as of 2026-10-13)

LVMH Moet Hennessy Louis Vuitton, Euronext Paris, EUR. EUR millions unless stated. Template: **FULL** (dossier §0): consolidated DCF is primary, segment-multiple cross-check is secondary, no SOTP. Model: `reports/runs/MC.PA_2026-10-13/02_model.py` (executed 2026-10-13; reads `facts.json` and `data/fundamentals.json` directly). Inputs tagged ASSUMPTION are my judgement calls. The Skeptic should challenge those first. This file contains no probabilities and no verdict.

**Tape check (RULE 0).** Price EUR 381.65 (facts: market.price_eur). Trailing P/E is 17.4x on own TTM diluted EPS of 21.94 (facts: ttm.eps_diluted), or 17.6x per fundamentals.json. The stock is down 27.6% over 12 months (facts: change_12m_pct) and sits at the bottom of its 52-week range. FY2025 EPS is 28% below the FY2023 peak, and PRO margin is at its 5-year low. Tape and fundamentals agree: this is a de-rating on falling earnings. The open question is whether the trough is cyclical or structural, and Section H puts that question to the Skeptic.

**Data-layer warnings (RULE 1).** fundamentals.json carries 1 warning: "cash-flow net income 17,099,000,000 differs from income-statement 10,878,000,000 by +57% (IFRS pre-tax start?) - income statement used". The corrected NI of 10,878 is used throughout. Two further notes:
- The data layer's `peg_valid: true` conflicts with my gate, which returns VOID (Section A). I do not use the data-layer PEG.
- fj capex is 4,670, while company operating investments are 4,567 (dossier §2). I use the company figure, except in the fj owner-earnings line, which is reproduced as published.

**Conventions stated once:**
- **IFRS 16.** Lease cash (principal 2,974 + interest 553, FY2025) is treated as an operating cost. EBIT is restated to pre-IFRS 16 as PRO − (lease cash − ROU depreciation), and D&A excludes ROU depreciation. **Lease liabilities (16,261) are therefore excluded from the EV bridge.** They are never both deducted and added.
- **SBC.** Bonus-share expense (FY2025 159, TTM 187) is already charged inside PRO under IFRS 2 and is never added back. The share count is held flat at 495.811m. SBC is deducted, not diluted.
- **EV bridge.** Claims = NFD 8,245 + minority put commitments 6,416 + minority interests at book 1,599 = **16,260** (facts: interim.H1_2026). NFD already nets cash and current AFS assets (checked: 20,485 − 6,803 − 5,399 = 8,283 vs 8,245, with the difference being hedges). DFS held-for-sale net assets (+2.1/share) and non-current investments (UNKNOWN) are not credited.
- **Valuation date and base.** Base revenue is TTM to 9M-2026 = 79,865 (facts: ttm.revenue_ttm_to_9m2026). Year 1 is roughly Q4-2026 to Q3-2027 and uses end-of-year discounting, which is conservative by about half a year.

```
0. SNAPSHOT AND EV BRIDGE
Price EUR 381.65 | shares 495.811m | market cap 189,226
Claims: NFD 8,245 + minority puts 6,416 + minorities (book) 1,599 = 16,260  (32.79/share)
EV ex-leases (model basis) 205,486 | EV incl. leases (IFRS 16 basis) 221,747
Cross-check: TTM minority share of profit 449 x own P/E 17.4 = 7,810 vs puts+book 8,015 (not used; shows bridge is not light)
```

## A. Lynch classification & category checks

**Growth facts (facts: annual):**
- Revenue CAGR FY2021–FY2025 is +5.9% (64,215 → 80,807). YoY: +23.3%, +8.8%, −1.7%, −4.6%.
- Diluted EPS CAGR is −2.2% (23.89 → 21.85). YoY: +17.3%, +8.2%, −17.2%, −13.0%. FY2025 is −28.0% vs the FY2023 peak.
- CONSENSUS (Yahoo, labelled, dossier §9): EPS CAGR FY25–27 is +5.7%.

**Classification: Cyclical (the luxury-demand cycle), currently at or near trough margins, on what was a Stalwart franchise. The category is changing.**
- On the 5-year numbers alone, EPS growth below 5% puts it in Slow Grower territory, and revenue at about 6% is below the Stalwart band of 10–12%.
- The EPS path is boom then bust: +17%, +8%, −17%, −13%. That is the Cyclical signature, and Lynch's rule for cyclicals (value on mid-cycle earnings) is the right valuation discipline here.
- The orchestrator asked whether this is a cyclical trough or a structural de-rating. The data supports both readings:
  - *Cyclical reading.* Gross margin has held at 66–69% throughout. H1-26 gross margin was 67.1% vs 66.8% in H1-25 (facts: interim), so it is stabilising. W&J (+8%), SR (+6%) and W&S (+5%) grew organically over 9M-26 (facts: Q3_2026). The Q3 FLG −5% is tied to China, plus a >1pt one-off Louis Vuitton logistics hit (dossier §4, secondary).
  - *Structural reading.* FLG PRO margin has fallen **every year since FY2021**: 41.6% → 40.6% → 39.9% → 37.1% → 35.0% → 34.1% (H1-26). That includes FY2022–23, when FLG revenue grew 25% and 9%. A margin that falls during a boom is not just operating deleverage. FLG is 74% of group PRO.
  - Implication: if structural, the right mid-cycle margin is below the 5-year average, and the category drifts toward Slow Grower. Section H, Q1 covers this.

**Cyclical checks:**
- Where are we in the cycle? PRO margin history is 26.7%, 26.6%, 26.5%, 23.1%, 22.0%, and TTM is 21.9%. The 5-year range is 22.0–26.7% with an average of 25.0%, so we are **at the 5-year low**. That is the reverse of the "low P/E at peak margins" trap.
- Normalised (mid-cycle) EPS is **26.52**. It is built as PRO at the 5-year average margin on TTM revenue, plus FY25 net financial and other operating items, taxed at the 5-year average ETR of 28.1%, less 3.1% minorities. The **normalised P/E is 14.4x**, against 17.4x trailing.
- Caveat: the 5-year window contains three post-COVID boom years (FY21–23), so the "average" may sit above a true mid-cycle margin.

**Stalwart checks:**
- P/E vs its own 5-year range: **UNKNOWN**, because the dossier has no historical price series. The one data point is 12 months ago: 527.18 / FY2024 EPS 25.12 = 21.0x, against 17.4x now.
- Diworsification:
  - The non-core businesses are Selective Retailing (Sephora, DFS), hotels (Belmond, Cheval Blanc) and media (Les Echos). SR is 23% of revenue but only 10% of PRO in FY2025 (1,780 / 17,755).
  - The portfolio is now being pruned: DFS Greater China was sold (Jan 2026, est. loss c.0.5bn) and Marc Jacobs was sold (1 Sep 2026). Impairments, mainly DFS, are in other operating items (−656 FY25, −664 FY24). Goodwill fell from 24,022 (FY23) to 18,315 (FY25) (dossier §5).
  - The Tiffany-era W&J (13,226 cash for acquisitions in 2021) has seen PRO margin fall from 18.7% (FY21) and 19.8% (FY23) to 14.4% (FY25) (facts: segments, own arithmetic). The return on that deal is not evidenced as strong.

**Slow-grower checks (the downside category):**
- FY2025 payout is 59.5% of EPS; EPS covers the dividend 1.68x.
- Operating FCF / dividends paid incl. minorities = 1.59x. On Group-share dividends of 6,463 it is 1.75x.
- DPS was 10, 12, 13, 13, 13 for FY21–25. It has been held flat for 3 years with no cut.

**Lynch metrics:**

| Metric | Formula | Value |
|---|---|---|
| PEG | `peg_is_valid(17.4, 15.7, min(hist −2.2%, consensus 5.7%))` | **VOID**: growth −2.2% ≤ 0, PEG undefined. Not cited. |
| Lynch ratio (historical) | (EPS CAGR −2.2 + yield 3.41) / P/E 17.4 | **0.07** (poor, <1) |
| Lynch ratio (CONSENSUS FY25–27) | (5.7 + 3.41) / 17.4 | **0.53** (poor, <1) |
| Net-cash-adjusted P/E | (381.65 − (−8,245/495.8 = −16.63)) / 21.94 | **18.2x**; 18.7x incl. minority puts |
| Inventory growth vs sales | — | **UNKNOWN**: facts.json has no inventory series |
| Receivables growth vs sales | — | **UNKNOWN**: facts.json has no receivables series |
| Net debt / owner earnings | NFD 8,245 / lease-adj OE 11,338 | **0.73x**; 1.29x incl. puts; 2.18x incl. puts + leases vs fj OE 14,209 |
| Maturity wall | 2026 7,923; 2027 1,986; 2028 1,767 (facts: Note 19.2) | Cash + AFS 12,202 (Jun-26) covers 2026–27. Interest cover is 51x (PRO / cost of NFD 348), or 19.7x incl. lease interest |

The missing inventory series matters for a cyclical. In the FY2024 cash calibration (Section 2 output), the model overstates cash by 2,101 (2.48% of revenue) in a year when revenue fell. That fits an inventory build, but I cannot attribute it.

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence / predictability: PARTLY.**
- Revenue can be sketched 10 years out with moderate confidence. There are five business groups, 6,283 stores, US 26% / Asia ex-Japan 26% / Europe 26% (dossier §8), and a 5.9% revenue CAGR.
- **Margins cannot be.** PRO margin swung from 26.7% to 21.9% in about 2.5 years, and FLG margin has fallen five years running. China demand has no recovery timeline (CFO, secondary §4). Asia ex-Japan has fallen from 31% to 26% of revenue.
- Fair value is roughly linear in the steady-state margin (Section G), so the predictability gap sits exactly on the load-bearing input.

**Moat, from evidence only:**
- *Gross margin (pricing power).* 68.3%, 68.4%, 68.8%, 67.0%, 66.2% (FY21–25). H1-26 is 67.1% vs 66.8% in H1-25. That is a 2.6-point range, down 2.6 points from peak but stabilising. Gross margin stayed above 66% through a −4.6% revenue year with no price cuts (CFO: "price cuts not part of strategy", secondary). Part of the decline is probably mix, since lower-margin SR grew while FLG shrank, but gross margin by segment is UNKNOWN.
- *ROIC.* NOPAT = PRO × (1 − ETR); invested capital = total equity + NFD.
  - Values: 21.6%, 23.5%, 22.9%, 17.8%, 15.7% (5-yr average 20.3%).
  - Including leases in invested capital: 17.4%, 19.0%, 18.7%, 14.5%, 13.0%.
  - ROIC has been above WACC in every year, but it is down 7.8 points from peak.
- *Capital intensity.* Capex/revenue ranges 4.1–8.7% (5-yr average 6.3%); capex/D&A ex-ROU ranges 0.85–1.80. Low intensity.
- *Market share.* UNKNOWN (not disclosed, dossier §8).
- **Rating: WIDE. Trend: ERODING.** ROIC fell two consecutive years, FLG margin is down 6.6 points over 4 years, and gross margin is down 2.6 points from peak. It is not yet proven structural, because the gross-margin stabilisation in H1-26 argues cyclical.

**Owner earnings (FY2025):**

| Version | Build | EUR m | Yield on mkt cap 189,226 |
|---|---|---|---|
| AGENTS.md definition (fj) | NI 10,878 + D&A 8,001 − capex 4,670 | 14,209 | 7.51% |
| Lease-adjusted (used) | 10,878 + 8,001 − 4,567 − lease principal 2,974 | 11,338 | **5.99%** |
| SBC-adjusted | SBC is already expensed in NI, so the line above is SBC-burdened. FCF-based: TTM company FCF 11,401 − SBC 187 | 11,214 | 5.93% |

The fj version flatters because its D&A includes 3,143 of ROU depreciation while the lease cash is never deducted. Minor inconsistency: NI is Group share, while D&A is 100% consolidated (minorities take 3.1% of profit).

**ROIC vs WACC:**
- FY2025 ROIC is **15.7% against a 9.5% WACC**, a spread of +6.2 points, down from +12–14 points in FY21–23. Including leases it is 13.0%, a spread of +3.5 points.
- Goodwill/IC is 24.2% in FY2025, below the 30% threshold, so headline ROIC is the relevant figure. Ex-goodwill ROIC is 20.8%.
- FY2023 was above the threshold (32.7%), with ex-goodwill ROIC of 34.0%.
- Acquired brand intangibles (e.g. Tiffany) are not in the dossier, so organic ROIC ex-all-acquired-intangibles is UNKNOWN. It would be higher.
- For the thesis, **headline ROIC is the one that matters**, because shareholders paid for the acquisitions.

## C. GARP & valuation matrix

| Metric | Current | 5-yr own average | Peer median (dossier §7; RMS, KER, CFR, Prada) |
|---|---|---|---|
| EV/EBITDA, IFRS 16 basis (EV incl. leases 221,747 / TTM PRO + D&A 25,291) | 8.8x (Yahoo basis: 10.8x) | UNKNOWN (no price history) | 16.2x (Yahoo basis) |
| EV/EBITDA, pre-IFRS 16 (EV ex-leases 205,486 / FY25 adj. EBITDA 22,229) | 9.2x | UNKNOWN | n/a (basis differs) |
| P/E trailing | 17.4x (own) / 17.6x (fj) | UNKNOWN (12m ago: 21.0x) | 30.3x (3 peers; KER n/a) |
| P/E forward | 15.7x (fj); 17.2x / 15.6x on CONSENSUS FY26 / FY27 EPS | UNKNOWN | 21.3x |
| P/E on normalised mid-cycle EPS 26.52 | 14.4x | UNKNOWN | n/a |
| P/FCF (company FCF TTM 11,401) | 16.6x | UNKNOWN | n/a |
| P/FCF, SBC-adjusted | 16.9x | UNKNOWN | n/a |
| FCF yield, company definition (after lease principal) | 6.03% | UNKNOWN (5-yr avg FCF *margin* 13.9%) | n/a |
| FCF yield, OCF − capex (Yahoo basis, comparable to peers) | 7.60% (Yahoo: 6.1%) | UNKNOWN | 3.15% |
| Owner-earnings yield (fj / lease-adj) | 7.51% / 5.99% | UNKNOWN | n/a |
| PEG | VOID (not cited) | — | — |
| Lynch ratio (historical / consensus growth) | 0.07 / 0.53 | UNKNOWN | n/a |
| Dividend yield | 3.41% | UNKNOWN | n/a |

Notes on the peer comparison:
- On the same Yahoo basis, LVMH trades at about two-thirds of the peer-median EV/EBITDA (10.8x vs 16.2x), about 0.74x the peer forward P/E (15.7x vs 21.3x), and about twice the peer FCF yield (6.1% vs 3.15%).
- Peer figures come from a single vendor, in mixed currencies and fiscal years. Prada's multiples were flagged as unchecked (dossier §7).
- The "5-yr own average" column is UNKNOWN because the dossier has no historical prices.

Segment cross-check (secondary, not used for fair value):
```
10. SEGMENT-MULTIPLE CROSS-CHECK (secondary; peer P/E used as EV/NOPAT proxy)
FY2025 segment PRO (trough)        FLG+W&J @ peer fwd median 21.3x, others @ Prada 9.7x   : EUR 465/share
FY2025 segment PRO (trough)        FLG+W&J @ peer fwd median 21.3x, others @ LVMH fwd 15.7x: EUR 491/share
5-yr avg segment PRO (mid-cycle)   FLG+W&J @ peer fwd median 21.3x, others @ Prada 9.7x   : EUR 522/share
5-yr avg segment PRO (mid-cycle)   FLG+W&J @ peer fwd median 21.3x, others @ LVMH fwd 15.7x: EUR 550/share
FLG+W&J at Prada 9.7x and others at 9.7x (FY25): EUR 217/share
```
How to read it: if FLG + W&J earned peer-median forward P/E, the price would be low by a wide margin. If everything earned Prada's 9.7x, it would be 217. The market is pricing LVMH's luxury segments well below the Hermès/Richemont multiple, so the cross-check bounds the answer but does not decide it. Peer P/E is an equity multiple applied here to segment NOPAT; peers' net cash and the absence of spirits or beauty-retail peer data both bias this.

## D. Discount rate build

```
5. DISCOUNT RATE
Ke = 4.75% + 1.0 x 5% = 9.75%
Kd pre-tax 4.75% (OAT proxy; historic cost of NFD on avg NFD = 4.33%); after tax at 28.1% = 3.42%
Weights: equity-like 197,241 (96.0%), net debt 8,245 (4.0%)
WACC = 9.50%; floor (local 10y + 4%) = 8.75%; USED = 9.50%
Rounded WACC used in DCF: 9.5%
```
- **ERP 5%** and **beta 1.0** follow the instructions (no sourced beta in the dossier).
- The risk-free rate is the France 10-year OAT of **~4.75%, from a SECONDARY source** (TradingEconomics snippet for 7 Oct, not verified for 13 Oct; dossier §1, §10 item 10).
- Kd uses the OAT as a proxy, because LVMH's credit spread is UNKNOWN. The historic cost of NFD is 4.3%. At a 4% debt weight this is immaterial.
- Minority puts and book minorities are weighted at Ke, as equity-like claims. Leases are excluded from the weights, consistent with the EV bridge.
- The local-currency floor of 10y + 4% = 8.75% does not bind; the CAPM result is 9.50%.
- Flag: the OAT includes a French sovereign spread, while only 8% of revenue is French and 21% is invoiced in EUR (dossier §2). A Bund-based rate would be lower, but the Bund yield is UNKNOWN. At WACC 8.5%, base value is 427/share (Section F grid).

## E. DCF scenarios

All four scenarios share: base revenue 79,865 (facts TTM to 9M-26); WACC 9.5% (held constant, so scenario differences are operational; WACC risk is in the grid); 10-year horizon; reinvestment-linked terminal value via `valuation.dcf()`; claims 16,260; 495.811m shares.

All four scenarios also share these costs, each as a % of revenue:
- Lease adjustment of 0.48% (FY2025: lease cash 3,527 − ROU depreciation 3,143).
- D&A ex-ROU of 5.03% (5-yr average).
- Capex of 6.26% (5-yr average).

| Input | BEAR | TROUGH-MARGIN | BASE | BULL |
|---|---|---|---|---|
| Growth path, yr 1–10 | −1, −3, +2, +3, +3, +3, +2.5, +2.5, +2, +2 | same as BASE | +1, +4.5, +5, +5, +5, +4.5, +4, +4, +3.5, +3 | +2, +6, +7, +7, +6.5, +6, +5.5, +5, +4.5, +4 |
| Growth anchor | Q3 FLG −5% / Asia −5% persists. The yr-2 downturn is milder than FY25 reported (−4.6%) | — | Yr 1: 9M organic +2% less ~1pt scope (DFS, Marc Jacobs). Yr 2: CONSENSUS FY27 rev +4.6%. Yrs 3–5: 5%, below the 5.9% FY21–25 CAGR | Above the FY21–25 CAGR; FX headwind eases 2027 (CFO, secondary) |
| PRO margin path | 21.2, 20.5, 21.0, 21.5, then 22.0% (5-yr low) | 21.9% flat (TTM trough) | 21.9% rising linearly to 25.0% (5-yr avg) by yr 5 | 22.2, 23.5, 25.0, then 26.5% (FY21–23 level) from yr 4 |
| Margin anchor | FY24→25 lost 1.1pt on −4.6% revenue; FX −70bps (CFO, secondary) | TTM 17,434 / 79,641 | Mid-cycle = 5-yr average (facts) | FY21–23 actuals 26.5–26.7%, FLG 39.9–41.6% |
| Cash-conversion gap (WC/other) | 2.48% (FY24, worst) | 1.49% (avg) | 1.49% (avg) | 0.49% (FY25) |
| Tax rate | 30.0% (H1-26 ETR) | 28.1% (5-yr avg) | 28.1% | 26.2% (FY21 ETR) |
| Terminal growth | 2.0% | 3.0% | 3.0% | 3.5% |
| Terminal ROIC | 12% | 15% | 15% (FY25 actual 15.7%) | 20% (5-yr avg 20.3%) |
| **Per-share value** | **EUR 213** | **EUR 309** | **EUR 355** | **EUR 486** |
| vs 381.65 | −44% | −19% | −7% | +27% |
| TV share of EV | 53% | 55% | 55% | 58% |

No scenario has terminal value above 75% of EV, so no flag. Terminal growth is at most 3.5% in every case, within the cap of min(4%, 4.75%).

There is no numeric management guidance: the Q3 and H1 releases are qualitative only (dossier §3). The base therefore uses the labelled consensus for year 2 only. That is a revenue growth estimate, not a broker valuation or rating (RULE 2).

The cash-conversion gap comes from FY2024–25. It is the model's pre-working-capital FCF minus reported company FCF plus after-tax cost of NFD (Section 2 output). It captures working capital, tax timing and cash restructuring.

The base FCF margin at steady state is 14.9%, against a 5-yr average company FCF margin of 13.9% (levered, and including the FY22–23 high-capex years). That anchors on the 5-yr average, as instructed.

```
6. DCF SCENARIOS (10 yr, FCFF, pre-IFRS16 basis)
--- BEAR: WACC 9.5% | g_T 2.0% | ROIC_T 12% | tax 30.0% | capex+gap 8.74% | D&A 5.03% | lease adj 0.48%
growth:     -1.0% -3.0% +2.0% +3.0% +3.0% +3.0% +2.5% +2.5% +2.0% +2.0%
PRO margin: 21.2% 20.5% 21.0% 21.5% 22.0% 22.0% 22.0% 22.0% 22.0% 22.0%
Yr     Revenue   EBITDA     EBIT     D&A  Cap+gap      FCF   FCF%       PV
1       79,066   20,367   16,386   3,981    6,910    8,537  10.8%    7,796
2       76,694   19,219   15,358   3,861    6,702    7,905  10.3%    6,593
3       78,228   19,994   16,056   3,938    6,836    8,337  10.7%    6,350
4       80,575   20,997   16,941   4,056    7,041    8,869  11.0%    6,169
5       82,992   22,019   17,841   4,178    7,253    9,409  11.3%    5,977
6       85,482   22,680   18,376   4,304    7,470    9,691  11.3%    5,622
7       87,619   23,246   18,835   4,411    7,657    9,934  11.3%    5,263
8       89,810   23,828   19,306   4,521    7,848   10,182  11.3%    4,926
9       91,606   24,304   19,692   4,612    8,005   10,386  11.3%    4,589
10      93,438   24,790   20,086   4,704    8,165   10,593  11.3%    4,275
PV explicit 57,560 | PV terminal 64,275 (53% of EV)
EV 121,834 - claims 16,260 = equity 105,574 -> EUR 213/share vs 381.65 (-44%)

--- TROUGH: WACC 9.5% | g_T 3.0% | ROIC_T 15% | tax 28.1% | capex+gap 7.74% | D&A 5.03% | lease adj 0.48%
growth:     +1.0% +4.5% +5.0% +5.0% +5.0% +4.5% +4.0% +4.0% +3.5% +3.0%
PRO margin: 21.9% 21.9% 21.9% 21.9% 21.9% 21.9% 21.9% 21.9% 21.9% 21.9%
Yr     Revenue   EBITDA     EBIT     D&A  Cap+gap      FCF   FCF%       PV
1       80,664   21,335   17,275   4,061    6,247   10,239  12.7%    9,351
2       84,294   22,296   18,052   4,244    6,528   10,700  12.7%    8,924
3       88,508   23,410   18,954   4,456    6,855   11,235  12.7%    8,557
4       92,934   24,581   19,902   4,679    7,197   11,796  12.7%    8,205
5       97,580   25,810   20,897   4,913    7,557   12,386  12.7%    7,868
6      101,971   26,971   21,838   5,134    7,897   12,944  12.7%    7,509
7      106,050   28,050   22,711   5,339    8,213   13,461  12.7%    7,132
8      110,292   29,172   23,620   5,553    8,542   14,000  12.7%    6,773
9      114,152   30,193   24,446   5,747    8,841   14,490  12.7%    6,402
10     117,577   31,099   25,180   5,919    9,106   14,924  12.7%    6,022
PV explicit 76,743 | PV terminal 92,644 (55% of EV)
EV 169,387 - claims 16,260 = equity 153,127 -> EUR 309/share vs 381.65 (-19%)

--- BASE: WACC 9.5% | g_T 3.0% | ROIC_T 15% | tax 28.1% | capex+gap 7.74% | D&A 5.03% | lease adj 0.48%
growth:     +1.0% +4.5% +5.0% +5.0% +5.0% +4.5% +4.0% +4.0% +3.5% +3.0%
PRO margin: 21.9% 22.7% 23.4% 24.2% 25.0% 25.0% 25.0% 25.0% 25.0% 25.0%
Yr     Revenue   EBITDA     EBIT     D&A  Cap+gap      FCF   FCF%       PV
1       80,664   21,335   17,275   4,061    6,247   10,239  12.7%    9,351
2       84,294   22,944   18,701   4,244    6,528   11,166  13.2%    9,313
3       88,508   24,773   20,317   4,456    6,855   12,215  13.8%    9,303
4       92,934   26,727   22,048   4,679    7,197   13,340  14.4%    9,279
5       97,580   28,814   23,902   4,913    7,557   14,547  14.9%    9,241
6      101,971   30,111   24,977   5,134    7,897   15,202  14.9%    8,819
7      106,050   31,315   25,976   5,339    8,213   15,810  14.9%    8,376
8      110,292   32,568   27,016   5,553    8,542   16,442  14.9%    7,955
9      114,152   33,708   27,961   5,747    8,841   17,018  14.9%    7,519
10     117,577   34,719   28,800   5,919    9,106   17,528  14.9%    7,073
PV explicit 86,229 | PV terminal 105,964 (55% of EV)
EV 192,192 - claims 16,260 = equity 175,932 -> EUR 355/share vs 381.65 (-7%)

--- BULL: WACC 9.5% | g_T 3.5% | ROIC_T 20% | tax 26.2% | capex+gap 6.75% | D&A 5.03% | lease adj 0.48%
growth:     +2.0% +6.0% +7.0% +7.0% +6.5% +6.0% +5.5% +5.0% +4.5% +4.0%
PRO margin: 22.2% 23.5% 25.0% 26.5% 26.5% 26.5% 26.5% 26.5% 26.5% 26.5%
Yr     Revenue   EBITDA     EBIT     D&A  Cap+gap      FCF   FCF%       PV
1       81,462   21,799   17,698   4,101    5,499   11,661  14.3%   10,650
2       86,350   24,229   19,882   4,347    5,829   13,189  15.3%   11,000
3       92,395   27,311   22,660   4,651    6,237   15,135  16.4%   11,528
4       98,862   30,706   25,729   4,977    6,674   17,289  17.5%   12,026
5      105,288   32,702   27,401   5,301    7,107   18,413  17.5%   11,696
6      111,605   34,664   29,045   5,619    7,534   19,518  17.5%   11,322
7      117,744   36,570   30,643   5,928    7,948   20,591  17.5%   10,909
8      123,631   38,399   32,175   6,224    8,346   21,621  17.5%   10,461
9      129,194   40,127   33,623   6,504    8,721   22,593  17.5%    9,983
10     134,362   41,732   34,967   6,764    9,070   23,497  17.5%    9,481
PV explicit 109,056 | PV terminal 148,174 (58% of EV)
EV 257,229 - claims 16,260 = equity 240,969 -> EUR 486/share vs 381.65 (+27%)

Reconciliation: TTM company FCF margin 14.3% (levered); 5-yr avg 13.9%; BASE yr1 model 12.7%, yr5+ 14.9%
```

## F. Reverse DCF & sensitivity grid

```
7. REVERSE DCF
BASE margins/WACC 9.5%/g 3%/ROIC 15%: price implies constant 10-yr revenue CAGR 4.81%
TROUGH margin (21.9% flat): price implies constant 10-yr revenue CAGR 6.50%
At BASE growth path, price implies PRO margin reaching 26.76% by yr 5 (TTM 21.9%, 5-yr avg 25.0%, 5-yr low 22.0%)
BASE operating case: price implies a discount rate (IRR) of 9.09%
```

**What must be true at EUR 381.65** (at WACC 9.5%):
- With margins recovering to the 5-yr average of 25.0%, revenue must compound at **4.8% a year for 10 years**. That compares with 5.9% FY21–25 (boom-inclusive), −1.7% and −4.6% in the last two years, and CONSENSUS +4.6% for FY27.
- If margins stay at the trough, the price needs **6.5%** growth.
- On the base growth path, the price needs PRO margin back to **26.8%**, about the FY2021 peak.
- Put differently, the base operating case earns an IRR of **9.1%** at today's price.

```
8. SENSITIVITY (BASE): WACC x terminal growth, EUR/share
WACC/g         2.0%     2.5%     3.0%     3.5%     4.0%
8.5%            401      413      427      443      463
9.0%            368      377      388      400      415
9.5%            340      347      355      364      375
10.0%           315      320      327      334      342
10.5%           293      297      302      308      314

BASE: WACC x terminal ROIC (g 3%)
WACC/ROIC         10%      12%      15%      20%      25%
8.5%              392      409      427      444      454
9.0%              357      373      388      403      412
9.5%              328      341      355      368      376
10.0%             303      315      327      338      346
10.5%             281      292      302      313      319

BASE: steady-state PRO margin (reached yr5) x WACC
WACC/PRO        22.0%    23.5%    25.0%    26.7%
8.5%              373      400      427      458
9.0%              339      364      388      416
9.5%              310      333      355      381
10.0%             285      306      327      351
10.5%             264      283      302      324
```

## G. Load-bearing inputs

```
9. LOAD-BEARING INPUTS: +/-10% (relative) on BASE, EUR/share
BASE = EUR 354.8
Input                                       -10%      +10%     swing
WACC                                       422.4     304.5     117.9
Base revenue (TTM)                         316.1     393.6      77.5
Steady-state PRO margin (5-yr avg)         317.5     392.1      74.6
Tax rate                                   371.3     338.4      32.8
Revenue growth (all yrs)                   343.5     366.5      23.0
Capex / revenue                            362.5     347.2      15.3
D&A / revenue (add-back)                   348.7     361.0      12.3
Terminal ROIC                              348.9     359.7      10.8
Terminal growth                            349.9     360.2      10.3
Claims (NFD+puts+MI)                       358.1     351.6       6.6
Cash-conversion gap                        356.7     353.0       3.6
Lease adjustment                           355.7     354.0       1.7
WC intensity (UNKNOWN, base 0): each 10% of incremental revenue tied up -> -4.6/share; 25% -> -11.5/share
Crediting DFS held-for-sale net assets (2,074 - 1,025): +2.1/share (not taken)
Tax at H1-26 ETR 30.0% instead of 5-yr avg: -11.4/share
BASE with TTM capex/rev 5.36% and FY25 cash gap 0.49% (i.e. today's cash conversion persists): EUR 377.9/share; TROUGH on same basis: EUR 331.9/share
Note: 'Base revenue' is a reported figure (low uncertainty); its swing shows operating leverage, not estimate risk.
```

| # | Input | Base value | Source | −10% / +10% → EUR/share (base 355) |
|---|---|---|---|---|
| 1 | WACC | 9.5% | CAPM: OAT 4.75% (**secondary**) + 1.0 × 5% ERP (instruction) | 422 / 305 |
| 2 | Steady-state PRO margin | 25.0% | facts: 5-yr average PRO / revenue | 318 / 392 |
| 3 | Base revenue | 79,865 | facts: ttm.revenue_ttm_to_9m2026 (reported, low uncertainty; this shows operating leverage) | 316 / 394 |
| 4 | Tax rate | 28.1% | facts: 5-yr average ETR (FY25 32.8%, H1-26 30.0%) | 371 / 338 |
| 5 | Revenue growth path | 1–5% | ASSUMPTION plus CONSENSUS FY27 (yr 2) | 344 / 367 |
| 6 | Capex / revenue | 6.26% | facts: 5-yr average (TTM 5.36%) | 363 / 347 |
| 7 | D&A ex-ROU / revenue | 5.03% | facts: 5-yr average | 349 / 361 |
| 8 | Terminal ROIC | 15% | ASSUMPTION, anchored to FY25 ROIC 15.7% | 349 / 360 |
| 9 | Terminal growth | 3.0% | ASSUMPTION (cap: min(4%, OAT 4.75%)) | 350 / 360 |
| 10 | Claims (NFD + puts + minorities) | 16,260 | facts: interim.H1_2026 | 358 / 352 |
| — | Cash-conversion gap | 1.49% | facts-derived calibration, 2 years only | 357 / 353 |
| — | Working-capital intensity | 0 (UNKNOWN) | no inventory data | −4.6/share per 10% of incremental revenue |
| — | Today's cash conversion persists (TTM capex 5.36% + FY25 gap) | — | facts | Base 378 (+23); Trough 332 (+23) |

The top three by swing are WACC, the steady-state margin, and base revenue. Base revenue is a reported figure, so it is not a real estimate risk. The three that actually carry estimate risk are **WACC (the OAT input is secondary-sourced), the mid-cycle PRO margin, and the tax rate.**

## H. Open questions for the Skeptic (where I was least sure)

1. **Is 25.0% really mid-cycle?** The 5-yr average includes three post-COVID boom years. FLG margin fell every year FY21 → H1-26, including in growth years, which looks structural. At 23.5% steady state, base is 333. At 22.0% (5-yr low) it is 310. The price needs 26.8% on the base growth path. *This is the single most important judgement in the model.*
2. **Discount rate.**
   - The OAT 4.75% is secondary and unverified for 13 Oct; it peaked above 5% the prior week. Beta of 1.0 is unsourced.
   - A Bund-based or revenue-weighted rate would be lower. WACC 8.5% gives 427; 10.5% gives 302.
   - Should a French sovereign spread price a business that is 92% non-French by revenue?
3. **Cash conversion.**
   - Base capex is the 5-yr average of 6.26%, which includes the FY23 peak of 8.7%. Base also deducts a 1.49% gap calibrated on only two years. On TTM cash conversion, base is 378.
   - The calibration assumes lease interest paid sits inside OCF in LVMH's cash-flow statement. Not verified. If it sits in financing, the gap understates and value is lower by roughly 7–8/share (my estimate from the capex sensitivity, not run).
4. **Inventory and receivables vs sales are UNKNOWN.** These are the key Lynch red-flag checks for a cyclical, and they are not done. The FY24 cash gap (2,101 while revenue fell) is consistent with an inventory build.
5. **EV bridge.**
   - Puts and book minorities are both included, on my reading that IFRS reclassifies put-covered minorities out of equity. If they overlap, value rises up to 3.2/share. A cross-check of TTM minority profit 449 × P/E 17.4 = 7,810 against 8,015 suggests the bridge is about right.
   - DFS held-for-sale net assets (+2.1/share) and non-current investments (UNKNOWN) are not credited.
   - Treasury shares at 30 Jun 2026 are UNKNOWN. Issued shares (495.8m) are used against Yahoo's 493.0m outstanding; the difference is −0.6% on per-share value.
6. **Tax rate.** FY25 ETR was 32.8% and H1-26 was 30.0%, against 26–27% for FY21–23. At 30.0%, base is −11/share.
7. **Is the bear deep enough?** The dossier has no pre-FY2021 history, so I cannot calibrate against a prior luxury recession. Bear assumes −1%/−3% revenue and a 20.5% trough margin.
8. **Scope and FX.** Base yr 1 assumes about −1pt scope (DFS FY25 revenue 1,494; Marc Jacobs revenue UNKNOWN). No FX path is modelled, although 79% of revenue is invoiced outside EUR. EUR/SGD translation for the SGD-base holder is not modelled.
9. **Segment cross-check spread (217 to 550).** The range is too wide to arbitrate, and the method is crude (peer P/E applied to segment NOPAT). It is shown, not used.
10. **Consensus FY27 +4.6% is used in base yr 2.** It is a labelled growth estimate, not a target or rating. Please confirm it is acceptable under RULE 2.

## Appendix: remaining model output (history, lease calibration, owner earnings and Lynch, multiples)

```
1. HISTORY: MARGINS, TAX, CAPITAL INTENSITY, ROIC
                              FY2021    FY2022    FY2023    FY2024    FY2025
Revenue                       64,215    79,184    86,153    84,683    80,807
Gross margin                   68.3%     68.4%     68.8%     67.0%     66.2%
PRO margin                     26.7%     26.6%     26.5%     23.1%     22.0%
Effective tax rate             26.2%     26.7%     26.2%     28.5%     32.8%
Capex / revenue                 4.1%      6.3%      8.7%      6.5%      5.7%
D&A ex-ROU / revenue            4.9%      4.1%      4.8%      5.4%      6.0%
Capex / D&A ex-ROU              0.85      1.54      1.80      1.21      0.94
Company op. FCF margin         21.1%     12.8%      9.4%     12.4%     14.0%
ROIC (eq+NFD)                  21.6%     23.5%     22.9%     17.8%     15.7%
ROIC incl. leases in IC        17.4%     19.0%     18.7%     14.5%     13.0%
  FY2023: goodwill 24,022 = 32.7% of IC; ROIC ex-goodwill 34.0%
  FY2025: goodwill 18,315 = 24.2% of IC; ROIC ex-goodwill 20.8%
5-yr: PRO margin avg 24.97%, low 21.97%, high 26.71%; TTM 21.89%
5-yr: ETR avg 28.07% | H1-26 ETR 30.03% | capex/rev avg 6.26% | D&A ex-ROU/rev avg 5.03% | company FCF margin avg 13.93% | ROIC avg 20.3%
FLG PRO margin: FY2021 41.6%, FY2022 40.6%, FY2023 39.9%, FY2024 37.1%, FY2025 35.0%, H1-26 34.1%
Gross margin H1-25 66.8% -> H1-26 67.1%
2. IFRS 16 ADJUSTMENT AND CASH-CONVERSION CALIBRATION (FY2024, FY2025: lease interest known)
FY2024: lease cash 3,425 - ROU depr 3,228 = adj 197 (0.23% rev) | EBIT_adj 19,374 | model pre-WC FCF 12,896 vs reported unlevered 10,794 -> gap 2,101 (2.48% rev)
FY2025: lease cash 3,527 - ROU depr 3,143 = adj 384 (0.48% rev) | EBIT_adj 17,371 | model pre-WC FCF 11,965 vs reported unlevered 11,567 -> gap 398 (0.49% rev)
Lease adj carried forward 0.48% of revenue (FY2025). Cash gap (WC/other/tax timing): avg 1.49%, high 2.48%, low 0.49%
FY2025 pre-IFRS16 EBITDA = 22,229 (27.5%)
3. OWNER EARNINGS, LYNCH METRICS, DEBT
Owner earnings (fj, AGENTS.md def) = 10,878 + 8,001 - 4,670 = 14,209  yield 7.51%
Lease-adjusted OE = 10,878 + 8,001 - 4,567 - lease principal 2,974 = 11,338  yield 5.99%  (with fj capex 4,670: 11,235)
SBC: already expensed in NI, so OE above is SBC-burdened. FCF-based (SBC added back in OCF): TTM company FCF 11,401 - SBC 187 = 11,214 -> SBC-adj FCF yield 5.93%
Revenue CAGR FY21-25 5.91% | EPS CAGR FY21-25 -2.21% | EPS peak-to-FY25 -28.0% | CONSENSUS EPS CAGR FY25-27 5.74%
YoY revenue: +23.3%, +8.8%, -1.7%, -4.6% | YoY EPS: +17.3%, +8.2%, -17.2%, -13.0%
PEG gate (trailing 17.4, forward 15.7, growth = lower of hist/consensus -2.21%): VOID - growth -2.2% <= 0: PEG undefined
  (consensus-only growth 5.74% would give: VALID - ok; not used)
Lynch ratio (hist EPS CAGR) = (-2.2 + 3.41) / 17.4 = 0.07
Lynch ratio (CONSENSUS FY25-27) = (5.7 + 3.41) / 17.4 = 0.53
Net-cash-adj P/E = (381.65 - (-16.63)) / 21.94 = 18.2x | incl. puts: 18.7x
Normalised EPS (PRO 25.0% x TTM rev, FY25 fin. & other-op items, ETR 28.1%, MI 3.1%) = 26.52 -> normalised P/E 14.4x
Dividend: payout 59.5% of EPS; EPS cover 1.68x; op FCF / dividends paid (incl MI) 1.59x; op FCF / Group-share dividends 6,463 = 1.75x
Net debt / lease-adj OE: NFD 0.73x | NFD+puts 1.29x | NFD+puts+leases vs fj OE 2.18x
Interest cover FY25: PRO / cost of NFD 51x; PRO / (NFD cost + lease int) 19.7x
Maturities: 2026 7,923, 2027 1,986, 2028 1,767 vs cash+AFS 13,502 (Dec-25), 12,202 (Jun-26)
4. MULTIPLES MATRIX (current)
EV/EBITDA (IFRS16: EV incl leases / PRO+D&A TTM)                      8.8x   peer median: 16.2x (Yahoo basis; LVMH Yahoo 10.8x)
EV/EBITDA (pre-IFRS16: EV ex-leases / FY25 adj)                       9.2x   peer median: n/a
P/E trailing (own TTM EPS 21.94)                                     17.4x   peer median: 30.3x
P/E forward (fj)                                                     15.7x   peer median: 21.3x
P/E on CONSENSUS FY26 / FY27 EPS                             17.2x / 15.6x   peer median: n/a
P/E on normalised (mid-cycle) EPS                                    14.4x   peer median: n/a
P/FCF (company def., TTM)                                            16.6x   peer median: n/a
P/FCF SBC-adjusted                                                   16.9x   peer median: n/a
FCF yield (company def. TTM)                                         6.03%   peer median: n/a
FCF yield (OCF-capex, Yahoo-style, TTM)                              7.60%   peer median: 3.15%
Owner-earnings yield (fj def / lease-adj)                    7.51% / 5.99%   peer median: n/a
PEG                                                       VOID (not cited)   peer median: n/a
Lynch ratio (hist / consensus growth)                          0.07 / 0.53   peer median: n/a
Dividend yield                                                       3.41%   peer median: n/a
P/E 12m ago (527.18 / FY24 EPS 25.12, last full year then reported): 21.0x
```
