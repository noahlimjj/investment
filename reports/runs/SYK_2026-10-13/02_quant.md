<!-- pipeline:value-quant -->
# Quant model: SYK (as of 2026-10-13)

_Status: COMPLETE. Model: `reports/runs/SYK_2026-10-13/02_model.py` (executed 2026-10-14, exit 0). Every computed number below comes from that run's output._
_Template: **FULL** (dossier §0). Data layer: `fundamentals.json` SYK warnings `[]`, errors `[]`._
_No probabilities, no verdict: those are the Skeptic's job._

**Price basis:** $283.71, the 2026-10-13 close (dossier §1). `00_inputs.json` has $282.70 intraday (0.4% lower), so the reverse DCF is shown at both prices. Market cap is $108,824M (383.573M shares outstanding, facts `shares_outstanding_latest`). Net debt is $11,466M (debt 14,942 − cash 3,391 − marketable securities 85; dossier §1, 10-Q Q2-26). EV is $120,290M.

**Tape reconciliation (RULE 0):** The price is down 22.3% over 12 months (dossier §1). Trailing GAAP P/E is 29.4x (TTM NI 3,729 / 386.0M diluted shares = EPS $9.66). Forward P/E is 18.9x on FY26 guide-midpoint adjusted EPS of $15.025 (dossier §3).
- **The story:** a quality compounder hit by three one-offs. These are the Q1 cyber incident (organic +2.4%), the peripheral-vascular manufacturing issue (Q2 Vascular −0.7%), and the CEO handover.
- **What the tape and model say:** the de-rating is real. But the reverse DCF (§F) shows today's price still discounts about 10% revenue growth a year for a decade at 5-yr-average margins. So the market has cut the multiple but has **not** priced a growth slowdown. That gap is the analysis.

---

## A. Lynch classification & category checks

**Category: STALWART (upper band). The category is not changing on current evidence, but FY26 sits at its lower edge.**

| Growth measure | Value | Source |
|---|---|---|
| Revenue CAGR FY20–25 (includes M&A) | 11.8% | facts `revenue_cagr` |
| Revenue CAGR FY21–25 | 10.1% | facts revenue |
| Organic cc growth FY21–25 (mean) | 12.6 / 9.7 / 11.5 / 10.2 / 10.3% (mean 10.9%) | dossier §5 |
| GAAP diluted EPS CAGR FY20–25 / FY21–25 | 14.9% (COVID-depressed FY20 base) / 12.7% | facts `eps_diluted` |
| Adjusted EPS CAGR FY23–25 | 13.4% (10.60 → 13.63) | dossier §2 |
| FY26 guidance | organic +8.3% to 9.3%; adjusted EPS +9.7% to 10.8% vs FY25 | dossier §3 |
| H1-26 organic | 5.8% (Q1 2.4% cyber, Q2 9.0%) | dossier §3 |

- **Why Stalwart:** both EPS and organic revenue growth have run at about 10–13% for five years. That is well below Fast Grower (20%+). It is not a Cyclical: the only organic decline in six years was FY20 (−4.8%, COVID).
- **Is the category changing?** The H1-26 dip is explained by the Q1 cyber incident, and Q2 was back at 9.0%. FY26 guidance (organic ~8.8%, adjusted EPS ~+10%) is at the bottom of the stalwart band. A prolonged vascular problem plus a CEO-transition stall would push SYK toward slow-grower growth at a stalwart multiple. That is the downside path the bear case models.

**Stalwart checks**
- **P/E vs own 5-yr range: UNKNOWN.** The dossier has no 5-yr price history. As a partial proxy, the 52-week closing range ($269.75–$388.35, dossier §1) on TTM GAAP EPS of $9.66 gives **27.9x–40.2x** (same-EPS approximation). Today's 29.4x is near the bottom of that one-year band.
- **Diworsification and acquisition returns:**
  - FY20–25 acquisitions were **$14,102M**, or **76.4%** of cumulative FCF ($18,470M; model output). Dividends were $6,506M and buybacks zero. The **$2,138M** shortfall was debt-funded (debt rose from 13,991 to 15,859; facts).
  - The deals are adjacencies inside hospital medtech, not outside the core. Inari ($4.81B, peripheral vascular) and AVS sit in MedSurg & Neurotech, and Spinal was exited. So this is **not diworsification by category**.
  - The returns evidence is weak, though. Impairments FY21–25 were **$1,717M**, or 17.4% of FY21–25 acquisition spend ($9,880M; dossier §5). Spinal Implants was written down ($977M FY24) and sold for $165M.
  - **Crude acquisition-return test:** first-year acquired revenue (dossier §5 derived) was ≤ $1,791M on $14,102M spent, i.e. 12.7% revenue per dollar. At the FY25 group EBITA margin of 23.1%, that is a **≤ 2.9% pre-tax first-year yield**.
    - This understates the true return: acquired lines are reported as "organic" after 12 months, acquired margins are UNKNOWN, and Inari's gross revenue is UNKNOWN.
    - The opposite bound is incremental group ROIC FY21→FY25: **19.4%** at a constant pooled tax rate, or **12.8%** at each year's ETR. That mixes capital-light legacy organic growth with M&A capital, so it overstates acquired returns. The true acquired return lies between the two bounds.

**Lynch metrics**

| Metric | Formula | Value |
|---|---|---|
| PEG gate | `peg_is_valid(29.39, 16.99, 0.1066)` | **(True, 'ok')**. Growth used = lower of historical GAAP EPS CAGR FY20–25 (14.9%) and CONSENSUS adjusted EPS FY25→FY27 CAGR (10.7%; dossier §9, labelled) = **10.7%** |
| PEG | forward P/E / growth% | 18.9 / 10.7 = **1.77**. Trailing GAAP basis 29.4 / 10.7 = 2.76 (basis mismatch: GAAP P/E against adjusted growth). Vendor 1.3 not used (basis unknown) |
| Lynch ratio | (EPS growth% + yield%) / P/E | forward (10.7 + 1.24) / 18.9 = **0.63**; trailing (10.7 + 1.24) / 29.4 = **0.41**. Both are below 1 ("poor" on Lynch's scale) |
| Net-cash-adjusted P/E | (price − net cash/share) / EPS | net cash/share = −29.89. (283.71 + 29.89) / 9.66 = **32.5x** TTM GAAP; / 15.025 = **20.9x** forward adjusted |
| Inventory growth vs sales growth | Δinventory% − Δsales% | FY21 −24.4pp, **FY22 +12.7pp, FY23 +10.1pp** (supply-chain build; DSI 197→238 days), FY24 −11.7pp, FY25 +0.1pp. H1-26: inventory +4.0% vs H1 sales +6.1%. TTM DSI 223 days. **No current flag**; FY22–23 flags have unwound |
| Receivables growth vs sales growth | ΔAR% − Δsales% | **FY22 +10.1pp (flag)**, then −5.5 / −4.3 / −9.9pp. H1-26 AR −7.3% (DSO 59 → 53 days). No current flag. Acquired inventory and AR contaminate both series |
| Net debt / owner earnings | 11,466 / 3,678 | **3.1x** (1.83x FY25 EBITDA, CF D&A basis, ex-impairment). Interest cover 8.1x FY25, 9.2x TTM |
| Maturity wall | dossier §5 | 2026 $1,000M, 2027 $1,382M, 2028 $2,606M (2026–28 total **$4,988M**) vs cash $3,391M + revolver $2,910M + TTM FCF after dividends **$3,385M/yr**. Covered; no survival question |
| Dividend (informational) | | Declared/share CAGR 2021–25 7.1%; yield 1.24% ($3.52 run-rate); payout FY25 39.6% of NI / 30.0% of FCF (TTM 35.3% / 28.0%). No buybacks since 2019; share count creeping up ~0.3%/yr (facts `diluted_share_cagr` 0.32%) |

---

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence and predictability: PARTLY.**
- **Revenue can be sketched 10 years out.** Organic growth was 9.7–12.6% for five straight years and volume-led (FY25: 9.9% volume + 0.4% price; FY24: 9.1% + 1.1%; dossier §5). The only breaks were COVID and the Q1-26 cyber incident.
- **Margins, tax and capital deployment cannot:**
  - GAAP operating margin swung between 15.1% and 19.5% with impairments of $36M–$977M a year.
  - The GAAP ETR jumped from 12–14% (FY21–24) to **28.1% FY25 / 27.6% TTM**, and the dossier gives no cause.
  - $14.1B of M&A plus the spine exit keeps reshaping the mix.
  - Instrument-set cash spend is UNKNOWN.

**Moat, from evidence:**

| Evidence | Data (source) | Read |
|---|---|---|
| Gross margin | FY21–25 mean 63.7%, range 62.8–64.1%, stdev 0.48pp; FY20 63.1%; TTM 65.0% (Q2 includes tariff refunds, [SNIPPET]) (facts) | Very stable. Took a 1.3pt dip in 2022 inflation and fully recovered |
| Pricing | Price contribution +1.1% FY24, +0.4% FY25, −0.7% FY20 (dossier §5) | Modest pricing power. Growth is volume |
| ROIC, group (NOPAT / (equity + debt − cash − STI), each year's ETR) | 9.3 / 9.0 / 11.7 / 10.4 / 10.3% FY21–25, mean **10.1%**; TTM **11.3%** | Consistent but modest. M&A capital dilutes it |
| ROIC ex-goodwill | 19.8 / 19.4 / 25.2 / 21.6 / 23.6%, mean **21.9%**; TTM 24.8% (FY25 goodwill) | High and consistent: strong organic economics |
| Goodwill / invested capital | 52–56% (FY25 56.4%); goodwill / total assets 40.3% | Above 30%, so both ROICs are shown |
| Capital intensity | Capex/revenue 2.8–3.4%; capex/depreciation 1.42–1.77x; capex/(CF D&A) 0.53–0.72 | Capital-light |
| Market share | "One of four leading global competitors" in joints, trauma and robotics (10-K, dossier §8). **Trend UNKNOWN** | Oligopoly structure, trend unsourced |

**Rating: WIDE (organic franchise), trend STABLE.**
- **For Wide:** ex-goodwill ROIC was at least 19% in all five years, gross margin stayed within a 1.3pt band, capital intensity is low, and organic volume growth ran about 10% in a four-player market.
- **Why not "widening":** gross margin is flat, price contribution fell from 1.1% to 0.4%, and share trend is UNKNOWN.

**Which ROIC matters for the thesis: group ROIC including goodwill.** SYK reinvests about 76% of FCF in acquisitions, so a shareholder owns the acquisition programme, not just the organic franchise. The DCF terminal ROIC is therefore set on group returns: EBITA basis ex-impairments at the base tax rate, FY21–25 mean **12.9%** (min 11.1%, max 14.3%). Ex-goodwill ROIC is not used.

**ROIC vs WACC (WACC 8.9%, §D):**
- Group ROIC: 10.1% 5-yr mean / 11.3% TTM. **Spread +1.2pt / +2.4pt.**
- EBITA ex-impairment group ROIC: 12.9%. Spread +4.0pt.
- Ex-goodwill ROIC: 21.9%. Spread +13pt.

The organic franchise earns far more than its cost of capital. The capital actually deployed earns only slightly more.

**Owner earnings = NI + D&A − capex, with D&A on the cash-flow basis (orchestrator note; dossier §2, §10 Conflict B):**

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | TTM (estimate) |
|---|---|---|---|---|---|---|---|
| Owner earnings | 1,924 | 2,459 | 2,768 | 3,618 | 3,288 | **3,678** | ~4,147 |
| SBC-adjusted owner earnings | 1,782 | 2,288 | 2,600 | 3,413 | 3,059 | **3,435** | ~3,896 |
| Segment-D&A basis (NOT used) | 2,188 | 2,741 | 3,048 | 3,931 | 3,664 | 4,055 | |

- **Basis check:** FY25 owner earnings of 3,678 match `fundamentals.json` `owner_earnings_usd` (the model asserts this).
- **Why not the segment-D&A basis:** that basis (facts derived `owner_earnings` 4,055) adds back ~$377M of inferred loaner-instrument amortisation. The matching replacement spend sits inside OCF and is never deducted, so it overstates.
- **TTM is an ESTIMATE:** TTM cash-flow-basis D&A is UNKNOWN. I used segment TTM D&A of 1,618 less the FY25 gap of 377.

**Owner-earnings yield on market cap ($108,824M):**
- FY25: **3.38%** (SBC-adjusted 3.16%)
- TTM estimate: 3.81% (SBC-adjusted 3.58%)

**ZBH comparison (user holding; value SYK on its own evidence). Dossier §7 vendor multiples:**

| | ZBH | SYK |
|---|---|---|
| EV/EBITDA | 9.8x | 16.3x |
| Forward P/E | 10.3x | 17.0x |
| FCF yield | 6.05% | 3.77% |

- **The structural difference:** SYK has **no separate "instruments" investing line**. Instrument-set cash is inside OCF (dossier §2), so SYK's OCF − PP&E capex is not understated the way ZBH's vendor FCF was.
- **SYK's equivalent trap is on the D&A side:** segment D&A includes about $377M of loaner amortisation. That is why owner earnings and the DCF use cash-flow-basis D&A.

---

## C. GARP & valuation matrix

Peer set (dossier §7, single vendor, TTM, not re-verified): BSX, MDT, ABT, ZBH, ISRG, EW. The median sits between low-multiple ZBH and high-multiple ISRG and EW.

| Metric | Current | 5-yr own average | Peer median |
|---|---|---|---|
| EV/EBITDA | **16.8x** TTM (GAAP OI 5,534 + segment D&A 1,618); 19.2x FY25 (CF-basis D&A, ex-impairment); vendor 16.3x | UNKNOWN (no historical prices) | 15.4x |
| P/E trailing (GAAP) | **29.4x** | UNKNOWN | 28.0x |
| P/E forward | **18.9x** on FY26 guide-midpoint adjusted EPS $15.025; vendor 17.0x (= FY27 consensus basis) | UNKNOWN | 15.7x (basis unknown) |
| P/FCF | **23.1x** TTM (FCF 4,702); 25.4x FY25 | UNKNOWN | 25.3x (1 / median FCF yield) |
| SBC-adjusted P/FCF | **24.4x** TTM | UNKNOWN | UNKNOWN |
| FCF yield | **4.32%** TTM; 3.94% FY25; vendor 3.77% | UNKNOWN | 3.96% |
| SBC-adjusted FCF yield | 4.09% TTM | UNKNOWN | UNKNOWN |
| Owner-earnings yield | **3.38%** FY25 (SBC-adjusted 3.16%); TTM estimate 3.81% | UNKNOWN | UNKNOWN |
| PEG (valid) | **1.77** forward adjusted; 2.76 trailing GAAP (mismatched basis) | UNKNOWN | UNKNOWN |
| Lynch ratio | **0.63** forward; 0.41 trailing | UNKNOWN | UNKNOWN |
| Net-cash-adjusted P/E | 32.5x TTM GAAP; 20.9x forward adjusted | UNKNOWN | UNKNOWN |
| Dividend yield | 1.24% | UNKNOWN | UNKNOWN |

**Read vs peers (no verdict):**
- **Premium:** SYK trades above the peer median on EV/EBITDA (16.8x vs 15.4x) and forward P/E (18.9x on guidance vs 15.7x; 17.0x on the vendor's FY27 basis).
- **In line:** FCF yield and P/FCF.
- **Lynch's lens:** the Lynch ratio of 0.63 says a ~10.7% grower is priced at nearly 19x.

---

## D. Discount rate build

| Component | Value | Source / note |
|---|---|---|
| Risk-free (10y UST) | 5.22% | `00_inputs.json` DGS10, 2026-10-08. Not stale (5 days) |
| ERP | 5.0% | `00_inputs.json` |
| Beta, raw | 0.781 | `fundamentals.json` `beta` |
| Beta, Blume-adjusted | 0.67 × 0.781 + 0.33 = **0.853** | |
| Cost of equity | 5.22% + 0.853 × 5.0% = **9.49%** | CAPM |
| Cost of debt, pre-tax | 5.22% | Equal to the risk-free rate, used as a **lower bound**. Market YTM and spread are UNKNOWN. FY25 interest / average debt = 4.12% is below Treasuries, so it is not a market rate |
| Cost of debt, after-tax | 4.31% | At the base tax rate of 17.3% |
| Weights | E 87.9% (market cap 108,824), D 12.1% (debt 14,942 at book) | Market value of debt UNKNOWN. Leases excluded, consistent with net debt |
| **WACC** | raw **8.86%**, above the 8.0% USD floor, so **8.9% used** | |
| Alternatives (not used) | beta 1.0 (unsourced default): 9.51%; raw beta (no Blume): 8.54%; Kd +100bp: 8.96% | |

**WACC is the most load-bearing input (§G).**

| WACC component moved (one at a time) | WACC | Base value/share |
|---|---|---|
| Risk-free ×0.9 (4.70%) | 8.35% | $234.42 |
| Risk-free ×1.1 | 9.37% | $191.25 |
| Beta ×0.9 | 8.49% | $227.46 |
| Beta ×1.1 | 9.24% | $195.90 |

---

## E. DCF scenarios

**Basis decisions (each applied once):**
- **SBC is deducted.** EBITDA = GAAP operating income + goodwill and other impairments (non-cash) + cash-flow D&A. SBC stays expensed inside operating income and is never added back. The share count is held **flat** at diluted 386.0M (dossier §1). One method, not both, not neither.
- **D&A is on the cash-flow basis, 4.75% of revenue** (FY25 depreciation 461 + amortisation 732, dossier §2). Loaner-instrument amortisation (~$377M) stays in opex as the proxy for instrument-set cash spend.
- **Acquired amortisation is handled with `acq_amort_pct`, with no D&A fade.** acq_amort_pct = **2.91%** (FY25 amortisation of intangibles 732 / revenue 25,116). D&A is held flat. The alternative (fade D&A to capex instead) gives $200.96 (−3.9%). Caveat: the cash-flow line covers all intangibles; the 10-K note's split between acquired and other intangibles was not read (UNKNOWN), so it is treated as all acquired.
- **Leases are kept out of net debt.** SYK is a US-GAAP filer, so the $205M operating-lease cost is already inside EBITDA. The alternative line "leases in net debt + lease cost in EBITDA" (+3.9%) is **not a valid alternative**: it adds back lease cost without deducting right-of-use depreciation. It is shown only to prove the choice is not neutral.
- **Valuation date:** `mid_year=True`, `stub_years=0.2875` (2026-06-30 → 2026-10-13).
- **Equity bridge = $12,218.5M:**
  - Net debt $11,466M.
  - AVS contingent consideration fair value $271M (10-Q, dossier §5) and product-liability accrual $144M (dossier §8).
  - The Q2-26 dividend declared in the base period: $0.88 × 383.573M = $337.5M, which a buyer today won't receive.
  - Not included: the FY24-deal contingent consideration ($208M fair value at acquisition; current value UNKNOWN), pensions (UNKNOWN), and the Q3-26 dividend (ex-date UNKNOWN; −$0.88/share if deducted).
- **Working capital (w) is calibrated at 19.4% of organic Δrevenue** (FY21–25 pooled). The model's pre-working-capital FCF is set against the actual SBC-adjusted unlevered FCF, so that 5-yr-average inputs reproduce the 5-yr-average FCF margin. The base year-1 FCF margin is **15.8%**, against a **5-yr mean of 15.6%** (FY25 17.8%, TTM 18.9%). The base is therefore anchored below current cash conversion by construction.

**Scenario inputs** (10-year horizon; base revenue is TTM $25,837M; year 1 = Jul-26 to Jun-27)

| Input | Bear | Base | Bull | Source |
|---|---|---|---|---|
| Year-1 growth | 5.8% | 8.8% | 9.3% | H1-26 organic / FY26 guide midpoint / guide top (dossier §3) |
| Growth path | 5.8% for years 1–3, then fades to 3.0% | Fades linearly to 3.5% by year 10 | 10.3% in years 2–4 (FY25 organic, dossier §5), then fades to 4.0% | |
| 10-yr revenue CAGR | 4.7% | 6.1% | 8.0% | output |
| EBITDA margin (ex-impairment) | 23.3% → **22.3%** by year 3 (5-yr low, FY22) | **23.8%** flat (FY21–25 mean) | 24.9% (FY25), +50bp/yr to **27.4%** by year 6 | facts + dossier |
| Tax (NOPAT) | **27.6%** (TTM GAAP ETR persists) | **17.3%** (FY21–25 pooled GAAP ETR) | 17.3% | facts |
| Capex / revenue | 3.19% (TTM) | 3.09% (5-yr mean) | 3.03% (FY25) | facts |
| D&A / acq_amort_pct | 4.75% / 2.91% | 4.75% / 2.91% | 4.75% / 2.91% | dossier §2 |
| w (WC per organic Δrevenue) | 19.4% | 19.4% | 19.4% | calibrated |
| Terminal growth | 3.0% | 3.5% | 4.0% | Cap = min(4%, 5.22%) = 4% |
| Terminal ROIC | 9.8% (5-yr min EBITA ex-impairment ROIC at 27.6% tax) | 12.9% (5-yr mean at 17.3%) | 14.3% (5-yr max) | facts + dossier |
| WACC | 8.9% | 8.9% | 8.9% | §D |

Sourced reason for the bull's margin expansion: ex-impairment EBITDA margin rose from 22.4% (FY21) to 24.9% (FY25), +2.46pt or **+61bp a year** (model output), and Q2-26 adjusted operating margin was 27.4%, +170bp year on year (dossier §3).

**Results**

| | Bear | Base | Bull |
|---|---|---|---|
| EV ($M) | 62,941 | 92,944 | 129,716 |
| Equity ($M) | 50,723 | 80,726 | 117,498 |
| **Per share** | **$131.41** | **$209.13** | **$304.40** |
| vs $283.71 | −53.7% | −26.3% | +7.3% |
| Terminal value share of EV | 51% | 56% | 61% |
| Implied EV / TTM EBITDA (segment basis) | 8.8x | 13.0x | 18.1x |
| Implied P/E on FY26 guide-midpoint adjusted EPS | 8.7x | 13.9x | 20.3x |

No scenario has terminal value above 75% of EV.

**What the base case leaves out (one input changed each; output below):**

| Change | Value/share | vs base |
|---|---|---|
| EBITDA margin held at the FY25 level | $221.59 | +6.0% |
| w = 0 | $216.60 | +3.6% |
| Both together ("current conversion persists"; 2 inputs) | $229.06 | +9.5% |
| Years at 8.8% growth before the fade: 3 / 5 / 7 | $218.62 / $227.82 / $236.71 | |

None of these alone reaches the price. Only the bull scenario (growth at the guide top, then the FY25 organic rate, plus margin expansion) clears it.

`02_model.py` output, section E (pasted verbatim):
```
========== E. DCF SCENARIOS ==========
Calibration of w (pre-WC model FCF - actual SBC-adj unlevered FCF) / organic delta-revenue:
  FY21 drag 93 on dRev 1,808, actual m 16.7% | FY22 drag 980 on dRev 1,659, actual m 11.7% | FY23 drag 590 on dRev 2,122, actual m 15.8% | FY24 drag 686 on dRev 2,091, actual m 16.0% | FY25 drag -407 on dRev 2,327, actual m 17.8%
  pooled w = 1,943 / 10,007 = 19.4% | 5-yr mean SBC-adj unlevered FCF margin 15.6% | FY25 17.8% | TTM 18.9%
Common: base rev TTM 25,837 (yr1 = Jul-26..Jun-27) | D&A 4.75% (FY25 CF basis) | acq_amort_pct 2.91% (FY25 amortisation of intangibles) | WACC 8.9% | w 19.4% | mid_year, stub 0.2875y | bridge 12,218.5 | shares 386.0

--- BEAR: tax 27.6% | capex 3.19% | g_term 3.0% | ROIC_term 9.8%
    growth   [5.8, 5.8, 5.8, 5.4, 5.0, 4.6, 4.2, 3.8, 3.4, 3.0]
    EBITDA m [23.3, 22.79, 22.27, 22.27, 22.27, 22.27, 22.27, 22.27, 22.27, 22.27]
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1   27,336   6,369  5,070  1,298    871  3,809  13.9%  3,650
  2   28,921   6,590  5,216  1,374    921  3,923  13.6%  3,452
  3   30,598   6,815  5,362  1,453    975  4,037  13.2%  3,262
  4   32,251   7,183  5,651  1,532  1,027  4,277  13.3%  3,174
  5   33,863   7,542  5,934  1,608  1,079  4,515  13.3%  3,076
  6   35,421   7,889  6,207  1,682  1,128  4,748  13.4%  2,970
  7   36,909   8,220  6,467  1,753  1,176  4,973  13.5%  2,857
  8   38,311   8,533  6,713  1,820  1,220  5,190  13.5%  2,738
  9   39,614   8,823  6,941  1,882  1,262  5,395  13.6%  2,614
 10   40,802   9,088  7,149  1,938  1,300  5,586  13.7%  2,485
10-yr revenue CAGR 4.7% | PV explicit 31,030 | PV terminal 31,911 | TV share 51%
EV 62,941 | equity 50,723 | PER SHARE $131.41 | vs $283.71: -53.7% | implied EV/TTM-EBITDA(seg) 8.8x | implied P/E on FY26 guide-mid adj EPS 8.7x

--- BASE: tax 17.3% | capex 3.09% | g_term 3.5% | ROIC_term 12.9%
    growth   [8.8, 8.21, 7.62, 7.03, 6.44, 5.86, 5.27, 4.68, 4.09, 3.5]
    EBITDA m [23.81, 23.81, 23.81, 23.81, 23.81, 23.81, 23.81, 23.81, 23.81, 23.81]
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1   28,111   6,693  5,358  1,335    868  4,455  15.8%  4,269
  2   30,419   7,243  5,798  1,445    939  4,850  15.9%  4,268
  3   32,737   7,795  6,240  1,555  1,010  5,252  16.0%  4,244
  4   35,040   8,343  6,679  1,664  1,082  5,656  16.1%  4,197
  5   37,298   8,881  7,109  1,772  1,151  6,058  16.2%  4,128
  6   39,482   9,401  7,526  1,875  1,219  6,453  16.3%  4,037
  7   41,562   9,896  7,922  1,974  1,283  6,836  16.4%  3,927
  8   43,506  10,359  8,293  2,067  1,343  7,200  16.6%  3,799
  9   45,285  10,783  8,632  2,151  1,398  7,542  16.7%  3,654
 10   46,870  11,160  8,934  2,226  1,447  7,856  16.8%  3,495
10-yr revenue CAGR 6.1% | PV explicit 41,011 | PV terminal 51,933 | TV share 56%
EV 92,944 | equity 80,726 | PER SHARE $209.13 | vs $283.71: -26.3% | implied EV/TTM-EBITDA(seg) 13.0x | implied P/E on FY26 guide-mid adj EPS 13.9x

--- BULL: tax 17.3% | capex 3.03% | g_term 4.0% | ROIC_term 14.3%
    growth   [9.3, 10.3, 10.3, 10.3, 9.25, 8.2, 7.15, 6.1, 5.05, 4.0]
    EBITDA m [24.89, 25.39, 25.89, 26.39, 26.89, 27.39, 27.39, 27.39, 27.39, 27.39]
 yr  Revenue  EBITDA   EBIT    D&A  Capex    FCF   FCFm     PV
  1   28,240   7,030  5,688  1,341    856  4,721  16.7%  4,524
  2   31,149   7,909  6,430  1,480    944  5,286  17.0%  4,651
  3   34,357   8,896  7,264  1,632  1,041  5,972  17.4%  4,826
  4   37,896  10,002  8,202  1,800  1,148  6,744  17.8%  5,004
  5   41,401  11,134  9,167  1,967  1,254  7,609  18.4%  5,184
  6   44,796  12,271 10,143  2,128  1,357  8,495  19.0%  5,315
  7   47,999  13,148 10,868  2,280  1,454  9,187  19.1%  5,278
  8   50,927  13,950 11,531  2,419  1,543  9,838  19.3%  5,191
  9   53,498  14,655 12,113  2,541  1,621 10,433  19.5%  5,054
 10   55,638  15,241 12,598  2,643  1,686 10,954  19.7%  4,873
10-yr revenue CAGR 8.0% | PV explicit 51,138 | PV terminal 78,578 | TV share 61%
EV 129,716 | equity 117,498 | PER SHARE $304.40 | vs $283.71: +7.3% | implied EV/TTM-EBITDA(seg) 18.1x | implied P/E on FY26 guide-mid adj EPS 20.3x

BASE consistency: yr-10 explicit reinvestment rate (capex - depreciation + WC) / NOPAT = 12.1% (implied RONIC 28.9%) vs terminal reinvestment rate g/ROIC = 27.1% (ROIC 12.9%): terminal reinvests more, i.e. is the more conservative (consistent with growth partly bought via M&A at group returns)

Alternative-basis checks on BASE (one change each):
  D&A fade to capex by yr10 INSTEAD of acq_amort_pct             $ 200.96 (-3.9% vs base; TV 55%)
  segment D&A basis 6.25% (adds back loaner amort, no spend)     $ 218.93 (+4.7% vs base; TV 54%)
  tax 22.5% (midpoint pooled / TTM) in NOPAT                     $ 194.46 (-7.0% vs base; TV 56%)
  tax = TTM GAAP ETR 27.6% in NOPAT                              $ 179.79 (-14.0% vs base; TV 56%)
  EBITDA margin held at FY25 level                               $ 221.59 (+6.0% vs base; TV 56%)
  w = 0 (no WC drag; FY25/TTM-like conversion)                   $ 216.60 (+3.6% vs base; TV 54%)
  leases in net debt (+501) and lease cost (+205) in EBITDA      $ 217.24 (+3.9% vs base; TV 56%)
  no debt-like items / no dividend deduction                     $ 211.08 (+0.9% vs base; TV 56%)
  also deduct Q3-26 dividend (ex-date UNKNOWN)                   $ 208.26 (-0.4% vs base; TV 56%)
  basic shares 383.573M instead of diluted 386.0M                $ 210.46 (+0.6% vs base; TV 56%)
  no mid-year, no stub (old convention)                          $ 198.98 (-4.9% vs base; TV 57%)
  COMBINED (2 inputs): FY25 margin + w=0 (current conversion persists) $ 229.06 (+9.5% vs base; TV 54%)
  instrument spend > loaner amortisation by $100M/yr (capex +100/TTM rev) $ 206.61 (-1.2% vs base; TV 56%)
```
(The $198.98 "no mid-year" value equals the grid cell at WACC 8.9% / g 2.5% only by coincidence. I verified it: $198.9776 vs $198.9849, from different PV components.)

---

## F. Reverse DCF & sensitivity grid

**What must be true at $283.71.** Holding base margins, capex, tax, terminal growth, ROIC and WACC fixed, the price implies a **10.20% constant revenue CAGR for 10 years** (year-10 revenue $68.3B vs TTM $25.8B). At the `00_inputs` price of $282.70 the figure is 10.16%.
- That equals the FY21–25 organic mean (10.9%) and the FY20–25 reported CAGR including M&A (11.8%). The price assumes the last five years continue for another ten, with no fade, at 5-yr-average margins and a 17.3% tax rate.
- **Equivalent framings:**
  - 7.39% CAGR at bull margins (expanding to 27.4%).
  - A flat **30.3% EBITDA margin** at the base growth path (5-yr mean 23.8%, high 25.3%).
  - An **IRR of 7.54%** on base cash flows, below the 8.9% WACC. The IRR on bull cash flows is 9.24%.
- Caveat: the constant-CAGR solve drops from about 10% growth to 3.5% at year 10. That cliff understates the value of a gradual fade, which is why the "years at 8.8% before fading" lines in §E are shown too.

`02_model.py` output, section F (pasted verbatim):
```
========== F. REVERSE DCF & SENSITIVITY ==========
Implied constant 10-yr revenue CAGR at BASE margins/capex/tax/g/ROIC, price $283.71 (close): 10.20% (yr-10 revenue 68,253)
Implied constant 10-yr revenue CAGR at BASE margins/capex/tax/g/ROIC, price $282.7 (00_inputs): 10.16% (yr-10 revenue 67,976)
Implied constant 10-yr revenue CAGR at BEAR margins/capex/tax/g/ROIC, price $283.71 (close): 14.47% (yr-10 revenue 99,799)
Implied constant 10-yr revenue CAGR at BULL margins/capex/tax/g/ROIC, price $283.71 (close): 7.39% (yr-10 revenue 52,729)
Implied flat EBITDA margin at BASE growth path: 30.3% (5-yr mean 23.8%, high 25.3%)
Implied discount rate (IRR) on BASE cash flows at $283.71: 7.54% vs WACC 8.9%
Implied discount rate (IRR) on BULL cash flows at $283.71: 9.24%
  BASE with 3 yrs at 8.8% before fading: $218.62
  BASE with 5 yrs at 8.8% before fading: $227.82
  BASE with 7 yrs at 8.8% before fading: $236.71

BASE value/share, WACC (rows) x terminal growth (cols); ROIC_term 12.9% fixed
              2.5%      3.0%      3.5%      4.0%      4.5%
    7.9%    240.41    249.14    259.76    273.00    290.02 <floor
    8.4%    217.94    224.31    231.89    241.11    252.59
    8.9%    198.98    203.66    209.13    215.65    223.56
    9.4%    182.78    186.23    190.20    194.84    200.36
    9.9%    168.76    171.30    174.19    177.51    181.38
  (4.5% column exceeds the 4% terminal-growth cap: illustrative only)

BASE value/share, WACC x terminal ROIC (g 3.5% fixed)
             10.0%     12.0%     12.9%     16.0%     20.0%
    7.9%    240.30    254.76    259.76    272.84    283.68
    8.4%    215.18    227.59    231.89    243.11    252.42
    8.9%    194.63    205.41    209.13    218.87    226.95
    9.4%    177.50    186.94    190.20    198.72    205.80
    9.9%    162.99    171.31    174.19    181.71    187.95
```
Reading the grids:
- The only base-case cell at or above the price ($290.02) breaks **both** policy limits: WACC 7.9% (below the 8% floor) and g 4.5% (above the 4% cap).
- Within the g cap alone, the highest cell is $273.00, but only at WACC 7.9%.
- Within both the cap and the floor, the highest is **$241.11** (WACC 8.4%, g 4.0%).
- In the ROIC grid, even a 20% terminal ROIC at WACC 7.9% gives $283.68, just under the price.

---

## G. Load-bearing inputs

Each input moved ±10% (relative), one at a time, on the base case of **$209.13**. Everything else is held fixed. Each row is labelled by the input it actually moves.

| Rank | Input (base value) | Source | −10% | +10% | Note |
|---|---|---|---|---|---|
| 1 | **WACC** (8.9%) | 00_inputs rf/ERP + fund beta (Blume) | $253.11 (+21.0%) | $177.50 (−15.1%) | Driven mostly by the 5.22% risk-free rate. Unsourced beta 1.0 would give WACC 9.51% |
| 2 | **EBITDA margin** (23.8%, 5-yr mean ex-impairment) | facts + dossier §2/§5 | $181.71 (−13.1%) | $236.56 (+13.1%) | FY25 level (24.9%): $221.59 |
| 3 | **Revenue growth path** (8.8% fading to 3.5%) | guidance, dossier §3 | $198.59 (−5.0%) | $220.18 (+5.3%) | Duration matters more than level: 5 years at 8.8% gives $227.82 |
| 4 | Terminal ROIC (12.9%) | facts + dossier | $203.56 (−2.7%) | $213.69 (+2.2%) | 20% (closer to ex-goodwill ROIC): $226.95 |
| 5 | **Tax rate in NOPAT** (17.3%) | facts ETR | $214.12 (+2.4%) | $204.15 (−2.4%) | **±10% understates it:** the plausible range is 17.3–27.6%. At 27.6%: **$179.79 (−14.0%)** |
| 6 | Terminal growth (3.5%) | assumption, under the 4% cap | $205.21 (−1.9%) | $213.57 (+2.1%) | |
| 7 | Net debt + bridge items ($12,218.5M) | dossier §1/§5/§8 | $212.30 (+1.5%) | $205.97 (−1.5%) | |
| 8 | D&A % of revenue (4.75%) | dossier §2 | $211.50 (+1.1%) | $206.76 (−1.1%) | Segment basis (6.25%, wrong): $218.93 |
| 9 | Capex % of revenue (3.09%) | facts | $211.15 (+1.0%) | $207.12 (−1.0%) | Instrument spend $100M/yr above amortisation: $206.61 |
| 10 | acq_amort_pct (2.91%) | dossier §2 | $207.35 (−0.9%) | $210.92 (+0.9%) | Fade method instead: $200.96 |
| 11 | WC intensity w (19.4%) | calibrated | $209.88 (+0.4%) | $208.39 (−0.4%) | |

**Top 3:**
1. **WACC**, which is mostly the risk-free rate.
2. **EBITDA margin.**
3. **Tax rate**, on its realistic 17.3–27.6% range. On a strict ±10% test the third is the growth path.

---

## H. Open questions for the Skeptic

These are the places I was least sure.

1. **Tax rate (biggest single judgement).**
   - GAAP ETR was 12.1–14.3% in FY21–24, then 28.1% FY25 and 27.6% TTM. The dossier has no cause.
   - The base uses the FY21–25 pooled rate of 17.3%, which already includes FY25.
   - Hint, not proof: in FY25 the actual unlevered FCF beat the model at the 28% book rate by $407M (the calibration's FY25 drag is −407). That fits the excess being non-cash (deferred tax).
   - Please check the 10-K tax note (current vs deferred; any one-off from the spine sale or an IP transfer). If 27.6% is the cash rate, the base is $179.79.
2. **5-yr-average anchor vs current cash conversion.**
   - The base year-1 FCF margin is 15.8%, against 17.8% in FY25 and 18.9% TTM.
   - Is TTM flattered by the H1-26 receivables release (−$296M; DSO 59 → 53 days, possibly cyber-related collection timing) and Q2 tariff refunds ([SNIPPET])?
   - Note that FY22 (11.7%) drags the 5-yr mean. If current conversion persists, the base is $229.06.
3. **Instrument-set (loaner) cash spend is UNKNOWN.**
   - The model keeps ~$377M of loaner amortisation in opex as a proxy for the spend.
   - If spend runs ahead of amortisation (likely for a growing Mako and implant base), FCF is overstated: each $100M/yr costs about $2.52/share (−1.2%).
   - FY25 OCF "Other, net" (−$470M) is a candidate location (dossier §2).
4. **Terminal ROIC: group (12.9%) or organic?**
   - The explicit period's year-10 organic reinvestment implies a RONIC of about 29%. The terminal assumes growth at group M&A returns (reinvestment rate 27.1%).
   - If you think SYK can grow organically in perpetuity without buying growth, a 20% terminal ROIC gives $226.95.
5. **Split of amortisation between acquired and other intangibles** (10-K intangibles note, not read). acq_amort_pct = 2.91% assumes it is all acquired. Using the fade method instead gives −3.9%.
6. **Cost of debt.** Spread and market YTM are UNKNOWN; the risk-free rate was used as a floor. Kd +100bp moves WACC to 8.96%.
   - The risk-free rate of 5.22% is current, not stale. But it is the dominant WACC driver: risk-free ×0.9 gives $234.42.
7. **Equity bridge gaps.**
   - Current fair value of the FY24-deal contingent consideration is UNKNOWN (it was $208M at acquisition).
   - Pensions: UNKNOWN. Q2-26 lease liabilities: UNKNOWN (excluded anyway).
   - Q3-26 dividend ex-date: UNKNOWN (−$0.88/share if deducted).
   - Law-firm investigations into the disclosure of the manufacturing issue ([SNIPPET], dossier §10): not quantified.
8. **Peripheral-vascular manufacturing issue (Inari/AVS).** It was confirmed by Q2 Vascular −0.7% (US −6.7%). Its continuation into Q3 is [SNIPPET] only. It is not modelled separately; the bear's three years at 5.8% growth cover a prolonged version. Q3 results are not yet out (date UNKNOWN).
9. **CEO transition** (Lobo to Stiles on 2027-01-01). Not modelled. No number attaches to it.
10. **Moat call.** I rated SYK Wide on organic evidence (ex-goodwill ROIC 19–25% every year, gross margin within a 1.3pt band). The shareholder's actual return is group ROIC of 9–12%, only about 1–3pt above WACC, because about 76% of FCF goes to M&A. Please challenge whether "Wide" should be judged at the group level.
11. **The base WACC is not floor-bound** (8.86% raw vs 8.0% floor). The floor only matters in the grid's 7.9% row.
