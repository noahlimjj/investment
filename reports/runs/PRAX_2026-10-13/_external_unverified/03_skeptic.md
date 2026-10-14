# Skeptic Audit: PRAX (Praxis Precision Medicines, Inc.) — as of 2026-10-13

_Status: COMPLETE. Audit of Quant model `02_model.py` and research dossier `01_research.md`._  
_Template: **rNPV (Clinical Neuroscience)**. Portfolio Status: **CURRENT HOLDING**._

---

## 1. Pre-Mortem (Blind Assessment)
**The single most likely structural reason Praxis is worth 50%+ less in 5 years:**

> Praxis is a pre-revenue clinical biotech capitalized at a **$6.94B valuation ($248.69/share)**, which discounts >$5.5B in peak annual commercial sales. The pre-mortem failure mode is clinical endpoint failure and subjective trial noise inherent in CNS drug development:
> 1. In essential tremor (ET), Phase 3 Essential3 relies on the TETRAS functional performance scale. ET trials are notoriously susceptible to high placebo responses, high day-to-day symptom variability, and subjective evaluator noise. If ulixacaltamide misses statistical significance on the primary functional endpoint or exhibits intolerable CNS adverse effects (ataxia, somnolence, dizziness), the program is dead.
> 2. PRAX-628's excitement is based on a tiny Phase 2a photo-paroxysmal response (PPR) surrogate study. Translating EEG photoparoxysmal suppression into durable, statistically significant seizure reduction in large heterogeneous Phase 2b/3 focal onset epilepsy trials has a >60% historical failure rate. Furthermore, the market is crowded with generic sodium channel blockers (lacosamide, oxcarbazepine) and established branded agents (cenobamate / Xcopri).
> 3. With zero commercial revenues and ongoing cash burn exceeding $300M annually, any Phase 3 clinical stumble eliminates the multi-billion valuation, collapsing the stock by 70%–85% toward the net cash floor ($27.11/share).

---

## 2. Number Audit of Quant Model
Re-tested `reports/runs/PRAX_2026-10-13/02_model.py`:
- Execution is verified and reproducible (exit code 0).
- Primary balance sheet and share count inputs re-verified against SEC filings (10-Q Q2-26 accn `0001689548-26-000083`):

| Input | Quant Value | Verified Value | Source / Notes | Status |
| :--- | :--- | :--- | :--- | :--- |
| Spot Price | $248.69 | $248.69 | 00_inputs.json / yfinance close | PASS |
| Diluted Shares | 27.920M | 27.920M | 10-Q Q2-26 cover date 2026-07-31 | PASS |
| Cash & ST Investments | $758.6M | $758.6M | 10-Q Q2-26 balance sheet ($474.8M cash + $283.8M ST investments) | PASS |
| Total Debt | $1.1M | $1.1M | 10-Q Q2-26 balance sheet (capital lease obligations) | PASS |
| Net Cash | $757.5M | $757.5M | $27.11/share | PASS |
| Risk-Free Rate | 5.22% | 5.22% | FRED DGS10 10y Treasury yield | PASS |
| Beta / ERP | 1.00 / 5.00% | 1.00 / 5.00% | Standard biotech CAPM parameters | PASS |
| Base WACC | 10.20% | 10.22% rounded | Conservative | PASS |
| Terminal Value | 0.0% | 0.0% | 2039 patent cliff; zero TV strictly enforced | PASS |

**Number Audit Result: 9 checked / 0 failed.** The Quant's mathematical model is audited and validated.

---

## 3. Steelman: Bull vs Bear

### The Steelman Bull Case
1. **Unmet Need in Essential Tremor:** Essential tremor afflicts ~7 million Americans with no new pharmacotherapy in half a century. Propranolol has poor tolerability and efficacy. If ulixacaltamide delivers robust functional tremor control, it commands immediate first-line status.
2. **Next-Generation Nav Selectivity:** PRAX-628's functional selectivity targets hyperactive epileptic firing while avoiding tonic inhibition of basal neurological circuits, potentially delivering unmatched efficacy without the sedation and cognitive blunting of legacy anti-epileptic drugs.
3. **Pristine Balance Sheet:** With $758.6M in liquid investments, $0 funded debt ($1.1M lease obligations), and $27.11/share in net cash, Praxis is fully funded through all registrational milestones with no near-term financing overhang.
4. **Acquisition Candidate:** Pure-play CNS biotechs with Phase 3 de-risked assets (like Cerevel, acquired by AbbVie for $8.7B) command enormous acquisition premiums from pharma majors looking for neuroscience growth.

### The Steelman Bear Case
1. **Extreme Valuation Disconnect:** At $248.69 ($6.94B Market Cap), the stock has gained +363% over the trailing 12 months, discounting >$5.5B in peak annual sales.
2. **High Attrition in CNS Trials:** Neuroscience Phase 3 clinical trials suffer from severe placebo effects and high endpoint variability. A single primary endpoint miss in Essential3 permanently derails the valuation.
3. **Pre-Revenue Binary Risk:** Praxis has $0 commercial sales. The entire enterprise value ($6.19B) consists of clinical hope without commercial validation.
4. **Commercial Infrastructure Gap:** Commercializing in outpatient neurology requires a substantial specialized sales force, eating heavily into operating margins during the first 3–4 years of commercial launch.

**The Single Variable That Flips The Thesis:**  
The statistical significance and clinical magnitude of ulixacaltamide on the primary TETRAS endpoint in Phase 3 Essential3 without tolerability-driven dropouts.

---

## 4. Capital Allocation & Quality of Earnings

- **Capital Allocation Grade: C**
  - **Dilution Track Record:** Highly dilutive. Share count increased from 4.8M to 27.9M over 5 years (split-adjusted). Management has aggressively sold equity into clinical pipeline run-ups.
  - **Accumulated Deficit:** Accumulated deficit stands at -$1.32B with $0 in commercial product sales generated.
  - **Capital Preservation:** Management maintained financial discipline by avoiding dilutive debt or toxic royalty financing, leaving the balance sheet carrying $0 funded debt ($1.1M lease obligations) and $757.5M in net cash ($27.11/share).
- **Quality of Earnings:**
  - TTM operating cash burn was -$305.1M. Stock-based compensation is $45.8M TTM (15.0% of cash burn).
  - Cash runway of ~2.5 years protects the company from emergency dilutive financing during pivotal Phase 3 trials.

---

## 5. Scenario Probability Weights & Verdict Validation

| Scenario | Value | Skeptic Weight | Weighted Per Share | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Bear Case** | $47.77 | **30%** | $14.33 | Phase 3 ET trial mixed/narrow; PRAX-628 attrition; peak sales $0.8B. |
| **Base Case** | $117.96 | **50%** | $58.98 | Ulixacaltamide approved in ET ($1.5B) + PRAX-628 in epilepsy ($1.2B); peak $2.7B. |
| **Bull Case** | $233.36 | **20%** | $46.67 | Blockbusters in ET ($2.5B) and refractory epilepsy ($2.5B); peak $5.0B. |
| **Expected Value** | — | **100%** | **$119.98 USD** | **Downside: -51.8% vs Spot ($248.69)** |

### Portfolio Action:
- Spot Price ($248.69) trades **59.4% ABOVE the Exit Above threshold ($155.98)**.
- Spot Price trades **6.6% ABOVE the Bull Case ($233.36)**.
- Praxis has delivered a sensational +363% rally. However, holding a pre-revenue clinical biotech at a price exceeding its most optimistic Bull case violates all disciplined GARP principles.
- **Final Verdict: TRIM.** Conviction: **HIGH**.
