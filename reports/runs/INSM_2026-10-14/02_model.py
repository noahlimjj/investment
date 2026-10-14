"""INSM Valuation Model (Insmed Incorporated)
As of 2026-10-14

Template: rNPV (Commercial / Clinical Biopharma: Arikayce + Brensocatib + TPIP)
All figures in USD (billions or per share as noted).
Terminal value is strictly 0.0% post-patent expiry (2039).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_insm_model():
    shares = 218.38 # millions of diluted shares (10-Q Q2-26)
    price_spot = 96.79 # USD per share as of 2026-10-14
    net_cash = 0.580 # $0.580B net cash ($2.66/share)
    tax_rate = 0.210

    # Cost of Capital build:
    # US 10y 5.22% (FRED DGS10) + Biotech Beta 1.0 * ERP 5.0% = 10.22% -> 10.20%
    wacc_base = 0.1020
    wacc_bear = 0.1100
    wacc_bull = 0.0950

    # Explicit commercial revenue curves through 2039 patent expiry (14 years)
    # --- Scenario 1: BEAR CASE ---
    # Peak company revenue $2.5B by 2030; modest bronchiectasis penetration, TPIP fails; margin 30%
    rev_curve_bear = [1.25, 1.60, 2.00, 2.30, 2.50, 2.50, 2.40, 2.20, 1.90, 1.60, 1.20, 0.80, 0.50, 0.20]
    margin_bear = 0.30
    pv_bear = 0.0
    for y, rev in enumerate(rev_curve_bear, 1):
        nopat = rev * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.88
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    eq_bear = pv_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # Peak company revenue $4.5B by 2031; brensocatib standard of care in NCFB ($3.2B) + Arikayce ($0.8B) + TPIP ($0.5B); margin 36%
    rev_curve_base = [1.35, 1.90, 2.60, 3.30, 4.00, 4.50, 4.50, 4.30, 3.90, 3.40, 2.70, 1.90, 1.10, 0.50]
    margin_base = 0.36
    pv_base = 0.0
    for y, rev in enumerate(rev_curve_base, 1):
        nopat = rev * margin_base * (1 - tax_rate)
        fcf = nopat * 0.90
        pv_base += fcf / ((1 + wacc_base) ** y)
    eq_base = pv_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # Peak company revenue $7.5B by 2032; brensocatib multi-indication blockbuster ($5.5B) + TPIP PAH success ($1.5B); margin 42%
    rev_curve_bull = [1.50, 2.40, 3.60, 4.80, 6.00, 7.00, 7.50, 7.50, 7.00, 6.00, 4.80, 3.40, 2.00, 1.00]
    margin_bull = 0.42
    pv_bull = 0.0
    for y, rev in enumerate(rev_curve_bull, 1):
        nopat = rev * margin_bull * (1 - tax_rate)
        fcf = nopat * 0.92
        pv_bull += fcf / ((1 + wacc_bull) ** y)
    eq_bull = pv_bull + net_cash
    per_share_bull = eq_bull * 1000.0 / shares

    # Probability weights: 25% Bear / 55% Base / 20% Bull
    p_bear, p_base, p_bull = 0.25, 0.55, 0.20
    weighted_ev = (per_share_bear * p_bear) + (per_share_base * p_base) + (per_share_bull * p_bull)

    # --- REVERSE DCF SOLVER ---
    target_eq = price_spot * shares / 1000.0
    target_pv = target_eq - net_cash
    # Standard base curve multipliers:
    # Find scale factor 'k' such that pv(k * rev_curve_base) == target_pv
    pv_unscaled = 0.0
    for y, rev in enumerate(rev_curve_base, 1):
        nopat = rev * margin_base * (1 - tax_rate)
        fcf = nopat * 0.90
        pv_unscaled += fcf / ((1 + wacc_base) ** y)
    implied_scale = target_pv / pv_unscaled
    implied_peak_sales = 4.50 * implied_scale

    print("================================================================================")
    print("INSMED INCORPORATED (INSM) rNPV VALUATION AUDIT (2026-10-14)")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE (Peak $2.5B, 30% margin): ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BASE CASE (Peak $4.5B, 36% margin): ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BULL CASE (Peak $7.5B, 42% margin): ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    print(f"REVERSE DCF: Implied Peak Sales to justify ${price_spot:.2f} = ${implied_peak_sales:.2f}B annually")
    print(f"Comparison: Base Case assumes $4.50B, Bull Case assumes $7.50B. Tape discounts {implied_peak_sales/4.50:.1f}x Base Case.\n")

    mos_required = 0.30
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"ENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_insm_model()
