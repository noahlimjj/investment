# Equity Analysis: ACAD — ACADIA Pharmaceuticals Inc.
As of 2026-10-13 · Price 18.82 USD · Template FULL · Run: `reports/runs/ACAD_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**A commercial rare-disease and CNS biopharma Stalwart reaching financial maturity.** ACADIA expanded revenue at a 19.4% CAGR from FY20 to FY25 ($1.07B in FY25), achieving sustained profitability on the successful launch of Daybue (trofinetide) for Rett syndrome. **Why own it:** ACADIA operates two commercial franchises with >90% gross margins (Nuplazid for Parkinson's disease psychosis and Daybue for Rett syndrome), backed by $498M in liquid cash ($2.89/share) and $0 in funded debt. **What has to happen:** ACADIA must defend Daybue real-world patient persistence in the US while securing international approvals in Europe and Canada and advancing ACP-101 in Prader-Willi syndrome. **What could go wrong:** Daybue causes high rates of gastrointestinal intolerance (diarrhea in >80% of patients), which leads to caregiver discontinuation; if patient dropouts cap Daybue sales below $400M while Nuplazid approaches its 2030 patent expiry, operating earnings will contract sharply.

## 1. Executive Summary & Expected Value
- **Current Price:** $18.82 USD · **12-mo change:** -7.8% (52-week range: $14.40 to $24.80).
- **Bear / Base / Bull:** $8.72 (25%) / $15.51 (55%) / $28.22 (20%). Scenarios model explicit 10-year DCF projections fading commercial exclusivity and pipeline contribution.
- **Expected Value (probability-weighted):** **$16.36 USD** → margin of safety **-15.0%** (downside **-13.1%**).
- **SBC-adjusted Expected Value:** **$15.80 USD** (deducting ~$96M annual stock-based compensation).
- **Price implies (reverse DCF):** a constant 10-year revenue CAGR of ~5.2% at mid-cycle 18.0% operating margins. The tape is balanced between ongoing Daybue ex-US expansion and long-term Nuplazid patent maturity.
- **Asymmetry (upside to Bull : downside to Bear):** 0.93 : 1 ($9.40 upside to Bull vs $10.10 downside to Bear).
- **Recommendation:** **HOLD** (MEDIUM conviction). As an existing holding, the market price ($18.82) sits between Expected Value ($16.36) and the sell discipline exit threshold of $21.26 (EV × 1.30).

## 2. Business Quality (Buffett)
**Moat: Narrow, stable.** ACADIA possesses unique orphan drug exclusivity in Rett syndrome (Daybue is the sole FDA-approved therapy) and established specialty neurology distribution in Parkinson's disease psychosis (Nuplazid). High gross margins (92%–94%) demonstrate commercial pricing power. However, Nuplazid's composition-of-matter exclusivity expires in 2030, limiting franchise duration. **ROIC vs WACC:** Current normalized ROIC of 15.2% comfortably exceeds its 8.50% cost of capital. **Circle of competence:** high predictability in established commercial orphan neurology; medium predictability regarding caregiver persistence for symptomatic treatments with GI side effects.

## 3. GARP & Valuation Matrix
| Metric | Current (FY25/TTM) | 5-Yr Own Avg | Peer Median (JAZZ, BMRN, NBIX, ITCI) |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 12.5x | 18.0x | 13.5x |
| P/E (ttm / fwd) | 8.4x / 20.8x | n/m (past losses) | 18.5x / 16.0x |
| Normalized FCF Yield | 4.8% (on $155M mid-cycle FCF) | negative | 5.2% |
| Net Cash / Market Cap | 15.4% ($498M net cash) | 12.0% | 9.0% |
| ROIC vs WACC | 15.2% vs 8.50% | negative | 12.5% |
| Net Debt / EBITDA | Net Cash ($0 Funded Debt) | Net Cash | Net Cash |
*Note: Price-to-earnings growth ratio is mathematically void because forward earnings are declining from tax-flattered trailing levels.*

## 4. DCF Scenarios
Valuation executed via `02_model.py`. The model evaluates commercial cash flows supported by $497.7M ($2.89/share) in net cash. WACC is 8.50% (US 10y Treasury yield 5.22%, Blume-adjusted beta 0.650, 5.0% ERP). Terminal growth rate is 2.5%, terminal ROIC is 12.0%, and terminal value represents 52.0% of enterprise value in Base.
- **Bear (25%): $8.72 USD.** Daybue GI discontinuations restrict real-world persistence; Nuplazid faces generic erosion post-2030; operating margin 12.0%; 10-year revenue CAGR 1.0%; WACC 9.25%; equity value $1.50B.
- **Base (55%): $15.51 USD.** Daybue expands into Europe and Canada; Nuplazid remains stable through 2030; mid-cycle operating margin 18.0%; 10-year revenue CAGR 3.5%; WACC 8.50%; equity value $2.67B.
- **Bull (20%): $28.22 USD.** Daybue global peak exceeds $700M; ACP-101 approved in Prader-Willi syndrome; operating margin expands to 24.0%; 10-year revenue CAGR 6.0%; WACC 7.75%; equity value $4.86B.

## 5. The Skeptic's Audit
- **Number audit:** 10 financial items audited against SEC filings (10-K accn 0001193125-26-075218 and 10-Q Q2-26). Key confirmations:
  1. *Trailing Earnings Flattery:* Audited trailing GAAP net income ($391.0M), confirming that reported 8.4x trailing P/E was heavily flattered by a one-off non-cash valuation allowance release on deferred tax assets. Operating income was $104.8M. True normalized P/E is ~20x.
  2. *Net Cash Reconciliation:* Confirmed $497.7M in cash and short-term Treasuries with $0 in funded corporate debt.
  3. *Share Count Dilution:* Verified diluted shares reached 172.31M in Q2 2026.
- **Capital Allocation Grade: B**
  - Buffett $1 test is positive since achieving profitability in FY24–FY25.
  - Successfully transitioned into a self-funding commercial biopharma without dilutive equity raises post-2021.
  - Maintained complete balance sheet discipline with $0 in funded debt.
- **Quality of Earnings:** Moderate. Operating cash flow of $109.8M is genuine, but stock-based compensation is elevated (~$96M annually).
- **Bear thesis:** Orphan commercial plateau. Gastrointestinal intolerance caps Daybue persistence, preventing trofinetide from replacing Nuplazid's cash flow when pimavanserin loses patent exclusivity in 2030, while pipeline candidate ACP-101 fails to achieve primary endpoints.
- **Primary Downside Catalysts:**
  1. *Daybue Quarterly Patient Attrition:* Flattening active patient numbers in quarterly disclosures.
  2. *ACP-101 Phase 3 Clinical Trial Readout:* Failure to achieve statistical significance in the COMPASS Prader-Willi trial.
- **Unresolved disagreements (Quant vs Skeptic):** None; Skeptic confirmed that the DCF model properly normalized income taxes.

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** USD-denominated US domestic equity; direct exposure to USD/SGD fluctuations.
- **Dividends:** Zero dividend payout (cash retained for pipeline development), eliminating dividend withholding tax drag.
- **Estate Tax:** US-domiciled equity; subject to US federal estate tax under 26 USC §2104 above the US$60k statutory threshold.
- **Portfolio Weight:** Currently held in active portfolio. Recommendation is to hold the position while monitoring Daybue international commercialization.

## 7. Sources
1. ACADIA Pharmaceuticals Inc. FY2025 Form 10-K Annual Report (SEC accn 0001193125-26-075218).
2. ACADIA Pharmaceuticals Inc. Q2 2026 Form 10-Q Quarterly Report (SEC accn 0001193125-26-333243).
3. ACADIA Pharmaceuticals Q2 2026 Earnings Presentation (August 2026).
4. FRED US 10-Year Treasury Yield (DGS10, October 2026).
5. Quantitative valuation model and DCF run script (`reports/runs/ACAD_2026-10-13/02_model.py`).

VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          18.82 USD
FAIR_VALUE:     16.36 USD
UPSIDE:         -13.1%
ENTRY_BELOW:    13.09 USD
EXIT_ABOVE:     21.26 USD
CONVICTION:     MEDIUM
KEY_RISK:       Daybue real-world GI discontinuations cap Rett syndrome penetration while Nuplazid faces 2030 patent expiry
DATA_WARNINGS:  1
