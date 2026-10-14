<!-- pipeline:value-quant -->
# Quant model: ZBH (as of 2026-10-13)

Zimmer Biomet Holdings, NYSE, USD. Template: **FULL** (dossier §0). Price **$92.17** (fund), market cap $17,580M,
EV $24,649M (facts: market). Trailing GAAP P/E 22.4x (fund), 12-month price change −2.0% (facts: market).
Status: current holding. Model: `reports/runs/ZBH_2026-10-13/02_model.py`. Every computed number below comes from that executed script.

**Tape check (RULE 0).** The stock is flat over 12 months and trades at about 10x forward *adjusted* EPS but 22x trailing *GAAP*.
The tape is not pricing growth. It is pricing a slow-growth franchise whose GAAP earnings fell from FY23 to FY25.
Nothing below assumes a growth story.

**Orchestrator correction applied.** facts.json `derived.fcf` and `owner_earnings` left out capitalised intangibles.
I re-ran `sec_facts.py ZBH` (no `--out`), cited below as **secfix**. Corrected FY2025 capex is $276.9M (PP&E $224.5M + intangibles $52.4M),
FCF is $1,420M and owner earnings are $1,522M. TTM capex is $220.3M PP&E + $121.0M intangibles (secfix TTM `capex_intangibles`),
which gives corrected TTM FCF of **$1,402M**, not the dossier's $1,523M. That makes TTM FCF lower than FY25, not higher.

**Data warnings surfaced (RULE 1):** `institutional_pct=1.1137` is a vendor artifact, not quoted (fund). FCF conflict: vendor $1,072M
vs SEC-corrected $1,420M (FY25) / $1,402M (TTM), unresolved; see H1. `errors`: none.

---

## A. Lynch classification & category checks

| Metric (facts / secfix) | Value |
|---|---|
| Revenue CAGR FY20–25 | 6.1% (COVID-depressed FY20 base) |
| Revenue CAGR FY21–25 | 4.8% |
| Revenue y/y FY22 / FY23 / FY24 / FY25 | 1.6% / 6.5% / 3.8% / 7.2% (FY25 includes ~2.5pt from Paragon 28, dossier §8) |
| FY2026 organic cc guidance | 2.25–3.25% (dossier §3) |
| GAAP diluted EPS FY20→FY25 | −0.67, 1.91, 1.10, 4.88, 4.43, 3.55 |
| GAAP EPS CAGR FY20–25 / FY23–25 | undefined (negative base) / **−14.8%/yr** |
| Consensus adj EPS FY27 vs FY26 (CONSENSUS) | +6.3% |

**Category: Slow Grower, bordering on Stalwart, and drifting down rather than up.** Underlying organic growth is about
2–3% (FY26 guide). The 6.1% headline CAGR rests on a COVID base and Paragon 28. GAAP EPS has fallen two years running.
Only consensus adjusted EPS (+6.3%, helped by buybacks) reaches stalwart-low territory, and nothing reaches the 10–12% of a real Stalwart.
There is some turnaround flavour (sales-force transition, 2025 Restructuring Plan, GAAP margin down from FY23), but survival is not in question (see debt below).
So it is not a Turnaround in Lynch's sense. Valuation implication: value it on cash flow at low growth. Do not apply a growth multiple.

**Slow-grower checks (dividend):**
- Dividends paid per diluted share were flat at **$0.951–0.961 for six years** (FY20–FY25, facts), so the dividend has not grown.
- Yield is **1.0%** ($0.96 / $92.17, dossier §1). That is weak for a slow grower, whose main appeal in Lynch's scheme is income.
- Coverage is very strong: dividends take 13.4% of TTM FCF and 23.4% of TTM GAAP NI.
- Cash return runs mostly through buybacks: TTM $750.8M is a **4.3% buyback yield** (facts TTM), and the FY26 plan is up to $1B (dossier §3).

**Stalwart cross-checks:**
- P/E versus its own 5-year range: **UNKNOWN**, because the dossier has no historical price series beyond one point a year ago.
- Diworsification: Paragon 28 (foot & ankle) and Monogram (robotics) are adjacent to core orthopaedics, so this is not diworsification.
  Even so, the $1,393.2M paid in 2025 (dossier §5) equals 98% of FY25 FCF.

**Lynch metrics (formulas shown):**
- **PEG: VOID, not cited.** `peg_is_valid(22.4, 10.2, g)` returns "missing growth" for the 5-yr historical rate (undefined),
  "growth −14.8% ≤ 0" for the FY23–25 historical rate, and "ok" for the 6.3% consensus rate. The lower-of rule takes the historical rate, so PEG is void.
  The gate's forward < trailing test is also basis-mismatched here (forward is adjusted, trailing is GAAP).
- **Lynch ratio** = (EPS growth % + dividend yield %) / P/E. I used the generous consensus growth of 6.3%:
  (6.3 + 1.04) / 22.4 = **0.33** on trailing GAAP P/E, and (6.3 + 1.04) / 10.2 = **0.72** on vendor forward adjusted P/E. Both are below 1, which is poor.
- **Net-cash-adjusted P/E** = (price − net cash per share) / EPS. Net cash per share = −7,068.9 / 190.74 = −$37.06.
  On TTM GAAP EPS of $4.23 (TTM NI 806.7 / 190.74 shares): (92.17 + 37.06) / 4.23 = **30.6x**. On guidance-mid adjusted EPS of $8.53: **15.2x**.
  The headline 10x forward P/E hides about $37 per share of debt.
- **Inventory vs sales** (facts): FY25 inventory +2.3% against sales +7.2% (−4.9pp), which is clean. FY24 −10.1pp, also clean. FY23 +4.5pp was a mild flag.
- **Receivables vs sales** (facts): **FY25 receivables +15.1% against sales +7.2%, a +7.9pp red flag.** FY22 was also flagged (+8.0pp).
  Part of FY25 is probably acquired Paragon 28 receivables, but the inorganic share is UNKNOWN (H6).
- **Debt structure:**
  - Net debt $7,068.9M (Jun-26): **4.6x FY25 owner earnings**, 4.5x TTM owner earnings, 3.06x TTM GAAP EBITDA.
  - Interest cover (GAAP EBIT / interest) is 3.75x for FY25.
  - Maturity wall (dossier §5): 2027 notes total $1,187.1M (4.700% $600M + Euro 1.164% $587.1M), which matches the $1,201.5M now in current debt.
    Cash is $410M. 2028: $500M. 2030: $807.5M plus Swiss notes (UNKNOWN). The $1.5B revolver runs to 2030; renewal of the $1.0B 364-day facility is UNKNOWN.
  - TTM FCF of $1,402M covers 2027 within a year, but the $1B buyback plan plus about $190M of dividends uses up the FCF.
    So the 2027 notes will probably be refinanced at today's rates. That is manageable, not a survival risk.

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

| FY | GM | GAAP Op M | GAAP EBITDA M | Capex(tot)/Rev | Capex/D&A | FCF M (secfix) | ROIC | ROIC ex-GW | GW/IC |
|---|---|---|---|---|---|---|---|---|---|
| FY20 | 70.2% | 1.4% | 16.0% | 1.8% | 0.12 | 17.8% | 0.3% | 0.6% | 46.0% |
| FY21 | 71.3% | 12.6% | 26.3% | 2.2% | 0.16 | 19.7% | 4.0% | 7.4% | 46.1% |
| FY22 | 70.9% | 10.0% | 23.4% | 3.1% | 0.23 | 16.4% | 2.9% | 5.7% | 49.5% |
| FY23 | 71.8% | 17.3% | 30.2% | 5.3% | 0.41 | 16.1% | 6.9% | 13.6% | 49.5% |
| FY24 | 71.5% | 16.7% | 29.7% | 4.6% | 0.36 | 14.9% | 6.2% | 12.2% | 49.3% |
| FY25 | 69.7% | 13.3% | 26.6% | 3.4% | 0.25 | 17.3% | 4.7% | 9.6% | 50.7% |
| TTM | 69.9% | 14.2% | 27.2% | 4.0% | — | 16.5% | 5.3% | 10.6% | 50.3% |
| 5-yr avg FY21–25 | 71.0% | — | 27.2% (low 23.4, high 30.2) | — | — | 16.9% | 4.9% | 9.7% | — |

Gross margin comes from facts cost of revenue. Capex(tot) includes capitalised intangibles (secfix).
ROIC = NOPAT / (equity + debt − cash) with the facts tax rate. ROIC ex-GW subtracts goodwill from invested capital.

**Circle of competence / predictability: PARTLY.** Revenue is sketchable 10 years out within a band. Implant demand is procedure-driven,
growth has been low-single-digit organic, and the product mix is stable (knees 40%, hips 25%, S.E.T. 26%; dossier §8).
Margins are not sketchable. GAAP operating margin has ranged 1.4–17.3%. Restructuring, integration and remediation charges recur.
Adjusted EPS ($8.53 guide) is roughly twice GAAP EPS ($4.23 TTM). And the Q2 adjusted operating margin fell 210bp y/y (dossier §3).
I am confident about revenue and not confident about the cash margin.

**Moat: NARROW. Trend: stable at the gross level, eroding at the operating level (low confidence).**
- Evidence for a moat: gross margin held in a 69.7–71.8% band for six years, which points to pricing power and switching costs.
  Capital intensity is low: total capex is 2–5% of revenue.
- Evidence against Wide:
  - Reported ROIC has been **below any plausible WACC every year** (0.3–6.9%).
  - Gross margin fell 2.1pp from FY23 (71.8%) to FY25 (69.7%).
  - Knees, 40% of sales, grew +0.4% in Q2 with international −0.9% (dossier §3). The dossier cites China pricing/volume weakness.
  - Market share: UNKNOWN (dossier §8), so share trend cannot be assessed.
- Capex/D&A of 0.12–0.41 is not a moat signal. It mostly shows that D&A is inflated by amortisation of acquired intangibles (H2).

**ROIC vs WACC (8.5%, section D):**
- Reported ROIC: FY25 4.7%, TTM 5.3%, 5-yr average 4.9%. That is about **350bp below WACC**.
- Goodwill is 50.7% of invested capital, above the 30% threshold, so ex-goodwill ROIC is shown: FY25 9.6%, TTM 10.6%, 5-yr average **9.7%**.
  That is about **100–200bp above WACC**, which is thin.
- Excluding intangibles as well gives 19.6% TTM. This understates the true figure, because GAAP EBIT is after acquired-intangible amortisation and the D&A split is UNKNOWN.

Which matters for the thesis?
- **Ex-goodwill (about 10%) describes the organic economics.** It is the basis for my terminal ROIC (10% base). It says organic growth creates only a little value.
- **Including goodwill (about 5%) is the scorecard for management's M&A.** Acquired growth has not earned its cost of capital.
  Management is still acquiring (Paragon 28, Monogram), so incremental M&A should be underwritten at the reported ROIC, not the ex-goodwill one.

**Owner earnings** (secfix, = NI + D&A − capex including intangibles):

| | FY21 | FY22 | FY23 | FY24 | FY25 | TTM |
|---|---|---|---|---|---|---|
| Owner earnings | 1,187 | 940 | 1,581 | 1,543 | **1,522** | 1,574 |
| OE − SBC | 1,111 | 835 | 1,481 | 1,442 | 1,432 | 1,476 |

- **Owner-earnings yield on $17,580M market cap:** FY25 **8.7%**, SBC-adjusted 8.1%. TTM 9.0%, SBC-adjusted 8.4%.
- Stress case: if 2025 acquisitions ($1,393.2M, dossier §5) were treated as recurring growth capex, FY25 owner earnings would be **$129M**.
  This bounds how much the yield depends on management not repeating 2025's M&A.
- Caveat: owner earnings add back all D&A, including about $1.1B of mostly-amortisation D&A. That is economically right only if the capex line captures all maintenance spending (H1).

## C. GARP & valuation matrix

| Metric | Current | 5-yr own avg | Peer median (dossier §7, n=6) |
|---|---|---|---|
| EV/EBITDA (GAAP TTM EBITDA $2,313M) | **10.7x** (FY25: 11.2x; vendor adj.: 9.8x) | UNKNOWN (no historical prices) | 14.8x (ex-SNN 13.3x) |
| P/E trailing (GAAP) | **22.4x** vendor / 21.8x on TTM NI ÷ 190.74M | UNKNOWN | 21.1x |
| P/E forward (adjusted EPS) | **10.8x** on guidance mid $8.53; 10.2x vendor (= FY27 consensus $9.07) | UNKNOWN | 14.2x |
| P/E forward (GAAP) | UNKNOWN | UNKNOWN | UNKNOWN |
| P/FCF (corrected TTM FCF $1,402M) | **12.5x** (FY25 12.4x) | UNKNOWN | 23.7x |
| SBC-adjusted P/FCF | **13.5x** | UNKNOWN | UNKNOWN |
| FCF yield | **8.0%** TTM / 8.1% FY25 (vendor-FCF basis 6.1%) | UNKNOWN | 4.2% |
| Owner-earnings yield | **9.0%** TTM / 8.7% FY25 | UNKNOWN | UNKNOWN |
| PEG | **VOID** (not cited) | n/a | n/a |
| Lynch ratio | **0.33** GAAP / 0.72 adjusted-forward | UNKNOWN | UNKNOWN |
| Net-cash-adj P/E | 30.6x GAAP / 15.2x adjusted | UNKNOWN | UNKNOWN |
| Dividend yield / buyback yield | 1.0% / 4.3% | — | — |

Peer multiples are single-vendor and on mixed bases: SNN EV/EBITDA looks distorted and adjusted-EPS bases differ (dossier §7).
ZBH screens cheap against peers on every cash metric: P/FCF about half the peer median, FCF yield about twice it.
Two caveats apply. ZBH is the slowest grower in the set. And its FCF basis is disputed by $348M (H1).

## D. Discount rate build

| Input | Value | Source |
|---|---|---|
| Risk-free (10y UST) | 5.20% | dossier §1 (yfinance ^TNX, **not cross-checked**) |
| ERP | 5.0% | stated assumption (task spec) |
| Beta | 1.0 | no sourced beta in dossier |
| Cost of equity | 5.20% + 1.0 × 5.0% = **10.20%** | computed |
| Pre-tax cost of debt | **5.50%** | coupon of 5.500% 2035 notes (dossier §5). Market YTM UNKNOWN. The historical 4.28% (FY25 interest $292.8M ÷ average debt) is below the Treasury yield, so not used |
| Tax rate | 18% | adjusted tax rate Q2 2026 (dossier §3). TTM GAAP ETR is 13.6% (facts) |
| After-tax Kd | 4.51% | computed |
| Weights | E 70.2% / D 29.8% | market cap $17,580M; debt $7,478.9M at **book** (market value UNKNOWN) |
| WACC | **8.50%** | computed. Above the 8% USD floor, so the floor does not bind |

## E. DCF scenarios

Engine: `valuation.dcf()`, 10 years. Year 1 = Jul-26 to Jun-27, base = TTM revenue $8,508.8M (facts TTM). Net debt is Jun-26, $7,068.9M.
Shares are 190.74M outstanding (facts `shares_outstanding_latest`).

- **SBC:** deducted. EBITDA = GAAP operating income + D&A, which already expenses SBC (about 1.1% of revenue). Not added back, and the share count is not grown.
- **D&A path:** TTM D&A/revenue of 13.0% is held for years 1–5, then fades linearly to equal capex% by year 10.
  The rationale is that acquired-intangible amortisation runs off, and the terminal formula treats D&A as maintenance capex.
  This is load-bearing: see the alternative check and H2.
- **Working capital:** 48.5% of incremental revenue, which is (inventory + receivables) / revenue for FY25 (facts).
  Payables are UNKNOWN, so this overstates the working-capital drag, which is conservative.
- **Calibration:** base year-1 unlevered FCF margin is 18.6%. Historical unlevered FCF margin, (corrected FCF + after-tax interest) / revenue, was 18.7% / 17.4% / 20.3% for FY23–25, an average of **18.8%**.
  So the base is anchored on history, as required.

| Input | Bear | Base | Bull |
|---|---|---|---|
| Rev growth yr1 | 2.25% (organic guide low) | 4.4% (FY26 reported guide mid) | 4.9% (guide top) |
| Rev growth yrs 2–10 | 1.7% (FY22 low) → 2.0% | 3.25% → 3.0% | 4.5% → 3.5% |
| GAAP EBITDA margin | 26.2% → **23.4%** by yr4 (FY22 5-yr low) | **27.2%** flat (= 5-yr avg and TTM) | 27.5% → **30.0%** by yr4 |
| Capex (incl. intangibles) / rev | 4.6% (FY24) | 4.0% (TTM) | 3.4% (FY25) |
| Tax on EBIT | 18% | 18% | 18% |
| WACC | 8.5% | 8.5% | 8.5% |
| Terminal growth | 2.0% | 3.0% | 3.5% (≤ min(4%, 5.2%)) |
| Terminal ROIC | 8.5% (= WACC: value-neutral growth) | 10% (5-yr ex-GW avg 9.7%) | 12% (FY24 ex-GW 12.2%) |
| **Per share** | **$59.25** (−35.7%) | **$95.27** (+3.4%) | **$131.74** (+42.9%) |
| TV share of EV | 46% | 51% | 56% |

No scenario has terminal value above 75% of EV.

The bull margin is sourced, not invented: FY23 and FY24 GAAP EBITDA margins were 30.2% and 29.7% on essentially the current portfolio (facts).
On top of that come the 2025 Restructuring Plan (~$155M charges to 2027, dossier §5) and Paragon 28 integration costs that should not recur.
The bull case is a return to FY23–24 margins, not expansion beyond them.

Bear is not modelled as a cyclical V. Orthopaedics is procedure-driven, and the only historical drop in the facts is COVID FY20.
Instead, bear is a steady squeeze: China/knee pricing pressure, GAAP margin at the FY22 low, and higher capex.

Executed output (`python3 reports/runs/ZBH_2026-10-13/02_model.py`, section E):
```
======== E. DCF SCENARIOS ========
Common: base revenue TTM 8,508.8 (yr1 = Jul-26..Jun-27) | tax 18% | WACC 8.5% | net debt 7,068.9 | shares 190.74 | WC 48.5% of delta rev | D&A 13.0% yrs1-5, fades to capex% by yr10

--- BEAR: growth [2.25, 1.7, 1.7, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    EBITDA m [26.2, 25.0, 24.0, 23.4, 23.4, 23.4, 23.4, 23.4, 23.4, 23.4] capex 4.6% g_term 2.0% ROIC_term 8.5%
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1    8,700   2,279  1,146  1,133    400  1,580  18.2%  1,456
  2    8,848   2,212  1,059  1,153    407  1,543  17.4%  1,310
  3    8,999   2,160    987  1,172    414  1,495  16.6%  1,170
  4    9,179   2,148    952  1,196    422  1,467  16.0%  1,058
  5    9,362   2,191    971  1,220    431  1,496  16.0%    995
  6    9,549   2,235  1,152  1,083    439  1,497  15.7%    918
  7    9,740   2,279  1,339    941    448  1,498  15.4%    846
  8    9,935   2,325  1,533    792    457  1,497  15.1%    780
  9   10,134   2,371  1,734    637    466  1,497  14.8%    718
 10   10,337   2,419  1,943    475    475  1,495  14.5%    661
PV explicit 9,914 | PV terminal 8,457 | TV share 46%
EV 18,371 | equity 11,302 | PER SHARE $59.25 | vs $92.17: -35.7%

--- BASE: growth [4.4, 3.25, 3.25, 3.25, 3.25, 3.0, 3.0, 3.0, 3.0, 3.0]
    EBITDA m [27.2, 27.2, 27.2, 27.2, 27.2, 27.2, 27.2, 27.2, 27.2, 27.2] capex 4.0% g_term 3.0% ROIC_term 10.0%
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1    8,883   2,416  1,259  1,157    355  1,653  18.6%  1,523
  2    9,172   2,495  1,300  1,195    367  1,754  19.1%  1,490
  3    9,470   2,576  1,342  1,234    379  1,811  19.1%  1,418
  4    9,778   2,660  1,386  1,274    391  1,870  19.1%  1,349
  5   10,096   2,746  1,431  1,315    404  1,931  19.1%  1,284
  6   10,398   2,828  1,662  1,167    416  1,967  18.9%  1,205
  7   10,710   2,913  1,905  1,008    428  1,991  18.6%  1,125
  8   11,032   3,001  2,161    840    441  2,015  18.3%  1,049
  9   11,363   3,091  2,431    660    455  2,038  17.9%    978
 10   11,703   3,183  2,715    468    468  2,061  17.6%    912
PV explicit 12,333 | PV terminal 12,909 | TV share 51%
EV 25,242 | equity 18,173 | PER SHARE $95.27 | vs $92.17: +3.4%

--- BULL: growth [4.9, 4.5, 4.5, 4.5, 4.0, 4.0, 3.5, 3.5, 3.5, 3.5]
    EBITDA m [27.5, 28.5, 29.5, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0] capex 3.4% g_term 3.5% ROIC_term 12.0%
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1    8,926   2,455  1,292  1,163    303  1,716  19.2%  1,582
  2    9,327   2,658  1,443  1,215    317  1,887  20.2%  1,603
  3    9,747   2,875  1,606  1,270    331  2,051  21.0%  1,606
  4   10,186   3,056  1,729  1,327    346  2,186  21.5%  1,577
  5   10,593   3,178  1,798  1,380    360  2,297  21.7%  1,527
  6   11,017   3,305  2,082  1,223    375  2,350  21.3%  1,441
  7   11,402   3,421  2,374  1,046    388  2,419  21.2%  1,366
  8   11,802   3,540  2,685    856    401  2,462  20.9%  1,282
  9   12,215   3,664  3,014    650    415  2,506  20.5%  1,203
 10   12,642   3,793  3,363    430    430  2,550  20.2%  1,128
PV explicit 14,315 | PV terminal 17,882 | TV share 56%
EV 32,197 | equity 25,128 | PER SHARE $131.74 | vs $92.17: +42.9%

Timing note: cash flows are discounted from 2026-06-30; rolling to 2026-10-13 multiplies EV by 1.0241 (BASE would be $98.46). Not applied above.

Alternative-basis checks on BASE:
  no D&A fade (D&A stays 13.0%, terminal NOPAT on GAAP EBIT)     $  70.36  (TV 38%)
  uncaptured capex: +$348M/yr (vendor FCF 1,072 basis)           $  69.84  (TV 52%)
  diluted share count 198.7 (FY25) instead of 190.74             $  91.46  (TV 51%)
  WC on inventory only (payables still UNKNOWN)                  $  97.55  (TV 50%)
```

## F. Reverse DCF & sensitivity

**What must be true at $92.17:**
- At base margins (27.2% GAAP EBITDA), 8.5% WACC, 3% terminal growth and 10% terminal ROIC, the price implies a **2.9% constant 10-year revenue CAGR**.
  That is almost exactly the organic cc guidance midpoint (2.75%).
- At base growth, the price implies a flat GAAP EBITDA margin of **26.7%**, against 27.2% TTM.
- Base cash flows return **8.65%**, the implied IRR, which is roughly the WACC.

So the market is pricing ZBH as "today's business, flat margins, low-single-digit growth, forever." Value depends on the margin:
- If margins drift to the FY22 low (bear margin path), the price needs 7.1% growth, which ZBH has not delivered organically.
- If margins return to FY23–24 levels (bull margin path), the price needs about 0% growth.

Section F output:
```
======== F. REVERSE DCF & SENSITIVITY ========
Implied constant 10-yr revenue CAGR at BASE margins/capex/WACC/g/ROIC: 2.91% (yr-10 revenue 11,339)
  ...at BEAR margins/capex/terminal: 7.07%
  ...at BULL margins/capex/terminal: -0.02%
Implied flat EBITDA margin at BASE growth: 26.66% (TTM 27.19%, 5-yr low 23.38%)
Implied discount rate (IRR) at BASE cash flows: 8.65%
  implied IRR at BEAR cash flows: 6.69%
  implied IRR at BULL cash flows: 10.20%

BASE per-share: WACC (rows) x terminal growth (cols)
             2.0%     2.5%     3.0%     3.5%     4.0%
    7.5%   114.73   117.78   121.44   125.95   131.67
    8.0%   102.65   104.69   107.09   109.95   113.47
    8.5%    92.41    93.74    95.27    97.06    99.19
    9.0%    83.60    84.44    85.38    86.44    87.66
    9.5%    75.95    76.43    76.95    77.52    78.14

BASE per-share: WACC (rows) x terminal ROIC (cols), g 3.0%
             7.0%     8.5%    10.0%    12.0%    15.0%
    7.5%   104.78   114.58   121.44   127.92   134.41
    8.0%    92.77   101.19   107.09   112.65   118.22
    8.5%    82.84    90.16    95.27   100.11   104.94
    9.0%    74.49    80.89    85.38    89.61    93.84
    9.5%    67.35    73.00    76.95    80.68    84.41
```

## G. Load-bearing inputs

Ranked by the swing in base per-share value ($95.27). Two structural assumptions come first, because they move value more than any ±10% flex.

| # | Input | Base value | Source | Effect on per-share |
|---|---|---|---|---|
| S1 | **Capex completeness** (are all maintenance/instrument outlays in the capex line?) | $341M TTM (PP&E + intangibles) | facts TTM + secfix | If the $348M vendor-vs-SEC FCF gap is uncaptured capex: **$69.84 (−27%)** |
| S2 | **D&A fades to capex by yr10** (acquired amortisation runs off) | 13.0% → 4.0% of rev | facts TTM D&A; my assumption | No fade: **$70.36 (−26%)** |
| 1 | WACC | 8.5% | section D (10y 5.20% unverified) | −10%: +$21.55 (+22.6%) / +10%: −$15.93 (−16.7%) |
| 2 | GAAP EBITDA margin | 27.2% | facts 5-yr avg / TTM | ±$15.65 (±16.4%) |
| 3 | Base revenue | $8,508.8M | facts TTM | ±$13.23 (±13.9%) |
| 4 | Share count | 190.74M | facts (basic, Jul-26) | −10%: +$10.59 / +10%: −$8.66. FY25 diluted 198.7M gives $91.46 |
| 5 | Net debt | $7,068.9M | facts market (leases/CVR/pension UNKNOWN) | ±$3.71 (±3.9%) |
| 6 | Terminal ROIC | 10% | facts derived, ex-GW 5-yr avg | −$3.22 / +$2.64 |
| 7 | Revenue growth path | 4.4% → 3.0% | dossier §3 guidance | −$2.65 / +$2.71 |
| 8 | Tax rate | 18% | dossier §3 (adjusted) | ±$2.51 |
| 9 | Capex % of revenue | 4.0% | facts/secfix TTM | ±$1.38 |
| 10 | Terminal growth | 3.0% | assumption ≤ 10y yield | −$0.95 / +$1.04 |

Not load-bearing: working capital % (±$0.53) and the D&A fade endpoint level (±$1.10).
Timing: discounting from Jun-26 instead of rolling forward to Oct-26 understates base by **$3.19** (rolled value $98.46). This was not applied.

Section G output:
```
======== G. LOAD-BEARING INPUTS (+/-10% each, BASE) ========
BASE $95.27
  WACC (8.5%)                              -10%:  +21.55 (+22.6%)   +10%:  -15.93 (-16.7%)
  EBITDA margin (27.2%)                    -10%:  -15.65 (-16.4%)   +10%:  +15.65 (+16.4%)
  Base revenue (TTM 8,509)                 -10%:  -13.23 (-13.9%)   +10%:  +13.23 (+13.9%)
  Share count (190.74)                     -10%:  +10.59 (+11.1%)   +10%:   -8.66 (-9.1%)
  Net debt (7,069)                         -10%:   +3.71 (+3.9%)   +10%:   -3.71 (-3.9%)
  Terminal ROIC (10%)                      -10%:   -3.22 (-3.4%)   +10%:   +2.64 (+2.8%)
  Revenue growth path                      -10%:   -2.65 (-2.8%)   +10%:   +2.71 (+2.8%)
  Tax rate (18%)                           -10%:   +2.51 (+2.6%)   +10%:   -2.51 (-2.6%)
  Capex % rev (4.0%)                       -10%:   +1.38 (+1.5%)   +10%:   -1.38 (-1.5%)
  Terminal D&A = capex endpoint (4.0%)     -10%:   +1.10 (+1.2%)   +10%:   -1.10 (-1.2%)
  Terminal growth (3.0%)                   -10%:   -0.95 (-1.0%)   +10%:   +1.04 (+1.1%)
  WC % of delta revenue (48.5%)            -10%:   +0.53 (+0.6%)   +10%:   -0.53 (-0.6%)
```

## H. Open questions for the Skeptic (where I was least sure)

1. **Is the capex line complete?** (S1, the largest single swing.)
   - Vendor FCF is $1,072M against SEC-corrected $1,420M, a gap of $348M.
   - D&A ($1,094M) is about 4x total capex ($277M) for a device maker that ships instrument sets.
   - Check the 10-K FY2025 cash-flow statement investing section for any capex-like line (instruments, other PP&E) not tagged `PaymentsToAcquirePropertyPlantAndEquipment` / `PaymentsToAcquireIntangibleAssets`.
   - If one exists, FCF yield falls from about 8% to about 6% and base value from about $95 to about $70.
2. **D&A composition** (S2). The split between depreciation and acquired-intangible amortisation is UNKNOWN, and so is the remaining life of acquired intangibles ($4,461.6M at Jun-26).
   The fade assumption is worth about $25 per share.
3. **10-year yield 5.20%** (dossier: yfinance ^TNX, not cross-checked). A 1pp change in WACC moves base value by −$18 to +$26 (grid).
   The cost of debt is a coupon proxy, and debt is weighted at book.
4. **GAAP vs adjusted.** Adjusted EPS is about 2x GAAP. Restructuring and integration charges have recurred, so I treat them as real and value off GAAP EBITDA.
   Anyone using the 10x forward P/E is implicitly assuming they stop.
5. **Margin direction.** The Q2 adjusted operating margin fell 210bp y/y, gross margin fell 2.1pp FY23→FY25, and adjusted EPS was flat on +4.8% sales (dossier §3–4).
   The price discounts a 26.7% EBITDA margin. Is the trend toward bear (23.4%) or bull (30%)? This is the variable that flips value.
6. **Receivables +15.1% vs sales +7.2% (FY25).** What part is acquired Paragon 28 receivables and what part is collection slippage? Organic DSO is UNKNOWN.
7. **Missing claims on EV:** operating leases, the Paragon 28 CVR (up to $1.00/share × Paragon share count, UNKNOWN), pensions and the Swiss note amount are all UNKNOWN.
   Net debt is understated by an unknown amount.
8. **M&A as recurring capex.** 2025 acquisitions ($1,393M) were about one year of FCF, and acquired capital earns about 5% ROIC (below WACC).
   If deals recur, owner earnings and the DCF overstate distributable cash.
9. **Share count.** I used 190.74M basic. Latest diluted is UNKNOWN, and FY25 diluted (198.7M) gives $91.46. The $1B FY26 buyback is not credited in net debt or share count, a partial offset.
10. **Currency.** All values are USD. The investor is SGD-based, so USD/SGD translation and US dividend withholding are not modelled here.
