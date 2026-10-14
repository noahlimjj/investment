<!-- pipeline:value-quant -->
# Quant model: RVMD (as of 2026-10-13)

Revolution Medicines, NASDAQ, USD. Price **$193.95** (close 2026-10-12; fund `price`). Template: **rNPV**
(dossier §0: RASONQUE approved 2026-08-26, product revenue not yet reported). Status: CURRENT HOLDING.
Model: `reports/runs/RVMD_2026-10-13/02_model.py` (executed; every number below is copied from its output).
No scenario probabilities and no verdict here; the Skeptic assigns those.

**Tape check (RULE 0).** Price $193.95, trailing P/E not meaningful (FY25 diluted EPS −5.95, facts), 12-month
change +297.8% (facts `market`), −12.3% from the 2026-08-27 all-time-high close. Under every set of operating
assumptions I can defend from the dossier, the rNPV comes out below the price: bear $15.60, base $63.38,
bull $130.49. The tape and the model disagree, and **that disagreement is the finding**: the price discounts
a ~$18.5B peak-sales RAS(ON) franchise (section F). Whether that is plausible is a question about epidemiology
and trial outcomes, and the dossier has sourced data for neither.

**Data warnings carried (fund `warnings`, 2):** (a) institutional_pct = 1.0127, a vendor artifact, not quoted;
(b) owner earnings are negative and confirmed against the cash flow statement (below). `errors`: none.
**Data conflict found:** FY2025 D&A is 7.78 in facts (XBRL `DepreciationDepletionAndAmortization` /
`DepreciationAmortizationAndAccretionNet`) vs 16.56 in fund. Owner earnings come out at −1,139.5 vs −1,130.7.
The gap is immaterial to valuation, but the Skeptic should note it.

---

## A. Lynch classification & category checks

**Category: none assignable on the data.** I am not forcing a category, per the AGENTS.md routing table.
`revenue_cagr` is `null` in facts, and revenue went 43 → 29 → 35 → 12 → 0 → 0 over FY2020–25 (collaboration
revenue only, facts `annual.revenue`). Diluted EPS went −2.01 → −5.95 (losses widening). With no earnings base, a
growth-rate category cannot be computed. **The category is changing.** The company has just moved from
clinical-stage to commercial launch. If the launch and the Ph3 programme work, it becomes a Lynch **Fast Grower**
from roughly 2027. Until revenue prints (Q3 report expected ~2026-11-05, unconfirmed, dossier §3), that is a
forecast, not a classification.

Because the business still burns cash, the relevant Lynch checks are the **Turnaround-style survival checks**:
- **Cash vs burn:** cash plus marketable securities are $3,938.0M (facts `balance_sheet_2026_06_30`). H1-2026 CFO
  was −741.5 (facts). At that run-rate and zero revenue, runway is **2.66 years**. FY26 GAAP opex guidance of
  $2.1–2.2B (dossier §3) implies H2-26 opex of 1,149.6–1,249.6, or about $2.4B annualised.
- **Modelled funding gap:** with no new financing, cumulative cash bottoms at **−$1,132M (bear, 2029),
  −$1,324M (base, 2029) and −$566M (bull, 2029)**. Every scenario needs outside capital before profitability.
  Possible sources are the Royalty Pharma capacity of up to $750M in royalty tranches plus up to $750M in term
  loan. Both are milestone-contingent, and royalty tranches raise the royalty burden (dossier §3).
  Alternatively the company issues equity. The 2020–25 diluted share CAGR was 28.2% (facts).
- **Maturity wall:** none inside 5 years. Converts mature May 2033. The term loan, if drawn, matures at the
  earlier of 6 years after first draw or 2032-12-31. The royalty liability is repaid from sales (dossier §3, §5).
  The mandatory $250M Tranche 1 draw was due around 2026-10-10; its status is **UNKNOWN**.

Lynch metrics:
| Metric | Formula | Value |
|---|---|---|
| PEG | P/E ÷ growth | **VOID.** `peg_is_valid(None, −34.32, None)` → "missing growth or P/E". Not cited further |
| Lynch ratio | (EPS growth % + div yield %) ÷ P/E | n/m (negative EPS, no dividend) |
| Net-cash-adjusted P/E | (price − net cash/sh) ÷ EPS | n/m (EPS negative). Net cash/sh = (3,938.0 − 500.0)/214.336 = **$16.04** (8.3% of price); **$15.18** after the warrant liability |
| Inventory vs sales growth | Δinv% − Δsales% | UNKNOWN: no sales, inventory not tagged (facts `gaps`) |
| Receivables vs sales growth | Δrec% − Δsales% | UNKNOWN: same reason |
| Net debt / owner earnings | (debt − cash) ÷ OE | n/m: the company holds net cash and OE is negative |

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

- **Circle of competence / predictability: No.** Revenue ten years out depends on Ph3 readouts that have not
  happened (RASolute 303/304/305/309, RASolve 301/307/308; dossier §8 pipeline table). It also depends on
  epidemiology and pricing data the dossier lacks: patient counts, duration of therapy, and gross-to-net are
  all UNKNOWN. The modelled range runs from $1.5B to $15.5B peak and comes entirely from assumptions. By
  Buffett's standard this is "too hard" pile. The only hard efficacy datum is RASolute 302: mOS 13.2 vs 6.7 months,
  HR 0.40 (dossier §8).
- **Moat, from evidence only: not rated (None evidenced). Trend: UNKNOWN.** There is no gross-margin series (no
  product sales), no positive ROIC in any year, and no market-share data. The real barrier is regulatory and IP:
  an approved first-in-class RAS(ON) inhibitor with Breakthrough Therapy Designations (dossier §8). Its
  duration is unknowable here because **patent expiry is UNKNOWN**. Under rNPV routing, LOE timing goes into the
  model as an input (section G) and does not get a moat adjective.
- **Owner earnings (NI + D&A − capex), FY2025:** **−$1,130.7M** (fund `owner_earnings_usd`) or −$1,139.5M
  (facts, lower D&A tag). That is an **OE yield of −2.72%** on the $41,570.5M market cap. TTM to Jun-26 OE is
  −$1,768.8M (yield −4.25%), which includes the Q2 non-cash EQRx warrant remeasurement of 151.0 (facts
  `quarter_q2_2026`). On SBC: NI is already after SBC (FY25 SBC 118.4, facts), so OE needs no further
  adjustment. The SBC-adjusted cash measure is FCF − SBC: FY25 −$1,032.1M (yield −2.48%), TTM −$1,450.9M
  (yield −3.49%).
- **ROIC vs WACC:** ROIC is **not meaningful**. NOPAT is negative, and invested capital at 30 Jun 2026 is
  **negative** (equity 2,606.2 + converts 487.4 + royalty liability 548.5 − cash and marketable securities
  3,938.0 = −295.8; facts). facts `derived.roic` is null in every year. Goodwill of 14.6 is trivial, so an
  ex-goodwill ROIC is also n/m. **WACC = 10.18%** (section D). In the base case, steady-state economics look
  like a 44.1% EBIT margin on $9.5B (2036). A return on capital cannot be stated until revenue exists.

## C. GARP & valuation matrix

| Metric | Current | 5-yr own avg | Peer median |
|---|---|---|---|
| EV/EBITDA | n/m (FY25 operating income −1,182.4, facts) | UNKNOWN (no historical prices in dossier; EBITDA negative every year) | UNKNOWN (dossier §7) |
| P/E trailing / forward | n/m (trailing null; forward −34.32, fund) | UNKNOWN | UNKNOWN |
| P/FCF | n/m (FCF negative) | UNKNOWN | UNKNOWN |
| SBC-adjusted P/FCF | n/m | UNKNOWN | UNKNOWN |
| FCF yield (FY25 / TTM) | −2.20% / −2.96% | UNKNOWN | UNKNOWN |
| SBC-adj FCF yield (FY25 / TTM) | −2.48% / −3.49% | UNKNOWN | UNKNOWN |
| Owner-earnings yield (FY25) | −2.72% | UNKNOWN | UNKNOWN |
| PEG | **VOID** (missing growth / P/E) | VOID | UNKNOWN |
| Lynch ratio | n/m | n/m | UNKNOWN |
| P/B | 15.95x (book 2,606.2) | UNKNOWN | UNKNOWN |
| EV (mcap − cash & MS + converts) | $38,132.6M | n/a | n/a |
| EV incl. royalty liability and warrants | $38,866.4M | n/a | n/a |
| Price paid for the franchise (price − net cash after warrants) | $178.77/sh = $38,318M | n/a | n/a |

The usual multiples have nothing to measure here. The useful metrics are the reverse rNPV (section F) and the
$38.3B the market assigns to an asset with zero reported sales.

## D. Discount rate build

```
3. DISCOUNT RATE
Ke = rf 5.20% + beta 1.0 x ERP 5.0% = 10.20%
Kd = SOFR floor 3.50% + 5.75% = 9.25% pre-tax; tax shield 0 (no taxable income) -> 9.25%
Weights (market): E 41,571 (97.5%), D 1,048.5 (2.5%)
WACC = 10.177%; 8% USD floor binding? False -> WACC used 10.18%
```

- rf = 10-yr UST **5.20%** (facts `market.us10y_pct`, yfinance ^TNX). The dossier flags this as **not
  cross-checked against Treasury.gov**. A ±1% WACC grid is in section F.
- ERP 5.0% (stated). Beta 1.0 (no sourced beta in dossier).
- Cost of debt uses the marginal secured borrowing rate from the term-loan terms, 3.5% SOFR floor + 5.75% =
  9.25% (dossier §3), not the 0.50% convert coupon. Tax shield is 0 because there is no taxable income.
- Debt at market-value weights: converts at $500M principal plus the royalty liability at $548.5M carrying.
  Debt is 2.5% of capital, so the WACC is almost entirely the cost of equity.
- 8% USD floor: not binding.
- A single WACC applies to all three scenarios. Scenario risk sits in the cash flows, not the rate. This
  differs from the August template, which used 11.0/9.5/8.5%.

## E. DCF scenarios

**Structure (rvmd_dcf.py template, re-derived):** the explicit horizon runs H2-2026 to 2050. Post-LOE erosion
is modelled, so **terminal value = 0** (valuation.py docstring rule) and the **TV share is 0% in all
scenarios**. Cash flows are discounted mid-year from 30 Jun 2026 (the cash date) and rolled forward to
2026-10-13.

Fixes vs the August template:
1. Only H2-2026 opex is charged against 30-Jun cash. The template charged full-year 2026, which counted the H1
   burn twice.
2. The NOL proxy is the accumulated deficit of 3,967.3 (facts). The template used an unsourced 3,400.
3. Peak sales are re-set as labelled assumptions. The template's peaks were anchored on unverified
   sell-side numbers.
4. Post-LOE R&D and fixed SG&A wind down with revenue, so successor products are neither credited nor
   charged.

**SBC treatment: deducted as a cost.** Opex is GAAP opex, which includes SBC (FY26 guidance includes
$270–290M SBC, dossier §3). The **share count is held at 214.336M and is not grown for SBC.**

**Claims deducted:** converts at $500.0M par and the warrant liability at $185.3M. The **royalty-sale liability
($548.5M) is not deducted**, because the royalty payments are modelled explicitly in the cash flows (tiers
4.55% / 2.50% / 1.00% / 0%, dossier §3). Deducting both would double-count $2.56/sh.

Inputs per scenario:
| Input | Bear | Base | Bull | Source |
|---|---|---|---|---|
| Indications that succeed | 2L+ mPDAC only (303, 301 fail) | + 1L mPDAC, 2L RAS NSCLC, 1L G12C/G12D NSCLC | + adjuvant PDAC / CRC / other | scenario design (dossier §8 pipeline) |
| Total of segment peaks ($M WW net) | 1,500 | 9,500 | 15,500 | **QUANT ASSUMPTION, unsourced** |
| 2026 revenue (H2) | 48 | 72 | 96 | Q3 CONSENSUS $24.1M (dossier §3) + Q4 at 1x/2x/3x Q3 |
| H2-2026 opex | 1,199.6 | 1,199.6 | 1,199.6 | guidance mid 2,150 − H1 950.4 (dossier §2–3) |
| R&D path | 1,800 in 2027–28, then max(400, 30% of rev) | 1,800 → 2,300 by 2029 | 1,800 → 2,800 by 2030 | 2027 ≈ 75% of H2-26 annualised opex; plateau = assumption |
| SG&A | 450 + 15% of revenue | same | same | 450 ≈ Q2-26 G&A 110.2 × 4 (facts); 15% = assumption |
| COGS | 10% of sales | same | same | **UNKNOWN**, assumption |
| Royalty Pharma | tiered, tranches 1–2 | same | same | dossier §3 |
| LOE / post-LOE retention | 2042 (darax), 2046 (others) / 70% per yr | same | same | **patent expiry UNKNOWN**, assumption |
| Tax / NOL | 21% / 3,967.3 + new losses | same | same | statutory; facts accumulated deficit (upper-bound proxy) |
| WACC | 10.18% | 10.18% | 10.18% | section D |
| **Per-share value** | **$15.60** (net-cash floor; **unfloored −$2.25**) | **$63.38** | **$130.49** | 02_model.py |
| vs price | −92.0% | −67.3% | −32.7% | |
| TV share of EV | 0% | 0% | 0% | TV = 0 by construction |
| Cash trough, no new financing ($M) | −1,132 (2029) | −1,324 (2029) | −566 (2029) | 02_model.py |

**Going-concern variant (valuation.dcf(), 10 years 2027–36 plus a Gordon TV at g = 1% and terminal ROIC 15%).**
This variant assumes the pipeline renews the franchise after 2036, which the rNPV deliberately does not credit.
It gives bear $9.57 (dcf() net-cash floor), **base $88.48 (TV 74.9% of EV, just under the 75% flag)** and bull
$177.96 (TV 68.5%). The gap between base $63 (rNPV) and $88 (going-concern) is what one pays for assuming
successor products. Even this more generous framing leaves the bull case 8.2% below the price.

Model output (verbatim):
```
4. rNPV SCENARIOS (explicit H2-2026..2050, decline modelled, terminal value = 0)
Segment peak WW net sales ($M) -- QUANT ASSUMPTIONS, unsourced:
  segment                          launch  ytp   LOE    BEAR    BASE    BULL
  2L+ mPDAC (approved)               2026    5  2042   1,500   2,500   3,000
  1L mPDAC (RASolute 303/305)        2028    6  2042       0   3,500   5,000
  2L RAS NSCLC (RASolve 301)         2028    5  2042       0   1,500   2,500
  1L G12C/G12D NSCLC (307/308)       2030    6  2046       0   2,000   3,000
  Adjuvant PDAC / CRC / other        2030    6  2046       0       0   2,000
  TOTAL of segment peaks                               1,500   9,500  15,500
Translation: WAC $39,800/30d = $484K per patient-year gross; gross-to-net UNKNOWN

--- BEAR: modelled peak revenue $1,500M ---
Yr      Revenue     R&D    SG&A  RPRoy     EBIT    Tax      FCF      PV  CashBal
2026H2       48   (opex  1,200)      2   -1,158      0   -1,158  -1,131    2,780
2027        382   1,800     507     17   -1,981      0   -1,981  -1,798      799
2028        688   1,800     553     31   -1,765      0   -1,765  -1,454     -966
2029        972     400     596     44     -165      0     -165    -124   -1,132
2030      1,241     400     636     56       24      0       24      16   -1,108
2031      1,500     450     675     68      157      0      157      97     -951
2032      1,500     450     675     68      157      0      157      88     -794
2033      1,500     450     675     68      157      0      157      80     -637
2034      1,500     450     675     68      157      0      157      72     -481
2035      1,500     450     675     68      157      0      157      66     -324
2036      1,500     450     675     68      157      0      157      59     -167
2038      1,500     450     675     68      157      0      157      49      146
2040      1,500     450     675     68      157      0      157      40      460
2042      1,050     280     472     48      145      0      145      31      761
2044        514     137     232     23       71      0       71      12      934
2046        252      67     113     11       35      0       35       5    1,018
2048        124      33      56      6       17      0       17       2    1,059
2050         61      16      27      3        8      0        8       1    1,080
PV flows $-3,722M + net cash after converts & warrants $3,253M = equity $-469M (floor applied: True)
PER SHARE (rolled to 2026-10-13): $15.60  vs price -92.0% | unfloored $-2.25 | TV share 0%
Cumulative cash trough (no new financing): $-1,132M in 2029  <-- FUNDING GAP

--- BASE: modelled peak revenue $9,500M ---
Yr      Revenue     R&D    SG&A  RPRoy     EBIT    Tax      FCF      PV  CashBal
2026H2       72   (opex  1,200)      3   -1,138      0   -1,138  -1,111    2,800
2027        637   1,800     545     29   -1,802      0   -1,802  -1,635      999
2028      1,368   2,050     655     62   -1,536      0   -1,536  -1,265     -538
2029      2,765   2,300     865    110     -787      0     -787    -588   -1,324
2030      4,215   2,300   1,082    143      268      0      268     182   -1,056
2031      5,850   2,300   1,327    159    1,478      0    1,478     910      422
2032      7,007   2,300   1,501    171    2,334      0    2,334   1,305    2,756
2033      8,107   2,300   1,666    181    3,149      0    3,149   1,598    5,905
2034      8,917   2,300   1,788    181    3,757    369    3,388   1,560    9,293
2035      9,213   2,300   1,832    181    3,979    836    3,143   1,314   12,436
2036      9,500   2,300   1,875    181    4,194    881    3,313   1,257   15,749
2038      9,500   2,300   1,875    181    4,194    881    3,313   1,036   22,376
2040      9,500   2,300   1,875    181    4,194    881    3,313     853   29,002
2042      7,250   1,755   1,431    174    3,165    665    2,501     530   34,816
2044      4,572   1,107     902    147    1,959    411    1,548     270   38,304
2046      2,661     644     525    108    1,118    235      883     127   40,462
2048      1,304     316     257     59      541    114      427      51   41,500
2050        639     155     126     29      265     56      209      20   42,009
PV flows $9,958M + net cash after converts & warrants $3,253M = equity $13,210M (floor applied: False)
PER SHARE (rolled to 2026-10-13): $63.38  vs price -67.3% | unfloored $63.38 | TV share 0%
Cumulative cash trough (no new financing): $-1,324M in 2029  <-- FUNDING GAP

--- BULL: modelled peak revenue $15,500M ---
Yr      Revenue     R&D    SG&A  RPRoy     EBIT    Tax      FCF      PV  CashBal
2026H2       96   (opex  1,200)      4   -1,117      0   -1,117  -1,090    2,821
2027        764   1,800     565     35   -1,712      0   -1,712  -1,554    1,109
2028      1,710   2,133     707     78   -1,379      0   -1,379  -1,136     -270
2029      3,670   2,467   1,001    133     -297      0     -297    -222     -566
2030      5,803   2,800   1,320    159      943      0      943     640      376
2031      8,484   2,800   1,723    181    2,932      0    2,932   1,806    3,308
2032     10,576   2,800   2,036    181    4,501      0    4,501   2,516    7,809
2033     12,556   2,800   2,333    181    5,986  1,237    4,749   2,410   12,558
2034     14,042   2,800   2,556    181    7,101  1,491    5,610   2,584   18,168
2035     14,782   2,800   2,667    181    7,656  1,608    6,048   2,528   24,216
2036     15,500   2,800   2,775    181    8,194  1,721    6,473   2,456   30,689
2038     15,500   2,800   2,775    181    8,194  1,721    6,473   2,023   43,636
2040     15,500   2,800   2,775    181    8,194  1,721    6,473   1,667   56,582
2042     12,350   2,231   2,211    181    6,492  1,363    5,129   1,088   68,184
2044      8,602   1,554   1,540    181    4,467    938    3,529     617   75,900
2046      5,265     951     943    154    2,691    565    2,126     306   81,097
2048      2,580     466     462    105    1,288    271    1,018     121   83,583
2050      1,264     228     226     58      625    131      494      48   84,783
PV flows $23,947M + net cash after converts & warrants $3,253M = equity $27,199M (floor applied: False)
PER SHARE (rolled to 2026-10-13): $130.49  vs price -32.7% | unfloored $130.49 | TV share 0%
Cumulative cash trough (no new financing): $-566M in 2029  <-- FUNDING GAP

5. GOING-CONCERN VARIANT via valuation.dcf(): 10 yrs 2027-36 + Gordon TV (pipeline renews)
BEAR: EV $-1,807M (PV explicit -2,290, PV TV 483) | TV share -26.7% | per share $9.57 (-95.1%)
BASE: EV $17,251M (PV explicit 4,338, PV TV 12,913) | TV share 74.9% | per share $88.48 (-54.4%)
BULL: EV $36,817M (PV explicit 11,587, PV TV 25,229) | TV share 68.5% | per share $177.96 (-8.2%)
(g=1% <= min(4%, 10y 5.20%); terminal ROIC 15%; tax on losses = credit, a rough NOL proxy; D&A=capex=1% rev)
```

## F. Reverse DCF & sensitivity grid

**What must be true at $193.95.**
- **rNPV (base structure):** the price requires segment peaks **1.94x** the base case, i.e. **~$18.5B of peak
  worldwide net sales**. That is ~38,100 patient-years on drug per year at full WAC ($484K per patient-year
  gross), or ~47,600 at an assumed 80% gross-to-net. The revenue path is $1.24B in 2027 → $17.3B in 2034, a
  **45.8% CAGR from 2027**.
- **Going-concern structure, cost structure re-derived:** ~$15.1B revenue by 2036 (35.0% CAGR 2027→36).
- **`valuation.reverse_dcf()` as specified:** a constant **79.0% revenue CAGR for 10 years** from FY26E $72M,
  reaching $24.5B by 2036. This version overstates the requirement, because dcf() holds the margin list fixed, so
  scaling revenue also scales the 2027–29 losses. I report it because it is required, but I treat the two
  structure-consistent solves above as the real answer.

```
6. REVERSE DCF
rNPV (base structure: segments, timing, R&D, cost ratios, WACC 10.18%, LOE 2042):
  $193.95 requires segment peaks x1.943 -> modelled peak WW net sales $18,456M
  = 38,115 patient-years on drug per year at full WAC; 47,644 at an assumed 80% gross-to-net
  implied revenue path: 2027 $1,237M -> 2034 $17,324M = CAGR 45.8%
  (same solve on BEAR structure: x11.795 -> peak $17,693M)
  (same solve on BULL structure: x1.292 -> peak $20,020M)
valuation.reverse_dcf() on going-concern base (margin path fixed at base-case years 2027-36, g 1%, ROIC 15%):
  monotonic check: CAGR 0% -> $10/sh, CAGR 150% -> $5,115/sh
  implied constant revenue CAGR from FY26E $72M: 79.0% for 10 yrs -> 2036 revenue $24,480M
  (base-case 2036 revenue for comparison: $9,500M)
  CAVEAT: dcf() takes a fixed margin LIST, so scaling revenue also scales the negative 2027-29
  margins (bigger losses); this overstates the required CAGR. Structure-consistent solve below.
Going-concern structure, cost structure re-derived at each scale: x1.585 -> 2036 revenue $15,056M; 2027->2036 CAGR 35.0%

7. SENSITIVITY
rNPV BASE per share: WACC x segment-peak scale (base total peaks 9,500M = 1.0x)
(UNFLOORED values; the valuation.py net-cash floor would lift any value below it to ~$15.6)
WACC         0.50x     0.75x     1.00x     1.50x     2.00x     2.50x
8.18%           -9        36        77       159       241       323
9.18%           -9        32        70       145       220       295
10.18%         -10        28        63       133       202       271
11.18%         -10        25        58       122       185       249
12.18%         -11        22        52       112       171       229

Going-concern BASE per share (valuation.sensitivity): WACC +/-1% x terminal growth +/-1%
WACC          g=0%      g=1%      g=2%
9.18%          100       104       109
10.18%          86        88        92
11.18%          74        76        78

rNPV BASE per share: WACC x LOE year of daraxonrasib (patent expiry UNKNOWN)
WACC         2038     2040     2042     2044     2046
9.18%          55       63       70       76       80
10.18%         50       57       63       68       72
11.18%         46       52       58       62       65
```

## G. Load-bearing inputs

```
8. LOAD-BEARING INPUTS: effect of +/-10% on BASE rNPV per share
Base $63.38
input                                 -10%      +10%   max |d|
Segment peak sales (all)             49.38     77.34     13.99
Years to peak (+/-1 yr)              71.45     55.79      8.07
R&D spend path                       70.49     56.26      7.11
Share count                          70.42     57.62      7.04
WACC                                 70.07     57.45      6.69
SG&A variable % of revenue           66.20     60.56      2.82
Cash & MS (30 Jun)                   61.49     65.27      1.89
COGS % of sales                      65.26     61.49      1.88
Post-LOE retention (decay)           62.10     65.07      1.70
SG&A fixed                           64.82     61.93      1.45
Tax rate                             64.61     62.15      1.23
H2-26 opex                           63.88     62.87      0.51
Royalty Pharma tier rates            63.84     62.91      0.47
NOL opening balance                  63.19     63.56      0.18
LOE year 2040 (+/-2 yrs, not 10%): $57.42
LOE year 2044 (+/-2 yrs, not 10%): $68.17
NOL = 0 (no usable NOL, e.g. s.382 limits): $61.44
WACC at 8% floor: $78.77; at 12%: $53.23
```

| # | Input | Value used | Source | ±10% effect on base $63.38/sh |
|---|---|---|---|---|
| 1 | Segment peak sales (all indications) | 9,500 total | **QUANT ASSUMPTION, unsourced**. Dossier §9: consensus peak sales UNKNOWN; prior sell-side figures banned/unverified | $49.38 / $77.34 (±$14.0) |
| 2 | Years to peak (ramp speed) | 5–6 yrs | assumption | ±1 yr: $71.45 / $55.79 (~$8.1) |
| 3 | R&D spend path | 1,800 → 2,300 | 2027 from guidance run-rate (dossier §3); plateau assumption | $70.49 / $56.26 (±$7.1) |
| 4 | Share count | 214.336M basic | facts (10-Q cover). Option/RSU overhang UNKNOWN (+5% → $60.36) | $70.42 / $57.62 (±$7.0) |
| 5 | WACC | 10.18% | CAPM: ^TNX 5.20% (not cross-checked) + 1.0 × 5% | $70.07 / $57.45 (±$6.7). At 8% floor $78.77; at 12% $53.23 |
| 6 | LOE year (daraxonrasib) | 2042 | **UNKNOWN** (patent expiry not in dossier) | ±2 yrs: $57.42 / $68.17 |
| 7 | SG&A variable % of revenue | 15% | assumption | $66.20 / $60.56 (±$2.8) |
| 8 | Cash & MS at 30 Jun 26 | 3,938.0 | facts (10-Q) | $61.49 / $65.27 (±$1.9) |
| 9 | COGS % of sales | 10% | **UNKNOWN** | $65.26 / $61.49 (±$1.9) |
| 10 | Post-LOE retention | 70%/yr | assumption | $62.10 / $65.07 (±$1.7) |
| 11 | Tax rate / NOL | 21% / 3,967.3 | statutory / facts accumulated deficit (proxy). NOL = 0 → $61.44 | tax ±$1.2; NOL ±$0.2 |
| 12 | Royalty Pharma tier rates | 4.55/2.50/1.00/0% | dossier §3 (10-Q) | ±$0.5 |

Peak sales dominate everything else. A 2.0x base peak at 9.18% WACC gives ~$220; at 1.5x the base peak, the
value is $133 at the model WACC.

Side calculations (verbatim):
```
9. SIDE CALCULATIONS
Royalty Pharma drag (tranches 1-2 tiers):
  $1B sales -> $46M (4.55% blended)
  $2B sales -> $91M (4.55% blended)
  $4B sales -> $141M (3.52% blended)
  $8B sales -> $181M (2.26% blended)
  $12B sales -> $181M (1.51% blended)
  $16B sales -> $181M (1.13% blended)
Convertible notes (conversion price UNKNOWN): extra claim above $500M par if in the money = 500 x (P/Conv - 1); per-share hit, illustrative only:
  hypothetical conv. price $100: extra claim $470M = $2.19/sh
  hypothetical conv. price $150: extra claim $146M = $0.68/sh
  hypothetical conv. price $194: extra claim $0M = $0.00/sh
Option/RSU overhang UNKNOWN: +5% diluted shares -> base $60.36 (from $63.38)
New HQ lease ~$32M/yr +3%/yr 2028-2042 (dossier s5): PV $257M = $1.20/sh (not separately deducted; assumed inside opex)
Term loan tranche 1 ($250M, draw status UNKNOWN): cash +250 / debt +250 -> NAV-neutral ex 2% fee ($5M = $0.023/sh); coupon >= 9.25% vs WACC 10.18%
Royalty-sale liability $548.5M if ALSO deducted (double count): -$2.56/sh
BEAR: PV of flows 2042+ (post-LOE tail) $83M = -2.2% of PV flows
BASE: PV of flows 2042+ (post-LOE tail) $1,687M = 16.9% of PV flows
BULL: PV of flows 2042+ (post-LOE tail) $3,740M = 15.6% of PV flows
BEAR: 2036 EBIT margin 10.4% on revenue $1,500M
BASE: 2036 EBIT margin 44.1% on revenue $9,500M
BULL: 2036 EBIT margin 52.9% on revenue $15,500M
2026 anchor: BASE with Q4-26 = 1x Q3 consensus -> $63.29 (vs $63.38)
2026 anchor: BASE with Q4-26 = 3x Q3 consensus -> $63.46 (vs $63.38)
```

## H. Open questions for the Skeptic

1. **Peak sales are pure assumption.** This is the single biggest weakness of the model. Sourced 2L+ mPDAC
   treated-patient counts (US and EU), real-world duration of therapy, and gross-to-net would turn the reverse
   solve ("~38–48K patient-years on drug per year") into a testable claim. The prior dive's peak-sales figures
   are unverified and banned, and I did not use them.
2. **Patent / LOE date is UNKNOWN.** I assumed 2042 for daraxonrasib and 2046 for the next molecules. Each ±2
   years moves the base by about $5–6/sh.
3. **Funding gap.** All three scenarios run cash negative by 2028–29 (−$0.6B to −$1.3B) without new capital.
   Three items are UNKNOWN: whether the mandatory $250M term-loan Tranche 1 was drawn (due ~2026-10-10), which
   milestones gate the remaining Royalty Pharma capital, and whether optional royalty tranches would lift the
   royalty tiers. Equity raised below intrinsic value would cut per-share value further. The model funds the
   gap at intrinsic value, which is neutral.
4. **Bear floor realism.** The bear case prints $15.60 only because of the valuation.py net-cash floor.
   Unfloored, it is −$2.25: the 2026–28 Ph3 spend is largely committed before any failure is known. I think the
   unfloored number is the more honest one.
5. **Discount rate.** ^TNX 5.20% is not cross-checked and beta is unsourced. Each 1% of WACC moves the base by
   about $5–7/sh.
6. **Unknown claims on equity.** The convert conversion price is UNKNOWN; for a hypothetical $100 conversion
   price the extra claim would be $2.19/sh. The EQRx warrant count is UNKNOWN (deducted at the $185.3M liability
   value). The option/RSU overhang is UNKNOWN (+5% shares costs about $3/sh). Lease liability is UNKNOWN; the
   new HQ lease PV is about $1.20/sh and is assumed to sit inside opex.
7. **COGS and SG&A structure** are unsourced. The modelled 2036 EBIT margin is 44.1% at $9.5B (base) and 52.9% at $15.5B
   (bull), which is high for a single-franchise company. Please check whether it is too generous, since that would push values
   lower still.
8. **Scenario design vs probabilities.** Each scenario treats indications as binary (all in or all out). I
   applied no probability-of-success haircut, so the Skeptic's weights carry all of the clinical risk. Do not
   apply PoS on top of these values as well.
9. **rNPV vs going-concern.** TV = 0 (base $63) vs a renewing pipeline (base $88): which framing the thesis
   relies on is a judgement call for the Skeptic.
10. **D&A tag conflict** (7.78 vs 16.56 for FY25): which XBRL tag is right? It is immaterial to value.
11. The **2026 revenue anchor** uses the yfinance Q3 revenue CONSENSUS of $24.1M (range 0–55.9), labelled as
    such. Its effect on value is negligible: base $63.29–$63.46 for Q4 = 1x–3x Q3. The Q3 print (~2026-11-05) is the first hard datum
    for the ramp and the cheapest signpost to watch.

## Sources
Inputs only from: `01_research.md` (dossier; its sources 1–10, incl. 10-Q accn 0001193125-26-335104, 8-K accn
0001193125-26-335039, 8-K accn 0001193125-26-366931, 8-K accn 0001193125-26-377362), `facts.json` (SEC XBRL
companyfacts CIK 1628171, retrieved 2026-10-13), `data/fundamentals.json` (RVMD record, as_of 2026-10-13).
Engine: `methodologies/valuation.py`. Structural template: `methodologies/rvmd_dcf.py`.
