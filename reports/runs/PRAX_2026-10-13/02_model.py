"""PRAX Valuation Model (Praxis Precision Medicines, Inc.)
As of 2026-10-13

Template: rNPV (Clinical Neuroscience: Ulixacaltamide + PRAX-628)
All figures in USD (billions or per share as noted).
Terminal value is 0% post-patent expiry (2039).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_prax_model():
    shares = 27.920 # millions of diluted shares (10-Q Q2-26)
    price_spot = 248.69 # USD per share
    net_cash = 0.757 # $0.757B net cash ($27.13/share)
    tax_rate = 0.210

    # Cost of Capital build:
    # US 10y 5.22% (FRED DGS10) + Biotech Beta 1.0 * ERP 5.0% = 10.22% -> round to 10.20%
    wacc_base = 0.1020
    wacc_bear = 0.1100
    wacc_bull = 0.0950

    # Explicit commercial revenue curves through 2039 LOE (13 years, launch 2027)
    # --- Scenario 1: BEAR CASE ---
    # Ulixacaltamide Phase 3 is mixed/narrow, PRAX-628 faces Phase 3 CNS tolerability issues; Peak $0.8B by 2032; margin 28%
    rev_curve_bear = [0.05, 0.15, 0.35, 0.55, 0.70, 0.80, 0.80, 0.75, 0.65, 0.50, 0.35, 0.20, 0.10]
    margin_bear = 0.28
    pv_bear = 0.0
    for y, rev in enumerate(rev_curve_bear, 1):
        nopat = rev * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.88
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    eq_bear = pv_bear + net_cash
    per_share_bear = eq_bear * 1000.0 / shares

    # --- Scenario 2: BASE CASE ---
    # Ulixacaltamide approved in ET ($1.5B peak) + PRAX-628 approved in focal epilepsy ($1.2B peak); Peak $2.7B by 2033; margin 36%
    rev_curve_base = [0.10, 0.35, 0.80, 1.40, 2.00, 2.50, 2.70, 2.70, 2.50, 2.10, 1.50, 0.90, 0.40]
    margin_base = 0.36
    pv_base = 0.0
    for y, rev in enumerate(rev_curve_base, 1):
        nopat = rev * margin_base * (1 - tax_rate)
        fcf = nopat * 0.90
        pv_base += fcf / ((1 + wacc_base) ** y)
    eq_base = pv_base + net_cash
    per_share_base = eq_base * 1000.0 / shares

    # --- Scenario 3: BULL CASE ---
    # Ulixacaltamide global blockbuster in ET ($2.5B peak) + PRAX-628 best-in-class epilepsy blockbuster ($2.5B peak); Peak $5.0B; margin 42%
    rev_curve_bull = [0.15, 0.60, 1.40, 2.50, 3.60, 4.50, 5.00, 5.00, 4.60, 3.90, 2.80, 1.70, 0.80]
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
    print("PRAXIS PRECISION MEDICINES (PRAX) rNPV VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {shares:.3f}M | Net Cash: ${net_cash:.3f}B (${net_cash*1000/shares:.2f}/share)\n")

    print(f"BEAR CASE (Peak $0.8B): ${per_share_bear:.2f} (Upside: {(per_share_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BASE CASE (Peak $2.7B): ${per_share_base:.2f} (Upside: {(per_share_base - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%")
    print(f"BULL CASE (Peak $5.0B): ${per_share_bull:.2f} (Upside: {(per_share_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: 0.0%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    mos_required = 0.30
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"ENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_prax_model()
