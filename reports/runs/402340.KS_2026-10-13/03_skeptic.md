# Skeptic Audit: 402340.KS (SK Square Co., Ltd.) — as of 2026-10-13

## 1. Pre-Mortem (Written before reading the Quant model)
**The Structural Downside Thesis (Business worth >50% less in 5 years):**
SK Square is the archetypal Korean Chaebol holding company value trap. The superficial bull thesis rests on a seductive optical illusion: *"SK Square trades at a 47% discount to its Net Asset Value, so you are buying the world's leading AI memory company (SK Hynix) for 50 cents on the dollar."*

This reasoning is fatally flawed for three structural reasons:
1. **Underlying Asset Overvaluation:** The Net Asset Value is anchored on SK Hynix's peak-cycle market capitalization of >KRW 1,050T (operating margin 76%, priced at 5 years of peak earnings). When SK Hynix mean-reverts to mid-cycle profitability, the underlying NAV evaporates.
2. **Double Gearing & Discount Widening in a Downcycle:** In Korean market history, holding company discounts do not compress during memory downcycles—they expand from ~45% to 55%–65% as retail and foreign liquidity flees holdcos first. If SK Hynix falls to its mid-cycle value of KRW ~715,000 and the holdco discount widens to 55%, SK Square's equity value collapses to **KRW ~360,000/share** (-58% from today's KRW 857,000).
3. **The Regulatory 20% Prison:** SK Square holds 146.10M shares of SK Hynix, representing **20.0002%** of issued shares. Under Korea's Fair Trade Act, a holding company must maintain a strict 20% minimum ownership in a listed subsidiary. Management **cannot sell a single share of SK Hynix** to monetize the "discount" or fund meaningful share cancellations. SK Square is structurally trapped as a passive dividend conduit with zero corporate catalyst to close the discount.

---

## 2. Number Audit & Portfolio Verification

| # | Item / Metric | Model Value | Skeptic Verification & Finding | Impact on Valuation |
|---|---|---|---|---|
| 1 | **SK Hynix Shareholding** | 146,100,000 shares | **VERIFIED:** Matches DART business report (제5기) and Q2 2026 portfolio deck. Exactly 20.0002% ownership. | Locked at regulatory floor |
| 2 | **Look-Through Ratio** | 1.108716 Hynix sh / Square sh | **VERIFIED:** 146.10M Hynix shares divided by 131.77M SK Square shares. | Sound look-through multiplier |
| 3 | **Non-Hynix Portfolio Value** | KRW 4.01T book; KRW 2.81T after 30% haircut | **AUDITED:** Unlisted stakes (11Street, T map Mobility, Content WAVVE) are chronically unprofitable venture assets. A 30% haircut is conservative; even at 100% write-off, per-share value changes by only KRW 21,300 (2.5%). | Minor impact (2.5% of NAV) |
| 4 | **Holdco Net Cash** | KRW 0.80T cash, 0 debt | **CONFIRMED:** Holdco balance sheet is debt-free. | Clean |
| 5 | **Price of Record** | KRW 857,000 (yfinance) | **AUDITED:** Naver KRX close was KRW 867,000 (1.2% variance). 857,000 is preserved for data-layer consistency. | Verified |
| 6 | **Market NAV per share** | KRW 1,636,378 | **VERIFIED:** Spot market NAV confirms the optical 47.6% market discount. | Accurate optical baseline |

---

## 3. Portfolio Redundancy Audit (SK Square vs SK Hynix)
- **Extreme Single-Asset Concentration:** SK Hynix represents **98.0% of SK Square's Net Asset Value**. SK Square is functionally a levered derivative proxy for SK Hynix wrapped in holding company governance friction.
- **Redundancy Finding:** The user already holds SK Hynix directly. Holding both SK Square and SK Hynix creates severe, uncompensated single-asset risk in memory hardware.
- **Does the 47% Discount Justify Owning SK Square Over Direct SK Hynix?**
  - **No.** As demonstrated in the Quant model, SK Square's current share price (KRW 857,000) is **4.7% HIGHER** than the un-discounted intrinsic asset value of its underlying holdings (KRW 818,808).
  - Investors are buying a peak-cycle memory stock through a discount that cannot be monetized. Direct ownership of SK Hynix provides liquidity, direct voting rights, and eliminates the Chaebol holding company discount overhang.

---

## 4. Capital Allocation Assessment: Grade C
1. **Value-Up Execution:** Management retired KRW ~310B of treasury shares in 2023–2024 and completed small buyback tranches. However, relative to a KRW 113T market cap, these returns are microscopic (~0.3% yield).
2. **Inability to Reallocate Capital:** Because the SK Hynix stake cannot be trimmed without violating the 20% Fair Trade Act rule, SK Square cannot pivot capital into other investments.
3. **Loss-Making Unlisted Bets:** E-commerce (11Street) and media (WAVVE) investments have consumed substantial capital with negligible or negative returns on capital.

---

## 5. Valuation Synthesis & Scenarios

| Scenario | Hynix Value Basis | Holdco Discount | SOTP Fair Value (KRW) | SOTP Fair Value (USD) | Upside vs Spot |
|---|---|---|---|---|---|
| **Bear Case** | Hynix Bear (KRW 411k) | 50% discount | KRW 241,610 | $180.10 | -71.8% |
| **Base Case** | **Hynix Expected Value (KRW 714k)** | **40% discount** | **KRW 491,285** | **$366.20** | **-42.7%** |
| **Bull Case** | Hynix Bull (KRW 1.27M) | 30% discount | KRW 1,002,812 | $747.49 | +17.0% |

- **Current Price:** **KRW 857,000** ($638.80 USD).
- **Base Fair Value:** **KRW 491,285** ($366.20 USD).
- **Margin of Safety:** **-42.7%**.
- **Asymmetry:** Downside to Bear (-71.8%) massively outweighs Upside to Bull (+17.0%).

---

## 6. Verdict Recommendation: TRIM
- **Required Margin of Safety:** 40% for Holdcos / Cyclical underlying.
- **Entry Below:** Fair Value × 0.60 = KRW 491,285 × 0.60 = **KRW 294,771**.
- **Exit Above:** Fair Value × 1.30 = KRW 491,285 × 1.30 = **KRW 638,670**.
- **Portfolio Status:** Held in active portfolio.
- **Recommendation:** **TRIM** (Conviction: **HIGH**).
  - Spot price (KRW 857,000) trades 34% above the Exit Above threshold (KRW 639,000).
  - SK Square should be trimmed immediately to eliminate redundant peak-cycle memory risk.

**Final Verdict:** **TRIM** (Conviction: **HIGH**).
