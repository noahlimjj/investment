"""NVO (Novo Nordisk ADR, 1 ADR = 1 B share) - FULL template model, as of 2026-10-13.
DKK millions unless stated. Modelled in DKK per share; converted to USD per ADR at the
00_inputs.json spot rate (DKKUSD).

Primary: 10-year FCFF DCF (bear / base / bull) via methodologies/valuation.py, reverse DCF,
WACC x g grid, +/-10% load-bearing sweep, plus LOE-timing and WAC-cut cash stress tests.

TREATMENTS (stated once, applied everywhere):
  BASE PERIOD    FY2025 (31 Dec 2025), revenue/EBIT put on an "adjusted" basis = reported less the
                 non-cash 340B provision reversal plus impairments. This is the definition the
                 company's H1-26 adjusted EBIT reconciles to (checked below). Year 1 = FY2026.
  VALUATION DATE dcf(mid_year=True, stub_years = 31 Dec 2025 -> 13 Oct 2026). Because the EV is
                 rolled forward and contains all FY2026 FCF, the bridge uses Dec-25 net debt PLUS
                 every distribution paid since then (FY25 final dividend, 2026 interim dividend,
                 2026 buybacks) and the CURRENT share count (4,413.1m, 6-K 9 Oct 2026).
  IFRS 16        Leases kept IN net debt (reported Borrowings; dossier S1 infers leases sit inside
                 Borrowings, UNCONFIRMED), and FCF is pre-lease (EBIT + D&A incl. ROU depreciation
                 - cash capex; lease principal not deducted). Sensitivity shown if leases are
                 outside Borrowings.
  SBC            DEDUCT method: IFRS 2 charges SBC inside EBIT and the model never adds it back;
                 share count held flat. (No dilution layer.)
  ACQUIRED INTANGIBLES  Akero (DKK 29,973m "purchase of intangibles" FY2025) treated as M&A, not
                 maintenance capex (orchestrator note). A recurring business-development /
                 in-licensing allowance (median FY21-24 purchase-of-intangibles / revenue) is
                 charged every year instead. acq_amort_pct NOT used: D&A (14.7bn) is 0.24x capex,
                 the opposite of the acquisition-heavy case, so terminal NOPAT is not depressed by
                 acquired-intangible amortisation.
  FY2026 CASH    Year-1 FCF is calibrated to the company's FY2026 FCF guidance (OCF - PP&E capex,
                 45-55 bDKK) via an explicit "cash gap" line (WC, cash tax timing, restructuring).

Tags: (facts: ...), (dossier S#), (fj: fundamentals.json), (inputs: 00_inputs.json),
ASSUMPTION = Quant-chosen, attack these first.
Run: python3 reports/runs/NVO_2026-10-13/02_model.py
"""
import json
import pathlib
import statistics as st
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
F = json.loads((RUN / "facts.json").read_text())
INP = json.loads((RUN / "00_inputs.json").read_text())
FJ = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["NVO"]
A, RA, DV = F["annual"], F["researcher_additions"], F["derived"]
YE = F["fiscal_year_ends"]                       # FY2020..FY2025
LBL = [f"FY{y[:4]}" for y in YE]


def ann(key):
    return [A[key][y]["val"] / 1e6 if y in A[key] else None for y in YE]


def add(key):
    return [RA[key][y]["val"] / 1e6 for y in YE]


def hdr(t):
    print("\n" + "=" * 96 + f"\n{t}\n" + "=" * 96)


avg = lambda v: sum(v) / len(v)

# ------------------------------------------------------------------ market inputs
P_USD = INP["price"]                             # inputs: 38.415 (intraday 13:52Z, price of record)
P_USD_CLOSE = FJ["price"]                        # fj: 38.015 close 2026-10-13 (dossier S1)
FX = INP["fx_spot_to_usd"]["DKKUSD"]             # inputs: USD per DKK
P_DKK = P_USD / FX
P_DKK_CLOSE = P_USD_CLOSE / FX
SH = RA["shares"]["outstanding"] / 1e6           # facts add.: 4,413.110m (6-K 0001171843-26-006585)
MCAP = P_DKK * SH
RF_DKK = INP["risk_free_10y"]["DKK"]["value_pct"] / 100   # inputs: 3.01% (OECD monthly, Aug-26)
RF_USD = INP["risk_free_10y"]["USD"]["value_pct"] / 100   # inputs: 5.22%
ERP = INP["equity_risk_premium_pct"] / 100                # inputs: 5.0%
BETA_RAW = FJ["beta"]                                      # fj: 0.384

hdr("0. SNAPSHOT, FX, SHARE COUNT")
print(f"Price of record USD {P_USD} (inputs, intraday) | close USD {P_USD_CLOSE} (fj) | "
      f"DKKUSD {FX:.6f} (inputs)")
print(f"=> DKK per ADR/B share: {P_DKK:.2f} (record) | {P_DKK_CLOSE:.2f} (close); "
      f"dossier S1: B share closed DKK 256.65 on Copenhagen")
print(f"Shares outstanding A+B net of treasury {SH:,.1f}m (facts add.) | market cap DKK {MCAP:,.0f}m "
      f"= USD {MCAP*FX/1e3:,.1f}bn (fj market_cap_usd {FJ['market_cap_usd']/1e9:,.1f}bn at close)")
print(f"fj warnings ({len(FJ['warnings'])}): {FJ['warnings']} | errors: {FJ['errors']}")

# ------------------------------------------------------------------ history
hdr("1. HISTORY: MARGINS, CAPITAL INTENSITY, ROIC (DKK m; facts.json + dossier S2)")
rev, gp, ebit, ni = ann("revenue"), ann("gross_profit"), ann("operating_income"), ann("net_income")
da, sbc, ocf, cpx = ann("d_and_a"), ann("sbc"), ann("ocf"), ann("capex")
cpx_int, acq, inv = ann("capex_intangibles"), ann("acquisitions"), ann("inventory")
cash, gw = ann("cash"), ann("goodwill")
eq, borr, leases, recv = add("equity"), add("borrowings_total"), add("lease_liabilities"), \
    add("trade_receivables")
da_imp = [5753, 6025, 7362, 9413, 19107, 21982]  # dossier S2: D&A + impairment (CF add-back)
etr = [DV[y]["effective_tax_rate"] for y in YE]  # facts derived
gm = [g / r for g, r in zip(gp, rev)]
om = [e / r for e, r in zip(ebit, rev)]
fcf_co = [o - c for o, c in zip(ocf, cpx)]                      # OCF - PP&E capex (company 2026 def)
fcf_fx = [DV[y]["fcf"] / 1e6 for y in YE]                        # facts: OCF - PP&E - intangibles
nopat = [e * (1 - t) for e, t in zip(ebit, etr)]
ic = [e + b - c for e, b, c in zip(eq, borr, cash)]
roic = [n / i for n, i in zip(nopat, ic)]


def row(lab, v, f="{:>10.1%}"):
    print(f"{lab:<34}" + "".join(f.format(x) if x is not None else f"{'UNKNOWN':>10}" for x in v))


print(f"{'':<34}" + "".join(f"{l:>10}" for l in LBL))
row("Revenue", rev, "{:>10,.0f}")
row("YoY revenue", [None] + [rev[i] / rev[i - 1] - 1 for i in range(1, 6)])
row("Gross margin", gm)
row("Operating (EBIT) margin", om)
row("Effective tax rate", etr)
row("Net margin", [n / r for n, r in zip(ni, rev)])
row("PP&E capex / revenue", [c / r for c, r in zip(cpx, rev)])
row("Intangibles purchased / revenue", [c / r for c, r in zip(cpx_int, rev)])
row("Business acquisitions / revenue", [c / r for c, r in zip(acq, rev)])
row("D&A / revenue", [d / r if d else None for d, r in zip(da, rev)])
row("PP&E capex / D&A", [c / d if d else None for c, d in zip(cpx, da)], "{:>10.2f}")
row("SBC / revenue", [s / r for s, r in zip(sbc, rev)], "{:>10.2%}")
row("FCF margin (OCF-PP&E capex)", [f / r for f, r in zip(fcf_co, rev)])
row("FCF margin (facts: OCF-PP&E-intang)", [f / r for f, r in zip(fcf_fx, rev)])
row("Invested capital (eq+borr-cash)", ic, "{:>10,.0f}")
row("ROIC (EBIT x (1-ETR) / IC)", roic)
row("Inventory growth - sales growth", [None] + [DV[y].get("inventory_growth_minus_sales_growth")
                                                 for y in YE[1:]], "{:>+10.1%}")
row("Receivables growth - sales growth", [None] + [(recv[i] / recv[i - 1]) - (rev[i] / rev[i - 1])
                                                   for i in range(1, 6)], "{:>+10.1%}")
for i in (4, 5):
    print(f"  {LBL[i]}: goodwill {gw[i]:,.0f} = {gw[i]/ic[i]:.1%} of IC (< 30%: ROIC ex-goodwill not "
          f"required; ex-goodwill {nopat[i]/(ic[i]-gw[i]):.1%})")
SEMA_Q2 = 31375 + 19484 + 3218   # dossier S8/S3: Ozempic + Wegovy injectable + Wegovy pill, Q2-26
print(f"Semaglutide share of Q2-26 adjusted sales (Rybelsus not broken out, so a floor) = {SEMA_Q2:,} / "
      f"78,488 = {SEMA_Q2/78488:.1%}")
print(f"FY20->FY25 multiples: invested capital x{ic[5]/ic[0]:.2f}, NOPAT x{nopat[5]/nopat[0]:.2f} "
      f"({nopat[0]:,.0f} -> {nopat[5]:,.0f}), revenue x{rev[5]/rev[0]:.2f}")
L5 = slice(1, 6)                                                  # FY2021-FY2025
OM5, GM5 = om[L5], gm[L5]
OM_AVG, OM_LOW, OM_HIGH = avg(OM5), min(OM5), max(OM5)
FCFM_CO_AVG, FCFM_FX_AVG = avg([f / r for f, r in zip(fcf_co[L5], rev[L5])]), \
    avg([f / r for f, r in zip(fcf_fx[L5], rev[L5])])
BD_PCT = st.median([c / r for c, r in zip(cpx_int[1:5], rev[1:5])])   # FY21-24, ex-Akero FY25
print(f"5-yr (FY21-25): EBIT margin avg {OM_AVG:.1%} low {OM_LOW:.1%} high {OM_HIGH:.1%} | GM avg "
      f"{avg(GM5):.1%} low {min(GM5):.1%} | FCF margin avg (OCF-PP&E) {FCFM_CO_AVG:.1%}, "
      f"(facts def) {FCFM_FX_AVG:.1%} | ROIC avg {avg(roic[L5]):.1%}")
print(f"6-yr ROIC series FY20-25: " + ", ".join(f"{r:.0%}" for r in roic))
print(f"Recurring BD/in-licensing allowance = median FY21-24 intangibles/revenue = {BD_PCT:.2%} "
      f"(FY25 Akero {cpx_int[5]:,.0f} excluded as M&A)")
print(f"Gross margin Q2-26 adjusted 78.2% vs Q2-25 82.7% (dossier S3) -> below the 5-yr GM low "
      f"{min(GM5):.1%}")
H1_REC_GROWTH = 88949 / recv[5] - 1                              # facts add. BS 30 Jun 26
H1_INV_GROWTH = 51352 / inv[5] - 1
print(f"H1-26 vs Dec-25: receivables {H1_REC_GROWTH:+.1%}, inventories {H1_INV_GROWTH:+.1%} vs H1 "
      f"adjusted sales +2% CER / reported +13.1% (dossier S2/S3)")

# ------------------------------------------------------------------ adjusted base
hdr("2. ADJUSTED BASE (FY2025) AND FY2026 GUIDANCE TRANSLATION")
R340_25, R340_26, IMP_Q2_26 = 2600, 26760, 6328                  # dossier S2/S3/S10
IMP25 = da_imp[5] - da[5]                                         # 21,982 - 14,666 = 7,316
ADJ_REV25 = rev[5] - R340_25
ADJ_EBIT25 = ebit[5] - R340_25 + IMP25
ADJ_EBITDA25 = ADJ_EBIT25 + da[5]
H1_ADJ_CHECK = 86679 - R340_26 + IMP_Q2_26                        # dossier S2/S3 H1-26 reported EBIT
print(f"Definition check: H1-26 reported EBIT 86,679 - 340B {R340_26:,} + Q2 impairment {IMP_Q2_26:,} "
      f"= {H1_ADJ_CHECK:,} vs company H1-26 adjusted EBIT 66,247 -> "
      f"{'MATCH' if H1_ADJ_CHECK == 66247 else 'MISMATCH'}")
print(f"FY2025 adjusted-equivalent: revenue {rev[5]:,.0f} - {R340_25:,} = {ADJ_REV25:,.0f} | EBIT "
      f"{ebit[5]:,.0f} - {R340_25:,} + impairments {IMP25:,.0f} = {ADJ_EBIT25:,.0f} "
      f"({ADJ_EBIT25/ADJ_REV25:.1%}) | EBITDA {ADJ_EBITDA25:,.0f} (company EBITDA 149,640 incl. 340B)")
print("  (FY2025 transformation costs ~DKK 8bn stay IN the adjusted EBIT: the H1-26 definition does not "
      "remove restructuring.)")
ADJ_NI25_CO = 116407                                               # dossier S2 (company adjusted NP)
ours = (-R340_25 + IMP25) * (1 - etr[5])
unexpl = ADJ_NI25_CO - ni[5] - ours
alt_ebit25 = ADJ_EBIT25 + unexpl / (1 - etr[5])
print(f"FY25 company adjusted NP {ADJ_NI25_CO:,} - reported {ni[5]:,.0f} = {ADJ_NI25_CO-ni[5]:,.0f}; our "
      f"adjustments explain {ours:,.0f} after tax -> {unexpl:,.0f} UNEXPLAINED (likely incl. ~8bn "
      f"transformation costs). If the company's FY25 adjusted EBIT base includes it: {alt_ebit25:,.0f} "
      f"({alt_ebit25/ADJ_REV25:.1%}) -> FY26 BASE guide-implied margin "
      f"{alt_ebit25*0.95/(ADJ_REV25*0.96):.1%} instead of {ADJ_EBIT25*0.95/(ADJ_REV25*0.96):.1%}")
for lab, e25 in (("our base", ADJ_EBIT25), ("alt base", alt_ebit25)):
    fy26, rv26 = e25 * 0.95, ADJ_REV25 * 0.96
    print(f"  implied H2-26 adjusted EBIT margin ({lab}): ({fy26:,.0f} - H1 66,247) / ({rv26:,.0f} - H1 "
          f"148,551) = {(fy26-66247)/(rv26-148551):.1%} vs H1-26 actual 44.6%")
FXS, FXE = -0.01, -0.02                                           # dossier S3: DKK vs CER effect
GUIDE = {"BEAR": (-0.06, -0.06, 45000), "BASE": (-0.03, -0.03, 50000), "BULL": (0.0, 0.0, 55000)}
CAPEX26 = 55000                                                   # dossier S3: "Around 55 bDKK"
DA26_ABS = (13840 - IMP_Q2_26) * 2                                # H1-26 D&A ex-impairment x2 (ASSUMPTION)
BD26_ABS = 854 * 2                                                # H1-26 intangibles x2 (ASSUMPTION)
TAX = {"BEAR": 0.23, "BASE": 0.22, "BULL": 0.21}                  # dossier S3 guide 21-23%
Y1 = {}
for k, (gs, ge, fcf_g) in GUIDE.items():
    r26 = ADJ_REV25 * (1 + gs + FXS)
    e26 = ADJ_EBIT25 * (1 + ge + FXE)
    pre = e26 * (1 - TAX[k]) + DA26_ABS - CAPEX26
    gap = pre - fcf_g
    Y1[k] = dict(g=gs + FXS, rev=r26, m=e26 / r26, gap=gap / r26, da=DA26_ABS / r26,
                 cpx=CAPEX26 / r26, bd=BD26_ABS / r26)
    print(f"{k:<5} FY26 sales {gs:+.0%} CER {gs+FXS:+.0%} DKK -> {r26:,.0f} | adj EBIT {ge+FXE:+.0%} DKK -> "
          f"{e26:,.0f} ({e26/r26:.2%}) | NOPAT@{TAX[k]:.0%} + D&A {DA26_ABS:,} - capex {CAPEX26:,} = "
          f"{pre:,.0f} vs guided FCF {fcf_g:,} -> cash gap {gap:,.0f} ({gap/r26:.2%} of rev)")
print(f"Cross-check FY2025: adj EBIT x (1-ETR {etr[5]:.1%}) + D&A - PP&E capex = "
      f"{ADJ_EBIT25*(1-etr[5]) + da[5] - cpx[5]:,.0f} vs actual OCF - PP&E capex {fcf_co[5]:,.0f}")
print("H2-26 implied company FCF = FY guide 45-55bn - H1 actual 55.3bn = -10.3 to -0.3bn (dossier S2/S3)")

# ------------------------------------------------------------------ bridge
hdr("3. EV -> EQUITY BRIDGE (valuation date 2026-10-13)")
BASE_END, VAL_DATE = date(2025, 12, 31), date(2026, 10, 13)
STUB = (VAL_DATE - BASE_END).days / 365.25
ND_DEC25 = borr[5] - cash[5]                                      # facts add.: 130,958 - 26,464
DIV_FINAL25 = 35312                                               # dossier S2: H1-26 dividends paid
DIV_INT26 = 3.75 * SH                                             # dossier S1: DKK 3.75 interim, Aug-26
BB_2026 = 10558.876422                                            # dossier S5: 6-K, as of 9 Oct 2026
CLAIMS = ND_DEC25 + DIV_FINAL25 + DIV_INT26 + BB_2026
ND_JUN26 = 121794 + 18333 - 44482 - 500                           # dossier S1 / facts add.
ND_OCT_EST = ND_JUN26 + DIV_INT26 + (BB_2026 - 5899)              # ignores Jul-Oct operating cash
print(f"Stub: {BASE_END} -> {VAL_DATE} = {STUB:.4f} yrs (mid-year discounting on)")
print(f"Net debt Dec-25 (borrowings {borr[5]:,.0f} - cash {cash[5]:,.0f}) = {ND_DEC25:,.0f}; "
      f"marketable securities Dec-25 UNKNOWN (500 at Jun-26)")
print(f"+ FY25 final dividend paid 2026 {DIV_FINAL25:,} + 2026 interim (3.75 x {SH:,.1f}m) "
      f"{DIV_INT26:,.0f} + 2026 buybacks to 9 Oct {BB_2026:,.0f}")
print(f"= claims deducted from rolled-forward EV: {CLAIMS:,.0f} ({CLAIMS/SH:.2f} DKK/share)")
print(f"Reconciliation: Jun-26 net debt {ND_JUN26:,} vs Dec-25 ND + H1 distributions "
      f"{ND_DEC25+DIV_FINAL25+5899:,.0f} -> H1-26 cash generated before distributions "
      f"{ND_DEC25+DIV_FINAL25+5899-ND_JUN26:,.0f} (company H1 FCF 55.3bn)")
print(f"Estimated Oct-26 net debt (Jun ND + interim div + Jul-Oct buybacks, no H2 op cash) "
      f"{ND_OCT_EST:,.0f}")
EV_MKT = MCAP + ND_JUN26
EV_MKT_OCT = MCAP + ND_OCT_EST
print(f"Market EV (mcap {MCAP:,.0f} + Jun-26 ND {ND_JUN26:,}) = {EV_MKT:,.0f} DKK m = "
      f"USD {EV_MKT*FX/1e3:,.1f}bn | with Oct-26 ND estimate {EV_MKT_OCT:,.0f}")

# ------------------------------------------------------------------ owner earnings & Lynch
hdr("4. OWNER EARNINGS, LYNCH METRICS, DIVIDEND, DEBT")
OE_FJ = FJ["owner_earnings"] / 1e6
OE_PPE = ni[5] + da[5] - cpx[5]
OE_PPE_IMP = ni[5] + da_imp[5] - cpx[5]
LEASE_PRIN25 = 1503                                               # dossier S2
print(f"Owner earnings (AGENTS.md, fj) = NI {ni[5]:,.0f} + D&A {da[5]:,.0f} - capex incl. Akero "
      f"{-FJ['capex']/1e6:,.0f} = {OE_FJ:,.0f} -> yield {OE_FJ/MCAP:.2%}")
print(f"Owner earnings ex-M&A intangibles = {ni[5]:,.0f} + {da[5]:,.0f} - PP&E {cpx[5]:,.0f} = "
      f"{OE_PPE:,.0f} -> yield {OE_PPE/MCAP:.2%}; less BD allowance {BD_PCT:.2%} x rev = "
      f"{OE_PPE - BD_PCT*rev[5]:,.0f} -> yield {(OE_PPE - BD_PCT*rev[5])/MCAP:.2%}")
print(f"  (adding back impairments too: {OE_PPE_IMP:,.0f}; lease principal {LEASE_PRIN25:,} NOT deducted "
      f"because leases are in net debt)")
print(f"SBC: IFRS 2 expense already inside NI, so OE above is SBC-burdened. FCF-based SBC-adjusted: "
      f"(OCF-PP&E {fcf_co[5]:,.0f} - SBC {sbc[5]:,.0f}) = {fcf_co[5]-sbc[5]:,.0f} -> yield "
      f"{(fcf_co[5]-sbc[5])/MCAP:.2%}")

eps = [A["eps_diluted"][y]["val"] for y in YE]                   # per-share DKK, NOT millions
EPS_CAGR_21_25 = (eps[5] / eps[1]) ** (1 / 4) - 1
EPS_CAGR_20_25_SPLITADJ = (eps[5] / (eps[0] / 2)) ** (1 / 5) - 1   # FY2020 pre 2:1 split (dossier S10.4)
REV_CAGR = F["revenue_cagr"]
CONS_EPS26, CONS_EPS27 = 22.53, 22.09                             # dossier S9, CONSENSUS (yfinance)
CONS_G = (CONS_EPS27 / eps[5]) ** 0.5 - 1
EPS_TTM = RA["ttm_h1_2026"]["diluted_eps_ttm"]                   # 26.20
DIL_SH_H1 = 69546 / 15.66                                         # H1-26 NI / diluted EPS (dossier S2)
EPS_TTM_X340 = EPS_TTM - R340_26 * (1 - TAX["BASE"]) / DIL_SH_H1  # ASSUMPTION: reversal taxed at 22%
EPS_TTM_X340_XIMP = EPS_TTM_X340 + IMP_Q2_26 * (1 - TAX["BASE"]) / DIL_SH_H1
EPS_ADJ25 = 26.17                                                 # dossier S2 (company adjusted)
print(f"\nRevenue CAGR FY20-25 {REV_CAGR:.1%} (facts) | YoY FY25 {rev[5]/rev[4]-1:+.1%}")
print(f"EPS CAGR FY21-25 = (23.03/10.37)^(1/4)-1 = {EPS_CAGR_21_25:.1%} | FY20-25 split-adj "
      f"(FY20 18.01/2) = {EPS_CAGR_20_25_SPLITADJ:.1%} | FY25 EPS YoY {eps[5]/eps[4]-1:+.1%}")
print(f"CONSENSUS EPS FY25->FY27 CAGR = (22.09/23.03)^(1/2)-1 = {CONS_G:+.2%} (dossier S9; labelled)")
print(f"EPS bases: TTM reported {EPS_TTM:.2f} | TTM ex-340B (26,760 x (1-22%) / {DIL_SH_H1:,.0f}m) "
      f"{EPS_TTM_X340:.2f} | also ex-Q2-26 impairment {EPS_TTM_X340_XIMP:.2f} | FY25 reported "
      f"{eps[5]:.2f} | FY25 company-adjusted {EPS_ADJ25:.2f} | CONSENSUS FY26 {CONS_EPS26}")
PE = {"fj trailing (flattered by 340B)": FJ["trailing_pe"],
      "TTM reported": P_DKK / EPS_TTM,
      "TTM ex-340B (normalised, used)": P_DKK / EPS_TTM_X340,
      "TTM ex-340B ex-impairment": P_DKK / EPS_TTM_X340_XIMP,
      "FY25 reported": P_DKK / eps[5],
      "FY25 company-adjusted": P_DKK / EPS_ADJ25,
      "fj forward": FJ["forward_pe"],
      "CONSENSUS FY26 / FY27": (P_DKK / CONS_EPS26, P_DKK / CONS_EPS27)}
for k, v in PE.items():
    print(f"  P/E {k:<34}" + (f"{v:.2f}x" if not isinstance(v, tuple) else f"{v[0]:.2f}x / {v[1]:.2f}x"))
PE_N = P_DKK / EPS_TTM_X340
G_LOWER = min(EPS_CAGR_21_25, CONS_G)
ok, why = peg_is_valid(PE_N, FJ["forward_pe"], G_LOWER)
print(f"PEG gate (P/E {PE_N:.2f}, fwd {FJ['forward_pe']:.2f}, growth = lower of hist {EPS_CAGR_21_25:.1%} / "
      f"consensus {CONS_G:+.2%} = {G_LOWER:+.2%}): {'VALID' if ok else 'VOID'} - {why}")
ok2, why2 = peg_is_valid(PE_N, FJ["forward_pe"], EPS_CAGR_21_25)
print(f"  (historical-only growth would give {'VALID' if ok2 else 'VOID'}: {why2}; not used, rule = lower)")
DPS_TTM = 7.95 + 3.75                                             # dossier S1: final FY25 + interim 26
DY = DPS_TTM / P_DKK
print(f"Dividend yield (DKK 7.95 + 3.75 = {DPS_TTM:.2f} / {P_DKK:.2f}) = {DY:.2%} | ADR vendor rate USD 1.80 / "
      f"{P_USD} = {1.80/P_USD:.2%} [vendor]")
for lab, g in (("lower growth (CONSENSUS)", G_LOWER), ("historical FY21-25, not used", EPS_CAGR_21_25)):
    print(f"Lynch ratio [{lab}] = ({g*100:+.1f} + {DY*100:.2f}) / {PE_N:.2f} = {(g*100+DY*100)/PE_N:.2f}")
NC_PS = -ND_JUN26 / SH
print(f"Net-cash-adj P/E = ({P_DKK:.2f} - ({NC_PS:.2f})) / {EPS_TTM_X340:.2f} = "
      f"{(P_DKK-NC_PS)/EPS_TTM_X340:.2f}x (Jun-26 net debt); with Oct-26 ND estimate "
      f"{(P_DKK+ND_OCT_EST/SH)/EPS_TTM_X340:.2f}x")
DIV_PAID_26 = DIV_FINAL25 + DIV_INT26
print(f"Dividend: FY25 payout 50.7% (company); EPS cover {eps[5]/11.70:.2f}x | FY25 dividends paid "
      f"{A['dividends_paid'][YE[5]]['val']/1e6:,.0f} vs OCF-PP&E {fcf_co[5]:,.0f} = "
      f"{fcf_co[5]/(A['dividends_paid'][YE[5]]['val']/1e6):.2f}x cover; vs company FCF 28,295 = "
      f"{28295/(A['dividends_paid'][YE[5]]['val']/1e6):.2f}x")
print(f"2026: dividends paid {DIV_PAID_26:,.0f} vs guided FCF 45-55bn (mid 50bn) = "
      f"{50000/DIV_PAID_26:.2f}x cover; + DKK 15bn buyback programme -> distributions "
      f"{DIV_PAID_26+15000:,.0f} vs FCF mid 50,000 = shortfall {DIV_PAID_26+15000-50000:,.0f}")
print(f"Debt: Jun-26 ND / owner earnings (ex-M&A) = {ND_JUN26/OE_PPE:.2f}x | vs fj OE {ND_JUN26/OE_FJ:.2f}x | "
      f"ND / FY25 adj EBITDA {ND_JUN26/ADJ_EBITDA25:.2f}x | current borrowings 18,333 vs cash 44,482 "
      f"= {44482/18333:.1f}x | FY25 EBIT / interest {DV[YE[5]]['interest_coverage']:.1f}x | maturity "
      f"ladder UNKNOWN")
print(f"Borrowings path FY21 {borr[1]:,.0f} -> FY25 {borr[5]:,.0f} -> Jun-26 {121794+18333:,} | "
      f"Akero CVR USD 0.5bn contingent = DKK {500/FX:,.0f}m ({500/FX/SH:.2f}/share), not in bridge")

# ------------------------------------------------------------------ multiples matrix
hdr("5. MULTIPLES MATRIX (DKK basis, current; peer medians from dossier S7, vendor values)")
peers = {"LLY": (26.4, 39.0, 24.4, 1.1), "AZN": (13.5, 23.4, 13.8, 2.1), "PFE": (8.4, 37.2, 9.7, 7.8),
         "AMGN": (15.6, 25.6, 16.8, 3.9), "MRK": (14.1, 112.8, 15.3, 4.3)}
pm = lambda k: st.median(v[k] for v in peers.values())
FCF26 = 50000
NORM_CAPEX_FCF = FCF26 + CAPEX26 - (0.06 + BD_PCT) * Y1["BASE"]["rev"]   # capex at steady-state 6% + BD
rows_m = [
    ("EV/EBITDA FY25 adjusted (EV Jun-26 ND)", f"{EV_MKT/ADJ_EBITDA25:.1f}x", f"{pm(0):.1f}x"),
    ("EV/EBITDA FY25 company 149,640", f"{EV_MKT/149640:.1f}x", "-"),
    ("P/E trailing, TTM ex-340B (normalised)", f"{PE_N:.1f}x", f"{pm(1):.1f}x (distorted: MRK/PFE)"),
    ("P/E trailing, fj (flattered)", f"{FJ['trailing_pe']:.1f}x", "-"),
    ("P/E forward (fj)", f"{FJ['forward_pe']:.1f}x", f"{pm(2):.1f}x"),
    ("P/FCF FY25 (OCF-PP&E 58,962)", f"{MCAP/fcf_co[5]:.1f}x", f"{1/(pm(3)/100):.1f}x (1/FCF yld)"),
    ("P/FCF FY25 company FCF 28,295", f"{MCAP/28295:.1f}x", "-"),
    ("P/FCF FY26 guidance mid 50bn", f"{MCAP/FCF26:.1f}x", "-"),
    ("P/FCF SBC-adj (FY26 mid - FY25 SBC)", f"{MCAP/(FCF26-sbc[5]):.1f}x", "-"),
    ("FCF yield FY26 guidance mid", f"{fcf_yield(FCF26, MCAP):.2%}", f"{pm(3):.1f}%"),
    ("FCF yield FY25 (OCF-PP&E)", f"{fcf_yield(fcf_co[5], MCAP):.2%}", "-"),
    ("FCF yield FY26, capex at steady 6%+BD", f"{fcf_yield(NORM_CAPEX_FCF, MCAP):.2%}", "-"),
    ("Owner-earnings yield (fj / ex-M&A)", f"{OE_FJ/MCAP:.2%} / {OE_PPE/MCAP:.2%}", "-"),
    ("PEG", "VOID (not cited)", "-"),
    ("Lynch ratio (lower growth)", f"{(G_LOWER*100+DY*100)/PE_N:.2f}", "-"),
    ("Dividend yield", f"{DY:.2%}", "-"),
]
for r_ in rows_m:
    print(f"{r_[0]:<44}{r_[1]:>20}   peer median: {r_[2]}")
print("5-yr own-average column: UNKNOWN (dossier has no FX-matched historical price series)")

# ------------------------------------------------------------------ discount rate
hdr("6. DISCOUNT RATE (DKK, because cash flows are modelled in DKK)")
BETA = 0.67 * BETA_RAW + 0.33
KE = RF_DKK + BETA * ERP
KD_HIST = A["interest_expense"][YE[5]]["val"] / 1e6 / ((borr[4] + borr[5]) / 2)
KD_PRE = KD_HIST                                                  # ASSUMPTION: FY25 implied, conservative
KD = KD_PRE * (1 - TAX["BASE"])
D_W = 121794 + 18333                                              # gross borrowings Jun-26 (book proxy)
WACC_RAW = (MCAP * KE + D_W * KD) / (MCAP + D_W)
FLOOR = RF_DKK + 0.04
WACC = max(WACC_RAW, FLOOR)
print(f"Beta: vendor raw {BETA_RAW} (fj) -> Blume 0.67 x {BETA_RAW} + 0.33 = {BETA:.3f}")
print(f"Ke = DKK 10y {RF_DKK:.2%} + {BETA:.3f} x ERP {ERP:.0%} = {KE:.2%}")
print(f"Kd pre-tax = FY25 interest expense {A['interest_expense'][YE[5]]['val']/1e6:,.0f} / avg borrowings "
      f"{(borr[4]+borr[5])/2:,.0f} = {KD_HIST:.2%} (tag may include other finance costs; DKK 10y alone "
      f"{RF_DKK:.2%}); after tax @22% = {KD:.2%}")
print(f"Weights: equity {MCAP:,.0f} ({MCAP/(MCAP+D_W):.1%}), debt {D_W:,} ({D_W/(MCAP+D_W):.1%})")
print(f"WACC (CAPM) = {WACC_RAW:.2%}; floor = DKK 10y + 4% = {FLOOR:.2%}; USED = {WACC:.2%} (floor binds)")
print(f"Staleness: DKK 10y is an OECD monthly average for Aug-26 (lags 1-2 months). USD 10y {RF_USD:.2%}. "
      f"USD-name floor would be 8.00%.")

# ------------------------------------------------------------------ scenarios
hdr("7. DCF SCENARIOS (10 yr FY2026-FY2035, FCFF, DKK; mid-year; stub-dated to 2026-10-13)")
N = 10
YRS = list(range(2026, 2036))


def build(g, ebit_m, cpx_pp, bd, da_p, gap, tax, wacc=WACC, tg=0.025, roic=0.20, claims=CLAIMS,
          base=ADJ_REV25, wc=0.0, stub=STUB):
    return dict(base_revenue=base, growth=list(g),
                ebitda_margin=[e + d for e, d in zip(ebit_m, da_p)],
                capex_pct=[c + b + x for c, b, x in zip(cpx_pp, bd, gap)], da_pct=list(da_p),
                tax=tax, wacc=wacc, net_debt=claims, shares=SH, terminal_growth=tg,
                terminal_roic=roic, wc_pct_of_delta_rev=wc, mid_year=True, stub_years=stub)


DA_PATH = lambda y1: [y1, 0.058, 0.064, 0.068] + [0.070] * 6     # ASSUMPTION: 2025-26 capex enters service
BD_PATH = lambda y1: [y1] + [BD_PCT] * 9
SCEN = {
    "BEAR": dict(  # low end of FY26 guide; WAC cut + LOE + Lilly hit FY27 hard; sema LOE in major
                   # markets FY31-32 with weak pipeline offset; margin below the 5-yr low (Q2-26 GM
                   # already below 5-yr low); capex falls slowly
        g=[Y1["BEAR"]["g"], -0.10, -0.04, 0.00, 0.01, -0.08, -0.10, -0.03, 0.00, 0.01],
        ebit_m=[Y1["BEAR"]["m"], 0.37, 0.37, 0.37, 0.37, 0.34, 0.34, 0.34, 0.35, 0.35],
        cpx_pp=[Y1["BEAR"]["cpx"], 0.15, 0.12, 0.09] + [0.07] * 6,
        bd=BD_PATH(Y1["BEAR"]["bd"]), da_p=DA_PATH(Y1["BEAR"]["da"]),
        gap=[Y1["BEAR"]["gap"], 2 * Y1["BEAR"]["gap"]] + [0.0] * 8,
        tax=TAX["BEAR"], tg=0.015, roic=0.12),
    "BASE": dict(  # FY26 guidance midpoint; FY27 WAC cut (-3%); recovery on volume FY28-31;
                   # sema LOE in major markets FY32-33 partly offset by pipeline; EBIT margin ~2pt
                   # below 5-yr avg after the WAC cut, roughly 'broadly stable' vs CMD ambition
        g=[Y1["BASE"]["g"], -0.03, 0.02, 0.03, 0.03, 0.02, -0.01, -0.01, 0.02, 0.025],
        ebit_m=[Y1["BASE"]["m"], 0.40, 0.41, 0.41, 0.41, 0.41, 0.395, 0.395, 0.40, 0.40],
        cpx_pp=[Y1["BASE"]["cpx"], 0.14, 0.10, 0.08] + [0.06] * 6,
        bd=BD_PATH(Y1["BASE"]["bd"]), da_p=DA_PATH(Y1["BASE"]["da"]),
        gap=[Y1["BASE"]["gap"], Y1["BASE"]["gap"]] + [0.0] * 8,
        tax=TAX["BASE"], tg=0.025, roic=0.20),
    "BULL": dict(  # top of FY26 guide; pill + CagriSema + Intl obesity volume (+37% CER Q2) absorb
                   # the WAC cut; mid-single-digit growth FY28-30; margin back to FY23-24 level
                   # (44.2%) on 10% lower headcount; LOE offset by >150bDKK pipeline ambition
        g=[Y1["BULL"]["g"], 0.02, 0.06, 0.06, 0.06, 0.04, 0.01, 0.01, 0.03, 0.03],
        ebit_m=[Y1["BULL"]["m"], 0.42, 0.44, 0.44, 0.44, 0.44, 0.425, 0.425, 0.44, 0.44],
        cpx_pp=[Y1["BULL"]["cpx"], 0.14, 0.10, 0.08] + [0.06] * 6,
        bd=BD_PATH(Y1["BULL"]["bd"]), da_p=DA_PATH(Y1["BULL"]["da"]),
        gap=[Y1["BULL"]["gap"]] + [0.0] * 9,
        tax=TAX["BULL"], tg=0.030, roic=0.30),
}
RES = {}
for name, p in SCEN.items():
    kw = build(**p)
    r = dcf(**kw)
    RES[name] = (r, kw)
    rv10 = r.rows[-1][1]
    print(f"\n[{name} inputs] growth: " + " ".join(f"{x:+.1%}" for x in p["g"]))
    print(f"  EBIT margin: " + " ".join(f"{x:.1%}" for x in p["ebit_m"]))
    print(f"  PP&E capex%: " + " ".join(f"{x:.1%}" for x in p["cpx_pp"]))
    print(f"  BD%:         " + " ".join(f"{x:.2%}" for x in p["bd"]))
    print(f"  D&A%:        " + " ".join(f"{x:.1%}" for x in p["da_p"]))
    print(f"  cash gap%:   " + " ".join(f"{x:.2%}" for x in p["gap"]))
    nopat_m = p["ebit_m"][-1] * (1 - p["tax"])
    print(f"  terminal: NOPAT margin {nopat_m:.1%}; reinvestment g/ROIC = {p['tg']/p['roic']:.1%} of NOPAT "
          f"= {nopat_m*p['tg']/p['roic']:.1%} of revenue -> implied gross capex+dWC = D&A "
          f"{p['da_p'][-1]:.1%} + {nopat_m*p['tg']/p['roic']:.1%} = {p['da_p'][-1]+nopat_m*p['tg']/p['roic']:.1%} "
          f"of revenue (explicit FY35 capex+BD {p['cpx_pp'][-1]+p['bd'][-1]:.2%})")
    print(f"\n--- {name}: WACC {kw['wacc']:.2%} | g_T {kw['terminal_growth']:.1%} | ROIC_T "
          f"{kw['terminal_roic']:.0%} | tax {kw['tax']:.0%} | BD {BD_PCT:.2%} | 10-yr rev CAGR "
          f"{(rv10/ADJ_REV25)**0.1-1:+.2%} | FY35 rev {rv10:,.0f}")
    print(f"{'FY':<6}{'g':>7}{'Revenue':>10}{'EBIT%':>7}{'EBITDA':>9}{'EBIT':>9}{'D&A':>8}"
          f"{'Cpx+BD+gap':>11}{'FCF':>9}{'FCF%':>7}{'PV':>9}")
    for (y, rv, eb, ei, d_, cx, fcf, pv), gg, em in zip(r.rows, p["g"], p["ebit_m"]):
        print(f"{YRS[y-1]:<6}{gg:>+7.1%}{rv:>10,.0f}{em:>7.1%}{eb:>9,.0f}{ei:>9,.0f}{d_:>8,.0f}{cx:>11,.0f}"
              f"{fcf:>9,.0f}{fcf/rv:>7.1%}{pv:>9,.0f}")
    flag = "  <-- TV > 75% OF EV: FLAG" if r.terminal_share > 0.75 else ""
    print(f"PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} ({r.terminal_share:.0%} of EV)"
          f"{flag}")
    print(f"EV {r.enterprise_value:,.0f} - claims {CLAIMS:,.0f} = equity {r.equity_value:,.0f} -> DKK "
          f"{r.per_share:,.1f}/share = USD {r.per_share*FX:,.2f}/ADR vs USD {P_USD} ({r.upside(P_DKK):+.1%}); "
          f"vs close {P_USD_CLOSE}: {r.per_share/P_DKK_CLOSE-1:+.1%}")
b0 = RES["BASE"][0]
print(f"\nFCF-margin anchor: BASE FY30-35 FCF margin "
      f"{avg([x[6]/x[1] for x in b0.rows[4:]]):.1%} vs 5-yr avg {FCFM_CO_AVG:.1%} (OCF-PP&E) / "
      f"{FCFM_FX_AVG:.1%} (facts def, incl. Akero)")
print(f"BASE terminal-year FCF margin implied by g/ROIC: "
      f"{b0.rows[-1][3]*(1-TAX['BASE'])*(1-0.025/0.20)/b0.rows[-1][1]:.1%} of FY35 revenue")
print(f"BASE FY2027 revenue {b0.rows[1][1]:,.0f} vs CONSENSUS FY2027 304,688 (dossier S9; comparison "
      f"only, not an input): {b0.rows[1][1]/304688-1:+.1%}")

# ------------------------------------------------------------------ reverse DCF
hdr("8. REVERSE DCF (what must be true at USD 38.415 = DKK %.2f)" % P_DKK)
bk = RES["BASE"][1]
strip = lambda kw: {k: v for k, v in kw.items() if k not in ("base_revenue", "growth")}
g_imp = reverse_dcf(price=P_DKK, base_revenue=ADJ_REV25, years=N, **strip(bk))
g_imp_c = reverse_dcf(price=P_DKK_CLOSE, base_revenue=ADJ_REV25, years=N, **strip(bk))
print(f"BASE margins/capex, WACC {WACC:.2%}, g 2.5%, ROIC 20%: implied constant 10-yr revenue CAGR "
      f"{g_imp:+.2%} (FY35 revenue {ADJ_REV25*(1+g_imp)**10:,.0f}); at close price {g_imp_c:+.2%}")
for nm in ("BEAR", "BULL"):
    gi = reverse_dcf(price=P_DKK, base_revenue=ADJ_REV25, years=N, **strip(RES[nm][1]))
    print(f"  at {nm} margins/capex/terminal: implied CAGR {gi:+.2%}")
g_imp8 = reverse_dcf(price=P_DKK, base_revenue=ADJ_REV25, years=N, **{**strip(bk), "wacc": 0.08})
print(f"  BASE operating inputs at WACC 8.00% (USD-name floor): implied CAGR {g_imp8:+.2%}")
# implied steady-state EBIT margin (FY27+) at BASE growth
lo, hi = 0.15, 0.60
for _ in range(60):
    mm = (lo + hi) / 2
    em = [SCEN["BASE"]["ebit_m"][0]] + [mm] * 9
    v = dcf(**build(**{**SCEN["BASE"], "ebit_m": em})).per_share
    lo, hi = (mm, hi) if v < P_DKK else (lo, mm)
print(f"At BASE growth path: price implies flat FY27-35 EBIT margin {mm:.2%} (5-yr avg {OM_AVG:.1%}, "
      f"low {OM_LOW:.1%}; FY26 guide-implied {Y1['BASE']['m']:.1%})")
lo, hi = 0.03, 0.20
for _ in range(60):
    w = (lo + hi) / 2
    v = dcf(**build(**{**SCEN["BASE"], "wacc": w})).per_share
    lo, hi = (w, hi) if v > P_DKK else (lo, w)
print(f"BASE operating case: price implies a discount rate (IRR) of {w:.2%}")
# terminal-only check: what does the price say about value beyond FY2035?
pv_exp_ps = (b0.pv_explicit - CLAIMS) / SH
print(f"BASE PV of FY26-35 explicit FCF less claims = DKK {pv_exp_ps:,.1f}/share; price needs "
      f"DKK {P_DKK - pv_exp_ps:,.1f}/share ({(P_DKK-pv_exp_ps)/P_DKK:.0%} of price) from the terminal "
      f"(BASE TV gives {b0.pv_terminal/SH:,.1f})")

# ------------------------------------------------------------------ sensitivity grid
hdr("9. SENSITIVITY (BASE): WACC x terminal growth, DKK/share (USD/ADR in brackets)")
waccs = [round(WACC + d, 4) for d in (-0.01, -0.005, 0, 0.005, 0.01)]
tgs = [0.015, 0.020, 0.025, 0.030, 0.035]
grid = sensitivity({"wacc": waccs}, {"terminal_growth": tgs}, **bk)
print(f"{'WACC / g':<10}" + "".join(f"{g:>16.1%}" for g in tgs) + "   (g 3.5% > DKK 10y cap 3.01%)")
for wv, rw in zip(waccs, grid):
    print(f"{wv:<10.2%}" + "".join(f"{v:>8,.0f} ({v*FX:>5.2f})" for v in rw))
print("\nBASE: WACC x terminal ROIC (g 2.5%), DKK/share")
rocs = [0.12, 0.15, 0.20, 0.25, 0.30]
grid2 = sensitivity({"wacc": waccs}, {"terminal_roic": rocs}, **bk)
print(f"{'WACC/ROIC':<10}" + "".join(f"{x:>9.0%}" for x in rocs))
for wv, rw in zip(waccs, grid2):
    print(f"{wv:<10.2%}" + "".join(f"{v:>9,.0f}" for v in rw))
print("\nBASE: flat FY27-35 EBIT margin x WACC, DKK/share")
ms = [0.34, 0.37, OM_LOW, OM_AVG, 0.442]
print(f"{'WACC/EBIT%':<10}" + "".join(f"{x:>9.1%}" for x in ms))
for wv in waccs:
    vals = [dcf(**build(**{**SCEN["BASE"], "ebit_m": [SCEN["BASE"]["ebit_m"][0]] + [x] * 9,
                           "wacc": wv})).per_share for x in ms]
    print(f"{wv:<10.2%}" + "".join(f"{v:>9,.0f}" for v in vals))

# ------------------------------------------------------------------ load-bearing +/-10%
hdr("10. LOAD-BEARING INPUTS: +/-10% (relative, one at a time) on BASE, DKK/share")
BS = SCEN["BASE"]
base_ps = b0.per_share


def run(**over):
    return dcf(**build(**{**BS, **over})).per_share


def da_fixed_ebitda(f):
    da2 = [d * f for d in BS["da_p"]]
    return run(da_p=da2, ebit_m=[e - (d2 - d) for e, d, d2 in zip(BS["ebit_m"], BS["da_p"], da2)])


tests = {
    "EBIT margin, all years": lambda f: run(ebit_m=[m * f for m in BS["ebit_m"]]),
    "WACC (7.01%)": lambda f: run(wacc=WACC * f),
    "FY27+ revenue level (WAC-cut yr)": lambda f: run(g=[BS["g"][0], (1 + BS["g"][1]) * f - 1] + BS["g"][2:]),
    "Terminal growth (2.5%)": lambda f: run(tg=0.025 * f),
    "Tax rate (22%)": lambda f: run(tax=TAX["BASE"] * f),
    "Terminal ROIC (20%)": lambda f: run(roic=0.20 * f),
    "PP&E capex / revenue": lambda f: run(cpx_pp=[c * f for c in BS["cpx_pp"]]),
    "Claims (ND Dec-25 + 2026 distrib.)": lambda f: run(claims=CLAIMS * f),
    "D&A / revenue (EBITDA fixed)": da_fixed_ebitda,
    "BD/in-licensing allowance": lambda f: run(bd=[b * f for b in BS["bd"]]),
    "FY26-27 cash gap": lambda f: run(gap=[x * f for x in BS["gap"]]),
}
out = []
for k, fn in tests.items():
    lo_v, hi_v = fn(0.9), fn(1.1)
    out.append((abs(hi_v - lo_v), k, lo_v, hi_v))
print(f"BASE = DKK {base_ps:,.1f}/share = USD {base_ps*FX:,.2f}/ADR")
print(f"{'Input':<38}{'-10%':>9}{'+10%':>9}{'swing':>8}{'-10% USD':>10}{'+10% USD':>10}")
for sw, k, lo_v, hi_v in sorted(out, reverse=True):
    print(f"{k:<38}{lo_v:>9,.1f}{hi_v:>9,.1f}{sw:>8,.1f}{lo_v*FX:>10.2f}{hi_v*FX:>10.2f}")
print(f"{'DKKUSD FX (USD value only)':<38}{base_ps*FX*0.9:>27.2f}{base_ps*FX*1.1:>10.2f}  "
      f"(DKK value unchanged)")
g_dn = run(g=[BS["g"][0]] + [x - 0.01 for x in BS["g"][1:]])
g_up = run(g=[BS["g"][0]] + [x + 0.01 for x in BS["g"][1:]])
print(f"Revenue growth FY27-35 -1pt / +1pt (absolute, not 10%): {g_dn:,.1f} / {g_up:,.1f}")

# ------------------------------------------------------------------ stress tests
hdr("11. STRESS TESTS ON BASE (one change each)")
G = BS["g"]
loe = {
    "No major-market LOE in horizon (FY32-33 at +2.5%)": G[:6] + [0.025, 0.025] + G[8:],
    "LOE early: FY30-31 -1%/-1%, FY32-33 +2%": G[:4] + [-0.01, -0.01, 0.02, 0.02] + G[8:],
    "LOE base timing FY32-33 -1%/-1% (BASE)": G,
    "LOE late: FY34-35 -1%/-1%": G[:6] + [0.025, 0.025, -0.01, -0.01],
    "Deep LOE FY32-33 -18%/-18%, no pipeline offset": G[:6] + [-0.18, -0.18] + G[8:],
}
for k, gpath in loe.items():
    v = run(g=gpath)
    print(f"{k:<52} DKK {v:>7,.1f}  USD {v*FX:>6.2f}  ({v/P_DKK-1:+.0%})")
SALES_DED = 140201                                                 # dossier S2: Jun-26 current provision
for pct in (0.10, 0.25, 0.50):
    hit = SALES_DED * pct * (1 - 0) / (1 + WACC) ** 1.5 * (1 + WACC) ** STUB / SH   # FY27 mid-year
    print(f"WAC-cut cash unwind: {pct:.0%} of sales-deduction provision ({SALES_DED*pct:,.0f}) paid out in "
          f"FY27 (pre-tax, no offset): -{hit:.1f} DKK/share -> {base_ps-hit:,.1f} (USD {(base_ps-hit)*FX:.2f})")
v8 = run(wacc=0.08)
print(f"WACC 8.00% (USD-name floor instead of DKK floor): DKK {v8:,.1f} (USD {v8*FX:.2f})")
for bp in (-0.005, 0.005):
    v = run(wacc=FLOOR + bp)
    print(f"DKK 10y {RF_DKK+bp:.2%} (stale input {bp*1e4:+.0f}bp) -> floor {FLOOR+bp:.2%}: DKK {v:,.1f} "
          f"(USD {v*FX:.2f})")
for cp in (0.045, 0.09):
    v = run(cpx_pp=BS["cpx_pp"][:4] + [cp] * 6)
    print(f"Steady-state PP&E capex FY30-35 {cp:.1%} instead of 6.0% (FY20-21 level 4.5%; FY22-23 avg 9.0%): "
          f"DKK {v:,.1f} (USD {v*FX:.2f})")
v = run(cpx_pp=[BS["cpx_pp"][0]] + [0.14, 0.14, 0.12] + [0.09] * 6)
print(f"Capex stays high (FY27-28 14%, FY29 12%, FY30-35 9%): DKK {v:,.1f} (USD {v*FX:.2f})")
print(f"Leases outside Borrowings (+8,572 Dec-25 leases to claims): {run(claims=CLAIMS+8572):,.1f} "
      f"({-8572/SH:+.2f})")
print(f"Akero CVR USD 0.5bn paid: {run(claims=CLAIMS+500/FX):,.1f} ({-500/FX/SH:+.2f})")
bear_lite = dcf(**build(**{**SCEN["BEAR"], "ebit_m": [SCEN["BEAR"]["ebit_m"][0]] + [OM_LOW] * 9})).per_share
print(f"BEAR growth with EBIT margin held at the 5-yr low {OM_LOW:.1%} (instead of 34-37%): DKK "
      f"{bear_lite:,.1f} (USD {bear_lite*FX:.2f})")
base_flatm = run(ebit_m=[BS["ebit_m"][0]] + [Y1["BASE"]["m"]] * 9)
print(f"BASE growth with CMD 'broadly stable margin' taken literally ({Y1['BASE']['m']:.1%} flat): DKK "
      f"{base_flatm:,.1f} (USD {base_flatm*FX:.2f})")
print(f"Price check: USD {P_USD} (record) vs {P_USD_CLOSE} (close): base upside "
      f"{base_ps/P_DKK-1:+.1%} vs {base_ps/P_DKK_CLOSE-1:+.1%}")

# ------------------------------------------------------------------ EPV cross-check
hdr("12. EARNINGS-POWER CROSS-CHECK (no growth, maintenance capex = D&A; Oct-26 ND estimate)")
for lab, rv in (("FY26 BASE revenue", Y1["BASE"]["rev"]), ("FY27 BASE revenue", b0.rows[1][1])):
    for m_ in (0.34, 0.37, 0.40, Y1["BASE"]["m"]):
        epv = rv * m_ * (1 - TAX["BASE"]) / WACC
        ps = (epv - ND_OCT_EST) / SH
        print(f"{lab} {rv:,.0f} x EBIT {m_:.1%} x (1-22%) / {WACC:.2%} = EPV {epv:,.0f} -> DKK {ps:,.1f} "
              f"(USD {ps*FX:.2f})")

# ------------------------------------------------------------------ summary
hdr("13. SUMMARY")
for nm in ("BEAR", "BASE", "BULL"):
    r = RES[nm][0]
    print(f"{nm:<5} DKK {r.per_share:>7,.1f}/share  USD {r.per_share*FX:>6.2f}/ADR  "
          f"({r.upside(P_DKK):+.1%} vs USD {P_USD})  TV {r.terminal_share:.0%} of EV")
print(f"Reverse DCF implied 10-yr revenue CAGR (BASE margins): {g_imp:+.2%}; implied flat EBIT margin at "
      f"BASE growth: {mm:.1%}; implied IRR at BASE: {w:.2%}")
print(f"FY2035 revenue BULL / BEAR = {RES['BULL'][0].rows[-1][1]:,.0f} / {RES['BEAR'][0].rows[-1][1]:,.0f} = "
      f"{RES['BULL'][0].rows[-1][1]/RES['BEAR'][0].rows[-1][1]:.2f}x")
print(f"ROIC FY25 {roic[5]:.1%} (adj-equiv {ADJ_EBIT25*(1-etr[5])/ic[5]:.1%}) vs WACC {WACC:.2%}")
