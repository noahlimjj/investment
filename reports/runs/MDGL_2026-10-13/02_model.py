"""MDGL Valuation Model (Madrigal Pharmaceuticals, Inc.)
As of 2026-10-13

Template: rNPV (Commercial Single-Asset Biopharma: Rezdiffra in MASH)
All figures in USD (billions or per share as noted).
Terminal value is 0% post-patent expiry (2038).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_mdgl_model():
    shares = 23.104 # millions of diluted shares
    price_spot = 455.53 # USD per share
    net_cash = 0.510 # $0.510B ($22.07/share)
    
    # Cost of Capital build:
    # US 10y 5.22% + Biotech Beta 1.0 * ERP 5.0% = 10.22% -> round to 10.20%
    wacc_base = 0.1020
    wacc_bear = 0.1100
    wacc_bull = 0.0950
    tax_rate = 0.210

    # Explicit commercial revenue curves through 2038 patent expiry
    # FY25 actual: $0.958B. Ramp to peak (2030-2032), plateau, then LOE decline.
    
    # --- Scenario 1: BEAR CASE ---
    # Peak sales $2.2B by 2030; GLP-1s erode MASH share; operating margin 32%
    rev_curve_bear = [1.35, 1.70, 2.00, 2.20, 2.20, 2.10, 2.00, 1.80, 1.50, 1.20, 0.80, 0.40]
    margin_bear = 0.32
    pv_bear = 0.0
    for y, rev in enumerate(rev_curve_bear, 1):
        nopat = rev * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.88 # capex is minimal, working capital scales
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    eq_bear = pv_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # Peak sales $3.8B by 2031; Oral backbone alongside GLP-1s; operating margin 38%
    rev_curve_base = [1.50, 2.10, 2.70, 3.30, 3.70, 3.80, 3.80, 3.60, 3.20, 2.70, 1.80, 0.90]
    margin_base = 0.38
    pv_base = 0.0
    for y, rev in enumerate(rev_curve_base, 1):
        nopat = rev * margin_base * (1 - tax_rate)
        fcf = nopat * 0.90
        pv_base += fcf / ((1 + wacc_base) ** y)
    eq_base = pv_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # Peak sales $5.2B by 2031; Global blockbuster + fibrosis regression; operating margin 44%
    rev_curve_bull = [1.70, 2.50, 3.40, 4.30, 4.90, 5.20, 5.20, 5.00, 4.50, 3.80, 2.60, 1.30]
    margin_bull = 0.44
    pv_bull = 0.0
    for y, rev in enumerate(rev_curve_bull, 1):
        nopat = rev * margin_bull * (1 - tax_rate)
        fcf = nopat * 0.92
        pv_bull += fcf / ((1 + wacc_bull) ** y)
    eq_bull = pv_bull + net_cash
    per_share_bull = eq_bull * 1000.0 / shares

    # Weightings: 25% Bear / 55% Base / 20% Bull
    p_bear, p_base, p_bull = 0.25, 0.55, 0.20
    weighted_ev = (per_share_bear * p_bear) + (per_share_base * p_base) + (per_share_bull * p_bull)

    print("================================================================================")
    print("MADRIGAL PHARMACEUTICALS (MDGL) rNPV VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE (Peak $2.2B): ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BASE CASE (Peak $3.8B): ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BULL CASE (Peak $5.2B): ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    # Required entry and exit
    mos_required = 0.30 # 30% for rNPV Commercial
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"ENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_mdgl_model()
