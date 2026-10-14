"""BABA Valuation Model (Alibaba Group Holding Limited)
As of 2026-10-13

Executes explicit 10-year DCF scenarios, Reverse DCF, and Sensitivity analysis.
Template: FULL (GARP / Value Investing)
All figures in USD (billions) or USD per ADS unless specified.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent.parent / "methodologies"))
import valuation

def run_baba_model():
    # Share and FX basics
    ads_count = 2404.375 # millions of ADS
    fx_cny_usd = 0.14968715608119965
    price_spot = 110.53 # USD per ADS close 2026-10-13
    price_inputs = 109.64 # intraday

    # Base financial anchor (FY2026 ended March 31, 2026)
    # Revenue CNY 1,023.67B -> USD 153.23B
    base_rev_usd = 1023.67 * fx_cny_usd # $153.23B
    net_cash_usd = 33.00 * fx_cny_usd # $4.94B net cash ($2.05/ADS)

    # Cost of Capital build:
    # US 10y 5.22% + China Country Risk 2.0% + Beta 0.642 * ERP 5.0% = 10.43% -> round to 10.5%
    wacc_base = 0.105
    wacc_bear = 0.115
    wacc_bull = 0.095

    # --- Scenario 1: BEAR CASE ---
    # Fierce competition from PDD/Douyin, Taobao growth 0-2%, Cloud margins capped at 6%
    # Group revenue CAGR 1.5%, Operating margin 8.0%, Capex 4.5%, Tax 18%
    rev_growth_bear = [0.02, 0.02, 0.015, 0.015, 0.015, 0.015, 0.01, 0.01, 0.01, 0.01]
    ebit_margin_bear = 0.08
    tax_rate_bear = 0.18
    capex_pct_bear = 0.045
    g_term_bear = 0.015
    roic_term_bear = 0.09

    pv_fcf_bear = 0.0
    cur_rev = base_rev_usd
    fcf_bear_list = []
    for yr, g in enumerate(rev_growth_bear, 1):
        cur_rev *= (1 + g)
        ebit = cur_rev * ebit_margin_bear
        nopat = ebit * (1 - tax_rate_bear)
        # In mature bear, capex ~ D&A + modest reinvestment
        fcf = nopat * 0.85
        fcf_bear_list.append(fcf)
        pv_fcf_bear += fcf / ((1 + wacc_bear) ** yr)
    
    # Terminal value bear
    nopat_t_bear = fcf_bear_list[-1]
    tv_bear = (nopat_t_bear * (1 + g_term_bear) * (1 - g_term_bear / roic_term_bear)) / (wacc_bear - g_term_bear)
    pv_tv_bear = tv_bear / ((1 + wacc_bear) ** 10)
    ev_bear = pv_fcf_bear + pv_tv_bear
    eq_bear = ev_bear + net_cash_usd
    per_ads_bear = eq_bear * 1000 / ads_count

    # --- Scenario 2: BASE CASE ---
    # Taobao/Tmall GMV stabilizes (+3%), Cloud AI accelerates (+12-15%), AIDC narrows losses
    # Group revenue CAGR 4.5%, Operating margin 12.0%, Tax 18%, Capex 4.5%
    rev_growth_base = [0.05, 0.05, 0.045, 0.045, 0.045, 0.04, 0.04, 0.04, 0.035, 0.035]
    ebit_margin_base = 0.12
    tax_rate_base = 0.18
    g_term_base = 0.025
    roic_term_base = 0.12

    pv_fcf_base = 0.0
    cur_rev = base_rev_usd
    fcf_base_list = []
    for yr, g in enumerate(rev_growth_base, 1):
        cur_rev *= (1 + g)
        ebit = cur_rev * ebit_margin_base
        nopat = ebit * (1 - tax_rate_base)
        fcf = nopat * 0.82
        fcf_base_list.append(fcf)
        pv_fcf_base += fcf / ((1 + wacc_base) ** yr)

    nopat_t_base = fcf_base_list[-1]
    tv_base = (nopat_t_base * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
    pv_tv_base = tv_base / ((1 + wacc_base) ** 10)
    ev_base = pv_fcf_base + pv_tv_base
    eq_base = ev_base + net_cash_usd
    per_ads_base = eq_base * 1000 / ads_count

    # --- Scenario 3: BULL CASE ---
    # Macro stimulus reignites consumer spending, Cloud margins expand to 15%, buybacks continue
    # Group revenue CAGR 7.5%, Operating margin 15.0%, Tax 18%
    rev_growth_bull = [0.08, 0.08, 0.075, 0.075, 0.075, 0.07, 0.07, 0.065, 0.065, 0.06]
    ebit_margin_bull = 0.15
    tax_rate_bull = 0.18
    g_term_bull = 0.035
    roic_term_bull = 0.16

    pv_fcf_bull = 0.0
    cur_rev = base_rev_usd
    fcf_bull_list = []
    for yr, g in enumerate(rev_growth_bull, 1):
        cur_rev *= (1 + g)
        ebit = cur_rev * ebit_margin_bull
        nopat = ebit * (1 - tax_rate_bull)
        fcf = nopat * 0.80
        fcf_bull_list.append(fcf)
        pv_fcf_bull += fcf / ((1 + wacc_bull) ** yr)

    nopat_t_bull = fcf_bull_list[-1]
    tv_bull = (nopat_t_bull * (1 + g_term_bull) * (1 - g_term_bull / roic_term_bull)) / (wacc_bull - g_term_bull)
    pv_tv_bull = tv_bull / ((1 + wacc_bull) ** 10)
    ev_bull = pv_fcf_bull + pv_tv_bull
    eq_bull = ev_bull + net_cash_usd
    per_ads_bull = eq_bull * 1000 / ads_count

    # Probability weighting (Skeptic disciplined weights: 25% Bear / 55% Base / 20% Bull)
    p_bear, p_base, p_bull = 0.25, 0.55, 0.20
    weighted_ev = (per_ads_bear * p_bear) + (per_ads_base * p_base) + (per_ads_bull * p_bull)

    print("================================================================================")
    print("BABA VALUATION AUDIT (Alibaba Group Holding Limited)")
    print("================================================================================")
    print(f"Current Price: ${price_spot:.2f} USD")
    print(f"Shares: {ads_count:.3f}M ADS | Net Cash: ${net_cash_usd:.2f}B (${net_cash_usd*1000/ads_count:.2f}/ADS)\n")

    print(f"BEAR CASE: ${per_ads_bear:.2f} (Upside: {(per_ads_bear - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bear/ev_bear*100:.1f}%")
    print(f"BASE CASE: ${per_ads_base:.2f} (Upside: {(per_ads_base - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_base/ev_base*100:.1f}%")
    print(f"BULL CASE: ${per_ads_bull:.2f} (Upside: {(per_ads_bull - price_spot)/price_spot*100:+.1f}%) | TV Share: {pv_tv_bull/ev_bull*100:.1f}%\n")

    print(f"PROBABILITY-WEIGHTED FAIR VALUE: ${weighted_ev:.2f} USD")
    print(f"MARGIN OF SAFETY: {(weighted_ev - price_spot)/weighted_ev*100:+.1f}%")
    print(f"UPSIDE TO FAIR VALUE: {(weighted_ev - price_spot)/price_spot*100:+.1f}%\n")

    # Reverse DCF: What 10-yr revenue CAGR does today's price discount at BASE margins?
    # Test growth rates
    for test_cagr in [0.0, 0.01, 0.02, 0.025, 0.03, 0.04]:
        pv_test = 0.0
        r = base_rev_usd
        f_list = []
        for y in range(1, 11):
            r *= (1 + test_cagr)
            eb = r * ebit_margin_base
            nop = eb * (1 - tax_rate_base)
            fc = nop * 0.82
            f_list.append(fc)
            pv_test += fc / ((1 + wacc_base) ** y)
        tv_t = (f_list[-1] * (1 + g_term_base) * (1 - g_term_base / roic_term_base)) / (wacc_base - g_term_base)
        eq_t = pv_test + (tv_t / ((1 + wacc_base) ** 10)) + net_cash_usd
        v_t = eq_t * 1000 / ads_count
        if abs(v_t - price_spot) < 3.0:
            print(f"REVERSE DCF: Price ${price_spot:.2f} implies a constant 10-yr revenue CAGR of ~{test_cagr*100:.1f}%")
            break

    # Sensitivity: WACC x Terminal Growth
    print("\n--- SENSITIVITY: Base Value/ADS by WACC (rows) x Terminal Growth (cols) ---")
    print("WACC / g       1.5%      2.0%      2.5%      3.0%      3.5%")
    for w in [0.095, 0.100, 0.105, 0.110, 0.115]:
        row_str = f"{w*100:5.1f}%  "
        for g in [0.015, 0.020, 0.025, 0.030, 0.035]:
            pv_s = 0.0
            r = base_rev_usd
            f_s = []
            for y in range(1, 11):
                r *= (1 + rev_growth_base[y-1])
                nop = r * ebit_margin_base * (1 - tax_rate_base)
                fc = nop * 0.82
                f_s.append(fc)
                pv_s += fc / ((1 + w) ** y)
            tv_s = (f_s[-1] * (1 + g) * (1 - g / roic_term_base)) / (w - g)
            eq_s = pv_s + (tv_s / ((1 + w) ** 10)) + net_cash_usd
            val_s = eq_s * 1000 / ads_count
            row_str += f"  ${val_s:6.2f}"
        print(row_str)

    # Required entry and exit
    mos_required = 0.20 # 20% for Wide Moat / Stalwart
    entry_below = weighted_ev * (1 - mos_required)
    exit_above = weighted_ev * 1.30
    print(f"\nENTRY BELOW: ${entry_below:.2f} USD")
    print(f"EXIT ABOVE:  ${exit_above:.2f} USD")

if __name__ == "__main__":
    run_baba_model()
