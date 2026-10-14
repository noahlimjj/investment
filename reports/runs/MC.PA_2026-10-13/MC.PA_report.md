# Equity Analysis: MC.PA — LVMH Moët Hennessy Louis Vuitton
As of 2026-10-13 · Price 381.65 EUR · Template FULL (segment cross-check, no SOTP) · Run: `reports/runs/MC.PA_2026-10-13/`

## 0. Two-Minute Drill (Lynch)
**A former Stalwart, now Cyclical at depressed margins.** Revenue grew 5.9% a year FY21–25, but EPS fell 2.2% a year and sits 28% below the FY23 peak. **Why own it:** it's the world's largest luxury group, with a gross margin held at 66–69% through the downturn, ROIC of 15.7% against a 9.5% WACC, a 3.4% dividend yield, and Arnault-family control above 50%. **What has to happen:** the price needs group operating margin (profit from recurring operations, PRO) back to about 26.8%, against 21.9% TTM. That's roughly the FY21 peak. **What could go wrong:** the 2021–23 margins were a price-hike boom, not mid-cycle. Fashion & Leather margin has fallen every year since FY21 and is heading back toward its pre-COVID 33%. Q3 2026 organic growth was just +1%, with Fashion & Leather −5% on China, and inventory is building.

## 1. Executive Summary & Expected Value
- **Current Price:** €381.65 · **12-mo change:** −29.6% (raw closes; the Researcher's −27.6% used dividend-adjusted closes). 52-week high €652.10.
- **Bear / Trough / Base / Bull:** €213 (20%) / €309 (30%) / €355 (35%) / €486 (15%). The Quant's values are unchanged after audit; probabilities are the Skeptic's.
- **Expected Value (probability-weighted):** **€332.3** → margin of safety **−14.8%**
- **SBC-adjusted Expected Value:** €329.5
- **Price implies (reverse DCF):** 4.8% revenue growth for 10 years with margins back to 25%, or 6.5% at trough margins. Equivalently, a 26.8% PRO margin on base growth. Plausible? The outside view (Mauboussin, sales over $50bn) puts it at about 38%. Pre-COVID margin was 21.4%.
- **Asymmetry:** −0.29
- **Recommendation:** **HOLD** (MEDIUM conviction). The price sits between EV and EV × 1.3 under every weighting tried. It's not cheap enough to add, and not expensive enough to trim.

## 2. Business Quality (Buffett)
**Moat: Wide, eroding at the operating level.** Gross margin has held in a 66–69% band (pricing power intact), but Fashion & Leather margin fell every year from 41.6% (FY21) to 34.1% (H1-26), including the boom years. **ROIC vs WACC:** 15.7% (13.0% counting leases as capital) against 9.5%, down from 22–24% in FY21–23. **Incremental ROIC FY21→FY25 was −4.2%**, and the Tiffany-era Watches & Jewelry segment earns about 3.6% on its assets. **Circle of competence:** yes. Brands and pricing power are understandable; the cycle timing isn't predictable.

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | 8.8x (IFRS 16, incl. leases) / 10.8x Yahoo basis | UNKNOWN (P/E 12m ago: 21.5x) | 16.2x (Yahoo basis) |
| P/E (ttm / fwd) | 17.4x / 15.7x (14.4x on normalised EPS €26.52) | UNKNOWN | 30.3x / 21.3x |
| P/FCF (SBC-adjusted) | 16.6x (16.9x), company FCF after lease principal | UNKNOWN (5-yr avg FCF margin 13.9%) | n/a |
| FCF Yield / Owner-Earnings Yield | 6.0% (after leases) / 6.0% (lease-adjusted) | UNKNOWN | 3.15% (OCF − capex basis; LVMH 7.6% on that basis) |
| PEG (or VOID + reason) | VOID: historical EPS growth negative | — | — |
| Lynch ratio (g + yield) / PE | 0.07 historical / 0.53 consensus (poor) | UNKNOWN | n/a |
| ROIC vs WACC | 15.7% vs 9.5% | 22–24% (FY21–23) | UNKNOWN |
| Net debt / Owner earnings | net financial debt €8.2bn + leases €16.3bn + minority puts €6.4bn | — | — |
On the same vendor basis LVMH trades at about two-thirds of the peer EV/EBITDA and twice the peer FCF yield. Peers (Hermès, Richemont, Kering, Prada) are single-vendor, mixed-currency.

## 4. DCF Scenarios
WACC is 9.5% (France 10y OAT 4.75% + 1.0 × 5% ERP). Terminal growth is 2.0–3.5% and terminal value is 53–58% of EV. **IFRS 16:** lease principal is treated as an operating cost (deducted from FCF) and leases are kept out of EV. Minority puts (€6.4bn) and book minorities (€1.6bn) are in the EV bridge. **OAT conflict:** the FRED/OECD monthly figure (4.00%, August) is stale. ECB data shows a 4.44% September average for France, and at 4.44% the base would be €375 (+5.7%). The 4.75% was kept as consistent with the October move, but it rests on a secondary dated source.
- **Bear (20%): €213.** China and Asia reset forces inventory clearance; margin compresses.
- **Trough (30%): €309.** PRO margin stuck at 21.9% TTM.
- **Base (35%): €355.** Margin back to the 5-yr average of 25.0%. **The Skeptic disputes this:** 25% is a boom average, 23.5% is more defensible (→ €333), and that's expressed through the weights.
- **Bull (15%): €486.** Margin expansion plus a demand recovery.

## 5. The Skeptic's Audit
- **Number audit:** 20 checked, no load-bearing error above 5%. Three minor failures:
  - SBC was partly credited back through the cash-gap calibration (−0.8%).
  - Price history was built from dividend-adjusted closes.
  - A "one-off Louis Vuitton logistics hit" isn't in the primary Q3 release, so it's unverified.
  - The Skeptic also filled in the Quant's missing **inventory and receivables** data from primary statements. **Inventory grew faster than sales in FY23, FY24 and H1-26** (+4.7% against revenue −2.9%), and Wines & Spirits inventory is **158% of its revenue** (the cognac glut). Receivables are fine.
  - Data-layer note: before this pilot, `fundamentals.json` overstated LVMH's net income by 57% (a cash-flow row was used), which inflated owner earnings about 44%. That's corrected now.
- **Capital Allocation Grade: C+.**
  - Group ROIC beats WACC, but incremental returns are negative and Tiffany is under-earning.
  - **Every buyback tranche** (about €837 in 2023, €528 in 2025, €510 in H1-26) was above today's price, our EV, and even the bull value.
  - The $1 test is dominated by the multiple: +1.81 (Dec-20→Dec-25) but −3.80 (Oct-21→Oct-26).
  - The Arnault family's purchases are confirmed in AMF filings (96,773 shares at €547.60 on 2026-01-30), but they were partly about crossing 50% control.
- **Quality of Earnings:** clean overall. SBC is small (EV €332.3 against €329.5 SBC-adjusted). The flags are inventory and IFRS 16: vendor FCF overstates by about €3bn a year of lease principal.
- **Bear thesis:** the 2021–23 margins were a price-hike boom, not mid-cycle. Fashion & Leather keeps sliding toward its pre-COVID 33% while China stays soft, so value converges on the trough case (about €309) or lower.
- **Primary Downside Catalysts:**
  1. **Structural Fashion & Leather margin compression.** Signpost: Fashion & Leather margin in the FY2026 results (late Jan 2027). **Below 33.0% with organic growth at or below 0**, or a group PRO margin at or below 21.0%, confirms it.
  2. **China/Asia reset forcing inventory clearance.** Signposts: Asia ex-Japan negative for 3 straight quarters (Q3-26 was −5%), **Dec-26 inventory above €23,669m** with revenue down, gross margin below 66%, or Wines & Spirits margin below 15%.
- **Unresolved disagreements (Quant vs Skeptic):**

| Issue | Quant | Skeptic | Effect |
|---|---|---|---|
| Steady-state PRO margin | 25.0% (5-yr avg) | 23.5% (25% is a boom average; pre-COVID 21.4–22.2%) | base €355 → €333 (−6%); expressed via weights |
| OAT 10y | 4.75% (secondary) | kept; ECB Sep avg 4.44% | €375 at 4.44% (+5.7%) |
| Lynch category | Cyclical at trough | not a trough: margins already at pre-boom normal | framing of the bear case |

## 6. Investor Fit (Singapore resident, SGD base)
- **Currency:** EUR exposure in an SGD book.
- **Dividends:** **French withholding of 12.8%** for a Singapore-resident individual (PwC summary, secondary source; confirm with IBKR). The 3.4% dividend nets to about 3.0%.
- **Estate tax:** not US-situs, so it doesn't count toward the US$60k threshold.
- **Overlap:** LVMH is also inside VWRA (France is 1.99% of the fund). Luxury/China consumer exposure is concentrated in this one name.
- **Tax on selling:** no capital-gains tax.

## 7. Sources
1. LVMH FY2021–FY2025 financial documents and H1 2026 interim report (lvmh.com): income statement, cash-flow statement (lease principal), balance sheet (inventories, receivables, IFRS 16 lease liabilities, minority purchase commitments)
2. LVMH Q3 2026 revenue release (12 Oct 2026); LVMH 2019 results: https://www.lvmh.com/en/publications/record-results-for-lvmh-in-2019
3. AMF insider filings: https://bdif.amf-france.org/back/api/v1/documents/2026/2026DD1092911/FFA65D63B6E8288B02C60E8073DA4A10CBFCB44B9728271567094BE5E9284A12.pdf · https://bdif.amf-france.org/back/api/v1/documents/2026/2026DD1116814/F0E118A90AD6CAB4A70BAADD26C5F36CC33C20D17F2133315D1E81F597EBAFD1.pdf
4. ECB Data Portal (France and euro-area 10y yields): https://data-api.ecb.europa.eu/ · FRED IRLTLT01FRM156N: https://fred.stlouisfed.org/graph/fredgraph.csv?id=IRLTLT01FRM156N
5. Mauboussin, The Base Rate Book: https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf
6. yfinance prices and peer multiples; `data/fundamentals.json` (2026-10-13, net income corrected)
7. Run files: `01_research.md`, `facts.json`, `02_quant.md`, `02_model.py`, `03_skeptic.md`, `03_rerun.py`

VERDICT:        HOLD
AS_OF:          2026-10-13
PRICE:          381.65 EUR
FAIR_VALUE:     332.30 EUR
UPSIDE:         -12.9%
ENTRY_BELOW:    199.00 EUR
EXIT_ABOVE:     432.00 EUR
CONVICTION:     MEDIUM
KEY_RISK:       Price needs PRO margin back to ~26.8% (FY21 peak) while Fashion & Leather margin slides toward its pre-COVID 33% and inventory builds
DATA_WARNINGS:  1
