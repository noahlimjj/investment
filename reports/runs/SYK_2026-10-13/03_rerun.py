"""03_rerun.py -- SKEPTIC RE-RUN of 02_model.py (SYK, as of 2026-10-13). Generated 2026-10-14.
Identical to 02_model.py except the lines tagged '# SKEPTIC-CORRECTION' plus the appended SKEPTIC section.
Corrections (see 03_skeptic.md s2):
  C1 PRICE 283.71 -> 282.55: the dossier's '2026-10-13 close' was an intraday pull (02:44 SGT = 18:44 UTC, before
     the 20:00 UTC close). Final raw close $282.55 (yfinance auto_adjust=False, bar re-pulled 2026-10-13 23:09 UTC).
  C2 BEAR tax 27.6% -> 21.4%. The TTM 27.6% contains a one-off, non-cash charge: FY25 10-K (accn 0000310764-26-000010)
     MD&A: 'The effective income tax rate for 2025 increased from 2024 due to the 2025 tax effect of transfers of
     intellectual property between tax jurisdictions'; rate reconciliation 'disposition of assets' +$405M (+9.0pt);
     deferred tax expense +$392M (current tax $876M vs $869M FY24). H1-26 ETR 16.3% (10-Q accn 0000310764-26-000050).
     Bear now uses the highest evidenced recurring rate: FY25 cash taxes paid $1,002M / pretax ex-impairment
     ($4,514M + $170M) = 21.4%. Bear terminal ROIC recomputed at that rate.
"""
"""SYK (Stryker) Quant model, as of 2026-10-13. USD millions unless stated.

Sources (cited inline):
  facts   = reports/runs/SYK_2026-10-13/facts.json (SEC XBRL via sec_facts.py; accns inside). Loaded and
            asserted below, so a hard-coded figure that drifts from facts.json fails loudly.
  fund    = data/fundamentals.json (validated yfinance layer; SYK warnings [] errors [])
  dossier = reports/runs/SYK_2026-10-13/01_research.md, section in brackets
  inputs  = reports/runs/SYK_2026-10-13/00_inputs.json (risk-free, ERP, discount-rate floor)

Basis decisions (each stated once, applied everywhere):
  D&A     Cash-flow-statement basis = depreciation + amortisation of intangibles (FY25 461 + 732 = 1,193 = fund
          d_and_a). NOT the segment-note/XBRL tag (FY25 1,570). The ~377 gap is inferred loaner-instrument
          amortisation [dossier s2; orchestrator note]. It is left INSIDE operating expense as the proxy for the
          instrument-set cash spend, which sits in OCF. Adding it back without the spend would overstate cash.
  EBITDA  GAAP operating income + goodwill & other impairments (non-cash) + cash-flow D&A. SBC stays expensed.
  SBC     DEDUCTED (inside GAAP operating income, never added back). Share count held FLAT at diluted 386.0M.
          One method, not both, not neither.
  Leases  US-GAAP filer: operating-lease cost (205 FY25) is inside EBITDA, so lease liabilities (501) stay OUT of
          net debt. (IFRS-16 rule n/a.)
  AcqAmort acq_amort_pct = FY25 amortisation of intangibles / revenue, passed to dcf(); D&A held flat, NO fade.
  Timing  Base period = TTM to 2026-06-30. mid_year=True. stub_years = 105 days to the 2026-10-13 price.
          The Q2-26 dividend ($0.88) declared in the base period is deducted in the equity bridge.
  WC      'w' = net working-capital + other operating reinvestment per $ of organic revenue growth, CALIBRATED so the
          model reproduces the FY21-25 SBC-adjusted unlevered FCF (payables are not in facts.json, so it cannot be
          built bottom-up).
No probabilities, no verdict (Skeptic's job).
"""
import json, pathlib, statistics as st, sys
from datetime import date

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

facts = json.load(open(HERE / "facts.json"))
inputs = json.load(open(HERE / "00_inputs.json"))
_f = json.load(open(ROOT / "data" / "fundamentals.json"))["records"]
fund = _f["SYK"] if isinstance(_f, dict) else next(r for r in _f if r["ticker"] == "SYK")
assert not fund["errors"], "fundamentals.json errors -> BLOCKED"
FYE = facts["fiscal_year_ends"]
YRS = ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25"]


def fa(k):
    return [facts["annual"][k][d]["val"] / 1e6 for d in FYE]


def tt(k):
    return facts["ttm"][k]["val"] / 1e6


# ---------------- facts.json annual (USD M) ----------------
REV, GP, OPINC = fa("revenue"), fa("gross_profit"), fa("operating_income")
PRETAX, TAXX, NI, INT = fa("pretax_income"), fa("income_tax"), fa("net_income"), fa("interest_expense")
DA_SEG, SBC, OCF, CAPEX = fa("d_and_a"), fa("sbc"), fa("ocf"), fa("capex")
ACQ, DIVS, CASH, STI = fa("acquisitions"), fa("dividends_paid"), fa("cash"), fa("short_term_investments")
DEBT = [a + b for a, b in zip(fa("debt_current"), fa("debt_noncurrent"))]
GW, INV, AR, TA = fa("goodwill"), fa("inventory"), fa("receivables"), fa("total_assets")
DIL = fa("diluted_shares")
EPS = [facts["annual"]["eps_diluted"][d]["val"] for d in FYE]
EQUITY = [None] + [facts["researcher_notes"]["equity_item6"][y] for y in ("2021", "2022", "2023", "2024", "2025")]
# ---------------- dossier-only annual series ----------------
DEP_CF = [340, 371, 371, 393, 427, 461]          # dossier s2, cash-flow statement depreciation
AMORT_CF = [472, 619, 627, 635, 623, 732]        # dossier s2, cash-flow statement amortisation of intangibles
IMP = [None, 264, 270, 36, 977, 170]             # dossier s5, goodwill & other impairments (10-K Item 6); FY20 UNKNOWN
ORG = [-0.048, 0.126, 0.097, 0.115, 0.102, 0.103]  # dossier s5 / facts researcher_notes, organic cc growth
ADJ_EPS = {"FY23": 10.60, "FY24": 12.19, "FY25": 13.63}  # dossier s2 (company non-GAAP)
DPS_DECL = {"2021": 2.585, "2022": 2.835, "2023": 3.050, "2024": 3.240, "2025": 3.400}  # dossier s5
DA_CF = [a + b for a, b in zip(DEP_CF, AMORT_CF)]
assert abs(DA_CF[5] - fund["d_and_a"] / 1e6) < 0.5, "CF-basis D&A must equal fund d_and_a"
assert REV == [14351, 17108, 18449, 20498, 22595, 25116] and DEBT[5] == 15859 and CAPEX[5] == 761
# ---------------- TTM to 2026-06-30 (facts ttm) and 6/30/26 balance sheet (dossier s1/s2) ----------------
T_REV, T_GP, T_OI, T_PRETAX, T_TAX = tt("revenue"), tt("gross_profit"), tt("operating_income"), tt("pretax_income"), tt("income_tax")
T_NI, T_INT, T_DA_SEG, T_SBC, T_OCF, T_CAPEX = tt("net_income"), tt("interest_expense"), tt("d_and_a"), tt("sbc"), tt("ocf"), tt("capex")
T_DIVS, T_ACQ = tt("dividends_paid"), tt("acquisitions")
DEBT_J26, CASH_J26, MKTSEC_J26, EQ_J26 = 14942, 3391, 85, 23988   # dossier s1 / s2 (10-Q Q2-26)
INV_J26, AR_J26 = 5521, 3743                                       # dossier s2
LEASES_FY25 = 153 + 348                                            # dossier s5 (excluded from net debt; see header)
SH_OUT = facts["shares_outstanding_latest"]["val"] / 1e6           # 383.573 (10-Q cover)
SH_DIL = 386.0                                                     # dossier s1, Q2-26 diluted weighted
PRICE = 282.55  # SKEPTIC-CORRECTION C1: final 2026-10-13 raw close (dossier 283.71 was intraday)
PRICE_INPUTS = inputs["price"]                                     # 282.70 intraday (00_inputs.json)
MCAP = PRICE * SH_OUT
NET_DEBT = DEBT_J26 - CASH_J26 - MKTSEC_J26                        # 11,466 (ex leases)
AVS_CONTINGENT, PROD_LIAB = 271, 144     # dossier s5 (10-Q Note 7 FV) / s8 (10-K accrual): debt-like
DIV_Q, DIV_DECLARED_UNPAID = 0.88, 0.88 * SH_OUT   # dossier s5: quarterly $0.88; Q2 declared in base period
BRIDGE = NET_DEBT + AVS_CONTINGENT + PROD_LIAB + DIV_DECLARED_UNPAID
EV = MCAP + NET_DEBT
# ---------------- guidance / consensus / peers ----------------
GUIDE_ORG = (0.083, 0.093)                    # dossier s3 verbatim FY26 organic
GUIDE_ADJ_EPS = (14.95, 15.10)                # dossier s3
H1_26_ORG, Q2_26_ORG, Q1_26_ORG = 0.058, 0.090, 0.024   # dossier s3
CONS_EPS26, CONS_EPS27 = 14.97, 16.69         # dossier s9 CONSENSUS (labelled; PEG gate only, never fair value)
PEERS = {  # dossier s7: EV/EBITDA, trailing P/E, fwd P/E, FCF yield %   (vendor, TTM)
    "BSX": (13.3, 17.7, 12.9, 3.87), "MDT": (13.2, 22.7, 14.4, 4.58), "ABT": (17.5, 33.2, 17.0, 4.05),
    "ZBH": (9.8, 22.6, 10.3, 6.05), "ISRG": (34.9, 48.6, 35.0, 1.75), "EW": (23.2, 51.1, 25.4, 2.49)}
SYK_VENDOR = (16.3, 29.4, 17.0, 3.77)
MATURITIES = {"2026": 1000, "2027": 1382, "2028": 2606, "2029": 1691, "2030": 2565, "after": 6729}  # dossier s5
REVOLVER_AVAIL = 2910                                                                                  # dossier s5
RF = inputs["risk_free_10y"]["USD"]["value_pct"] / 100
ERP = inputs["equity_risk_premium_pct"] / 100
FLOOR = inputs["discount_rate_floor"]["USD"] / 100
BETA_RAW = fund["beta"]


def pct(x, d=1):
    return f"{x*100:.{d}f}%"


def line(t):
    print("\n" + "=" * 10 + " " + t + " " + "=" * 10)


cagr = lambda a, b, n: (b / a) ** (1 / n) - 1
I5 = range(1, 6)  # FY21..FY25 = the 5-yr window

# =====================================================================================
line("0. TAPE / RECONCILIATION")
print(f"Price ${PRICE} (dossier s1 close) | 00_inputs ${PRICE_INPUTS} | fund ${fund['price']} | "
      f"shares out {SH_OUT:.3f}M, diluted {SH_DIL}M | mcap {MCAP:,.0f}")
print(f"Net debt (ex leases) {DEBT_J26:,} - {CASH_J26:,} - {MKTSEC_J26} = {NET_DEBT:,} | EV {EV:,.0f} | "
      f"equity bridge adds AVS contingent {AVS_CONTINGENT} + product liability {PROD_LIAB} + declared Q2 div "
      f"{DIV_DECLARED_UNPAID:,.1f} = {BRIDGE:,.1f}")
print(f"TTM GAAP diluted EPS (NI/diluted) {T_NI/SH_DIL:.2f} -> P/E {PRICE/(T_NI/SH_DIL):.1f}x | fund trailing P/E "
      f"{fund['trailing_pe']:.2f} | 12m price change -22.3% (dossier s1) | fund warnings {fund['warnings']}")

# =====================================================================================
line("A. LYNCH: growth, category checks")
eps_ttm = T_NI / SH_DIL
print(f"Revenue CAGR FY20-25 {pct(cagr(REV[0], REV[5], 5))} (facts revenue_cagr {pct(facts['revenue_cagr'])}) | "
      f"FY21-25 {pct(cagr(REV[1], REV[5], 4))}")
print("Revenue y/y: " + " ".join(f"{YRS[i]} {pct(REV[i]/REV[i-1]-1)}" for i in I5) +
      f" | TTM vs FY25 base n/a")
print("Organic cc growth: " + " ".join(f"{YRS[i]} {pct(ORG[i])}" for i in range(6)) +
      f" | FY21-25 mean {pct(st.mean(ORG[1:]))} | H1-26 {pct(H1_26_ORG)} (Q1 {pct(Q1_26_ORG)} cyber, Q2 {pct(Q2_26_ORG)})")
g_eps5 = cagr(EPS[0], EPS[5], 5)
print(f"GAAP diluted EPS {EPS} | CAGR FY20-25 {pct(g_eps5)} (FY20 = COVID base) | FY21-25 "
      f"{pct(cagr(EPS[1], EPS[5], 4))} | adj EPS FY23-25 CAGR {pct(cagr(ADJ_EPS['FY23'], ADJ_EPS['FY25'], 2))}")
print(f"FY26 guide adj EPS {GUIDE_ADJ_EPS} -> growth vs FY25 adj {pct(GUIDE_ADJ_EPS[0]/ADJ_EPS['FY25']-1)} to "
      f"{pct(GUIDE_ADJ_EPS[1]/ADJ_EPS['FY25']-1)} | CONSENSUS FY27/FY26 {pct(CONS_EPS27/CONS_EPS26-1)}")
print("Inventory / receivables growth vs sales growth (pp; facts derived inventory_growth_minus_sales_growth):")
for i in I5:
    sg, ig, ag = REV[i]/REV[i-1]-1, INV[i]/INV[i-1]-1, AR[i]/AR[i-1]-1
    print(f"  {YRS[i]}: sales {pct(sg):>6} inv {pct(ig):>6} ({(ig-sg)*100:+5.1f}pp)  AR {pct(ag):>6} ({(ag-sg)*100:+5.1f}pp)"
          f"  DSI {INV[i]/(REV[i]-GP[i])*365:4.0f}d  DSO {AR[i]/REV[i]*365:3.0f}d"
          + ("  <-- INV FLAG" if ig - sg > 0.05 else "") + ("  <-- AR FLAG" if ag - sg > 0.05 else ""))
print(f"  H1-26 (6/30/26 vs 12/31/25): inventory {pct(INV_J26/INV[5]-1)}, receivables {pct(AR_J26/AR[5]-1)}, "
      f"H1 sales +6.1% y/y (dossier s3); TTM DSI {INV_J26/(T_REV-T_GP)*365:.0f}d, DSO {AR_J26/T_REV*365:.0f}d")
# dividends (slow-grower check, informational)
dps_cagr = cagr(DPS_DECL["2021"], DPS_DECL["2025"], 4)
print(f"Dividend declared/share 2021-25 {list(DPS_DECL.values())} CAGR {pct(dps_cagr)} | 2026 run-rate "
      f"{4*DIV_Q:.2f} -> yield {pct(4*DIV_Q/PRICE, 2)} | payout FY25 NI {pct(DIVS[5]/NI[5])} FCF "
      f"{pct(DIVS[5]/(OCF[5]-CAPEX[5]))} | TTM NI {pct(T_DIVS/T_NI)} FCF {pct(T_DIVS/(T_OCF-T_CAPEX))}")
# funding of growth
cum_fcf = sum(OCF[i] - CAPEX[i] for i in range(6))
print(f"FY20-25 cumulative: FCF {cum_fcf:,.0f} | dividends {sum(DIVS):,.0f} | acquisitions {sum(ACQ):,.0f} | buybacks 0 | "
      f"shortfall {sum(DIVS)+sum(ACQ)-cum_fcf:,.0f} | debt {DEBT[0]:,.0f}->{DEBT[5]:,.0f}, cash+STI "
      f"{CASH[0]+STI[0]:,.0f}->{CASH[5]+STI[5]:,.0f}")
print(f"Acquisitions / cumulative FCF FY20-25 = {sum(ACQ)/cum_fcf:.1%}")
# acquisition return test (crude, dossier s5 derived acquired revenue)
acq_rev = {"FY21": 790, "FY22": 222, "FY23": 18, "FY24": 100, "FY25 (Vascular upper bound)": 661}
ebita_m25 = (OPINC[5] + IMP[5] + AMORT_CF[5]) / REV[5]
print(f"Acquisition test: first-year acquired revenue (dossier s5 derived) {acq_rev} sum <= {sum(acq_rev.values()):,} on "
      f"FY20-25 spend {sum(ACQ):,.0f} = {sum(acq_rev.values())/sum(ACQ):.1%} revenue per $; at FY25 group EBITA m "
      f"{pct(ebita_m25)} -> pre-tax yield <= {pct(sum(acq_rev.values())/sum(ACQ)*ebita_m25)} (acquired margins UNKNOWN; "
      f"acquired lines count as organic after 12 months, so this understates)")
impair_sum = sum(IMP[1:])
print(f"Impairments FY21-25 {impair_sum:,} = {impair_sum/sum(ACQ[1:]):.1%} of FY21-25 acquisition spend {sum(ACQ[1:]):,.0f}")
# debt structure
OE_FY25 = NI[5] + DA_CF[5] - CAPEX[5]
print(f"Net debt {NET_DEBT:,} / FY25 owner earnings {OE_FY25:,.0f} = {NET_DEBT/OE_FY25:.2f}x | / FY25 EBITDA(CF D&A, ex-imp) "
      f"{NET_DEBT/(OPINC[5]+IMP[5]+DA_CF[5]):.2f}x | interest cover FY25 {OPINC[5]/INT[5]:.1f}x, TTM {T_OI/T_INT:.1f}x")
fcf_after_div = (T_OCF - T_CAPEX) - T_DIVS
print(f"Maturities {MATURITIES} | 2026-28 wall {1000+1382+2606:,} vs cash {CASH_J26:,} + revolver {REVOLVER_AVAIL:,} + "
      f"TTM FCF after dividends {fcf_after_div:,.0f}/yr")
pe_hi, pe_lo = 388.35 / eps_ttm, 269.75 / eps_ttm
print(f"Stalwart P/E check: own 5-yr P/E range UNKNOWN (no historical prices in dossier). 52w closing range on TTM GAAP "
      f"EPS {eps_ttm:.2f}: {pe_lo:.1f}x-{pe_hi:.1f}x (same-EPS approximation)")

# =====================================================================================
line("B. BUFFETT: margins, capital intensity, ROIC, owner earnings")
TAX_POOL5 = sum(TAXX[i] for i in I5) / sum(PRETAX[i] for i in I5)
TAX_TTM = T_TAX / T_PRETAX
etr = [TAXX[i] / PRETAX[i] for i in range(6)]
print(f"GAAP ETR: " + " ".join(f"{YRS[i]} {pct(etr[i])}" for i in range(6)) +
      f" | TTM {pct(TAX_TTM)} | FY21-25 pooled {pct(TAX_POOL5)}")
ebitda_x = [None] + [(OPINC[i] + IMP[i] + DA_CF[i]) / REV[i] for i in I5]
print(f"{'':6}{'GM':>7}{'OpM':>7}{'EBITDAx':>9}{'FCFm':>7}{'Cpx/R':>7}{'Cpx/Dep':>8}{'Cpx/DAcf':>9}{'DAcf/R':>8}{'Amort/R':>8}{'SBC/R':>7}")
for i in range(6):
    ex = pct(ebitda_x[i]) if ebitda_x[i] else "n/a"
    print(f"{YRS[i]:6}{pct(GP[i]/REV[i]):>7}{pct(OPINC[i]/REV[i]):>7}{ex:>9}{pct((OCF[i]-CAPEX[i])/REV[i]):>7}"
          f"{pct(CAPEX[i]/REV[i]):>7}{CAPEX[i]/DEP_CF[i]:>8.2f}{CAPEX[i]/DA_CF[i]:>9.2f}{pct(DA_CF[i]/REV[i]):>8}"
          f"{pct(AMORT_CF[i]/REV[i]):>8}{pct(SBC[i]/REV[i]):>7}")
print(f"TTM   {pct(T_GP/T_REV):>7}{pct(T_OI/T_REV):>7}{'UNKNOWN':>9}{pct((T_OCF-T_CAPEX)/T_REV):>7}{pct(T_CAPEX/T_REV):>7}"
      f"  (TTM CF-basis D&A and TTM impairments UNKNOWN)")
gm5 = [GP[i] / REV[i] for i in I5]
M_AVG, M_LOW, M_HIGH, M_FY25 = st.mean(ebitda_x[1:]), min(ebitda_x[1:]), max(ebitda_x[1:]), ebitda_x[5]
print(f"Ex-imp EBITDA margin FY21->FY25 change {(ebitda_x[5]-ebitda_x[1])*100:+.2f}pt = {(ebitda_x[5]-ebitda_x[1])*1e4/4:+.0f}bp/yr")
print(f"5-yr (FY21-25) GM mean {pct(st.mean(gm5))} range {pct(min(gm5))}-{pct(max(gm5))} stdev {st.pstdev(gm5)*100:.2f}pp | "
      f"EBITDAx mean {pct(M_AVG)} low {pct(M_LOW)} high {pct(M_HIGH)} FY25 {pct(M_FY25)}")
# ROIC = NOPAT / (equity + debt - cash - STI)  (facts derived definition, equity from 10-K Item 6)
IC = [None] + [EQUITY[i] + DEBT[i] - CASH[i] - STI[i] for i in I5]
IC_J26 = EQ_J26 + DEBT_J26 - CASH_J26 - MKTSEC_J26
print(f"\n{'':6}{'IC':>8}{'GW/IC':>7}{'ROIC':>7}{'ROICxGW':>9}{'EBITA-ROIC':>11}{'EBITAx@pool':>12}")
roic, roic_xgw, ebita_roic, ebitax_pool = [], [], [], []
for i in I5:
    nopat = OPINC[i] * (1 - etr[i])
    r, rx = nopat / IC[i], nopat / (IC[i] - GW[i])
    er = (OPINC[i] + AMORT_CF[i]) * (1 - etr[i]) / IC[i]
    ep = (OPINC[i] + IMP[i] + AMORT_CF[i]) * (1 - TAX_POOL5) / IC[i]
    roic.append(r); roic_xgw.append(rx); ebita_roic.append(er); ebitax_pool.append(ep)
    print(f"{YRS[i]:6}{IC[i]:>8,.0f}{pct(GW[i]/IC[i]):>7}{pct(r):>7}{pct(rx):>9}{pct(er):>11}{pct(ep):>12}")
t_nopat = T_OI * (1 - TAX_TTM)
print(f"TTM   {IC_J26:>8,.0f}{'':>7}{pct(t_nopat/IC_J26):>7}   (GW at 6/30/26 UNKNOWN; ex-GW uses FY25 GW: "
      f"{pct(t_nopat/(IC_J26-GW[5]))})")
print(f"5-yr mean: ROIC {pct(st.mean(roic))} | ex-GW {pct(st.mean(roic_xgw))} | EBITA-ROIC {pct(st.mean(ebita_roic))} | "
      f"EBITA ex-imp @ pooled tax {pct(st.mean(ebitax_pool))} (min {pct(min(ebitax_pool))}, max {pct(max(ebitax_pool))})")
d_nopat = OPINC[5]*(1-TAX_POOL5) - OPINC[1]*(1-TAX_POOL5)
print(f"Incremental ROIC FY21->FY25 at constant pooled tax: dNOPAT {d_nopat:,.0f} / dIC {IC[5]-IC[1]:,.0f} = "
      f"{pct(d_nopat/(IC[5]-IC[1]))} | at each-year ETR: {pct((OPINC[5]*(1-etr[5])-OPINC[1]*(1-etr[1]))/(IC[5]-IC[1]))}")
print(f"Goodwill / total assets FY25 {pct(GW[5]/TA[5])}; goodwill / IC FY25 {pct(GW[5]/IC[5])} (>30% -> ex-GW shown)")
# owner earnings
print("\nOwner earnings = NI + D&A(cash-flow basis) - capex  | SBC-adjusted | segment-D&A version (NOT used):")
OE = [NI[i] + DA_CF[i] - CAPEX[i] for i in range(6)]
for i in range(6):
    print(f"  {YRS[i]}: OE {OE[i]:>6,.0f}  OE-SBC {OE[i]-SBC[i]:>6,.0f}  (seg-D&A basis {NI[i]+DA_SEG[i]-CAPEX[i]:>6,.0f}, "
          f"facts derived owner_earnings {facts['derived'][FYE[i]]['owner_earnings']/1e6:>6,.0f})")
assert abs(OE[5] - fund["owner_earnings_usd"] / 1e6) < 0.5
gap25 = DA_SEG[5] - DA_CF[5]
T_OE_EST = T_NI + (T_DA_SEG - gap25) - T_CAPEX
print(f"  TTM (ESTIMATE: TTM CF-basis D&A UNKNOWN; seg D&A {T_DA_SEG:,.0f} less FY25 gap {gap25:,.0f}): OE ~{T_OE_EST:,.0f}, "
      f"OE-SBC ~{T_OE_EST-T_SBC:,.0f}")
print(f"OE yield on mcap {MCAP:,.0f}: FY25 {pct(OE[5]/MCAP,2)} | FY25 SBC-adj {pct((OE[5]-SBC[5])/MCAP,2)} | "
      f"TTM est {pct(T_OE_EST/MCAP,2)} | TTM est SBC-adj {pct((T_OE_EST-T_SBC)/MCAP,2)}")

# =====================================================================================
line("C. MULTIPLES MATRIX")
ebitda_ttm_seg = T_OI + T_DA_SEG
ebitda25_cf = OPINC[5] + DA_CF[5]
ebitda25_cfx = OPINC[5] + IMP[5] + DA_CF[5]
T_FCF = T_OCF - T_CAPEX
fwd_eps_guide = sum(GUIDE_ADJ_EPS) / 2
med = lambda k: st.median(v[k] for v in PEERS.values())
print(f"EV/EBITDA: TTM (GAAP OI + segment D&A {ebitda_ttm_seg:,.0f}) {EV/ebitda_ttm_seg:.1f}x | FY25 CF-basis "
      f"{EV/ebitda25_cf:.1f}x | FY25 CF-basis ex-imp {EV/ebitda25_cfx:.1f}x | vendor {SYK_VENDOR[0]}x | peer median {med(0):.1f}x")
print(f"P/E trailing GAAP TTM {PRICE/eps_ttm:.1f}x (vendor {fund['trailing_pe']:.1f}x) | peer median {med(1):.2f}x")
print(f"P/E forward on FY26 guide-mid adj EPS {fwd_eps_guide:.3f}: {PRICE/fwd_eps_guide:.1f}x | vendor fwd {fund['forward_pe']:.1f}x "
      f"(= price / FY27 CONSENSUS {PRICE/CONS_EPS27:.1f}x) | peer median {med(2):.2f}x")
print(f"P/FCF TTM {MCAP/T_FCF:.1f}x | FY25 {MCAP/(OCF[5]-CAPEX[5]):.1f}x | SBC-adj TTM {MCAP/(T_FCF-T_SBC):.1f}x | "
      f"peer median P/FCF (1/FCF yield) {100/med(3):.1f}x")
print(f"FCF yield TTM {pct(fcf_yield(T_FCF, MCAP),2)} | FY25 {pct(fcf_yield(OCF[5]-CAPEX[5], MCAP),2)} | SBC-adj TTM "
      f"{pct(fcf_yield(T_FCF-T_SBC, MCAP),2)} | vendor {SYK_VENDOR[3]}% | peer median {med(3):.2f}%")
print(f"OE yield FY25 {pct(OE[5]/MCAP,2)} (SBC-adj {pct((OE[5]-SBC[5])/MCAP,2)})")
g_cons2 = cagr(ADJ_EPS["FY25"], CONS_EPS27, 2)
g_peg = min(g_eps5, g_cons2)
print(f"PEG growth candidates: historical GAAP EPS CAGR FY20-25 {pct(g_eps5)} | CONSENSUS adj EPS FY25->FY27 CAGR "
      f"{pct(g_cons2)} -> lower = {pct(g_peg)}")
ok, why = peg_is_valid(fund["trailing_pe"], fund["forward_pe"], g_peg)
print(f"peg_is_valid(trailing {fund['trailing_pe']:.2f}, fwd {fund['forward_pe']:.2f}, {g_peg:.4f}) -> ({ok}, '{why}')")
dy = 4 * DIV_Q / PRICE
pe_fwd = PRICE / fwd_eps_guide
if ok:
    print(f"PEG (fwd guide-mid P/E / growth%) = {pe_fwd:.1f} / {g_peg*100:.1f} = {pe_fwd/(g_peg*100):.2f} | "
          f"trailing GAAP basis {PRICE/eps_ttm:.1f}/{g_peg*100:.1f} = {PRICE/eps_ttm/(g_peg*100):.2f} (basis mismatch) | vendor {fund['peg']}")
print(f"Lynch ratio (growth% + yield%) / P/E: fwd ({g_peg*100:.1f} + {dy*100:.2f}) / {pe_fwd:.1f} = "
      f"{(g_peg*100+dy*100)/pe_fwd:.2f} | trailing GAAP ({g_peg*100:.1f} + {dy*100:.2f}) / {PRICE/eps_ttm:.1f} = "
      f"{(g_peg*100+dy*100)/(PRICE/eps_ttm):.2f}")
ncps = -NET_DEBT / SH_OUT
print(f"Net cash/share {ncps:.2f} -> net-cash-adj P/E: TTM GAAP ({PRICE} - ({ncps:.2f})) / {eps_ttm:.2f} = "
      f"{(PRICE-ncps)/eps_ttm:.1f}x | on guide-mid adj EPS {(PRICE-ncps)/fwd_eps_guide:.1f}x")
print(f"ZBH (user holding) vs SYK, dossier s7 vendor: EV/EBITDA {PEERS['ZBH'][0]} vs {SYK_VENDOR[0]} | fwd P/E "
      f"{PEERS['ZBH'][2]} vs {SYK_VENDOR[2]} | FCF yield {PEERS['ZBH'][3]}% vs {SYK_VENDOR[3]}%")

# =====================================================================================
line("D. DISCOUNT RATE")
BETA = 0.67 * BETA_RAW + 0.33
KE = RF + BETA * ERP
KD = RF                               # market YTM / spread UNKNOWN -> risk-free used as a LOWER BOUND for Kd
kd_hist = INT[5] / ((DEBT[4] + DEBT[5]) / 2)
WE, WD = MCAP / (MCAP + DEBT_J26), DEBT_J26 / (MCAP + DEBT_J26)
TAX_BASE = TAX_POOL5
wacc_raw = WE * KE + WD * KD * (1 - TAX_BASE)
WACC = round(max(wacc_raw, FLOOR), 3)
print(f"Beta raw {BETA_RAW} (fund) -> Blume 0.67*{BETA_RAW}+0.33 = {BETA:.3f}")
print(f"Ke = {pct(RF,2)} + {BETA:.3f} x {pct(ERP,1)} = {pct(KE,2)}")
print(f"Kd pre-tax {pct(KD,2)} (= 10y UST, spread UNKNOWN; FY25 interest / avg debt = {pct(kd_hist,2)} is below UST, not a "
      f"market rate) | after-tax at {pct(TAX_BASE)}: {pct(KD*(1-TAX_BASE),2)}")
print(f"Weights: E {MCAP:,.0f} ({pct(WE)}) market; D {DEBT_J26:,} ({pct(WD)}) book (market value UNKNOWN; leases excluded)")
print(f"WACC raw {pct(wacc_raw,2)} | floor {pct(FLOOR)} -> WACC used {pct(WACC)}")
for lab, b, kd in (("beta 1.0 (unsourced default)", 1.0, KD), ("raw beta 0.781 (no Blume)", BETA_RAW, KD),
                   ("Kd +100bp", BETA, KD + 0.01)):
    w = WE * (RF + b * ERP) + WD * kd * (1 - TAX_BASE)
    print(f"  alt {lab:<30} WACC {pct(w,2)}")

# =====================================================================================
line("E. DCF SCENARIOS")
N = 10
STUB = (date(2026, 10, 13) - date(2026, 6, 30)).days / 365.25
DA_PCT = DA_CF[5] / REV[5]
ACQ_AM = AMORT_CF[5] / REV[5]
CAPEX5 = st.mean(CAPEX[i] / REV[i] for i in I5)
CAPEX_TTM, CAPEX_FY25 = T_CAPEX / T_REV, CAPEX[5] / REV[5]
# --- calibrate w: model pre-WC FCF vs actual SBC-adjusted unlevered FCF, FY21-25 pooled ---
drag, odrev, act_m = [], [], []
for i in I5:
    pre = (OPINC[i] + IMP[i]) * (1 - etr[i]) + DA_CF[i] - CAPEX[i]          # model FCF before WC
    act = OCF[i] - CAPEX[i] - SBC[i] + INT[i] * (1 - etr[i])                # actual unlevered, SBC-adjusted
    drag.append(pre - act); odrev.append(ORG[i] * REV[i - 1]); act_m.append(act / REV[i])
W = sum(drag) / sum(odrev)
FCF5 = st.mean(act_m)
print("Calibration of w (pre-WC model FCF - actual SBC-adj unlevered FCF) / organic delta-revenue:")
print("  " + " | ".join(f"{YRS[i]} drag {drag[k]:,.0f} on dRev {odrev[k]:,.0f}, actual m {pct(act_m[k])}" for k, i in enumerate(I5)))
print(f"  pooled w = {sum(drag):,.0f} / {sum(odrev):,.0f} = {pct(W)} | 5-yr mean SBC-adj unlevered FCF margin {pct(FCF5)} | "
      f"FY25 {pct(act_m[-1])} | TTM {pct((T_OCF-T_CAPEX-T_SBC+T_INT*(1-TAX_TTM))/T_REV)}")
print(f"Common: base rev TTM {T_REV:,.0f} (yr1 = Jul-26..Jun-27) | D&A {pct(DA_PCT,2)} (FY25 CF basis) | acq_amort_pct "
      f"{pct(ACQ_AM,2)} (FY25 amortisation of intangibles) | WACC {pct(WACC)} | w {pct(W)} | mid_year, stub {STUB:.4f}y | "
      f"bridge {BRIDGE:,.1f} | shares {SH_DIL}")


def fade(a, b, n):  # n values stepping linearly from a (exclusive) to b (inclusive)
    return [a + (b - a) * (k + 1) / n for k in range(n)]


TAX_BEAR = 1002 / (4514 + 170)   # SKEPTIC-CORRECTION C2: FY25 cash taxes paid / pretax ex-impairment (10-K XBRL)


def roic_at(tax, f):
    return f((OPINC[i] + IMP[i] + AMORT_CF[i]) * (1 - tax) / IC[i] for i in I5)


SCEN = {
    "BEAR": dict(growth=[H1_26_ORG] * 3 + fade(H1_26_ORG, 0.030, 7),
                 ebitda_margin=fade(M_AVG, M_LOW, 3) + [M_LOW] * 7,
                 capex=CAPEX_TTM, tax=TAX_BEAR, tg=0.030, troic=roic_at(TAX_BEAR, min)),  # SKEPTIC-CORRECTION C2
    "BASE": dict(growth=[sum(GUIDE_ORG) / 2] + fade(sum(GUIDE_ORG) / 2, 0.035, 9),
                 ebitda_margin=[M_AVG] * N,
                 capex=CAPEX5, tax=TAX_BASE, tg=0.035, troic=roic_at(TAX_BASE, st.mean)),
    "BULL": dict(growth=[GUIDE_ORG[1]] + [ORG[5]] * 3 + fade(ORG[5], 0.040, 6),
                 ebitda_margin=[M_FY25 + 0.005 * k for k in range(6)] + [M_FY25 + 0.025] * 4,
                 capex=CAPEX_FY25, tax=TAX_BASE, tg=0.040, troic=roic_at(TAX_BASE, max)),
}


def kw(s, **over):
    p = {**SCEN[s], **over}
    n = len(p["growth"])
    return dict(base_revenue=p.get("base_revenue", T_REV), growth=p["growth"], ebitda_margin=p["ebitda_margin"],
                capex_pct=p.get("capex_pct", [p["capex"]] * n), da_pct=p.get("da_pct", [DA_PCT] * n), tax=p["tax"],
                wacc=p.get("wacc", WACC), net_debt=p.get("net_debt", BRIDGE), shares=p.get("shares", SH_DIL),
                terminal_growth=p["tg"], terminal_roic=p["troic"], wc_pct_of_delta_rev=p.get("w", W),
                acq_amort_pct=p.get("acq_amort_pct", [ACQ_AM] * n), mid_year=True, stub_years=STUB)


RES = {}
for s in ("BEAR", "BASE", "BULL"):
    r = dcf(**kw(s)); RES[s] = r; p = SCEN[s]
    print(f"\n--- {s}: tax {pct(p['tax'])} | capex {pct(p['capex'],2)} | g_term {pct(p['tg'])} | ROIC_term {pct(p['troic'])}")
    print(f"    growth   {[round(g*100,2) for g in p['growth']]}")
    print(f"    EBITDA m {[round(m*100,2) for m in p['ebitda_margin']]}")
    print(f"{'yr':>3}{'Revenue':>9}{'EBITDA':>8}{'EBIT':>7}{'D&A':>7}{'Capex':>7}{'FCF':>7}{'FCFm':>7}{'PV':>7}")
    for y, rev, eb, ebit, da, cx, f, pv in r.rows:
        print(f"{y:>3}{rev:>9,.0f}{eb:>8,.0f}{ebit:>7,.0f}{da:>7,.0f}{cx:>7,.0f}{f:>7,.0f}{pct(f/rev):>7}{pv:>7,.0f}")
    cagr10 = (r.rows[-1][1] / T_REV) ** (1 / N) - 1
    print(f"10-yr revenue CAGR {pct(cagr10)} | PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} | "
          f"TV share {r.terminal_share:.0%}" + ("  ** TV > 75% FLAG **" if r.terminal_share > .75 else ""))
    print(f"EV {r.enterprise_value:,.0f} | equity {r.equity_value:,.0f} | PER SHARE ${r.per_share:,.2f} | "
          f"vs ${PRICE}: {r.upside(PRICE):+.1%} | implied EV/TTM-EBITDA(seg) {r.enterprise_value/ebitda_ttm_seg:.1f}x | "
          f"implied P/E on FY26 guide-mid adj EPS {r.per_share/fwd_eps_guide:.1f}x")
b = RES["BASE"]
y10 = b.rows[-1]
expl_reinv = (y10[5] - DEP_CF[5] / REV[5] * y10[1] + W * (y10[1] - b.rows[-2][1])) / (y10[3] * (1 - TAX_BASE))
print(f"\nBASE consistency: yr-10 explicit reinvestment rate (capex - depreciation + WC) / NOPAT = {pct(expl_reinv)} "
      f"(implied RONIC {pct(SCEN['BASE']['tg']/expl_reinv)}) vs terminal reinvestment rate g/ROIC = "
      f"{pct(SCEN['BASE']['tg']/SCEN['BASE']['troic'])} (ROIC {pct(SCEN['BASE']['troic'])}): terminal reinvests more, i.e. "
      f"is the more conservative (consistent with growth partly bought via M&A at group returns)")
print("\nAlternative-basis checks on BASE (one change each):")
ALT = {
    "D&A fade to capex by yr10 INSTEAD of acq_amort_pct": dict(da_pct=[DA_PCT] * 5 + fade(DA_PCT, CAPEX5, 5), acq_amort_pct=None),
    "segment D&A basis 6.25% (adds back loaner amort, no spend)": dict(da_pct=[DA_SEG[5] / REV[5]] * N,
                                                                      ebitda_margin=[M_AVG + (DA_SEG[5]-DA_CF[5])/REV[5]] * N),
    "tax 22.5% (midpoint pooled / TTM) in NOPAT": dict(tax=(TAX_BASE + TAX_TTM) / 2),
    "tax = TTM GAAP ETR 27.6% in NOPAT": dict(tax=TAX_TTM),
    "EBITDA margin held at FY25 level": dict(ebitda_margin=[M_FY25] * N),
    "w = 0 (no WC drag; FY25/TTM-like conversion)": dict(w=0.0),
    "leases in net debt (+501) and lease cost (+205) in EBITDA": dict(net_debt=BRIDGE + LEASES_FY25,
                                                                      ebitda_margin=[M_AVG + 205 / REV[5]] * N),
    "no debt-like items / no dividend deduction": dict(net_debt=NET_DEBT),
    "also deduct Q3-26 dividend (ex-date UNKNOWN)": dict(net_debt=BRIDGE + DIV_Q * SH_OUT),
    "basic shares 383.573M instead of diluted 386.0M": dict(shares=SH_OUT),
    "no mid-year, no stub (old convention)": None,
    "COMBINED (2 inputs): FY25 margin + w=0 (current conversion persists)": dict(ebitda_margin=[M_FY25] * N, w=0.0),
    "instrument spend > loaner amortisation by $100M/yr (capex +100/TTM rev)": dict(capex_pct=[CAPEX5 + 100 / T_REV] * N),
}
for lab, over in ALT.items():
    if over is None:
        k = kw("BASE"); k.update(mid_year=False, stub_years=0.0)
    else:
        k = kw("BASE", **over)
    if k.get("acq_amort_pct") is None:
        k.pop("acq_amort_pct")
    r = dcf(**k)
    print(f"  {lab:<62} ${r.per_share:7.2f} ({r.per_share/b.per_share-1:+.1%} vs base; TV {r.terminal_share:.0%})")

# =====================================================================================
line("F. REVERSE DCF & SENSITIVITY")
for s in ("BASE", "BEAR", "BULL"):
    k = kw(s); k.pop("base_revenue"); k.pop("growth")
    for px, lab in ((PRICE, "close"), (PRICE_INPUTS, "00_inputs")):
        gi = reverse_dcf(price=px, base_revenue=T_REV, years=N, **k)
        if s != "BASE" and lab != "close":
            continue
        print(f"Implied constant 10-yr revenue CAGR at {s} margins/capex/tax/g/ROIC, price ${px} ({lab}): {pct(gi,2)} "
              f"(yr-10 revenue {T_REV*(1+gi)**N:,.0f})")


def solve(fn, lo, hi, target, it=80):
    for _ in range(it):
        mid = (lo + hi) / 2
        if fn(mid) < target: lo = mid
        else: hi = mid
    return mid


m_impl = solve(lambda m: dcf(**kw("BASE", ebitda_margin=[m] * N)).per_share, 0.10, 0.60, PRICE)
print(f"Implied flat EBITDA margin at BASE growth path: {pct(m_impl)} (5-yr mean {pct(M_AVG)}, high {pct(M_HIGH)})")
irr = solve(lambda w: -dcf(**kw("BASE", wacc=w)).per_share, 0.04, 0.20, -PRICE)
print(f"Implied discount rate (IRR) on BASE cash flows at ${PRICE}: {pct(irr,2)} vs WACC {pct(WACC)}")
irr_b = solve(lambda w: -dcf(**kw("BULL", wacc=w)).per_share, 0.045, 0.20, -PRICE)
print(f"Implied discount rate (IRR) on BULL cash flows at ${PRICE}: {pct(irr_b,2)}")
# growth held at a constant rate for X years then base fade: years of guide-rate growth needed
for hold in (3, 5, 7):
    g = [sum(GUIDE_ORG)/2] * hold + fade(sum(GUIDE_ORG)/2, 0.035, N - hold)
    print(f"  BASE with {hold} yrs at 8.8% before fading: ${dcf(**kw('BASE', growth=g)).per_share:,.2f}")
wg = [WACC - 0.01, WACC - 0.005, WACC, WACC + 0.005, WACC + 0.01]
gg = [0.025, 0.030, 0.035, 0.040, 0.045]
kb = kw("BASE")
grid = sensitivity({"wacc": wg}, {"terminal_growth": gg}, **kb)
print(f"\nBASE value/share, WACC (rows) x terminal growth (cols); ROIC_term {pct(SCEN['BASE']['troic'])} fixed")
print(f"{'':>8}" + "".join(f"{x*100:>9.1f}%" for x in gg))
for wv, rowv in zip(wg, grid):
    tag = " <floor" if wv < FLOOR else ""
    print(f"{wv*100:>7.1f}%" + "".join(f"{v:>10.2f}" for v in rowv) + tag)
print("  (4.5% column exceeds the 4% terminal-growth cap: illustrative only)")
grid2 = sensitivity({"wacc": wg}, {"terminal_roic": [0.10, 0.12, SCEN['BASE']['troic'], 0.16, 0.20]}, **kb)
print(f"\nBASE value/share, WACC x terminal ROIC (g {pct(SCEN['BASE']['tg'])} fixed)")
print(f"{'':>8}" + "".join(f"{x*100:>9.1f}%" for x in [0.10, 0.12, SCEN['BASE']['troic'], 0.16, 0.20]))
for wv, rowv in zip(wg, grid2):
    print(f"{wv*100:>7.1f}%" + "".join(f"{v:>10.2f}" for v in rowv))

# =====================================================================================
line("G. LOAD-BEARING INPUTS (+/-10% relative, one at a time, BASE)")
base_ps = b.per_share
bp = SCEN["BASE"]
TESTS = [
    ("EBITDA margin (5-yr mean ex-imp)", lambda f: dict(ebitda_margin=[m * f for m in bp["ebitda_margin"]])),
    ("WACC", lambda f: dict(wacc=WACC * f)),
    ("Revenue growth path (every year)", lambda f: dict(growth=[g * f for g in bp["growth"]])),
    ("Terminal growth", lambda f: dict(tg=bp["tg"] * f)),
    ("Tax rate (NOPAT only; WACC held)", lambda f: dict(tax=bp["tax"] * f)),
    ("Terminal ROIC", lambda f: dict(troic=bp["troic"] * f)),
    ("Capex % revenue", lambda f: dict(capex=bp["capex"] * f)),
    ("WC intensity w", lambda f: dict(w=W * f)),
    ("acq_amort_pct (terminal add-back)", lambda f: dict(acq_amort_pct=[ACQ_AM * f] * N)),
    ("D&A % revenue (tax shield)", lambda f: dict(da_pct=[DA_PCT * f] * N)),
    ("Net debt + bridge items", lambda f: dict(net_debt=BRIDGE * f)),
]
out = []
for lab, mk in TESTS:
    lo_, hi_ = dcf(**kw("BASE", **mk(0.9))).per_share, dcf(**kw("BASE", **mk(1.1))).per_share
    out.append((abs(hi_ - lo_), lab, lo_, hi_))
print(f"BASE ${base_ps:,.2f}")
for sw, lab, lo_, hi_ in sorted(out, reverse=True):
    print(f"  {lab:<36} -10%: ${lo_:7.2f} ({lo_/base_ps-1:+6.1%})  +10%: ${hi_:7.2f} ({hi_/base_ps-1:+6.1%})  swing ${sw:6.2f}")
# discount-rate components translated
for lab, b_, rf_ in (("beta x0.9", BETA * 0.9, RF), ("beta x1.1", BETA * 1.1, RF), ("rf x0.9", BETA, RF * 0.9), ("rf x1.1", BETA, RF * 1.1)):
    w = max(WE * (rf_ + b_ * ERP) + WD * rf_ * (1 - TAX_BASE), FLOOR)
    print(f"  WACC component {lab:<10} (beta {b_:.3f}, rf {pct(rf_,2)}) -> WACC {pct(w,2)} -> "
          f"${dcf(**kw('BASE', wacc=round(w,4))).per_share:,.2f}")

# =====================================================================================
# SKEPTIC SECTION (03_skeptic.md s3-s5). Everything below is additive; nothing above is overwritten except C1/C2.
# =====================================================================================
line("S. SKEPTIC: corrected scenarios, variants, quality of earnings, $1 test, EV")
QUANT_ORIG = {"BEAR": 131.41, "BASE": 209.13, "BULL": 304.40}   # 02_quant.md s E (pre-correction)
for s_ in ("BEAR", "BASE", "BULL"):
    print(f"  {s_}: corrected ${RES[s_].per_share:,.2f} vs Quant ${QUANT_ORIG[s_]:,.2f} "
          f"({RES[s_].per_share/QUANT_ORIG[s_]-1:+.1%}); TV share {RES[s_].terminal_share:.0%}")
print(f"  Bear tax {pct(TAX_BEAR)} (was TTM {pct(TAX_TTM)}); bear terminal ROIC {pct(SCEN['BEAR']['troic'])}")


def tv_midyear_fix(r):
    """Library discounts TV at n while explicit flows are mid-year (n-0.5). Consistent mid-year TV = TV*(1+WACC)^0.5."""
    add = r.pv_terminal * ((1 + WACC) ** 0.5 - 1)
    return (r.equity_value + add) / SH_DIL


M_3Y = st.mean(ebitda_x[3:6])                 # FY23-25 mean ex-imp EBITDA margin
SBC_PCT = SBC[5] / REV[5]
DEBT_FV = 14024                               # 10-Q Q2-26 XBRL DebtInstrumentFairValue (accn 0000310764-26-000050)
FCTO = 754 + 11                               # 10-K FY25: German FCTO assessments 2010-17 (UTB share unknown)
TAX_EX_IP = (1268 - 405) / 4514               # FY25 ETR ex 'disposition of assets' one-off
TAX_H1_26 = 393 / 2414                        # 10-Q Q2-26 H1 ETR
g_h2_implied = (0.088 - (11888 / REV[5]) * 0.058) / (1 - 11888 / REV[5])   # guide-mid FY organic vs H1 actual
base_g = SCEN["BASE"]["growth"]
VAR = {
    "S1 TV discounted mid-year-consistent (x(1+WACC)^0.5)": ("tvfix", None),
    f"S2 EBITDA margin = FY23-25 mean {pct(M_3Y,2)} (vs 5-yr {pct(M_AVG,2)})": ("kw", dict(ebitda_margin=[M_3Y] * N)),
    f"S3 SBC treated as non-cash (margin +{pct(SBC_PCT,2)}; reference only)": ("kw", dict(ebitda_margin=[M_AVG + SBC_PCT] * N)),
    "S4 debt at fair value 14,024 (bridge -918)": ("kw", dict(net_debt=BRIDGE - (DEBT_J26 - DEBT_FV))),
    "S5 German FCTO assessment 765 added to bridge (max; partly reserved)": ("kw", dict(net_debt=BRIDGE + FCTO)),
    "S6 Q3-26 dividend also deducted (337.5)": ("kw", dict(net_debt=BRIDGE + DIV_Q * SH_OUT)),
    f"S7 year-1 growth = guide-implied H2-26 organic {pct(g_h2_implied,1)} (yrs 2-10 unchanged)": ("kw", dict(growth=[g_h2_implied] + base_g[1:])),
    f"S8a base tax = H1-26 ETR {pct(TAX_H1_26)}": ("kw", dict(tax=TAX_H1_26)),
    f"S8b base tax = FY25 ETR ex-IP one-off {pct(TAX_EX_IP)}": ("kw", dict(tax=TAX_EX_IP)),
    f"S8c base tax = FY25 cash-tax rate {pct(TAX_BEAR)}": ("kw", dict(tax=TAX_BEAR)),
}
bps = RES["BASE"].per_share
VOUT = {}
print(f"\nBASE (corrected) ${bps:,.2f}. Variants, one change each:")
for lab, (kind, over) in VAR.items():
    v = tv_midyear_fix(RES["BASE"]) if kind == "tvfix" else dcf(**kw("BASE", **over)).per_share
    VOUT[lab[:2]] = v
    print(f"  {lab:<78} ${v:7.2f} ({v/bps-1:+.1%})")
# Skeptic-judgment scenario set: TV fix on all three + base margin at FY23-25 mean
r_base_sk = dcf(**kw("BASE", ebitda_margin=[M_3Y] * N))
SK = {"BEAR": tv_midyear_fix(RES["BEAR"]), "BASE": tv_midyear_fix(r_base_sk), "BULL": tv_midyear_fix(RES["BULL"])}
print(f"\nSkeptic-judgment set (S1 on all + S2 on base): bear ${SK['BEAR']:.2f} base ${SK['BASE']:.2f} bull ${SK['BULL']:.2f}")
gi_sk = reverse_dcf(price=PRICE, base_revenue=T_REV, years=N, **{k: v for k, v in kw("BASE", ebitda_margin=[M_3Y] * N).items()
                                                                 if k not in ("base_revenue", "growth")})
gi_c = reverse_dcf(price=PRICE, base_revenue=T_REV, years=N, **{k: v for k, v in kw("BASE").items() if k not in ("base_revenue", "growth")})
print(f"Reverse DCF at ${PRICE}: base margins {pct(gi_c,2)} | FY23-25 margins {pct(gi_sk,2)} (constant 10-yr revenue CAGR)")

# ---------------- probabilities & EV ----------------
P = {"BEAR": 0.25, "BASE": 0.50, "BULL": 0.25}
def ev_stats(vals, lab):
    ev = sum(P[k] * vals[k] for k in P)
    mos = 1 - PRICE / ev
    asym = (ev - PRICE) / (PRICE - vals["BEAR"]) if vals["BEAR"] < PRICE else float("nan")
    print(f"  {lab:<34} EV ${ev:7.2f} | MoS {mos:+.1%} | asymmetry {asym:+.2f} | price/EV {PRICE/ev:.3f} | "
          f"EVx0.8 ${ev*0.8:.2f} EVx0.7 ${ev*0.7:.2f} EVx1.3 ${ev*1.3:.2f}")
    return ev
print(f"\nProbabilities {P}; price ${PRICE}")
EV_Q = ev_stats(QUANT_ORIG, "Quant values (uncorrected)")
EV_C = ev_stats({k: RES[k].per_share for k in P}, "Corrected (C1+C2) -- PRIMARY")
EV_SK = ev_stats(SK, "Skeptic-judgment (S1+S2)")
for pb in ((0.30, 0.50, 0.20), (0.20, 0.50, 0.30), (0.20, 0.55, 0.25), (0.30, 0.45, 0.25)):
    vals = {k: RES[k].per_share for k in P}
    ev = pb[0] * vals["BEAR"] + pb[1] * vals["BASE"] + pb[2] * vals["BULL"]
    print(f"  probability sensitivity bear/base/bull {pb}: corrected EV ${ev:.2f} (x1.3 ${ev*1.3:.2f})")

# ---------------- quality of earnings ----------------
print("\nSBC % OCF / % revenue: " + " ".join(f"{YRS[i]} {pct(SBC[i]/OCF[i])}/{pct(SBC[i]/REV[i],2)}" for i in range(6)) +
      f" | TTM {pct(T_SBC/T_OCF)}/{pct(T_SBC/T_REV,2)}")
print(f"FCF FY25 {OCF[5]-CAPEX[5]:,.0f} -> SBC-adj {OCF[5]-CAPEX[5]-SBC[5]:,.0f} | TTM {T_OCF-T_CAPEX:,.0f} -> {T_OCF-T_CAPEX-T_SBC:,.0f}")
print("Accruals NI vs OCF (OCF/NI) and Sloan ratio (NI-OCF)/avg total assets:")
for i in range(1, 6):
    print(f"  {YRS[i]}: NI {NI[i]:,.0f} OCF {OCF[i]:,.0f} OCF/NI {OCF[i]/NI[i]:.2f} Sloan {(NI[i]-OCF[i])/((TA[i]+TA[i-1])/2):+.1%}")
print(f"  FY21-25 cumulative NI {sum(NI[1:]):,.0f} OCF {sum(OCF[1:]):,.0f} ratio {sum(OCF[1:])/sum(NI[1:]):.2f}")
OTHER_NET = {"FY25": -470, "FY24": -306, "FY23": -134, "FY22": -107, "FY21": -47, "FY20": 2}   # dossier s2 / 10-K CF stmt
GAP = {"FY25": 377, "FY24": 376, "FY23": 313, "FY22": 280, "FY21": 282, "FY20": 264}
print("OCF 'Other, net' vs inferred loaner amortisation inside it (no separate CF add-back line in the 10-K):")
for y in OTHER_NET:
    print(f"  {y}: Other,net {OTHER_NET[y]:+5d} | inferred loaner amort {GAP[y]} | implied other outflows {OTHER_NET[y]-GAP[y]:+5d}")
ADJ = {"FY23": (10.60, 8.25), "FY24": (12.19, 7.76), "FY25": (13.63, 8.40)}
for y, (adj, gaap) in ADJ.items():
    print(f"  {y}: adj EPS {adj} vs GAAP {gaap}: add-backs ${adj-gaap:.2f}/sh = {1-gaap/adj:.1%} of adj EPS; x diluted "
          f"{DIL[YRS.index(y)]:.1f}M = ~${(adj-gaap)*DIL[YRS.index(y)]:,.0f}M after tax")
amort_ps = [AMORT_CF[i] for i in (3, 4, 5)]
print(f"  intangible amortisation (pre-tax) FY23-25 {amort_ps}; impairments {IMP[3:]}")

# ---------------- capital allocation: $1 test, shares, buybacks ----------------
PX = {"2020-12-31": 245.04, "2021-10-13": 256.50, "2025-12-31": 351.47, "2026-10-13": 282.55}   # yfinance raw closes
DIL_SH = {"2020": 380.3, "2021": 382.3, "2025": 386.5}                                           # facts diluted
mA0, mA1 = PX["2020-12-31"] * DIL_SH["2020"], PX["2025-12-31"] * DIL_SH["2025"]
ret_A = sum(NI[1:6]) - sum(DIVS[1:6])
print(f"\n$1 test A (FY-end): mcap {mA0:,.0f} (245.04 x 380.3) -> {mA1:,.0f} (351.47 x 386.5); d {mA1-mA0:,.0f} / retained "
      f"FY21-25 {ret_A:,.0f} (NI {sum(NI[1:6]):,.0f} - div {sum(DIVS[1:6]):,.0f}) = {(mA1-mA0)/ret_A:.2f}")
mB0, mB1 = PX["2021-10-13"] * DIL_SH["2021"], PRICE * SH_DIL
print(f"$1 test B (as-of): mcap {mB0:,.0f} (256.50 x 382.3) -> {mB1:,.0f} ({PRICE} x {SH_DIL}); d {mB1-mB0:,.0f} / retained "
      f"(approx FY21-25) {ret_A:,.0f} = {(mB1-mB0)/ret_A:.2f}; using TTM window NI FY22-25+TTM-FY25 proxy: see md")
SH10 = {2014: 382.8, 2015: 380.9, 2016: 378.5, 2017: 380.1, 2018: 380.3, 2019: 379.9, 2020: 380.3, 2021: 382.3,
        2022: 382.2, 2023: 383.7, 2024: 385.6, 2025: 386.5}                                        # XBRL diluted
BB = {2014: 100, 2015: 700, 2016: 13, 2017: 230, 2018: 300, 2019: 307}                             # XBRL repurchases
AVGPX = {2015: 93.43, 2016: 110.61, 2017: 139.93, 2018: 166.88, 2019: 198.49}                       # yfinance yearly mean close
print(f"Diluted shares 2014->2025: {SH10[2014]} -> {SH10[2025]} ({(SH10[2025]/SH10[2014])**(1/11)-1:+.2%}/yr); "
      f"2020->2025 {(SH10[2025]/SH10[2020])**(1/5)-1:+.2%}/yr")
print(f"Buybacks 2014-19 ${sum(BB.values()):,}M; 2020-H1'26 $0. Avg close in buyback years: {AVGPX}")
print(f"Acquisitions FY14-25 (XBRL): {916+153+4332+831+2451+802+sum(ACQ):,.0f}")
# SBC treated as non-cash in all three scenarios (reference only; the primary values above are SBC-as-cash)
SBC_NC = {s_: dcf(**kw(s_, ebitda_margin=[m + SBC_PCT for m in SCEN[s_]["ebitda_margin"]])).per_share for s_ in P}
print(f"\nSBC as non-cash (all scenarios): bear ${SBC_NC['BEAR']:.2f} base ${SBC_NC['BASE']:.2f} bull ${SBC_NC['BULL']:.2f} -> "
      f"EV ${sum(P[k]*SBC_NC[k] for k in P):.2f} (vs SBC-as-cash EV ${EV_C:.2f})")
print("TV mid-year fix by scenario: " + " ".join(f"{k} ${tv_midyear_fix(RES[k]):.2f} ({tv_midyear_fix(RES[k])/RES[k].per_share-1:+.1%})" for k in P))
# break-even bear probability (base fixed at 50%) for price = EV x 1.3
v = {k: RES[k].per_share for k in P}
pbe = (0.5 * v["BASE"] + 0.5 * v["BULL"] - PRICE / 1.3) / (v["BULL"] - v["BEAR"])
print(f"Break-even p(bear) with p(base)=50% for price = EV x 1.3: {pbe:.1%}")
print(f"IRR at ${PRICE}: base {pct(irr,2)}, bull {pct(irr_b,2)} vs rf {pct(RF,2)}")
