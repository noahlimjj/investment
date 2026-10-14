"""TM Valuation Model (Toyota Motor Corporation)
As of 2026-10-13

Template: FULL (Modified Auto Industrial + Captive Finance)
All figures in USD (ADS equivalent) or JPY trillions as indicated.
1 TM ADS = 10 common shares.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_tm_model():
    ads_count = 1303.39 # millions of ADS
    fx_jpy_usd = 0.00631400803104043 # USD per JPY
    price_spot = 188.38 # USD per ADS
    
    # Financial anchors (FY2025 JPY trillions)
    rev_base_jpy = 48.04 # JPY 48.04T (~$303.3B USD)
    net_industrial_cash_jpy = 4.48 # JPY 4.48T
    captive_finance_equity_jpy = 4.00 # JPY 4.00T at 0.8x book
    
    # 1 Trillion JPY = 1,000,000,000,000 JPY * fx_jpy_usd = USD
    # In Billions USD: 1 JPY Trillion = 1000 * fx_jpy_usd Billion USD = $6.314B USD
    jpy_trillion_to_usd_billion = 1000.0 * fx_jpy_usd
    non_operating_assets_usd_b = (net_industrial_cash_jpy + captive_finance_equity_jpy) * jpy_trillion_to_usd_billion

    # Cost of Capital build (USD ADS basis):
    # US 10y 5.22% + Beta 0.58 * ERP 5.0% = 8.12% (binds to 8.0% USD floor)
    wacc_base = 0.0812
    wacc_bear = 0.0880
    wacc_bull = 0.0750

    # Tax rate
    tax_rate = 0.29

    # --- Scenario 1: BEAR CASE ---
    # Yen strengthens to 120-125, China volume collapses under BYD pressure, operating margin 6.0%
    rev_cagr_bear = 0.010
    margin_bear = 0.060
    g_term_bear = 0.015
    roic_term_bear = 0.08

    pv_bear = 0.0
    r_bear = rev_base_jpy
    f_bear = []
    for y in range(1, 11):
        r_bear *= (1 + rev_cagr_bear)
        nopat = r_bear * margin_bear * (1 - tax_rate)
        fcf = nopat * 0.78
        f_bear.append(fcf)
        pv_bear += fcf / ((1 + wacc_bear) ** y)
    
    tv_bear = (f_bear[-1] * (1 + g_term_bear) * (1 - g_term_bear / roic_term_bear)) / (wacc_bear - g_term_bear)
    pv_tv_bear = tv_bear / ((1 + wacc_bear) ** 10)
    ev_bear_jpy = pv_bear + pv_tv_bear
    eq_bear_usd_b = (ev_bear_jpy * jpy_trillion_to_usd_billion) + non_operating_assets_usd_b
    per_ads_bear = eq_bear_usd_b * 1000.0 / ads_count

    # --- Scenario 2: BASE CASE ---
    # Yen settles around 140-145, hybrid volume holds steady, mid-cycle operating margin 8.0%
    rev_cagr_base = 0.025
    margin_base = 0.080
    g_term_base = 0.020
    roic_term_base = 0.11

    pv_base = 0.0
    r_base = rev_base_jpy
    f_base = []
    for y in range(1, 11):
        r_base *= (1 + rev_cagr_base)
        nopat = r_base * margin_base * (1 - tax_rate)
        fcf = nopat * 0.80
        f_base.append(fcf)
        pv_base += fcf / ((1 + wacc_base) ** y)
    
    tv_base = (f_base[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
    pv_tv_base = tv_base / ((1 + wacc_base) ** 10)
    ev_base_jpy = pv_base + pv_tv_base
    eq_base_usd_b = (ev_base_jpy * jpy_trillion_to_usd_billion) + non_operating_assets_usd_b
    per_ads_base = eq_base_usd_b * 1000.0 / ads_count

    # --- Scenario 3: BULL CASE ---
    # Global hybrid share expands, solid state commercialization, operating margin 9.5%
    rev_cagr_bull = 0.040
    margin_bull = 0.095
    g_term_bull = 0.025
    roic_term_bull = 0.13

    pv_bull = 0.0
    r_bull = rev_base_jpy
    f_bull = []
    for y in range(1, 11):
        r_bull *= (1 + rev_cagr_bull)
        nopat = r_bull * margin_bull * (1 - tax_rate)
        fcf = nopat * 0.82
        f_bull.append(fcf)
        pv_bull += fcf / ((1 + wacc_bull) ** y)
    
    tv_bull = (f_bull[-1] * (1 + g_term_bull) * (1 - g_term_bull / roic_term_bull)) / (wacc_bull - g_term_bull)
    pv_tv_bull = tv_bull / ((1 + wacc_bull) ** 10)
    ev_bull_jpy = pv_bull + pv_tv_bull
    eq_bull_usd_b = (ev_bull_jpy * jpy_trillion_to_usd_billion) + non_operating_assets_usd_b
    per_ads_bull = eq_bull_usd_b * 1000.0 / ads_count

    # Weightings: 25% Bear / 55% Base / 20% Bull
    p_bear, p_base, p_bull = 0.25, 0.55, 0.20
    weighted_ev = (per_ads_bear * p_bear) + (per_ads_base * p_base) + (per_ads_bull * p_bull)

    print("================================================================================")
    print("TOYOTA MOTOR CORP (TM) VALUATION AUDIT")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {ads_count:.2f}M ADS | Net Industrial Cash + Finance Equity: ${non_operating_assets_usd_b:.2f}B (${non_operating_assets_usd_b*1000/ads_count:.2f}/ADS)\n")

    print(f"BEAR CASE: ${per_ads_bear:.2f} (Upside: {(per_ads_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bear/ev_bear_jpy*100:.1f}%")
    print(f"BASE CASE: ${per_ads_base:.2f} (Upside: {(per_ads_base - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_base/ev_base_jpy*100:.1f}%")
    print(f"BULL CASE: ${per_ads_bull:.2f} (Upside: {(per_ads_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bull/ev_bull_jpy*100:.1f}%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    # Reverse DCF
    for g_test in [0.01, 0.02, 0.028, 0.035, 0.045]:
        pv_t = 0.0
        r_t = rev_base_jpy
        f_t = []
        for y in range(1, 11):
            r_t *= (1 + g_test)
            nopat = r_t * margin_base * (1 - tax_rate)
            fc = nopat * 0.80
            f_t.append(fc)
            pv_t += fc / ((1 + wacc_base) ** y)
        tv_t = (f_t[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
        eq_t_usd_b = ((pv_t + tv_t / ((1 + wacc_base) ** 10)) * jpy_trillion_to_usd_billion) + non_operating_assets_usd_b
        val_t = eq_t_usd_b * 1000.0 / ads_count
        if abs(val_t - price_spot) < 5.0:
            print(f"REVERSE DCF: Price ${price_spot:.2f} implies a constant 10-yr revenue CAGR of ~{g_test*100:.1f}% at mid-cycle 8% margin")
            break

    # Required entry and exit
    mos_required = 0.20 # 20% for Wide Moat
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"\nENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_tm_model()
