# Skeptic Audit: SYK (Stryker Corporation) — as of 2026-10-13

## 1. Pre-Mortem (Written before reading the Quant model)
**The Structural Downside Thesis (Business worth >50% less in 5 years):**
Stryker is priced as an infallible mid-teens compounder in hospital medtech. The core vulnerability is the **exhaustion and diminishing returns of its debt-funded serial acquisition treadmill**.

The structural decline mechanism:
1. **Acquisition Dependency & Integration Drag:** Over FY20–FY25, Stryker deployed $14.1B on M&A—consuming 76% of cumulative free cash flow and adding billions in net debt. However, acquisition returns have begun to sour: cumulative impairments reached $1.72B over the period (17.4% of deal spend), punctuated by the disastrous write-down ($977M) and firesale ($165M) of Spinal Implants. If recent large acquisitions like Inari Medical ($4.81B, peripheral vascular) suffer extended manufacturing or regulatory disruptions (evidenced by ongoing peripheral vascular supply issues in Q2/Q3 2026), acquired revenue yield will fall well below cost of capital.
2. **Robotic Moat Erosion:** Stryker's Mako robotic system has historically driven joint replacement market share. However, competing platforms (Zimmer Biomet's ROSA, Johnson & Johnson's VELYS, Smith & Nephew's CORI) are closing the feature gap with lower capital requirements and open implant architectures. If orthopedic procedure volumes normalize post-COVID backlog clearance and Mako placement growth slows, orthopedic implant growth will decelerate toward low single digits.
3. **Leadership Handover Risk:** Long-time CEO Kevin Lobo steps down at year-end 2026. Executive transitions at acquisitive medtech conglomerates frequently uncover latent integration friction, leading to "kitchen sink" write-downs and guidance resets.
4. **Multiple De-rating:** Stryker trades at a forward adjusted P/E of ~19x and trailing GAAP P/E of ~29x. If organic revenue growth slips from ~9–10% to 4–5%, the stock de-rates to a mature medtech multiple of 14x–16x, cutting equity value by 45%–55% to ~$130–$150/share.

---

## 2. Number Audit & Corrections to Quant Model

| # | Quant Input / Metric | Quant Value | Skeptic Verification & Finding | Impact on Valuation |
|---|---|---|---|---|---|
| 1 | **Price of Record** | $283.71 close 2026-10-13 | **VERIFIED:** Reconciles with official close. $282.70 was intraday. | Basis confirmed |
| 2 | **Loaner Instrument D&A Add-back** | Cash-flow D&A ($3,678M) used; NOT SEC facts $4,055M | **AUDITED & UPHELD:** The Quant correctly rejected the $4,055M tag. Adding back loaner instrument amortisation (~$377M) without charging the ongoing cash replacement spend in OCF artificially inflates owner earnings. | Prevents +$9.80/share distortion |
| 3 | **Capex Completeness** | PP&E capex $868M (FY25) | **VERIFIED:** Confirmed SEC facts flag on FY24 was a false positive caused by a $750M short-term investment purchase. | PP&E capex clean |
| 4 | **Organic vs Acquired Revenue CAGR** | ~9.0% organic vs 11.8% reported | **VERIFIED:** Acquisitions contributed ~2.5–3.0 percentage points of historical reported growth. | Base model appropriately models organic fade |
| 5 | **Tax Rate in NOPAT** | 17.3% (5-yr pooled rate) | **AUDIT NOTE:** TTM GAAP effective tax rate was 27.6% and pooled ETR is 17.3%. At a conservative 22.5% tax rate, Base value falls from $209.13 to **$194.46** (-7.0%). | Sensitises fair value downward |
| 6 | **Terminal Value Share** | 56% in Base | **VERIFIED:** Well below the 75% flag limit. | Pass |
| 7 | **Net Debt & EV Bridge** | $11,466M net debt | **VERIFIED:** Debt $14,942M less cash $3,391M and ST investments $85M = $11,466M. | Clean |
| 8 | **Diluted Share Count** | 386.0M shares | **VERIFIED:** Basic is 383.57M; diluted count matches Q2 10-Q. | Clean |

---

## 3. Quality of Earnings & GAAP Reconciliation
- **Persistent Non-GAAP Distortion:** The gap between GAAP and non-GAAP earnings is structurally wide:
  - TTM GAAP EPS: **$9.66**.
  - Guided FY26 Adjusted EPS: **$15.025** (a **55% premium** over GAAP).
  - This gap is driven by perpetual amortization of acquisition intangibles ($400M–$500M annually), cyber incident remediation, and acquisition-related restructuring charges. While analysts treat these as "one-offs," serial acquirers incur these costs perpetually.
- **Cash Flow Conversion:** Free cash flow conversion of adjusted net income averages 80–85%, burdened by ongoing working capital absorption and instrument set replenishment.

---

## 4. Capital Allocation Assessment: Grade C+
1. **Buffett $1 Retained Earnings Test:**
   - 5-year change in market cap vs retained earnings is positive (~1.4x), reflecting multiple expansion and medtech secular tailwinds.
2. **Serial M&A Track Record:**
   - Deployed $14.1B over FY20–FY25, consuming 76% of cumulative FCF.
   - Cumulative impairments of $1.72B represent a meaningful 17.4% write-off rate of deal capital.
   - Spinal Implants write-down and sale proved value-destructive.
3. **Share Repurchase Discipline:**
   - Buybacks have been zero over the past five years as all discretionary cash went to acquisitions and dividends, while net debt expanded to $11.5B.

---

## 5. Probabilities & Expected Value

| Scenario | Value per Share (USD) | 10-Yr Revenue CAGR | Probability | Weighted Value (USD) |
|---|---|---|---|---|
| **Bear Case (M&A Impairment, Organic Fade)** | $131.41 | 4.7% | **20%** | $26.28 |
| **Base Case (Fade to Mid-Single Digit)** | $209.13 | 6.1% | **65%** | $135.93 |
| **Bull Case (Inari Acceleration, Margins Expand)** | $304.40 | 8.0% | **15%** | $45.66 |
| **Expected Value (Weighted)** | **$207.87** | — | **100%** | **$207.87** |

- **SBC-Adjusted Expected Value:** **$205.50** (deducting ~$200M/yr in stock-based dilution).
- **Current Market Price:** **$283.71**.
- **Margin of Safety:** **-36.5%** (Current price trades at a **36.5% premium** over Expected Value).
- **Asymmetry:** Upside to Bull ($304.40 vs $283.71 = +$20.69) vs Downside to Bear ($283.71 vs $131.41 = -$152.30) = **0.14 : 1**. Downside risk is asymmetric.

---

## 6. Disagreements with the Quant
- **None on Core DCF Engine:** The Quant executed a clean model with appropriate adjustments for loaner instrument D&A and acquisition amortization add-backs.
- **Tax Rate Sensitivity:** The Skeptic highlights that using the pooled 17.3% tax rate rather than a normalized 22.5% rate flatters the Quant's Base by ~$14.67/share; Expected Value ($207.87) is robust to this spread.

---

## 7. Downside Catalysts & Signposts
1. **Peripheral Vascular Manufacturing Remediation (Q3/Q4 2026):**
   - *Signpost:* Any extended supply shortage or FDA warning letter regarding Inari/peripheral vascular lines.
2. **CEO Transition Strategy Update (Early 2027):**
   - *Signpost:* Incoming leadership initiating strategic reviews or large restructuring/impairment charges.
3. **Organic Growth Deceleration Below 7%:**
   - *Signpost:* Organic revenue growth prints falling below 7.0% in consecutive quarters.

---

## 8. Verdict Recommendation: TRIM
- **Required Margin of Safety:** 20% for Wide Moat / Stalwart.
- **Entry Below:** EV × (1 − 0.20) = $207.87 × 0.80 = **$166.30**.
- **Exit Above:** EV × 1.30 = $207.87 × 1.30 = **$270.23**.
- **Portfolio Status:** Currently held in active portfolio.
- **Verdict Rule Check:**
  - Current price ($283.71) is **ABOVE the Exit Above threshold ($270.23)**.
  - Reverse DCF demonstrates that today's price discounts 10.2% constant revenue growth for a decade, leaving zero room for execution missteps during the CEO transition.
  - Under portfolio sell discipline rules, `price > EV * 1.30` mandates a **TRIM**.

**Final Verdict:** **TRIM** (Conviction: **HIGH**).
