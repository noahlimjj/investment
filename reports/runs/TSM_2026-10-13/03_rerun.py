"""TSM Skeptic re-run, 2026-10-13. Same engine and scenario structure as 02_model.py,
with the audited corrections applied one at a time so each delta is visible.

Corrections (see 03_skeptic.md section 2):
  C1 Temporal      rf 5.277% (^TNX close of 2026-10-07, mislabelled 10-13) -> 5.22% FRED DGS10 2026-10-08
                   (^TNX close 2026-10-13 = 5.208%, yfinance).
  C2 Temporal      3Q26 revenue is now reported: Jan-Sep 2026 NT$3,898,727M (6-K 2026-10-08,
                   accn 0001046179-26-000680) - 1H26 2,404,483.7 = NT$1,494,243M. It replaces the guide.
  C3 Comparability FY26 "+40% in US dollars" was applied to NT$ FY25 revenue. It is now applied in USD:
                   FY25 US$122.43B = 1Q25 25.53 (1Q26 35.90 / 1.406, 6-K 2026-04-16) + 2Q25 30.07
                   (2Q26 40.2 / 1.337, dossier) + 3Q25 33.10 (4Q25 33.73 / 1.019, 6-K 2026-01-15) + 4Q25 33.73.
                   4Q26 = 1.40 x 122.43 - (35.90 + 40.20 + 3Q26 US$) converted at the company's 32.0.
                   3Q26 US$ = NT$1,494,243 / 31.974 (yfinance TWD=X Jul-Sep 2026 average).
  C4 Model/temporal Valuation date: 02_model.py discounts from 30 Jun 2026 at year ends, then compares with a
                   13 Oct 2026 price. Apply the mid-year convention (x(1+WACC)^0.5 on EV), roll forward 105
                   days, and deduct dividends that a 13-Oct buyer no longer receives (NT$13.0/share = 2026
                   NT$24 plan - 1H26 paid 285,258.1 / 25,932.5 = 11.0).
  C5 Source fidelity Beta 1.0 is unsourced; yfinance TSM beta 1.239 (5y monthly). Skeptic uses the
                   Blume-adjusted 0.67 x 1.239 + 0.33 = 1.16. Kept as a DISAGREEMENT, shown separately.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from methodologies.valuation import dcf  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
F = json.loads((RUN / "facts.json").read_text())
A, T, M, BS, I = F["annual"], F["ttm"], F["market"], F["balance_sheet_latest"], F["interim"]
YRS = ["2021", "2022", "2023", "2024", "2025"]

PRICE_ADS, FX, ADS = M["price"], M["usdtwd"], 5
SHARES = M["common_shares_m"]
MCAP = M["market_cap_twd_m"]
PRICE_SH = PRICE_ADS * FX / ADS
CASH, DEBT, NCI = BS["cash_and_current_securities"], BS["total_debt"], BS["nci"]
NET_DEBT = DEBT + NCI - CASH
TAX = 0.18
BASE_REV = T["revenue"]
FY25 = A["revenue"]["2025"]
H1_26 = I["1H26"]["revenue"]
Q3_LO, Q3_HI = [x * 1000 * 32.0 for x in F["guidance"]["3Q26"]["revenue_usd_b"]]
SBC_PCT = T["sbc"] / T["revenue"]
K_CAL = A["d_and_a"]["2025"] / (sum(A["capex_ppe"][y] for y in YRS) / 5)

# ---- new primary-source inputs (C2, C3, C4)
YTD_SEP26 = 3_898_727                     # NT$M, 6-K 2026-10-08 monthly revenue report
Q3_ACT = YTD_SEP26 - H1_26                # NT$M
FX_3Q = 31.974                            # yfinance TWD=X Jul-Sep 2026 mean (66 obs)
USD_FY25 = 35.90 / 1.406 + 40.2 / 1.337 + 33.73 / 1.019 + 33.73
USD_1Q26, USD_2Q26 = 35.90, 40.2
USD_3Q26 = Q3_ACT / FX_3Q / 1000
DIV_GAP_SH = F["guidance"]["div_2026_twd_per_share"] - I["1H26"]["cash_dividends_paid"] / SHARES
ROLL_DAYS = 105                           # 30 Jun -> 13 Oct 2026


def wacc_for(rf, beta, erp=0.05):
    ke = rf + beta * erp
    we, wd = MCAP / (MCAP + DEBT), DEBT / (MCAP + DEBT)
    return we * ke + wd * rf * (1 - TAX)


def da_path(capex_pct, growth, base=BASE_REV, k=K_CAL):
    hist = [A["capex_ppe"][y] for y in ["2022", "2023", "2024", "2025"]] + [T["capex_ppe"]]
    r, out = base, []
    for g, c in zip(growth, capex_pct):
        r *= 1 + g
        out.append(k * sum(hist[-5:]) / 5 / r)
        hist.append(r * c)
    return out


def y1(q3, q4, h1_27_mult):
    return (q3 + q4 + H1_26 * h1_27_mult) / BASE_REV - 1


def q4_ntd(fy26_g, corrected, q3):
    if not corrected:                     # 02_model.py method: NT$ FY25 x (1+g)
        return FY25 * (1 + fy26_g) - H1_26 - q3
    usd_q3 = q3 / FX_3Q / 1000
    return (USD_FY25 * (1 + fy26_g) - USD_1Q26 - USD_2Q26 - usd_q3) * 1000 * 32.0


def scenarios(corrected_y1: bool):
    if corrected_y1:
        q3b = q3u = q3d = Q3_ACT
    else:
        q3b, q3u, q3d = (Q3_LO + Q3_HI) / 2, Q3_HI, Q3_LO
    base_g1 = y1(q3b, q4_ntd(0.40, corrected_y1, q3b), 1.25)
    bull_g1 = y1(q3u, q4_ntd(0.42, corrected_y1, q3u), 1.35)
    bear_g1 = y1(q3d, Q3_LO, 0.95)        # 4Q26 falls back to the 3Q guide floor; 1H27 -5%
    return {
        "BEAR": dict(growth=[bear_g1, -.10, .08, .08, .07, .06, .05, .05, .04, .03],
                     ebitda=[.68, .62, .63, .63, .63, .63, .63, .63, .63, .63],
                     capex=[.37, .38, .34, .32, .30, .29, .28, .27, .26, .26], g_t=.02, roic_t=.15),
        "BASE": dict(growth=[base_g1, .20, .17, .14, .12, .10, .08, .07, .05, .04],
                     ebitda=[.70, .69, .68, .68, .68, .68, .68, .68, .68, .68],
                     capex=[.37, .37, .35, .33, .31, .30, .29, .28, .27, .26], g_t=.03, roic_t=.25),
        "BULL": dict(growth=[bull_g1, .30, .25, .20, .16, .13, .10, .08, .06, .05],
                     ebitda=[.73, .72, .71, .71, .71, .71, .71, .71, .71, .71],
                     capex=[.37, .38, .36, .33, .30, .28, .27, .26, .25, .24], g_t=.04, roic_t=.35),
    }


def value(s, wacc, timing: bool, growth=None, ebitda_scale=1.0):
    gr = growth if growth is not None else s["growth"]
    r = dcf(base_revenue=BASE_REV, growth=gr,
            ebitda_margin=[e * ebitda_scale - SBC_PCT for e in s["ebitda"]],
            capex_pct=s["capex"], da_pct=da_path(s["capex"], gr), tax=TAX, wacc=wacc,
            net_debt=NET_DEBT, shares=SHARES, terminal_growth=s["g_t"],
            terminal_roic=s["roic_t"], wc_pct_of_delta_rev=0.10)
    if not timing:
        return r.per_share * ADS / FX, r
    ev = r.enterprise_value * (1 + wacc) ** 0.5            # mid-year convention
    eq_jun = ev - NET_DEBT
    eq_oct = eq_jun * (1 + wacc) ** (ROLL_DAYS / 365) - DIV_GAP_SH * SHARES
    return eq_oct / SHARES * ADS / FX, r


def implied_cagr(s, wacc, timing):
    lo, hi = -0.2, 0.6
    for _ in range(80):
        mid = (lo + hi) / 2
        if value(s, wacc, timing, growth=[mid] * 10)[0] < PRICE_ADS: lo = mid
        else: hi = mid
    return mid


def implied_irr(s, timing):
    lo, hi = 0.03, 0.25
    for _ in range(80):
        mid = (lo + hi) / 2
        if value(s, mid, timing)[0] > PRICE_ADS: lo = mid
        else: hi = mid
    return mid


if __name__ == "__main__":
    print(f"Price US${PRICE_ADS}/ADS (= 2026-10-12 close; yfinance 2026-10-13 print 439.57) | FX {FX}")
    print(f"3Q26 actual NT${Q3_ACT:,.0f}M vs guide NT${Q3_LO:,.0f}-{Q3_HI:,.0f}M (at 32); "
          f"US${USD_3Q26:.2f}B at {FX_3Q} vs guide US$44.6-45.8B")
    print(f"FY25 USD revenue (derived from releases) US${USD_FY25:.2f}B; FY26 at +40% = US${USD_FY25*1.4:.2f}B; "
          f"4Q26 implied US${USD_FY25*1.4-USD_1Q26-USD_2Q26-USD_3Q26:.2f}B")
    print(f"Dividend gap 30 Jun->13 Oct: NT${DIV_GAP_SH:.2f}/share = US${DIV_GAP_SH*ADS/FX:.2f}/ADS")

    W_Q = wacc_for(0.05277, 1.0)
    W_C1 = wacc_for(0.0522, 1.0)
    BETA_ADJ = 0.67 * 1.239 + 0.33
    W_C5 = wacc_for(0.0522, BETA_ADJ)
    W_RAW = wacc_for(0.0522, 1.239)
    print(f"\nWACC: Quant {W_Q:.3%} | C1 rf 5.22% {W_C1:.3%} | C5 beta {BETA_ADJ:.3f} {W_C5:.3%} "
          f"| raw beta 1.239 {W_RAW:.3%}")

    S_Q, S_C = scenarios(False), scenarios(True)
    steps = [
        ("Q0 Quant as published", S_Q, W_Q, False),
        ("C1 + rf 5.22%", S_Q, W_C1, False),
        ("C2+C3 + 3Q26 actual, FY26 growth in USD", S_C, W_C1, False),
        ("C4 + mid-year, roll-fwd, less divs (AUDITED, beta 1.0)", S_C, W_C1, True),
        ("C5 + beta 1.16 (SKEPTIC CENTRAL)", S_C, W_C5, True),
        ("    alt: raw beta 1.239", S_C, W_RAW, True),
    ]
    print("\nStep-by-step (US$/ADS)        BEAR     BASE     BULL   base vs prior step")
    prev = None
    for name, S, w, tm in steps:
        vals = {k: value(S[k], w, tm)[0] for k in ("BEAR", "BASE", "BULL")}
        d = "" if prev is None else f"{vals['BASE']/prev-1:+.1%}"
        print(f"{name:<56}{vals['BEAR']:>8.2f}{vals['BASE']:>9.2f}{vals['BULL']:>9.2f}   {d}")
        if not name.startswith("    "):
            prev = vals["BASE"]

    for label, w in (("AUDITED beta 1.0", W_C1), ("SKEPTIC beta 1.16", W_C5)):
        print(f"\n--- {label}: WACC {w:.3%}")
        for k in ("BEAR", "BASE", "BULL"):
            v, r = value(S_C[k], w, True)
            cagr = (r.rows[-1][1] / BASE_REV) ** 0.1 - 1
            print(f"  {k}: US${v:.2f}  TV share {r.terminal_share:.0%}  Y1 g {S_C[k]['growth'][0]:.1%}  "
                  f"10y rev CAGR {cagr:.1%}  Y1 rev {r.rows[0][1]:,.0f}")
        print(f"  Reverse DCF (BASE margins, same conventions): implied 10-yr revenue CAGR "
              f"{implied_cagr(S_C['BASE'], w, True):.1%}")
    print(f"\nImplied IRR on corrected BASE cash flows (with timing conventions): {implied_irr(S_C['BASE'], True):.2%}")
    print(f"Implied IRR on corrected BULL cash flows: {implied_irr(S_C['BULL'], True):.2%}")

    print("\nSkeptic BASE sensitivity (US$/ADS), WACC x terminal g, with C1-C4:")
    for w in (W_C5 - 0.01, W_C1, W_C5, W_C5 + 0.01):
        row = []
        for g in (0.02, 0.03, 0.04):
            s = dict(S_C["BASE"], g_t=g)
            row.append(value(s, w, True)[0])
        print(f"  {w:.2%}  " + "  ".join(f"{x:8.2f}" for x in row))
    print("\nSkeptic BASE at steady-state EBITDA 71.6% (TTM) / 64% (bear-ish):")
    for m in (0.716, 0.64):
        print(f"  {m:.1%}: US${value(S_C['BASE'], W_C5, True, ebitda_scale=m/0.68)[0]:.2f}")
