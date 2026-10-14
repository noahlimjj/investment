"""CELC Valuation Model (Celcuity Inc.)
As of 2026-10-13

Template: rNPV (Clinical Oncology: Gedatolisib in HR+/HER2- Breast Cancer)
All figures in USD (billions or per share as noted).
Terminal value is 0% post-patent expiry (2039).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_celc_model():
    shares = 48.932 # millions of diluted shares (10-Q Q2-26)
    price_spot = 64.38 # USD per share ($64.375 in 00_inputs.json)
    net_cash = -0.0003 # ~$0.00B (liquid cash $754.0M vs debt $754.4M)
    tax_rate = 0.210

    # Cost of Capital build:
    # US 10y 5.22% (FRED DGS10) + Oncology Biotech Beta 1.0 * ERP 5.0% = 10.22% -> round to 10.20%
    wacc_base = 0.1020
    wacc_bear = 0.1100
    wacc_bull = 0.0950

    # Explicit commercial revenue curves through 2039 LOE (13 years, launch 2027)
    # --- Scenario 1: BEAR CASE ---
    # VIKTORIA-1 shows modest PFS (1.5-2 mo); IV weekly infusion limits uptake vs oral capivasertib; Peak $0.7B; margin 28%
    rev_curve_bear = [0.05, 0.15, 0.30, 0.48, 0.60, 0.70, 0.70, 0.65, 0.55, 0.45, 0.30, 0.18, 0.08]
    margin_bear = 0.28
    pv_bear = 0.0
    for y, rev in enumerate(rev_curve_bear, 1):
        nopat = rev * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.88
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    eq_bear = pv_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # VIKTORIA-1 meets primary PFS endpoint in both PIK3CA-mutant and wildtype cohorts; Peak $1.8B; margin 35%
    rev_curve_base = [0.08, 0.25, 0.55, 0.95, 1.35, 1.65, 1.80, 1.80, 1.65, 1.40, 1.00, 0.60, 0.25]
    margin_base = 0.35
    pv_base = 0.0
    for y, rev in enumerate(rev_curve_base, 1):
        nopat = rev * margin_base * (1 - tax_rate)
        fcf = nopat * 0.90
        pv_base += fcf / ((1 + wacc_base) ** y)
    eq_base = pv_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # VIKTORIA-1 demonstrates OS advantage; preferred 2L/3L regimen; solid tumor expansion; Peak $3.2B; margin 42%
    rev_curve_bull = [0.12, 0.40, 0.90, 1.60, 2.30, 2.80, 3.20, 3.20, 2.95, 2.50, 1.80, 1.10, 0.50]
    margin_bull = 0.42
    pv_bull = 0.0
    for y, rev in enumerate(rev_curve_bull, 1):
        nopat = rev * margin_bull * (1 - tax_rate)
        fcf = nopat * 0.92
        pv_bull += fcf / ((1 + wacc_bull) ** y)
    eq_bull = pv_bull + net_cash
    per_share_bull = eq_bull * 1000.0 / shares

    # Probability weights: 30% Bear / 50% Base / 20% Bull
    p_bear, p_base, p_bull = 0.30, 0.50, 0.20
    weighted_ev = (per_share_bear * p_bear) + (per_share_base * p_base) + (per_share_bull * p_bull)

    print("================================================================================")
    print("CELCUITY INC. (CELC) rNPV VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE (Peak $0.7B): ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BASE CASE (Peak $1.8B): ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BULL CASE (Peak $3.2B): ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    mos_required = 0.30
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"ENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_celc_model()
