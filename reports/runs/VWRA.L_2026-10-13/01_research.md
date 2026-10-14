<!-- pipeline:value-researcher -->
# Research dossier: VWRA.L (as of 2026-10-13)

## 0. Routing
FUND. Passive global equity UCITS ETF; sec_facts.py not applicable (exit not run). Operating-company metrics do not apply (fundamentals.py warning).

## 1. Snapshot
- Price 193.34 USD (yfinance via methodologies/fundamentals.py, close 2026-10-13); quote ccy USD, LSE line. Bid 193.34 / ask 193.36 = spread about 0.01% (yfinance snapshot, 2026-10-13; indicative only).
- NAV US$193.64 at close 12 Oct 2026 (Vanguard UK page, accessed 2026-10-13); yfinance navPrice 193.7734.
- 12m price change +18.1% (yfinance daily closes, 163.70 on 2025-10-13 to 193.34), 3y +81.0%, 5y +72.9% (price only, USD, own calc from yfinance history; ex-dividend not applicable as fund accumulates, so price = total return).
- 52w range from daily closes: 161.84 (2025-11-21) to 195.82 (2026-08-17). CONFLICT: yfinance info field says 140.22 to 202.3. Not reconciled; closes used.
- AUM: share class US$60.19B; total fund assets US$87.29B (Vanguard UK page, no as-of date; yfinance totalAssets 87.29B agrees). justETF shows EUR 55,367m (undated, differs - likely share class, different date/FX).
- Shares outstanding date 30 Sep 2026 (count not extracted: UNKNOWN).
- 10y yield: not relevant to FUND; UNKNOWN (not collected).

## 2. Fund facts
- Name: Vanguard FTSE All-World UCITS ETF (USD) Accumulating, ticker VWRA (Bloomberg VWRA LN), ISIN IE00BK5BQT80. Issuer Vanguard Group (Ireland) Ltd.
- Domicile: Ireland (Vanguard UK page; justETF).
- TER/OCF: 0.14% p.a. (Vanguard UK page, undated; justETF 0.14%). CONFLICT: trackingdifferences.com says 0.19% (stale source, not used).
- Distribution: accumulating, all dividends reinvested (Vanguard UK page).
- Index: FTSE All-World Index (TAWNT01U); 4,263 constituents (31 Aug 2026).
- Replication: physical, optimised sampling (justETF). Holdings 3,784 (Vanguard UK, 31 Aug 2026); justETF shows 3,759 (undated). CONFLICT <1%, differing as-of.
- Inception: share class 23 Jul 2019; LSE listing 25 Jul 2019.
- Portfolio turnover reported at 30 Jun 2026 (value not extracted: UNKNOWN).

## 3. Top 10 holdings (31 Aug 2026, Vanguard UK page; justETF agrees to 2dp)
NVIDIA 4.77%; Apple 4.24%; Microsoft 3.49%; Amazon 2.33%; Alphabet A 1.87%; TSMC 1.70%; Broadcom 1.59%; Alphabet C 1.44%; Meta 1.17%; Micron 1.00%. Combined 23.60% (justETF). Note Alphabet is two lines (3.31% combined).

## 4. Country weights (31 Aug 2026)
Vanguard UK: US 61.68% (benchmark 61.71%); Japan 6.00; Taiwan 3.31; UK 3.25; Canada 3.01; China 2.72; South Korea 2.50; France 1.99; Switzerland 1.97; Germany 1.89; Australia 1.59; India 1.59; Netherlands 1.14; Spain 0.87; Italy 0.80.
CONFLICT: justETF shows US 59.77%, Japan 5.97, Taiwan 3.29, UK 3.25 (same stated date; difference 1.9pp, likely classification method). Vanguard figure preferred as issuer primary.

## 5. Sector weights (31 Aug 2026, justETF only, coarse classification)
Technology 36.04%; Finance 18.63%; Industrials 9.16%; Consumer Non-Cyclicals 8.10%; Other 28.07%. Vanguard page gives no sector table. Single non-issuer source.

## 6. Tracking
- Annualised tracking error vs FTSE All-World: 1y 0.07%, 3y 0.07%, 5y 0.08% (Vanguard UK, 31 Aug 2026). This is volatility of difference, not tracking difference.
- Tracking difference 1/3/5y vs index: UNKNOWN (index total-return series not retrieved; no issuer performance table on fetched pages). Only indicative: trackingdifferences.com average TD 0.02%/yr "since 2020" (undated, low reliability).
- Fund NAV-based returns per justETF (undated, not stated whether annualised): 1y +23.61%, 3y +71.03%, 5y +79.66%, YTD +20.06%, since inception +142.14%. Likely EUR-denominated and not comparable to USD price returns above (1y +18.1%); do not mix.

## 7. Liquidity
Average volume 225,212 shares (yfinance info, window unstated). Indicative spread about 0.01% (see snapshot). Spread over time/depth: UNKNOWN. Also trades as VWRP (GBP), VWRL-family distributing sister is separate fund.

## 8. Index aggregate valuation
- Fund and benchmark P/E 21.0x, P/B 3.6x (Vanguard UK, 31 Aug 2026). Median market cap 190.0B fund vs 191.0B benchmark (via search summary of Vanguard page).
- yfinance trailingPE 20.97 (2026-10-13), agrees.
- Proxy, different index (MSCI ACWI, not FTSE): trailing P/E 23.24, forward P/E 17.13, dividend yield 1.59%, all as of 31 Jul 2026 (MSCI index page via search summary; forward P/E looks low relative to trailing, unverified). iShares ACWI ETF trailing P/E 25.18 (7 Oct 2026), trailing yield 1.40% (31 Aug 2026). Vendor P/E definitions differ (Vanguard 21.0x vs iShares FTSE All World 24.9x trailing in a search summary), so levels are not comparable across vendors.
- FTSE All-World dividend yield: UNKNOWN (a 1.32% figure at 30 Sep 2026 appears on Vanguard page unlabeled; do not use).
- CAPE: Siblis global index 29.12 (1 Jul 2026), different universe, proxy only. FTSE All-World CAPE: UNKNOWN.

## 9. Tax/structure notes (from instruction, not re-verified here)
Irish domicile, 15% US dividend WHT treaty rate, no US-situs estate exposure: user-stated premise, not independently sourced in this run. Singapore taxes no capital gains/foreign dividends for individuals generally: not verified here.

## 10. Data warnings & conflicts
- fundamentals.py warning: fund/ETF, operating-company metrics n/a.
- Conflicts: TER 0.14 vs 0.19 (stale); US weight 61.68 vs 59.77; holdings 3,784 vs 3,759; AUM figures by share class/currency; 52w range yfinance info vs closes; justETF returns vs price returns.
- UNKNOWN: tracking difference 1/3/5y; FTSE All-World forward P/E, dividend yield, CAPE; shares outstanding; turnover; spread history; sector table from issuer; 10y yield.
- Fetched pages passed through a summariser; numbers from WebFetch not deterministically extracted.
- Alphabet counted as two lines, so single-name concentration is understated.

## Sources
1. https://www.vanguard.co.uk/professional/product/etf/equity/9679/ftse-all-world-ucits-etf-usd-accumulating (accessed 2026-10-13)
2. https://www.vanguard.co.uk/professional/product/etf/equity/9505/ftse-all-world-ucits-etf-usd-distributing (sister fund page, same index data)
3. https://www.justetf.com/en/etf-profile.html?isin=IE00BK5BQT80
4. https://www.trackingdifferences.com/ETF/ISIN/IE00BK5BQT80
5. yfinance via methodologies/fundamentals.py, data/fundamentals.json (2026-10-13)
6. MSCI ACWI page https://www.msci.com/indexes/index/892400/msci-acwi-index (via search summary)
7. https://siblisresearch.com/data/world-cape-ratio/ (via search summary)
8. iShares ACWI NAV page https://www.ishares.com/us/products/239600/NAV (via search summary; the FTSA factsheet fetched was a different, newly launched fund and not used)
