"""MC.PA (LVMH) - FULL template model, as of 2026-10-13. EUR millions unless stated.

Primary: consolidated 10-year FCFF DCF via methodologies/valuation.py (bear / trough-margin /
base / bull), reverse DCF, WACC x g grid, +/-10% load-bearing sweep.
Secondary: segment-multiple cross-check (dossier S0 suggestion), Lynch and Buffett metrics.

IFRS 16 TREATMENT (stated once, applied everywhere):
  Leases are treated as an OPERATING cost. EBIT is put on a pre-IFRS 16 basis:
      EBIT_adj = PRO - (lease principal + lease interest - right-of-use depreciation)
  D&A in the model excludes ROU depreciation. Lease liabilities (16,261) are therefore
  EXCLUDED from the EV bridge. They are never both deducted and added.
SBC TREATMENT: bonus-share expense is already charged inside PRO under IFRS 2 and is not
  added back anywhere in the model; share count is held flat at 495.811m. (Deduct, not dilute.)
EV BRIDGE: net financial debt + minority-put commitments + minority interests at book.
  DFS held-for-sale net assets and non-current investments are NOT credited (conservative).

Every input is tagged: (facts: ...), (dossier S#), (fj: fundamentals.json), or
ASSUMPTION (Quant-chosen; Skeptic should attack these first).
Run: python3 reports/runs/MC.PA_2026-10-13/02_model.py
"""
import json
import pathlib
import statistics as st
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
F = json.loads((RUN / "facts.json").read_text())
A, H1_26, H1_25, Q3, TTM, MKT = (F["annual"], F["interim"]["H1_2026"], F["interim"]["H1_2025"],
                                 F["interim"]["Q3_2026"], F["ttm"], F["market"])
FJ = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["MC.PA"]
YRS = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
s = lambda key: [A[key][y] for y in YRS]

def hdr(t):
    print("\n" + "=" * 92 + f"\n{t}\n" + "=" * 92)

# ------------------------------------------------------------------ sourced market inputs
PRICE = MKT["price_eur"]                                     # facts: market.price_eur
SHARES = H1_26["shares_issued_30jun2026"] / 1e6              # facts: 495.811m issued 30 Jun 26
MCAP = PRICE * SHARES
NFD = H1_26["nfd"]                                           # facts: 8,245 (nets cash + AFS)
PUTS = H1_26["purchase_commitments_minorities"]              # facts: 6,416
MI_BOOK = H1_26["minority_interests_equity"]                 # facts: 1,599
LEASES = H1_26["lease_total"]                                # facts: 16,261 (excluded from bridge)
CLAIMS = NFD + PUTS + MI_BOOK
EV_EXL = MCAP + CLAIMS
EV_INL = EV_EXL + LEASES
RF = MKT["ten_year_yield_france_oat_pct"] / 100              # facts: 4.75% OAT (SECONDARY source)

hdr("0. SNAPSHOT AND EV BRIDGE")
print(f"Price EUR {PRICE} | shares {SHARES:.3f}m | market cap {MCAP:,.0f}")
print(f"Claims: NFD {NFD:,} + minority puts {PUTS:,} + minorities (book) {MI_BOOK:,} = {CLAIMS:,}"
      f"  ({CLAIMS/SHARES:.2f}/share)")
print(f"EV ex-leases (model basis) {EV_EXL:,.0f} | EV incl. leases (IFRS 16 basis) {EV_INL:,.0f}")
# Cross-check on minorities: capitalise TTM minority P&L share at own trailing P/E
H1_25_PRE_MI = 5915                                          # dossier S2 table: H1-25 net profit before minorities
mi_ttm = -A["minority_interests"]["FY2025"] - H1_26["minority_interests"] - (H1_25_PRE_MI - H1_25["net_profit_group"])
pe_own = PRICE / TTM["eps_diluted"]
print(f"Cross-check: TTM minority share of profit {mi_ttm:,} x own P/E {pe_own:.1f} = "
      f"{mi_ttm*pe_own:,.0f} vs puts+book {PUTS+MI_BOOK:,} (not used; shows bridge is not light)")

# ------------------------------------------------------------------ history / ratios
hdr("1. HISTORY: MARGINS, TAX, CAPITAL INTENSITY, ROIC")
rev, gp, pro = s("revenue"), s("gross_profit"), s("profit_from_recurring_operations")
op, nfi, tax = s("operating_profit_ebit_reported"), s("net_financial_income_expense"), s("income_taxes")
da_tot, rou = s("d_and_a_incl_provisions_plus_rou_depr"), s("depreciation_of_right_of_use_assets")
capex = [-x for x in s("operating_investments_capex")]
lp = [-x for x in s("repayment_of_lease_liabilities")]
ofcf, eq_tot, nfd_h = s("operating_free_cash_flow_company_def"), s("equity_total"), \
    s("net_financial_debt_excl_leases_excl_minority_puts")
leases_h = s("lease_liabilities_total_ifrs16")
etr = [-t / (o + n) for t, o, n in zip(tax, op, nfi)]
da_x = [d - r for d, r in zip(da_tot, rou)]                  # D&A + provisions, ex-ROU
gm = [g / r for g, r in zip(gp, rev)]
pm = [p / r for p, r in zip(pro, rev)]
print(f"{'':<26}" + "".join(f"{y:>10}" for y in YRS))
rowp = lambda lab, v, f="{:>10.1%}": print(f"{lab:<26}" + "".join(f.format(x) for x in v))
rowp("Revenue", rev, "{:>10,}")
rowp("Gross margin", gm)
rowp("PRO margin", pm)
rowp("Effective tax rate", etr)
rowp("Capex / revenue", [c / r for c, r in zip(capex, rev)])
rowp("D&A ex-ROU / revenue", [d / r for d, r in zip(da_x, rev)])
rowp("Capex / D&A ex-ROU", [c / d for c, d in zip(capex, da_x)], "{:>10.2f}")
rowp("Company op. FCF margin", [f / r for f, r in zip(ofcf, rev)])
nopat = [p * (1 - t) for p, t in zip(pro, etr)]
ic = [e + n for e, n in zip(eq_tot, nfd_h)]
roic = [n / i for n, i in zip(nopat, ic)]
roic_l = [n / (i + l) for n, i, l in zip(nopat, ic, leases_h)]
rowp("ROIC (eq+NFD)", roic)
rowp("ROIC incl. leases in IC", roic_l)
gw = {"FY2023": 24022, "FY2025": 18315}                      # dossier S5 (Yahoo balance sheet, S7)
for y, g in gw.items():
    i = YRS.index(y)
    print(f"  {y}: goodwill {g:,} = {g/ic[i]:.1%} of IC; ROIC ex-goodwill {nopat[i]/(ic[i]-g):.1%}")
avg = lambda v: sum(v) / len(v)
PRO_AVG, PRO_LOW, PRO_HIGH = avg(pm), min(pm), max(pm)
TTM_PRO_M = TTM["pro"] / TTM["revenue"]
ETR_AVG = avg(etr)
ETR_H1 = H1_26["income_taxes"] * -1 / (H1_26["net_profit_before_minorities"] - H1_26["income_taxes"])
CAPEX_AVG = avg([c / r for c, r in zip(capex, rev)])
DA_AVG = avg([d / r for d, r in zip(da_x, rev)])
FCFM_AVG = avg([f / r for f, r in zip(ofcf, rev)])
print(f"5-yr: PRO margin avg {PRO_AVG:.2%}, low {PRO_LOW:.2%}, high {PRO_HIGH:.2%}; TTM {TTM_PRO_M:.2%}")
print(f"5-yr: ETR avg {ETR_AVG:.2%} | H1-26 ETR {ETR_H1:.2%} | capex/rev avg {CAPEX_AVG:.2%} | "
      f"D&A ex-ROU/rev avg {DA_AVG:.2%} | company FCF margin avg {FCFM_AVG:.2%} | "
      f"ROIC avg {avg(roic):.1%}")
seg = A["pro_by_group"]; segr = A["revenue_by_group"]
print("FLG PRO margin: " + ", ".join(f"{y} {seg[y]['FLG']/segr[y]['FLG']:.1%}" for y in YRS) +
      f", H1-26 {H1_26['pro_by_group']['FLG']/H1_26['revenue_by_group']['FLG']:.1%}")
print(f"Gross margin H1-25 {H1_25['gross_profit']/H1_25['revenue']:.1%} -> H1-26 "
      f"{H1_26['gross_profit']/H1_26['revenue']:.1%}")

# ------------------------------------------------------------------ lease adjustment + cash gap
hdr("2. IFRS 16 ADJUSTMENT AND CASH-CONVERSION CALIBRATION (FY2024, FY2025: lease interest known)")
LEASE_INT = {"FY2024": 510, "FY2025": 553}                   # dossier S5 (S1)
COST_NFD = {"FY2024": 442, "FY2025": 348}                    # dossier S5 (S1)
gaps, ladj = [], []
for y in ("FY2024", "FY2025"):
    i = YRS.index(y)
    adj = lp[i] + LEASE_INT[y] - rou[i]                       # lease cash in excess of ROU depr
    ebit_adj = pro[i] - adj
    model_fcf = ebit_adj * (1 - etr[i]) + da_x[i] - capex[i]
    reported_unlev = ofcf[i] + COST_NFD[y] * (1 - etr[i])
    gap = model_fcf - reported_unlev
    gaps.append(gap / rev[i]); ladj.append(adj / rev[i])
    print(f"{y}: lease cash {lp[i]+LEASE_INT[y]:,} - ROU depr {rou[i]:,} = adj {adj:,} ({adj/rev[i]:.2%} rev)"
          f" | EBIT_adj {ebit_adj:,} | model pre-WC FCF {model_fcf:,.0f} vs reported unlevered "
          f"{reported_unlev:,.0f} -> gap {gap:,.0f} ({gap/rev[i]:.2%} rev)")
LEASE_ADJ = ladj[-1]                                          # FY2025 ratio carried forward
GAP_AVG, GAP_HI, GAP_LO = avg(gaps), max(gaps), min(gaps)
print(f"Lease adj carried forward {LEASE_ADJ:.2%} of revenue (FY2025). "
      f"Cash gap (WC/other/tax timing): avg {GAP_AVG:.2%}, high {GAP_HI:.2%}, low {GAP_LO:.2%}")
EBITDA_ADJ25 = pro[-1] - ladj[-1] * rev[-1] + da_x[-1]
print(f"FY2025 pre-IFRS16 EBITDA = {EBITDA_ADJ25:,.0f} ({EBITDA_ADJ25/rev[-1]:.1%})")

# ------------------------------------------------------------------ owner earnings, Lynch
hdr("3. OWNER EARNINGS, LYNCH METRICS, DEBT")
NI25 = A["net_profit_group_share"]["FY2025"]
OE_FJ = FJ["owner_earnings"] / 1e6
OE_LEASE = NI25 + da_tot[-1] - capex[-1] - lp[-1]
OE_LEASE_FJCAPEX = NI25 + da_tot[-1] - (-FJ["capex"] / 1e6) - lp[-1]
SBC25, SBC_TTM = A["sbc_bonus_share_expense"]["FY2025"], 187
print(f"Owner earnings (fj, AGENTS.md def) = {NI25:,} + {da_tot[-1]:,} - {-FJ['capex']/1e6:,.0f} = {OE_FJ:,.0f}"
      f"  yield {OE_FJ/MCAP:.2%}")
print(f"Lease-adjusted OE = {NI25:,} + {da_tot[-1]:,} - {capex[-1]:,} - lease principal {lp[-1]:,} = "
      f"{OE_LEASE:,.0f}  yield {OE_LEASE/MCAP:.2%}  (with fj capex 4,670: {OE_LEASE_FJCAPEX:,.0f})")
print(f"SBC: already expensed in NI, so OE above is SBC-burdened. FCF-based (SBC added back in OCF): "
      f"TTM company FCF {TTM['operating_fcf']:,} - SBC {SBC_TTM} = {TTM['operating_fcf']-SBC_TTM:,} "
      f"-> SBC-adj FCF yield {(TTM['operating_fcf']-SBC_TTM)/MCAP:.2%}")

eps_t, eps25 = TTM["eps_diluted"], A["eps_diluted_eur"]["FY2025"]
eps21 = A["eps_diluted_eur"]["FY2021"]
rev_cagr = (rev[-1] / rev[0]) ** (1 / 4) - 1
eps_cagr = (eps25 / eps21) ** (1 / 4) - 1
cons27 = (F["consensus_labelled"]["eps_fy2027_avg"] / eps25) ** 0.5 - 1
print(f"Revenue CAGR FY21-25 {rev_cagr:.2%} | EPS CAGR FY21-25 {eps_cagr:.2%} | "
      f"EPS peak-to-FY25 {eps25/A['eps_diluted_eur']['FY2023']-1:.1%} | "
      f"CONSENSUS EPS CAGR FY25-27 {cons27:.2%}")
print("YoY revenue: " + ", ".join(f"{rev[i]/rev[i-1]-1:+.1%}" for i in range(1, 5)) +
      " | YoY EPS: " + ", ".join(f"{A['eps_diluted_eur'][YRS[i]]/A['eps_diluted_eur'][YRS[i-1]]-1:+.1%}"
                                for i in range(1, 5)))
pe_fj, fpe_fj = FJ["trailing_pe"], FJ["forward_pe"]
g_lower = min(eps_cagr, cons27)
ok, why = peg_is_valid(pe_own, fpe_fj, g_lower)
print(f"PEG gate (trailing {pe_own:.1f}, forward {fpe_fj:.1f}, growth = lower of hist/consensus "
      f"{g_lower:.2%}): {'VALID' if ok else 'VOID'} - {why}")
ok2, why2 = peg_is_valid(pe_own, fpe_fj, cons27)
print(f"  (consensus-only growth {cons27:.2%} would give: {'VALID' if ok2 else 'VOID'} - {why2}; not used)")
dy = MKT["dividend_yield_pct_13_eur"]
for lab, g in (("hist EPS CAGR", eps_cagr), ("CONSENSUS FY25-27", cons27)):
    print(f"Lynch ratio ({lab}) = ({g*100:.1f} + {dy:.2f}) / {pe_own:.1f} = {(g*100+dy)/pe_own:.2f}")
nc_ps = -NFD / SHARES
print(f"Net-cash-adj P/E = ({PRICE} - ({nc_ps:.2f})) / {eps_t} = {(PRICE-nc_ps)/eps_t:.1f}x | "
      f"incl. puts: {(PRICE+(NFD+PUTS)/SHARES)/eps_t:.1f}x")
# Normalised (mid-cycle) EPS: PRO at 5-yr avg margin on TTM revenue
mi_share = -A["minority_interests"]["FY2025"] / A["net_profit_before_minorities"]["FY2025"]
ni_norm = (PRO_AVG * TTM["revenue"] + nfi[-1] + A["operating_profit_ebit_reported"]["FY2025"]
           - pro[-1]) * (1 - ETR_AVG) * (1 - mi_share)
eps_norm = ni_norm / (H1_26["diluted_shares_weighted_avg"] / 1e6)
print(f"Normalised EPS (PRO {PRO_AVG:.1%} x TTM rev, FY25 fin. & other-op items, ETR {ETR_AVG:.1%}, "
      f"MI {mi_share:.1%}) = {eps_norm:.2f} -> normalised P/E {PRICE/eps_norm:.1f}x")
dps = A["dividend_per_share_eur_for_fiscal_year"]["FY2025"]
print(f"Dividend: payout {dps/eps25:.1%} of EPS; EPS cover {eps25/dps:.2f}x; op FCF / dividends paid "
      f"(incl MI) {ofcf[-1]/-A['dividends_paid_incl_minorities']['FY2025']:.2f}x; "
      f"op FCF / Group-share dividends 6,463 = {ofcf[-1]/6463:.2f}x")
print(f"Net debt / lease-adj OE: NFD {NFD/OE_LEASE:.2f}x | NFD+puts {(NFD+PUTS)/OE_LEASE:.2f}x | "
      f"NFD+puts+leases vs fj OE {(NFD+PUTS+LEASES)/OE_FJ:.2f}x")
print(f"Interest cover FY25: PRO / cost of NFD {pro[-1]/348:.0f}x; PRO / (NFD cost + lease int) "
      f"{pro[-1]/(348+553):.1f}x")
mat = F["debt_maturities_gross_after_derivatives_31dec2025"]
print(f"Maturities: 2026 {mat['2026']:,}, 2027 {mat['2027']:,}, 2028 {mat['2028']:,} vs cash+AFS "
      f"{A['cash_plus_current_afs_financial_assets']['FY2025']:,} (Dec-25), "
      f"{H1_26['cash_and_equivalents']+H1_26['current_afs_financial_assets']:,} (Jun-26)")

# ------------------------------------------------------------------ multiples matrix
hdr("4. MULTIPLES MATRIX (current)")
ebitda_ifrs_ttm = TTM["pro"] + 7857                           # dossier S2 TTM D&A 7,857
peers = {"RMS": (30.3, 26.1, 18.0, 3.7), "KER": (None, 21.4, 14.5, 10.0),
         "CFR": (31.5, 21.2, 18.2, 2.6), "PRADA": (11.4, 9.7, 6.6, 1.9)}   # dossier S7
med = lambda k: st.median([v[k] for v in peers.values() if v[k] is not None])
fcf_y_yahoo = TTM["nocf"] - (-TTM["operating_investments"])
rows = [
    ("EV/EBITDA (IFRS16: EV incl leases / PRO+D&A TTM)", f"{EV_INL/ebitda_ifrs_ttm:.1f}x", f"{med(2):.1f}x (Yahoo basis; LVMH Yahoo 10.8x)"),
    ("EV/EBITDA (pre-IFRS16: EV ex-leases / FY25 adj)", f"{EV_EXL/EBITDA_ADJ25:.1f}x", "n/a"),
    ("P/E trailing (own TTM EPS 21.94)", f"{pe_own:.1f}x", f"{med(0):.1f}x"),
    ("P/E forward (fj)", f"{fpe_fj:.1f}x", f"{med(1):.1f}x"),
    ("P/E on CONSENSUS FY26 / FY27 EPS", f"{PRICE/22.18:.1f}x / {PRICE/24.43:.1f}x", "n/a"),
    ("P/E on normalised (mid-cycle) EPS", f"{PRICE/eps_norm:.1f}x", "n/a"),
    ("P/FCF (company def., TTM)", f"{MCAP/TTM['operating_fcf']:.1f}x", "n/a"),
    ("P/FCF SBC-adjusted", f"{MCAP/(TTM['operating_fcf']-SBC_TTM):.1f}x", "n/a"),
    ("FCF yield (company def. TTM)", f"{fcf_yield(TTM['operating_fcf'], MCAP):.2%}", "n/a"),
    ("FCF yield (OCF-capex, Yahoo-style, TTM)", f"{fcf_yield(fcf_y_yahoo, MCAP):.2%}", f"{med(3):.2f}%"),
    ("Owner-earnings yield (fj def / lease-adj)", f"{OE_FJ/MCAP:.2%} / {OE_LEASE/MCAP:.2%}", "n/a"),
    ("PEG", "VOID (not cited)", "n/a"),
    ("Lynch ratio (hist / consensus growth)", f"{(eps_cagr*100+dy)/pe_own:.2f} / {(cons27*100+dy)/pe_own:.2f}", "n/a"),
    ("Dividend yield", f"{dy:.2f}%", "n/a"),
]
for r in rows:
    print(f"{r[0]:<52}{r[1]:>22}   peer median: {r[2]}")
print(f"P/E 12m ago (527.18 / FY24 EPS 25.12, last full year then reported): {527.18/25.12:.1f}x")

# ------------------------------------------------------------------ discount rate
hdr("5. DISCOUNT RATE")
ERP, BETA = 0.05, 1.0                                         # instruction: ERP 5%, beta 1.0 (no sourced beta)
KE = RF + BETA * ERP
KD_PRE = RF                                                   # ASSUMPTION: OAT as cost of debt; LVMH spread UNKNOWN
KD_HIST = 348 / ((9228 + 6857) / 2)                           # FY25 cost of NFD / avg NFD (facts)
KD = KD_PRE * (1 - ETR_AVG)
E_W = MCAP + PUTS + MI_BOOK                                   # puts + minorities are equity-like claims at Ke
D_W = NFD
WACC_RAW = (E_W * KE + D_W * KD) / (E_W + D_W)
FLOOR = RF + 0.04
WACC = max(WACC_RAW, FLOOR)
print(f"Ke = {RF:.2%} + {BETA} x {ERP:.0%} = {KE:.2%}")
print(f"Kd pre-tax {KD_PRE:.2%} (OAT proxy; historic cost of NFD on avg NFD = {KD_HIST:.2%}); "
      f"after tax at {ETR_AVG:.1%} = {KD:.2%}")
print(f"Weights: equity-like {E_W:,.0f} ({E_W/(E_W+D_W):.1%}), net debt {D_W:,} ({D_W/(E_W+D_W):.1%})")
print(f"WACC = {WACC_RAW:.2%}; floor (local 10y + 4%) = {FLOOR:.2%}; USED = {WACC:.2%}")
WACC = round(WACC, 3)
print(f"Rounded WACC used in DCF: {WACC:.1%}")

# ------------------------------------------------------------------ scenarios
hdr("6. DCF SCENARIOS (10 yr, FCFF, pre-IFRS16 basis)")
BASE_REV = TTM["revenue_ttm_to_9m2026"]                       # facts: 79,865 (TTM to Sep-26)
N = 10
def path(*pairs):
    out = []
    for v, c in pairs:
        out += [v] * c
    while len(out) < N:
        out.append(out[-1])
    return out[:N]

def build(g, pro_m, capex_p=CAPEX_AVG, da_p=DA_AVG, gap=GAP_AVG, lease_adj=LEASE_ADJ, tax=ETR_AVG,
          wacc=WACC, tg=0.03, roic=0.15, claims=CLAIMS, base=BASE_REV, wc=0.0):
    return dict(base_revenue=base, growth=g,
                ebitda_margin=[m - lease_adj + da_p for m in pro_m],
                capex_pct=[capex_p + gap] * N, da_pct=[da_p] * N, tax=tax, wacc=wacc,
                net_debt=claims, shares=SHARES, terminal_growth=tg, terminal_roic=roic,
                wc_pct_of_delta_rev=wc)

SCEN = {
    # ASSUMPTIONS throughout; anchors in comments
    "BEAR": dict(  # China downturn deepens yrs 1-2 (Q3 FLG -5%, Asia ex-Japan -5%); margins only
                   # recover to the 5-yr low; FY24 cash gap; H1-26 tax rate
        g=path((-0.01, 1), (-0.03, 1), (0.02, 1), (0.03, 3), (0.025, 2), (0.02, 2)),
        pro_m=[0.212, 0.205, 0.210, 0.215, PRO_LOW] + [PRO_LOW] * 5,
        gap=GAP_HI, tax=ETR_H1, tg=0.02, roic=0.12),
    "TROUGH": dict(  # orchestrator ask: base growth, margin frozen at TTM trough
        g=path((0.01, 1), (0.045, 1), (0.05, 3), (0.045, 1), (0.04, 2), (0.035, 1), (0.03, 1)),
        pro_m=[TTM_PRO_M] * N, tg=0.03, roic=0.15),
    "BASE": dict(  # yr1 = organic +2% (9M) less ~1pt scope (DFS, Marc Jacobs); yr2 = CONSENSUS
                   # FY27 rev +4.6%; yrs 3-5 5% (below FY21-25 CAGR 5.9%); fade to 3%.
                   # PRO margin recovers linearly to 5-yr average by yr 5 (mid-cycle).
        g=path((0.01, 1), (0.045, 1), (0.05, 3), (0.045, 1), (0.04, 2), (0.035, 1), (0.03, 1)),
        pro_m=[TTM_PRO_M + (PRO_AVG - TTM_PRO_M) * min(i, 4) / 4 for i in range(N)],
        tg=0.03, roic=0.15),
    "BULL": dict(  # FX headwind eases 2027 (CFO, S9 secondary); W&J +8% / SR +6% 9M organic;
                   # margin back to FY21-23 level (26.5-26.7%) by yr 4; FY25 cash gap; FY21/23 ETR
        g=path((0.02, 1), (0.06, 1), (0.07, 2), (0.065, 1), (0.06, 1), (0.055, 1), (0.05, 1),
               (0.045, 1), (0.04, 1)),
        pro_m=[0.222, 0.235, 0.250, 0.265] + [0.265] * 6,
        gap=GAP_LO, tax=etr[0], tg=0.035, roic=0.20),
}
RES = {}
for name, p in SCEN.items():
    kw = build(**p)
    r = dcf(**kw)
    RES[name] = (r, kw)
    print(f"\n--- {name}: WACC {kw['wacc']:.1%} | g_T {kw['terminal_growth']:.1%} | ROIC_T "
          f"{kw['terminal_roic']:.0%} | tax {kw['tax']:.1%} | capex+gap {kw['capex_pct'][0]:.2%} | "
          f"D&A {kw['da_pct'][0]:.2%} | lease adj {LEASE_ADJ:.2%}")
    print("growth:     " + " ".join(f"{x:+.1%}" for x in kw["growth"]))
    print("PRO margin: " + " ".join(f"{m:.1%}" for m in p["pro_m"]))
    print(f"{'Yr':<4}{'Revenue':>10}{'EBITDA':>9}{'EBIT':>9}{'D&A':>8}{'Cap+gap':>9}{'FCF':>9}"
          f"{'FCF%':>7}{'PV':>9}")
    for y, rv, eb, ei, da, cx, fcf, pv in r.rows:
        print(f"{y:<4}{rv:>10,.0f}{eb:>9,.0f}{ei:>9,.0f}{da:>8,.0f}{cx:>9,.0f}{fcf:>9,.0f}"
              f"{fcf/rv:>7.1%}{pv:>9,.0f}")
    flag = "  <-- TV > 75% FLAG" if r.terminal_share > 0.75 else ""
    print(f"PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} "
          f"({r.terminal_share:.0%} of EV){flag}")
    print(f"EV {r.enterprise_value:,.0f} - claims {CLAIMS:,} = equity {r.equity_value:,.0f} -> "
          f"EUR {r.per_share:,.0f}/share vs {PRICE} ({r.upside(PRICE):+.0%})")
print(f"\nReconciliation: TTM company FCF margin {TTM['operating_fcf']/TTM['revenue']:.1%} (levered); "
      f"5-yr avg {FCFM_AVG:.1%}; BASE yr1 model {RES['BASE'][0].rows[0][6]/RES['BASE'][0].rows[0][1]:.1%}, "
      f"yr5+ {RES['BASE'][0].rows[5][6]/RES['BASE'][0].rows[5][1]:.1%}")

# ------------------------------------------------------------------ reverse DCF
hdr("7. REVERSE DCF")
bk = RES["BASE"][1]
rkw = {k: v for k, v in bk.items() if k not in ("base_revenue", "growth")}
g_imp = reverse_dcf(price=PRICE, base_revenue=BASE_REV, years=N, **rkw)
print(f"BASE margins/WACC {WACC:.1%}/g 3%/ROIC 15%: price implies constant 10-yr revenue CAGR {g_imp:.2%}")
tk = RES["TROUGH"][1]
g_imp_t = reverse_dcf(price=PRICE, base_revenue=BASE_REV, years=N,
                      **{k: v for k, v in tk.items() if k not in ("base_revenue", "growth")})
print(f"TROUGH margin ({TTM_PRO_M:.1%} flat): price implies constant 10-yr revenue CAGR {g_imp_t:.2%}")
# implied steady-state PRO margin at BASE growth path (bisection on margin)
lo, hi = 0.10, 0.40
for _ in range(60):
    m = (lo + hi) / 2
    v = dcf(**build(SCEN["BASE"]["g"], [TTM_PRO_M + (m - TTM_PRO_M) * min(i, 4) / 4 for i in range(N)])).per_share
    lo, hi = (m, hi) if v < PRICE else (lo, m)
print(f"At BASE growth path, price implies PRO margin reaching {m:.2%} by yr 5 "
      f"(TTM {TTM_PRO_M:.1%}, 5-yr avg {PRO_AVG:.1%}, 5-yr low {PRO_LOW:.1%})")
# implied WACC at base
lo, hi = 0.05, 0.15
for _ in range(60):
    w = (lo + hi) / 2
    v = dcf(**build(**{**SCEN["BASE"], "wacc": w})).per_share
    lo, hi = (w, hi) if v > PRICE else (lo, w)
print(f"BASE operating case: price implies a discount rate (IRR) of {w:.2%}")

# ------------------------------------------------------------------ sensitivity
hdr("8. SENSITIVITY (BASE): WACC x terminal growth, EUR/share")
waccs = [round(WACC + d, 4) for d in (-0.01, -0.005, 0, 0.005, 0.01)]
tgs = [0.02, 0.025, 0.03, 0.035, 0.04]
grid = sensitivity({"wacc": waccs}, {"terminal_growth": tgs}, **bk)
print(f"{'WACC/g':<10}" + "".join(f"{g:>9.1%}" for g in tgs))
for wv, row in zip(waccs, grid):
    print(f"{wv:<10.1%}" + "".join(f"{v:>9,.0f}" for v in row))
print("\nBASE: WACC x terminal ROIC (g 3%)")
rocs = [0.10, 0.12, 0.15, 0.20, 0.25]
grid2 = sensitivity({"wacc": waccs}, {"terminal_roic": rocs}, **bk)
print(f"{'WACC/ROIC':<12}" + "".join(f"{r_:>9.0%}" for r_ in rocs))
for wv, row in zip(waccs, grid2):
    print(f"{wv:<12.1%}" + "".join(f"{v:>9,.0f}" for v in row))
print("\nBASE: steady-state PRO margin (reached yr5) x WACC")
ms = [PRO_LOW, 0.235, PRO_AVG, PRO_HIGH]
print(f"{'WACC/PRO':<12}" + "".join(f"{x:>9.1%}" for x in ms))
for wv in waccs:
    vals = [dcf(**build(SCEN["BASE"]["g"], [TTM_PRO_M + (x - TTM_PRO_M) * min(i, 4) / 4 for i in range(N)],
                        wacc=wv)).per_share for x in ms]
    print(f"{wv:<12.1%}" + "".join(f"{v:>9,.0f}" for v in vals))

# ------------------------------------------------------------------ load-bearing +/-10%
hdr("9. LOAD-BEARING INPUTS: +/-10% (relative) on BASE, EUR/share")
base_ps = RES["BASE"][0].per_share
B = SCEN["BASE"]
def run(**over):
    p = {**B, **over}
    return dcf(**build(**p)).per_share
tests = {
    "Steady-state PRO margin (5-yr avg)": lambda f: run(pro_m=[TTM_PRO_M + (PRO_AVG*f - TTM_PRO_M) * min(i, 4) / 4 for i in range(N)]),
    "WACC": lambda f: run(wacc=WACC * f),
    "Revenue growth (all yrs)": lambda f: run(g=[x * f for x in B["g"]]),
    "Terminal growth": lambda f: run(tg=0.03 * f),
    "Tax rate": lambda f: run(tax=ETR_AVG * f),
    "Capex / revenue": lambda f: run(capex_p=CAPEX_AVG * f),
    "D&A / revenue (add-back)": lambda f: run(da_p=DA_AVG * f),
    "Terminal ROIC": lambda f: run(roic=0.15 * f),
    "Base revenue (TTM)": lambda f: run(base=BASE_REV * f),
    "Cash-conversion gap": lambda f: run(gap=GAP_AVG * f),
    "Claims (NFD+puts+MI)": lambda f: run(claims=CLAIMS * f),
    "Lease adjustment": lambda f: run(lease_adj=LEASE_ADJ * f),
}
out = []
for k, fn in tests.items():
    lo_v, hi_v = fn(0.9), fn(1.1)
    out.append((abs(hi_v - lo_v), k, lo_v, hi_v))
print(f"BASE = EUR {base_ps:,.1f}")
print(f"{'Input':<38}{'-10%':>10}{'+10%':>10}{'swing':>10}")
for sw, k, lo_v, hi_v in sorted(out, reverse=True):
    print(f"{k:<38}{lo_v:>10,.1f}{hi_v:>10,.1f}{sw:>10,.1f}")
print(f"WC intensity (UNKNOWN, base 0): each 10% of incremental revenue tied up -> "
      f"{run(wc=0.10) - base_ps:+.1f}/share; 25% -> {run(wc=0.25) - base_ps:+.1f}/share")
print(f"Crediting DFS held-for-sale net assets (2,074 - 1,025): {(2074-1025)/SHARES:+.1f}/share (not taken)")
print(f"Tax at H1-26 ETR {ETR_H1:.1%} instead of 5-yr avg: {run(tax=ETR_H1) - base_ps:+.1f}/share")
CAPEX_TTM = -TTM["operating_investments"] / TTM["revenue"]
print(f"BASE with TTM capex/rev {CAPEX_TTM:.2%} and FY25 cash gap {GAP_LO:.2%} (i.e. today's cash conversion "
      f"persists): EUR {run(capex_p=CAPEX_TTM, gap=GAP_LO):,.1f}/share; TROUGH on same basis: EUR "
      f"{dcf(**build(**{**SCEN['TROUGH'], 'capex_p': CAPEX_TTM, 'gap': GAP_LO})).per_share:,.1f}/share")
print("Note: 'Base revenue' is a reported figure (low uncertainty); its swing shows operating leverage, "
      "not estimate risk.")

# ------------------------------------------------------------------ segment cross-check
hdr("10. SEGMENT-MULTIPLE CROSS-CHECK (secondary; peer P/E used as EV/NOPAT proxy)")
fwd_med = med(1)
own_fwd = fpe_fj
def segval(pro_by, mult_lux, mult_other, t=ETR_AVG):
    lux = (pro_by["FLG"] + pro_by["WJ"]) * (1 - t) * mult_lux
    oth = (pro_by["WS"] + pro_by["PC"] + pro_by["SR"] + pro_by["Other_elim"]) * (1 - t) * mult_other
    return (lux + oth - CLAIMS) / SHARES
mid = {k: avg([seg[y][k] for y in YRS]) for k in seg["FY2025"]}
for lab, pb in (("FY2025 segment PRO (trough)", seg["FY2025"]), ("5-yr avg segment PRO (mid-cycle)", mid)):
    for mo_lab, mo in (("others @ Prada 9.7x", 9.7), (f"others @ LVMH fwd {own_fwd:.1f}x", own_fwd)):
        print(f"{lab:<34} FLG+W&J @ peer fwd median {fwd_med:.1f}x, {mo_lab:<22}: EUR {segval(pb, fwd_med, mo):,.0f}/share")
print(f"FLG+W&J at Prada {9.7}x and others at {9.7}x (FY25): EUR {segval(seg['FY2025'], 9.7, 9.7):,.0f}/share")
