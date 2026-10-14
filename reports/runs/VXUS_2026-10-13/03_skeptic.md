<!-- pipeline:value-skeptic -->
# Skeptic audit: VXUS (as of 2026-10-13)
Template: FUND. Under FUND, §3 is index-level earnings quality and §4 is a structure and cost audit graded A–F.
Status: CURRENT HOLDING alongside VWRA (the core).
Written by value-skeptic. It was rewritten on resume after an outside agent overwrote an earlier copy, which was moved to `_external_unverified/` and has not been read. Integrity check on resume:
- `01_research.md` and `02_quant.md` differ from the copies I audited only by a one-line provenance marker. Their bodies are byte-identical (15,620 B, and a diff of `02_quant.md`).
- `facts.json`, `00_inputs.json` and `02_model.py` have unchanged ctimes.
- The `02_model.py` output is identical on re-run.

## 1. Pre-mortem (written before reading the model)
Written after reading only `01_research.md` and `facts.json`, before opening `02_quant.md` / `02_model.py`.

**Single most likely structural reason the holding is worth materially less in 5 years.** The large risk sits in the index, not the wrapper.
- VXUS trades at a factsheet trailing P/E of 18.3x (2026-06-30). The EPS growth behind it (12.6%) is concentrated in one cyclical cluster:
  - TSMC 4.3% + Samsung 2.6% + SK hynix 2.2% + ASML 1.7% = 10.8% of the fund.
  - Taiwan + Korea = 16.6% of common stock.
  - Together these make up a semiconductor/memory upcycle tied to AI capex.
- The 10y UST is 5.22%. If AI capex rolls over, memory and foundry earnings mean-revert *and* the multiple compresses at the same time. A 5-year return near zero is then plausible with no defect in the fund.
- VWRA's ex-US sleeve carries the same market risk, so **it is not a reason to switch vehicles**.

**The structural defect that is certain, and specific to this holder (Singapore NRA), is the wrapper.**
- (a) US 30% withholding under §871(a) applies to the whole ordinary distribution, even though about 89% of the underlying income is foreign-source. At a 2.35% yield that is about 0.7%/yr. It recurs, it can't be recovered, and it applies to every dollar held.
- (b) US-situs estate exposure under §2104(a) + §851(a). The §2105(d) RIC look-through expired after 2011. Above $60k, with only the $13k credit, the tail is very large, though its timing is unknown.

Neither (a) nor (b) makes VXUS "worth less" in the index sense. Both make it **strictly worse than a structurally equivalent Irish vehicle, if one exists that is cheap and tracks well**.

My prior before reading the model was that the verdict turns on whether that substitute is mature yet:
- The Irish ex-US UCITS had $35M of assets, launched on 2026-08-18, and has no tracking record.
- The other route is VWRA. It removes the defect but changes the allocation, because it is 62% US.

## 2. Number audit
How the checks were done:
- **Recomputation:** an independent script (scratchpad `calc/skeptic_calc.py`), which does not import `02_model.py`.
- **Data re-pulls:** yfinance, re-pulled on 2026-10-14.
- **Web spot-checks: 5 figures**, at 5 sources:
  1. Vanguard 1042-S QSG notices (2025 and 2023)
  2. justETF profile of IE0009A5ADV9
  3. Vanguard FTC worksheet (2024)
  4. 26 USC §2001(c) (Cornell LII)
  5. 26 USC §2101(b) (Cornell LII)
- **Searches that produced no usable figure:**
  - a Vanguard QII / interest-related-dividend file: none found;
  - the FTSE Global All Cap ex US index dividend yield: only aggregator snippets, discarded.

| # | Input | Quant value | Verified value | Source | Status | Δ FV |
|---|---|---|---|---|---|---|
| 1 | Price | 84.52 USD (2026-10-13 close) | 84.535 (revised close, re-pull) | yfinance history(auto_adjust=False) | PASS (+0.02%) | 0 |
| 2 | 12-month price change | +15.35% | 73.27 → 84.52 = +15.35% | yfinance | PASS | 0 |
| 3 | TTM distributions / yield | 1.985 / 2.349% | 1.985 / 2.349%. 5-yr average DPS (2021–25) 1.966 = **2.33%** on today's price. CY2025 2.399 = 2.84% | yfinance dividends, re-pulled | PASS, with a Temporal flag (below) | 0 |
| 4 | Foreign tax paid, f | 7.48% of ordinary cash dividends (2024) | 7.48%, row "Total International Stock (VXUS) 88.6575% 61.1496% 7.48%". Column 3 is defined as a % of "Ordinary Cash Dividends", so the gross-up DY×(1+f) is correct | Vanguard FTCWS_012025.pdf (downloaded) | PASS. Temporal: 2024 is the latest year (FTCWS_012026 returns 404) | 0 |
| 5 | US WHT on distributions | 30% on 100% | 30% (§871(a)(1)(A); RIC dividends are US-source under §861(a)(2)(A); no SG treaty in Pub 901). **§871(k)(2) short-term-gain exemption = 0**: Total International Stock is absent from Vanguard's *complete* QSG lists for 2025 (1042SB 022026, 2 pages, alphabetical, ends at Windsor II) and 2023 (1042sb-2024). §871(k)(1) interest-related share: UNKNOWN | Vanguard 1042-S notices; Researcher's statute pulls | PASS. Resolves the dossier's "list may be truncated" caveat | 0 |
| 6 | TER VXUS | 0.05% | not re-fetched (spot-check budget). Factsheet F3369_062026 per dossier | dossier §2 | PASS (cited, not re-verified); ±10% = ±0.5 bp | 0 |
| 7 | VWRA OCF / US weight | 0.14% / 61.68% | consistent with the VWRA run, whose Skeptic verified 0.14% | VWRA run 03_skeptic | PASS | 0 |
| 8 | IE ex-US UCITS (IE0009A5ADV9) | OCF 0.12%; launched 2026-08-18; TNA US$35M (2026-08-31) | TER 0.12%, inception 18 Aug 2026, 2,340 holdings, physical sampling, accumulating, Irish domicile: all match. **Size now EUR 113m (justETF, undated) / US$117.1M (yfinance VXUA.L totalAssets, undated).** LSE USD ticker VXUA. 1-month median volume 104,048 shares at about US$4.85 | justETF (fetched 2026-10-14); yfinance | PASS. Temporal update: about 3.3× the 2026-08-31 TNA | 0 |
| 9 | Look-through ROE / payout / g envelope | 12.57% / 47.11% / 2.89–6.65% | identical | python recompute | PASS | 0 |
| 10 | Exit P/E bear / bull | 14.29x / 21.08x | identical | python recompute | PASS | 0 |
| 11 | Drag gap vs VWRA sleeve / IE ex-US | 61.5 / 63.5 bp | 61.5 / 63.5 bp (30% × 2.349% = 70.5 bp, less 9.0 / 7.0 bp TER) | python recompute | PASS | 0 |
| 12 | Scenario nets, SG / VW / IE | bear 2.13/2.75/2.77; base 6.64/7.26/7.28; bull 9.82/10.44/10.46 | identical to 0.01 pp | independent code | PASS | 0 |
| 13 | Starting P/E staleness | 18.3x (2026-06-30) | price 85.49 (2026-06-30) → 84.52 (−1.13%), so ~18.1x at constant E; E/P 5.53% vs UST 5.22% (+0.31 pp) | yfinance | PASS (not stale) | 0 |
| 14 | 10y UST | 5.22% | 00_inputs (FRED DGS10, 2026-10-08), re-verified by the Researcher, same as the VWRA run | 00_inputs | PASS (not re-fetched) | 0 |
| 15 | Estate rate schedule | UNKNOWN | §2101(b) computes NRA estate tax on the **§2001(c)** schedule. Tentative tax on $60,000 = $13,000 (equal to the credit). Marginal 26% ($60–80k), 28% ($80–100k), 30% ($100–150k), 32% ($150–250k), 34% ($250–500k) … 40% over $1M | Cornell LII 26 USC 2001, 2101 | PASS. Resolves dossier UNKNOWN #7 (rates) | 0 (outside FV) |
| 16 | Shares / net debt / base revenue | n/a (FUND) | n/a | – | n/a | – |
| 17 | Model fidelity | additive M2; TV share 100% | TV share 100% by construction, and **flagged** by the Quant. Additive M2 vs year-by-year M2b differ by 0–11 bp on the gap. No SBC double count (per-share growth) | `02_model.py` read in full | PASS | 0 |
| 18 | Switching spread | UNKNOWN | **still UNKNOWN.** The yfinance bid/ask snapshot is unusable (VWRA.L bid 198.94 > ask 193.18; VXUS bid 86.43 vs last 84.525 is stale). VXUA.L snapshot 13.4 bp, single undated quote, indicative only | yfinance info | UNKNOWN | 0 |

**Result: 17 inputs checked, 0 failed, 3 flags, no change to fair value. No `03_rerun.py`** (nothing crossed the 5% threshold). The 3 flags:
- the yield temporal flag;
- the VXUA size update;
- the switching spread, which is still UNKNOWN.

**Temporal flag on the yield (#3).**
- Q1–Q3 2026 distributions were 0.622, the lowest Q1–Q3 in the 2021–26 series (0.969–1.036 in 2021–25).
- December's share of calendar-year payouts rose from 0.39 (2022) to 0.57 (2025).
- The cause is UNKNOWN: timing, or a real fall in USD dividends.

The Quant's 2.35% is close to the 5-year average DPS on today's price (2.33%), so it is a fair base, not a low one. DPS grew 5.1%/yr over 2021–25, so the gap drifts upward over time, which M2b captures. The plausible range for the gap is 61–76 bp (2.33–2.84% yield).

## 3. Index-level earnings quality
- **Concentration.**
  - Top 10 = 15.0%, and the largest single name is TSMC at 4.3%. Name concentration is low.
  - **Earnings concentration is not low.** Four semiconductor names are 10.8% of the fund, and Taiwan + Korea are 16.6% of common stock (factsheet, 2026-06-30).
  - Per the investor profile (memory, not re-verified), the user **also holds TSM, SK hynix and SK Square directly**. VXUS's top cluster stacks on direct positions in the same memory/foundry cycle. VWRA carries the same names (TSMC is VWRA's #6 at 1.70%), so this is not a vehicle differentiator.
- **Earnings above trend.**
  - The factsheet's trailing EPS growth is 12.6%, about 2× the top of the sustainable envelope (6.65% = ROE 12.57% × retention 52.9%).
  - The 1-yr NAV return is 27.42%, against 9.97%/yr over 10 yrs (to 2026-06-30).
  - I treat current index EPS as cyclically elevated, so the normalised E/P is below the headline 5.46%. That can't be quantified: CAPE and the 5-yr P/E history are UNKNOWN.
- **Definitional issues.**
  - P/E is 18.3x on the factsheet vs 16.14x on yfinance, 13% apart on different definitions.
  - Factsheet ROE is 13.3% vs P/B ÷ P/E = 12.57%.
  - Only the bear case is sensitive to the definition (2.13% → 3.40%, Quant §10a).
- **Distribution quality.**
  - 2026 Q1–Q3 payouts are down 40% while the price is up 15% over 12 months. This is unexplained (see §2 #3).
  - Signpost: the December 2026 distribution. On 2024–25 patterns (0.39–0.57 of the year), a Dec payout below ~0.5 would suggest a real decline rather than timing. This threshold is my judgement.
- **SBC / accruals / adjusted-vs-GAAP:** not applicable at fund level. Whether index EPS is before or after SBC is UNKNOWN. The Quant uses per-share growth, so dilution enters once. **SBC-adjusted fair value: n/a (FUND).**

## 4. Structure and cost audit (Structure Grade)
**Comparison for a Singapore-resident non-US holder.** All figures are from the dossier and facts, verified as marked in §2.

| Item | VXUS (held) | VWRA (core) | Vanguard FTSE All-World ex-US UCITS, IE0009A5ADV9 (VXUA) | iShares MSCI World ex-USA (IE000R4ZNTN3) + Core MSCI EM IMI (IE00BKM4GZ66) |
|---|---|---|---|---|
| TER | **0.05%** | 0.14% | 0.12% | 0.15% / 0.18% |
| Tracking difference | +0.13 / +0.14 / 0.00 pp (3/5/10y, vs a WHT-adjusted index): excellent | −0.07 to +0.03 pp (calendar 2020–25) | **UNKNOWN** (8 weeks old) | UNKNOWN |
| Investor-level US WHT | **30% of every distribution** (§871(a); no treaty; QSG exemption 0 in 2023 and 2025; IRD UNKNOWN) | none (accumulating) | none (accumulating) | none (accumulating) |
| All-in drag on ex-US exposure (TER + source WHT + US WHT) | **93.0 bp/yr** | 31.6 bp | 29.6 bp | ~33–36 bp (gap 57.5–60.5 bp) |
| Estate situs | **US-situs** | non-US (Irish plc) | non-US | non-US |
| Size / record | US$651bn fund; since 2011 | ~US$87bn (yfinance totalAssets, undated) | US$117M (yfinance) / EUR 113m (justETF); since 2026-08-18 | EUR 3,262M / EUR 40,259M |
| Universe | all-cap, 8,755 stocks | large+mid, 3,784, 62% US | large+mid, 2,340 | developed large+mid 735 + EM IMI 2,902 |

**Estate situs: I agree with the Researcher's reading, and add one piece of evidence.**
- The statute chain holds. §2104(a) treats a NRNC's stock as US property "only if issued by a domestic corporation". §851(a) defines a RIC as "any domestic corporation". §2105(d) look-through ended for deaths after 2011. Singapore is not a death-tax treaty country (Form 706-NA instructions).
- Extra evidence of RIC status: Vanguard's FTC worksheet states the fund "passes the Foreign Tax Credit to its shareholders". That is the §853 pass-through, an election available to a RIC (§853 text not re-fetched in this run).
- Not a legal opinion. Reg. 20.2104-1 was not retrieved.

**Estate sizing (new, from §2001(c)).**
- If the user's aggregate US-situs holdings exceed US$60k, each further US$10k of VXUS adds:
  - **US$2,600** of estate tax at $60–80k;
  - **US$2,800** at $80–100k;
  - **US$3,000** at $100–150k.
- For comparison, the whole 10-yr base wrapper drag is **US$1,125** per US$10k. A single death event costs 2–3× the decade's withholding drag.
- The aggregate is **UNKNOWN**. The investor profile (memory, not re-verified) lists about 10 direct holdings that appear to be US-incorporated issuers, plus VXUS, on total net liquidation of ~S$138k ≈ US$108k (at 0.7812).
- So the marginal estate rate on VXUS is between 0% (if aggregate US-situs is below $60k) and about 30%. Selling VXUS lowers the aggregate for every other US holding as well.

**Timing finding: the December distribution.**
- December carried 39–57% of each year's payouts (2022–25).
- Dec 2024 was 1.005 and Dec 2025 was 1.363. That is 1.19–1.61% of today's price, so **30% WHT on that one payment = 36–48 bp of the position**: 7–9 months of the annual gap, lost on a single date.
- Ex-dates were 2024-12-20 and 2025-12-19.
- **A switch executed before mid-December 2026 avoids it.** This alone outweighs any plausible one-off trading cost (the Quant's payback grid gives 0.16 yrs at 10 bp and 0.79 yrs at 50 bp).

**Substitute maturity (the orchestrator's question).**
- **VXUA (IE0009A5ADV9).**
  - Size: grew from US$35M to about US$117M in roughly 6 weeks (undated).
  - Tracking: no record yet.
  - Coverage: large+mid only, so it drops VXUS's small caps. Their return effect is UNKNOWN; each ±0.10 pp/yr moves the gap ∓10 bp.
  - Closure risk is **cost-only for this holder**: with no CGT, a closure returns NAV in cash, and the cost is one re-trade spread plus time out of the market.
  - Tracking breakeven: VXUA would need to trail its index by **63.5 bp/yr beyond its TER** before VXUS-SG wins. Vanguard's Irish flagship VWRA has run −0.07 to +0.03 pp (2020–25).
  - On-screen liquidity is about US$0.5M/day, so use limit orders.
  - **Immature, but not a blocker.**
- **iShares pair.** Mature and liquid, but it means two funds to rebalance and a change of index family. Gap 57.5–60.5 bp in its favour.
- **VWRA.** Mature, and verified Grade A in the VWRA run. But US$1 of ex-US exposure via VWRA brings **US$1.61 of US equity** with it, so it replaces the *position*, not the *tilt*.

**Switching frictions.**
- Capital-gains tax: none for this user.
- Exit liquidity: VXUS trades about 5.1M shares/day (yfinance averageVolume), so a retail-size exit is trivially absorbed.
- Spreads and IBKR commissions: **UNKNOWN** (the snapshot was unusable and the commission schedule was not verified). The Quant's hypothetical payback grid covers 10–100 bp.

**Structure Grade: D** (for this holder). The grade reflects four things:
- The fund itself is excellent: cheapest TER in the set, about zero tracking difference over 10 yrs, US$651bn. For a US taxpayer it would grade A.
- For a Singapore NRA, the wrapper adds a verified, unrecoverable 30% withholding: an all-in drag of 93 bp vs about 30 bp in an Irish wrapper on the same stocks, 3× the cost.
- It also adds US-situs estate exposure at 26–30% marginal rates in the user's likely band.
- It is not F because the defect is fully escapable at negligible cost and the fund is not otherwise impaired.

## 5. Probabilities & expected value
**Outside view / base rate used.**
- **Earnings-yield anchor:** long-run real return ≈ starting E/P = 5.46% (18.3x), or 5.53% at today's price. Trailing earnings are cyclically elevated (§3), so the normalised anchor is lower. Inflation is UNKNOWN.
- **The Quant's base fits the anchor.** The base, 7.35% nominal pre-investor-tax, matches the anchor if inflation is about 1.9%. So it is inside the band, not above it.
- **Reverse anchor (Quant §5a):** at a constant 18.3x, per-share EPS must compound:
  - **3.58%/yr** just for VXUS-SG to match the UST (2.96% inside an Irish wrapper);
  - **7.58%** to earn UST + 4%, which is above the 6.65% sustainable envelope.
- **Weights: 25/55/20, the same as the VWRA run, for comparability.** The ex-US index is cheaper (18.3x vs 21x), which argues for a lighter bear. Its trailing EPS is more cyclically elevated (semis/memory), which argues for a heavier one. I net them to the same weights. **This is a judgement prior, not a sourced frequency.**

| Scenario (10-yr, nominal USD) | VXUS, SG holder | VWRA ex-US sleeve | Irish ex-US UCITS | p |
|---|---|---|---|---|
| Bear (g 3%, exit 14.3x) | 2.13%/yr | 2.75% | 2.77% | **25%** |
| Base (g 5%, exit 18.3x) | 6.64%/yr | 7.26% | 7.28% | **55%** |
| Bull (g 6.65%, exit 21.1x) | 9.82%/yr | 10.44% | 10.46% | **20%** |
| **EV, return-weighted** | **6.15%/yr** | 6.77% | 6.79% | |
| EV, wealth-weighted | 6.44%/yr | 7.05% | 7.07% | |
| E[US$10k → yr 10] | 18,657 | 19,760 | 19,797 | |

- **Expected cost of keeping VXUS:** an E[10-yr wealth gap] of **US$1,103 per US$10k** vs the VWRA sleeve, and US$1,140 vs the Irish ex-US UCITS. Across weightings of 20/60/20 to 30/50/20, the gap is US$1,084–1,158.
  - **The keep/switch decision is insensitive to the probabilities,** because the gap is a property of the wrapper.
- **Implied ERP vs 5.22% UST:**
  - VXUS-SG: EV +0.93%, base +1.42%;
  - Irish wrapper: EV +1.57%, base +2.04%.
  - **Thin in either wrapper.** The VXUS wrapper consumes about 30% of what is left.
- **Margin of safety:** n/a under FUND rules. For information only, the probability-weighted HEV at k 10.22% is 59.59, so MoS = **−41.8%** and asymmetry = −0.55. The ex-US index, like VWRA, beats Treasuries in expectation but not a conventional equity hurdle.
- **Asymmetry of the decision (keep vs switch):** the Irish wrapper beats VXUS-SG in **every** modelled scenario, by 61.5 bp (M2) and by 61.5–74.3 bp (M2b), so **switching has no modelled downside**. Two risks are not modelled:
  - VXUA's tracking difference, which would need to be worse than −63.5 bp to flip the result;
  - loss of VXUS's small caps (±10 bp per 0.10 pp).

## 6. Bear thesis & downside catalysts
**Pre-mortem revisited.** The model confirms both halves:
- **The index:** the bear case (multiple back to 14.3x, 3% growth) gives 2.13%/yr after tax, which is 3.1 pp below Treasuries.
- **The wrapper:** a certain 61.5 bp/yr of leakage, plus an estate tail at 26–30% marginal rates. It is the only part of the downside the user can remove, and removing it costs almost nothing.

**Top 2 structural downside catalysts:**
1. **Semiconductor/memory earnings normalise while the multiple holds, then compresses (index).**
   - *Signpost:* the Vanguard factsheet's trailing "earnings growth rate" (12.6% at 2026-06-30) and P/E.
   - *Threshold:* earnings growth falls below 5% (the base assumption) while P/E stays ≥18x. That would mean the multiple is being held up by falling E, and the 14.3x bear exit becomes the path.
2. **The rate squeeze on a thin premium (index).**
   - *Signpost:* FRED DGS10 against the index E/P (5.53% at today's price).
   - *Threshold:* DGS10 above the index E/P for a full quarter, so the trailing equity premium over Treasuries turns negative. The gap is +0.31 pp today.

**Holder-specific defect (already present, not a future catalyst):** every VXUS distribution is withheld at 30%.
- *Signpost:* the IBKR statement for the December 2026 distribution.
- *Threshold:* any withholding > 3.83% keeps VXUS behind VWRA, and the statute rate is 30%.
- *Further threshold:* aggregate US-situs holdings above US$60,000 put VXUS in the 26%+ marginal estate band.

**The single variable that flips the thesis:**
- **For the keep/sell decision:** the effective US withholding rate on VXUS distributions. VXUS matches the VWRA sleeve only at ≤3.83%, or at a distribution yield ≤0.30%. The statute rate is 30%, and the verified QSG exemption is 0.
- **For the return level:** the year-10 exit P/E (±10% → −9.9% / +9.8% on HEV).

## 7. Disagreements with the Quant
**No disagreement on any number. The independent recomputation matches to 0.01 pp.** The Quant gives no verdict, so there is no verdict disagreement. Below are refinements, kept separate rather than merged into the Quant's figures:

| # | Issue | Quant | Skeptic | Evidence | Effect on FV / decisive gap |
|---|---|---|---|---|---|
| 1 | §871(k) exempt share | UNKNOWN; swept 0 / 10% / 25% | QSG exemption = **0** (not on the complete 2023 or 2025 lists). IRD UNKNOWN. So the 25%-exempt case (43.8 bp) is implausible, and the plausible floor is about 54 bp (10% exempt) | Vanguard 1042SB 022026 and 1042sb-2024 | FV 0. Gap range narrows from 44–76 bp to **54–76 bp** |
| 2 | Estate cost | "rate schedule UNKNOWN; not in the bp figures" | Sourced §2101(b)/§2001(c): **US$2,600–3,000 per US$10k** of VXUS at an aggregate of $60–150k; aggregate UNKNOWN | Cornell LII 26 USC 2001, 2101 | FV 0. Strengthens the case to switch |
| 3 | Substitute maturity | TNA US$35M (2026-08-31) | US$117M (yfinance) / EUR 113m (justETF), undated. Closure risk is cost-only for a no-CGT holder. TD breakeven −63.5 bp | justETF; yfinance | FV 0 |
| 4 | Drag timing | annualised | 36–48 bp of the position is withheld on **one date**, the December ex-date, so the switch should precede it | yfinance dividends (Dec 2024/2025) | FV 0. Execution timing |
| 5 | Yield representativeness (Quant's open question 2) | 2.35% TTM, flagged as possibly unrepresentative | Agree with the Quant's base: 2.35% ≈ the 5-yr average DPS on today's price (2.33%). The 2026 Q1–Q3 drop is unexplained | yfinance 2021–26 | none |

None of these is worth more than 15% of fair value, so none is an unresolved disagreement for the conviction rule.

## 8. Verdict recommendation
**VERDICT: SELL** (move the exposure; don't trim it).
- **Why SELL rather than TRIM.** Under the FUND rules, SELL is for a structural defect. For a Singapore NRA, VXUS has one, and it is verified from primary sources:
  - 30% §871(a) withholding on 100% of distributions, with no treaty and a QSG exemption of 0;
  - US-situs estate exposure under §2104(a)/§851(a).
- **The defect applies to every dollar held**, so there is no position size at which keeping some VXUS beats an Irish wrapper. A partial TRIM keeps the defect on the remainder for no offsetting benefit.
- Mature substitutes exist (VWRA; the iShares pair). The immature one (VXUA) affects the *destination*, not *whether* to exit.
- Switching has no tax cost and pays back within months, and selling before the December ex-date avoids 36–48 bp in one go.
- **Destination is an allocation choice for the user/orchestrator:**
  - **(a) If the ex-US overweight was not deliberate:** move into **VWRA**. This moves the book toward the market-cap core the user adopted on 2026-10-13. It adds about US$1.61 of US equity per US$1 of ex-US.
  - **(b) If the ex-US tilt is wanted:** move into **VXUA (IE0009A5ADV9, LSE, USD, Acc, 0.12%)**, which I judge acceptable now: its closure risk is cost-only, and its TD would need to be worse than −63.5 bp to lose. Use a limit order. Or use the iShares World ex-USA + EM IMI pair for a mature record.
  - **Either route:** execute before the December 2026 ex-date (prior years: 12-20 and 12-19).
- **FAIR_VALUE:**
  - 6.64%/yr: the Quant's base 10-yr net return for VXUS held by a Singapore resident, accepted.
  - Probability-weighted EV: 6.15%/yr (6.44% wealth-weighted).
  - The same exposure in an Irish wrapper: base 7.26–7.28%, EV 6.77–6.79%.
- **ENTRY_BELOW / EXIT_ABOVE:** n/a (FUND).
- **CONVICTION: MEDIUM** (mechanical).
  - Start HIGH; drop one level because the terminal-value share is 100% by construction (same treatment as the VWRA run).
  - No corrected inputs, no disagreement over 15%, primary financials.
  - Note for the orchestrator: the SELL rests on the wrapper gap, which does not depend on the terminal assumption (exit P/E and growth move it by 0 bp in M2). On the switch economics alone, I would call it HIGH.
- **KEY_RISK:**
  - For the decision: the destination's execution (VXUA has no TD record, and VWRA changes the US weight).
  - For the exposure: semiconductor-cycle earnings normalisation with the 10y UST (5.22%) about equal to the index E/P (5.53%).

One line: SELL VXUS and move the money. On the same stocks, the wrapper costs a Singapore holder ~62 bp/yr more, verified at a 30% statutory rate with no exemption, and adds a US estate tail. That gap holds in every scenario, and switching costs almost nothing.

Recommended block (Skeptic; the orchestrator synthesises the final one):
```
VERDICT:        SELL
AS_OF:          2026-10-13
PRICE:          84.52 USD
FAIR_VALUE:     6.64%/yr (base 10-yr net, SG holder; EV 6.15%/yr; Irish wrapper on same exposure 7.26-7.28% base)
UPSIDE:         n/a (FUND)
ENTRY_BELOW:    n/a
EXIT_ABOVE:     n/a
CONVICTION:     MEDIUM (mechanical; switch economics alone would be HIGH)
KEY_RISK:       30% US WHT (~62 bp/yr) + US-situs estate exposure for a SG holder; destination (VXUA) has no TD record
DATA_WARNINGS:  1
```

Sources:
- Vanguard 1042-S QSG notices: https://investor.vanguard.com/content/dam/retail/us/en/pdfs/taxes/1042sb-022026.pdf and https://investor.vanguard.com/content/dam/retail/publicsite/en/documents/taxes/1042sb-2024.pdf
- Vanguard FTC worksheet: https://investor.vanguard.com/content/dam/retail/publicsite/en/documents/taxes/FTCWS_012025.pdf
- justETF: https://www.justetf.com/en/etf-profile.html?isin=IE0009A5ADV9
- 26 USC 2001: https://www.law.cornell.edu/uscode/text/26/2001
- 26 USC 2101: https://www.law.cornell.edu/uscode/text/26/2101
- yfinance (VXUS, VWRA.L, VXUA.L), re-pulled 2026-10-14
- Run files: 01_research.md, 02_quant.md, 02_model.py output
