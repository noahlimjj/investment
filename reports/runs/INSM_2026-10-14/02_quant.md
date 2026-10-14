<!-- pipeline:value-quant -->
# Stage 2: Value Quant Valuation — Insmed Incorporated (INSM)
**As of Date:** 2026-10-14  
**Spot Price:** $96.79 USD | **Shares Diluted:** 218.38M  
**Template:** rNPV (Commercial / Pipeline Biopharma)  
**Executed Model:** `reports/runs/INSM_2026-10-14/02_model.py`

---

## 1. Valuation Methodology & Capital Structure
- **Asset Class Routing:** Commercial / Clinical Biopharma (`rNPV` template).
  - Traditional DCF terminal value models are inappropriate due to patent loss of exclusivity (LOE) on lead asset brensocatib in 2039. Terminal value is set strictly to **0.0%**.
  - Moat, PEG, and Owner Earnings multiples are VOID given the negative trailing earnings base (-$841M TTM operating loss).
- **Cost of Capital (WACC):**
  - Risk-free rate (US 10-Yr Treasury): 5.22% (FRED DGS10).
  - Biopharma Beta: 1.00.
  - Equity Risk Premium: 5.00%.
  - Cost of Equity / WACC: **10.20% Base**, **11.00% Bear**, **9.50% Bull**.
- **Net Cash per Share:** $1.160B liquid cash − $0.580B convertible debt = **+$580.4M Net Cash ($2.66 / share)**.

---

## 2. Multi-Scenario rNPV Valuation Results

| Scenario | Weight | Peak Revenue | Operating Margin | WACC | Equity Value | Fair Value / Share | Upside vs $96.79 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bear Case** | 25% | $2.50B | 30.0% | 11.00% | $3.17B | **$14.52 USD** | -85.0% |
| **Base Case** | 55% | $4.50B | 36.0% | 10.20% | $5.98B | **$27.36 USD** | -71.7% |
| **Bull Case** | 20% | $7.50B | 42.0% | 9.50% | $11.03B | **$50.53 USD** | -47.8% |

- **Probability-Weighted Expected Value:** **$28.78 USD**
- **Margin of Safety:** **-236.3%**
- **Upside to Fair Value:** **-70.3%**
- **Buy Trigger (Entry Below):** **$20.15 USD** (30% discount to fair value)
- **Exit Above Trigger:** **$37.42 USD** (30% premium to fair value)

---

## 3. The Reverse DCF (What Must Be True?)
- **Current Enterprise Value:** $20.56B ($21.14B Market Cap − $0.58B Net Cash).
- **Implied Peak Sales:** To justify today's spot price of **$96.79 USD**, Insmed must generate **$17.15 Billion in annual peak sales** across its commercial life.
- **Plausibility Check:**
  - $17.15B peak sales would rank brensocatib alongside Keytruda and Ozempic as one of the top 3 selling pharmaceutical assets in history.
  - Base case epidemiological models for NCFB cap peak addressable sales at ~$3.2B.
  - Spot price trades at **3.8x the Base Case peak revenue** ($17.15B vs $4.50B) and **1.9x the Bull Case fair value** ($96.79 vs $50.53).
- **Asymmetry:** Upside to Base Case is -71.7%; downside to Bear Case is -85.0%. Asymmetry is 0.0:1 in favor of the downside.

---

## 4. Valuation Matrix (GARP Context)
- **Trailing P/E:** VOID (negative earnings).
- **Forward P/E:** VOID.
- **PEG:** VOID (negative base).
- **EV / Sales:** 18.1x TTM (vs biopharma peer median of 8.5x).
- **Price / Net Cash:** 36.4x.
