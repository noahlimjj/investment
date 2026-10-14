<!-- pipeline:value-quant -->
# Quant model: 000660.KS (as of 2026-10-13)

SK hynix Inc., KRX common share. **Price KRW 1,443,000** (KRX close 2026-10-13). Template **FULL**, Lynch **Cyclical**. Current holding (Singapore resident, SGD base).
Model: `reports/runs/000660.KS_2026-10-13/02_model.py` (sha1 c5eb807f4494, executed 2026-10-14, exit 0). Every number below is either quoted from a source with an inline citation or printed by that run. Output blocks are pasted verbatim.
Units: KRW millions in the code, KRW T (trillion) in the text. **Per-share values are KRW per common share on 728,866,596 shares outstanding** (facts: derived.shares_outstanding = 730,492,365 issued − 1,625,769 treasury, post-ADS, before any of the Aug–Nov 2026 buyback). One SKHY ADS = 1/10 share; the ADS line (≈45% premium, dossier §1) is not valued here.
No scenario probabilities and no verdict (Skeptic's job).

**Provenance.** The previous `02_quant.md` in this RUN_DIR was overwritten by an outside agent while this stage was paused. The orchestrator moved it to `_external_unverified/`, and nothing in it was read or used. This file is rebuilt only from my own `02_model.py`, re-read and re-run. Integrity check on inputs: `01_research.md` grew by exactly 35 bytes between my first read and the resume, which equals the added first line `<!-- pipeline:value-researcher -->`. Every dossier figure the model uses was re-checked as present.

**Tape check (RULE 0).** Price 1,443,000 sits at a 6.28x reported trailing P/E (10.61x on operating earnings), +247.7% over 12 months but −50.6% from the 52-week high (2,919,000, 2026-06-22) and −21.6% in six sessions (dossier §1). A 3x forward P/E (CONSENSUS) together with a halving from the high means the market already expects earnings to mean-revert. The question for the model is how far, and for how long the peak lasts.

## A. Lynch classification & category checks

**Category: Cyclical. It is not changing, but the HBM era may have lifted the mid-cycle margin.** Revenue went +3.8% (FY22), −26.6% (FY23), +102.0% (FY24), +46.8% (FY25), then TTM +94.7% vs FY25. EBIT went 12.4T → 7.0T → −7.7T → 23.5T → 47.2T → 128.7T TTM. The 5-yr CAGR is UNKNOWN because FY2020 is not in facts.json. The 4-yr FY21→FY25 CAGR is 22.6% for revenue and 45.4% for net income (FY2021 EPS UNKNOWN). The growth rate alone would read "Fast Grower". But there was a loss year three years ago (FY2023 EBIT margin −23.6%, ROIC −7.7%), and gross margin has run from −1.6% to 83.2% (Q2-26), which is the definition of a cyclical.

*Is the category changing?* Evidence for a structural shift: at the same position against trend (factor ~1.03), EBIT margin was 35.5% in FY2024 vs 15.7% in FY2022 (+19.8pp). HBM share is #1 at 56.4% (IDC Q1-26 via 424B4, one data point), and there are LTAs with about 10 customers (dossier §3, §8). Evidence against: the 2026 surge is price-led. In Q2, DRAM ASP rose by a mid-30% and NAND ASP by a mid-50% QoQ while DRAM bits "increased slightly" (dossier §3). The Q2-26 run-rate is 3.37x the fitted revenue trend. The tape is −50.6% from the high. So I keep Cyclical and capture the HBM shift as the bull's higher mid-cycle margin (42.0%), not as a re-categorisation.

**Where are we in the cycle? At or near the peak.**
- TTM EBIT margin is 68.0% and Q2-26 is 76.3%, both **above the top of the FY21–25 range (−23.6% to 48.6%)**.
- Cycle factor (revenue ÷ log-linear trend FY21–25): the Q2-26 run-rate is 3.37x and TTM is 2.17x, against 0.62–1.23 over FY21–25.
- Late-cycle supply signals (dossier §3, §5, §8): 100% utilisation. 2026 capex is guided to "high KRW 40 trillion" against 28.6T in FY2025. The board has committed Y2 KRW 35.2T, M17 19.1T and P&T7 7.1T. M15X has been pulled forward and the Yongin phase-1 cleanroom opens early 2027. CXMT raised CNY 57.92B [SNIPPET].
- Counter-signals: management says supply will stay "tight ... for a considerable period", there are 3–5 year LTAs with deposits [WF], and inventory is not building (DIO 126 → 123 days).
- Lynch's warning applies: the reported P/E is 6.28x, but **P/E on mid-cycle EPS is 48.7x**. A low P/E at peak margins is a warning, not a bargain, so the valuation below runs on mid-cycle economics.

**Lynch metrics (formulas shown in the output):**

| Metric | Formula | Value | Read |
|---|---|---|---|
| PEG | P/E ÷ growth; growth = lower of hist. NI CAGR 45.4% and CONSENSUS FY26→27 EPS 32.4% | 0.19 (reported P/E), 0.33 (operating P/E). The gate returns valid: growth ≥ 5% and forward 3.07x < trailing 6.28x | Built on peak-cycle EPS, so it does not drive anything for a cyclical |
| Lynch ratio | (EPS growth % + yield %) ÷ P/E | 5.19 reported, 3.07 operating, **0.21 on mid-cycle P/E** with 10% trend growth | Peak earnings make it look attractive; on mid-cycle it is poor (<1) |
| Net-cash-adj. P/E | (price − net cash/sh) ÷ EPS | 5.87x (company net cash 95,177/sh, reported EPS); 9.24x (full bridge 186,960/sh, operating EPS 136,008) | |
| Mid-cycle P/E | price ÷ (trend revenue 96.6T × 29.0% × (1−t) ÷ shares) | 48.7x (mid-cycle EPS KRW 29,636) | The figure that matters for a cyclical |
| Inventory vs sales | growth of inventories vs revenue | FY25 +7.3% vs +46.8%; H1-26 +25.9% vs run-rate +177.0%; DIO 126 → 123 d | No red flag |
| Receivables vs sales | growth of receivables vs revenue | H1-26 +162.8% vs TTM revenue +94.7% (**flag on a TTM basis**); vs run-rate +177.0% it is in line, and DSO went 58 → 55 d | Explained by the ramp so far. Recheck at Q3 (47.8T at 6/30) |
| Debt | net debt ÷ owner earnings; maturity wall | Net cash. Borrowings 18.6T (5.9T current) vs cash+ST 88.0T. Maturity ladder UNKNOWN, interest expense UNKNOWN | Survival is not a question |

Data layer (RULE 1): `fundamentals.json` shows **warnings: none, errors: none** for 000660.KS. It is, however, stale for this cycle (FY2025 base). Its 711.1M share count is pre-ADS, and its `roe` 0.927 cannot be reproduced from filings (FY2025 NI/equity = 0.356), so it is not used. `trailing_pe` is null, so it is not treated as zero.

```
====== 0. Price, shares, market cap, data-layer status =====================================
Price KRW 1,443,000 | shares 728.866596M | mcap 1,051.8T (facts 1,051.8T) | US$784.0B
KRW/USD 1,341.58 | KRW/SGD 1,048.08 | price = S$1,377/share
Vendor shares (fund) 711.1M vs 728.9M used (dossier §10.2: vendor count is pre-ADS)
fundamentals.json warnings: none | errors: none
Tax rate used 23.0% (H1-26 effective, dossier §2) | stub 0.2877 yr
12m price change 247.7% | 52w high 2,919,000 -> price is -50.6% vs high
====== A1. History (KRW T) and margins =====================================================
             Rev      GM  EBIT m    NI m   D&A%  Capex%   FCF m EBITDA m Capex/DA
FY2021      43.0    UNKN   28.9%   22.4%   UNKN   29.0%   17.0%     UNKN     UNKN [SNIPPET capex/FCF]
FY2022      44.6   35.0%   15.7%    5.5%   UNKN   42.6%   -9.5%     UNKN     UNKN [SNIPPET capex/FCF]
FY2023      32.8   -1.6%  -23.6%  -27.9%  40.5%   26.8%  -13.7%    16.9%     0.66
FY2024      66.2   48.1%   35.5%   29.9%  19.0%   25.2%   19.8%    54.5%     1.32
FY2025      97.1   60.4%   48.6%   44.2%  14.3%   29.4%   25.5%    62.9%     2.05
TTM6/26    189.2   76.3%   68.0%   85.7%   7.9%   19.3%   47.8%    75.9%     2.45
Q2-26       79.3   83.2%   76.3%  118.4%   (quarter; x4 run-rate revenue 317.3T)

EBIT margin FY21-25: min -23.6% (FY2023), max 48.6% (FY2025), simple avg 21.0%, revenue-weighted 29.0%
TTM EBIT margin 68.0% and Q2-26 76.3% are ABOVE the 5-yr max -> peak/near-peak of the cycle
GM range FY22-TTM: -1.6% .. 83.2% (Q2-26)
FCF margin FY21-25 (FY21-22 [SNIPPET]): simple 7.8%, rev-wtd 12.9% | FY23-25 primary only: simple 10.5%, rev-wtd 17.0% | TTM 47.8%
Capex/revenue FY23-25 rev-wtd 27.5%
====== A2. Growth and Lynch category =======================================================
5-yr CAGR: UNKNOWN (FY2020 not in facts.json). 4-yr FY2021->FY2025 used instead:
  revenue CAGR 22.6% | net income CAGR 45.4% (FY2021 EPS UNKNOWN -> NI used)
  FY2022: revenue +3.8%, EBIT 12.4T -> 7.0T
  FY2023: revenue -26.6%, EBIT 7.0T -> -7.7T
  FY2024: revenue +102.0%, EBIT -7.7T -> 23.5T
  FY2025: revenue +46.8%, EBIT 23.5T -> 47.2T
  TTM vs FY2025 revenue +94.7%; H1-26 vs H1-25 +230.8%

Log-linear trend FY2021-25: fitted growth 22.4%/yr; fitted FY2025 level 78.9T
period     revenue   trend  factor  EBIT m
FY2021        43.0    35.1    1.22   28.9%
FY2022        44.6    43.0    1.04   15.7%
FY2023        32.8    52.6    0.62  -23.6%
FY2024        66.2    64.5    1.03   35.5%
FY2025        97.1    78.9    1.23   48.6%
TTM6/26      189.2    87.3    2.17   68.0%
Q2-26 RR     317.3    94.2    3.37   76.3%
On-trend margins (factor ~1.03): FY2022 15.7% (pre-HBM) vs FY2024 35.5% (HBM era): +19.8pp; at factor ~1.23: FY2021 28.9% vs FY2025 48.6%
====== A3. Lynch metrics (each with formula) ===============================================
Trailing P/E (reported) = price / TTM basic EPS = 1,443,000 / 229,700 = 6.28x (TTM NI includes H1-26 finance income 82.9T)
Trailing P/E (operating) = mcap / (TTM EBIT x (1-t)) = 1,051.8T / 99.1T = 10.61x
Forward P/E = price / CONSENSUS FY2027 EPS 470,324 = 3.07x (fund forward_pe 3.07x)
PEG growth = lower of historical NI CAGR 45.4% and CONSENSUS FY26->FY27 EPS 32.4% = 32.4%; peg_is_valid -> True (ok)
  PEG = 6.28 / 32.4 = 0.19 (reported P/E); 0.33 (operating P/E). Peak-cycle EPS -> not a verdict driver for a cyclical.
Dividend yield = 3,000 / 1,443,000 = 0.21% (fixed KRW 1,500/yr policy 2025-27 -> 0.10%)
Lynch ratio = (EPS growth % + yield %) / P/E = (32.4 + 0.21) / 6.28 = 5.19 (reported) | / 10.61 = 3.07 (operating)
Mid-cycle EPS = trend revenue 96.6T x mid-cycle EBIT 29.0% x (1-t) / 728.9M = KRW 29,636 -> mid-cycle P/E 48.7x
Lynch ratio on mid-cycle P/E with base trend growth 10% (Y4 fade target) = (10 + 0.21) / 48.7 = 0.21
====== A4. EV bridge / net cash (KRW M) -- IFRS 16: leases IN net debt, FCF pre-lease ======
  + cash, ST fin. instr., ST investment assets        87,957,923
  - borrowings                                       -18,586,634
  - lease liabilities (IFRS 16)                       -2,526,505
  - current tax liabilities (unpaid)                 -31,958,025
  + ADS net proceeds US$26.2B at spot                 35,149,395
  + LT investment assets x (1-30%)                    59,716,667
  + LT financial instruments                           7,101,803
  - non-controlling interest                            -312,618
  - Q2 dividend declared (ex 8/28)                      -273,325
  = non-operating net assets (NET_CASH for DCF)      136,268,681  = KRW 186,960/share
Company net cash (cash+ST - borrowings) 69,371,289 = KRW 95,177/share
Operating EV implied by price = mcap - bridge = 915.5T (facts simple EV 984.9T)
Net-cash-adjusted P/E = (price - net cash/sh) / EPS: company net cash -> (1,443,000 - 95,177) / 229,700 = 5.87x | full bridge on operating EPS 136,008 -> 9.24x
====== A5. Inventory / receivables vs sales; debt ==========================================
FY2023->FY2024: inventories -1.2%, receivables +97.3%, revenue +102.0%
FY2024->FY2025: inventories +7.3%, receivables +39.8%, revenue +46.8%
12/31/25->6/30/26: inventories +25.9%, receivables +162.8%; revenue run-rate H2-25 ann. 114.6T -> Q2-26 ann. 317.3T = +177.0%; TTM vs FY2025 +94.7%
DSO: 12/31/25 on H2-25 run-rate 58 d -> 6/30/26 on Q2 run-rate 55 d | DIO: 126 d -> 123 d
Debt 6/30/26: borrowings 18.6T (current 5.9T) + leases 2.5T vs cash+ST 88.0T; maturity ladder 2027-31 UNKNOWN; interest expense UNKNOWN
```

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence / predictability: No.** I cannot sketch revenue and margins 10 years out with reasonable confidence. Revenue moved −26.6% and then +102.0% in consecutive years. EBIT margin went from −23.6% (FY2023) to 76.3% (Q2-26) in about ten quarters. HBM revenue, HBM ASP and 2027 HBM pricing are UNKNOWN; the CFO declined to give a direction (dossier §4). The swing variable, DRAM/HBM price, is set by the capacity decisions of three or four suppliers plus a state-funded Chinese entrant. What *is* predictable is capacity (board-approved fabs with dated windows) and customer concentration. This belongs in the "too hard" pile for any point estimate, which is why section E is a wide scenario range and section F frames the price as "what must be true".

**Moat, from evidence only. Rating: None (on the through-cycle evidence test); trend: widening in the upcycle, unproven through a downturn.**
- *Pricing power (gross margin):* FY2022 35.0% (fund), FY2023 −1.6%, FY2024 48.1%, FY2025 60.4%, TTM 76.3%, Q2-26 83.2%. That is a range of about 85pp, with no through-cycle pricing power.
- *ROIC level and consistency:* FY2023 −7.7%, FY2024 21.2%, FY2025 32.9%, TTM 50.6% (95.8% excluding the 85.3T + 7.1T of non-operating LT investments). The FY23–25 average is 15.5%, against a WACC of 13.83%. Only three years of primary balance-sheet data exist (FY2021–22 UNKNOWN).
- *Capital intensity:* capex/revenue was 26.8% / 25.2% / 29.4% in FY23–25 (revenue-weighted 27.5%), and capex/D&A went 0.66 (FY23) → 2.45 (TTM). Staying in the game takes about a quarter of revenue in capex every year.
- *Market share:* HBM #1 at 56.4%, DRAM #2 at 29.1%, NAND #2 at 18.5% (IDC Q1-26). That is one data point, so the share trend is UNKNOWN. Samsung began HBM4 supply in February 2026 [WF].
- *Why "None" and not "Narrow":* a business with a durable moat does not post a −23.6% EBIT margin and −7.7% ROIC three years before a record. What the evidence shows is a technology and scale lead in HBM. It is contested, and it has not been tested through a downturn. The +19.8pp on-trend margin uplift is the best evidence of something structural, but it rests on two pairs of years. If HBM LTAs keep EBIT margins above ~25% through the next downturn, upgrade to Narrow.

**Owner earnings (NI + D&A − capex):**
- FY2025: 28.3T, a 2.7% yield on market cap (matches fund `owner_earnings`).
- TTM reported: 140.5T (13.4%). This is inflated by H1-26 finance income of 82.9T (a 63.2T fair-value gain plus 14.0T of dividends, Kioxia-linked per the press, dossier §2).
- **TTM adjusted (NI replaced by EBIT × (1−t)): 77.5T, a 7.4% yield.**
- SBC-adjusted: SBC is already expensed in NI and EBIT. The TTM add-back is 0.3T, 0.15% of revenue. So SBC-adjusted OE equals OE, and SBC-adjusted FCF is 90.1T.
- TTM FCF of 90.4T falls to **51.5T adjusted**, after removing 14.0T of dividends received and the 24.9T build in unpaid current tax.

**ROIC vs WACC:** TTM ROIC is 50.6%, a peak figure, against WACC 13.83%. **Through-cycle (FY23–25 average) ROIC is 15.5% against 13.83%**, only just above the cost of capital. Goodwill is UNKNOWN (not in the dossier; the Intel NAND deal implies some), so the ex-goodwill test (goodwill > 30% of IC) cannot be run. The thesis turns on the through-cycle figure, and that is why base terminal ROIC is set at 15%.

```
====== B1. ROIC = NOPAT / (equity + debt incl. leases - cash&ST), period-end, tax 23.0% ====
FY2023   NOPAT    -6.0T / IC    77.1T = -7.7%
FY2024   NOPAT    18.1T / IC    85.2T = 21.2%
FY2025   NOPAT    36.4T / IC   110.5T = 32.9%
TTM6/26  NOPAT    99.1T / IC   195.8T = 50.6%
TTM ex non-operating LT investments (IC 103.4T): 95.8%
Through-cycle ROIC FY2023-25 simple avg 15.5% | goodwill UNKNOWN -> ex-goodwill test not possible
(fund: roe 0.927 is not reproducible from filings: FY2025 NI/equity = 0.356; not used)
====== B2. Owner earnings = NI + D&A - capex (AGENTS.md) ===================================
FY2025: 42.9T + 13.9T - 28.6T = 28.3T (fund owner_earnings 28.3T) -> yield 2.7%
TTM reported: 162.1T + 14.9T - 36.5T = 140.5T -> yield 13.4% (inflated by non-operating gains)
TTM adjusted (NI -> EBIT x (1-t)): 99.1T + 14.9T - 36.5T = 77.5T -> yield 7.4%
SBC: already expensed in NI/EBIT (CF add-back TTM 0.3T = 0.15% of revenue); SBC-adjusted OE = OE (no add-back to remove). SBC-adj. FCF = FCF - SBC = 90.1T
TTM FCF 90.4T; less dividends received in OCF 14.0T and current-tax build 24.9T = adjusted 51.5T
```

## C. GARP & valuation matrix

| Multiple | Current | 5-yr own average | Peer median (dossier §7, vendor, unsynchronised) |
|---|---|---|---|
| EV/EBITDA (TTM) | 6.38x (operating EV 915.5T) / 6.86x (facts simple EV 984.9T) | UNKNOWN | 10.55x (n=5); hynix vendor 6.68x |
| EV/EBIT | 3.78x on Q2×4 run-rate; **32.6x on mid-cycle EBIT** (trend × 29.0%) | UNKNOWN | UNKNOWN |
| P/E trailing | 6.28x reported; 10.61x operating | UNKNOWN | 18.2x (n=4) |
| P/E forward | 3.07x (CONSENSUS FY2027 EPS 470,324) | UNKNOWN | 4.31x (n=4) |
| P/E mid-cycle | **48.7x** | UNKNOWN | n/a |
| P/FCF | 11.6x TTM; 20.4x on adjusted FCF 51.5T | UNKNOWN | UNKNOWN |
| SBC-adj. P/FCF | 11.7x | UNKNOWN | UNKNOWN |
| FCF yield | 8.6% TTM; 4.9% adjusted; 2.4% FY2025 | UNKNOWN | 1.4% (n=5, latest-FY FCF) |
| Owner-earnings yield | 7.4% TTM adjusted; 13.4% TTM reported; 2.7% FY2025 | UNKNOWN | UNKNOWN |
| PEG | 0.19 / 0.33 (gate valid, peak EPS, not a driver) | UNKNOWN | UNKNOWN |
| Lynch ratio | 5.19 / 3.07 / 0.21 (mid-cycle) | UNKNOWN | UNKNOWN |

The 5-yr own averages are UNKNOWN because the dossier has no historical price series (only the 12-month-ago and 52-week points). Peer trailing figures from the vendor mix fiscal periods (dossier §7), so the peer column is only a rough cross-section. Consensus (Yahoo via yfinance, dossier §9) enters only the forward P/E and PEG lines above, both labelled. It does not touch the DCF. Dossier §9 notes the vendor's period estimates are internally inconsistent by about 12%.

```
====== C. Multiples matrix (current; 5-yr own avg UNKNOWN: no historical prices in dossier; peers = dossier §7) ====
EV/EBITDA TTM: operating EV 915.5T / 143.6T = 6.38x | facts simple EV 984.9T -> 6.86x
EV/EBIT run-rate (Q2 x4 242.2T): 3.78x | EV/EBIT mid-cycle (28.0T = trend x 29.0%): 32.6x
P/E trailing reported 6.28x | operating 10.61x | forward (CONSENSUS FY27) 3.07x | mid-cycle 48.7x
P/FCF TTM 11.6x | SBC-adj 11.7x | adjusted FCF 51.5T -> 20.4x
FCF yield TTM 8.6% | SBC-adj 8.6% | adjusted 4.9% | FY2025 2.4%
Owner-earnings yield: TTM adjusted 7.4% | TTM reported 13.4% | FY2025 2.7%
Peer median EV/EBITDA (vendor): 10.550 (n=5) | SK hynix vendor: 6.68
Peer median Trailing P/E (vendor): 18.200 (n=4) | SK hynix vendor: null
Peer median Forward P/E (vendor): 4.310 (n=4) | SK hynix vendor: 3.07
Peer median FCF yield (vendor): 0.014 (n=5) | SK hynix vendor: 2.4% (FY2025 FCF)
```

## D. Discount rate build

| Component | Value | Source |
|---|---|---|
| Risk-free (KRW 10y) | 4.369% | inputs: KTB 10y close 2026-10-06 (orchestrator-updated) |
| ERP | 5.0% | inputs |
| Beta | raw 2.391 → **Blume 1.932** (0.67 × 2.391 + 0.33) | fund: beta (vendor; benchmark and window UNKNOWN) |
| Cost of equity | 14.03% | CAPM |
| Pre-tax cost of debt | 5.37% = rf + 1% (**ASSUMPTION**: interest expense not in dossier) → 4.14% after tax | immaterial at 1.97% debt weight (rf + 3% → WACC 13.86%) |
| Weights | E 1,051.8T (market), D 21.1T (book, used as a proxy for market value) | facts |
| **WACC** | **13.83%** | floor = KRW 10y + 4% = 8.37%, **not binding** |

Staleness check: on the older OECD August monthly rf (4.286%), WACC is 13.75% and base value is 730,745 (+0.4%), which is immaterial. **The beta is the lever.** At beta 1.0, WACC is 9.27% and base value is 1,003,655 (+37.9%). On the raw unadjusted 2.391, WACC is 16.08%. I use the rule-mandated Blume-adjusted vendor beta, and flag in H that, combined with an explicitly modelled downturn, it may count cyclical risk twice.

```
====== D. Discount rate (CAPM + after-tax debt, market-value weights) ======================
rf 4.369% (inputs: KRW KTB 10y 2026-10-06) | ERP 5.0% | raw beta 2.391 (fund) -> Blume 0.67x2.391+0.33 = 1.932
Ke = 4.369% + 1.932 x 5.0% = 14.03% | Kd pre-tax 5.37% (ASSUMPTION rf+1%) after-tax 4.14%
Weights: E 1,051.8T, D 21.1T -> D/(D+E) 1.97%
WACC = 13.83% | floor (KRW 10y + 4%) 8.37% -> floor binding: False
  WACC if rf = OECD Aug monthly 4.286%   13.75%
  WACC if beta = 1.0 (no vendor beta)    9.27%
  WACC if raw beta 2.391 (no Blume)      16.08%
  WACC if Kd = rf + 3%                   13.86%
```

## E. DCF scenarios

**Structure.** The DCF is FCFF via `valuation.dcf()`, 10 years, Y1 = Jul-2026 to Jun-2027. It uses `mid_year=True` and `stub_years=0.2877` (2026-06-30 balance sheet → 2026-10-13 price date). The revenue base is the Q2-26 annualised run-rate of 317.3T. The 6/30 receivables, inventory and net cash are already sized to that run-rate, so starting from TTM would double-count a working-capital build. Revenue = cycle factor × trend, where trend is the log-linear FY21–25 fit (22.4%/yr; FY2025 trend level 78.9T). Y1 is set in absolute terms. Y2 and Y3 carry cycle factors, and from Y4 revenue sits on trend (factor 1.0) at the **mid-cycle EBIT margin**, which also drives the terminal value. Capex in Y1–Y4 is absolute (guidance and board commitments). From Y5, capex = D&A + (g ÷ ROIC) × trend-NOPAT − ΔWC, so growth is never free and the explicit period is consistent with the terminal ROIC. D&A follows D&A_t = D&A_{t−1} + (capex_{t−1} − D&A_{t−1}) ÷ 6, which is calibrated to FY24 (−0.4%) and FY25 (−4.8%). WC is 15% of Δrevenue (gross inventories plus receivables; payables UNKNOWN). Tax is 23.0% (H1-26 effective, dossier §2). WACC is 13.83% in all scenarios, so scenarios differ only in business outcomes.

**Stated method choices.**
- *IFRS 16:* leases (2.5T) are kept **in** net debt, and FCF is pre-lease (OCF − capex, lease principal not deducted).
- *SBC:* margins are reported EBIT with SBC expensed, and `dcf()` adds nothing back, so SBC is treated as a cost. The share count is **not** grown (one method, never both).
- *Acquired-intangible amortisation:* D&A is below capex (FY25 13.9T vs 28.6T), so `acq_amort_pct` is not used and no D&A fade is applied.
- *Non-operating bridge (+136.3T = KRW 186,960/share):* cash+ST 88.0T − borrowings 18.6T − leases 2.5T − **unpaid current tax 31.96T** + ADS net proceeds US$26.2B at spot (35.1T) + LT investment assets 85.3T × (1 − **30% haircut, ASSUMPTION**) + LT financial instruments 7.1T − NCI 0.3T − the Q2 dividend (KRW 375, ex-date 8/28; a buyer today does not receive it).
- *Buyback:* the KRW 40.0T programme is not assumed executed, because progress is UNKNOWN. Its effect is shown in E2.

| Input | Bear | Base | Bull | Source / basis |
|---|---|---|---|---|
| Y1 revenue | 238.0T (run-rate × 0.75) | 317.3T (Q2-26 × 4) | 383.9T (× 1.10 bits × 1.10 ASP) | facts Q2; dossier §3 guidance (Q3 DRAM bits +~10%, H2 bits > H1); KRW up ~13% vs USD (dossier §10.8); ASP step is an ASSUMPTION |
| Y1 EBIT margin | 55% | 70% | 76.3% (Q2-26 actual) | TTM 68.0%, Q2 76.3%; bear/base are ASSUMPTIONS |
| Y2 factor / margin | 0.62 / −23.6% (FY2023 trough) | 2.0 / 55% | 2.6 / 68.0% (TTM actual) | facts; mgmt "tight ... considerable period" |
| Y3 factor / margin | 0.85 / 5% | 0.80 / 5% (trough) | 1.20 / 45% | ASSUMPTION, against FY21–25 factor/margin pairs |
| Mid-cycle EBIT (Y4–Y10 and TV) | 21.0% (FY21–25 simple avg) | **29.0% (FY21–25 revenue-weighted)** | 42.0% (FY24–25 HBM-era avg) | facts |
| Trend growth to Y4 | 5% | 22.4% fading to 10% | 22.4% held | fitted slope; fades are ASSUMPTIONS |
| Growth Y5–Y10 | 5, 5, 4, 4, 3, 3% | 9, 8, 7, 6, 5, 4% | 15, 13, 11, 9, 7, 5% | ASSUMPTION |
| Capex Y1–Y4 (T) | 50 / 30 / 25 / 25 | 55 / 60 / 45 / 40 | 60 / 70 / 60 / 55 | 2026 guide "high-40T" (H1 19.0T done); 6-K commitments; FY23-style cut in bear |
| Terminal (and incremental) ROIC | 10% | 15% | 25% | FY23–25 avg 15.5%; FY24 21.2%, FY25 32.9% |
| Terminal growth | 2% | 3% | 4% | ≤ min(4%, rf 4.369%) |
| **Value per share (KRW)** | **411,148** | **727,950** | **1,267,426** | vs price 1,443,000: −71.5% / −49.6% / −12.2% |
| TV share of EV | 24.1% | 27.9% | 35.9% | none above 75% |
| In S$ (KRW/SGD 1,048.08) | 392 | 695 | 1,209 | inputs FX |

**For the SK Square valuation downstream:** SK Square's 146,100,000 hynix shares (dossier §6) are worth 60.1T (bear), 106.4T (base) and 185.2T (bull), against 210.8T at the current price. All three figures are on the 728,866,596-share basis. If the buyback is fully executed at prices above these values, per-share value falls (E2), which matters for a holder that does not sell into it.

```
====== E0. D&A rule calibration and base-period anchors ====================================
D&A FY2024: rule 12.5T vs actual 12.6T (-0.4%)
D&A FY2025: rule 13.3T vs actual 13.9T (-4.8%)
Base revenue = Q2-26 x4 = 317.3T (TTM 189.2T); WC 15.0% of delta revenue; tax 23.0%
SBC: margins are reported EBIT (SBC expensed); dcf() adds no SBC back -> SBC treated as a cost, share count held at 728.87M (not grown). Never both.
Acquired-intangible amortisation: D&A < capex (FY25 13.9T vs 28.6T) -> acq_amort_pct not used, no D&A fade.
====== E1. Scenario inputs and outputs (KRW T; per-share KRW) ==============================

--- BEAR: WACC 13.83%, g_term 2.0%, terminal ROIC 10.0%, mid-cycle EBIT 21.0%, trend r [0.05, 0.05, 0.05, 0.05] ---
Y        Rev  growth factor  EBIT m EBITDA m    D&A  Capex   Cpx%     FCF  FCF m  PV FCF
Y1     238.0  -25.0%   2.80   55.0%    62.8%   18.5   50.0  21.0%    81.2  34.1%    76.1
Y2      55.5  -76.7%   0.62  -23.6%    19.2%   23.7   30.0  54.1%    11.0  19.9%     9.1
Y3      79.6  +43.4%   0.85    5.0%    36.1%   24.8   25.0  31.4%    -0.8  -1.0%    -0.6
Y4      98.3  +23.5%   1.00   21.0%    46.3%   24.8   25.0  25.4%    12.9  13.1%     8.2
Y5     103.2   +5.0%   1.00   21.0%    45.1%   24.9   32.5  31.5%     8.3   8.1%     4.7
Y6     108.4   +5.0%   1.00   21.0%    45.1%   26.1   34.1  31.5%     8.8   8.1%     4.3
Y7     112.7   +4.0%   1.00   21.0%    45.4%   27.5   34.1  30.3%    10.9   9.7%     4.7
Y8     117.2   +4.0%   1.00   21.0%    45.4%   28.6   35.5  30.3%    11.4   9.7%     4.3
Y9     120.7   +3.0%   1.00   21.0%    45.6%   29.7   35.0  29.0%    13.7  11.3%     4.5
Y10    124.4   +3.0%   1.00   21.0%    45.6%   30.6   36.1  29.0%    14.1  11.3%     4.1
Avg FCF margin Y5-Y10 9.7% (5-yr hist: simple 7.8%, rev-wtd 12.9%) | Y10 reinvestment 30.0% of NOPAT vs terminal g/ROIC 20.0%
PV explicit 124.0T + PV terminal 39.4T = EV 163.4T | TV share 24.1%
+ non-operating net assets 136.3T = equity 299.7T / 728.867M sh
>>> BEAR VALUE/SHARE KRW 411,148  vs price 1,443,000 => -71.5% | S$392 | of which net assets KRW 186,960
    implied: EV / mid-cycle Y4 EBIT 7.9x; price / Y4 NOPAT-per-share 66.1x

--- BASE: WACC 13.83%, g_term 3.0%, terminal ROIC 15.0%, mid-cycle EBIT 29.0%, trend r [0.224, 0.17, 0.135, 0.1] ---
Y        Rev  growth factor  EBIT m EBITDA m    D&A  Capex   Cpx%     FCF  FCF m  PV FCF
Y1     317.3   +0.0%   2.97   70.0%    75.8%   18.5   55.0  17.3%   134.6  42.4%   126.1
Y2     250.2  -21.2%   2.00   55.0%    64.8%   24.6   60.0  24.0%    80.6  32.2%    66.4
Y3     113.6  -54.6%   0.80    5.0%    31.8%   30.5   45.0  39.6%    10.3   9.1%     7.5
Y4     156.2  +37.5%   1.00   29.0%    50.1%   32.9   40.0  25.6%    21.4  13.7%    13.6
Y5     170.2   +9.0%   1.00   29.0%    49.0%   34.1   54.8  32.2%    15.2   8.9%     8.5
Y6     183.8   +8.0%   1.00   29.0%    49.4%   37.5   57.4  31.2%    19.2  10.4%     9.4
Y7     196.7   +7.0%   1.00   29.0%    49.8%   40.9   59.4  30.2%    23.5  11.9%    10.1
Y8     208.5   +6.0%   1.00   29.0%    50.1%   43.9   60.8  29.2%    28.0  13.4%    10.6
Y9     218.9   +5.0%   1.00   29.0%    50.4%   46.8   61.5  28.1%    32.6  14.9%    10.8
Y10    227.7   +4.0%   1.00   29.0%    50.6%   49.2   61.5  27.0%    37.3  16.4%    10.9
Avg FCF margin Y5-Y10 12.7% (5-yr hist: simple 7.8%, rev-wtd 12.9%) | Y10 reinvestment 26.7% of NOPAT vs terminal g/ROIC 20.0%
PV explicit 284.3T + PV terminal 110.0T = EV 394.3T | TV share 27.9%
+ non-operating net assets 136.3T = equity 530.6T / 728.867M sh
>>> BASE VALUE/SHARE KRW 727,950  vs price 1,443,000 => -49.6% | S$695 | of which net assets KRW 186,960
    implied: EV / mid-cycle Y4 EBIT 8.7x; price / Y4 NOPAT-per-share 30.1x

--- BULL: WACC 13.83%, g_term 4.0%, terminal ROIC 25.0%, mid-cycle EBIT 42.0%, trend r [0.224, 0.224, 0.224, 0.224] ---
Y        Rev  growth factor  EBIT m EBITDA m    D&A  Capex   Cpx%     FCF  FCF m  PV FCF
Y1     383.9  +21.0%   3.59   76.3%    81.1%   18.5   60.0  15.6%   174.2  45.4%   163.3
Y2     340.3  -11.4%   2.60   68.0%    75.5%   25.4   70.0  20.6%   140.3  41.2%   115.5
Y3     192.3  -43.5%   1.20   45.0%    62.1%   32.8   60.0  31.2%    61.7  32.1%    44.6
Y4     196.2   +2.0%   1.00   42.0%    61.1%   37.4   55.0  28.0%    45.3  23.1%    28.8
Y5     225.6  +15.0%   1.00   42.0%    59.9%   40.3   79.7  35.3%    29.2  12.9%    16.3
Y6     255.0  +13.0%   1.00   42.0%    60.4%   46.9   85.4  33.5%    39.6  15.5%    19.4
Y7     283.0  +11.0%   1.00   42.0%    60.9%   53.3   89.4  31.6%    51.3  18.1%    22.1
Y8     308.5   +9.0%   1.00   42.0%    61.2%   59.3   91.4  29.6%    63.9  20.7%    24.2
Y9     330.1   +7.0%   1.00   42.0%    61.6%   64.7   91.3  27.7%    76.9  23.3%    25.6
Y10    346.6   +5.0%   1.00   42.0%    62.0%   69.1   89.1  25.7%    89.7  25.9%    26.2
Avg FCF margin Y5-Y10 19.4% (5-yr hist: simple 7.8%, rev-wtd 12.9%) | Y10 reinvestment 20.0% of NOPAT vs terminal g/ROIC 16.0%
PV explicit 504.4T + PV terminal 283.1T = EV 787.5T | TV share 35.9%
+ non-operating net assets 136.3T = equity 923.8T / 728.867M sh
>>> BULL VALUE/SHARE KRW 1,267,426  vs price 1,443,000 => -12.2% | S$1,209 | of which net assets KRW 186,960
    implied: EV / mid-cycle Y4 EBIT 9.6x; price / Y4 NOPAT-per-share 16.6x

Summary (KRW per share, 728,866,596 shares):
  BEAR  KRW    411,148  (-71.5%)  TV share 24.1%  EV 163.4T
  BASE  KRW    727,950  (-49.6%)  TV share 27.9%  EV 394.3T
  BULL  KRW  1,267,426  (-12.2%)  TV share 35.9%  EV 787.5T
====== E2. Downstream: SK Square look-through and buyback / bridge variants ================
  SK Square stake 146,100,000 sh x BEAR KRW 411,148 = 60.1T (at price: 210.8T)
  SK Square stake 146,100,000 sh x BASE KRW 727,950 = 106.4T (at price: 210.8T)
  SK Square stake 146,100,000 sh x BULL KRW 1,267,426 = 185.2T (at price: 210.8T)
  BEAR: buyback fully executed (24.07M sh at KRW 1,443,000, 34.7T) -> KRW 375,909/sh (-8.6% vs no buyback)
  BEAR: buyback fully executed (24.07M sh at KRW 1,662,000, 40.0T) -> KRW 368,430/sh (-10.4% vs no buyback)
  BASE: buyback fully executed (24.07M sh at KRW 1,443,000, 34.7T) -> KRW 703,530/sh (-3.4% vs no buyback)
  BASE: buyback fully executed (24.07M sh at KRW 1,662,000, 40.0T) -> KRW 696,051/sh (-4.4% vs no buyback)
  BULL: buyback fully executed (24.07M sh at KRW 1,443,000, 34.7T) -> KRW 1,261,430/sh (-0.5% vs no buyback)
  BULL: buyback fully executed (24.07M sh at KRW 1,662,000, 40.0T) -> KRW 1,253,951/sh (-1.1% vs no buyback)
  BASE with LT investment haircut 0%: KRW 763,064
  BASE with LT investment haircut 30%: KRW 727,950
  BASE with LT investment haircut 50%: KRW 704,542
  BASE with LT investment haircut 100%: KRW 646,019
  ADS proceeds at issue rate 1,504.9 instead of spot: +KRW 5,871/share
  Profit-share accruals (LT employee benefits 2.88T + rise in other non-trade payables 5.52T, dossier §8) if debt-like: -KRW 11,524/share (not deducted)
```

## F. Reverse DCF & sensitivity grid

**What must be true at KRW 1,443,000 (BASE assumptions, WACC 13.83%):**
1. `reverse_dcf()`: revenue must compound at **11.4%/yr for 10 years from the Q2-26 run-rate** (Y10 revenue 936.3T vs FY2025's 97.1T), or **19.6%/yr from TTM** (Y10 1,136.8T), while margins follow the base cycle path. Caveat: `reverse_dcf()` holds the base per-year margin, capex and D&A percentage lists fixed while scaling revenue.
2. **Peak duration:** the price is first covered when the Y1 peak (2.97x trend, 70% EBIT) lasts **5 years** before the base downturn. Each extra peak year adds about 170–200k per share.
3. **Mid-cycle scale:** holding base margins, mid-cycle revenue would need to be **2.94x** the base (Y4 459.2T vs 156.2T).
4. **Mid-cycle margin:** holding ROIC at 15%, no margin up to 95% reaches the price, because a higher margin at fixed ROIC also raises reinvestment. With ROIC moving with margin (capital per unit of revenue fixed), the required mid-cycle margin is **84.3%** (terminal ROIC 43.6%), above every full year on record (max 48.6%).
5. **Implied IRR** on base cash flows at today's price is **6.79%**, against a WACC of 13.83%.
6. *Through-cycle view (no peak cash):* on trend revenue at 29.0% margins, value ranges from 403,899 to 1,089,940 across growth of 0–25% and ROIC of 15–40%. At ROIC 15%, extra growth adds almost nothing (ROIC ≈ WACC).

Terminal growth barely matters (727,117–728,809 for ±10%), because terminal ROIC (15%) is close to WACC. The WACC row of the grid matters far more than the g column.

```
====== F1. Reverse DCF: what must be true at KRW 1,443,000? ================================
reverse_dcf (BASE margin/capex/D&A % paths, WACC 13.83%, g 3%, ROIC 15%):
  from Q2-26 run-rate 317.3T: constant revenue CAGR 11.4% for 10 yrs (Y10 revenue 936.3T)
  from TTM 189.2T: constant revenue CAGR 19.6% (Y10 revenue 1,136.8T)
Holding BASE revenue path, ROIC fixed 15%: required mid-cycle EBIT margin (Y4-Y10 + terminal) = NOT REACHED at <=95% (value at 95%: KRW 1,338,062) (base 29.0%, 5-yr max 48.6%)
Same, with ROIC co-moving with margin (capital per unit of revenue fixed at BASE): required margin = 84.3% (implied terminal ROIC 43.6%)
Holding BASE margins: required trend/mid-cycle revenue scale = 2.94x base (Y4 mid-cycle revenue 459.2T vs base 156.2T)
Implied IRR on BASE cash flows at today's price = 6.79% (vs WACC 13.83%)
Years the Y1 peak (run-rate revenue, 70% EBIT) must persist before the BASE downturn/mid-cycle:
  peak 1 yr(s): KRW 727,950 (-49.6%)
  peak 2 yr(s): KRW 928,969 (-35.6%)
  peak 3 yr(s): KRW 1,100,329 (-23.7%)
  peak 4 yr(s): KRW 1,271,924 (-11.9%)
  peak 5 yr(s): KRW 1,455,336 (+0.9%)
  peak 6 yr(s): KRW 1,628,836 (+12.9%)
  -> price is first covered at peak_years = 5

Through-cycle view (no peak cash): trend revenue 96.6T, EBIT 29.0% every year, D&A 21.6%, value/share by constant growth x ROIC:
ROIC             0%         5%        10%        15%        20%        25%
15%         423,303    435,385    444,100    446,015    435,536    403,899
25%         429,707    474,639    533,550    610,830    711,839    842,965
40%         433,309    496,720    583,865    703,538    867,259  1,089,940
====== F2. Sensitivity: BASE value/share (KRW) by WACC x terminal growth ===================
WACC \ g         2.0%       2.5%       3.0%       3.5%       4.0%
11.83%        804,339    808,154    812,313    816,877    821,922
12.83%        760,910    763,203    765,656    768,295    771,151
13.83%        725,258    726,574    727,950    729,396    730,921
14.83%        695,520    696,200    696,887    697,581    698,282
15.83%        670,372    670,638    670,881    671,099    671,288
BASE at beta 1.0 (WACC 9.27%): KRW 1,003,655 | at OECD rf (WACC 13.75%): KRW 730,745
====== F3. Sensitivity: BASE value/share by mid-cycle EBIT margin x trend-growth path (all else BASE) ====
margin         bear trend 5%           base fade   fitted 22.4% held
21.0%                553,227             653,749             705,951
25.6%                579,523             696,025             759,504
29.0%                599,381             727,950             799,945
35.5%                636,352             787,388             875,238
42.0%                674,144             848,145             952,202
Same grid at beta 1.0 WACC:
21.0%                667,912             854,809             996,228
25.6%                718,249             939,613           1,111,791
29.0%                756,262           1,003,655           1,199,061
35.5%                827,034           1,122,886           1,361,538
42.0%                899,378           1,244,765           1,527,622
```

## G. Load-bearing inputs

Each line moves one named input ×0.9 and ×1.1 and holds everything else at BASE. The one exception is labelled: "margin + ROIC together" deliberately moves both, holding capital per unit of revenue fixed. The ±10% swings are modest (largest 7.5%) for two reasons: KRW 186,960 of the 727,950 base is non-operating net assets, and Y1–Y2 peak cash is fixed by near-term inputs. **The large swings come from discrete structural choices:** one extra year of peak (+27.6%) and beta 1.0 instead of 1.932 (+37.9%). Those two, plus the scenario choice itself, are the real load-bearing assumptions.

| Rank | Input (base value) | ×0.9 | ×1.1 | max Δ | Source |
|---|---|---|---|---|---|
| 1 | WACC 13.83% (beta-driven) | 782,329 | 686,388 | 7.5% | inputs rf + fund beta (Blume) + ERP |
| 2 | Mid-cycle margin + ROIC together (29.0% / 15%) | 690,389 | 765,511 | 5.2% | facts; capital per unit of revenue fixed |
| 3 | Trend revenue level (FY25 fit 78.9T) | 691,099 | 764,802 | 5.1% | facts FY21–25 log fit |
| 4 | Raw beta 2.391 | 756,896 | 703,086 | 4.0% | fund: beta |
| 5 | Mid-cycle EBIT margin 29.0% (ROIC fixed) | 701,108 | 754,792 | 3.7% | facts FY21–25 rev-wtd |
| 6 | Y1 EBIT margin 70% | 705,118 | 750,783 | 3.1% | ASSUMPTION (TTM 68.0%, Q2 76.3%) |
| 7 | Y1 revenue 317.3T | 705,890 | 750,011 | 3.0% | facts Q2-26 × 4 |
| 8 | Trend growth path (22.4%→10%, 9%→4%) | 707,018 | 749,776 | 3.0% | ASSUMPTION |
| 9 | Tax rate 23.0% | 746,611 | 709,289 | 2.6% | dossier §2 H1-26 effective |
| 10 | Capex Y1–Y4 (55/60/45/40T) | 745,681 | 710,220 | 2.4% | dossier §3 guide + 6-K commitments |
| 11 | Y2 EBIT margin 55% | 715,524 | 740,377 | 1.7% | ASSUMPTION |
| 12 | Terminal / incremental ROIC 15% | 716,040 | 737,695 | 1.6% | facts FY23–25 avg ROIC |
| 13 | Y2 cycle factor 2.0x | 716,059 | 739,842 | 1.6% | ASSUMPTION |
| 14 | LT investment assets 85.3T | 719,757 | 736,143 | 1.1% | facts H1 |
| 15 | Terminal growth 3% | 727,117 | 728,809 | 0.1% | ASSUMPTION |
| 16 | Y3 trough factor 0.80x | 727,713 | 728,188 | 0.0% | ASSUMPTION |
| — | **Peak duration 1 → 2 years** (discrete) | | 928,969 | +27.6% | ASSUMPTION; mgmt "considerable period" |
| — | **Beta 1.932 → 1.0** (discrete) | | 1,003,655 | +37.9% | rule default if no vendor beta |
| — | LT investment haircut 30% → 0% / 100% | 646,019 (100%) | 763,064 (0%) | −11.3% / +4.8% | ASSUMPTION |

```
====== G. Load-bearing inputs: BASE value/share with each input x0.9 / x1.1 (one at a time) ====
BASE = KRW 727,950
input                                            x0.9       x1.1   max |d|  source
WACC 13.83% (beta-driven)                     782,329    686,388     7.5%  inputs rf + fund beta (Blume) + ERP
Mid-cycle margin + ROIC together              690,389    765,511     5.2%  facts; capital/revenue fixed
Trend revenue level (FY25 fit 78.9T)          691,099    764,802     5.1%  facts FY21-25 log fit
Raw beta 2.391                                756,896    703,086     4.0%  fund: beta
Mid-cycle EBIT margin 29.0% (ROIC fixed)      701,108    754,792     3.7%  facts FY21-25 rev-wtd
Y1 EBIT margin 70%                            705,118    750,783     3.1%  ASSUMPTION (TTM 68.0 / Q2 76.3)
Y1 revenue 317.3T                             705,890    750,011     3.0%  facts Q2-26 x4
Trend growth path (22.4%->10%, 9%->4%)        707,018    749,776     3.0%  ASSUMPTION
Tax rate 23.0%                                746,611    709,289     2.6%  dossier §2 H1-26 effective
Capex Y1-Y4 (55/60/45/40T)                    745,681    710,220     2.4%  dossier §3 guide + 6-K commitments
Y2 EBIT margin 55%                            715,524    740,377     1.7%  ASSUMPTION
Terminal/incremental ROIC 15%                 716,040    737,695     1.6%  facts FY23-25 avg ROIC
Y2 cycle factor 2.0x                          716,059    739,842     1.6%  ASSUMPTION
LT investment assets 85.3T                    719,757    736,143     1.1%  facts H1 LT inv. assets
Terminal growth 3%                            727,117    728,809     0.1%  ASSUMPTION <= min(4%, rf)
Y3 trough cycle factor 0.80x                  727,713    728,188     0.0%  ASSUMPTION (FY2023 0.62)

Discrete inputs (not +/-10%):
  Peak duration 1 -> 2 yrs             KRW    928,969 (+27.6%)
  Beta 1.932 -> 1.0 (WACC 9.27%)       KRW  1,003,655 (+37.9%)
  LT investment haircut 30% -> 0%      KRW    763,064 (+4.8%)
  LT investment haircut 30% -> 100%    KRW    646,019 (-11.3%)
```

## H. Open questions for the Skeptic

1. **Beta 2.391 (vendor; benchmark and window UNKNOWN) drives WACC to 13.83%.** The downturn is also modelled explicitly in the cash flows, so cyclical risk may be counted twice. At beta 1.0 the base is 1,003,655 (+37.9%). This is the largest single methodological lever, and I followed the rule rather than override it.
2. **How long does the peak last?** The base gives one year at the run-rate peak, then Y2 at 2.0x trend, then a Y3 trough. The price requires about five years of peak conditions (F1). Management says supply stays tight "for a considerable period" and there are 3–5 year LTAs, but nothing quantifies prices. **Q3-26 results (~10-28/29, unconfirmed) are the first test.** Y1 inputs alone move value by only about 3% per ±10%, so Q3 matters mainly for what it implies about *duration* (pricing into 2027, HBM 2027 contracts), not for the quarter itself.
3. **The mid-cycle anchor rests on thin history.** The trend is fitted on five annual points, two of which (FY2021–22) are rounded release figures. FY2019–20 are not in facts.json, so the orchestrator's suggested FY2019–FY2025 window could not be used. The base mid-cycle (29.0% EBIT on 156.2T in Y4) is the core judgement.
4. **Is the HBM uplift structural?** The +19.8pp on-trend margin uplift comes from two pairs of years. HBM share is a single IDC data point, and its trend is UNKNOWN. The bull's 42.0% mid-cycle depends on it.
5. **LT investment assets of 85.3T at a 30% haircut.** The Kioxia carrying value is UNKNOWN, and the deferred tax liability of 7.84T may already partly cover the tax on the gain. The value range is 646,019 (100% haircut) to 763,064 (0%).
6. **Bridge items:** the ADS proceeds are converted at spot. At the issue rate of 1,504.9 they would be +5,871 per share, and whether they were converted is UNKNOWN. The unpaid current tax of 31.96T is fully deducted, though part may relate to fair-value gains. Profit-share accruals are **not** deducted (−11,524 per share if they are debt-like).
7. **Buyback:** if the 24.07M shares are bought at KRW 1,443,000–1,662,000, base per-share value falls by 3.4–4.4%, and bear by 8.6–10.4%. Shares bought to date are UNKNOWN.
8. **Tax at 23.0%** is the H1-26 effective rate, which includes tax on the finance gains. The operating tax rate is UNKNOWN (±10% → ∓2.6%).
9. **Working capital at 15%** is gross because payables are UNKNOWN. The capex basis (cash vs accrual) is UNKNOWN, and Y1 capex of 55T is an assumption built from the "high-40T" calendar-2026 guide.
10. **Is the bear deep enough, or too deep?** Its Y2 revenue of 55.5T is below FY2024's 66.2T: the FY2023 trough factor of 0.62 applied to a 5% trend. Its value of 411,148 is roughly the 52-week low (411,500).
11. **Reading the reverse DCF:** `reverse_dcf()` scales revenue but keeps base per-year percentage lists, for example Y3 capex at 39.6% of a much larger revenue. Read the 11.4% and 19.6% CAGRs alongside the cleaner peak-duration and IRR lines.
12. **FX:** KRW appreciation is modelled only as a Y1 offset in the base, with no FX path beyond Y1. For an SGD-based holder, KRW/SGD adds to the return on top of the KRW values here (S$ conversions use today's spot only).
13. **Consensus quality:** the vendor estimates are internally inconsistent by about 12% (dossier §9). They appear only in the forward P/E and PEG lines and never in the DCF.
