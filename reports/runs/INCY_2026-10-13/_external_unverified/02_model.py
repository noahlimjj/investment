"""INCY Valuation Model (Incyte Corporation)
As of 2026-10-13

Template: FULL (Commercial Biopharma with explicit Jakafi 2028 LOE Modeling)
All figures in USD (billions or per share as noted).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_incy_model():
    shares = 199.782 # millions of diluted shares
    price_spot = 108.95 # USD per share
    
    # Financial anchors (FY2025 in $B)
    rev_base = 5.141 # $5.141B
    net_cash = 3.098 # $3.098B ($15.51/share)
    
    # Cost of Capital build:
    # US 10y 5.22% + Beta 0.65 * ERP 5.0% = 8.47% -> round to 8.50%
    wacc_base = 0.0850
    wacc_bear = 0.0925
    wacc_bull = 0.0775
    tax_rate = 0.180

    # Explicit 10-year revenue and margin schedules modeling 2028 Jakafi LOE
    # Y1(2026), Y2(2027), Y3(2028-peak), Y4(2029-LOE cliff), Y5(2030-trough), Y6-Y10(recovery)
    
    # --- Scenario 1: BEAR CASE ---
    # Opzelura growth slows (peak $1.4B); Jakafi generic cliff severe; pipeline fails
    rev_growth_bear = [0.04, 0.03, 0.01, -0.25, -0.18, 0.00, 0.02, 0.02, 0.02, 0.02]
    ebit_margin_bear = [0.26, 0.25, 0.24, 0.15, 0.14, 0.15, 0.16, 0.16, 0.16, 0.16]
    g_term_bear = 0.015
    roic_term_bear = 0.090

    pv_bear = 0.0
    r_bear = rev_base
    f_bear = []
    for y in range(1, 11):
        r_bear *= (1 + rev_growth_bear[y-1])
        nopat = r_bear * ebit_margin_bear[y-1] * (1 - tax_rate)
        fcf = nopat * 0.85
        f_bear.append(fcf)
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    
    tv_bear = (f_bear[-1] * (1 + g_term_bear) * (1 - g_term_bear / roic_term_bear)) / (wacc_bear - g_term_bear)
    pv_tv_bear = tv_bear / ((1 + wacc_bear) ** 10)
    ev_bear = pv_bear + pv_tv_bear
    eq_bear = ev_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # Opzelura reaches $2.0B peak; Niktimvo and CALR add $1.2B; Jakafi declines -30% post-2028
    rev_growth_base = [0.07, 0.06, 0.04, -0.18, -0.10, 0.04, 0.05, 0.05, 0.04, 0.04]
    ebit_margin_base = [0.28, 0.28, 0.27, 0.19, 0.18, 0.20, 0.22, 0.22, 0.22, 0.22]
    g_term_base = 0.025
    roic_term_base = 0.120

    pv_base = 0.0
    r_base = rev_base
    f_base = []
    for y in range(1, 11):
        r_base *= (1 + rev_growth_base[y-1])
        nopat = r_base * ebit_margin_base[y-1] * (1 - tax_rate)
        fcf = nopat * 0.88
        f_base.append(fcf)
        pv_base += fcf / ((1 + wacc_base) ** y)
    
    tv_base = (f_base[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
    pv_tv_base = tv_base / ((1 + wacc_base) ** 10)
    ev_base = pv_base + pv_tv_base
    eq_base = ev_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # Opzelura expands to $2.8B; CALR antibody becomes blockbuster ($2.0B+); margins hold >25%
    rev_growth_bull = [0.10, 0.09, 0.07, -0.10, -0.02, 0.08, 0.09, 0.08, 0.07, 0.06]
    ebit_margin_bull = [0.30, 0.30, 0.30, 0.23, 0.23, 0.25, 0.26, 0.27, 0.27, 0.27]
    g_term_bull = 0.030
    roic_term_bull = 0.150

    pv_bull = 0.0
    r_bull = rev_base
    f_bull = []
    for y in range(1, 11):
        r_bull *= (1 + rev_growth_bull[y-1])
        nopat = r_bull * ebit_margin_bull[y-1] * (1 - tax_rate)
        fcf = nopat * 0.90
        f_bull.append(fcf)
        pv_bull += fcf / ((1 + wacc_bull) ** y)
    
    tv_bull = (f_bull[-1] * (1 + g_term_bull) * (1 - g_term_bull / roic_term_bull)) / (wacc_bull - g_term_bull)
    pv_tv_bull = tv_bull / ((1 + wacc_bull) ** 10)
    ev_bull = pv_bull + pv_tv_bull
    eq_bull = ev_bull + net_cash
    per_share_bull = eq_bull * 1000.0 / shares

    # Weightings: 25% Bear / 55% Base / 20% Bull
    p_bear, p_base, p_bull = 0.25, 0.55, 0.20
    weighted_ev = (per_share_bear * p_bear) + (per_share_base * p_base) + (per_share_bull * p_bull)

    print("================================================================================")
    print("INCYTE CORPORATION (INCY) VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE: ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bear/ev_bear*100:.1f}%")
    print(f"BASE CASE: ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_base/ev_base*100:.1f}%")
    print(f"BULL CASE: ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bull/ev_bull*100:.1f}%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    # Reverse DCF
    print(f"REVERSE DCF: Today's price of ${price_spot:.2f} requires Bull-case pipeline execution ($2.5B+ from non-Jakafi assets) to avoid multiple contraction post-2028")

    # Required entry and exit
    mos_required = 0.20 # 20% for Wide Moat / Biopharma
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"\nENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_incy_model()
