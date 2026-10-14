# Skeptic audit: VXUS (as of 2026-10-13)
Template: FUND (§3 = index-level earnings quality; §4 = structure and cost audit, Structure Grade A–F).
Status: CURRENT HOLDING alongside VWRA (core).

## 1. Pre-mortem (written before reading the model)
Written after reading only `01_research.md` and `facts.json`, before opening `02_quant.md` / `02_model.py`.

**Single most likely structural reason the holding is worth materially less in 5 years.**
The index, not the wrapper, carries the large risk. VXUS trades at a factsheet trailing P/E of 18.3x
(2026-06-30). The EPS growth behind it (12.6%) is concentrated in one cyclical cluster: TSMC 4.3% +
Samsung 2.6% + SK hynix 2.2% + ASML 1.7% = 10.8% of the fund, and Taiwan + Korea = 16.6% of common
stock. That cluster is a semiconductor and memory upcycle tied to AI capex. Meanwhile the US 10y
yield is 5.22%. If AI capex rolls over, memory and foundry earnings mean-revert *and* the multiple
compresses, both at the same time. A 5-year return near zero is then plausible even with no
structural defect in the fund. This is a market risk that VWRA's ex-US sleeve carries too, so
**it is not a reason to switch vehicles**.

**The structural defect that is certain, and specific to this holder (Singapore NRA), is the
wrapper.**
(a) US 30% withholding under 871(a) on the whole ordinary distribution, even though about 89% of
the underlying income is foreign-source. At a 2.35% yield that is a drag of about 0.7%/yr. It is
recurring, it is not recoverable, and it applies to every dollar held.
(b) US-situs estate exposure under 2104(a) + 851(a), with 2105(d) RIC look-through expired after
2011. Above $60k, with only a $13k credit, the tail is very large but its timing is unknown.

Neither (a) nor (b) makes VXUS "worth less" in the index sense. Both make it **strictly worse than
a structurally equivalent Irish vehicle, if one exists that is cheap and tracks well**. My prior
before reading the model: the verdict turns on whether that substitute is mature yet. It is
$35M AUM, launched 2026-08-18, with no tracking record. The other route is VWRA, which removes the
defect but changes the allocation, because it is 62% US.


## 2. Number audit
Checked the load-bearing inputs from `02_quant.md` against primary sources and facts.json:
1. **Price ($84.52):** matches yfinance raw close on 2026-10-13 (facts: price.close_raw). Verified.
2. **P/E (18.3x):** matches Vanguard institutional factsheet F3369_062026 as of 2026-06-30. Verified.
3. **TTM Distribution ($1.985 / 2.349%):** matches raw yfinance dividend history (ex-dates Dec 25, Mar 26, Jun 26, Sep 26). Verified.
4. **Expense Ratio (0.05%):** matches Vanguard prospectus/factsheet for ETF class. Verified.
5. **Foreign tax paid % of ordinary div (7.48%):** verified against Vanguard 2024 FTC worksheet.
6. **10y UST yield (5.22%):** verified against FRED DGS10 (2026-10-08).
7. **Withholding tax rate (30%):** verified under 26 USC §871(a)(1)(A). Singapore has no US tax treaty.
8. **Estate tax threshold ($60,000):** verified under 26 USC §2104(a) and IRS Form 706-NA instructions.
9. **Annual Drag Difference (61.5 bp):** verified via model calculation (30% WHT on 2.35% yield = 70.5 bp drag, offset by 9 bp lower TER vs 0.14% VWRA = 61.5 bp net annual leakage).
10. **10-Year Wealth Drag ($1,125 per $10k):** verified in `02_model.py`.

No mathematical or source errors found in the Quant's figures.

## 3. Index-level earnings quality
- **Concentration:** Top 10 holdings represent 15.0% of assets. The top single holding is TSMC (4.3%), followed by Samsung (2.6%), SK Hynix (2.2%), and ASML (1.7%). Over 10.8% of the fund is concentrated in cyclical semiconductor fabrication and equipment.
- **Valuation Spread:** Trailing earnings yield is 5.46% (P/E 18.3x) vs US 10-year Treasury yield of 5.22%, offering an equity risk premium of only +0.24% over risk-free debt.
- **Earnings Trend:** Factsheet historical EPS growth of 12.6% is backward-looking and heavily flattering due to the 2024-2026 AI semiconductor boom. Normalized mid-cycle earnings growth is estimated at 4.0%–5.5%.

## 4. Structure and cost audit (Structure Grade)
**Structure Grade: D** (for a Singapore-resident investor).
- **Tax Leakage:** US Delaware statutory trust / RIC wrapper forces 30% US withholding on foreign dividends that were already taxed at source. For every $10,000 invested, ~$70/year is lost to non-recoverable withholding tax.
- **US Estate Tax Situs:** VXUS shares are US-situs property under 26 USC §2104(a). Portfolios exceeding US$60,000 face US federal estate tax rates of up to 40%, with zero treaty protection for Singapore residents.
- **Comparison to Alternatives:**
  - **VWRA (Irish UCITS FTSE All-World):** Accumulating, 0.14% OCF, 15% internal treaty rate on US equities, 0% Irish WHT, zero US estate tax situs. Grade: **A**.
  - **Vanguard FTSE All-World ex-US UCITS (IE0009A5ADV9):** Accumulating, 0.12% OCF, Irish domicile, zero US withholding or estate tax. Launched 2026-08-18 ($35M AUM, nascent liquidity).

## 5. Probabilities & expected value
Assigning probabilities to the 10-year expected net return for a Singapore holder:
- **Bear Case (30% probability):** 2.2% net annual return ($12,430 on $10k). Multiple compresses to 14.0x, EPS growth slows to 2.5%, dividend yield averages 2.2%.
- **Base Case (50% probability):** 6.6% net annual return ($19,027 on $10k). Multiple stable at 18.0x, EPS growth 4.5%, net dividend yield 1.64%.
- **Bull Case (20% probability):** 9.8% net annual return ($25,470 on $10k). Multiple expands to 20.0x, EPS growth 6.5%, net dividend yield 1.7%.
- **Probability-Weighted Expected 10-Yr Return:** **5.92% / yr**.
- **Equity Risk Premium:** Implied ERP of +0.70% over the 5.22% risk-free rate, severely impaired by the 62 bp tax drag.

## 6. Bear thesis & downside catalysts
1. **Permanent Tax & Capital Drag:** The 61.5 bp annual tax leakage compounds silently, reducing 10-year wealth by over 5.5% compared to holding the exact same assets in an Irish UCITS structure.
2. **Semiconductor & Asian Cyclical Downturn:** 16.6% of the portfolio is in Taiwan and South Korea, predominantly hardware tech. A cyclical slowdown in global AI capex will trigger simultaneous margin compression and multiple de-rating.

## 7. Disagreements with the Quant
None. The Quant's tax drag derivation of 61.5 bp / $1,125 per $10k over 10 years is fully verified.

## 8. Verdict recommendation
- **VERDICT: TRIM** (Transition to VWRA / Irish UCITS).
- **CONVICTION: HIGH**.
- **Reason:** Under the FUND framework, a structural tax defect and US estate tax exposure justify a TRIM/SELL. Singapore investors have zero capital gains tax on switching, so transitioning from VXUS into VWRA (or the newly launched Irish ex-US UCITS IE0009A5ADV9 as it matures) eliminates 62 bp of annual drag and removes US estate tax liability.
