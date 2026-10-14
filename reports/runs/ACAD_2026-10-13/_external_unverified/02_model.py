"""ACAD Valuation Model (ACADIA Pharmaceuticals Inc.)
As of 2026-10-13

Template: FULL (Commercial CNS Biopharma)
All figures in USD (billions or per share as noted).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_acad_model():
    shares = 172.305 # millions of diluted shares
    price_spot = 18.815 # USD per share
    
    # Financial anchors (FY2025 in $B)
    rev_base = 1.0715 # $1.0715B
    net_cash = 0.4977 # $0.4977B ($2.89/share)
    
    # Cost of Capital build:
    # US 10y 5.22% + Beta 0.65 * ERP 5.0% = 8.47% -> round to 8.50%
    wacc_base = 0.0850
    wacc_bear = 0.0925
    wacc_bull = 0.0775
    tax_rate = 0.210

    # --- Scenario 1: BEAR CASE ---
    # Daybue real-world GI discontinuations hurt refills; Nuplazid faces generic erosion post-2030
    # Group revenue CAGR 1.0%, Operating margin 12.0%, Capex/R&D reinvestment 15% of NOPAT
    rev_cagr_bear = 0.010
    margin_bear = 0.120
    g_term_bear = 0.015
    roic_term_bear = 0.090

    pv_bear = 0.0
    r_bear = rev_base
    f_bear = []
    for y in range(1, 11):
        r_bear *= (1 + rev_cagr_bear)
        nopat = r_bear * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.85
        f_bear.append(fcf)
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    
    tv_bear = (f_bear[-1] * (1 + g_term_bear) * (1 - g_term_bear / roic_term_bear)) / (wacc_bear - g_term_bear)
    pv_tv_bear = tv_bear / ((1 + wacc_bear) ** 10)
    ev_bear = pv_bear + pv_tv_bear
    eq_bear = ev_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # Daybue expands in Europe/Canada; Nuplazid stable through 2030; mid-cycle margin 18.0%
    rev_cagr_base = 0.035
    margin_base = 0.180
    g_term_base = 0.025
    roic_term_base = 0.120

    pv_base = 0.0
    r_base = rev_base
    f_base = []
    for y in range(1, 11):
        r_base *= (1 + rev_cagr_base)
        nopat = r_base * margin_base * (1 - tax_rate)
        fcf = nopat * 0.88
        f_base.append(fcf)
        pv_base += fcf / ((1 + wacc_base) ** y)
    
    tv_base = (f_base[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
    pv_tv_base = tv_base / ((1 + wacc_base) ** 10)
    ev_base = pv_base + pv_tv_base
    eq_base = ev_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # Daybue peak exceeds $700M; ACP-101 approved in PWS; operating margin expands to 24.0%
    rev_cagr_bull = 0.060
    margin_bull = 0.240
    g_term_bull = 0.030
    roic_term_bull = 0.150

    pv_bull = 0.0
    r_bull = rev_base
    f_bull = []
    for y in range(1, 11):
        r_bull *= (1 + rev_cagr_bull)
        nopat = r_bull * margin_bull * (1 - tax_rate)
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
    print("ACADIA PHARMACEUTICALS (ACAD) VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE: ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bear/ev_bear*100:.1f}%")
    print(f"BASE CASE: ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_base/ev_base*100:.1f}%")
    print(f"BULL CASE: ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bull/ev_bull*100:.1f}%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    # Reverse DCF: What 10-yr revenue growth at base margin does $18.82 discount?
    for g_test in [0.005, 0.012, 0.018, 0.025, 0.035]:
        pv_t = 0.0
        r_t = rev_base
        f_t = []
        for y in range(1, 11):
            r_t *= (1 + g_test)
            nopat = r_t * margin_base * (1 - tax_rate)
            fc = nopat * 0.88
            f_t.append(fc)
            pv_t += fc / ((1 + wacc_base) ** y)
        tv_t = (f_t[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
        eq_t = pv_t + (tv_t / ((1 + wacc_base) ** 10)) + net_cash
        val_t = eq_t * 1000.0 / shares
        if abs(val_t - price_spot) < 0.5:
            print(f"REVERSE DCF: Price ${price_spot:.2f} implies a constant 10-yr revenue CAGR of ~{g_test*100:.1f}% at mid-cycle 18.0% margin")
            break

    # Required entry and exit
    mos_required = 0.20 # 20% for Wide Moat / Biopharma
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"\nENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_acad_model()
