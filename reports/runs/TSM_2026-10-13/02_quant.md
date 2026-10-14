<!-- pipeline:value-quant -->
# Quant model: TSM (as of 2026-10-13)

Template: **FULL** (profitable operating company; dossier §0). Price US$444.35/ADS (facts: market.price), USDTWD 32.133 (facts: market.usdtwd), 1 ADS = 5 common shares (facts: market.adr_ratio) => NT$2,855.7 per common share. All model numbers come from `02_model.py` (executed 2026-10-13, full output pasted under E/F). Units are NT$ millions unless stated. The DCF runs in NT$ per common share and converts to US$/ADS as × 5 ÷ 32.133.

**Tape check (RULE 0).** The stock is +48.3% over 12 months (facts: change_12m), trades at a 33.4x trailing P/E (34.3x excluding the VIS gain), and TTM revenue grew about 35% (dossier §2). The tape and the growth story agree. The numbers below show that the tape is paying for growth well above my base case.

**Data-layer warnings (fundamentals.json TSM): 1.** "cash-flow net income 2,041,654,700,000 differs from income-statement 1,697,604,000,000 by +20% (IFRS pre-tax start?) - income statement used". The re-fetched record is now correct (NI 1,697,604; owner earnings US$34.3B). Other data-layer issues not in `warnings`: `fx_to_usd` = 1.0 even though financials are in TWD (dossier §10.4), and the yfinance EV/EBITDA (5.1x), FCF yield (31.7%) and PEG (0.86) are currency-mismatched or vendor figures. **None of these three is used.** Errors: none.

## A. Lynch classification & category checks

**Category: Fast Grower with a Cyclical overlay.** It is changing from Cyclical toward Fast Grower, but that change is not proven through a full cycle.

| Evidence (02_model.py §A) | Value |
|---|---|
| Revenue CAGR FY21–25 = (3,809,054 / 1,587,415)^(1/4) − 1 (facts: annual.revenue) | **24.5%** |
| Net income (parent) CAGR FY21–25 (facts: net_income_parent). FY21 EPS is UNKNOWN, but shares were flat at 25,930M → 25,932.5M, so NI CAGR ≈ EPS CAGR | **30.1%** |
| EPS CAGR FY23–25 (32.85 → 65.47) | 41.2% |
| FY23 down-year: revenue y/y / NI y/y | −4.5% / −14.2% |
| Gross margin, 5-yr range (avg) vs TTM / 2Q26 | 51.6–59.9% (56.3%) vs **64.2% / 67.7%** |
| Operating margin, 5-yr range (avg) vs TTM | 40.9–50.8% (45.9%) vs **56.1%** |
| EBITDA margin FY23 / FY24 / FY25 / TTM (FY21–22 D&A UNKNOWN) | 67.2% / 68.6% / 68.9% / 71.6% |

- **Why Fast Grower:** both the revenue CAGR (24.5%) and the NI CAGR (30.1%) clear the 20% threshold. HPC grew from 43% to 58% of revenue (FY23 → FY25) and reached 66% in 2Q26 (dossier §3, §8).
- **Why the Cyclical overlay stays:** FY23 revenue fell 4.5% and NI fell 14.2%. Capex runs at 33–53% of revenue. Most importantly, **TTM margins sit above the top of the 5-yr range** (GM 64.2% vs a 59.9% max; OM 56.1% vs a 50.8% max). In Lynch's terms, earnings are being measured near peak margin. Evidence for "less cyclical than before": in the FY23 downturn, the cash (EBITDA) margin held at 67.2%, versus 68.9% at FY25. The swing came from depreciation and utilisation, not pricing. That is one down-year with D&A data, which is not enough to call the cycle gone.
- **What this means for valuation:** value it as a grower, but on **mid-cycle margins**. The base EBITDA margin is anchored on the FY23–25 average (about 68%), not on the TTM 71.6% or the 1H26 74.2%. The mid-cycle P/E is also reported below.

**Fast-grower checks**
- *Runway:* HPC share is still rising (66% in 2Q26). N2 is ramping (3% of 2Q26 wafer revenue). Arizona has a US$265B total pledge with "probably additional four or more fabs". A14 is due for volume in 2028 and A13/A12 in 2029 (dossier §3, §4, §8). Analyst-quoted figures that management did not confirm: N2 capacity CAGR of about 70% for 2026–28, and an AI accelerator CAGR in the mid-to-high 50s (dossier §4). Market share: UNKNOWN.
- *Funded internally?* Yes. TTM OCF 2,634,679 − capex 1,500,530 = FCF 1,134,150, which exceeds the 2026 dividend plan of NT$24 × 25,932.5M = 622,380 (54.9% of TTM FCF). Debt has been flat at about NT$1.05–1.07T since FY24, and there is no equity issuance (shares flat).
- *P/E vs growth:* normalised P/E 34.3x vs 30.1% historical NI growth, so the P/E sits slightly above the growth rate. The DCF base-case revenue CAGR is 12.8%, well below the historical rate.
- *Cyclical check (where in the cycle?):* margins are above the 5-yr range, so this is a late-cycle or peak-margin position. The classic trap is a low P/E at peak margins. Here the P/E is **not** low, so the risk is the opposite: margin and multiple could compress together. The 3Q26 guide (GM 65–67%, OM 56–58%) and the disclosed 2H26 dilution (N2 3–4 pts GM, overseas fabs 2–4 pts) point to margins easing from the 2Q26 peak (dossier §3).

**Lynch metrics** (02_model.py §A/§C)
- P/E trailing = 2,855.7 / EPS 85.49 = **33.4x**. Normalised (ex NT$2.24 VIS gain; facts: interim.2Q26.oneoff_vis_gain_eps) = 2,855.7 / 83.25 = **34.3x**. Mid-cycle = 2,855.7 / (TTM revenue × 5-yr average net margin 41.0% / shares = NT$70.26) = **40.6x**. Forward P/E 19.9x is a yfinance figure on an unknown basis and is unvalidated (dossier §9). It implies forward EPS of about NT$143/share, roughly +72% on normalised TTM. I have not verified it.
- **PEG:** `peg_is_valid(34.3, 19.9, 0.301)` returns **True (ok)**. Consensus growth is UNKNOWN (dossier §9), so the "lower of historical and consensus" rule can only use the historical 30.1%. PEG = 34.3 / 30.1 = **1.14**. Using the revenue CAGR instead gives 34.3 / 24.5 = 1.40. Caveats: the gate passed only because of the unvalidated vendor forward P/E, and the historical growth rate ends at an above-range margin year.
- **Lynch ratio** = (EPS growth 30.1 + dividend yield 0.84) / P/E 34.3 = **0.90**, which is poor (below 1). On the mid-cycle P/E it is **0.76**. Dividend yield = NT$24 / NT$2,855.7 = 0.84% (facts: guidance.div_2026_twd_per_share).
- **Net-cash-adjusted P/E** = (2,855.7 − net cash/share 94.4) / 83.25 = **33.2x**. Net cash = 3,517,787 − 1,068,556 = 2,449,231 (facts: balance_sheet_latest).
- **Inventory vs sales growth:** UNKNOWN. Only FY25 inventory (288,109.5) is in the dossier, and facts.json has no inventory series. Partial signal: inventory days were 87 in 2Q26, **up 7 days on the N2 ramp**, and AR days were 29 (dossier §2, CFO). I flag the inventory-days rise, but cannot test it against sales growth.
- **Receivables vs sales growth:** UNKNOWN (no AR series).
- **Debt structure:** net debt / owner earnings = −2,449,231 / 1,346,751 = **−1.82x** (net cash). Maturity ladder: UNKNOWN (dossier §5). Within 12 months, current-portion LT liabilities of 167,410 are covered 18.7x by cash alone.
- *Slow-grower dividend check (supplementary):* FY25 dividends paid 466,779 = 27.5% of NI and 46.6% of FCF. The dividend record is rising (265,786 in FY21 → 466,779 in FY25; NT$24/share planned for 2026, +33%).

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence / predictability: PARTLY.** Cash margins are unusually predictable (EBITDA 67–72% across FY23–TTM, including a down year), and the technology roadmap is published through 2029. But the **10-year revenue level is not predictable**. It depends on the durability of AI accelerator demand (management declined to give a number, and its own call raised the double-ordering question; dossier §4), on concentration (top-10 customers 70% → 78% FY23–25, top-2 at 36%), and on a Taiwan geopolitical risk that is binary and not modelled. I can sketch margins; I cannot sketch revenue with confidence.

**Moat: WIDE, trend WIDENING (by the margin and ROIC evidence), with caveats.**
| Evidence | Series | Source |
|---|---|---|
| Gross margin | 51.6 → 59.6 → 54.4 → 56.1 → 59.9% (FY21–25); TTM 64.2%, 2Q26 67.7% | facts: annual, interim |
| Pricing power | GM held above 54% in the FY23 down-year; CEO: "we don't suddenly increase our price by ... 4x or 5x", 68% GM aspiration | dossier §4 |
| ROIC | FY24 34.7%, FY25 44.0%, TTM 46.8% (FY21–23 UNKNOWN because debt is UNKNOWN; ROE 27.6/34.2/24.8/27.3/31.7%) | 02_model.py §B |
| Capital intensity | capex/revenue 52.9 → 47.8 → 43.9 → 33.0 → 33.4%, TTM 33.6% (5-yr avg 42.2%); capex/D&A FY23 1.78x, FY24 1.44x, FY25 1.85x, TTM 2.16x; **FY26 guide implies about 2.88x FY25 D&A** | 02_model.py §A/§B |
| Market share | UNKNOWN | dossier §8 |

Caveats against "widening": the trend is measured from a 2023 trough. Customer concentration is rising. Overseas fabs dilute GM by 2–4 pts. The FY26 capex step-up (US$60–64B, about 37% of FY26E revenue) means the moat must be re-bought every node.

**ROIC vs WACC:** TTM ROIC **46.8%** = NOPAT 2,042,748 (operating income 2,491,156 × 0.82) / IC 4,366,856 (parent equity 6,432,518 + debt 1,068,556 − cash 3,134,218). Counting current securities as cash gives 51.3%. **WACC 10.19%** (§D). The spread is about 37 pts. Goodwill is UNKNOWN (not in facts.json), so the ex-goodwill test cannot be run. No material M&A was identified (dossier §5), so goodwill is unlikely to be large, but it is unverified.

**Owner earnings** (NI + D&A − capex, AGENTS.md definition)
| | NT$M | US$ | Yield on mkt cap |
|---|---|---|---|
| FY25 (fund: owner_earnings; capex incl. intangibles 1,282,597) | 1,103,103 | US$34.3B (fund) | 1.49% |
| FY25, PPE capex only | 1,113,290 | | |
| TTM = 2,216,481 + 688,888 − 1,500,530 | 1,404,840 | | |
| TTM normalised (− VIS gain 2.24 × 25,932.5 = 58,089) | **1,346,751** | | **1.82%** |
| SBC-adjusted (− SBC): FY25 / TTM normalised | 1,101,857 / 1,346,067 | | ~same |

SBC is about 0.02% of revenue, so it is immaterial for TSMC. The forward warning: FY26 capex guided at about NT$1.98T (US$62B mid × 32) is 2.88x FY25 D&A. Owner earnings will lag net income until depreciation catches up.

## C. GARP & valuation matrix

| Metric | Current | 5-yr own avg | Peer median (dossier §7) |
|---|---|---|---|
| EV/EBITDA (TTM; EV 71,646,742 incl. NCI / EBITDA 3,180,044) | **22.5x** | UNKNOWN (no historical prices in dossier) | UNKNOWN (vendor EV currency-mismatched) |
| P/E trailing / normalised / mid-cycle | 33.4x / **34.3x** / 40.6x | UNKNOWN | 37.8x (yfinance, unvalidated) |
| P/E forward | 19.9x (yfinance, unvalidated, basis unknown) | UNKNOWN | 19.4x (yfinance, unvalidated) |
| P/FCF (74,054,021 / 1,134,150) | **65.3x** | UNKNOWN | UNKNOWN |
| SBC-adjusted P/FCF | 65.3x | UNKNOWN | UNKNOWN |
| FCF yield (TTM) / SBC-adjusted | **1.53%** / 1.53% | UNKNOWN (5-yr avg FCF *margin* 22.1%) | UNKNOWN |
| Owner-earnings yield (TTM normalised / FY25) | **1.82%** / 1.49% | UNKNOWN | UNKNOWN |
| PEG (gate VALID; historical growth only) | 1.14 (1.40 on revenue CAGR) | UNKNOWN | UNKNOWN |
| Lynch ratio | **0.90** (0.76 mid-cycle) | UNKNOWN | UNKNOWN |
| Net-cash-adjusted P/E | 33.2x | UNKNOWN | UNKNOWN |
| ROIC vs WACC | 46.8% vs 10.19% | FY24–25 avg 39.3% | UNKNOWN |
| Net debt / owner earnings | −1.82x (net cash) | UNKNOWN | UNKNOWN |

Peer set (dossier §7): ASML, AMAT, GFS, UMC, MU. It is a mix of equipment makers, foundries and memory, and the figures come from a single vendor. Treat it as context, not an anchor.

## D. Discount rate build

| Input | Value | Source |
|---|---|---|
| Risk-free rate | 5.277% | US 10y, facts: market.us10y_pct (^TNX 2026-10-13) |
| ERP | 5.0% | stated (brief) |
| Beta | 1.0 | no sourced beta in dossier |
| Cost of equity | **10.277%** | CAPM |
| Pre-tax cost of debt | 5.277% (proxy) | TSMC bond yields UNKNOWN, so the US 10y is used as a proxy (ASSUMPTION) |
| After-tax Kd (tax 18%) | 4.327% | |
| Weights (market value) | E 98.58% / D 1.42% | mkt cap 74,054,021; debt 1,068,556 |
| **WACC** | **10.19%** | USD floor of 8% not binding |
| Alt rf 5.22% (FRED DGS10, 2026-10-08, orchestrator note) | 10.14% | about −0.06 pp, immaterial |

**Currency choice (stated).** I discount NT$ cash flows at a **USD-built** rate. Reasons: (1) the equity the investor owns is priced in USD; (2) TSMC guides revenue in USD with an NT$ FX assumption (dossier §3), which suggests USD-linked pricing; (3) the Taiwan 10y is **UNKNOWN**, so a TWD-consistent rate (and the TWD floor of local 10y + 4%) cannot be built. Effect: if Taiwan rates are below US rates, a TWD WACC would be lower and NT$ value higher. Whether that would hold in USD per ADS depends on the future USDTWD path, which I do not model (spot conversion only). The ±1 pp WACC grid in §F brackets this.

**Geopolitical risk.** The base WACC has **no Taiwan country-risk premium** (beta 1.0, no CRP sourced). A +2 pp row in the grid shows the effect (base about US$218). I recommend the Skeptic treat cross-strait risk as an explicit scenario probability **or** a premium, not both, to avoid double-counting.

## E. DCF scenarios

Structure: year t = the 12 months to 30 June of 2026+t. Base revenue = TTM to 2Q26, 4,440,492.5 (facts: ttm.revenue). Net debt for DCF = debt 1,068,556 + NCI 41,953 − cash and current securities 3,517,787 = −2,407,278 (30 Jun 2026). Shares 25,932.5M. Tax 18% (2Q26 effective; dossier §2). Working capital = 10% of Δrevenue (ASSUMPTION: inventory ≈ 7.6% of revenue, AR 29 days ≈ 7.9%, payables UNKNOWN). Horizon 10 years.

**D&A rule:** D&A = 0.675 × trailing 5-period average capex, calibrated on FY25 (688,096 / average FY21–25 capex 1,020,020). This lets the depreciation wave from the capex step-up reach operating margin.

**SBC:** **deducted from the EBITDA margin** (SBC/revenue 0.0154%). The share count is held flat (25,930M in FY21 → 25,932.5M now), so there is no double count. SBC is immaterial either way.

**Year-1 revenue build:**
- Base: 3Q26 guide mid (US$45.2B × 32 = 1,446,400) + 4Q26 implied by FY26 +40% (1,481,792) + 1H27 = 1H26 × 1.25. This assumes NT$ growth equals the guided USD growth.

| Input | Bear | Base | Bull |
|---|---|---|---|
| Y1 revenue build | 2 × 3Q26 low (1,427,200) + 1H27 = 1H26 × 0.95 | 3Q mid + 4Q implied from FY26 +40% + 1H27 = 1H26 × 1.25 | 3Q high + 4Q from FY26 +42% + 1H27 = 1H26 × 1.35 |
| Growth Y1…Y10 | 15.7, **−10**, 8, 8, 7, 6, 5, 5, 4, 3% | 33.6, 20, 17, 14, 12, 10, 8, 7, 5, 4% | 40.8, 30, 25, 20, 16, 13, 10, 8, 6, 5% |
| 10-yr revenue CAGR | 5.0% | 12.8% | 16.9% |
| EBITDA margin | 68 → **62 (downturn)** → 63% | 70 → 69 → 68% (FY23–25 avg) | 73 → 72 → 71% |
| Resulting OM (Y10) | 46.3% (Y2–Y5 about 43%, near the 5-yr low of 40.9–42.6%) | 51.5% (Y1 56.9%, in line with the 3Q26 guide of 56–58%) | 56.0% |
| Capex % revenue | 37, 38, 34 → 26% | 37, 37, 35 → 26% | 37, 38, 36 → 24% |
| Terminal g / terminal ROIC | 2% / 15% | 3% / 25% | 4% / 35% |
| WACC | 10.19% | 10.19% | 10.19% |
| Avg FCF margin (5-yr hist 22.1%) | 24.1% | 26.3% | 29.1% |
| **Value NT$/share** | **843.3** | **1,861.8** | **3,115.0** |
| **Value US$/ADS (× 5 / 32.133)** | **131.23** | **289.71** | **484.70** |
| vs US$444.35 | −70.5% | −34.8% | +9.1% |
| TV share of EV | 58% | 65% | 70% (none above the 75% flag) |

Rationale and sources:
- **Bear:** the 3Q26 guide floor is effectively locked. Then comes an AI-digestion/double-ordering downturn (the risk management itself discussed, dossier §4): 1H27 −5% (FY23-like) and Y2 −10%. Margins compress to the 5-yr-low operating margin, and capex stays sticky into the downturn (FY23 capex/revenue was 43.9%).
- **Base:** FY26 "slightly above 40%" revenue (dossier §3) and the FY26 capex guide of US$60–64B (about 37% of revenue). Management says capex in the next three years will be "even more significantly higher" than the last three: the base spends NT$7.75T over Y1–3 vs NT$3.18T in FY23–25. Growth then fades to 4%. The EBITDA margin is anchored on the FY23–25 average (mid-cycle), not the TTM peak.
- **Bull:** 1H27 continues the 1H26 pace (+35.6%), backed by the N2 ramp and the Arizona expansion (dossier §4). The margin stays near 1H26 levels (EBITDA 74.2%, using depreciation only), consistent with the CEO's 68% GM aspiration.

Conventions **not** applied, all conservative: end-of-year discounting from 30 Jun 2026 (no roll-forward to 13 Oct: ×1.028; no mid-year convention: ×~1.050; together base about US$312.72). Government capex grants (FY25 NT$76,259M) are excluded. Non-current financial assets (FY25 134,337) are excluded.

`02_model.py` output, sections 0 / A / B / D / E (verbatim):
```

======== 0. Units, price and EV ================================================
ADS price US$444.35 x 32.133 NT$/US$ / 5 = NT$2,855.7 per common share
Market cap NT$74,054,021M | cash+current securities 3,517,787 | debt 1,068,556 | NCI 41,953
Net cash 2,449,231 = NT$94.4/share | EV 71,646,742 (US$2,229.7B)

======== A. History, growth, Lynch metrics =====================================
FY            Rev       g      GM      OM      NM  EBITDA%   D&A%  Capex%  Cx/DA   FCF%
2021    1,587,415     n/a   51.6%   40.9%   37.3%      UNK    UNK   52.9%    UNK  17.2%
2022    2,263,891  +42.6%   59.6%   49.5%   43.9%      UNK    UNK   47.8%    UNK  23.3%
2023    2,161,736   -4.5%   54.4%   42.6%   39.4%    67.2%  24.6%   43.9%   1.78  13.5%
2024    2,894,308  +33.9%   56.1%   45.7%   40.0%    68.6%  22.9%   33.0%   1.44  30.1%
2025    3,809,054  +31.6%   59.9%   50.8%   44.6%    68.9%  18.1%   33.4%   1.85  26.3%
TTM     4,440,492     n/a   64.2%   56.1%   49.9%    71.6%  15.5%   33.6%   2.16  25.5%
1H26 EBITDA margin (op inc + depreciation, amortisation excluded: UNKNOWN for 1H) = 74.2%

Revenue CAGR FY21-25 = (3,809,054/1,587,415)^(1/4)-1 = 24.5%
Net income (parent) CAGR FY21-25 = 30.1%  [EPS FY21 UNKNOWN; shares flat 25,930M -> 25,932.5M so NI CAGR ~ EPS CAGR]
EPS CAGR FY23-25 (2 yr) = 41.2% | FY23 NI y/y = -14.2%, FY23 rev y/y = -4.5%
5-yr ranges: GM 51.6%-59.9% (avg 56.3%); OM 40.9%-50.8% (avg 45.9%); NM avg 41.0%; capex/rev avg 42.2%; FCF margin avg 22.1%

P/E trailing = 2,855.7 / EPS 85.49 = 33.4x
P/E normalised (ex NT$2.24 VIS gain) = 2,855.7 / 83.25 = 34.3x
P/E mid-cycle = price / (TTM rev x 5-yr avg net margin 41.0% / shares = NT$70.26) = 40.6x
P/E forward (yfinance, basis unknown, unvalidated) = 19.9x

PEG gate peg_is_valid(trailing 34.3, fwd 19.9, g 30.1%) -> True (ok)
PEG = normalised P/E / NI CAGR = 34.3 / 30.1 = 1.14 (using revenue CAGR 24.5 instead: 1.40); consensus growth UNKNOWN
Dividend yield = NT$24 / 2,855.7 = 0.8%
Lynch ratio = (g 30.1 + yld 0.84) / P/E 34.3 = 0.90; on mid-cycle P/E: 0.76
Net-cash-adjusted P/E = (2,855.7 - net cash/sh 94.4) / 83.25 = 33.2x

======== B. Owner earnings, ROIC, capital intensity ============================
OE FY25 (fund) = NI 1,697,604 + D&A 688,096 - capex 1,282,597 = 1,103,103 (US$34.3B); PPE-only capex version 1,113,290
OE TTM = NI 2,216,481 + D&A 688,888 - capex 1,500,530 = 1,404,840; normalised (- VIS 58,089) = 1,346,751
SBC-adjusted: FY25 1,101,857 | TTM norm 1,346,067  (SBC 0.0% of rev)
OE yield on mkt cap: FY25 1.5% | TTM normalised 1.8%
Forward check: FY26 capex mid US$62B x 32 = NT$1,984,000M = 37.2% of FY26E rev 5,332,676; vs FY25 D&A 688,096 -> capex/D&A 2.88x
Dividends FY25 466,779 = 27.5% of NI, 46.6% of FCF; 2026 plan NT$24 x 25,932.5M = 622,380 = 54.9% of TTM FCF
Self-funding TTM: OCF 2,634,679 - capex 1,500,530 = FCF 1,134,150 > 2026 dividend 622,380
Net debt / OE = -2,449,231 / 1,346,751 = -1.82x (net cash)
Current portion LT liabilities 167,410 covered 18.7x by cash; maturity ladder UNKNOWN

ROIC = NOPAT / (equity + debt - cash), tax 17% for annual (FY25 rate), 18% TTM
  FY2024: NOPAT 1,097,304 / IC 3,163,682 = 34.7%
  FY2025: NOPAT 1,606,956 / IC 3,651,765 = 44.0%
  FY2021-23: debt UNKNOWN -> ROIC UNKNOWN. ROE (NI / year-end parent equity) instead:
    FY2021 ROE 27.6%
    FY2022 ROE 34.2%
    FY2023 ROE 24.8%
    FY2024 ROE 27.3%
    FY2025 ROE 31.7%
  TTM: NOPAT 2,042,748 / IC 4,366,856 (cash only) = 46.8%; / IC 3,983,287 (cash+current securities) = 51.3%
  Goodwill: UNKNOWN (not in facts.json) -> ROIC ex-goodwill test cannot be run

======== D. Discount rate ======================================================
Ke = 5.277% + 1.0 x 5% = 10.277%
Kd after tax = 5.277% x (1-0.18) = 4.327% (pre-tax Kd UNKNOWN, proxied by US 10y)
Weights (market value): E 98.58%, D 1.42%  ->  WACC = 10.192%; USD floor 8% not binding
Alt: with FRED DGS10 5.22% (orchestrator note, 2026-10-08): WACC 10.136%
TWD-currency WACC: Taiwan 10y UNKNOWN -> TWD floor (local 10y + 4%) UNKNOWN
======== E. DCF scenarios (NT$M; year t = 12 months to 30 Jun of 2026+t; base = TTM to 2Q26) 
D&A calibration k = 688,096 / 1,020,020 = 0.675
3Q26 guide NT$ (US$ x 32): 1,427,200-1,465,600; SBC/rev deducted from EBITDA = 0.0154%

--- BEAR: WACC 10.19%, terminal g 2.0%, terminal ROIC 15%, tax 18%, WC 10% of d-rev ---
    Y1 = 2 x 3Q26 low 1,427,200 + 1H27 (1H26 x0.95)
Yr        g    Revenue EBITDA%   D&A%    OM%  Capex%        FCF   FCF%         PV
1     15.7%  5,138,660   68.0%  15.1%  52.9%   37.0%  1,033,237  20.1%    937,666
2    -10.0%  4,624,794   62.0%  19.2%  42.8%   38.0%    804,197  17.4%    662,307
3      8.0%  4,994,777   63.0%  19.9%  43.1%   34.0%  1,023,632  20.5%    765,049
4      8.0%  5,394,359   63.0%  20.3%  42.7%   32.0%  1,217,100  22.6%    825,506
5      7.0%  5,771,964   63.0%  20.0%  42.9%   30.0%  1,419,947  24.6%    874,006
6      6.0%  6,118,282   63.0%  19.4%  43.5%   29.0%  1,565,067  25.6%    874,226
7      5.0%  6,424,196   63.0%  18.2%  44.7%   28.0%  1,699,547  26.5%    861,534
8      5.0%  6,745,406   63.0%  17.5%  45.5%   27.0%  1,842,433  27.3%    847,578
9      4.0%  7,015,222   63.0%  17.0%  46.0%   26.0%  1,987,215  28.3%    829,624
10     3.0%  7,225,679   63.0%  16.7%  46.3%   26.0%  2,049,502  28.4%    776,485
10-yr rev CAGR 5.0% | avg FCF margin 24.1% (5-yr hist avg 22.1%)
PV explicit 8,253,981 | PV terminal 11,208,593 | TV share 58%
EV 19,462,574 - net debt -2,407,278 = equity 21,869,853
VALUE: NT$843.3/share x 5 / 32.133 = US$131.23/ADS vs US$444.35 -> -70.5%

--- BASE: WACC 10.19%, terminal g 3.0%, terminal ROIC 25%, tax 18%, WC 10% of d-rev ---
    Y1 = 3Q26 mid 1,446,400 + 4Q26 implied 1,481,792 + 1H27 (1H26 x1.25)
Yr        g    Revenue EBITDA%   D&A%    OM%  Capex%        FCF   FCF%         PV
1     33.6%  5,933,797   70.0%  13.1%  56.9%   37.0%  1,200,105  20.2%  1,089,100
2     20.0%  7,120,556   69.0%  13.0%  56.0%   37.0%  1,441,345  20.2%  1,187,039
3     17.0%  8,331,051   68.0%  13.8%  54.1%   35.0%  1,815,056  21.8%  1,356,549
4     14.0%  9,497,398   68.0%  14.9%  53.1%   33.0%  2,299,001  24.2%  1,559,312
5     12.0% 10,637,086   68.0%  15.7%  52.3%   31.0%  2,818,870  26.5%  1,735,072
6     10.0% 11,700,794   68.0%  16.3%  51.6%   30.0%  3,250,584  27.8%  1,815,734
7      8.0% 12,636,858   68.0%  16.5%  51.4%   29.0%  3,662,658  29.0%  1,856,674
8      7.0% 13,521,438   68.0%  16.5%  51.5%   28.0%  4,064,638  30.1%  1,869,863
9      5.0% 14,197,510   68.0%  16.5%  51.5%   27.0%  4,436,188  31.2%  1,852,023
10     4.0% 14,765,410   68.0%  16.5%  51.5%   26.0%  4,774,896  32.3%  1,809,042
10-yr rev CAGR 12.8% | avg FCF margin 26.3% (5-yr hist avg 22.1%)
PV explicit 16,130,408 | PV terminal 29,744,450 | TV share 65%
EV 45,874,857 - net debt -2,407,278 = equity 48,282,136
VALUE: NT$1,861.8/share x 5 / 32.133 = US$289.71/ADS vs US$444.35 -> -34.8%

--- BULL: WACC 10.19%, terminal g 4.0%, terminal ROIC 35%, tax 18%, WC 10% of d-rev ---
    Y1 = 3Q26 high 1,465,600 + 4Q26 1,538,773 + 1H27 (1H26 x1.35)
Yr        g    Revenue EBITDA%   D&A%    OM%  Capex%        FCF   FCF%         PV
1     40.8%  6,250,426   73.0%  12.4%  60.6%   37.0%  1,386,755  22.2%  1,258,485
2     30.0%  8,125,554   72.0%  11.6%  60.4%   38.0%  1,690,638  20.8%  1,392,348
3     25.0% 10,156,943   71.0%  12.1%  58.9%   36.0%  2,273,931  22.4%  1,699,506
4     20.0% 12,188,331   71.0%  13.1%  57.9%   33.0%  3,156,282  25.9%  2,140,768
5     16.0% 14,138,465   71.0%  13.9%  57.1%   30.0%  4,146,917  29.3%  2,552,512
6     13.0% 15,976,465   71.0%  14.6%  56.4%   28.0%  5,062,906  31.7%  2,828,074
7     10.0% 17,574,111   71.0%  15.0%  56.0%   27.0%  5,797,764  33.0%  2,939,002
8      8.0% 18,980,040   71.0%  15.0%  56.0%   26.0%  6,485,737  34.2%  2,983,645
9      6.0% 20,118,843   71.0%  15.0%  56.0%   25.0%  7,111,461  35.3%  2,968,897
10     5.0% 21,124,785   71.0%  15.0%  56.0%   24.0%  7,694,511  36.4%  2,915,183
10-yr rev CAGR 16.9% | avg FCF margin 29.1% (5-yr hist avg 22.1%)
PV explicit 23,678,421 | PV terminal 54,693,486 | TV share 70%
EV 78,371,907 - net debt -2,407,278 = equity 80,779,185
VALUE: NT$3,115.0/share x 5 / 32.133 = US$484.70/ADS vs US$444.35 -> +9.1%

BASE Y10 consistency: reinvestment 1,454,890 = 23.4% of NOPAT; implied incremental ROIC = g 4% / 23.4% = 17.1%; terminal uses g 3% / ROIC 25% = 12.0% reinvestment -> terminal FCF margin 37.1% vs Y10 32.3%

Summary (US$/ADS): BEAR 131.23 | BASE 289.71 | BULL 484.70
Conventions NOT applied (all would raise value): roll-forward 30 Jun->13 Oct x1.028; mid-year discounting ~x1.050 on explicit+TV; govt capex grants (FY25 NT$76,259M) excluded; non-current financial assets (FY25 134,337) excluded
```

## F. Reverse DCF & sensitivity grid

- **Reverse DCF:** at base margins, capex path, WACC 10.19%, g 3% and terminal ROIC 25%, **US$444.35 implies a 10-yr revenue CAGR of 18.6–19.4%**. The 18.6% figure re-derives D&A from capex at each trial; `reverse_dcf()` with a fixed D&A path gives 19.4%. That means year-10 revenue of about NT$24.5T, **5.5x TTM (about US$762B)**, sustained at a 68% EBITDA margin. For comparison, the FY21–25 history was 24.5%, and my base case is 12.8%. Including one down-year, the history *has* run above the implied rate. It has never done so for 10 years, from a US$138B base, at these margins.
- At WACC 9.19% the implied CAGR is 16.2%; at 11.19% it is 20.9%.
- **Implied IRR** on the base-case cash flows at today's price is **7.93%**, below the 10.19% WACC and just below the 8% USD floor. Base at WACC 8% = US$437.58; at 9% = US$356.29.

```
======== F. Reverse DCF and sensitivity (BASE) =================================
reverse_dcf() (BASE margins/capex%, BASE D&A% path fixed): implied 10-yr revenue CAGR 19.4%
Same with D&A re-derived from capex at each trial growth:            18.6%
  -> Year-10 revenue NT$24,488,402M = 5.5x TTM (~US$762B at 32.133)
  Compare: hist FY21-25 CAGR 24.5%; BASE path CAGR 12.8%
  implied CAGR at WACC 9.19%: 16.2%
  implied CAGR at WACC 11.19%: 20.9%
  implied CAGR at BEAR-like EBITDA (x0.93): 20.0%
Implied IRR (discount rate that equates BASE cash flows to price): 7.93% vs WACC 10.19%
BASE at WACC 8%: US$437.58/ADS | BULL at WACC 8%: US$796.87/ADS
BASE at WACC 9%: US$356.29/ADS | BULL at WACC 9%: US$619.72/ADS
BASE with roll-forward x1.028 and mid-year x1.050 applied: US$312.72/ADS (upper bound; ignores dividends paid since 30 Jun)

BASE sensitivity: US$/ADS, WACC (rows) x terminal growth (cols), ROIC_t 25%
             2.0%     3.0%     4.0%
   9.19%   319.08   343.75   377.68
  10.19%   273.45   289.71   311.03
  11.19%   238.28   249.35   263.35
  12.19%   210.43   218.16   227.67  (+2pp ~ Taiwan risk premium)
(sensitivity() cross-check, centre cell US$289.71)

BASE sensitivity: US$/ADS, WACC x terminal ROIC (g 3%)
              15%      20%      25%      35%      45%
   9.19%   323.10   336.01   343.75   352.60   357.51
  10.19%   273.48   283.62   289.71   296.66   300.52
  11.19%   236.33   244.47   249.35   254.92   258.02

======== C. Multiples (current) ================================================
EV/EBITDA TTM = 71,646,742 / 3,180,044 = 22.5x  (EV incl NCI)
P/E trailing 33.4x | normalised 34.3x | mid-cycle 40.6x | fwd (vendor) 19.9x
P/FCF = 74,054,021 / 1,134,150 = 65.3x | SBC-adj 65.3x
FCF yield 1.53% | SBC-adj 1.53% | OE yield TTM norm 1.82% | FY25 1.49%
PEG 1.14 (gate ok, historical NI CAGR only) | Lynch ratio 0.90 | ROIC TTM 46.8% vs WACC 10.19%
Peer median P/E (dossier §7, yfinance, unvalidated): trailing 37.8x, forward 19.4x

======== G. Load-bearing inputs: BASE US$/ADS at -10% / +10% of each input =====
BASE = US$289.71/ADS
  WACC 10.19%                        -10%:   344.97 (+19.1%)   +10%:   248.67 (-14.2%)
  EBITDA margin path (x0.9/x1.1)     -10%:   245.58 (-15.2%)   +10%:   333.84 (+15.2%)
  USDTWD 32.133                      -10%:   321.90 (+11.1%)   +10%:   263.37 ( -9.1%)
  Revenue growth rates (all yrs)     -10%:   262.93 ( -9.2%)   +10%:   319.10 (+10.1%)
  Capex % of revenue path            -10%:   306.11 ( +5.7%)   +10%:   273.31 ( -5.7%)
  Tax rate 18%                       -10%:   297.12 ( +2.6%)   +10%:   282.30 ( -2.6%)
  Terminal growth 3%                 -10%:   284.39 ( -1.8%)   +10%:   295.47 ( +2.0%)
  D&A calibration k 0.675            -10%:   294.43 ( +1.6%)   +10%:   284.99 ( -1.6%)
  Terminal ROIC 25%                  -10%:   287.00 ( -0.9%)   +10%:   291.92 ( +0.8%)
  Net cash (NT$2.41T incl NCI)       -10%:   288.26 ( -0.5%)   +10%:   291.15 ( +0.5%)
  Working capital 10% of d-rev       -10%:   290.11 ( +0.1%)   +10%:   289.31 ( -0.1%)

======== Data-layer warnings (fundamentals.json) ===============================
 - cash-flow net income 2,041,654,700,000 differs from income-statement 1,697,604,000,000 by +20% (IFRS pre-tax start?) - income statement used
 errors: []

======== Derived figures cited in 02_quant.md ==================================
Vendor fwd P/E implies EPS US$22.32/ADS = NT$143.4/share = +72% vs normalised TTM 83.25
Net cash per ADS = NT$94.4 x 5 / 32.133 = US$14.70
BASE capex Y1-3 = 7,745,979 vs FY23-25 actual 3,178,234 (2.4x)
Inventory FY25 / revenue FY25 = 288,109.5 / 3,809,054 = 7.6%; AR 29 days / 365 = 7.9%
FY24-25 average ROIC = 39.3%
TTM revenue in US$ = 4,440,492 / 32.133 = US$138.2B
BASE with steady-state EBITDA 71.6% (path scaled x1.053): US$313.17/ADS (+23.46)
BASE with steady-state EBITDA 74.2% (path scaled x1.092): US$330.21/ADS (+40.50)
WACC +/-1pp effect on BASE (g 3%): +54.04 / -40.36
```

## G. Load-bearing inputs

Base = US$289.71/ADS. Each input is moved ±10% while all else is held at base (02_model.py §G).

| # | Input (base value) | Source | −10% | +10% |
|---|---|---|---|---|
| 1 | WACC 10.19% | rf facts: us10y_pct 5.277%; ERP 5% and beta 1.0 assumed | US$344.97 (+19.1%) | US$248.67 (−14.2%) |
| 2 | EBITDA margin path (70 → 68%) | facts: FY23–25 EBITDA 67.2 / 68.6 / 68.9%; TTM 71.6% | US$245.58 (−15.2%) | US$333.84 (+15.2%) |
| 3 | USDTWD 32.133 (per-ADS conversion) | facts: market.usdtwd | US$321.90 (+11.1%) | US$263.37 (−9.1%) |
| 4 | Revenue growth path (Y1 33.6%, 12.8% CAGR) | dossier §3 guide (FY26 +40%, 3Q26); 2027+ is ASSUMPTION | US$262.93 (−9.2%) | US$319.10 (+10.1%) |
| 5 | Capex % revenue (37 → 26%) | facts: guidance FY26 US$60–64B; history 33–53% | US$306.11 (+5.7%) | US$273.31 (−5.7%) |
| 6 | Tax rate 18% | dossier §2 (2Q26 18.0%, FY25 17.0%) | US$297.12 (+2.6%) | US$282.30 (−2.6%) |
| 7 | Terminal growth 3% | ASSUMPTION, cap min(4%, 5.277%) | US$284.39 (−1.8%) | US$295.47 (+2.0%) |
| 8 | D&A calibration k 0.675 | facts: FY25 D&A / avg FY21–25 capex | US$294.43 (+1.6%) | US$284.99 (−1.6%) |
| 9 | Terminal ROIC 25% | ASSUMPTION (TTM ROIC 46.8%) | US$287.00 (−0.9%) | US$291.92 (+0.8%) |
| 10 | Net cash NT$2.41T (incl. NCI) | facts: balance_sheet_latest | US$288.26 (−0.5%) | US$291.15 (+0.5%) |
| 11 | Working capital 10% of Δrevenue | ASSUMPTION (payables UNKNOWN) | US$290.11 (+0.1%) | US$289.31 (−0.1%) |

Note on #2: ±10% of a 68% margin is ±6.8 pts, which is roughly the gap between the base (68%) and the TTM (71.6%) or 1H26 (74.2%) margin. Year-1 growth is inside #4. The 2027 growth assumption (1H27 +25%) is the single least-sourced number in the base case.

## H. Open questions for the Skeptic

1. **Discount rate is the biggest lever.** A USD CAPM rate (10.19%) applied to NT$ cash flows, with no Taiwan risk premium and an unsourced beta of 1.0. The Taiwan 10y is UNKNOWN. A 1 pp move shifts base value by about US$40–55. The price implies a 7.93% IRR on my base cash flows.
2. **Growth after FY26 is unsourced.** Management gave no AI CAGR and no 3-year capex figure (dossier §4), and consensus is UNKNOWN. Base 1H27 is +25%, Y2 +20%. Is the 12.8% 10-yr CAGR too low for a business that just compounded 24.5%, or too high given the FY23 precedent and rising concentration?
3. **Mid-cycle margin.** The base uses 68% EBITDA (the FY23–25 average) against 71.6% TTM and 74.2% 1H26. If the AI mix has structurally lifted margins, the base is too conservative by about US$23–41 (US$313.17 at a 71.6% steady-state EBITDA margin; US$330.21 at 74.2%; 02_model.py derived figures). If the 2H26 N2 and overseas dilution (up to 3–4 + 3–4 pts GM) is larger than the guide, the bear margin path becomes relevant.
4. **Terminal inconsistency (small but real).** Base Y10 reinvestment is 23.4% of NOPAT, an implied incremental ROIC of 17.1%. The terminal uses g 3% / ROIC 25% (12% reinvestment), so FCF margin steps up from 32.3% to 37.1% at the terminal. The value effect is under 1% (terminal ROIC row in the grid), but the Skeptic may prefer a 15–20% terminal ROIC.
5. **D&A rule** is calibrated on one data point (FY25). It drives the OM path (base Y1 OM 56.9% vs the 3Q26 guide of 56–58%, which is consistent), but is otherwise untested.
6. **The PEG passed the gate only on a vendor forward P/E** (19.9x, unvalidated, implying about +72% EPS). If that figure is wrong (for example, a different FX or EPS basis), the gate outcome is unchanged (forward < trailing still likely), but the PEG should carry little weight either way.
7. **Units and FX.** FY26 assumes NT$ growth = USD growth, though the dossier notes a 2Q26 gap of 36.0% NT$ vs 33.7% USD. The per-ADS value scales 1:1 inversely with USDTWD. For a SGD-base holder, USD/SGD adds a further leg that is not modelled here.
8. **Conservative conventions.** No roll-forward or mid-year convention (together about +7.9%), grants excluded, non-current financial assets excluded. Should any of these be applied?
9. **UNKNOWNs that could matter:** goodwill (ROIC ex-goodwill), debt maturity ladder, inventory and receivables growth series (inventory days +7 in 2Q26), market share, consensus, Taiwan 10y, peer EV multiples on a consistent currency basis, and the 3Q26 actuals (due mid-October, date UNKNOWN). The 3Q26 print will land within days and directly tests Y1.
10. **Tail risk is not in any scenario.** A cross-strait disruption would make the bear case (US$131) look optimistic. The only floor-like figure I can compute is net cash of NT$94.4/share = US$14.70/ADS (94.4 × 5 / 32.133). I have not modelled the overseas fabs as a stand-alone value.
