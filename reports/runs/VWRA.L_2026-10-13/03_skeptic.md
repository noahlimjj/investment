<!-- pipeline:value-skeptic -->
# Skeptic audit: VWRA.L (as of 2026-10-13)

Template: FUND. Held (designated core). Price 193.34 USD (yfinance close 2026-10-13, re-pulled from price history). Index trailing P/E 21.0x (Vanguard, 31 Aug 2026, re-fetched). 12-month change +18.1% (recomputed). Tape check: the index is at 21x trailing after +81.0% over 3 years, with the US 10y at 5.22%. Its earnings yield (4.76%) is **below** the Treasury yield. Any narrative below that implies "cheap" would contradict the tape. None does.

Corrected model: `reports/runs/VWRA.L_2026-10-13/03_rerun.py`, executed. It is `02_model.py` with rf = 5.22%, plus a Skeptic §8. Quoted outputs below come from that run.

Adapted per orchestrator: §3 is index-level earnings quality, not SBC. §4 is a structure/cost audit, not capital allocation. The margin-of-safety table does not drive the verdict (SKILL.md, FUND template).

## 1. Pre-mortem (written before reading the model)
Recorded at 21:26 SGT before `02_quant.md` was opened. Verbatim substance:

> The most likely structural reason VWRA is worth materially less (in real terms) in 5 years is a **valuation/discount-rate squeeze on a market whose earnings are increasingly one trade**.
> - Of the top 10, NVDA + TSMC + AVGO + MU = 9.06% are AI-capex *suppliers*. MSFT + AMZN + GOOGL (two lines) + META = 10.30% are the AI-capex *spenders*. About a fifth of the index rests on one capex cycle in which the spenders' capex is the suppliers' revenue.
> - If AI capex returns disappoint, semis' earnings fall from peak margins **and** multiples compress from ~21x (Vanguard) / 23–25x (other vendors), with CAPE ~29 (proxy).
> - With the 10y at 5.22%, the earnings yield (4.76%) is below the risk-free rate.
> - Fund-specific (non-market) structural risk is low. The vehicle cannot go bust. Only a change to the tax treaty or situs rules would damage the wrapper itself.
> - The bear case is a lost decade, not a permanent loss.

## 2. Number audit
FAIR_VALUE for a FUND is the base 10-yr net annualised return (Quant: **6.30%/yr**). "Δ FV" is the effect on that figure. Where relevant it also shows the effect on the Quant's "hurdle-equivalent value" (HEV: the price at which a scenario earns exactly k).

| # | Input | Quant value | Verified value | Source | Status | Δ FV |
|---|---|---|---|---|---|---|
| 1 | Price | 193.34 USD | 193.34 (close 2026-10-13) | yfinance `history()` re-pull | PASS | 0 |
| 2 | NAV | 193.64 (12 Oct) | not re-fetched. Price/NAV −0.155% is consistent with a 1-day gap | Vanguard UK (Researcher) | PASS (plausible) | 0 |
| 3 | Shares / net debt / base revenue | n/a | n/a (fund; fund-level borrowing UNKNOWN) | – | n/a | – |
| 4 | Starting P/E | 21.0x | 21.0x fund and benchmark, at 31 Aug 2026. Price is −1.1% since then, so ≈20.8x on unchanged EPS | Vanguard UK page, re-fetched 2026-10-13 | PASS. Temporal drift is minor. Comparability: vendor definitions differ (MSCI 23.24x) | base 0. Bear −1.0 pp if the 23.24x definition applies (output 8g) |
| 5 | Starting-P/E sensitivity (§G row 1, ranked #1 load-bearing) | ±10% → +11.0% / −9.0% | A definitional P/E error moves the base by **0**, because the exit P/E follows the same vendor definition (output 8g). The ±10% row holds exit at 21x, so it is really an exit-P/E (re-rating) test mislabelled as measurement | recomputed | **FAIL: model fidelity** (mis-specified test; ranking wrong) | 0 on FV. Corrects the ranking: exit P/E is #1 |
| 6 | Hurdle k / rf | 8.00% floor (10y UNKNOWN) | rf **5.22%** (FRED DGS10, 2026-10-08). CAPM k = rf + 5% = **10.22%**. The floor no longer binds | FRED CSV, fetched and read (series ran 4.79% on 1 Sep to 5.31% on 5 Oct) | **FAIL: temporal / source** (input was UNKNOWN and is now sourced) | FV 0 (a return does not depend on k). HEV base 165.02 → **134.64 (−18.4%)**. M3 centre 183.52 → **118.02 (−35.7%)**. Re-run as `03_rerun.py` |
| 7 | Terminal g cap | 4% = min(4%, rf) | min(4%, 5.22%) = 4% | recomputed | PASS | 0 |
| 8 | Per-share EPS growth | 5.0% (ASSUMPTION) | envelope recomputed: 3.17% to 11.42%. Arithmetic correct | output §1 | PASS (arithmetic). Judgement in §7 | ±0.5 pp per ±1 pp g |
| 9 | Exit P/E (base) | 21.0x (no re-rating) | ASSUMPTION. At the sourced rf, the Quant's own M3 gives justified 12.8x (k 10.22%) to 15.3x (k 9.22%) at g = 4% (output 8d) | recomputed | DISPUTED (internal consistency), kept in §7 | 19x exit → 5.26% (−1.04 pp) |
| 10 | Look-through ROE | 17.14% | 3.6 / 21.0 = 17.14% | recomputed | PASS | 0 |
| 11 | Dividend yield | 1.59% (MSCI ACWI proxy, 31 Jul) | FTSE All-World yield UNKNOWN. Vanguard shows an unlabeled 1.32% (30 Sep) | dossier §8 | COMPARABILITY (flagged by Quant) | at 1.32%: 6.06% (−0.24 pp) |
| 12 | TER | 0.14% | 0.14% | Vanguard UK page, re-fetched | PASS | 0 |
| 13 | US dividend WHT at fund level | 15% (user-stated, unverified) | **15% verified.** Art. 10(2)(b) "15 percent of the gross amount of the dividends in all other cases". Art. 4(1)(d): an Irish Collective Investment Undertaking is a treaty resident. Art. 23(2)(d)(i) LOB: units listed and regularly traded on a recognized exchange, London included | US–Ireland treaty text, irs.gov/pub/irs-trty/ireland.pdf | PASS (premise now primary-sourced). Vanguard's own disclosure that it claims the rate was not read | 0 |
| 14 | WHT drag formula | DY × US weight × 15% | US dividends are a smaller share of index dividends than the US cap weight, because the US yield is lower. Non-US WHT leakage is omitted. Net sign UNKNOWN | formula review | MODEL FIDELITY (minor) | about ±0.1 pp (+0.10% leakage → 6.20%) |
| 15 | US weight | 61.68% | not re-fetched. justETF conflict 59.77% | Vanguard (Researcher) | not re-checked, non-load-bearing | ±0.01 pp |
| 16 | 1y / 3y / 5y price change | 18.1 / 81.0 / 72.9% | 18.1 / 81.0 / 72.9% (163.70 / 106.84 / 111.83 → 193.34) | yfinance history recompute | PASS | – |
| 17 | Top-10 weight | 23.6% | 23.60% (sum of 10 lines) | facts recompute | PASS | – |
| 18 | Formulas: Bogle decomposition, HEV = P·((1+r)/(1+k))^10, reverse solve, justified P/E = (1−g/ROE)(1+g)/(k−g) | – | all re-derived. E.g. k 8%, g 4% → 19.93x | recomputed | PASS. Terminal share 100% by construction, flagged by the Quant | – |

**Result: 18 checked, 2 failed (#5 model fidelity, #6 temporal/source), 2 minor flags (#11, #14). FAIR_VALUE (base 6.30%/yr) is unchanged.** Every k-dependent "value" falls sharply once the real rf is used: HEV base −18.4%, M3 centre −35.7%. Both are >5%, so the model was re-run.

Web spot-checks used (5): FRED DGS10; US–Ireland treaty; 26 USC §2104(a) together with the IRS nonresident estate page; Vanguard product page; FTSE All-World factsheet (search failed, so the yield stays UNKNOWN).

## 3. Quality of earnings (index level)
- **SBC:** index-level SBC as % of OCF or revenue is UNKNOWN. Whether Vanguard's P/E uses GAAP EPS (SBC expensed) or operating EPS is also UNKNOWN. M2 uses per-share EPS growth, so dilution net of buybacks is captured once. No double count, no omission. An SBC-adjusted fair value is not computable for a fund. If index EPS is "operating" and excludes SBC, the true P/E is higher than 21x, and the bear moves toward the 23.24x case (−0.28%/yr, output 8g).
- **Earnings above trend:** CAPE (proxy 29.12) / P/E 21.0 = 1.39x (1.25x on the MSCI P/E). Current EPS sits above its 10-yr real average by more than normal growth would explain. The base grows 5% from this elevated level with no reset. A 10% reset spread over 10 years cuts the base to **5.20%/yr** (output 8f).
- **Accruals at the index level (mechanism; magnitude UNKNOWN):** the top-10 "spenders" are carrying capex well above depreciation. That flatters current EPS relative to FCF, and a depreciation wave becomes a future EPS headwind. The "suppliers" (9.06% of the fund) book that capex as revenue at what may be peak margins. Both effects point the same way: trailing EPS is cyclically flattered.
- **Concentration (recomputed):**
  - Top 10 = 23.60%.
  - AI-semis suppliers = 9.06%. Platforms/hyperscalers = 10.30%. Apple 4.24%.
  - The top 10 ex-TSMC are 35.5% of the US sleeve.
  - Tech 36.04% (justETF only, coarse).
  - "3,784 holdings" overstates diversification. In practice this is a ~62% US large-cap fund with a heavy AI tilt.
- **Overlap with the user's book (memory, not re-verified):** TSM (1.70% in the fund), SK Hynix and SK Square (Korea 2.50%), and Micron (1.00%, held through the fund). Direct semis holdings stack on top of the fund's AI-semis exposure. Look-through totals are UNKNOWN because the direct-position sizes are not in this run.

## 4. Structure and cost audit (replaces capital allocation)
| Item | Finding | Source | Status |
|---|---|---|---|
| TER | 0.14% | Vanguard UK page (re-fetched 2026-10-13) | Verified |
| Peer TER / TD (better-structured substitute?) | **UNKNOWN**: not sourced this run | – | Open. It is the only legitimate TRIM trigger under FUND rules |
| Tracking difference 1/3/5y | **UNKNOWN**. Tracking error 0.07 / 0.07 / 0.08% (volatility, not level). Indicative TD 0.02%/yr (low-reliability third party) | Vanguard; trackingdifferences.com | Open |
| Spread / liquidity | about 0.01% snapshot; fund AUM 87.29B USD | yfinance; Vanguard | adequate |
| Domicile / legal form | Ireland, Vanguard Funds PLC, UCITS | Vanguard page | Verified |
| US dividend WHT | 15% at fund level (treaty Art. 10(2)(b), Art. 4(1)(d), LOB 23(2)(d)(i)), vs 30% statutory | treaty text (IRS) | **Verified** (primary) |
| Non-US dividend WHT | leakage on Japan, Switzerland and other dividends: UNKNOWN, not modelled | – | Open, about ≤0.1 pp |
| US estate-tax situs | **Not US-situs.** 26 USC §2104(a): stock held by a nonresident non-citizen is US property "only if issued by a domestic corporation". VWRA's issuer is an Irish PLC. IRS: Form 706-NA is required when US-situated assets exceed **$60,000**, and US-situs examples include "Stock of corporations organized in or under U.S. law" | law.cornell.edu/uscode/text/26/2104; irs.gov "Some nonresidents with U.S. assets must file estate tax returns" | **Verified** (primary) |
| Distribution | accumulating, so no investor-level distribution event | Vanguard | Verified |

**Capital Allocation Grade: n/a (fund). Structure grade: A (provisional).** Domicile, WHT and situs are optimal for a Singapore-resident investor, with the claims now verified from primary law. TER is low. The grade is provisional only because peer TER and tracking difference are UNKNOWN.

**$1 test / buybacks / M&A / insiders:** not applicable to a fund. Insider activity: UNKNOWN (no transaction data, and not meaningful).

**Structural finding for the portfolio (the actionable item):**
- By the same §2104(a) rule, **VXUS (and VOO, if still held) are US-situs.** Their issuers are US-registered funds, which are domestic issuers. Both count toward the $60k threshold.
- Their distributions to a Singapore nonresident carry the 30% US WHT (AGENTS.md investor-fit premise; not re-verified this run). For VXUS that sits on top of foreign-source WHT.
- VWRA is the better-structured substitute for VXUS's ex-US sleeve. Under the FUND rules, any "TRIM" belongs on VXUS/VOO, not on VWRA. This is an allocation question for the orchestrator.

## 5. Probabilities & expected value
**Outside view / base rate used:**
- Bogle/earnings-yield anchor: long-run real return ≈ starting earnings yield. Here that is 4.76% gross (4.47% net), or 3.43% (3.15% net) on the CAPE proxy.
- The Quant base (6.30% nominal) matches the E/P anchor if inflation is ≈1.8%, and the CAPE anchor if inflation is ≈3.2%. Inflation is UNKNOWN. So the base is inside the outside-view band, not above it.
- Reverse anchor (output 8b): to merely match Treasuries at a constant 21x, index per-share EPS must compound **3.92%/yr**. To earn UST + 4%, it needs **7.92%/yr**. To earn CAPM k, **8.92%/yr**. Sustaining ~8–9% per-share EPS growth for 10 years from above-trend margins is not the typical outcome for a ~4,000-stock global index.
- Lost-decade outcomes like the bear (≈0–1%/yr nominal) are historically associated with high starting valuations (the 2000–09 decade being the obvious case). So I weight the bear above what I would at average valuations. This is a judgement prior, not a sourced frequency.

| Scenario | 10-yr net return | Price yr 10 | ERP vs 5.22% | p |
|---|---|---|---|---|
| Bear (3% g, exit 15x, DY 1.40%) | 0.72%/yr | 207.77 | −4.50% | **25%** |
| Base (5% g, exit 21x, DY 1.59%) | 6.30%/yr | 356.26 | +1.08% | **55%** |
| Bull (7.5% g, exit 24x) | 10.25%/yr | 512.89 | +5.03% | **20%** |

- **Expected value:**
  - E[price yr 10] = **350.47**. That is **6.13%/yr** wealth-weighted (5.70%/yr return-weighted).
  - Implied ERP: **+0.91%** over the 10y UST.
  - Sensitivity of weights: 20/60/20 gives 6.35%; 30/50/20 gives 5.90%.
- **Implied ERP (orchestrator request):**
  - Base 6.30% − 5.22% = **+1.08%**. Probability-weighted **+0.91%**.
  - Perpetual market-implied k at 21x (ROE 17.1%, g 4%) = 7.80%, so ERP **+2.58%**. At g 3% it is +1.83% (output 8c).
  - **This is thin.** It is well below the 5% ERP the Quant's own CAPM assumes. Holders are being paid about 1 pp/yr over a 10-yr Treasury to take equity risk, before USD/SGD drift (UNKNOWN; ±1%/yr = ×1.105 / ×0.904 on the 10-yr SGD outcome).
- **Margin of safety:** n/a under the FUND template. For information (output 8e):

  | k | EV of HEV | MoS | Asymmetry |
  |---|---|---|---|
  | CAPM 10.22% | 132.45 | **−46.0%** | −0.53 |
  | Quant's 8% floor | 162.33 | −19.1% | −0.32 |
  | Bond parity 5.22% | 210.70 | **+8.2%** | +0.25 |

  The fund beats Treasuries in expectation, but not a conventional equity hurdle.

## 6. Bear thesis & downside catalysts
**Pre-mortem revisited:** the model confirms it. No recession is needed for a disappointing decade. A modest 10% earnings normalisation plus a partial de-rating to 19x gives **4.17%/yr, an ERP of −1.05%** (output 8f). That is below the Treasury yield the user can lock in today. It is a plausible path, not a tail.

1. **AI-capex cycle rollover** (hits the 9.06% suppliers directly, then the 10.30% spenders' depreciation).
   - Signposts: the combined capex guidance of MSFT/AMZN/GOOGL/META in quarterly filings, and NVIDIA's YoY revenue growth.
   - Threshold that confirms it: two consecutive quarters of lower combined capex guidance, or NVIDIA quarterly revenue down YoY.
2. **Rate squeeze / de-rating.** The 10y rose from 4.79% (1 Sep) to 5.31% (5 Oct) and was 5.22% on 8 Oct, while the E/P is 4.76%.
   - Signposts: FRED DGS10, and the trailing P/E on Vanguard's monthly page.
   - Threshold: the 10y holds above 5.5% for 3 months while P/E stays ≥20x (the yield gap widens past −0.75 pp). Or index P/E prints below 18x, which is the de-rating arriving.

**Single variable that flips the thesis:**
- *For the verdict:* structure. Loss of the 15% treaty rate or of non-US situs, or the appearance of a materially cheaper equivalent with equal tracking difference.
- *For the return expectation:* 10-yr index per-share EPS growth vs **3.92%/yr**. Below that, at a constant 21x, the fund underperforms a 10-yr Treasury.

## 7. Disagreements with the Quant (kept, not averaged)
| # | Issue | Quant view | Skeptic view | Evidence | Effect |
|---|---|---|---|---|---|
| 1 | Discount rate | 8% floor (rf UNKNOWN) | CAPM 10.22% (rf 5.22% sourced) | FRED DGS10 | FV return 0. HEV base 165.02 → 134.64. M3 centre 183.52 → 118.02. **Correction, applied in 03_rerun.py** |
| 2 | Most load-bearing input | Starting P/E (±10% → +11% / −9%) | Exit P/E. A starting-P/E definitional error leaves the base unchanged | output 8g | Ranking only |
| 3 | Base exit P/E 21x | neutral "no re-rating" | Generous with 10y 5.22% > E/P 4.76%. The Quant's own M3 at the sourced k gives a justified 12.8–15.3x. Not overwritten; expressed through bear weight 25% | output 8d, 8f | If 19x: 6.30 → 5.26% (−1.04 pp, 16.5% of FV). Not adopted in the base; probability effect −0.17 pp |
| 4 | Earnings above trend | open question | Yes. Partial reset belongs in the distribution | CAPE/PE 1.25–1.39x (cross-vendor) | 10% reset: 5.20% (−1.10 pp). In the bear weight, not the base |
| 5 | Bear "at the floor" (3.17% envelope) | bear sits at the floor | The envelope is not a floor. It assumes ROE holds at 17% with no mean reversion and no net issuance. The bear is not a worst case | arithmetic of envelope | Under the 23.24x definition the bear is −0.28%/yr |
| 6 | Dividend yield | 1.59% proxy | Unresolved. The FTSE figure is UNKNOWN, and Vanguard shows an unlabeled 1.32% | dossier §8 | −0.24 pp at 1.32% |
| 7 | WHT leakage | DY × US wt × 15% | Misallocates US vs non-US dividends and omits non-US WHT | formula | about ±0.1 pp |

No unresolved disagreement exceeds 15% of FV in the adopted numbers. #3 would at 19x (16.5%), but I hold it as a probability input, not a replacement base.

## 8. Verdict recommendation
- **VERDICT: HOLD** (core).
  - Cost and structure are verified best-for-purpose: 0.14% TER; 15% treaty WHT and non-US estate situs, both confirmed from primary law.
  - The FUND rules forbid TRIM on "index looks expensive" alone.
  - Expected return is 6.13%/yr (base 6.30%) against a 5.22% Treasury. **The implied ERP of about 0.9–1.1% is thin**, and the user should know that adding here buys roughly bond-plus-1% with equity drawdown risk.
- **FAIR_VALUE:** 6.30%/yr base (Quant, accepted). EV 6.13%/yr. **ENTRY_BELOW / EXIT_ABOVE:** n/a.
- **CONVICTION: MEDIUM.** Mechanically, applying the rules gives LOW: one drop for terminal share 100% (inherent to any accumulating-fund decomposition) and one for proxy index valuation inputs. I apply one drop only. The HOLD rests on structure facts that are primary-sourced, not on the proxy valuation inputs. The orchestrator should note both.
- **KEY_RISK:** a thin ERP (about 1%) on a 62%-US, AI-concentrated index at 21x with the 10y at 5.22%, so a lost decade vs Treasuries is plausible without any recession.
- **Allocation note:** the structural defect in the user's book is VXUS/VOO (US-situs, 30% WHT), not VWRA. The open item that could justify a VWRA switch is a peer TER/TD comparison, which is UNKNOWN in this run.

One line: HOLD the core. The wrapper is best-in-class and verified, but the price only pays about 1 pp over Treasuries, so don't mistake "core" for "cheap".

Recommended block (Skeptic; orchestrator synthesises the final one):
```
VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          193.34 USD
FAIR_VALUE:     6.30%/yr (base 10-yr net; probability-weighted EV 6.13%/yr)
UPSIDE:         n/a (FUND)
ENTRY_BELOW:    n/a
EXIT_ABOVE:     n/a
CONVICTION:     MEDIUM (mechanical rule application gives LOW; see above)
KEY_RISK:       Implied ERP ~1% over a 5.22% 10y UST on a 62%-US, AI-concentrated index at 21x
DATA_WARNINGS:  1
```

Sources: FRED DGS10 https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 · US–Ireland treaty https://www.irs.gov/pub/irs-trty/ireland.pdf · 26 USC §2104 https://www.law.cornell.edu/uscode/text/26/2104 · IRS https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns · Vanguard https://www.vanguard.co.uk/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating · yfinance price history (re-pulled 2026-10-13) · run files 01/02, 03_rerun.py output.
