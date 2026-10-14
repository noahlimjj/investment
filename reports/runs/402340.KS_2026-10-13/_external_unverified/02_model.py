"""SOTP Valuation Model for SK Square (402340.KS)
As of 2026-10-13

Values SK Square as a pure holding company based on:
1. Look-through valuation of 146,100,000 SK Hynix shares from pipeline run 000660.KS_2026-10-13
2. Non-hynix portfolio assets and holdco net cash
3. Structural Korean holdco discount analysis
"""

def run_sotp():
    # Share counts
    sq_shares = 131774099
    hynix_shares_held = 146100000
    lookthrough_ratio = hynix_shares_held / sq_shares # 1.108716

    # Non-hynix assets (KRW billions)
    # Q2 portfolio update / NAV table
    non_hynix_portfolio_book = 4010.0 # KRW 4.01T
    haircut_non_hynix = 0.30 # 30% haircut on unlisted assets
    non_hynix_val = non_hynix_portfolio_book * (1 - haircut_non_hynix) # 2.807T
    holdco_net_cash = 800.0 # KRW 0.80T net cash, 0 debt
    total_non_hynix_krw = (non_hynix_val + holdco_net_cash) * 1e9 # to KRW
    non_hynix_per_sq_share = total_non_hynix_krw / sq_shares # KRW 27,373

    # SK Hynix values from 000660.KS_2026-10-13 pipeline run
    hynix_price = 1443000.0
    hynix_bear = 411148.0
    hynix_base = 727950.0
    hynix_bull = 1267426.0
    hynix_ev = 713831.0 # 30% Bear, 55% Base, 15% Bull

    # SK Square price
    sq_price = 857000.0
    fx_krw_usd = 0.0007453897851519287

    # 1. Market NAV Analysis (at spot prices)
    market_nav_hynix = hynix_shares_held * hynix_price
    market_nav_total = market_nav_hynix + (non_hynix_portfolio_book + holdco_net_cash) * 1e9
    market_nav_per_share = market_nav_total / sq_shares
    current_market_discount = (market_nav_per_share - sq_price) / market_nav_per_share

    # 2. Look-Through Intrinsic SOTP (Pre-discount)
    sotp_gross_bear = (hynix_bear * lookthrough_ratio) + non_hynix_per_sq_share
    sotp_gross_base = (hynix_base * lookthrough_ratio) + non_hynix_per_sq_share
    sotp_gross_bull = (hynix_bull * lookthrough_ratio) + non_hynix_per_sq_share
    sotp_gross_ev = (hynix_ev * lookthrough_ratio) + non_hynix_per_sq_share

    # 3. Holding Company Discount Scenarios
    # Historical Korea holdco discount is 35% - 55%
    discounts = [0.0, 0.30, 0.40, 0.45, 0.50]

    print("================================================================================")
    print("SK SQUARE (402340.KS) SOTP VALUATION AUDIT")
    print("================================================================================")
    print(f"SK Square Shares: {sq_shares:,}")
    print(f"SK Hynix Shares Held: {hynix_shares_held:,} ({lookthrough_ratio:.6f} per Square share)")
    print(f"Non-Hynix Net Assets per share: KRW {non_hynix_per_sq_share:,.0f}")
    print(f"Current SK Square Price: KRW {sq_price:,.0f} (${sq_price * fx_krw_usd:.2f} USD)")
    print(f"Current Market NAV per share: KRW {market_nav_per_share:,.0f}")
    print(f"Current Implied Market Discount: {current_market_discount*100:.1f}%\n")

    print("--- SOTP Gross Asset Value (Look-Through to Pipeline Hynix Model) ---")
    print(f"Bear (Hynix 411k):  KRW {sotp_gross_bear:,.0f} (${sotp_gross_bear * fx_krw_usd:.2f})")
    print(f"Base (Hynix 728k):  KRW {sotp_gross_base:,.0f} (${sotp_gross_base * fx_krw_usd:.2f})")
    print(f"Bull (Hynix 1.27M): KRW {sotp_gross_bull:,.0f} (${sotp_gross_bull * fx_krw_usd:.2f})")
    print(f"Weighted EV:        KRW {sotp_gross_ev:,.0f} (${sotp_gross_ev * fx_krw_usd:.2f})\n")

    print("--- SOTP Fair Value Across Holdco Discounts ---")
    for d in discounts:
        val = sotp_gross_ev * (1 - d)
        upside = (val - sq_price) / sq_price * 100
        print(f"Discount {d*100:4.1f}%: Fair Value KRW {val:,.0f} (${val * fx_krw_usd:.2f} USD) | Upside: {upside:+.1f}%")

    base_discount = 0.40 # standard Korean chaebol holdco discount
    fv_base = sotp_gross_ev * (1 - base_discount)
    entry_below = fv_base * 0.60 # 40% margin of safety
    exit_above = fv_base * 1.30

    print("\n--- Summary for Base Holdco Discount (40%) ---")
    print(f"FAIR VALUE:  KRW {fv_base:,.0f} (${fv_base * fx_krw_usd:.2f} USD)")
    print(f"UPSIDE:      {(fv_base - sq_price)/sq_price*100:+.1f}%")
    print(f"ENTRY BELOW: KRW {entry_below:,.0f} (${entry_below * fx_krw_usd:.2f} USD)")
    print(f"EXIT ABOVE:  KRW {exit_above:,.0f} (${exit_above * fx_krw_usd:.2f} USD)")

if __name__ == "__main__":
    run_sotp()
