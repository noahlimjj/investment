# Skeptic Audit: MDGL (Madrigal Pharmaceuticals, Inc.) — as of 2026-10-13

_Status: COMPLETE. Audit of Quant model `02_model.py` and research dossier `01_research.md`._  
_Template: **rNPV (Single-Asset Biopharma)**. Portfolio Status: **CURRENT HOLDING**._

---

## 1. Pre-Mortem (Blind Assessment)
**The single most likely structural reason Madrigal is worth 50%+ less in 5 years:**

> Madrigal is a single-asset company priced at a **$10.5B valuation ($455.53/share)**, discounting >$6.8B in peak annual sales. The pre-mortem failure mode is commercial saturation and therapeutic disintermediation:
> 1. Next-generation incretin/GLP-1 therapies (tirzepatide, CagriSema, oral orforglipron) achieve robust metabolic weight loss and prevent progression of metabolic dysfunction, capturing the top of the funnel at primary care before patients reach hepatologists.
> 2. Second-generation THR-beta agonists and FGF21 analogs (pegozafermin, efruxifermin) enter the clinic with comparable or superior fibrosis regression data, forcing commercial payors to institute aggressive rebate demands, compressing net realized price from ~$45k/year to <$25k/year.
> 3. Rezdiffra real-world compliance falters due to gastrointestinal adverse events (diarrhea in ~30% of clinical trial patients). Peak US sales stall under $2.2B, operating margins fail to expand past 32%, and equity value violently compresses toward the Bear case ($128.54) or net cash floor ($22.07/share).

---

## 2. Number Audit of Quant Model
Re-tested `reports/runs/MDGL_2026-10-13/02_model.py`:
- Execution is verified and reproducible (exit code 0).
- Primary inputs re-verified against SEC filings (10-Q Q2-26 accn `0001628280-26-050845`):

| Input | Quant Value | Verified Value | Source / Notes | Status |
| :--- | :--- | :--- | :--- | :--- |
| Spot Price | $455.53 | $455.53 | yfinance close 2026-10-13 | PASS |
| Diluted Shares | 23.104M | 23.104M | 10-Q Q2-26 cover and balance sheet | PASS |
| Cash & Investments | $850.0M | $850.0M | 10-Q Q2-26 Note 3 & balance sheet | PASS |
| Term Debt (Hercules) | $340.0M | $339.9M | 10-Q Note 7 credit facility | PASS |
| Net Cash | $510.0M | $510.1M | $22.07/share | PASS |
| Risk-Free Rate | 5.22% | 5.22% | FRED DGS10 10y Treasury yield | PASS |
| Beta / ERP | 1.00 / 5.00% | 1.00 / 5.00% | Biotech standard CAPM | PASS |
| Base WACC | 10.20% | 10.22% rounded | Conservative | PASS |
| Terminal Value | 0.0% | 0.0% | LOE 2038; zero terminal value strictly enforced | PASS |

**Number Audit Result: 9 checked / 0 failed.** The Quant's model calculations are verified.

---

## 3. Steelman: Bull vs Bear

### The Steelman Bull Case
1. **Entrenched First-Mover Monopoly in MASH:** Rezdiffra is the only FDA-approved oral treatment for MASH fibrosis (F2–F3). Madrigal successfully navigated commercial formulary access across UHC, CVS Caremark, and Cigna without requiring invasive liver biopsies.
2. **Complementary Synergy with GLP-1s:** Rather than competing, hepatologists are adopting Rezdiffra as a liver-directed oral backbone in combination with GLP-1s, where resmetirom delivers targeted THR-beta antifibrotic activity without muscle mass loss.
3. **Ex-US Geographic Expansion:** EMA review is advancing toward 2026 approval, opening access to European markets where incretin reimbursement for MASH is heavily restricted.
4. **Operating Leverage:** Gross margins are pristine (94%–96%). As revenue scales past $1.5B in 2027, fixed commercial infrastructure delivers rapid margin expansion toward 40%+.

### The Steelman Bear Case
1. **Extreme Valuation Disconnect:** At $455.53, the stock trades at 47.3x forward earnings and EV/Sales >9.5x, requiring peak sales of $6.8B–$7.0B to break even on an intrinsic DCF basis.
2. **Class Crowding & Price War:** Eli Lilly, Novo Nordisk, Akero, and 89bio have late-stage Phase 3 MASH programs. Payor formulary exclusive contracts will demand 40%+ rebates once a second entrant is approved.
3. **Single-Asset Binary Risk:** Madrigal has no pipeline diversification. 100% of the firm's enterprise value rests on resmetirom. Any post-marketing hepatotoxicity or clinical failure wipes out equity value.
4. **Finite Commercial Clock:** Hatch-Waxman exclusivity and composition patents end in 2038. With zero terminal value post-2038, the window to generate cash flows to justify a $10.5B valuation is closing each quarter.

**The Single Variable That Flips The Thesis:**  
The durability of net realized price per patient (whether it stays above $40,000/yr or gets negotiated down toward $20,000/yr under payor tiering and competitive entrants).

---

## 4. Capital Allocation & Quality of Earnings

- **Capital Allocation Grade: B**
  - **Financing Discipline:** Replaced early clinical equity dilution with structured debt (Hercules facility) and commercial revenue generation. Dilution has been contained to ~28% cumulative over 5 years while commercializing a multi-billion blockbuster.
  - **Reinvestment Return:** Generated +4.8x market value created per $1 of paid-in capital ($2.1B accumulated deficit vs $10.5B market cap).
  - **Insider Transactions:** static insider ownership is ~4.6% (data warning notes institutional pct vendor artifact >1.0). Static insider holdings provide adequate alignment, though recent Form 4 open-market transactions represent modest executive diversification sales.
- **Quality of Earnings:**
  - GAAP net losses are rapidly inflecting: FY24 -$465.9M to FY25 -$288.3M.
  - Operating cash burn dropped from -$455.6M (FY24) to -$189.6M (FY25).
  - Net cash of $510M ensures zero external dilutive financing is needed before cash-flow self-sufficiency.

---

## 5. Scenario Probability Weights & Verdict Validation

| Scenario | Value | Skeptic Weight | Weighted Per Share | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Bear Case** | $128.54 | **25%** | $32.14 | Payor rebating and GLP-1 encroachment limit peak to $2.2B. |
| **Base Case** | $239.36 | **55%** | $131.65 | Solid oral backbone adoption, peak sales $3.8B by 2031. |
| **Bull Case** | $374.18 | **20%** | $74.84 | Global blockbuster adoption, peak sales $5.2B. |
| **Expected Value** | — | **100%** | **$238.62 USD** | **Downside: -47.6% vs Spot ($455.53)** |

### Portfolio Action:
- Spot Price ($455.53) trades **46.8% ABOVE the Exit Above threshold ($310.21)**.
- Spot trades **21.7% ABOVE the Bull Case ($374.18)**.
- Madrigal is an active holding in the portfolio. Holding a single-asset biotech at nearly 2x its fundamental expected value violates every GARP risk boundary.
- **Final Verdict: TRIM.** Conviction: **HIGH**.
