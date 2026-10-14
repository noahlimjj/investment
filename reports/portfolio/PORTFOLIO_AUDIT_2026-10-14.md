# Portfolio audit (2026-10-14)

> Built only from verified `/analyse` runs: report_lint pass, stage-file provenance (each stage written by its value-* subagent) and a lint seal from a Claude Code session. Runs that fail verification are listed with the reason and contribute nothing.
> Generated 2026-10-14T07:43+00:00 UTC · holdings snapshot `ibkr_20261014_112528.png` (2026-10-14T04:41:32.689404+00:00) · live prices: yfinance last price (may be delayed)

## Coverage
- Holdings: 19 · verified verdicts: 9 · need a pipeline run: 10
- Verified verdicts: SELL 1 (VXUS) · TRIM 5 (TSM, ZBH, RVMD, SYK, 000660.KS) · HOLD 3 (VWRA.L, MC.PA, NVO)
- No verified verdict (run `/analyse`): LAD, BABA, TM, PRAX, INCY, CELC, MDGL, INSM, 402340.KS, ACAD

## Verified verdicts

| Ticker | Verdict | Run (age) | Run price | Live | EV / expected return | EV vs live | Entry / Exit | Live vs bands | Key risk |
|---|---|---|---|---|---|---|---|---|---|
| **VXUS** | SELL (MEDIUM) | 2026-10-13 (1d) | 84.52 USD | 84.54 USD | 6.64%/yr base 10-yr net return for a Singapore holder (probability-weighted 6.15%/yr; same exposure in an Irish wrapper 6.77%/yr) | n/a | n/a (FUND) | n/a | Structural: 30% US withholding (~62 bp/yr) and US-situs estate exposure; switch before the December ex-date |
| **000660.KS** | TRIM (HIGH) | 2026-10-13 (1d) | 1,443,000 KRW | 1,419,000 KRW | 713,831 KRW | -49.7% | 428,299 KRW / 927,980 KRW | above EXIT_ABOVE | Price requires peak HBM margins to persist 5 full years without a cyclical downturn while Samsung ramps supply |
| **RVMD** | TRIM (MEDIUM) | 2026-10-13 (1d) | 193.95 USD | 188.44 USD | 63.76 USD | -66.2% | 38.26 USD / 82.89 USD | above EXIT_ABOVE | Price needs ~$18.5B peak sales, i.e. NSCLC success (RASolve 301, 2027) on top of PDAC |
| **SYK** | TRIM (HIGH) | 2026-10-13 (1d) | 283.71 USD | 282.55 USD | 207.87 USD | -26.4% | 166.30 USD / 270.23 USD | above EXIT_ABOVE | Price discounts ~10% revenue CAGR for a decade while M&A returns lag and peripheral vascular issues persist |
| **TSM** | TRIM (MEDIUM) | 2026-10-13 (1d) | 444.35 USD | 445.12 USD | 268.24 USD | -39.7% | 160.94 USD / 348.71 USD | above EXIT_ABOVE | Price embeds ~18-19%/yr growth for 10 yrs (bull case) while capex and overseas fabs lock in costs before any AI digestion |
| **ZBH** | TRIM (MEDIUM) | 2026-10-13 (1d) | 92.17 USD | 92.08 USD | 71.18 USD | -22.7% | 49.82 USD / 92.53 USD | between EV and EXIT_ABOVE | Price needs FY23-peak-plus margins while margins erode and buybacks run ~1.5x value on rising debt |
| **MC.PA** | HOLD (MEDIUM) | 2026-10-13 (1d) | 381.65 EUR | 390.25 EUR | 332.30 EUR | -14.8% | 199.00 EUR / 432.00 EUR | between EV and EXIT_ABOVE | Price needs PRO margin back to ~26.8% (FY21 peak) while Fashion & Leather margin slides toward its pre-COVID 33% and inventory builds |
| **NVO** | HOLD (MEDIUM) | 2026-10-13 (1d) | 38.02 USD | 38.06 USD | 45.40 USD | +19.3% | 34.05 USD / 59.02 USD | between ENTRY_BELOW and EV | US WAC list cuts of 35-50% in 2027 and tirzepatide competition compress EBIT margins toward 30-33% on DKK 140B debt load |
| **VWRA.L** | HOLD (MEDIUM) | 2026-10-13 (1d) | 193.34 USD | 193.74 USD | 6.30%/yr base 10-yr net return (probability-weighted 6.13%/yr) | n/a | n/a (FUND) | n/a | Implied equity premium ~1% over a 5.22% 10y Treasury on a 62%-US, AI-concentrated index at 21x |

## No verified verdict

| Ticker | Shares | Status | Why |
|---|---|---|---|
| **LAD** | 10 | UNVERIFIED | runs LAD_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |
| **BABA** | 6 | UNVERIFIED | runs BABA_2026-10-13 failed verification: 03_skeptic.md lacks the <!-- pipeline:value-skeptic --> header: not pipeline output; provenance: 02_quant.md: no provenance record: not written by its value-* subagent (outside agent or hand edit) - re-run that stage through /analyse |
| **TM** | 38 | UNVERIFIED | runs TM_2026-10-13 failed verification: 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output; 03_skeptic.md lacks the <!-- pipeline:value-skeptic --> header: not pipeline output |
| **PRAX** | 6 | UNVERIFIED | runs PRAX_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |
| **INCY** | 40 | UNVERIFIED | runs INCY_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |
| **CELC** | 20 | UNVERIFIED | runs CELC_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |
| **MDGL** | 10 | UNVERIFIED | runs MDGL_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |
| **INSM** | 40 | UNVERIFIED | runs INSM_2026-10-14, INSM_2026-10-13 failed verification: provenance: 01_research.md: no provenance record: not written by its value-* subagent (outside agent or hand edit) - re-run that stage through /analyse; provenance: 02_quant.md: no provenance record: not written by its value-* subagent (outside agent or hand edit) - re-run that stage through /analyse |
| **402340.KS** | 8 | UNVERIFIED | runs 402340.KS_2026-10-13 failed verification: 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output; 03_skeptic.md lacks the <!-- pipeline:value-skeptic --> header: not pipeline output |
| **ACAD** | 200 | UNVERIFIED | runs ACAD_2026-10-13 failed verification: 01_research.md lacks the <!-- pipeline:value-researcher --> header: not pipeline output; 02_quant.md lacks the <!-- pipeline:value-quant --> header: not pipeline output |

## Holding notes (verbatim from the verified reports)

### TSM — Taiwan Semiconductor Manufacturing (ADR) (TRIM, MEDIUM)

**Fast Grower with a cyclical overlay.** Revenue grew 24.5% a year FY21–25, but FY23 fell 4.5%. **Why own it:** TSMC makes most of the world's leading-edge chips. Its return on invested capital is about 47%, there has been no dilution in 5 years, and AI demand has it guiding to roughly +40% USD revenue growth in FY26. **What has to happen:** at $444 the market needs about 18–19% a year revenue growth for 10 years. No company with over $50B of revenue has sustained 20%+ for a decade (Mauboussin base rates, secondary source). **What could go wrong:** AI capex pauses for digestion while TSMC's own capex (US$60–64B in FY26) and overseas fabs are locked in. Margins would then fall toward management's 56% gross-margin floor just as the multiple compresses. It's a great business at a price that already assumes the bull case.

- **Bear thesis:** AI-capex digestion hits while TSMC's capex and overseas commitments are locked in. Margins revert toward 56% and the multiple compresses at the same time.
- **Report:** `reports/runs/TSM_2026-10-13/TSM_report.md`

### VWRA.L — Vanguard FTSE All-World UCITS ETF (USD Acc) (HOLD, MEDIUM)

No Lynch category: this is an index fund, not a company. **Why own it:** it's a cheap, tax-efficient way for a Singapore resident to own about 3,800 global stocks. Fees are 0.14%, US dividends are taxed at 15% inside the fund, and the fund is not counted for US estate tax. **What has to happen:** global per-share earnings have to compound at roughly 4% or more a year for it to beat a 10-year Treasury, and at about 8% for a normal equity premium. **What could go wrong:** you're buying a 62%-US, AI-heavy index at 21x earnings. Its earnings yield (4.76%) is below the 5.22% Treasury yield, so a decade that only matches bonds is plausible without any recession.

- **Bear thesis:** a valuation and discount-rate squeeze on a market whose earnings are increasingly one trade. A 10% earnings normalisation plus a de-rating to 19x gives 4.17%/yr, below today's Treasury yield.
- **Report:** `reports/runs/VWRA.L_2026-10-13/VWRA.L_report.md`

### VXUS — Vanguard Total International Stock ETF (US-domiciled) (SELL, MEDIUM)

No Lynch category: this is an index fund. **Why own it:** cheap (0.05% expense ratio), broad ex-US equity exposure, including small caps. **The problem is the wrapper, not the index:** for a Singapore resident, a US-domiciled fund's distributions carry 30% US withholding, and the fund is US-situs for estate tax. The same stocks held through an Irish UCITS fund (VWRA's ex-US sleeve, or an Irish ex-US fund) avoid both. **What it costs:** about **62bp a year**, or roughly **US$1,100 per US$10,000 over 10 years**. That holds in every scenario modelled, so switching has no modelled downside.

- **Bear thesis:** semiconductor and memory earnings revert while the multiple compresses. On top of that the wrapper leaks about 62bp/yr for certain, and **the leak is the only part of the downside you can remove.**
- **Report:** `reports/runs/VXUS_2026-10-13/VXUS_report.md`

### ZBH — Zimmer Biomet Holdings (TRIM, MEDIUM)

**Slow Grower drifting down.** The organic growth guide is 2.25–3.25%, GAAP EPS fell about 15% a year from FY23 to FY25, and knees are flat. **Why own it:** ZBH is a scaled hip-and-knee franchise with a 70% gross margin, and it looks cheap on adjusted earnings (10.8x forward). **What has to happen:** to justify $92, margins must climb back above the FY23 peak (30.8% EBITDA against 27.2% today), or revenue must compound at about 6% for a decade, something it hasn't done organically in any 4-year window since 2016. **What could go wrong:** that is already happening. Adjusted operating margin is down 210bp, and management is buying back stock at about 1.5x our value, partly with borrowed money.

- **Bear thesis:** the price assumes FY23-peak-plus margins while the trend runs the other way, and capital is being returned above value with borrowed money.
- **Report:** `reports/runs/ZBH_2026-10-13/ZBH_report.md`

### RVMD — Revolution Medicines (TRIM, MEDIUM)

**No Lynch category yet.** Revenue is zero, so it's not a turnaround either; it becomes a Fast Grower from about 2027 if the launch works. **Why own it:** RASONQUE (daraxonrasib) was approved on 2026-08-26 as a first-in-class RAS(ON) inhibitor for pancreatic cancer (overall-survival hazard ratio 0.40), with three molecules in Phase 3 and five breakthrough designations. **What has to happen:** $194 needs about **$18.5B of peak sales**. Pancreatic cancer alone can't get there (Quant $6.0B, Skeptic up to $8.4B), so lung cancer must become a second multi-billion franchise, and that hasn't read out (RASolve 301, 2027). **What could go wrong:** lung disappoints or the pancreatic launch undershoots, and the stock re-rates toward $58–105 while the company still needs about $1.3B more funding before profitability.

- **Bear thesis:** pancreatic cancer alone can't carry $194; the price needs lung to become a second multi-billion franchise.
- **Report:** `reports/runs/RVMD_2026-10-13/RVMD_report.md`

### SYK — Stryker Corporation (TRIM, HIGH)

**An elite medical-technology Stalwart priced as an infallible high-growth compounder.** Stryker has grown reported revenue at 11.8% annualized from FY20 to FY25 (approximately 9.0% organic), driven by its market-leading Mako surgical robotics and orthopedic implants. **Why own it:** Stryker holds durable #1 and #2 positions across joint replacement, neurotechnology, and hospital capital equipment, supported by deep surgeon switching costs, proprietary robotics workflows, and consistent mid-teens adjusted EPS growth. **What has to happen:** to justify its current $283.71 price tag, Stryker must sustain a constant 10.2% revenue CAGR for a full decade at 24% EBITDA margins while successfully scaling its $4.8B Inari Medical acquisition and managing a major CEO transition at year-end 2026. **What could go wrong:** serial acquisitions ($14.1B spent in FY20–FY25) have yielded $1.7B in cumulative impairments and pushed net debt to $11.5B; if peripheral vascular manufacturing issues linger or robotic competitors (Zimmer's ROSA, J&J's VELYS) slow Mako's momentum, organic growth will fade toward 5%, triggering an overdue multiple contraction from 29x trailing GAAP P/E toward mature medtech norms.

- **Bear thesis:** The serial acquisition treadmill stalls as integration friction and regulatory scrutiny increase. As hospital robotics competition closes the gap on Mako and peripheral vascular manufacturing issues drag into 2027, organic growth slows toward 4%–5%, deflating Stryker's premium valuation multiple toward 15x–16x.
- **Report:** `reports/runs/SYK_2026-10-13/SYK_report.md`

### 000660.KS — SK Hynix Inc. (TRIM, HIGH)

**A classic Peter Lynch Cyclical trading at the euphoria of a peak memory cycle.** Operating margins reached an unprecedented 76.3% in Q2 2026 (TTM 68.0%) driven by temporary quasi-monopoly pricing power in High Bandwidth Memory (HBM3E) for AI accelerators. **Why own it:** SK Hynix is the undisputed packaging leader in HBM via its MR-MUF technology, enjoys close alignment with Nvidia, and holds a fortress balance sheet with over KRW 69T in net cash plus US$26.2B in recent ADS listing proceeds. **What has to happen:** to justify today's market price of KRW 1,443,000, current peak shortage conditions and 70%+ EBIT margins must persist uninterrupted for five consecutive years without an industry downcycle. **What could go wrong:** memory hardware has never decoupled from supply-demand cycles; as Samsung Electronics and Micron qualify 12-layer HBM3E/HBM4 and hyperscalers digest AI cluster capex, HBM prices will collapse, compressing operating margins back toward mid-cycle averages (25–29%) and slashing earnings by more than 60%.

- **Bear thesis:** The HBM shortage ends as Samsung qualifies 12-layer HBM3E with Nvidia and hyperscalers digest AI cluster investments. Memory prices collapse, driving operating margins from 76% down to 20–25% while billions in fab capex commitments (M15X, Yongin) convert into heavy fixed depreciation charges.
- **Report:** `reports/runs/000660.KS_2026-10-13/000660.KS_report.md`

### MC.PA — LVMH Moët Hennessy Louis Vuitton (HOLD, MEDIUM)

**A former Stalwart, now Cyclical at depressed margins.** Revenue grew 5.9% a year FY21–25, but EPS fell 2.2% a year and sits 28% below the FY23 peak. **Why own it:** it's the world's largest luxury group, with a gross margin held at 66–69% through the downturn, ROIC of 15.7% against a 9.5% WACC, a 3.4% dividend yield, and Arnault-family control above 50%. **What has to happen:** the price needs group operating margin (profit from recurring operations, PRO) back to about 26.8%, against 21.9% TTM. That's roughly the FY21 peak. **What could go wrong:** the 2021–23 margins were a price-hike boom, not mid-cycle. Fashion & Leather margin has fallen every year since FY21 and is heading back toward its pre-COVID 33%. Q3 2026 organic growth was just +1%, with Fashion & Leather −5% on China, and inventory is building.

- **Bear thesis:** the 2021–23 margins were a price-hike boom, not mid-cycle. Fashion & Leather keeps sliding toward its pre-COVID 33% while China stays soft, so value converges on the trough case (about €309) or lower.
- **Report:** `reports/runs/MC.PA_2026-10-13/MC.PA_report.md`

### NVO — Novo Nordisk A/S (HOLD, MEDIUM)

**A former Fast Grower now transitioning to a Stalwart facing Cyclical-like pricing resets.** Revenue grew 24.3% annualized from FY20 to FY25, but 2026 guidance calls for sales of -6% to 0% at constant exchange rates as US pricing concessions bite. **Why own it:** Novo Nordisk is the global duopoly leader in metabolic therapies (diabetes and obesity) with unassailable manufacturing scale, deep clinical formulation IP, an underlying ROIC above 30%, and a share price that has already de-rated 68% from its 2024 peak to 11.8x normalised trailing earnings. **What has to happen:** the company must successfully transition patient volumes from injectable semaglutide to next-generation combination therapies (CagriSema) and oral amycretin while defending net operating margins above 38% after the 2027 US Wholesale Acquisition Cost (WAC) list price cuts. **What could go wrong:** semaglutide represents nearly 70% of total revenue; if 35–50% US list price cuts translate directly into severe net price deflation while Eli Lilly's tirzepatide and next-gen oral GLP-1s erode market share, operating margins will compress toward 30% while the company carries DKK 140B in gross borrowings.

- **Bear thesis:** Semaglutide monoculture collapse. Mandatory US WAC cuts of 35–50% from Jan 1, 2027, combine with Eli Lilly's tirzepatide superiority and incoming oral competitors, driving net operating margins from 43% down to 30–33% while fixed debt obligations of DKK 140B constrain capital flexibility.
- **Report:** `reports/runs/NVO_2026-10-13/NVO_report.md`

## Data notes

- **VWRA.L**: position column truncated in the screenshot ('.1087'): leading digits hidden behind the Instrument column, so the share count is UNKNOWN. Re-send a screenshot with the Position column fully visible (landscape, or scroll right).
- **VXUS**: position column truncated in the screenshot ('.5925'): leading digits hidden behind the Instrument column, so the share count is UNKNOWN. Re-send a screenshot with the Position column fully visible (landscape, or scroll right).

