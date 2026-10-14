"""Valuation Model for BATS.L (British American Tobacco p.l.c.)
Date: 2026-10-14
Currency: GBP (millions unless stated)
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

# Add methodologies to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "methodologies"))
from valuation import dcf, reverse_dcf, peg_is_valid

# -----------------------------------------------------------------------------
# 1. LOAD PRIMARY DATA & INPUTS
# -----------------------------------------------------------------------------
RUN_DIR = Path(__file__).resolve().parent
inputs_path = RUN_DIR / "00_inputs.json"
inputs = json.loads(inputs_path.read_text()) if inputs_path.exists() else {}

fund_path = Path("data/fundamentals.json")
fund_data = json.loads(fund_path.read_text()) if fund_path.exists() else {}
rec = fund_data.get("records", {}).get("BATS.L", {})

# Official prices
PRICE_RAW_GBP = 41.94  # Raw close from history (4,194 pence)
PRICE_VENDOR = rec.get("price", 42.25)
SHARES_M = 2150.425    # millions
MARKET_CAP_M = PRICE_RAW_GBP * SHARES_M  # ~£90,188m

# Balance sheet (GBP millions)
CASH_M = 2533.0
DEBT_M = 35063.0
NET_DEBT_M = DEBT_M - CASH_M  # £32,530m

# TTM Financial Base (GBP millions)
BASE_REV = 27100.0
NET_INCOME_M = 7765.0
DA_M = 2270.0
CAPEX_M = 704.0
FCF_M = 5638.0
OWNER_EARNINGS_M = 9331.0
GRORA_M = 22630.0

# Valuation parameters
TAX_RATE = 0.25         # UK statutory corporate tax rate
WACC_BASE = 0.082       # 8.2% WACC (UK 10y Gilt ~4.2% + 4.0% ERP/Spread)
TERMINAL_ROIC = 0.15    # 15% terminal ROIC on reinvested capital

print(f"{'='*80}")
print(f"BATS.L QUANTITATIVE VALUATION MODEL (2026-10-14)")
print(f"Price: £{PRICE_RAW_GBP:.2f} (Vendor: £{PRICE_VENDOR:.2f}) | Shares: {SHARES_M:.1f}m | Mkt Cap: £{MARKET_CAP_M:,.0f}m")
print(f"Net Debt: £{NET_DEBT_M:,.0f}m | EV: £{MARKET_CAP_M + NET_DEBT_M:,.0f}m | FCF: £{FCF_M:,.0f}m")
print(f"{'='*80}\n")

# -----------------------------------------------------------------------------
# 2. SCENARIO SPECIFICATIONS (10-YEAR HORIZON)
# -----------------------------------------------------------------------------
# Base Case: Combustibles price mix (+4%) offsets volume (-6%), New Categories grow +8%. Net rev CAGR +1.0%.
# EBITDA margin steady at 48.0%, capex at 2.6% of rev, D&A at 8.0%.
# Terminal growth: 1.0% (conservative inflation-lagging terminal rate).
n_years = 10
scenarios = {
    "Bear": {
        "growth": [-0.02, -0.02, -0.02, -0.015, -0.015, -0.01, -0.01, -0.01, -0.005, -0.005], # -1.3% CAGR
        "ebitda_margin": [0.44] * n_years,
        "capex_pct": [0.030] * n_years,
        "da_pct": [0.085] * n_years,
        "wacc": 0.090,
        "g_term": 0.005,
        "prob": 0.25,
        "desc": "US menthol ban implemented; accelerating volume decay; illicit vapes persist"
    },
    "Trough": {
        "growth": [0.00] * n_years, # 0% growth
        "ebitda_margin": [0.46] * n_years,
        "capex_pct": [0.027] * n_years,
        "da_pct": [0.082] * n_years,
        "wacc": 0.085,
        "g_term": 0.010,
        "prob": 0.30,
        "desc": "Stagnant revenues; pricing power fully matches combustible volume decline"
    },
    "Base": {
        "growth": [0.015, 0.015, 0.012, 0.012, 0.010, 0.010, 0.008, 0.008, 0.008, 0.008], # +1.1% CAGR
        "ebitda_margin": [0.485] * n_years,
        "capex_pct": [0.026] * n_years,
        "da_pct": [0.080] * n_years,
        "wacc": 0.082,
        "g_term": 0.015,
        "prob": 0.35,
        "desc": "New categories expand margins; pricing power intact; steady £1B+ annual buybacks"
    },
    "Bull": {
        "growth": [0.030, 0.030, 0.025, 0.025, 0.020, 0.020, 0.018, 0.018, 0.015, 0.015], # +2.2% CAGR
        "ebitda_margin": [0.510] * n_years,
        "capex_pct": [0.025] * n_years,
        "da_pct": [0.078] * n_years,
        "wacc": 0.078,
        "g_term": 0.020,
        "prob": 0.10,
        "desc": "US FDA cracks down on illicit vapes; Velo scales rapidly; accelerated deleveraging"
    }
}

results = {}
ev_weighted = 0.0

print(f"{'Scenario':<10} | {'WACC':<6} | {'Term g':<6} | {'Intrinsic/sh':<12} | {'Upside':<8} | {'Prob':<6} | {'Weighted':<10}")
print("-" * 75)

for name, sc in scenarios.items():
    res = dcf(
        base_revenue=BASE_REV,
        growth=sc["growth"],
        ebitda_margin=sc["ebitda_margin"],
        capex_pct=sc["capex_pct"],
        da_pct=sc["da_pct"],
        tax=TAX_RATE,
        wacc=sc["wacc"],
        net_debt=NET_DEBT_M,
        shares=SHARES_M,
        terminal_growth=sc["g_term"],
        terminal_roic=TERMINAL_ROIC,
        terminal_value=True,
        mid_year=True
    )
    ups = res.upside(PRICE_RAW_GBP) * 100.0
    w_val = res.per_share * sc["prob"]
    ev_weighted += w_val
    results[name] = (res, ups, sc)
    print(f"{name:<10} | {sc['wacc']*100:.1f}%  | {sc['g_term']*100:.1f}%  | £{res.per_share:<11.2f} | {ups:>+6.1f}% | {sc['prob']*100:.0f}%   | £{w_val:<9.2f}")

print("-" * 75)
print(f"PROBABILITY-WEIGHTED EXPECTED VALUE: £{ev_weighted:.2f}")
upside_ev = ((ev_weighted - PRICE_RAW_GBP) / PRICE_RAW_GBP) * 100.0
print(f"WEIGHTED MARGIN OF SAFETY / UPSIDE:  {upside_ev:+.1f}%\n")

# -----------------------------------------------------------------------------
# 3. REVERSE DCF (WHAT GROWTH IS PRICED IN TODAY?)
# -----------------------------------------------------------------------------
implied_growth = reverse_dcf(
    price=PRICE_RAW_GBP,
    base_revenue=BASE_REV,
    years=10,
    ebitda_margin=[0.485] * 10,
    capex_pct=[0.026] * 10,
    da_pct=[0.080] * 10,
    tax=TAX_RATE,
    wacc=WACC_BASE,
    net_debt=NET_DEBT_M,
    shares=SHARES_M,
    terminal_growth=0.015,
    terminal_roic=TERMINAL_ROIC,
    mid_year=True
)
print(f"REVERSE DCF ANALYSIS:")
print(f"At today's price of £{PRICE_RAW_GBP:.2f}, the market discounts a 10-year revenue CAGR of: {implied_growth*100:+.2f}%\n")

# -----------------------------------------------------------------------------
# 4. SENSITIVITY MATRIX (WACC x TERMINAL GROWTH)
# -----------------------------------------------------------------------------
waccs = [0.075, 0.080, 0.082, 0.085, 0.090]
g_terms = [0.005, 0.010, 0.015, 0.020]

print("SENSITIVITY MATRIX (Intrinsic Value per Share in £):")
base_sc = scenarios["Base"]
header = "WACC \\ g_term | " + " | ".join(f"{g*100:4.1f}%" for g in g_terms)
print(header)
print("-" * len(header))

for w in waccs:
    row = [f"{w*100:4.1f}%       | "]
    for g in g_terms:
        r = dcf(
            base_revenue=BASE_REV,
            growth=base_sc["growth"],
            ebitda_margin=base_sc["ebitda_margin"],
            capex_pct=base_sc["capex_pct"],
            da_pct=base_sc["da_pct"],
            tax=TAX_RATE,
            wacc=w,
            net_debt=NET_DEBT_M,
            shares=SHARES_M,
            terminal_growth=g,
            terminal_roic=TERMINAL_ROIC,
            terminal_value=True,
            mid_year=True
        )
        row.append(f"£{r.per_share:5.2f} | ")
    print("".join(row))

# -----------------------------------------------------------------------------
# 5. PETER LYNCH & BUFFETT OWNER EARNINGS METRICS
# -----------------------------------------------------------------------------
eps_ttm = NET_INCOME_M / SHARES_M
div_yield = 5.84
fwd_pe = rec.get("forward_pe", 10.9)
lynch_ratio = (2.0 + 5.84) / fwd_pe if fwd_pe else None
net_cash_per_share = (CASH_M - DEBT_M) / SHARES_M
net_cash_adj_pe = (PRICE_RAW_GBP - net_cash_per_share) / eps_ttm if eps_ttm > 0 else None
oe_yield = (OWNER_EARNINGS_M / MARKET_CAP_M) * 100.0
fcf_yield_val = (FCF_M / MARKET_CAP_M) * 100.0

print(f"\n{'='*80}")
print("LYNCH & BUFFETT METRICS:")
print(f"TTM Diluted EPS:           £{eps_ttm:.2f}")
print(f"Trailing P/E:              {PRICE_RAW_GBP / eps_ttm:.1f}x (Reported: {rec.get('trailing_pe', 14.5):.1f}x)")
print(f"Forward P/E:               {fwd_pe:.1f}x")
print(f"Owner Earnings Yield:      {oe_yield:.2f}% (£{OWNER_EARNINGS_M:,.0f}m / £{MARKET_CAP_M:,.0f}m)")
print(f"Free Cash Flow Yield:      {fcf_yield_val:.2f}% (£{FCF_M:,.0f}m / £{MARKET_CAP_M:,.0f}m)")
print(f"Dividend Yield:            5.84% (£2.45/share)")
print(f"Lynch Ratio:               {lynch_ratio:.2f} (EPS growth ~2% + 5.84% yield / Fwd P/E {fwd_pe:.1f}x)")
print(f"Net Cash / (Debt) per sh:  £{net_cash_per_share:.2f} (Net debt covers {abs(net_cash_per_share)/PRICE_RAW_GBP*100:.1f}% of price)")
print(f"Net-Cash-Adjusted P/E:     {net_cash_adj_pe:.1f}x")
print(f"PEG Gate Check:            Valid = {peg_is_valid(rec.get('trailing_pe', 14.5), fwd_pe, 0.08)}")
print(f"{'='*80}\n")
