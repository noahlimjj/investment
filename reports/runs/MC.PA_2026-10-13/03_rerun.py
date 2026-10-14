"""MC.PA (LVMH) - Skeptic re-run, as of 2026-10-13. EUR millions unless stated.

Loads the Quant's 02_model.py UNCHANGED (runpy; its stdout is suppressed) so every variant below
uses the identical build()/dcf() machinery. Nothing in 02_model.py is overwritten.

No load-bearing input failed the number audit by >5% of fair value, so the Quant's scenario
values are NOT replaced. This script quantifies: (1) verification deltas, (2) the SBC-as-cash
variant, (3) risk-free-rate sensitivity with primary ECB data, (4) the mid-cycle-margin
disagreement with a primary pre-COVID anchor, (5) inventory / receivables (Lynch checks) from
primary LVMH statements, (6) capital-allocation tests, (7) probabilities, EV, MoS, asymmetry.

Primary sources added by the Skeptic (all read 2026-10-13):
  [K1] LVMH H1 2026 press release with condensed statements (S3): balance sheet, cash-flow
       statement (lease interest paid sits INSIDE net cash from operating activities).
  [K2] LVMH Financial Documents 31 Dec 2025 (S1): Note 11 inventories, Note 12 receivables,
       Note 15.2 change in WC, segment inventories, ETR note (French additional tax 2025).
  [K3] LVMH Financial Documents 31 Dec 2023 (S2): inventories FY2021-23 by segment.
  [K4] lvmh.com "Record results for LVMH in 2019" (28 Jan 2020): FY2018/FY2019 revenue and PRO.
  [K5] ECB Data Portal: IRS/M.FR.L.L40.CI.0000.EUR.N.Z (France long-term rate, monthly avg),
       IRS/M.DE..., YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y (euro AAA 10y spot, daily).
  [K6] AMF BDIF 2026DD1092911 (Financiere Agache, 30 Jan 2026) and 2026DD1116814 (23 Apr 2026).
  [K7] yfinance MC.PA daily closes (raw, auto_adjust=False), pulled 2026-10-13.
  [K8] Mauboussin, Callahan, Majd, "The Base Rate Book", Credit Suisse, Sep 2016, sales-growth
       table for sales > $50bn (inflation-adjusted).
Run: python3 reports/runs/MC.PA_2026-10-13/03_rerun.py
"""
import contextlib
import io
import pathlib
import runpy

RUN = pathlib.Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    Q = runpy.run_path(str(RUN / "02_model.py"))

dcf, build, SCEN, RES = Q["dcf"], Q["build"], Q["SCEN"], Q["RES"]
PRICE, SHARES, CLAIMS, WACC = Q["PRICE"], Q["SHARES"], Q["CLAIMS"], Q["WACC"]
A, F, TTM = Q["A"], Q["F"], Q["TTM"]
N, TTM_PRO_M, PRO_AVG = Q["N"], Q["TTM_PRO_M"], Q["PRO_AVG"]
QV = {k: RES[k][0].per_share for k in ("BEAR", "TROUGH", "BASE", "BULL")}


def hdr(t):
    print("\n" + "=" * 92 + f"\n{t}\n" + "=" * 92)


def ps(scen, **over):
    return dcf(**build(**{**SCEN[scen], **over})).per_share


def margin_path(m):
    return [TTM_PRO_M + (m - TTM_PRO_M) * min(i, 4) / 4 for i in range(N)]


hdr("0. QUANT VALUES REPRODUCED (02_model.py unchanged)")
print("  ".join(f"{k} {v:,.1f}" for k, v in QV.items()))

# ------------------------------------------------------------------ 1. verification deltas
hdr("1. NUMBER AUDIT: VERIFICATION DELTAS ON BASE (EUR/share)")
base = QV["BASE"]
PX_YF = 380.45                                    # [K7] close 2026-10-13
SH_OUT = 492.965227                               # Yahoo sharesOutstanding (nets treasury); [K1] treasury
                                                  # shares carried at EUR 1,417m at 30 Jun 2026
NONOP = 1225 + 1967 + (2074 - 1025)               # [K1] JV/associates + non-current AFS + DFS HFS net
r = RES["BASE"][0]
print(f"Price: facts 381.65 vs yfinance close {PX_YF} -> {PX_YF/PRICE-1:+.2%} (no change to FV)")
print(f"Shares: issued {SHARES:.3f}m vs outstanding {SH_OUT:.3f}m -> BASE "
      f"{(r.enterprise_value-CLAIMS)/SH_OUT:,.1f} ({(SHARES/SH_OUT-1):+.2%})")
print(f"Non-operating assets not credited ({NONOP:,}): BASE "
      f"{(r.enterprise_value-CLAIMS+NONOP)/SHARES:,.1f} ({NONOP/SHARES:+.1f}/share, "
      f"{NONOP/SHARES/base:+.1%})")
mid = (1 + WACC) ** 0.5
print(f"Mid-year discounting instead of end-year: BASE {(r.enterprise_value*mid-CLAIMS)/SHARES:,.1f} "
      f"({(r.enterprise_value*mid-CLAIMS)/SHARES/base-1:+.1%}) - library convention, NOT applied")
# Lease interest: K1 cash-flow statement shows 'Lease liabilities: interest paid (252)/(545)'
# INSIDE net cash from operating activities -> Quant's gap calibration is correct as built.
print("Lease interest paid is inside OCF ([K1]: H1-26 (252), FY25 (545)) -> Quant calibration "
      "holds; the -7 to -8/share contingency in Quant H.3 does not apply")

# ------------------------------------------------------------------ 2. SBC
hdr("2. SBC: SHARE OF OCF / REVENUE; SBC TREATED AS CASH")
sbc25, sbc_ttm = A["sbc_bonus_share_expense"]["FY2025"], 187
print(f"SBC FY25 {sbc25} = {sbc25/A['net_cash_from_operating_activities']['FY2025']:.2%} of OCF, "
      f"{sbc25/A['revenue']['FY2025']:.2%} of revenue; TTM {sbc_ttm} = "
      f"{sbc_ttm/TTM['nocf']:.2%} of OCF, {sbc_ttm/TTM['revenue']:.2%} of revenue")
# The model expenses SBC inside PRO, but the cash-gap calibration compares against reported FCF,
# whose OCF adds back non-cash bonus-share expense ('other adjustments and computed expenses').
# The calibration therefore re-credits ~SBC. SBC-as-cash: add SBC/revenue to the gap.
sbc_pct = sbc_ttm / TTM["revenue"]
SBCV = {}
for k in QV:
    gap_k = SCEN[k].get("gap", Q["GAP_AVG"])
    SBCV[k] = ps(k, gap=gap_k + sbc_pct)
print("SBC-as-cash values: " + "  ".join(f"{k} {v:,.1f} ({v/QV[k]-1:+.1%})" for k, v in SBCV.items()))
print(f"TTM company FCF {TTM['operating_fcf']:,} -> SBC-adj {TTM['operating_fcf']-sbc_ttm:,} "
      f"(yield {(TTM['operating_fcf']-sbc_ttm)/(PRICE*SHARES):.2%})")

# ------------------------------------------------------------------ 3. accruals / WC / inventory
hdr("3. ACCRUALS, WORKING CAPITAL, INVENTORY & RECEIVABLES (Lynch checks)")
Y = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
ni = [A["net_profit_before_minorities"][y] for y in Y]
ocf = [A["net_cash_from_operating_activities"][y] for y in Y]
lp = [-A["repayment_of_lease_liabilities"][y] for y in Y]
rev = [A["revenue"][y] for y in Y]
print(f"5-yr NI (pre-MI) {sum(ni):,} | OCF {sum(ocf):,} (x{sum(ocf)/sum(ni):.2f}) | OCF - lease principal "
      f"{sum(ocf)-sum(lp):,} (x{(sum(ocf)-sum(lp))/sum(ni):.2f})")
wc = {"FY2023": -4577, "FY2024": -1925, "FY2025": -576, "H1-25": -1990, "H1-26": -2446}   # [K2][K1]
print("Change in WC (cash): " + ", ".join(f"{k} {v:,}" for k, v in wc.items()) +
      "  -> WC consumed cash every period; OCF is not flattered")
inv = {"FY2021": 16549, "FY2022": 20319, "FY2023": 22952, "FY2024": 23669, "FY2025": 22659}  # [K3][K2]
inv_h1 = {"H1-25": 23090, "H1-26": 24184}                                                  # [K1]
recv = {"FY2023": 4728, "FY2024": 4730, "FY2025": 4332, "H1-25": 4257, "H1-26": 3941}     # [K2][K1]
gross_add = {"FY2023": 4230, "FY2024": 1114, "FY2025": 1315}                               # [K2] Note 11
inv_prov = {"FY2023": 986, "FY2024": 834, "FY2025": 803}                                   # [K2] impairment charge
print(f"{'':10}{'Inventory':>10}{'Inv g':>8}{'Rev g':>8}{'Inv/Rev':>9}")
for i, y in enumerate(Y):
    ig = "" if i == 0 else f"{inv[y]/inv[Y[i-1]]-1:+.1%}"
    rg = "" if i == 0 else f"{rev[i]/rev[i-1]-1:+.1%}"
    print(f"{y:10}{inv[y]:>10,}{ig:>8}{rg:>8}{inv[y]/rev[i]:>9.1%}")
h1g = inv_h1["H1-26"] / inv_h1["H1-25"] - 1
print(f"{'Jun-26':10}{inv_h1['H1-26']:>10,}{h1g:>+8.1%}{38644/39810-1:>+8.1%}"
      f"{inv_h1['H1-26']/TTM['revenue']:>9.1%}  (YoY vs Jun-25; H1 revenue; Inv/TTM rev)")
print("Gross inventory additions (pre-FX): " + ", ".join(f"{k} +{v:,}" for k, v in gross_add.items()) +
      " | impairment charges: " + ", ".join(f"{k} {v:,}" for k, v in inv_prov.items()))
seg_inv = {"WS": (6278, 8451), "FLG": (3374, 5120), "WJ": (3949, 5432), "SR": (2410, 2749)}   # FY21, FY25
for s_, (a0, a1) in seg_inv.items():
    r0, r1 = A["revenue_by_group"]["FY2021"][s_], A["revenue_by_group"]["FY2025"][s_]
    print(f"  {s_:<4} inventory/revenue FY21 {a0/r0:.0%} -> FY25 {a1/r1:.0%} "
          f"(inventory {a1/a0-1:+.0%}, revenue {r1/r0-1:+.0%})")
print("Receivables: " + ", ".join(f"{k} {v:,}" for k, v in recv.items()) +
      f" -> Jun-26 YoY {recv['H1-26']/recv['H1-25']-1:+.1%} vs revenue -2.9%: no flag")
oth = {"FY2021": 4, "FY2022": -54, "FY2023": -242, "FY2024": -664, "FY2025": -656}
pro = [A["profit_from_recurring_operations"][y] for y in Y]
print("'Other operating income/expenses' excluded from PRO: " +
      ", ".join(f"{y} {oth[y]:,} ({oth[y]/pro[i]:+.1%} of PRO)" for i, y in enumerate(Y)) +
      f" | 5-yr sum {sum(oth.values()):,} = {sum(oth.values())/sum(pro):+.1%} of PRO")

# ------------------------------------------------------------------ 4. risk-free rate
hdr("4. RISK-FREE RATE: PRIMARY ECB DATA AND EFFECT ON BASE")
print("ECB France long-term (convergence) rate monthly avg: Aug-26 4.00%, Sep-26 4.44% [K5]")
print("ECB Germany: Aug-26 3.19%, Sep-26 3.47% -> FR-DE spread Sep-26 0.97pt [K5]")
print("ECB euro AAA 10y spot: 14-Sep 3.54%, 28-Sep 3.63%, 07-Oct 3.54%, 12-Oct 3.50% [K5]")
print("Secondary: AFT TEC10 4.48% on 14-Sep (abcbourse); OAT 4.75% on 07-Oct (TradingEconomics)")
print("FRED IRLTLT01FRM156N 4.00% = Aug monthly average -> TEMPORALLY STALE, rejected")
ERP = 0.05
E_W = PRICE * SHARES + Q["PUTS"] + Q["MI_BOOK"]
D_W = Q["NFD"]


def wacc_for(rf, beta=1.0, floor_rf=None):
    ke = rf + beta * ERP
    kd = rf * (1 - Q["ETR_AVG"])
    w = (E_W * ke + D_W * kd) / (E_W + D_W)
    fl = (floor_rf if floor_rf is not None else rf) + 0.04
    return round(max(w, fl), 4)


for lab, rf, beta, frf in (("OAT 4.44% (ECB Sep avg)", 0.0444, 1.0, None),
                           ("OAT 4.75% (Quant, Oct-7)", 0.0475, 1.0, None),
                           ("OAT 5.00% (late-Sep peak)", 0.0500, 1.0, None),
                           ("OAT 4.75%, Yahoo beta 0.88", 0.0475, 0.879, None),
                           ("AAA 3.50% Rf, floor on OAT 4.75%", 0.0350, 1.0, 0.0475)):
    w = wacc_for(rf, beta, frf)
    vals = {k: ps(k, wacc=w) for k in QV}
    print(f"{lab:<34} WACC {w:.2%} -> " + "  ".join(f"{k} {v:,.0f}" for k, v in vals.items()))

# ------------------------------------------------------------------ 5. mid-cycle margin anchor
hdr("5. MID-CYCLE PRO MARGIN: OUTSIDE VIEW FROM PRIMARY PRE-COVID DATA [K4]")
fy18 = dict(rev=46826, pro=10003)
fy19 = dict(rev=53670, pro=11504, seg_rev=dict(WS=5576, FLG=22237, PC=6835, WJ=4405, SR=14791),
            seg_pro=dict(WS=1729, FLG=7344, PC=683, WJ=736, SR=1395))
print(f"FY2018 PRO margin {fy18['pro']/fy18['rev']:.1%} (pre-IFRS 16) | FY2019 {fy19['pro']/fy19['rev']:.1%} "
      f"(IFRS 16, comparable) | FLG FY2019 {fy19['seg_pro']['FLG']/fy19['seg_rev']['FLG']:.1%}")
r25 = A["revenue_by_group"]["FY2025"]
mixadj = sum(fy19["seg_pro"][k] / fy19["seg_rev"][k] * r25[k] for k in fy19["seg_rev"]) \
    + A["pro_by_group"]["FY2025"]["Other_elim"]
print(f"FY2019 segment margins on FY2025 mix (+FY25 other/elims): {mixadj:,.0f} / {A['revenue']['FY2025']:,}"
      f" = {mixadj/A['revenue']['FY2025']:.1%}")
pm = [p / r for p, r in zip(pro, rev)]
seven = (sum(pm) + fy18["pro"] / fy18["rev"] + fy19["pro"] / fy19["rev"]) / 7
print(f"7 verified years (FY18, FY19, FY21-25; FY20 COVID year UNKNOWN, so biased up): avg {seven:.1%}")
print(f"5-yr avg used by Quant {PRO_AVG:.1%}: three of five years are the FY21-23 boom (26.5-26.7%)")
for m in (mixadj / A["revenue"]["FY2025"], 0.230, 0.235, seven, PRO_AVG):
    print(f"  steady-state PRO {m:.1%}: BASE {dcf(**build(SCEN['BASE']['g'], margin_path(m))).per_share:,.1f}")
SKEP_BASE = dcf(**build(SCEN["BASE"]["g"], margin_path(0.235))).per_share

# ------------------------------------------------------------------ 6. outside view on growth
hdr("6. OUTSIDE VIEW ON GROWTH [K8] (sales > $50bn, 10-yr real CAGR, 1950-2015)")
dist = {"<(5)": 0.0 + 0.3 + 1.0 + 3.1 + 9.8, "(5)-0": 26.9, "0-5": 37.8, "5-10": 17.2, ">10": 3.0 + 0.9}
print("Distribution (%): " + ", ".join(f"{k} {v:.1f}" for k, v in dist.items()) + " | mean 0.8%, median 1.1%")
for lab, nom in (("reverse DCF, margins to 25%", 0.0481), ("reverse DCF, margins at trough", 0.0650),
                 ("Quant BASE path (10-yr CAGR)", None)):
    if nom is None:
        g = SCEN["BASE"]["g"]
        c = 1.0
        for x in g:
            c *= 1 + x
        nom = c ** (1 / len(g)) - 1
    real = nom - 0.02                             # ASSUMPTION: 2% EUR inflation (ECB target)
    # share above `real`: linear within the 0-5 bucket, all of >5
    p = (dist["5-10"] + dist[">10"] + dist["0-5"] * max(0.0, 5 - real * 100) / 5) / 100
    print(f"  {lab:<32} nominal {nom:.2%} ~ real {real:.2%} -> base rate of achieving it ~{p:.0%}")

# ------------------------------------------------------------------ 7. capital allocation
hdr("7. CAPITAL ALLOCATION: $1 TEST, INCREMENTAL ROIC, BUYBACK PRICES, M&A")
px = {"2020-12-31": 510.9, "2021-10-13": 653.9, "2025-12-31": 645.0, "2026-10-13": PX_YF}   # [K7] raw closes
dil21 = A["diluted_shares_weighted_avg"]["FY2021"] / 1e6       # proxy for Dec-2020 / Oct-2021 count
mv = {"2020-12-31": px["2020-12-31"] * dil21, "2021-10-13": px["2021-10-13"] * dil21,
      "2025-12-31": px["2025-12-31"] * A["shares_issued_year_end"]["FY2025"] / 1e6,
      "2026-10-13": PX_YF * SHARES}
div = [-A["dividends_paid_incl_minorities"][y] for y in Y]
ret5 = sum(ni) - sum(div)
ret_h1 = 6019 - 3991
print(f"Retained FY21-25 = NI pre-MI {sum(ni):,} - dividends incl. MI {sum(div):,} = {ret5:,}; "
      f"+H1-26 {ret_h1:,} = {ret5+ret_h1:,}")
for a, b, ret in (("2020-12-31", "2025-12-31", ret5), ("2021-10-13", "2026-10-13", ret5 + ret_h1),
                  ("2020-12-31", "2026-10-13", ret5 + ret_h1)):
    d = mv[b] - mv[a]
    print(f"  {a} MV {mv[a]:,.0f} -> {b} MV {mv[b]:,.0f}: dMV {d:+,.0f} per EUR retained {d/ret:+.2f}")
nopat = [p * (1 - t) for p, t in zip(pro, Q["etr"])]
ic = [e + n for e, n in zip([A["equity_total"][y] for y in Y],
                            [A["net_financial_debt_excl_leases_excl_minority_puts"][y] for y in Y])]
print(f"Incremental ROIC FY21->FY25: dNOPAT {nopat[-1]-nopat[0]:+,.0f} / dIC {ic[-1]-ic[0]:+,} = "
      f"{(nopat[-1]-nopat[0])/(ic[-1]-ic[0]):+.1%}; FY19-pre-boom comparison UNKNOWN (no FY19 IC)")
wj_assets = 32954 - 3064                         # [K2] W&J segment total assets ex-ROU, FY2025
wj_nopat = A["pro_by_group"]["FY2025"]["WJ"] * (1 - Q["ETR_AVG"])
print(f"W&J (Tiffany era) FY25 NOPAT {wj_nopat:,.0f} / segment assets ex-ROU {wj_assets:,} = "
      f"{wj_nopat/wj_assets:.1%} (gross of payables; vs WACC {WACC:.1%})")
flg_assets = 39354 - 8790
print(f"FLG FY25 NOPAT {13209*(1-Q['ETR_AVG']):,.0f} / segment assets ex-ROU {flg_assets:,} = "
      f"{13209*(1-Q['ETR_AVG'])/flg_assets:.1%}")
print(f"Goodwill + brands at Jun-26: {18561+23331:,} = {(18561+23331)/141769:.1%} of total assets [K1]")
bb = {"2023 programme": 837, "2025 total purchases": 528, "H1-26 (avg close H1-26, proxy)": 509.7}
print("Buyback average prices: " + ", ".join(f"{k} ~{v}" for k, v in bb.items()))
sh = A["diluted_shares_weighted_avg"]
print(f"Diluted shares {sh['FY2021']/1e6:.1f}m (FY21) -> {sh['FY2025']/1e6:.1f}m (FY25) -> 494.96m (H1-26): "
      f"{(494.957592/(sh['FY2021']/1e6))**(1/4.5)-1:+.2%}/yr; cumulative buyback cash FY21-H1-26 "
      f"{552+1604+1569+224+1634+1658:,}")

# ------------------------------------------------------------------ 8. probabilities, EV
hdr("8. PROBABILITIES, EXPECTED VALUE, MARGIN OF SAFETY, ASYMMETRY")
P = {"BEAR": 0.20, "TROUGH": 0.30, "BASE": 0.35, "BULL": 0.15}
assert abs(sum(P.values()) - 1) < 1e-9
ev = sum(P[k] * QV[k] for k in P)
ev_sbc = sum(P[k] * SBCV[k] for k in P)
w_margin = 0.20 * 0.22 + 0.30 * TTM_PRO_M + 0.35 * PRO_AVG + 0.15 * 0.265
print("Scenario      value   prob   p x v")
for k in P:
    print(f"{k:<12}{QV[k]:>7.1f}{P[k]:>7.0%}{P[k]*QV[k]:>8.1f}")
print(f"EV {ev:,.1f} | SBC-as-cash EV {ev_sbc:,.1f} | probability-weighted steady-state margin {w_margin:.1%}")
mos = 1 - PRICE / ev
asym = (ev - PRICE) / (PRICE - QV["BEAR"])
print(f"MoS = 1 - {PRICE}/{ev:.1f} = {mos:+.1%} | asymmetry (EV-price)/(price-bear) = {asym:+.2f}")
alt = {**QV, "BASE": SKEP_BASE}
ev_alt = sum(P[k] * alt[k] for k in P)
print(f"Cross-check: same weights with Skeptic BASE (23.5% margin) {SKEP_BASE:,.1f} -> EV {ev_alt:,.1f} "
      f"(double-counts margin skepticism; not used)")
for lab, pp in (("Quant-friendly 10/25/45/20", (0.10, 0.25, 0.45, 0.20)),
                ("Harsh 30/30/30/10", (0.30, 0.30, 0.30, 0.10))):
    e = sum(p_ * QV[k] for p_, k in zip(pp, P))
    print(f"Weight sensitivity {lab}: EV {e:,.1f}, EV x 1.3 = {e*1.3:,.1f}, EV x 0.6 = {e*0.6:,.1f}")
MOS_REQ = 0.40                                   # Cyclical (Quant category) per analyse skill
print(f"ENTRY_BELOW = EV x (1-{MOS_REQ:.0%}) = {ev*(1-MOS_REQ):,.0f} | EXIT_ABOVE = EV x 1.3 = {ev*1.3:,.0f}")
print(f"Price/EV {PRICE/ev:.3f}: EV < price <= EV x 1.3 -> held: HOLD (unless bear thesis already showing)")
