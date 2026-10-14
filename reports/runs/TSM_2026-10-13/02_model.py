"""TSM (TSMC ADR) valuation model, as of 2026-10-13. Quant stage of the three-agent pipeline.

Units: NT$ millions unless stated. DCF is done in NT$ per COMMON share, then converted to
US$ per ADS (x5 shares / spot USDTWD 32.133).
Every input is cited inline: (facts: ...) = facts.json, (dossier §n) = 01_research.md,
(fund: ...) = data/fundamentals.json. Items marked ASSUMPTION are the Quant's judgement.

Run:  python3 reports/runs/TSM_2026-10-13/02_model.py
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from methodologies.valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
F = json.loads((RUN / "facts.json").read_text())
FUND = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["TSM"]
A, T, M, BS, I = F["annual"], F["ttm"], F["market"], F["balance_sheet_latest"], F["interim"]
YRS = ["2021", "2022", "2023", "2024", "2025"]


def pct(x): return f"{x*100:.1f}%"
def hr(t): print(f"\n{'='*8} {t} {'='*(70-len(t))}")


# ------------------------------------------------------------------ market / units
PRICE_ADS = M["price"]                     # US$ (facts: market.price)
FX = M["usdtwd"]                           # NT$ per US$ (facts: market.usdtwd)
ADS_RATIO = 5                              # common shares per ADS (facts: market.adr_ratio)
SHARES = M["common_shares_m"]              # M common shares (facts: market.common_shares_m)
MCAP = M["market_cap_twd_m"]               # NT$M (facts: market.market_cap_twd_m)
PRICE_SH_TWD = PRICE_ADS * FX / ADS_RATIO  # NT$ per common share
CASH = BS["cash_and_current_securities"]   # (facts: balance_sheet_latest) 30 Jun 2026
DEBT = BS["total_debt"]
NCI = BS["nci"]
NET_CASH = CASH - DEBT
NET_DEBT_FOR_DCF = DEBT + NCI - CASH       # NCI treated as a claim ahead of TSMC common equity
EV = MCAP + NET_DEBT_FOR_DCF
TAX = 0.18                                 # 2Q26 effective 18.0% (dossier §2); FY25 17.0%
ONEOFF_EPS = I["2Q26"]["oneoff_vis_gain_eps"]          # NT$2.24 VIS gain (facts: interim.2Q26)
ONEOFF_NI = ONEOFF_EPS * SHARES                        # NT$M, after-tax EPS effect x shares

hr("0. Units, price and EV")
print(f"ADS price US${PRICE_ADS} x {FX} NT$/US$ / {ADS_RATIO} = NT${PRICE_SH_TWD:,.1f} per common share")
print(f"Market cap NT${MCAP:,.0f}M | cash+current securities {CASH:,.0f} | debt {DEBT:,.0f} | NCI {NCI:,.0f}")
print(f"Net cash {NET_CASH:,.0f} = NT${NET_CASH/SHARES:,.1f}/share | EV {EV:,.0f} (US${EV/FX/1000:,.1f}B)")

# ------------------------------------------------------------------ A. history & Lynch
hr("A. History, growth, Lynch metrics")
rev = {y: A["revenue"][y] for y in YRS}
ni = {y: A["net_income_parent"][y] for y in YRS}
gm = {y: A["gross_profit"][y] / rev[y] for y in YRS}
om = {y: A["operating_income"][y] / rev[y] for y in YRS}
nm = {y: ni[y] / rev[y] for y in YRS}
capi = {y: A["capex_ppe"][y] / rev[y] for y in YRS}
fcfm = {y: A["fcf_ocf_less_ppe"][y] / rev[y] for y in YRS}
print(f"{'FY':<6}{'Rev':>11}{'g':>8}{'GM':>8}{'OM':>8}{'NM':>8}{'EBITDA%':>9}{'D&A%':>7}{'Capex%':>8}{'Cx/DA':>7}{'FCF%':>7}")
prev = None
for y in YRS:
    da = A["d_and_a"][y]
    eb = f"{(A['operating_income'][y]+da)/rev[y]*100:.1f}%" if da else "UNK"
    dap = f"{da/rev[y]*100:.1f}%" if da else "UNK"
    cxda = f"{A['capex_ppe'][y]/da:.2f}" if da else "UNK"
    g = f"{(rev[y]/prev-1)*100:+.1f}%" if prev else "n/a"
    print(f"{y:<6}{rev[y]:>11,.0f}{g:>8}{pct(gm[y]):>8}{pct(om[y]):>8}{pct(nm[y]):>8}{eb:>9}{dap:>7}{pct(capi[y]):>8}{cxda:>7}{pct(fcfm[y]):>7}")
    prev = rev[y]
DA_TTM = T["depreciation"] + T["amortization"]
EBITDA_TTM = T["operating_income"] + DA_TTM
print(f"{'TTM':<6}{T['revenue']:>11,.0f}{'n/a':>8}"
      f"{pct(T['gross_profit']/T['revenue']):>8}{pct(T['operating_income']/T['revenue']):>8}"
      f"{pct(T['net_income_consolidated']/T['revenue']):>8}{pct(EBITDA_TTM/T['revenue']):>9}"
      f"{pct(DA_TTM/T['revenue']):>7}{pct(T['capex_ppe']/T['revenue']):>8}{T['capex_ppe']/DA_TTM:>7.2f}"
      f"{pct(T['fcf']/T['revenue']):>7}")
eb1h26 = (I["1H26"]["operating_income"] + I["1H26"]["depreciation"]) / I["1H26"]["revenue"]
print(f"1H26 EBITDA margin (op inc + depreciation, amortisation excluded: UNKNOWN for 1H) = {pct(eb1h26)}")

rev_cagr = (rev["2025"] / rev["2021"]) ** 0.25 - 1
ni_cagr = (ni["2025"] / ni["2021"]) ** 0.25 - 1
eps_cagr_23_25 = (A["eps_diluted_twd"]["2025"] / A["eps_diluted_twd"]["2023"]) ** 0.5 - 1
print(f"\nRevenue CAGR FY21-25 = (3,809,054/1,587,415)^(1/4)-1 = {pct(rev_cagr)}")
print(f"Net income (parent) CAGR FY21-25 = {pct(ni_cagr)}  [EPS FY21 UNKNOWN; shares flat "
      f"{A['diluted_shares_m']['2021']:,}M -> {SHARES:,}M so NI CAGR ~ EPS CAGR]")
print(f"EPS CAGR FY23-25 (2 yr) = {pct(eps_cagr_23_25)} | FY23 NI y/y = {pct(ni['2023']/ni['2022']-1)}, "
      f"FY23 rev y/y = {pct(rev['2023']/rev['2022']-1)}")
avg = lambda d: sum(d.values()) / len(d)
print(f"5-yr ranges: GM {pct(min(gm.values()))}-{pct(max(gm.values()))} (avg {pct(avg(gm))}); "
      f"OM {pct(min(om.values()))}-{pct(max(om.values()))} (avg {pct(avg(om))}); NM avg {pct(avg(nm))}; "
      f"capex/rev avg {pct(avg(capi))}; FCF margin avg {pct(avg(fcfm))}")

EPS_TTM = T["eps_diluted_twd"]
EPS_NORM = EPS_TTM - ONEOFF_EPS
EPS_MID = T["revenue"] * avg(nm) / SHARES          # TTM revenue x 5-yr avg net margin
pe_ttm, pe_norm, pe_mid = PRICE_SH_TWD / EPS_TTM, PRICE_SH_TWD / EPS_NORM, PRICE_SH_TWD / EPS_MID
PE_FWD_VENDOR = FUND["forward_pe"]                 # yfinance, unvalidated (dossier §1, §9)
print(f"\nP/E trailing = {PRICE_SH_TWD:,.1f} / EPS {EPS_TTM} = {pe_ttm:.1f}x")
print(f"P/E normalised (ex NT${ONEOFF_EPS} VIS gain) = {PRICE_SH_TWD:,.1f} / {EPS_NORM:.2f} = {pe_norm:.1f}x")
print(f"P/E mid-cycle = price / (TTM rev x 5-yr avg net margin {pct(avg(nm))} / shares = NT${EPS_MID:.2f}) = {pe_mid:.1f}x")
print(f"P/E forward (yfinance, basis unknown, unvalidated) = {PE_FWD_VENDOR:.1f}x")

DIV_SH = F["guidance"]["div_2026_twd_per_share"]
div_yield = DIV_SH / PRICE_SH_TWD
g_hist = ni_cagr                                   # consensus UNKNOWN -> only historical available
ok, why = peg_is_valid(pe_norm, PE_FWD_VENDOR, g_hist)
print(f"\nPEG gate peg_is_valid(trailing {pe_norm:.1f}, fwd {PE_FWD_VENDOR:.1f}, g {pct(g_hist)}) -> {ok} ({why})")
peg = pe_norm / (g_hist * 100)
peg_rev = pe_norm / (rev_cagr * 100)
print(f"PEG = normalised P/E / NI CAGR = {pe_norm:.1f} / {g_hist*100:.1f} = {peg:.2f} "
      f"(using revenue CAGR {rev_cagr*100:.1f} instead: {peg_rev:.2f}); consensus growth UNKNOWN")
lynch = (g_hist * 100 + div_yield * 100) / pe_norm
lynch_mid = (g_hist * 100 + div_yield * 100) / pe_mid
print(f"Dividend yield = NT${DIV_SH} / {PRICE_SH_TWD:,.1f} = {pct(div_yield)}")
print(f"Lynch ratio = (g {g_hist*100:.1f} + yld {div_yield*100:.2f}) / P/E {pe_norm:.1f} = {lynch:.2f}; "
      f"on mid-cycle P/E: {lynch_mid:.2f}")
nc_sh = NET_CASH / SHARES
print(f"Net-cash-adjusted P/E = ({PRICE_SH_TWD:,.1f} - net cash/sh {nc_sh:.1f}) / {EPS_NORM:.2f} = "
      f"{(PRICE_SH_TWD-nc_sh)/EPS_NORM:.1f}x")

# ------------------------------------------------------------------ B. quality
hr("B. Owner earnings, ROIC, capital intensity")
OE_FUND = FUND["owner_earnings"] / 1e6           # NT$M (fund: owner_earnings, FY2025, capex incl intangibles)
OE_FY25_PPE = ni["2025"] + A["d_and_a"]["2025"] - A["capex_ppe"]["2025"]
capex_ttm_all = T["capex_ppe"] + T["capex_intangibles"]
OE_TTM = T["net_income_consolidated"] + DA_TTM - capex_ttm_all
OE_TTM_NORM = OE_TTM - ONEOFF_NI
print(f"OE FY25 (fund) = NI 1,697,604 + D&A 688,096 - capex 1,282,597 = {OE_FUND:,.0f} "
      f"(US${FUND['owner_earnings_usd']/1e9:.1f}B); PPE-only capex version {OE_FY25_PPE:,.0f}")
print(f"OE TTM = NI {T['net_income_consolidated']:,.0f} + D&A {DA_TTM:,.0f} - capex {capex_ttm_all:,.0f} = {OE_TTM:,.0f}; "
      f"normalised (- VIS {ONEOFF_NI:,.0f}) = {OE_TTM_NORM:,.0f}")
print(f"SBC-adjusted: FY25 {OE_FUND-A['sbc']['2025']:,.0f} | TTM norm {OE_TTM_NORM-T['sbc']:,.0f}  (SBC {pct(T['sbc']/T['revenue'])} of rev)")
print(f"OE yield on mkt cap: FY25 {pct(OE_FUND/MCAP)} | TTM normalised {pct(OE_TTM_NORM/MCAP)}")
CAPEX_FY26_MID = 62_000 * 32.0                    # US$62B midpoint (facts: guidance) x company FX 32
fy26_rev = A["revenue"]["2025"] * 1.40            # "slightly above 40%" USD growth, assumed = NT$ growth
print(f"Forward check: FY26 capex mid US$62B x 32 = NT${CAPEX_FY26_MID:,.0f}M = {pct(CAPEX_FY26_MID/fy26_rev)} "
      f"of FY26E rev {fy26_rev:,.0f}; vs FY25 D&A 688,096 -> capex/D&A {CAPEX_FY26_MID/A['d_and_a']['2025']:.2f}x")
div25 = A["dividends_paid"]["2025"]
div26 = DIV_SH * SHARES
print(f"Dividends FY25 {div25:,.0f} = {pct(div25/ni['2025'])} of NI, {pct(div25/A['fcf_ocf_less_ppe']['2025'])} of FCF; "
      f"2026 plan NT${DIV_SH} x {SHARES:,.1f}M = {div26:,.0f} = {pct(div26/T['fcf'])} of TTM FCF")
print(f"Self-funding TTM: OCF {T['ocf']:,.0f} - capex {capex_ttm_all:,.0f} = FCF {T['fcf']:,.0f} > 2026 dividend {div26:,.0f}")
print(f"Net debt / OE = {-NET_CASH:,.0f} / {OE_TTM_NORM:,.0f} = {-NET_CASH/OE_TTM_NORM:.2f}x (net cash)")
print(f"Current portion LT liabilities {BS['lt_liabilities_current_portion']:,.0f} covered "
      f"{BS['cash_and_equivalents']/BS['lt_liabilities_current_portion']:.1f}x by cash; maturity ladder UNKNOWN")

print("\nROIC = NOPAT / (equity + debt - cash), tax 17% for annual (FY25 rate), 18% TTM")
for y in ["2024", "2025"]:
    nopat = A["operating_income"][y] * (1 - 0.17)
    ic = A["equity_parent"][y] + A["total_debt_incl_noncurrent_leases"][y] - A["cash_and_equivalents"][y]
    print(f"  FY{y}: NOPAT {nopat:,.0f} / IC {ic:,.0f} = {pct(nopat/ic)}")
print("  FY2021-23: debt UNKNOWN -> ROIC UNKNOWN. ROE (NI / year-end parent equity) instead:")
for y in YRS:
    print(f"    FY{y} ROE {pct(ni[y]/A['equity_parent'][y])}")
nopat_ttm = T["operating_income"] * (1 - TAX)
eq_parent_ttm = BS["total_equity"] - NCI
ic_ttm_cash = eq_parent_ttm + DEBT - BS["cash_and_equivalents"]
ic_ttm_all = eq_parent_ttm + DEBT - CASH
ROIC_TTM = nopat_ttm / ic_ttm_cash
print(f"  TTM: NOPAT {nopat_ttm:,.0f} / IC {ic_ttm_cash:,.0f} (cash only) = {pct(ROIC_TTM)}; "
      f"/ IC {ic_ttm_all:,.0f} (cash+current securities) = {pct(nopat_ttm/ic_ttm_all)}")
print("  Goodwill: UNKNOWN (not in facts.json) -> ROIC ex-goodwill test cannot be run")

# ------------------------------------------------------------------ D. discount rate
hr("D. Discount rate")
RF = M["us10y_pct"] / 100          # 5.277% (facts: market.us10y_pct, ^TNX 2026-10-13)
ERP, BETA = 0.05, 1.0              # ERP stated; no sourced beta in dossier -> 1.0
KE = RF + BETA * ERP
KD_PRE = RF                        # TSMC bond yields UNKNOWN -> proxy = US 10y (ASSUMPTION)
KD = KD_PRE * (1 - TAX)
WE, WD = MCAP / (MCAP + DEBT), DEBT / (MCAP + DEBT)
WACC_RAW = WE * KE + WD * KD
WACC = max(WACC_RAW, 0.08)
print(f"Ke = {RF:.3%} + {BETA} x {ERP:.0%} = {KE:.3%}")
print(f"Kd after tax = {KD_PRE:.3%} x (1-{TAX}) = {KD:.3%} (pre-tax Kd UNKNOWN, proxied by US 10y)")
print(f"Weights (market value): E {WE:.2%}, D {WD:.2%}  ->  WACC = {WACC_RAW:.3%}; USD floor 8% not binding")
alt = WE * (0.0522 + ERP) + WD * 0.0522 * (1 - TAX)
print(f"Alt: with FRED DGS10 5.22% (orchestrator note, 2026-10-08): WACC {alt:.3%}")
print("TWD-currency WACC: Taiwan 10y UNKNOWN -> TWD floor (local 10y + 4%) UNKNOWN")

# ------------------------------------------------------------------ E. DCF
hr("E. DCF scenarios (NT$M; year t = 12 months to 30 Jun of 2026+t; base = TTM to 2Q26)")
BASE_REV = T["revenue"]
N = 10
H1_26 = I["1H26"]["revenue"]
FY25 = A["revenue"]["2025"]
Q3_LO, Q3_HI = [x * 1000 * F["guidance"]["3Q26"]["fx"] for x in F["guidance"]["3Q26"]["revenue_usd_b"]]
SBC_PCT = T["sbc"] / T["revenue"]          # SBC deducted from EBITDA margin; share count held flat


def year1_growth(q3, fy26_growth, h1_27_growth):
    """Y1 = 3Q26 (guided) + 4Q26 (implied by FY26 growth) + 1H27 (= 1H26 x (1+g))."""
    fy26 = FY25 * (1 + fy26_growth)
    q4 = fy26 - H1_26 - q3
    y1 = q3 + q4 + H1_26 * (1 + h1_27_growth)
    return y1 / BASE_REV - 1, q3, q4


def da_path(capex_pct, growth, k=0.675):
    """D&A = k x trailing-5-period average capex. k calibrated on FY25: 688,096 / avg(FY21-25 capex)
    = 688,096 / 1,019,620 = 0.675. Seed history = FY22, FY23, FY24, FY25, TTM capex."""
    hist = [A["capex_ppe"][y] for y in ["2022", "2023", "2024", "2025"]] + [T["capex_ppe"]]
    r, out = BASE_REV, []
    for g, c in zip(growth, capex_pct):
        r *= 1 + g
        out.append(k * sum(hist[-5:]) / 5 / r)
        hist.append(r * c)
    return out


K_CAL = A["d_and_a"]["2025"] / (sum(A["capex_ppe"][y] for y in YRS) / 5)
print(f"D&A calibration k = 688,096 / {sum(A['capex_ppe'][y] for y in YRS)/5:,.0f} = {K_CAL:.3f}")
print(f"3Q26 guide NT$ (US$ x 32): {Q3_LO:,.0f}-{Q3_HI:,.0f}; SBC/rev deducted from EBITDA = {SBC_PCT:.4%}")

SCEN = {}
# ---- BASE: FY26 +40% (guide), 3Q26 mid, 1H27 +25% (~5-yr rev CAGR 24.5%), fade to 4%
g1, q3, q4 = year1_growth((Q3_LO + Q3_HI) / 2, 0.40, 0.25)
SCEN["BASE"] = dict(
    growth=[g1, .20, .17, .14, .12, .10, .08, .07, .05, .04],
    ebitda=[.70, .69, .68, .68, .68, .68, .68, .68, .68, .68],     # FY23-25 avg 68.2%; TTM 71.6% treated as peak
    capex=[.37, .37, .35, .33, .31, .30, .29, .28, .27, .26],      # FY26 guide 37%; "even more significantly higher" 3 yrs
    g_t=0.03, roic_t=0.25, note=f"Y1 = 3Q26 mid {q3:,.0f} + 4Q26 implied {q4:,.0f} + 1H27 (1H26 x1.25)")
# ---- BEAR: 3Q low, FY26 exactly +40% but 4Q flat to 3Q low; 1H27 -5% (FY23-like), Y2 -10% digestion
y1_bear = (Q3_LO * 2 + H1_26 * 0.95) / BASE_REV - 1
SCEN["BEAR"] = dict(
    growth=[y1_bear, -.10, .08, .08, .07, .06, .05, .05, .04, .03],
    ebitda=[.68, .62, .63, .63, .63, .63, .63, .63, .63, .63],     # -> OM ~40-41% = 5-yr low (FY21 40.9%)
    capex=[.37, .38, .34, .32, .30, .29, .28, .27, .26, .26],      # capex sticky into downturn (FY23: 43.9%)
    g_t=0.02, roic_t=0.15, note=f"Y1 = 2 x 3Q26 low {Q3_LO:,.0f} + 1H27 (1H26 x0.95)")
# ---- BULL: 3Q high, FY26 +42%, 1H27 +35% (= 1H26 pace +35.6%), N2/AI ramp
g1u, q3u, q4u = year1_growth(Q3_HI, 0.42, 0.35)
SCEN["BULL"] = dict(
    growth=[g1u, .30, .25, .20, .16, .13, .10, .08, .06, .05],
    ebitda=[.73, .72, .71, .71, .71, .71, .71, .71, .71, .71],     # 1H26 74.2% (dep only); Wei "68% GM I'll be happy"
    capex=[.37, .38, .36, .33, .30, .28, .27, .26, .25, .24],
    g_t=0.04, roic_t=0.35, note=f"Y1 = 3Q26 high {q3u:,.0f} + 4Q26 {q4u:,.0f} + 1H27 (1H26 x1.35)")


def kwargs(s, wacc=WACC, k=K_CAL, tax=TAX, wc=0.10, net_debt=NET_DEBT_FOR_DCF, ebitda_scale=1.0,
           capex_scale=1.0, growth=None):
    gr = growth if growth is not None else s["growth"]
    cx = [c * capex_scale for c in s["capex"]]
    return dict(growth=gr, ebitda_margin=[e * ebitda_scale - SBC_PCT for e in s["ebitda"]],
                capex_pct=cx, da_pct=da_path(cx, gr, k), tax=tax, wacc=wacc,
                net_debt=net_debt, shares=SHARES, terminal_growth=s["g_t"],
                terminal_roic=s["roic_t"], wc_pct_of_delta_rev=wc)


def to_ads(ps_twd, fx=FX): return ps_twd * ADS_RATIO / fx


RES = {}
for name in ("BEAR", "BASE", "BULL"):
    s = SCEN[name]
    kw = kwargs(s)
    r = dcf(base_revenue=BASE_REV, **kw)
    RES[name] = r
    print(f"\n--- {name}: WACC {WACC:.2%}, terminal g {s['g_t']:.1%}, terminal ROIC {s['roic_t']:.0%}, "
          f"tax {TAX:.0%}, WC 10% of d-rev ---\n    {s['note']}")
    print(f"{'Yr':<4}{'g':>7}{'Revenue':>11}{'EBITDA%':>8}{'D&A%':>7}{'OM%':>7}{'Capex%':>8}{'FCF':>11}{'FCF%':>7}{'PV':>11}")
    for (yr, rv, eb, ebit, da, cx, fcf, pvf), g in zip(r.rows, kw["growth"]):
        print(f"{yr:<4}{g*100:>6.1f}%{rv:>11,.0f}{eb/rv*100:>7.1f}%{da/rv*100:>6.1f}%{ebit/rv*100:>6.1f}%"
              f"{cx/rv*100:>7.1f}%{fcf:>11,.0f}{fcf/rv*100:>6.1f}%{pvf:>11,.0f}")
    avg_fcfm = sum(row[6] / row[1] for row in r.rows) / N
    cagr = (r.rows[-1][1] / BASE_REV) ** (1 / N) - 1
    flag = "  << TV > 75% FLAG" if r.terminal_share > 0.75 else ""
    print(f"10-yr rev CAGR {pct(cagr)} | avg FCF margin {pct(avg_fcfm)} (5-yr hist avg {pct(avg(fcfm))})")
    print(f"PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} | TV share {r.terminal_share:.0%}{flag}")
    print(f"EV {r.enterprise_value:,.0f} - net debt {NET_DEBT_FOR_DCF:,.0f} = equity {r.equity_value:,.0f}")
    print(f"VALUE: NT${r.per_share:,.1f}/share x {ADS_RATIO} / {FX} = US${to_ads(r.per_share):,.2f}/ADS "
          f"vs US${PRICE_ADS} -> {to_ads(r.per_share)/PRICE_ADS-1:+.1%}")

r10 = RES["BASE"].rows[-1]
nopat10 = r10[3] * (1 - TAX)
reinv10 = r10[5] - r10[4] + 0.10 * (r10[1] - RES["BASE"].rows[-2][1])
print(f"\nBASE Y10 consistency: reinvestment {reinv10:,.0f} = {pct(reinv10/nopat10)} of NOPAT; "
      f"implied incremental ROIC = g 4% / {pct(reinv10/nopat10)} = {pct(0.04/(reinv10/nopat10))}; "
      f"terminal uses g 3% / ROIC 25% = {pct(0.03/0.25)} reinvestment -> terminal FCF margin "
      f"{pct(nopat10*1.03*(1-0.12)/(r10[1]*1.03))} vs Y10 {pct(r10[6]/r10[1])}")
print("\nSummary (US$/ADS): " + " | ".join(f"{k} {to_ads(v.per_share):,.2f}" for k, v in RES.items()))
roll = (1 + WACC) ** (105 / 365)
midyr = (1 + WACC) ** 0.5
print(f"Conventions NOT applied (all would raise value): roll-forward 30 Jun->13 Oct x{roll:.3f}; "
      f"mid-year discounting ~x{midyr:.3f} on explicit+TV; govt capex grants (FY25 NT$76,259M) excluded; "
      f"non-current financial assets (FY25 134,337) excluded")

# ------------------------------------------------------------------ F. reverse DCF + sensitivity
hr("F. Reverse DCF and sensitivity (BASE)")
b = SCEN["BASE"]
kw_b = kwargs(b)
kw_rev = {k: v for k, v in kw_b.items() if k not in ("growth", "da_pct")}
PRICE_SH = PRICE_SH_TWD


def rev_solve(wacc=WACC, ebitda_scale=1.0):
    lo, hi = -0.2, 0.6
    for _ in range(80):
        mid = (lo + hi) / 2
        kk = kwargs(b, wacc=wacc, ebitda_scale=ebitda_scale, growth=[mid] * N)
        if dcf(base_revenue=BASE_REV, **kk).per_share < PRICE_SH: lo = mid
        else: hi = mid
    return mid


# library reverse_dcf needs a fixed da_pct; use the BASE D&A path (cross-check vs custom solver)
g_lib = reverse_dcf(price=PRICE_SH, base_revenue=BASE_REV, years=N,
                    **{k: v for k, v in kw_b.items() if k != "growth"})
g_imp = rev_solve()
print(f"reverse_dcf() (BASE margins/capex%, BASE D&A% path fixed): implied 10-yr revenue CAGR {pct(g_lib)}")
print(f"Same with D&A re-derived from capex at each trial growth:            {pct(g_imp)}")
print(f"  -> Year-10 revenue NT${BASE_REV*(1+g_imp)**N:,.0f}M = {(1+g_imp)**N:.1f}x TTM "
      f"(~US${BASE_REV*(1+g_imp)**N/FX/1000:,.0f}B at {FX})")
print(f"  Compare: hist FY21-25 CAGR {pct(rev_cagr)}; BASE path CAGR "
      f"{pct((RES['BASE'].rows[-1][1]/BASE_REV)**(1/N)-1)}")
for w in (WACC - 0.01, WACC + 0.01):
    print(f"  implied CAGR at WACC {w:.2%}: {pct(rev_solve(wacc=w))}")
print(f"  implied CAGR at BEAR-like EBITDA (x0.93): {pct(rev_solve(ebitda_scale=0.93))}")

# implied IRR at BASE operating path
lo, hi = 0.03, 0.25
for _ in range(80):
    mid = (lo + hi) / 2
    if dcf(base_revenue=BASE_REV, **kwargs(b, wacc=mid)).per_share > PRICE_SH: lo = mid
    else: hi = mid
print(f"Implied IRR (discount rate that equates BASE cash flows to price): {mid:.2%} vs WACC {WACC:.2%}")

for w in (0.08, 0.09):
    print(f"BASE at WACC {w:.0%}: US${to_ads(dcf(base_revenue=BASE_REV, **kwargs(b, wacc=w)).per_share):.2f}/ADS | "
          f"BULL at WACC {w:.0%}: US${to_ads(dcf(base_revenue=BASE_REV, **kwargs(SCEN['BULL'], wacc=w)).per_share):.2f}/ADS")
print(f"BASE with roll-forward x{roll:.3f} and mid-year x{midyr:.3f} applied: "
      f"US${to_ads(RES['BASE'].per_share)*roll*midyr:.2f}/ADS (upper bound; ignores dividends paid since 30 Jun)")
print("\nBASE sensitivity: US$/ADS, WACC (rows) x terminal growth (cols), ROIC_t 25%")
gs = [0.02, 0.03, 0.04]
ws = [WACC - 0.01, WACC, WACC + 0.01, WACC + 0.02]
print(f"{'':>8}" + "".join(f"{g:>9.1%}" for g in gs))
for w in ws:
    row = [to_ads(dcf(base_revenue=BASE_REV, **{**kw_b, 'wacc': w, 'terminal_growth': g}).per_share) for g in gs]
    tag = "  (+2pp ~ Taiwan risk premium)" if abs(w - WACC - 0.02) < 1e-9 else ""
    print(f"{w:>8.2%}" + "".join(f"{v:>9.2f}" for v in row) + tag)
grid = sensitivity({"wacc": [WACC - 0.01, WACC, WACC + 0.01]}, {"terminal_growth": gs},
                   base_revenue=BASE_REV, **{k: v for k, v in kw_b.items() if k not in ("wacc", "terminal_growth")})
print(f"(sensitivity() cross-check, centre cell US${to_ads(grid[1][1]):.2f})")

print("\nBASE sensitivity: US$/ADS, WACC x terminal ROIC (g 3%)")
rs = [0.15, 0.20, 0.25, 0.35, 0.45]
print(f"{'':>8}" + "".join(f"{r:>9.0%}" for r in rs))
for w in ws[:3]:
    print(f"{w:>8.2%}" + "".join(f"{to_ads(dcf(base_revenue=BASE_REV, **{**kw_b, 'wacc': w, 'terminal_roic': r}).per_share):>9.2f}" for r in rs))

# ------------------------------------------------------------------ C. multiples matrix
hr("C. Multiples (current)")
FCF_TTM = T["fcf"]
print(f"EV/EBITDA TTM = {EV:,.0f} / {EBITDA_TTM:,.0f} = {EV/EBITDA_TTM:.1f}x  (EV incl NCI)")
print(f"P/E trailing {pe_ttm:.1f}x | normalised {pe_norm:.1f}x | mid-cycle {pe_mid:.1f}x | fwd (vendor) {PE_FWD_VENDOR:.1f}x")
print(f"P/FCF = {MCAP:,.0f} / {FCF_TTM:,.0f} = {MCAP/FCF_TTM:.1f}x | SBC-adj {MCAP/(FCF_TTM-T['sbc']):.1f}x")
print(f"FCF yield {fcf_yield(FCF_TTM, MCAP):.2%} | SBC-adj {fcf_yield(FCF_TTM-T['sbc'], MCAP):.2%} | "
      f"OE yield TTM norm {OE_TTM_NORM/MCAP:.2%} | FY25 {OE_FUND/MCAP:.2%}")
print(f"PEG {peg:.2f} (gate ok, historical NI CAGR only) | Lynch ratio {lynch:.2f} | ROIC TTM {pct(ROIC_TTM)} vs WACC {WACC:.2%}")
peers_t = sorted([56.8, 42.9, 37.8, 21.2, 13.3]); peers_f = sorted([29.9, 26.9, 18.4, 19.4, 4.8])
print(f"Peer median P/E (dossier §7, yfinance, unvalidated): trailing {peers_t[2]}x, forward {peers_f[2]}x")

# ------------------------------------------------------------------ G. load-bearing inputs
hr("G. Load-bearing inputs: BASE US$/ADS at -10% / +10% of each input")
base_v = to_ads(RES["BASE"].per_share)


def val(**over):
    kw = kwargs(b, **{k: v for k, v in over.items() if k in ("wacc", "k", "tax", "wc", "net_debt",
                                                              "ebitda_scale", "capex_scale", "growth")})
    for k in ("terminal_growth", "terminal_roic"):
        if k in over: kw[k] = over[k]
    return to_ads(dcf(base_revenue=BASE_REV, **kw).per_share, over.get("fx", FX))


tests = [
    ("EBITDA margin path (x0.9/x1.1)", dict(ebitda_scale=0.9), dict(ebitda_scale=1.1)),
    ("Capex % of revenue path", dict(capex_scale=0.9), dict(capex_scale=1.1)),
    ("Revenue growth rates (all yrs)", dict(growth=[g * 0.9 for g in b["growth"]]), dict(growth=[g * 1.1 for g in b["growth"]])),
    ("WACC 10.19%", dict(wacc=WACC * 0.9), dict(wacc=WACC * 1.1)),
    ("Terminal growth 3%", dict(terminal_growth=0.027), dict(terminal_growth=0.033)),
    ("Terminal ROIC 25%", dict(terminal_roic=0.225), dict(terminal_roic=0.275)),
    ("USDTWD 32.133", dict(fx=FX * 0.9), dict(fx=FX * 1.1)),
    ("D&A calibration k 0.675", dict(k=K_CAL * 0.9), dict(k=K_CAL * 1.1)),
    ("Tax rate 18%", dict(tax=TAX * 0.9), dict(tax=TAX * 1.1)),
    ("Net cash (NT$2.41T incl NCI)", dict(net_debt=NET_DEBT_FOR_DCF * 0.9), dict(net_debt=NET_DEBT_FOR_DCF * 1.1)),
    ("Working capital 10% of d-rev", dict(wc=0.09), dict(wc=0.11)),
]
out = []
for name, lo_kw, hi_kw in tests:
    vl, vh = val(**lo_kw), val(**hi_kw)
    out.append((max(abs(vl - base_v), abs(vh - base_v)), name, vl, vh))
print(f"BASE = US${base_v:.2f}/ADS")
for sw, name, vl, vh in sorted(out, reverse=True):
    print(f"  {name:<34} -10%: {vl:>8.2f} ({vl/base_v-1:+6.1%})   +10%: {vh:>8.2f} ({vh/base_v-1:+6.1%})")

hr("Data-layer warnings (fundamentals.json)")
for w in FUND["warnings"]:
    print(" -", w)
print(f" errors: {FUND['errors']}")

hr("Derived figures cited in 02_quant.md")
fwd_eps_twd = PRICE_ADS / PE_FWD_VENDOR * FX / ADS_RATIO
print(f"Vendor fwd P/E implies EPS US${PRICE_ADS/PE_FWD_VENDOR:.2f}/ADS = NT${fwd_eps_twd:.1f}/share = "
      f"{fwd_eps_twd/EPS_NORM-1:+.0%} vs normalised TTM {EPS_NORM:.2f}")
print(f"Net cash per ADS = NT${nc_sh:.1f} x 5 / {FX} = US${to_ads(nc_sh):.2f}")
cx13 = sum(r[5] for r in RES["BASE"].rows[:3])
cx_hist = sum(A["capex_ppe"][y] for y in ["2023", "2024", "2025"])
print(f"BASE capex Y1-3 = {cx13:,.0f} vs FY23-25 actual {cx_hist:,.0f} ({cx13/cx_hist:.1f}x)")
print(f"Inventory FY25 / revenue FY25 = 288,109.5 / {A['revenue']['2025']:,.0f} = {288109.5/A['revenue']['2025']:.1%}; "
      f"AR 29 days / 365 = {29/365:.1%}")
roic24 = A["operating_income"]["2024"] * 0.83 / (A["equity_parent"]["2024"] + A["total_debt_incl_noncurrent_leases"]["2024"] - A["cash_and_equivalents"]["2024"])
roic25 = A["operating_income"]["2025"] * 0.83 / (A["equity_parent"]["2025"] + A["total_debt_incl_noncurrent_leases"]["2025"] - A["cash_and_equivalents"]["2025"])
print(f"FY24-25 average ROIC = {pct((roic24+roic25)/2)}")
print(f"TTM revenue in US$ = {T['revenue']:,.0f} / {FX} = US${T['revenue']/FX/1000:,.1f}B")
for m in (EBITDA_TTM / T["revenue"], eb1h26):
    v = to_ads(dcf(base_revenue=BASE_REV, **kwargs(b, ebitda_scale=m / 0.68)).per_share)
    print(f"BASE with steady-state EBITDA {pct(m)} (path scaled x{m/0.68:.3f}): US${v:.2f}/ADS ({v-base_v:+.2f})")
print(f"WACC +/-1pp effect on BASE (g 3%): +{to_ads(dcf(base_revenue=BASE_REV, **kwargs(b, wacc=WACC-0.01)).per_share)-base_v:.2f} / "
      f"{to_ads(dcf(base_revenue=BASE_REV, **kwargs(b, wacc=WACC+0.01)).per_share)-base_v:.2f}")
