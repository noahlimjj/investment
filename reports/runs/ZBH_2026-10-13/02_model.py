"""ZBH (Zimmer Biomet) Quant model, as of 2026-10-13. USD millions unless stated.

Sources (cited inline):
  facts   = reports/runs/ZBH_2026-10-13/facts.json (SEC XBRL via sec_facts.py)
  secfix  = `python3 methodologies/sec_facts.py ZBH` re-run 2026-10-13 (corrected derived series:
            capex now INCLUDES PaymentsToAcquireIntangibleAssets; orchestrator correction)
  fund    = data/fundamentals.json (yfinance-backed, validated layer)
  dossier = reports/runs/ZBH_2026-10-13/01_research.md, section number in brackets

SBC treatment: EBITDA is GAAP operating income + D&A. GAAP operating income already expenses
SBC, so SBC is DEDUCTED (never added back). Share count is held flat at the latest outstanding
count, not grown. One method, not both, not neither.
"""
import sys, pathlib, statistics as st
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "methodologies"))
from valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield

YRS = ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25"]
# ---- facts.json annual (USD M) ----
REV   = [6127.5, 6827.3, 6939.9, 7394.2, 7678.6, 8231.5]
OPINC = [83.1, 860.3, 696.3, 1277.7, 1285.7, 1098.1]
NI    = [-138.9, 401.6, 231.4, 1024.0, 903.8, 705.1]
DA    = [898.4, 937.7, 926.4, 951.7, 996.3, 1093.8]
SBC   = [73.8, 76.0, 105.0, 99.8, 101.0, 90.2]
OCF   = [1204.5, 1499.2, 1356.2, 1581.6, 1499.4, 1697.1]
CAPEX_PPE = [111.9, 143.6, 187.9, 291.1, 203.8, 224.5]
COGS  = [1824.3, 1960.4, 2019.5, 2083.8, 2191.2, 2493.7]
INV   = [2450.7, 2148.0, 2147.2, 2385.2, 2235.3, 2286.4]
AR    = [1452.7, 1259.6, 1381.5, 1442.4, 1480.7, 1704.4]
GW    = [8983.1, 8919.4, 8580.2, 8818.5, 8951.1, 9947.1]
IC    = [19518.6, 19351.4, 17341.1, 17832.6, 18147.2, 19624.9]       # facts derived.invested_capital
ROIC_TAX = [0.21, 0.1072, 0.2783, 0.0395, 0.1268, 0.1513]           # facts derived.roic_tax_rate_used
DIL   = [207.0, 210.4, 210.3, 209.7, 203.9, 198.7]
DIVS  = [198.5, 200.1, 201.2, 200.9, 196.0, 190.3]
# ---- secfix corrected series (capex incl. capitalised intangibles) ----
FCF_FIX = [1093, 1347, 1139, 1187, 1143, 1420]
OE_FIX  = [648, 1187, 940, 1581, 1543, 1522]
INTANG_CAPEX = [OCF[i] - CAPEX_PPE[i] - FCF_FIX[i] for i in range(6)]  # implied, +/-1 rounding
# ---- TTM to 2026-06-30 (facts ttm; capex_intangibles from secfix) ----
T_REV, T_COGS, T_OPINC, T_NI, T_DA, T_SBC = 8508.8, 2563.3, 1205.0, 806.7, 1108.4, 98.2
T_OCF, T_CAPEX_PPE, T_CAPEX_INT, T_PRETAX, T_TAX = 1743.3, 220.3, 121.0, 933.6, 126.6
T_BUYBACK, T_DIV = 750.8, 188.4
# ---- market / balance sheet (facts.market, dossier s1/s3/s5) ----
PRICE, MCAP, SHARES = 92.17, 17580.3, 190.74
DEBT, CASH = 7478.9, 410.0                 # Jun-26: current 1,201.5 + LT 6,277.5
NET_DEBT = DEBT - CASH                     # 7,068.9
EQUITY_JUN26, GW_JUN26, INTANG_JUN26 = 12632.5, 9919.5, 4461.6
EV = MCAP + NET_DEBT
INT_EXP = {"FY23": 201.2, "FY24": 218.0, "FY25": 292.8}   # dossier s2 (10-K text)
DPS = 0.96                                 # dossier s1
UST10 = 0.052                              # dossier s1 (yfinance ^TNX, not cross-checked)
GUIDE_ADJ_EPS_MID = (8.47 + 8.59) / 2      # dossier s3
CONS_EPS_26, CONS_EPS_27 = 8.534, 9.071    # facts consensus_labelled (CONSENSUS)
TRAIL_PE_VENDOR, FWD_PE_VENDOR = 22.371359, 10.179344   # fund
M_AND_A_2025 = 1393.2                      # dossier s5: Paragon 28 + Monogram, net of cash

def pct(x): return f"{x*100:5.1f}%"
def line(t=""): print("\n" + "=" * 8 + " " + t + " " + "=" * 8)

# =====================================================================================
line("A. LYNCH: growth, balance sheet quality")
cagr = lambda a, b, n: (b / a) ** (1 / n) - 1
print(f"Revenue CAGR FY20-25 {pct(cagr(REV[0], REV[5], 5))} | FY21-25 {pct(cagr(REV[1], REV[5], 4))} | "
      f"FY22-24 {pct(cagr(REV[2], REV[4], 2))}")
print("Revenue y/y: " + " ".join(f"{YRS[i]} {pct(REV[i]/REV[i-1]-1)}" for i in range(1, 6)))
eps = [NI[i] / DIL[i] for i in range(6)]
print("GAAP diluted EPS (NI/diluted shares): " + " ".join(f"{YRS[i]} {eps[i]:.2f}" for i in range(6)))
print(f"GAAP EPS CAGR FY20-25: undefined (FY20 negative) | FY21-25 {pct(cagr(eps[1], eps[5], 4))} | "
      f"FY23-25 {pct(cagr(eps[3], eps[5], 2))}")
print(f"Consensus adj EPS FY27/FY26 growth: {pct(CONS_EPS_27/CONS_EPS_26-1)} (CONSENSUS, labelled)")
dps_hist = [DIVS[i] / DIL[i] for i in range(6)]
print("Dividends paid / diluted shares: " + " ".join(f"{YRS[i]} {dps_hist[i]:.3f}" for i in range(6)))
print("Inventory growth vs sales growth / receivables growth vs sales growth (pp):")
for i in range(1, 6):
    sg, ig, ag = REV[i]/REV[i-1]-1, INV[i]/INV[i-1]-1, AR[i]/AR[i-1]-1
    print(f"  {YRS[i]}: sales {pct(sg)} inv {pct(ig)} ({(ig-sg)*100:+5.1f}pp) AR {pct(ag)} ({(ag-sg)*100:+5.1f}pp)"
          + ("  <-- AR FLAG" if ag - sg > 0.03 else ""))
T_OE = T_NI + T_DA - T_CAPEX_PPE - T_CAPEX_INT
T_FCF = T_OCF - T_CAPEX_PPE - T_CAPEX_INT
print(f"Net debt (Jun-26) {NET_DEBT:,.1f} | / OE FY25 {NET_DEBT/OE_FIX[5]:.1f}x | / OE TTM {NET_DEBT/T_OE:.1f}x | "
      f"/ GAAP EBITDA TTM {NET_DEBT/(T_OPINC+T_DA):.2f}x")
print(f"Interest cover: FY25 EBIT/interest {OPINC[5]/INT_EXP['FY25']:.2f}x | TTM EBIT / FY25 interest "
      f"{T_OPINC/INT_EXP['FY25']:.2f}x")
print(f"Cash {CASH} vs current debt 1,201.5 -> gap {CASH-1201.5:,.1f}; TTM FCF {T_FCF:,.1f}; "
      f"TTM buybacks+divs {T_BUYBACK+T_DIV:,.1f}")

# =====================================================================================
line("B. BUFFETT: margins, ROIC, owner earnings")
gm = [1 - COGS[i]/REV[i] for i in range(6)]
om = [OPINC[i]/REV[i] for i in range(6)]
em = [(OPINC[i]+DA[i])/REV[i] for i in range(6)]
capx_tot = [CAPEX_PPE[i] + INTANG_CAPEX[i] for i in range(6)]
print(f"{'':6}{'GM':>7}{'OpM':>7}{'EBITDAm':>9}{'Capex/R':>9}{'Capex/DA':>9}{'FCFm':>7}{'ROIC':>7}{'ROICxGW':>9}{'GW/IC':>7}")
roic, roic_xgw = [], []
for i in range(6):
    nopat = OPINC[i] * (1 - ROIC_TAX[i])
    r, rx = nopat / IC[i], nopat / (IC[i] - GW[i])
    roic.append(r); roic_xgw.append(rx)
    print(f"{YRS[i]:6}{pct(gm[i]):>7}{pct(om[i]):>7}{pct(em[i]):>9}{pct(capx_tot[i]/REV[i]):>9}"
          f"{capx_tot[i]/DA[i]:>9.2f}{pct(FCF_FIX[i]/REV[i]):>7}{pct(r):>7}{pct(rx):>9}{pct(GW[i]/IC[i]):>7}")
T_IC = EQUITY_JUN26 + DEBT - CASH
T_ETR = T_TAX / T_PRETAX
T_NOPAT = T_OPINC * (1 - T_ETR)
print(f"TTM: GM {pct(1-T_COGS/T_REV)} OpM {pct(T_OPINC/T_REV)} EBITDAm {pct((T_OPINC+T_DA)/T_REV)} "
      f"capex(tot)/R {pct((T_CAPEX_PPE+T_CAPEX_INT)/T_REV)} FCFm {pct(T_FCF/T_REV)} ETR {pct(T_ETR)}")
print(f"TTM ROIC {pct(T_NOPAT/T_IC)} | ex-GW {pct(T_NOPAT/(T_IC-GW_JUN26))} | ex-GW ex-intangibles "
      f"{pct(T_NOPAT/(T_IC-GW_JUN26-INTANG_JUN26))} (GAAP EBIT is after acquired-intangible amortisation; "
      f"D&A split UNKNOWN) | GW/IC {pct(GW_JUN26/T_IC)}")
print(f"5-yr (FY21-25) avg: GM {pct(st.mean(gm[1:]))} EBITDAm {pct(st.mean(em[1:]))} (low {pct(min(em[1:]))}, "
      f"high {pct(max(em[1:]))}) FCFm {pct(st.mean(FCF_FIX[i]/REV[i] for i in range(1,6)))} "
      f"ROIC {pct(st.mean(roic[1:]))} ROICxGW {pct(st.mean(roic_xgw[1:]))}")
unlev = {y: (FCF_FIX[i] + INT_EXP[y]*(1-ROIC_TAX[i])) / REV[i] for i, y in enumerate(YRS) if y in INT_EXP}
print("Unlevered FCF margin (FCF + after-tax interest)/rev: " +
      " ".join(f"{y} {pct(v)}" for y, v in unlev.items()) + f" | 3-yr avg {pct(st.mean(unlev.values()))}")
print("Owner earnings (secfix, NI + D&A - capex incl. intangibles) and SBC-adjusted:")
for i in range(6):
    print(f"  {YRS[i]}: OE {OE_FIX[i]:>6,}  OE-SBC {OE_FIX[i]-SBC[i]:>7,.0f}")
print(f"  TTM : OE {T_OE:>6,.0f}  OE-SBC {T_OE-T_SBC:>7,.0f}")
print(f"OE yield on mcap {MCAP:,.0f}: FY25 {pct(OE_FIX[5]/MCAP)} | FY25 SBC-adj {pct((OE_FIX[5]-SBC[5])/MCAP)} | "
      f"TTM {pct(T_OE/MCAP)} | TTM SBC-adj {pct((T_OE-T_SBC)/MCAP)}")
print(f"Stress: FY25 OE less 2025 acquisitions ({M_AND_A_2025}) = {OE_FIX[5]-M_AND_A_2025:,.0f}")

# =====================================================================================
line("C. MULTIPLES MATRIX")
ebitda_ttm = T_OPINC + T_DA
eps_ttm_basic = T_NI / SHARES
pe_ttm = PRICE / eps_ttm_basic
ncps = -NET_DEBT / SHARES
dy = DPS / PRICE
peers = {  # dossier s7: EV/EBITDA, trailing PE, forward PE, FCF yield
    "SYK": (16.3, 29.3, 16.9, .038), "MDT": (13.2, 22.6, 14.3, .046), "BSX": (13.3, 17.7, 13.0, .039),
    "SNN": (44.8, 18.8, 11.5, .091), "EW": (23.2, 51.4, 25.5, .025), "GMED": (9.7, 19.5, 14.1, .054)}
med = lambda k: st.median(v[k] for v in peers.values())
med_xsnn = lambda k: st.median(v[k] for t, v in peers.items() if t != "SNN")
print(f"EV {EV:,.1f} (mcap {MCAP:,.1f} + net debt {NET_DEBT:,.1f}); leases/CVR/pension UNKNOWN")
print(f"EV/EBITDA GAAP TTM {EV/ebitda_ttm:.2f}x | GAAP FY25 {EV/(OPINC[5]+DA[5]):.2f}x | vendor 9.8x | "
      f"peer median {med(0):.1f}x (ex-SNN {med_xsnn(0):.1f}x)")
print(f"P/E trailing: vendor {TRAIL_PE_VENDOR:.1f}x | TTM GAAP NI/outstanding shares EPS {eps_ttm_basic:.2f} -> {pe_ttm:.1f}x | "
      f"peer median {med(1):.2f}x")
print(f"P/E forward: on guide-mid adj EPS {GUIDE_ADJ_EPS_MID:.2f} -> {PRICE/GUIDE_ADJ_EPS_MID:.1f}x | vendor {FWD_PE_VENDOR:.1f}x "
      f"(= price / FY27 cons {PRICE/CONS_EPS_27:.2f}x) | peer median {med(2):.2f}x | forward GAAP P/E UNKNOWN")
print(f"P/FCF (corrected TTM FCF {T_FCF:,.1f}) {MCAP/T_FCF:.1f}x | FY25 {MCAP/FCF_FIX[5]:.1f}x | "
      f"SBC-adj TTM {MCAP/(T_FCF-T_SBC):.1f}x | peer median P/FCF {st.median(1/v[3] for v in peers.values()):.1f}x")
print(f"FCF yield TTM {pct(fcf_yield(T_FCF, MCAP))} | FY25 {pct(fcf_yield(FCF_FIX[5], MCAP))} | vendor-FCF basis "
      f"{pct(fcf_yield(1072.2, MCAP))} | peer median {pct(med(3))}")
print(f"OE yield TTM {pct(T_OE/MCAP)}")
print(f"Dividend yield {pct(dy)} | buyback yield TTM {pct(T_BUYBACK/MCAP)} | FCF payout (divs) {pct(T_DIV/T_FCF)} | "
      f"GAAP NI payout {pct(T_DIV/T_NI)}")
g_hist5 = None                               # FY20 EPS negative -> 5-yr CAGR undefined
g_hist3 = cagr(eps[3], eps[5], 2)
g_cons = CONS_EPS_27 / CONS_EPS_26 - 1
for lab, g in (("hist 5y (undefined)", g_hist5), ("hist FY23-25", g_hist3), ("consensus FY27", g_cons)):
    print(f"peg_is_valid(trailing {TRAIL_PE_VENDOR:.1f}, fwd {FWD_PE_VENDOR:.1f}, {lab}) -> "
          f"{peg_is_valid(TRAIL_PE_VENDOR, FWD_PE_VENDOR, g)}")
print("Lower-of rule -> historical growth is undefined/negative -> PEG VOID, not cited.")
for lab, pe in (("trailing GAAP", TRAIL_PE_VENDOR), ("forward adj (vendor)", FWD_PE_VENDOR)):
    print(f"Lynch ratio ({lab}) = ({g_cons*100:.1f} + {dy*100:.2f}) / {pe:.1f} = {(g_cons*100+dy*100)/pe:.2f}"
          f"  [generous: uses consensus growth]")
print(f"Net cash/share {ncps:.2f} -> net-cash-adj P/E: GAAP TTM ({PRICE:.2f}-({ncps:.2f}))/{eps_ttm_basic:.2f} = "
      f"{(PRICE-ncps)/eps_ttm_basic:.1f}x | on guide-mid adj EPS {(PRICE-ncps)/GUIDE_ADJ_EPS_MID:.1f}x")

# =====================================================================================
line("D. DISCOUNT RATE")
ERP, BETA = 0.05, 1.0
ke = UST10 + BETA * ERP
kd_pre = 0.055          # coupon of 5.500% 2035 notes (dossier s5); market YTM UNKNOWN
TAX = 0.18              # adjusted tax rate Q2 2026 (dossier s3)
kd_hist = INT_EXP["FY25"] / ((DEBT + 0.0) + (5341.6 + 863.0)) * 2
wE, wD = MCAP / (MCAP + DEBT), DEBT / (MCAP + DEBT)
wacc_raw = wE * ke + wD * kd_pre * (1 - TAX)
WACC = max(wacc_raw, 0.08)
print(f"Ke = {UST10:.2%} + {BETA} x {ERP:.0%} = {ke:.2%}")
print(f"Kd pre-tax {kd_pre:.2%} (coupon proxy) | historical FY25 interest / avg(Dec-24, Jun-26 debt) {kd_hist:.2%} "
      f"(below Treasury, so not used) | after-tax {kd_pre*(1-TAX):.2%}")
print(f"Weights (debt at book, market value UNKNOWN): E {wE:.1%} D {wD:.1%} -> WACC {wacc_raw:.2%}; floor 8% -> {WACC:.2%}")
WACC = round(WACC, 3)
print(f"WACC used: {WACC:.1%}")

# =====================================================================================
line("E. DCF SCENARIOS")
N = 10
DA0 = T_DA / T_REV
WC = (INV[5] + AR[5]) / REV[5]       # inventory + receivables / revenue; payables UNKNOWN -> conservative
def fade(start, end, hold=5, n=N):
    out = [start] * hold
    k = n - hold
    out += [start + (end - start) * (j + 1) / k for j in range(k)]
    return out
def ramp(vals): return (vals + [vals[-1]] * N)[:N]

SCEN = {
  "BEAR": dict(growth=ramp([.0225, .017, .017, .02]), ebitda_margin=ramp([.262, .250, .240, .234]),
               capex=.046, tg=.020, troic=.085),
  "BASE": dict(growth=ramp([.044, .0325, .0325, .0325, .0325, .03]), ebitda_margin=ramp([.272]),
               capex=.040, tg=.030, troic=.10),
  "BULL": dict(growth=ramp([.049, .045, .045, .045, .04, .04, .035]), ebitda_margin=ramp([.275, .285, .295, .30]),
               capex=.034, tg=.035, troic=.12),
}
def kwargs(s, **over):
    p = {**SCEN[s], **over}
    da = fade(DA0, p["capex"])        # amortisation of acquired intangibles runs off; steady-state D&A = capex
    return dict(base_revenue=T_REV, growth=p["growth"], ebitda_margin=p["ebitda_margin"],
                capex_pct=[p["capex"]] * N, da_pct=da, tax=TAX, wacc=p.get("wacc", WACC),
                net_debt=NET_DEBT, shares=SHARES, terminal_growth=p["tg"], terminal_roic=p["troic"],
                wc_pct_of_delta_rev=WC)
print(f"Common: base revenue TTM {T_REV:,.1f} (yr1 = Jul-26..Jun-27) | tax {TAX:.0%} | WACC {WACC:.1%} | "
      f"net debt {NET_DEBT:,.1f} | shares {SHARES} | WC {WC:.1%} of delta rev | D&A {DA0:.1%} yrs1-5, fades to capex% by yr10")
res = {}
for s in ("BEAR", "BASE", "BULL"):
    kw = kwargs(s); r = dcf(**kw); res[s] = r
    p = SCEN[s]
    print(f"\n--- {s}: growth {[round(g*100,2) for g in p['growth']]}")
    print(f"    EBITDA m {[round(m*100,1) for m in p['ebitda_margin']]} capex {p['capex']:.1%} "
          f"g_term {p['tg']:.1%} ROIC_term {p['troic']:.1%}")
    print(f"{'yr':>3}{'Revenue':>9}{'EBITDA':>8}{'EBIT':>7}{'D&A':>7}{'Capex':>7}{'FCF':>7}{'FCFm':>7}{'PV':>7}")
    for y, rev, eb, ebit, da, cx, f, pv in r.rows:
        print(f"{y:>3}{rev:>9,.0f}{eb:>8,.0f}{ebit:>7,.0f}{da:>7,.0f}{cx:>7,.0f}{f:>7,.0f}{pct(f/rev):>7}{pv:>7,.0f}")
    print(f"PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} | TV share {r.terminal_share:.0%}"
          + ("  ** TV > 75% FLAG **" if r.terminal_share > .75 else ""))
    print(f"EV {r.enterprise_value:,.0f} | equity {r.equity_value:,.0f} | PER SHARE ${r.per_share:,.2f} | "
          f"vs ${PRICE}: {r.upside(PRICE):+.1%}")
adj = (1 + WACC) ** (3.5 / 12)
print(f"\nTiming note: cash flows are discounted from 2026-06-30; rolling to 2026-10-13 multiplies EV by {adj:.4f} "
      f"(BASE would be ${(res['BASE'].enterprise_value*adj-NET_DEBT)/SHARES:,.2f}). Not applied above.")

print("\nAlternative-basis checks on BASE:")
alt = {
 "no D&A fade (D&A stays 13.0%, terminal NOPAT on GAAP EBIT)": dict(da_pct=[DA0]*N),
 "uncaptured capex: +$348M/yr (vendor FCF 1,072 basis)": dict(capex_pct=[.040 + 348/T_REV]*N),
 "diluted share count 198.7 (FY25) instead of 190.74": dict(shares=198.7),
 "WC on inventory only (payables still UNKNOWN)": dict(wc_pct_of_delta_rev=INV[5]/REV[5]),
}
for lab, over in alt.items():
    kw = {**kwargs("BASE"), **over}
    if "da_pct" not in over and "capex_pct" in over:
        kw["da_pct"] = fade(DA0, over["capex_pct"][0])
    r = dcf(**kw)
    print(f"  {lab:<62} ${r.per_share:7.2f}  (TV {r.terminal_share:.0%})")

# =====================================================================================
line("F. REVERSE DCF & SENSITIVITY")
kwb = kwargs("BASE"); kwb.pop("base_revenue"); kwb.pop("growth")
g_impl = reverse_dcf(price=PRICE, base_revenue=T_REV, years=N, **kwb)
print(f"Implied constant 10-yr revenue CAGR at BASE margins/capex/WACC/g/ROIC: {g_impl:.2%} "
      f"(yr-10 revenue {T_REV*(1+g_impl)**N:,.0f})")
for s in ("BEAR", "BULL"):
    k = kwargs(s); k.pop("base_revenue"); k.pop("growth")
    print(f"  ...at {s} margins/capex/terminal: {reverse_dcf(price=PRICE, base_revenue=T_REV, years=N, **k):.2%}")
lo, hi = 0.10, 0.40
for _ in range(80):
    m = (lo + hi) / 2
    v = dcf(**kwargs("BASE", ebitda_margin=[m]*N)).per_share
    lo, hi = (m, hi) if v < PRICE else (lo, m)
print(f"Implied flat EBITDA margin at BASE growth: {m:.2%} (TTM {(T_OPINC+T_DA)/T_REV:.2%}, 5-yr low {min(em[1:]):.2%})")
lo, hi = 0.04, 0.25
for _ in range(80):
    w = (lo + hi) / 2
    v = dcf(**kwargs("BASE", wacc=w)).per_share
    lo, hi = (lo, w) if v < PRICE else (w, hi)
print(f"Implied discount rate (IRR) at BASE cash flows: {w:.2%}")
for s in ("BEAR", "BULL"):
    lo, hi = 0.03, 0.30
    for _ in range(80):
        w = (lo + hi) / 2
        v = dcf(**kwargs(s, wacc=w)).per_share
        lo, hi = (lo, w) if v < PRICE else (w, hi)
    print(f"  implied IRR at {s} cash flows: {w:.2%}")

waccs = [WACC - .01, WACC - .005, WACC, WACC + .005, WACC + .01]
gs = [.02, .025, .03, .035, .04]
grid = sensitivity({"wacc": waccs}, {"terminal_growth": gs}, **kwargs("BASE"))
print("\nBASE per-share: WACC (rows) x terminal growth (cols)")
print(f"{'':>8}" + "".join(f"{g:>9.1%}" for g in gs))
for w, row in zip(waccs, grid):
    print(f"{w:>8.1%}" + "".join(f"{v:>9.2f}" for v in row))
rocs = [.07, .085, .10, .12, .15]
grid2 = sensitivity({"wacc": waccs}, {"terminal_roic": rocs}, **kwargs("BASE"))
print("\nBASE per-share: WACC (rows) x terminal ROIC (cols), g 3.0%")
print(f"{'':>8}" + "".join(f"{r:>9.1%}" for r in rocs))
for w, row in zip(waccs, grid2):
    print(f"{w:>8.1%}" + "".join(f"{v:>9.2f}" for v in row))

# =====================================================================================
line("G. LOAD-BEARING INPUTS (+/-10% each, BASE)")
b0 = res["BASE"].per_share
def flex(name, f):
    lo_, hi_ = f(0.9), f(1.1)
    return name, lo_ - b0, hi_ - b0
B = SCEN["BASE"]
def mk(**o): return dcf(**kwargs("BASE", **o)).per_share
tests = [
 flex("EBITDA margin (27.2%)", lambda x: mk(ebitda_margin=[m*x for m in B["ebitda_margin"]])),
 flex("WACC (8.5%)", lambda x: mk(wacc=WACC*x)),
 flex("Net debt (7,069)", lambda x: dcf(**{**kwargs("BASE"), "net_debt": NET_DEBT*x}).per_share),
 flex("Base revenue (TTM 8,509)", lambda x: dcf(**{**kwargs("BASE"), "base_revenue": T_REV*x}).per_share),
 flex("Share count (190.74)", lambda x: dcf(**{**kwargs("BASE"), "shares": SHARES*x}).per_share),
 flex("Terminal D&A = capex endpoint (4.0%)", lambda x: dcf(**{**kwargs("BASE"), "da_pct": fade(DA0, .04*x)}).per_share),
 flex("Capex % rev (4.0%)", lambda x: dcf(**{**kwargs("BASE"), "capex_pct": [.04*x]*N}).per_share),
 flex("Terminal growth (3.0%)", lambda x: mk(tg=.03*x)),
 flex("Terminal ROIC (10%)", lambda x: mk(troic=.10*x)),
 flex("Tax rate (18%)", lambda x: dcf(**{**kwargs("BASE"), "tax": TAX*x}).per_share),
 flex("Revenue growth path", lambda x: mk(growth=[g*x for g in B["growth"]])),
 flex("WC % of delta revenue (48.5%)", lambda x: dcf(**{**kwargs("BASE"), "wc_pct_of_delta_rev": WC*x}).per_share),
]
tests.sort(key=lambda t: -(abs(t[1]) + abs(t[2])))
print(f"BASE ${b0:.2f}")
for n_, d_lo, d_hi in tests:
    print(f"  {n_:<40} -10%: {d_lo:+7.2f} ({d_lo/b0:+.1%})   +10%: {d_hi:+7.2f} ({d_hi/b0:+.1%})")
