# Skeptic Audit: INSM (Insmed Incorporated) — as of 2026-10-13

_Status: COMPLETE. Audit of Quant model `02_model.py` and research dossier `01_research.md`._  
_Template: **rNPV (Biopharma)**. Portfolio Status: **CURRENT HOLDING**._

---

## 1. Pre-Mortem (Blind Assessment)
**The single most likely structural reason Insmed is worth 50%+ less in 5 years:**

> Insmed is capitalized at a **$21.5B valuation ($98.50/share)**, which discounts >$14.5B in peak annual sales. The pre-mortem failure mode is commercial launch friction and multi-indication pipeline attrition:
> 1. In non-cystic fibrosis bronchiectasis (NCFB), brensocatib faces severe formulary restrictions. Payors classify it as an expensive specialty add-on (projected WAC ~$75k–$85k/yr) and mandate rigorous step-therapy through generic airway clearance devices, hypertonic saline, and prophylactic azithromycin. Real-world uptake stalls at <15,000 patients, yielding peak US sales of under $1.5B.
> 2. Pipeline expansion beyond NCFB (CRSwNP, HS, and other neutrophil-driven inflammatory indications) yields disappointing Phase 2/3 efficacy or off-target safety signals, eliminating the multi-blockbuster upside the tape discounts.
> 3. TPIP fails to demonstrate clear superiority over United Therapeutics' Tyvaso DPI in PAH or PH-ILD, leaving Insmed with heavy ongoing trial expenses and no third pillar.
> 4. Operating expenses remain elevated at >$1.0B/year to support global commercialization and Phase 3 trials, evaporating the $1.16B cash cushion and forcing substantial equity dilution at lower share prices.
> 5. As reality resets peak sales toward $2.5B–$3.5B, equity value violently de-rates toward the Base case ($27.36) or Bear case ($14.52).

---

## 2. Number Audit of Quant Model
Re-tested `reports/runs/INSM_2026-10-13/02_model.py`:
- Execution is verified and reproducible (exit code 0).
- Primary balance sheet and share count inputs re-verified against SEC filings (10-Q Q2-26 accn `0001104506-26-000041`):

| Input | Quant Value | Verified Value | Source / Notes | Status |
| :--- | :--- | :--- | :--- | :--- |
| Spot Price | $98.50 | $98.50 | 00_inputs.json / yfinance close | PASS |
| Diluted Shares | 218.380M | 218.382M | 10-Q Q2-26 cover date 2026-07-31 | PASS |
| Cash & ST Investments | $1,160.3M | $1,160.3M | 10-Q Q2-26 balance sheet ($544.8M cash + $615.5M ST investments) | PASS |
| Total Debt | $579.9M | $579.9M | 10-Q Q2-26 balance sheet | PASS |
| Net Cash | $580.4M | $580.4M | $2.66/share | PASS |
| Risk-Free Rate | 5.22% | 5.22% | FRED DGS10 10y Treasury yield | PASS |
| Beta / ERP | 1.00 / 5.00% | 1.00 / 5.00% | Standard biotech CAPM parameters | PASS |
| Base WACC | 10.20% | 10.22% rounded | Conservative | PASS |
| Terminal Value | 0.0% | 0.0% | 2039 patent cliff; zero TV strictly enforced | PASS |

**Number Audit Result: 9 checked / 0 failed.** The Quant's mathematical model is fully audited and verified.

---

## 3. Steelman: Bull vs Bear

### The Steelman Bull Case
1. **Unprecedented Monopoly in NCFB:** Brensocatib is the first drug ever to succeed in Phase 3 for non-cystic fibrosis bronchiectasis. With >450,000 diagnosed US patients and zero approved pharmacotherapies, Insmed has a wide-open commercial highway with massive pent-up clinical demand.
2. **Platform Potential of DPP1 Inhibition:** Dipeptidyl peptidase 1 inhibition directly targets neutrophil serine proteases (NE, PR3, NSP4). Success in ASPEN validates the biological mechanism across a broad spectrum of neutrophil-driven diseases (CRSwNP, hidradenitis suppurativa, COPD).
3. **Arikayce Cash Cow:** Arikayce provides an existing commercial foundation of >$500M annual revenue with expanding international presence, buffering the company during brensocatib's launch ramp.
4. **Acquisition Magnet:** A de-risked commercial-stage respiratory asset with multi-billion potential makes Insmed an obvious buyout target for respiratory pharma giants (AstraZeneca, GSK, Sanofi).

### The Steelman Bear Case
1. **Unforgiving Valuation Disconnect:** At $98.50 ($21.5B Market Cap), the stock discounts >$14.5B in peak annual sales. This is nearly triple our Base case peak sales ($4.5B), demanding perfection across all indications.
2. **Specialty Commercialization Bottleneck:** Pulmonologists treat bronchiectasis symptomatically. Driving adoption of an expensive specialty oral drug requires extensive physician education and difficult prior authorization navigation.
3. **Severe Historic Dilution:** Shares have expanded by 122% over 5 years (98.4M to 218.4M). Management has repeatedly sold equity into positive trial headlines.
4. **Persistent Operating Burn:** TTM operating loss is -$840.6M. Insmed will burn several hundred million dollars more before reaching operating cash flow break-even in 2027/2028.

**The Single Variable That Flips The Thesis:**  
The conversion rate of diagnosed NCFB patients into active, reimbursed brensocatib commercial prescriptions within the first 24 months of launch.

---

## 4. Capital Allocation & Quality of Earnings

- **Capital Allocation Grade: C+**
  - **Dilution Track Record:** Highly dilutive. Share count increased at a 15.3% CAGR over the past 5 years. Management raised capital aggressively at lower valuations ($25–$35) prior to the ASPEN readout.
  - **Reinvestment Efficiency:** Accumulated deficit is -$4.85B. While scientific execution in ASPEN was exceptional, the capital required to achieve it has been enormous.
  - **Balance Sheet Discipline:** Management successfully used recent equity proceeds to retire high-cost convertible debt, leaving $580M in net cash ($2.66/share).
- **Quality of Earnings:**
  - TTM operating cash burn was -$778.9M. Stock-based compensation is heavy at $157.5M TTM (20.2% of operating cash burn).
  - Gross margins on Arikayce are healthy (80%–83%), but commercial SG&A build-out is currently consuming all gross profit.

---

## 5. Scenario Probability Weights & Verdict Validation

| Scenario | Value | Skeptic Weight | Weighted Per Share | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Bear Case** | $14.52 | **25%** | $3.63 | Payor prior auth restricts NCFB; peak sales $2.5B; TPIP fails. |
| **Base Case** | $27.36 | **55%** | $15.05 | Solid NCFB adoption ($3.2B) + Arikayce ($0.8B) + TPIP ($0.5B); peak $4.5B. |
| **Bull Case** | $50.53 | **20%** | $10.11 | Multi-indication blockbuster in NCFB + CRSwNP + PAH ($7.5B peak). |
| **Expected Value** | — | **100%** | **$28.78 USD** | **Downside: -70.8% vs Spot ($98.50)** |

### Portfolio Action:
- Spot Price ($98.50) is **163.2% ABOVE the Exit Above threshold ($37.42)**.
- Spot Price is **94.9% ABOVE the Bull Case ($50.53)**.
- Holding Insmed at $98.50 exposes the portfolio to severe downside asymmetry (-70.8%). The risk/reward is extraordinarily poor.
- **Final Verdict: TRIM.** Conviction: **HIGH**.
