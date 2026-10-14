"""Valuation model for ASML Holding N.V. (ASML.AS)
Executed DCF scenarios and reverse DCF according to methodologies/valuation.py
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from methodologies.valuation import dcf, reverse_dcf, sensitivity, peg_is_valid

BASE_REV = 32667.0       # FY2025 EUR millions
NET_CASH = 8931.0        # Cash 12916 - Debt 3985 EUR millions
SHARES = 389.0           # Diluted shares millions
SPOT_PRICE = 1509.60     # Spot price EUR
RAW_CLOSE = 1575.80      # Official raw close EUR

# WACC: Risk free (NL 10y) 3.564% + Blume Beta (1.202) * ERP (5.0%) = 9.574% -> 9.5%
WACC_BASE = 0.095

print(f"{'='*70}")
print(f"VALUATION MODEL EXECUTION: ASML.AS")
print(f"{'='*70}\n")

# 1. Bear Case (China export clampdown, foundry capex digestion)
# Growth: 6% tapering to 3%; EBITDA margin 33.0% (EBIT 29.5%); WACC 10.0%, g 2.0%
g_bear = [0.06, 0.06, 0.05, 0.05, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03]
res_bear = dcf(
    base_revenue=BASE_REV,
    growth=g_bear,
    ebitda_margin=[0.33] * 10,
    capex_pct=[0.048] * 10,
    da_pct=[0.035] * 10,
    tax=0.18,
    wacc=0.10,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_growth=0.02,
    terminal_roic=0.20,
    mid_year=True
)

# 2. Trough Case (Normalized baseline)
g_trough = [0.09, 0.09, 0.08, 0.08, 0.07, 0.06, 0.05, 0.05, 0.04, 0.04]
res_trough = dcf(
    base_revenue=BASE_REV,
    growth=g_trough,
    ebitda_margin=[0.355] * 10,
    capex_pct=[0.045] * 10,
    da_pct=[0.032] * 10,
    tax=0.18,
    wacc=0.095,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_growth=0.025,
    terminal_roic=0.25,
    mid_year=True
)

# 3. Base Case (AI & 2nm demand drives High-NA ramp)
g_base = [0.13, 0.13, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05]
res_base = dcf(
    base_revenue=BASE_REV,
    growth=g_base,
    ebitda_margin=[0.377] * 10,  # 34.6% EBIT + 3.1% D&A
    capex_pct=[0.042] * 10,
    da_pct=[0.031] * 10,
    tax=0.18,
    wacc=0.095,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_growth=0.030,
    terminal_roic=0.30,
    mid_year=True
)

# 4. Bull Case (High-NA supercycle, EUV gross margins >55%)
g_bull = [0.17, 0.16, 0.15, 0.14, 0.12, 0.11, 0.09, 0.08, 0.07, 0.06]
res_bull = dcf(
    base_revenue=BASE_REV,
    growth=g_bull,
    ebitda_margin=[0.40] * 10,   # 37.0% EBIT + 3.0% D&A
    capex_pct=[0.040] * 10,
    da_pct=[0.030] * 10,
    tax=0.18,
    wacc=0.090,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_growth=0.035,
    terminal_roic=0.35,
    mid_year=True
)

print(f"SCENARIOS:")
print(f"  Bear Case:   EUR {res_bear.per_share:>8.2f} (EV: EUR {res_bear.enterprise_value:,.0f}M, TV share: {res_bear.terminal_share*100:.1f}%)")
print(f"  Trough Case: EUR {res_trough.per_share:>8.2f} (EV: EUR {res_trough.enterprise_value:,.0f}M, TV share: {res_trough.terminal_share*100:.1f}%)")
print(f"  Base Case:   EUR {res_base.per_share:>8.2f} (EV: EUR {res_base.enterprise_value:,.0f}M, TV share: {res_base.terminal_share*100:.1f}%)")
print(f"  Bull Case:   EUR {res_bull.per_share:>8.2f} (EV: EUR {res_bull.enterprise_value:,.0f}M, TV share: {res_bull.terminal_share*100:.1f}%)\n")

# Reverse DCF: What constant revenue CAGR does current price imply?
rev_kwargs = dict(
    base_revenue=BASE_REV,
    years=10,
    ebitda_margin=[0.377] * 10,
    capex_pct=[0.042] * 10,
    da_pct=[0.031] * 10,
    tax=0.18,
    wacc=0.095,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_growth=0.030,
    terminal_roic=0.30,
    mid_year=True
)

implied_g_spot = reverse_dcf(price=SPOT_PRICE, **rev_kwargs)
implied_g_close = reverse_dcf(price=RAW_CLOSE, **rev_kwargs)

print(f"REVERSE DCF:")
print(f"  At spot price EUR {SPOT_PRICE:.2f}: Implies 10-year constant revenue CAGR of {implied_g_spot*100:.2f}%")
print(f"  At raw close  EUR {RAW_CLOSE:.2f}: Implies 10-year constant revenue CAGR of {implied_g_close*100:.2f}%\n")

# Sensitivity matrix
sens_kwargs = dict(
    base_revenue=BASE_REV,
    growth=g_base,
    ebitda_margin=[0.377] * 10,
    capex_pct=[0.042] * 10,
    da_pct=[0.031] * 10,
    tax=0.18,
    net_debt=-NET_CASH,
    shares=SHARES,
    terminal_roic=0.30,
    mid_year=True
)

wacc_vals = [0.085, 0.095, 0.105]
g_vals = [0.025, 0.030, 0.035]
sens_grid = sensitivity({'wacc': wacc_vals}, {'terminal_growth': g_vals}, **sens_kwargs)

print("SENSITIVITY MATRIX (Rows: WACC 8.5%, 9.5%, 10.5% | Cols: g 2.5%, 3.0%, 3.5%):")
for w, row in zip(wacc_vals, sens_grid):
    row_str = " | ".join(f"EUR {v:.2f}" for v in row)
    print(f"  WACC {w*100:.1f}% -> {row_str}")

# PEG validity
peg_valid, peg_reason = peg_is_valid(57.16, 28.66, 0.185)
print(f"\nPEG VALIDITY: {peg_valid} ({peg_reason})")
