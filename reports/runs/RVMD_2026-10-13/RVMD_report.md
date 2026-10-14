# Equity Analysis: RVMD — Revolution Medicines
As of 2026-10-13 · Price 193.95 USD · Template rNPV · Run: `reports/runs/RVMD_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**No Lynch category yet.** Revenue is zero, so it's not a turnaround either; it becomes a Fast Grower from about 2027 if the launch works. **Why own it:** RASONQUE (daraxonrasib) was approved on 2026-08-26 as a first-in-class RAS(ON) inhibitor for pancreatic cancer (overall-survival hazard ratio 0.40), with three molecules in Phase 3 and five breakthrough designations. **What has to happen:** $194 needs about **$18.5B of peak sales**. Pancreatic cancer alone can't get there (Quant $6.0B, Skeptic up to $8.4B), so lung cancer must become a second multi-billion franchise, and that hasn't read out (RASolve 301, 2027). **What could go wrong:** lung disappoints or the pancreatic launch undershoots, and the stock re-rates toward $58–105 while the company still needs about $1.3B more funding before profitability.

## 1. Executive Summary & Expected Value
- **Current Price:** $193.95 · **12-mo change:** +298% (−12% from the 2026-08-27 high of $221.15)
- **Bear / Base / Bull:** $15.61 (15%) / $57.72 (65%) / $119.53 (20%). **Corrected by the Skeptic** from the Quant's $15.60 / $63.38 / $130.49.
- **Expected Value (probability-weighted):** **$63.76** → margin of safety **−204%**. On the Skeptic's alternative (higher pancreatic peak sales), EV is $105.38, still −84%.
- **SBC-adjusted Expected Value:** $63.76. SBC is already a cost; it's worth about $14.6 a share (25% of base value).
- **Price implies (reverse rNPV):** about 1.94x the Quant's base peak sales, or about 38,000 patient-years on drug per year at list price, a 45.8% revenue CAGR from 2027 to 2034. The literal `reverse_dcf()` figure of 79% overstates it, because the function scales early losses too.
- **Asymmetry:** −0.73
- **Recommendation:** **TRIM** (MEDIUM conviction, dropped one level for the unresolved pancreatic peak-sales disagreement, which is worth more than 15% of fair value). The price is above even the bull case on both the Quant's and the Skeptic's numbers.

## 2. Business Quality (Buffett)
**Moat:** not rated, since none is evidenced yet: no margin or ROIC history, and patent expiry is UNKNOWN. First-in-class status and clinical data are the potential moat. **Circle of competence:** clinical-stage oncology sits **outside** a Buffett/Lynch circle. Outcomes hinge on trial readouts and launch uptake that can't be predicted from financials. That alone argues for keeping the position small. **ROIC vs WACC:** not meaningful (negative NOPAT). WACC is 10.2%.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | n/m (EBITDA negative) | n/m | UNKNOWN |
| P/E (ttm / fwd) | n/m (losses) | n/m | UNKNOWN |
| P/FCF (SBC-adjusted) | n/m (TTM FCF −$1,451M SBC-adjusted) | n/m | UNKNOWN |
| FCF Yield / Owner-Earnings Yield | negative / negative | n/m | n/m |
| PEG (or VOID + reason) | VOID: no earnings | n/a | n/a |
| Lynch ratio (g + yield) / PE | n/m | n/a | n/a |
| ROIC vs WACC | n/m vs 10.2% | n/m | n/m |
| Net debt / Owner earnings | net cash $3.94B (30 Jun) vs $500M converts + $549M royalty liability; runway ~2.7 yrs | n/m | n/m |
Runway: every scenario runs short of cash in 2029 without new funding (−$0.6B to −$1.3B at the low point).

## 4. DCF Scenarios (rNPV)
WACC is 10.2%: 10-yr US Treasury 5.22% (FRED), ERP 5%, beta 1.0. **Terminal value is 0% in every case**, an explicit decline after loss of exclusivity (assumed 2042, UNKNOWN). As a going-concern cross-check with a 1% terminal value, base is $88.48 and terminal value is 74.9% of EV, right at the flag. **Skeptic corrections:** IRA Medicare price negotiation added (−6.5% to base), 9.74M vested options at $25.62 added under the treasury-stock method (−2.6%), and the risk-free rate set to FRED's 5.22% (−0.2%). The 10-Q verified the convert conversion price at $198.80 and 2.19M warrant shares.
- **Bear (15%): $15.61.** Lung and first-line pancreatic fail; second-line-plus pancreatic only (~$1.5B peak); floored at net cash.
- **Base (65%): $57.72.** Pancreatic ~$6.0B worldwide peak plus partial lung; IRA haircut.
- **Bull (20%): $119.53.** Pancreatic plus lung both succeed (~$15.5B peak).
Base rates: oncology Phase 3 to approval is 35.5%, or 63.6% with biomarker selection (Wong, Siah & Lo 2019). About two-thirds of launches miss year-1 forecasts (McKinsey).

## 5. The Skeptic's Audit
- **Number audit:** 16 checked, 3 failed (IRA negotiation omitted, vested options omitted, risk-free rate). Base fell 8.9%. The Quant also found and fixed two errors in the August `rvmd_dcf.py` template: H1-26 cash burn counted twice and an unsourced NOL figure. The Researcher found that ~$750M of the "$1.5B committed capital" in the August deep dive is a floating-rate secured term loan (SOFR with a 3.5% floor, plus 5.75%), not non-dilutive cash. Draw status: UNKNOWN.
- **Capital Allocation Grade: B−** (financing discipline in place of the $1 test, given the $3.97B accumulated deficit).
  - Market value created is $6.06 per $1 paid in at market, or $1.78 at our EV.
  - The 2026 raises came above intrinsic value ($142 follow-on; converts at $198.80), so they were accretive.
  - On the other side: 28%/yr dilution; a Royalty Pharma deal with an implied 21% IRR to RP in the base case; a secured term loan; and **zero insider buys against ~$157M of insider sales** ($48M since approval).
  - The 672k sq ft HQ lease is **related-party**: the landlord is affiliated with Farallon, a ~6.4% holder.
- **Quality of Earnings:** SBC is 18% of the absolute value of TTM OCF and grew 68%/yr from FY20 to FY25. Early RASONQUE gross margins **will be flattered** because pre-launch inventory was expensed as R&D, so don't extrapolate Q3–Q4 2026 COGS. A $151M non-cash warrant charge in Q2 ends when the warrants expire in Dec 2026.
- **Bear thesis:** pancreatic cancer alone can't carry $194; the price needs lung to become a second multi-billion franchise.
- **Primary Downside Catalysts:**
  1. **RASolve 301** (second-line RAS-mutant lung cancer vs docetaxel, 2027). Signpost: an overall-survival hazard ratio of **0.80 or worse, or a progression-free-survival-only win**. That would take about $20 a share off base.
  2. **Pancreatic launch.** Signposts: quarterly RASONQUE sales from the ~2026-11-05 report (date unconfirmed), then the RASolute 303 first-line readout. **FY2027 net sales below $600M** (the price implies about $1.24B), or 303 failing or showing a hazard ratio above 0.75, confirms it.
- **Unresolved disagreements (Quant vs Skeptic):**

| Issue | Quant | Skeptic | Effect |
|---|---|---|---|
| Pancreatic peak sales | $6.0B worldwide | up to $8.4B (ACS 2026 US deaths of 52,740 × **assumed** share and duration) | base $57.72 → $95.21 (+65%); EV → $105.38. **Still TRIM** |
| Bear floor | net-cash floor $15.60 (unfloored −$2.25) | partly agree; earlier R&D cut gives +$2.81 | −$2.7 on EV if unfloored |
| Funding the 2028–29 gap | neutral at intrinsic value | raising at market would be accretive (+$4.3); in a bear case, dilutive | not applied |

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD.
- **Dividends:** none, so withholding doesn't matter.
- **Estate tax:** **US-situs**, and it's a large-cap US name, so it counts toward the US$60k estate-tax threshold together with ZBH and other US listings.
- **Tax on selling:** no capital-gains tax, so trimming after a +298% year costs nothing in tax.
- **Sizing:** binary-ish outcomes outside the Buffett/Lynch circle argue for a small position regardless of verdict. Biotech exposure overlaps with INSM, PRAX, MDGL, CELC, ACAD and INCY in the same book.

## 7. Sources
1. RVMD 10-Q Q2 2026 and 10-K FY2025 (SEC EDGAR): cash, converts ($198.80 conversion), warrants, options (Note 13), Royalty Pharma terms
2. 8-K 2026-08-05 (FY26 opex guidance); 8-K 2026-09-01 (HQ lease); FDA approval of RASONQUE 2026-08-26; Form 4 filings (EDGAR XML)
3. FRED DGS10: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
4. American Cancer Society, Cancer Facts & Figures 2026 (US pancreatic cancer deaths)
5. Wong, Siah & Lo (2019), *Biostatistics*: clinical-trial success rates by phase and therapeutic area
6. yfinance price history; `data/fundamentals.json` (2026-10-13)
7. Run files: `01_research.md`, `facts.json`, `02_quant.md`, `02_model.py`, `03_skeptic.md`, `03_rerun.py`

VERDICT:        TRIM
AS_OF:          2026-10-13
PRICE:          193.95 USD
FAIR_VALUE:     63.76 USD
UPSIDE:         -67.1%
ENTRY_BELOW:    38.26 USD
EXIT_ABOVE:     82.89 USD
CONVICTION:     MEDIUM
KEY_RISK:       Price needs ~$18.5B peak sales, i.e. NSCLC success (RASolve 301, 2027) on top of PDAC
DATA_WARNINGS:  2
