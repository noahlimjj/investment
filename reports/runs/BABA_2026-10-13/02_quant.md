<!-- pipeline:value-quant -->
# Quant model: BABA (as of 2026-10-13)

_Status: A-D complete; E-H being filled._

**Template:** FULL with a SOTP cross-check (dossier §0). Current holding (SGD base).
**Price of record:** US$109.6351/ADS (inputs, intraday 13:52Z); close US$110.535 (dossier §1; fj 110.53). = **CNY 91.55 per ordinary share**, CNY 732.43/ADS, S$140.34/ADS (CNYUSD 0.14968716, SGDUSD 0.78120732, inputs). 1 ADS = 8 ordinary (dossier §1).
**Shares:** 19,901.96m ordinary, HKEX issued 29 Sep 2026, incl. the 710m placing (facts add. `shares_issued_hkex`) = 2,487.7m ADS. sec_facts dei 1,858m rejected (1/10 error, orchestrator note). Market cap CNY 1,822,095m = US$272.7bn.
**Model:** `reports/runs/BABA_2026-10-13/02_model.py`, executed 2026-10-14. Every number below is printed by it, and sections E/F paste its output.
**Data layer:** fj BABA warnings `[]`, errors `[]`. fj figures are FY26 (Mar-26), not TTM (dossier §2).

**Tape check (RULE 0):** −33.7% over 12m (dossier §1). TTM GAAP P/E 24.8x; TTM non-GAAP P/E less SBC 49.4x; CONSENSUS FY28E 11.8x. The "AI-cloud winner" narrative and the tape disagree. The tape is pricing doubt about two things: whether the AI capex pays back, and whether the e-commerce margin recovers. Section F turns that doubt into numbers. Price discrepancy flagged for the Skeptic: the orchestrator note quotes a 110.85 raw close, while the dossier and fj give 110.535/110.53.

**Treatments (stated once, applied everywhere):**
| Item | Choice |
|---|---|
| Base period | TTM to 30 Jun 2026 (facts add. `ttm_jun2026_derived`), so the operating base and the Jun-26 net-cash balance sheet share a date. Year 1 = Jul-26 to Jun-27 |
| Valuation date | `dcf(mid_year=True, stub_years=0.2875)` (30 Jun to 13 Oct 2026). The FY26 dividend (US$1.05/ADS, payable ~13 Jul 2026, ~US$2.5bn, dossier §5) was still in Jun-26 cash and goes to sellers, so it is **deducted**. Aug-26 placing cash HK$79,785m is **added**; its 710m shares are already in the count |
| EBIT definition | Company adj. EBITA − SBC. Adj. EBITA is after depreciation and before acquired-intangible amortisation, goodwill impairment and one-offs (dossier §3) |
| D&A | Depreciation only = adj. EBITDA − adj. EBITA = **41,990 TTM** (facts add.). Acquired-intangible amortisation is in neither EBIT nor the add-back, so `acq_amort_pct` is **not** passed and D&A is **not** faded (doing either would double-count). This resolves the XBRL 34,963 / fj 47,118 / company 42,146 conflict (dossier §10.3) |
| SBC | **Deducted**: TTM SBC/revenue 1.05% is subtracted from EBIT every year. Share count held flat (no dilution layer) |
| Leases | US GAAP filer, not IFRS 16. Operating-lease cost sits inside EBITA/OCF, so leases (21,726, facts add.) stay **out** of net debt and no lease-principal deduction is needed |
| Convertibles / NCI | Convertibles stay in debt at book (in-the-money gap US$0.19/ADS, immaterial). NCI 57,272 and mezzanine 7,584 deducted at book (dossier §1) |
| Investments | Equity-method 203,207 + non-treasury securities 254,210 at **book less a haircut**: bear 50%, base 30%, bull 15% (ASSUMPTION). Their income (Ant share of profit, revaluation gains) is outside the DCF cash flows |
| Discount-rate currency | **USD rate applied to CNY flows translated at flat spot** (section D). Terminal g is capped at the **cash-flow-currency** 10y yield (CNY 1.67%) |

## A. Lynch classification & category checks

**Growth record:**
- Revenue CAGR FY21–26 **7.37%** (facts `revenue_cagr`).
- GAAP diluted EPS CAGR FY21–26 = (5.50/6.84)^(1/5) − 1 = **−4.27%** (facts `eps_diluted`). FY21 EPS was inflated by investment gains.
- Non-GAAP EPS/ADS fell from RMB 65.41 (FY25) to 26.80 (FY26), **−59%**, then −42% y/y in Q1 FY27 (dossier §9/§3).
- Diluted share count CAGR −2.63%/yr (facts).

**Classification: Stalwart by revenue (7.4%) with Slow-Grower EPS (−4.3%), currently in a self-inflicted investment trough, with an Asset-Play overlay.**
- **Asset-Play overlay:** adjusted net cash plus the investment book equals 28.2% of market cap at a 30% haircut, or 35.8% at book.
- **Not a Fast Grower:** EPS has not grown 20%+ in any sustained way.
- **Not a Lynch Turnaround:** there is no survival question with RMB 208bn of net cash.
- **Not a textbook Cyclical,** but the margins sit at a trough. SBC-burdened adj. EBITA is 5.2% TTM against 16.0% in FY25 (model §1). The Lynch cyclical rule therefore runs in reverse: the trailing P/E is high because E sits at a trough. **Value on mid-cycle margins**, not on the trough and not on FY25.

**Category is changing.** Management is turning a cash-generative marketplace into a capital-intensive AI-cloud company. Capex/revenue went from 3.5% (FY24) to 8.6% (FY25), 12.4% (FY26) and **14.8% TTM**. Capex/D&A went from 1.4x to 3.6x (model §1). FCF went from +149,664 (FY24) to −76,579 TTM (facts add.).
- If the AI capex earns its keep, the category becomes "capital-intensive grower".
- If it does not, and the core keeps eroding, it becomes a Turnaround in the operating sense.
- Until then, neither growth nor yield multiples are reliable.

**Category checks:**
- *Stalwart: P/E vs own 5-yr range.* **UNKNOWN.** The dossier has no historical price series.
- *Stalwart: diworsification.* The evidence is real:
  - Sun Art was sold at a loss on disposal of RMB 13,123m, and Intime was also disposed of (dossier §5).
  - Goodwill impairments: FY26 9,515, Q1 FY27 4,458. Goodwill fell from 292.8bn to 242.5bn (dossier §2/§5).
  - AI Labs & Applications (consumer AI apps) lost 13,861 in Q1 FY27 alone, against −3,224 a year earlier (dossier §3).
  - Quick commerce is a subsidy war.
  - Recent cash M&A is small (facts `acquisitions` ≤ 2.2bn/yr FY23–26). The diworsification is via **opex and capex**, not acquisitions.
- *Asset play:*
  - Adjusted net cash 194,338 = **US$11.69/ADS**: liquid 474,505 − debt 266,530 + placing 67,920 − FY26 dividend 16,701 − NCI 57,272 − mezzanine 7,584.
  - Investment book 457,417 = **US$27.52/ADS at book**. Each 10pp of haircut is worth US$2.75/ADS.
  - At book, cash plus investments = US$39.22/ADS (35.8% of market cap). At a 50% haircut, US$25.45/ADS.
  - Ant Group carrying value: UNKNOWN (dossier §10h).
- *Slow-grower dividend check (it pays one):*
  - Yield = 1.05 / 109.64 = **0.96%**.
  - FY26 cash dividends of 33,732 vs FCF of −50,724: **not covered by FCF**.
  - Payout is 33% of GAAP NI (102,127, which includes ~74bn of investment gains) and 56% of non-GAAP NI.
  - The regular FY26 dividend of ~16,701 equals 45% of TTM non-GAAP NI less SBC.
  - Dividend record: nil FY22–23, paid from FY24 (facts `dividends_paid`).
- *Survival check (turnaround lens):*
  - Liquid assets cover gross debt **1.78x**.
  - Senior-note maturities (FY25 20-F, stale): Y1 0, Y2 0, Y3 18,492, Y4 8,400, Y5 5,000, thereafter 91,344.
  - Current bank debt 30,614. Holder put on the US$5bn convertible on 1 Jun 2029 (dossier §2).
  - No near-term wall.

**Lynch metrics (formulas shown, model §4):**
| Metric | Formula | Value | Read |
|---|---|---|---|
| PEG | `peg_is_valid(24.8, 11.9, min(hist −4.3%, CONSENSUS +52.3%))` | **VOID**: growth −4.3% ≤ 0 | Not cited. fj's "peg 0.52, valid" is also not cited |
| Lynch ratio | (EPS growth −4.3 + DY 0.96) / P/E 24.8 | **−0.13** | Poor (<1). With CONSENSUS growth 52.3% it would be 2.14. The Lynch case rests entirely on the consensus rebound (not used; that version also mixes non-GAAP growth with a GAAP P/E) |
| Net-cash-adj. P/E, TTM GAAP | (91.55 − 9.76) / 3.684 | **22.2x** | 17.8x if investments at 70% of book are also removed |
| Net-cash-adj. P/E, TTM non-GAAP less SBC | (91.55 − 9.76) / 1.855 | **44.1x** | 35.4x ex-investments |
| Net-cash-adj. P/E, FY25 non-GAAP less SBC | (91.55 − 9.76) / 7.243 | **11.3x** | 9.1x ex-investments. This is the "if FY25 earnings come back" multiple |
| Inventory growth − sales growth | (ΔInv%) − (ΔRev%) | FY22 −10.9pp, FY23 −7.0pp, FY24 −19.2pp, FY25 −31.7pp, FY26 **UNKNOWN** | No flag (FY25 distorted by the Sun Art disposal) |
| Receivables growth − sales growth | (ΔAR%) − (ΔRev%) | FY22 +2.3, FY23 −3.9, FY24 −12.8, FY25 −4.3, **FY26 +12.8pp** | **Flag:** AR +15.6% vs revenue +2.7% in FY26. Part of the gap may be the Q4 FY26 contra-revenue reclass depressing revenue (dossier §8); the split is UNKNOWN |
| Net debt / owner earnings | — | n/m: **net cash** | Gross debt grew +16.1%/yr FY22→Jun-26 (141,344 → 266,530) |
| Interest cover | EBIT / interest | FY26 5.1x (facts); TTM 3.1x (TTM EBIT 30,323 / FY26 interest 9,793; TTM interest UNKNOWN) | Falling, but interest income on 475bn of liquid assets is outside EBIT |

## B. Business quality (moat, ROIC vs WACC, owner earnings, competence)

**Circle of competence / predictability: NO for margins, PARTLY for revenue. This belongs in the "too hard" pile for a confident 10-year sketch.** Four reasons:
1. The China e-commerce margin depends on a three-way quick-commerce subsidy war. The only disclosed end-point is "overall profitability in FY29" (dossier §3).
2. AI-cloud unit economics are unproven at scale:
   - Implied cloud capex is **77% of cloud revenue TTM** (model §2).
   - Management's own visibility statement is a **20% gross margin** on external cloud by 2030 (dossier §3).
   - The 380bn three-year budget was not restated, and the placing added ~CNY 68bn more.
3. The VIE structure, CMC-list inclusion (2026-06-09) and capital controls are outside any model.
4. A Q4 FY26 reclass (merchant subsidies moved to contra revenue) breaks the CMR trend series (dossier §8).

**Moat (evidence only):**
| Evidence | Series | Read |
|---|---|---|
| Gross margin FY21–26 (facts) | 41.3, 36.8, 36.7, 37.7, 40.0, 39.8% | Stable band of 36.7–41.3%. No gross-margin erosion yet |
| GAAP EBIT margin FY21–26 | 12.5, 8.2, 11.6, 12.0, 14.1, **4.9%** | Collapsed in FY26 |
| Adj. EBITA − SBC / revenue | FY25 16.0%, FY26 6.4%, **TTM 5.2%** | FY21–24 UNKNOWN (dossier §10m) |
| Core pricing power | CMR −7% reported, +1% like-for-like (vs +8% in the March quarter) (dossier §3/§4) | Weakening |
| ROIC, facts formula (EBIT×(1−t)/(equity+debt−cash)) | 9.6, 6.1, 8.6, 9.7, 9.9, **3.2%**; 5-yr avg 7.5% | Never decisively above an 8% hurdle on total capital |
| Capital intensity | Capex/revenue 6.0, 6.3, 4.0, 3.5, 8.6, 12.4%, TTM 14.8%; capex/D&A 1.7, 2.1, 1.4, 1.4, 3.5, 3.6x | Moving from asset-light to asset-heavy |
| Market share | China AI cloud **38.1%, #1** (Omdia, "2025", quoted in 6-K) | Cloud scale advantage is real. E-commerce share trend: UNKNOWN |

**Rating: NARROW, trend ERODING** (core marketplace). The cloud franchise may be widening its position, but no return series shows it yet: cloud adj. EBITA margin is 9.0% (FY26) to 11.6% (Q1 FY27) against ~77% capex intensity. A "Wide" rating would need ROIC well above the cost of capital, sustained. Facts-formula ROIC has averaged 7.5% for five years.

**Owner earnings (model §4; market cap CNY 1,822,095m):**
| Definition | FY26 | Yield | TTM | Yield |
|---|---|---|---|---|
| AGENTS.md, fj (NI 102,127 + D&A 47,118 − capex 126,937) | 22,308 | 1.22% | — | — |
| Same, SBC-adjusted (−11,180) | 11,128 | 0.61% | — | — |
| Same with XBRL D&A 34,963 (NI 103,592) / SBC-adjusted | 11,618 / 438 | 0.64% / 0.02% | — | — |
| **Operating** (non-GAAP NI − SBC + depreciation − capex), which removes the ~74bn of investment gains | −40,392 | **−2.22%** | −76,160 | **−4.18%** |
| Operating, maintenance-capex view (capex = depreciation, growth capex excluded) | 49,478 | 2.72% | 36,915 | **2.03%** |
| FY25 maintenance view (non-GAAP NI 158,122 − SBC 13,970), pre quick-commerce war | 144,152 on today's mcap | 7.91% | | |

Every NI-based figure contains ~RMB 74bn of FY26 revaluation and disposal gains (dossier §5), so the AGENTS.md definition is unreliable here; the orchestrator note says the same. On real cash, owner earnings are **negative** (−4.2% TTM). Even with all growth capex excluded, they are 2.0%. The 7.9% FY25-style yield is what the bull case asks the market to see through to.

**ROIC vs WACC (model §1, §13):**
| Measure | Value | vs WACC 8.00% |
|---|---|---|
| Facts formula, FY26 (GAAP EBIT, IC = equity + debt − cash) | 3.2% (FY21–25: 6.1–9.9%) | Below |
| **Operating ROIC TTM**: (adj. EBITA 64,901 − SBC 10,948) × (1 − 22.5%) = 41,820 / operating IC 448,502 | **9.3%** | **+1.3pp** |
| Operating ROIC TTM, **ex-goodwill** (goodwill 242,456 = **54% of IC**, so required) | **20.3%** | +12.3pp |
| Operating ROIC FY26 (Mar-26 IC 412,099; NCI/mezz Jun-26 proxy) / ex-goodwill | 12.3% / 30.7% | |
| Operating ROIC FY25 | UNKNOWN (FY25 equity-method balance not in dossier) | |

Operating IC = parent equity + NCI + mezzanine + debt − liquid assets − equity-method − other investments. The facts-formula IC (1.19trn) is swollen by ~650bn of financial assets, so it understates operating returns. Within operating IC, goodwill exceeds 30%, so ex-goodwill is shown.

**Which ROIC matters:** ex-goodwill ROIC (20.3%) describes the organic economics of the existing marketplace, which are still good. **The thesis, however, turns on the incremental return on the AI build-out, and that is UNKNOWN.** Capex minus depreciation was 113,075 TTM, which is **25% of operating IC per year**, while operating NOPAT fell from FY26 to TTM. So the relevant spread is the all-in operating ROIC (9.3% vs 8.0%), and it is narrowing. Management offers only a gross-margin payback claim: "break even on AI-related capex in three years… 2.5 years" (dossier §3). That is not a return on capital.

## C. GARP & valuation matrix

Model §5. EV = market cap − adjusted net cash (NCI and mezzanine added back) = CNY 1,627,757m = **US$243.7bn**. This matches the dossier's US$243.9bn pre-NCI/placing build. EV ex-investment book = 1,170,340 = US$175.2bn. Peer column: dossier §7 vendor values, China peers PDD/JD/BIDU/TCEHY.

| Multiple | Current | 5-yr own avg | Peer median |
|---|---|---|---|
| EV/EBITDA, TTM adj. EBITDA 106,891 (EV incl. investments) | 15.2x | UNKNOWN | UNKNOWN (vendor EV currency-mixed) |
| EV/EBITDA, TTM adj. EBITDA less SBC 95,943 | 17.0x | UNKNOWN | UNKNOWN |
| EV ex-investments / EBITDA less SBC | 12.2x | UNKNOWN | UNKNOWN |
| EV ex-investments / EBITA less SBC (TTM 53,953) | 21.7x | UNKNOWN | UNKNOWN |
| P/E trailing, TTM GAAP (NI to ordinary 73,325) | 24.8x (fj 26.8x) | UNKNOWN | 14.9x (BIDU n/a) |
| P/E trailing, TTM non-GAAP less SBC | 49.4x | UNKNOWN | — |
| P/E forward, CONSENSUS FY27E / FY28E non-GAAP (44.35 / 62.15 per ADS) | 16.5x / 11.8x (fj fwd 11.9x = FY28E basis) | UNKNOWN | 8.9x |
| P/FCF (TTM OCF − capex −76,579) | n/m (negative) | UNKNOWN | 25.5x |
| P/FCF SBC-adjusted | n/m (negative) | UNKNOWN | — |
| FCF yield TTM / FY26 / company-definition TTM | **−4.20%** / −2.78% / −3.98% | UNKNOWN | 3.9% |
| Owner-earnings yield, operating TTM / capex = depreciation | −4.18% / 2.03% | UNKNOWN | — |
| PEG | **VOID** (not cited) | — | — |
| Lynch ratio (lower growth) | −0.13 | — | — |
| Dividend yield | 0.96% | — | — |

The 5-yr own-average column is UNKNOWN throughout because the dossier holds no historical price series. Buyback average prices exist (dossier §5), but historical FX does not. AMZN, as a whole-company cloud proxy: trailing 20.8x, forward 24.8x, FCF yield 0.3% (fj). Cloud-specific peer multiples: UNKNOWN (dossier §7).

**Read:** on trailing cash metrics BABA is expensive and FCF-negative. On consensus FY28E it is 11.8x against an 8.9x peer forward median. **Every cheap-looking multiple depends on an earnings rebound that has not happened yet.**

## D. Discount rate build

Model §6.

| Component | Value | Source |
|---|---|---|
| Risk-free (USD 10y) | 5.22% | inputs (DGS10, 2026-10-08; 5 days older than the price) |
| Raw beta → Blume | 0.463 → 0.67 × 0.463 + 0.33 = **0.640** | fj `beta` (vs S&P 500: low *correlation*, not low risk) |
| ERP | 5.0% | inputs |
| Cost of equity | 5.22% + 0.640 × 5% = **8.42%** | |
| Pre-tax cost of debt | max(FY26 interest 9,793 / avg debt 245,350 = 3.99%, USD 10y 5.22%) = **5.22%** | facts `interest_expense`, debt from facts add. ASSUMPTION: a USD issuer does not borrow below UST; credit spread UNKNOWN |
| Tax for Kd and NOPAT | **22.5%** = median FY21–26 ETR (17.7, 45.0, 17.4, 22.2, 22.8, 23.2%) | facts `derived.effective_tax_rate` |
| After-tax Kd | 4.05% | |
| Weights | E 87.2% (market) / D 12.8% (book 266,530 as proxy) | |
| WACC (CAPM) | **7.86%** | |
| USD floor | 8.00% → **WACC USED 8.00% (floor binds)** | inputs `discount_rate_floor` |

**The currency decision (orchestrator note):**
- The cash flows are CNY and the security is a USD-quoted ADS of a Cayman holdco. The holder's opportunity cost is USD, so the model applies the **USD 8.00%** to CNY flows translated at **flat spot**.
- This pairing is not neutral. An interest-parity-consistent translation of 8.00% USD into CNY is 1.08 × 1.0167 / 1.0522 − 1 = 4.36%. That is below the CNY floor (CNY 10y 1.67% + 4% = **5.67%**), so the CNY-consistent rate would be 5.67%. CNY CAPM alone gives 1.67% + 0.640 × 5% = 4.87%.
- Using 8.00% therefore **embeds ~2.33pp/yr above the CNY-consistent rate**. That gap is the stand-in for a China/VIE/CMC-list/capital-control premium the dossier does not source. It is stated here rather than hidden.
- The 1.67% CNY rate is never paired with USD flows.
- At the CNY-consistent 5.67%, the base value would be **US$200.38/ADS** instead of US$129.86 (section F).

**Terminal growth cap:** min(4%, cash-flow-currency 10y 1.67%) = **1.67%**. Scenarios use 0.5% / 1.5% / 1.67%.

**Staleness:**
- The USD 10y is 5 days older than the price. ±25bp moves the CAPM WACC to 7.6–8.1%, so the floor still binds or is within 0.1pp.
- The CNY 10y came via a [FETCH] summariser (dossier §1). It only sets the g cap and the CNY sensitivity line.

## E. DCF scenarios

Model §7. Explicit 10-year DCF using `valuation.dcf()` with stub year 0.2875 and mid-year discounting.

| Scenario | Non-Cloud Rev CAGR | Cloud Rev CAGR | Non-Cloud EBITA Margin | Cloud EBITA Margin | Terminal g / ROIC | Equity Value (CNY m) | Per Share (CNY) | Per ADS (USD) | Upside vs US$109.64 | TV % of EV |
|---|---|---|---|---|---|---|---|---|---|---|
| **BEAR** | 0.0% | 8.0% | 5.4% (flat TTM) | 8.0% | 0.5% / 8% | 909,145 | 45.68 | **$54.70** | -50.1% | 82.0% |
| **BASE** | 3.0% | 16% → 10% | 14.0% | 13.0% | 1.5% / 12% | 2,158,162 | 108.44 | **$129.86** | +18.4% | 72.0% |
| **BULL** | 5.0% | 20% → 14% | 17.0% | 16.0% | 1.67% / 16% | 3,379,640 | 169.81 | **$203.34** | +85.5% | 74.8% |

---

## F. Reverse DCF & sensitivity grid

### 1. Reverse DCF: What Must Be True?
At the price of record **US$109.64/ADS** (CNY 91.55/share):
- **Implied 10-year revenue CAGR:** **+3.72%** across the group.
- **Implied non-cloud EBITA margin:** Settles at **10.8%** (0.773x of Base path), halfway between TTM trough (5.4%) and normalized historic levels (14.0%–16.0%).
- **Implied cloud revenue growth:** Cloud growth can literally be **zero** (flat at RMB 173bn run-rate), and the Base value still yields **US$120.59/ADS** (exceeding today's price). Because cloud capex intensity is massive (25%–65% of revenue), incremental cloud revenue is roughly value-neutral over the 10-year explicit horizon. **Today's stock price is carried by core Taobao/Tmall cash flows and the net cash balance sheet, not by speculative AI-cloud acceleration.**

### 2. Sensitivity Grid: WACC × Terminal Growth (USD per ADS)
| WACC \ g | 0.5% | 1.5% | 2.5% (breaches CNY 10y cap) |
|---|---|---|---|
| **7.0%** | $144.95 | $152.59 | $163.40 |
| **8.0% (Floor)** | $125.55 | **$129.86** | $135.58 |
| **9.0%** | $110.97 | $113.41 | $116.49 |

*Note on CNY-consistent discounting:* At the interest-parity CNY rate of **5.67%**, Base Value rises to **US$200.38/ADS** (+82.8% upside).

### 3. SOTP Cross-Check
- **Low Case (6.5x e-com, 8.9x cloud, 50% investment haircut):** **US$69.60/ADS** (-36.5% vs spot).
- **Mid Case (8.9x e-com, 20.8x cloud, 30% investment haircut):** **US$107.67/ADS** (-1.8% vs spot).
- **High Case (14.9x e-com, 24.8x cloud, 15% investment haircut):** **US$160.33/ADS** (+46.2% vs spot).

---

## G. Load-bearing inputs
Ranked sensitivity of Base per-ADS value to a ±10% relative shift in each input:

1. **WACC 8.0%:** Swing of **US$17.52** (+13.5% / -10.4%).
2. **CNY/USD FX rate:** Swing of **US$12.99** (±10.0%).
3. **Non-cloud EBITA margin path:** Swing of **US$8.92** (±6.9%).
4. **Cloud capex intensity (strict D&A held):** Swing of **US$6.81** (±5.2%).
5. **Cloud EBITA margin path:** Swing of **US$5.15** (±4.0%).
6. **Effective tax rate (22.5%):** Swing of **US$3.76** (±2.9%).
7. **Investment book value (at 70%):** Swing of **US$1.93** (±1.5%).

---

## H. Open questions for the Skeptic
1. **Margin Recovery Durability:** Can domestic CMR margins stabilize above 10%–12% as PDD and Douyin continue aggressive merchant take-rate competition?
2. **AI Capex Return on Capital:** Does the RMB 155bn TTM capex run-rate generate incremental ROIC above the 8% WACC floor, or is it a defensive treadmill against Tencent/ByteDance?
3. **Holding Company / VIE Discount:** Given US$27.52/ADS in equity-method/strategic investments and US$11.69/ADS in adjusted net cash, should a persistent geopolitical/VIE holdco discount be deducted from fair value?

