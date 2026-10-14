"""BABA (Alibaba ADS, NYSE; 1 ADS = 8 ordinary shares) - FULL template + SOTP cross-check, as of 2026-10-13.
CNY millions unless stated. Modelled per ORDINARY share in CNY, converted to USD per ADS at
00_inputs.json CNYUSD (x8 x FX), and to SGD per ADS at 00_inputs.json SGDUSD.

TREATMENTS (stated once, applied everywhere)
  BASE PERIOD     TTM to 30 Jun 2026 (facts add. ttm_jun2026_derived), so the operating base and the
                  balance sheet used for net cash (Jun-26, dossier S1) share a date. Year 1 = Jul-26..Jun-27.
  VALUATION DATE  dcf(mid_year=True, stub_years = 2026-06-30 -> 2026-10-13). The FY26 dividend
                  (US$1.05/ADS, record 11 Jun, payable ~13 Jul 2026) was still in Jun-26 cash and a buyer
                  today does not receive it -> deducted. Aug-26 placing cash (HK$79,785m) and its 710m
                  shares are both included (cash added; shares in the HKEX 29-Sep count).
  EBIT DEFINITION Company adjusted EBITA minus SBC. Adjusted EBITA is after depreciation, before
                  amortisation of acquired intangibles, goodwill impairment and one-offs (EU DSA fine).
  D&A             = depreciation only = adj EBITDA - adj EBITA (TTM 41,990). Acquired-intangible
                  amortisation is excluded from BOTH EBIT and the add-back, so it never enters the model;
                  therefore acq_amort_pct is NOT passed and D&A is NOT faded (either would double-count).
                  Resolves the XBRL 34,963 / fj 47,118 / company 42,146 D&A conflict (dossier S10.3).
  SBC             DEDUCT method: SBC/revenue (TTM ratio) is subtracted from EBIT every year; share count
                  held flat at HKEX issued 19,901,959,514 (no dilution layer).
  LEASES          US GAAP filer (not IFRS 16): operating-lease cost sits inside EBITA/OCF, so leases
                  (RMB 21,726m) are kept OUT of net debt. No lease-principal adjustment needed.
  CONVERTIBLES    Kept in debt at book (54,905). In-the-money conversion value gap is small (printed).
  INVESTMENTS     Equity-method (203,207) + non-treasury equity securities (254,210) at BOOK less a
                  scenario haircut (bear 50 / base 30 / bull 15%, ASSUMPTION). Their income (Ant share of
                  profit, revaluation gains) is NOT in the DCF cash flows, so no double count.
  DISCOUNT RATE   USD rate (the ADS is a USD asset of a Cayman holdco; the holder's opportunity cost is
                  USD) applied to CNY cash flows translated at FLAT spot. Not crediting the CNY forward
                  premium (USD 10y 5.22% vs CNY 10y 1.67%) is the deliberate, stated stand-in for a
                  China / VIE / capital-control premium, which the dossier does not source. The
                  IRP-consistent CNY rate is shown as a sensitivity. Terminal g capped at the yield of the
                  CASH-FLOW currency (CNY 1.67%), not the USD 4% cap.

Tags: (facts: ...), (dossier S#), (fj: fundamentals.json), (inputs: 00_inputs.json),
ASSUMPTION = Quant-chosen; attack these first.
Run: python3 reports/runs/BABA_2026-10-13/02_model.py
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
FJALL = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]
FJ = FJALL["BABA"]
A, RA, DV = F["annual"], F["researcher_additions"], F["derived"]
YE = F["fiscal_year_ends"]                                   # FY2021..FY2026 (31 Mar)
LBL = [f"FY{y[2:4]}" for y in YE]
avg = lambda v: sum(v) / len(v)


def ann(key):
    return [A[key][y]["val"] / 1e6 if y in A[key] else None for y in YE]


def hdr(t):
    print("\n" + "=" * 100 + f"\n{t}\n" + "=" * 100)


def row(lab, v, f="{:>10.1%}"):
    print(f"{lab:<40}" + "".join(f.format(x) if x is not None else f"{'UNKNOWN':>10}" for x in v))


# =============================================================== 0. market inputs
P_USD = INP["price"]                                         # inputs: 109.6351 (intraday 13:52Z) = price of record
P_USD_CLOSE = 110.535                                        # dossier S1 raw close 2026-10-13 (fj 110.53)
FX = INP["fx_spot_to_usd"]["CNYUSD"]                         # inputs: USD per CNY 0.14968716
SGDUSD = INP["fx_spot_to_usd"]["SGDUSD"]                     # inputs: USD per SGD 0.78120732
ADS = 8                                                      # dossier S1: 1 ADS = 8 ordinary
SH = 19_901.959514                                           # m ordinary, HKEX issued 2026-09-29 (facts add.)
SH_GAAP_BASIC = 18_671 + 710                                 # dossier S1: Q1 FY27 basic wtd + placing
SH_DIL = 19_324 + 710                                        # dossier S1: Q1 FY27 diluted wtd + placing
P_CNY = P_USD / FX / ADS                                     # CNY per ordinary share
P_CNY_CLOSE = P_USD_CLOSE / FX / ADS
MCAP = P_CNY * SH                                            # CNY m
to_ads = lambda cny_per_sh: cny_per_sh * ADS * FX            # CNY/ordinary share -> USD/ADS
to_sgd = lambda usd: usd / SGDUSD
RF_USD = INP["risk_free_10y"]["USD"]["value_pct"] / 100      # inputs: 5.22% (DGS10 2026-10-08)
RF_CNY = 0.0167                                              # dossier S1: ChinaBond 10y 2026-10-13 [FETCH];
                                                             # inputs CNY = null ("Researcher must source")
ERP = INP["equity_risk_premium_pct"] / 100                   # inputs: 5.0%
BETA_RAW = FJ["beta"]                                        # fj: 0.463

hdr("0. SNAPSHOT, FX, SHARE COUNT (tape check per RULE 0)")
print(f"Price of record US${P_USD:.4f}/ADS (inputs, intraday 13:52Z) | close US${P_USD_CLOSE} (dossier S1; "
      f"fj {FJ['price']}) | CNYUSD {FX:.8f} | SGDUSD {SGDUSD:.6f} (inputs)")
print(f"=> CNY {P_CNY:.3f} per ordinary share (record) / {P_CNY_CLOSE:.3f} (close) | CNY {P_CNY*ADS:.2f}/ADS "
      f"| S${to_sgd(P_USD):.2f}/ADS")
print(f"Shares: HKEX issued {SH:,.1f}m (= {SH/ADS:,.1f}m ADS) USED | GAAP basic+placing {SH_GAAP_BASIC:,}m | "
      f"diluted+placing {SH_DIL:,}m | sec_facts dei 1,858m REJECTED (1/10 error, orchestrator note)")
print(f"Market cap CNY {MCAP:,.0f}m = US${MCAP*FX/1e3:,.1f}bn (fj US${FJ['market_cap_usd']/1e9:,.1f}bn at close)")
print(f"Tape: 12m -33.7% (US$166.81 -> 110.535, dossier S1); 52w closing low 94.81 (2026-06-26); "
      f"fj trailing P/E {FJ['trailing_pe']:.2f}, forward {FJ['forward_pe']:.2f}")
print(f"fj warnings ({len(FJ['warnings'])}): {FJ['warnings']} | errors: {FJ['errors']}")
print("Price discrepancy to flag: orchestrator note quotes a 110.85 raw close; dossier/fj say 110.535/110.53. "
      "Model uses inputs 109.6351; close shown alongside.")

# =============================================================== 1. history
hdr("1. HISTORY FY21-FY26 (CNY m; facts.json annual + researcher_additions; dossier S2)")
rev, cor, ebit = ann("revenue"), ann("cost_of_revenue"), ann("operating_income")
ni, da_x, sbc, ocf = ann("net_income"), ann("d_and_a"), ann("sbc"), ann("ocf")
cash, eq, gw, recv = ann("cash"), ann("equity"), ann("goodwill"), ann("receivables")
intexp = ann("interest_expense")
eps = [A["eps_diluted"][y]["val"] for y in YE]
capex = [RA["capex_total_incl_intangibles"][f"FY20{y[2:4]}"]["val"] for y in YE]
debt = [RA["debt_financial_excl_leases"][y] for y in YE]
inv = [RA["inventories"][y] for y in YE]
leases = [RA["operating_lease_liabilities"][y] for y in YE]
etr = [DV[y]["effective_tax_rate"] for y in YE]
tax_roic = [DV[y]["roic_tax_rate_used"] for y in YE]
gm = [1 - c / r for c, r in zip(cor, rev)]
om = [e / r for e, r in zip(ebit, rev)]
fcf = [o - c for o, c in zip(ocf, capex)]
ic = [e + d - c for e, d, c in zip(eq, debt, cash)]           # facts formula: equity + debt - cash
nopat = [e * (1 - t) for e, t in zip(ebit, tax_roic)]
roic = [n / i for n, i in zip(nopat, ic)]
print(f"{'':<40}" + "".join(f"{l:>10}" for l in LBL))
row("Revenue", rev, "{:>10,.0f}")
row("Revenue YoY", [None] + [rev[i] / rev[i - 1] - 1 for i in range(1, 6)])
row("Gross margin", gm)
row("GAAP EBIT margin", om)
row("Effective tax rate (facts)", etr)
row("SBC / revenue", [s / r for s, r in zip(sbc, rev)])
row("D&A (XBRL) / revenue", [d / r for d, r in zip(da_x, rev)])
row("Capex incl. intangibles / revenue", [c / r for c, r in zip(capex, rev)])
row("Capex / D&A (XBRL)", [c / d for c, d in zip(capex, da_x)], "{:>10.2f}")
row("FCF (OCF - capex)", fcf, "{:>10,.0f}")
row("FCF margin", [f / r for f, r in zip(fcf, rev)])
row("Invested capital (eq+debt-cash)", ic, "{:>10,.0f}")
row("ROIC (GAAP EBIT x (1-t) / IC)", roic)
row("Goodwill / IC", [g / i for g, i in zip(gw, ic)])
row("Diluted EPS (CNY/share)", eps, "{:>10.2f}")
row("Inventory growth - sales growth", [None] + [None if inv[i] is None else
    (inv[i] / inv[i - 1] - 1) - (rev[i] / rev[i - 1] - 1) for i in range(1, 6)], "{:>+10.1%}")
row("Receivables growth - sales growth", [None] + [(recv[i] / recv[i - 1] - 1) - (rev[i] / rev[i - 1] - 1)
                                                   for i in range(1, 6)], "{:>+10.1%}")
row("EBIT / interest (facts)", [DV[y]["interest_coverage"] for y in YE], "{:>10.1f}")
L5 = slice(1, 6)                                              # FY22..FY26 (5 most recent)
FCFM5 = [f / r for f, r in zip(fcf[L5], rev[L5])]
print(f"5-yr FY22-26: GM avg {avg(gm[L5]):.1%} (low {min(gm[L5]):.1%}, high {max(gm[L5]):.1%}) | GAAP EBIT margin "
      f"avg {avg(om[L5]):.1%} (low {min(om[L5]):.1%}, high {max(om[L5]):.1%}) | FCF margin avg {avg(FCFM5):.1%} "
      f"| ROIC avg {avg(roic[L5]):.1%}")
print(f"FY21-25 FCF margin avg {avg([f / r for f, r in zip(fcf[0:5], rev[0:5])]):.1%} (pre-AI-capex era)")
REV_CAGR = F["revenue_cagr"]
EPS_CAGR = (eps[5] / eps[0]) ** (1 / 5) - 1
print(f"Revenue CAGR FY21-26 {REV_CAGR:.2%} (facts) | GAAP diluted EPS CAGR FY21-26 = (5.50/6.84)^(1/5)-1 = "
      f"{EPS_CAGR:+.2%} | diluted share CAGR {F['diluted_share_cagr']:+.2%} (facts)")
ADJ_EBITA = {"FY25": 173065, "FY26": 76416, "TTM": 64901}     # dossier S2
NG_NI = {"FY25": 158122, "FY26": 60658, "TTM": 47863}         # dossier S2 non-GAAP NI
SBC_D = {"FY25": 13970, "FY26": 11180, "TTM": 10948}
REV_D = {"FY25": rev[4], "FY26": rev[5], "TTM": 1044971}
for k in ADJ_EBITA:
    print(f"  {k}: adj EBITA {ADJ_EBITA[k]:,} ({ADJ_EBITA[k]/REV_D[k]:.1%}) | less SBC = "
          f"{(ADJ_EBITA[k]-SBC_D[k])/REV_D[k]:.1%} of revenue  <- model EBIT definition")
print("  FY21-FY24 adjusted EBITA: UNKNOWN (dossier S10 m) -> 5-yr range on the model definition not available;"
      " GAAP EBIT range used as the proxy")

# =============================================================== 2. TTM base & engines
hdr("2. TTM (Jul-25..Jun-26) BASE AND TWO-ENGINE SPLIT (facts add. ttm_jun2026_derived; dossier S3/S8)")
T = RA["ttm_jun2026_derived"]
REV0 = T["revenue"]                                           # 1,044,971
EBITA0 = T["adj_ebita"]                                       # 64,901
D0 = T["adj_ebitda"] - T["adj_ebita"]                         # 41,990 depreciation [DERIVED]
CAPEX0 = T["capex"]                                           # 155,065
SBC_PCT = T["sbc_noncash"] / REV0                             # 1.05%
Q1 = RA["q1_fy27_quarter"]
CLOUD_Q1, CLOUD_Q1_PY = 48437, 48437 / 1.45                   # dossier S3: +45% y/y (prior derived)
CLOUD_EBITA_Q1, CLOUD_EBITA_Q1_PY = 5628, 2419                # dossier S3
CLOUD_FY26, CLOUD_EBITA_FY26 = 158132, 14265                  # dossier S8 (OLD structure, perimeter caveat)
CLOUD0 = CLOUD_FY26 - CLOUD_Q1_PY + CLOUD_Q1                  # TTM cloud revenue [DERIVED]
CLOUD_EBITA0 = CLOUD_EBITA_FY26 - CLOUD_EBITA_Q1_PY + CLOUD_EBITA_Q1
CORE0 = REV0 - CLOUD0
CORE_EBITA0 = EBITA0 - CLOUD_EBITA0
CORE_CX = 0.025                                               # ASSUMPTION: non-cloud capex 2.5% of non-cloud rev
print(f"TTM revenue {REV0:,} | adj EBITA {EBITA0:,} ({EBITA0/REV0:.1%}) | adj EBITDA {T['adj_ebitda']:,} | "
      f"depreciation (EBITDA-EBITA) {D0:,} ({D0/REV0:.1%}) | capex {CAPEX0:,} ({CAPEX0/REV0:.1%}) | "
      f"SBC {T['sbc_noncash']:,} ({SBC_PCT:.2%})")
print(f"Cloud TTM revenue = FY26 158,132 - Q1FY26 {CLOUD_Q1_PY:,.0f} + Q1FY27 48,437 = {CLOUD0:,.0f} "
      f"({CLOUD0/REV0:.1%}); EBITA {CLOUD_EBITA0:,.0f} ({CLOUD_EBITA0/CLOUD0:.1%}). Q1FY27 run-rate x4 = "
      f"{CLOUD_Q1*4:,} at {CLOUD_EBITA_Q1/CLOUD_Q1:.1%}. CAVEAT: FY26 is old 'Cloud Intelligence' perimeter.")
print(f"Non-cloud TTM revenue {CORE0:,.0f} | EBITA {CORE_EBITA0:,.0f} ({CORE_EBITA0/CORE0:.1%}); Q1FY27 non-cloud "
      f"{(Q1['adj_ebita']-CLOUD_EBITA_Q1)/(Q1['revenue']-CLOUD_Q1):.1%}, Q1FY26 "
      f"{(38844-CLOUD_EBITA_Q1_PY)/(Q1['revenue_prior_year']-CLOUD_Q1_PY):.1%}; non-cloud rev growth Q1 y/y "
      f"{(Q1['revenue']-CLOUD_Q1)/(Q1['revenue_prior_year']-CLOUD_Q1_PY)-1:+.1%}")
print(f"  of which AI Labs Q1FY27 EBITA -13,861 (annualised {-13861*4:,}); non-cloud ex-AI-Labs Q1 margin "
      f"{(Q1['adj_ebita']-CLOUD_EBITA_Q1+13861)/(Q1['revenue']-CLOUD_Q1-3338):.1%}")
cloud_cx0 = (CAPEX0 - CORE_CX * CORE0) / CLOUD0
print(f"Implied TTM cloud capex intensity = (155,065 - 2.5% x non-cloud) / cloud rev = {cloud_cx0:.0%}")
ttm_fcf_model = (EBITA0 - T["sbc_noncash"]) * (1 - st.median(etr)) + D0 - CAPEX0
print(f"Model FCF identity on TTM: (EBITA - SBC) x (1 - median ETR) + depreciation - capex = {ttm_fcf_model:,.0f} vs "
      f"actual OCF - capex {T['ocf_minus_capex']:,} / company FCF {T['fcf_company']:,} -> identity reconciles within "
      f"{abs(ttm_fcf_model - T['ocf_minus_capex']):,.0f}")
DEP_K = 1 / 6                                                 # ASSUMPTION: depreciation catches up 1/6 per yr
cal = 24515 + (85972 - 24515) * DEP_K
print(f"Depreciation roll D_t = D_t-1 + (capex_t-1 - D_t-1)/6. Calibration: FY25 D&A 24,515 + (FY25 capex 85,972"
      f" - 24,515)/6 = {cal:,.0f} vs FY26 actual XBRL 34,963 ({cal/34963-1:+.1%})")

# =============================================================== 3. bridge
hdr("3. EV -> EQUITY BRIDGE (Jun-26 balance sheet, rolled to 2026-10-13)")
BASE_END, VAL_DATE = date(2026, 6, 30), date(2026, 10, 13)
STUB = (VAL_DATE - BASE_END).days / 365.25
LIQ, DEBT_J = 474505, 266530                                  # dossier S1 (6-K 0001104659-26-099220)
NET_CASH = LIQ - DEBT_J
PLACING = 79785 / 7.8476 / FX                                 # HK$m -> US$m (dossier S1 rate) -> CNY m
DIV_FY26 = 2500 / FX                                          # dossier S5: ~US$2.5bn, payable ~13 Jul 2026
NCI, MEZZ = 57272, 7584                                       # dossier S1 (Jun-26 book)
EQM, OTH_INV = 203207, 254210                                 # dossier S1/S5 (book)
INV_BOOK = EQM + OTH_INV
NET_CASH_ADJ = NET_CASH + PLACING - DIV_FY26 - NCI - MEZZ
print(f"Stub {BASE_END} -> {VAL_DATE} = {STUB:.4f} yrs (mid-year on)")
print(f"Cash & liquid investments {LIQ:,} - financial debt {DEBT_J:,} = net cash {NET_CASH:,} "
      f"(US${NET_CASH*FX/1e3:.1f}bn)")
print(f"+ placing HK$79,785m / 7.8476 / CNYUSD = CNY {PLACING:,.0f} | - FY26 dividend US$2.5bn = CNY {DIV_FY26:,.0f}"
      f" (alt: 1.05 x 2,322.5m ADS = US${1.05*2322.5:,.0f}m) | - NCI {NCI:,} - mezzanine {MEZZ:,}")
print(f"= adjusted net cash {NET_CASH_ADJ:,.0f} = CNY {NET_CASH_ADJ/SH:.2f}/share = US${to_ads(NET_CASH_ADJ/SH):.2f}/ADS")
print(f"Investment book (equity-method {EQM:,} + other {OTH_INV:,}) = {INV_BOOK:,} = CNY {INV_BOOK/SH:.2f}/share = "
      f"US${to_ads(INV_BOOK/SH):.2f}/ADS at book; each 10pp of haircut = US${to_ads(0.1*INV_BOOK/SH):.2f}/ADS")
for h in (0.0, 0.15, 0.30, 0.50):
    tot = NET_CASH_ADJ + INV_BOOK * (1 - h)
    print(f"  haircut {h:.0%}: net cash + investments = {tot:,.0f} = US${to_ads(tot/SH):.2f}/ADS "
          f"({tot/MCAP:.1%} of market cap)")
print("Excluded: operating leases 21,726 (in EBITA), restricted cash 42,585, supplier finance 15,361 (operating), "
      "Jul-26 buybacks (~US$0.2-0.4bn, immaterial)")
CB_GAP = (5000 / 12.5222) * (P_USD / ADS) - 5000              # dossier S1: conv. price US$12.5222/share
print(f"May-24 convertible US$5.0bn at US$12.5222/share: conversion value - face = US${CB_GAP:,.0f}m "
      f"(= US${CB_GAP/(SH/ADS):.2f}/ADS understatement if treated as debt; immaterial). Dossier's 519.1m shares "
      f"implies US${5000/519.1:.2f}/share, inconsistent with 12.5222 -> open question")
EV_TOTAL = MCAP - NET_CASH_ADJ                                # EV incl. investments (NCI & mezz added)
EV_OPER = EV_TOTAL - INV_BOOK                                 # EV ex investment book at book
print(f"Market EV (mcap - adjusted net cash) = {EV_TOTAL:,.0f} = US${EV_TOTAL*FX/1e3:.1f}bn | ex investment book = "
      f"{EV_OPER:,.0f} = US${EV_OPER*FX/1e3:.1f}bn (dossier pre-NCI EV US$243.9bn / pro forma 233.7bn)")

# =============================================================== 4. owner earnings, Lynch
hdr("4. OWNER EARNINGS, LYNCH METRICS, DIVIDEND, DEBT")
NI26_FJ = FJ["net_income"] / 1e6                              # 102,127 incl. NCI
OE_FJ = FJ["owner_earnings"] / 1e6                            # 22,308 (fj, D&A 47,118)
OE_X = ni[5] + da_x[5] - capex[5]
OE_CO = ni[5] + 42146 - capex[5]                              # company recon D&A (dossier S10.3)
print(f"AGENTS.md owner earnings FY26 = NI + D&A - capex:")
print(f"  fj: {NI26_FJ:,.0f} + 47,118 - 126,937 = {OE_FJ:,.0f} -> yield {OE_FJ/MCAP:.2%}; SBC-adj "
      f"{OE_FJ-sbc[5]:,.0f} -> {(OE_FJ-sbc[5])/MCAP:.2%}")
print(f"  XBRL D&A: {ni[5]:,.0f} + {da_x[5]:,.0f} - {capex[5]:,.0f} = {OE_X:,.0f} -> {OE_X/MCAP:.2%}; SBC-adj "
      f"{OE_X-sbc[5]:,.0f} -> {(OE_X-sbc[5])/MCAP:.2%}")
print(f"  company D&A 42,146: {OE_CO:,.0f} -> {OE_CO/MCAP:.2%}")
print("  ALL OF THE ABOVE contain ~RMB 74bn FY26 investment revaluation/disposal gains (dossier S5) -> unreliable.")
OE_OP = {}
for k, dep, cx in (("FY26", 37067, capex[5]), ("TTM", D0, CAPEX0)):
    base = NG_NI[k] - SBC_D[k]
    OE_OP[k] = (base, base + dep - cx)
    print(f"Operating owner earnings {k} = (non-GAAP NI {NG_NI[k]:,} - SBC {SBC_D[k]:,}) + depreciation {dep:,} - "
          f"capex {cx:,} = {base+dep-cx:,.0f} -> yield {(base+dep-cx)/MCAP:+.2%}")
    print(f"  maintenance-capex view (capex = depreciation, growth capex excluded): {base:,.0f} -> "
          f"{base/MCAP:.2%}")
print(f"  FY25 (pre quick-commerce war), same view: {NG_NI['FY25']-SBC_D['FY25']:,} -> "
      f"{(NG_NI['FY25']-SBC_D['FY25'])/MCAP:.2%} on today's market cap")

NI_TTM_ORD = T["net_income_ord"]                              # 73,325
PE_TTM = MCAP / NI_TTM_ORD
PE_FY26 = P_CNY / eps[5]
PE_NG_TTM = MCAP / NG_NI["TTM"]
PE_NG_SBC = MCAP / (NG_NI["TTM"] - SBC_D["TTM"])
CONS27, CONS28 = 44.35, 62.15                                 # dossier S9 CONSENSUS non-GAAP EPS/ADS, RMB
PE_C27, PE_C28 = P_CNY * ADS / CONS27, P_CNY * ADS / CONS28
NG_EPS26_ADS = 26.80                                          # dossier S9
CONS_G = (CONS28 / NG_EPS26_ADS) ** 0.5 - 1
print(f"\nP/E: TTM GAAP (mcap / NI to ordinary {NI_TTM_ORD:,}) {PE_TTM:.1f}x | FY26 GAAP (CNY {P_CNY:.2f} / EPS 5.50) "
      f"{PE_FY26:.1f}x | fj trailing {FJ['trailing_pe']:.1f}x | TTM non-GAAP {PE_NG_TTM:.1f}x | TTM non-GAAP less SBC "
      f"{PE_NG_SBC:.1f}x")
print(f"     CONSENSUS forward (non-GAAP EPS/ADS): FY27E {CONS27} -> {PE_C27:.1f}x | FY28E {CONS28} -> {PE_C28:.1f}x "
      f"(fj forward {FJ['forward_pe']:.1f}x matches the FY28E basis)")
G_LOW = min(EPS_CAGR, CONS_G)
ok, why = peg_is_valid(PE_TTM, FJ["forward_pe"], G_LOW)
print(f"PEG gate: P/E {PE_TTM:.1f}, fwd {FJ['forward_pe']:.1f}, growth = lower of historical GAAP EPS CAGR "
      f"{EPS_CAGR:+.1%} and CONSENSUS FY26->FY28 non-GAAP EPS CAGR {CONS_G:+.1%} = {G_LOW:+.1%} -> "
      f"{'VALID' if ok else 'VOID'} ({why}). fj peg 0.52 'valid' NOT cited.")
DY = 1.05 / P_USD                                             # dossier S5: FY26 US$1.05/ADS regular
LYN = (G_LOW * 100 + DY * 100) / PE_TTM
LYN_C = (CONS_G * 100 + DY * 100) / PE_TTM
print(f"Dividend yield = 1.05 / {P_USD:.2f} = {DY:.2%}")
print(f"Lynch ratio = (EPS growth {G_LOW*100:+.1f} + DY {DY*100:.2f}) / P/E {PE_TTM:.1f} = {LYN:.2f}  [rule: lower growth]")
print(f"  (not used: with CONSENSUS growth {CONS_G*100:.1f}: {LYN_C:.2f} - the entire Lynch case rests on the "
      f"consensus rebound; it mixes non-GAAP growth with a GAAP P/E)")
NC_PS = NET_CASH_ADJ / SH
NCI_PS = (NET_CASH_ADJ + INV_BOOK * 0.7) / SH
for lab, e in (("TTM GAAP", NI_TTM_ORD / SH), ("TTM non-GAAP less SBC", (NG_NI['TTM'] - SBC_D['TTM']) / SH),
               ("FY25 non-GAAP less SBC", (NG_NI['FY25'] - SBC_D['FY25']) / SH)):
    print(f"Net-cash-adj P/E [{lab}] = ({P_CNY:.2f} - {NC_PS:.2f}) / {e:.3f} = {(P_CNY-NC_PS)/e:.1f}x | also ex "
          f"investments @70% of book: ({P_CNY:.2f} - {NCI_PS:.2f}) / {e:.3f} = {(P_CNY-NCI_PS)/e:.1f}x")
DIV_CASH26 = A["dividends_paid"][YE[5]]["val"] / 1e6
print(f"Dividend FY26 cash paid {DIV_CASH26:,.0f} (incl. FY25 special) vs FCF {fcf[5]:,.0f} -> NOT covered by FCF; "
      f"payout of GAAP NI {DIV_CASH26/NI26_FJ:.0%}, of non-GAAP NI {DIV_CASH26/NG_NI['FY26']:.0%}. Regular FY26 "
      f"dividend ~{DIV_FY26:,.0f} = {DIV_FY26/(NG_NI['TTM']-SBC_D['TTM']):.0%} of TTM non-GAAP NI less SBC")
print(f"Debt: net cash {NET_CASH:,} -> net debt / owner earnings NEGATIVE (net cash) | gross debt {DEBT_J:,} vs "
      f"liquid {LIQ:,} = {LIQ/DEBT_J:.2f}x cover | current bank 30,614 | senior-note maturities (FY25 20-F, "
      f"stale): Y1 0, Y2 0, Y3 18,492, Y4 8,400, Y5 5,000, after 91,344 | US$5bn CB holder put 1 Jun 2029")
print(f"Interest cover: FY26 GAAP EBIT/interest {DV[YE[5]]['interest_coverage']:.1f}x (facts); TTM EBIT 30,323 / FY26 "
      f"interest {intexp[5]:,.0f} = {30323/intexp[5]:.1f}x (TTM interest UNKNOWN). Debt CAGR FY22->Jun26 "
      f"{(DEBT_J/debt[1])**(1/4.25)-1:+.1%}/yr")

# =============================================================== 5. multiples
hdr("5. MULTIPLES MATRIX (CNY basis; peer column = dossier S7 vendor values)")
peers = {k: FJALL[k] for k in ("PDD", "JD", "BIDU", "TCEHY")}
pe_t = [v["trailing_pe"] for v in peers.values() if v["trailing_pe"]]
pe_f = [v["forward_pe"] for v in peers.values() if v["forward_pe"]]
fcfy = [v["fcf_usd"] / v["market_cap_usd"] for v in peers.values()]
print(f"China peers PDD/JD/BIDU/TCEHY: trailing P/E median {st.median(pe_t):.1f}x (BIDU n/a) | forward "
      f"{st.median(pe_f):.1f}x | FCF yield {st.median(fcfy):.1%} | EV/EBITDA UNKNOWN (currency-mixed vendor EV)")
amz = FJALL["AMZN"]
EBITDA_SBC = T["adj_ebitda"] - T["sbc_noncash"]
fcf_ttm = T["ocf_minus_capex"]
mm = [
    ("EV/EBITDA TTM adj (EV incl. investments)", f"{EV_TOTAL/T['adj_ebitda']:.1f}x", "UNKNOWN"),
    ("EV/EBITDA TTM adj less SBC", f"{EV_TOTAL/EBITDA_SBC:.1f}x", "UNKNOWN"),
    ("EV ex-investments / EBITDA less SBC", f"{EV_OPER/EBITDA_SBC:.1f}x", "UNKNOWN"),
    ("EV ex-investments / EBITA less SBC (TTM)", f"{EV_OPER/(EBITA0-T['sbc_noncash']):.1f}x", "UNKNOWN"),
    ("P/E trailing TTM GAAP", f"{PE_TTM:.1f}x", f"{st.median(pe_t):.1f}x"),
    ("P/E trailing TTM non-GAAP less SBC", f"{PE_NG_SBC:.1f}x", "-"),
    ("P/E forward CONSENSUS FY27E / FY28E", f"{PE_C27:.1f}x / {PE_C28:.1f}x", f"{st.median(pe_f):.1f}x"),
    ("P/FCF TTM (OCF-capex -76,579)", "n/m (negative)", f"{1/st.median(fcfy):.1f}x"),
    ("P/FCF SBC-adjusted", "n/m (negative)", "-"),
    ("FCF yield TTM (OCF-capex)", f"{fcf_yield(fcf_ttm, MCAP):+.2%}", f"{st.median(fcfy):.1%}"),
    ("FCF yield FY26 (OCF-capex)", f"{fcf_yield(fcf[5], MCAP):+.2%}", "-"),
    ("FCF yield TTM company definition", f"{fcf_yield(T['fcf_company'], MCAP):+.2%}", "-"),
    ("Owner-earnings yield TTM operating", f"{OE_OP['TTM'][1]/MCAP:+.2%}", "-"),
    ("Owner-earnings yield, capex=depreciation", f"{OE_OP['TTM'][0]/MCAP:.2%}", "-"),
    ("Owner-earnings yield FY26 fj (incl. gains)", f"{OE_FJ/MCAP:.2%}", "-"),
    ("PEG", "VOID (not cited)", "-"),
    ("Lynch ratio (lower growth)", f"{LYN:.2f}", "-"),
    ("Dividend yield", f"{DY:.2%}", "-"),
]
for a_, b_, c_ in mm:
    print(f"{a_:<46}{b_:>22}   peer median: {c_}")
print(f"AMZN (cloud comp, USD): trailing P/E {amz['trailing_pe']:.1f}x, forward {amz['forward_pe']:.1f}x, FCF yield "
      f"{amz['fcf_usd']/amz['market_cap_usd']:.1%}")
print("5-yr own-average column: UNKNOWN (dossier holds no historical price series; buyback average prices exist "
      "but historical FX does not)")

# =============================================================== 6. discount rate
hdr("6. DISCOUNT RATE (USD opportunity cost applied to CNY flows at flat spot)")
BETA = 0.67 * BETA_RAW + 0.33
KE = RF_USD + BETA * ERP
KD_HIST = intexp[5] / ((debt[4] + debt[5]) / 2)
KD_PRE = max(KD_HIST, RF_USD)                                 # ASSUMPTION: USD issuer not below UST; spread UNKNOWN
TAX = st.median(etr)                                          # median FY21-26 ETR (facts)
KD = KD_PRE * (1 - TAX)
E_W, D_W = MCAP, DEBT_J
WACC_RAW = (E_W * KE + D_W * KD) / (E_W + D_W)
WACC = max(WACC_RAW, 0.08)
WACC_CNY_FLOOR = RF_CNY + 0.04
WACC_IRP = (1 + WACC) * (1 + RF_CNY) / (1 + RF_USD) - 1
print(f"Beta: fj raw {BETA_RAW} -> Blume 0.67 x {BETA_RAW} + 0.33 = {BETA:.3f} (vs S&P; low correlation, not low risk)")
print(f"Ke = USD 10y {RF_USD:.2%} + {BETA:.3f} x ERP {ERP:.0%} = {KE:.2%}")
print(f"Kd pre-tax = max(FY26 interest {intexp[5]:,.0f} / avg debt {(debt[4]+debt[5])/2:,.0f} = {KD_HIST:.2%}, USD 10y "
      f"{RF_USD:.2%}) = {KD_PRE:.2%}; after tax @ median ETR {TAX:.1%} = {KD:.2%}")
print(f"Weights (market equity, book debt as proxy): E {E_W/(E_W+D_W):.1%} / D {D_W/(E_W+D_W):.1%}")
print(f"WACC (CAPM) = {WACC_RAW:.2%}; USD floor 8.00% -> USED {WACC:.2%} ({'floor binds' if WACC_RAW < 0.08 else 'CAPM'})")
print(f"Cross-checks: CNY CAPM Ke = {RF_CNY:.2%} + {BETA:.3f} x 5% = {RF_CNY+BETA*ERP:.2%}; CNY floor (10y + 4%) "
      f"= {WACC_CNY_FLOOR:.2%}; IRP translation of {WACC:.2%} USD into CNY = {WACC_IRP:.2%} -> below CNY floor, "
      f"so the CNY-consistent rate would be {max(WACC_IRP, WACC_CNY_FLOOR):.2%}")
print(f"=> Using {WACC:.2%} on CNY flows embeds ~{WACC-max(WACC_IRP, WACC_CNY_FLOOR):.2%}/yr over the CNY-consistent "
      f"rate: this is the (unsourced) China/VIE/CMC-list/capital-control premium, stated not hidden.")
print(f"Terminal g cap = min(4%, cash-flow-currency 10y {RF_CNY:.2%}) = {min(0.04, RF_CNY):.2%}")
print("Staleness: USD 10y dated 2026-10-08 (5 days before price); CNY 10y via [FETCH] summariser.")

# =============================================================== 7. scenarios
hdr("7. DCF SCENARIOS (10 yr Jul-26..Jun-36, FCFF, CNY; mid-year; stub-dated 2026-10-13)")
N = 10
YRS = [f"J{27+i}" for i in range(N)]                         # year ending June
SCEN = {
    # BEAR: AI price war / overcapacity -> cloud growth halves fast and EBITA margin compresses as the
    # depreciation wave lands; capex stays committed; China e-com keeps losing CMR (-7% Q1) to PDD/Douyin,
    # quick commerce never reaches profit -> non-cloud margin stays near the TTM 5.4% / FY26 GAAP 4.9% low;
    # China consumption soft in Y1-2 (growth 0/-1%).
    "BEAR": dict(g_cloud=[.25, .15, .10, .08, .06, .05, .04, .03, .03, .03],
                 g_core=[.00, -.01, .00, .01, .01, .01, .01, .01, .01, .01],
                 m_cloud=[.09, .08, .07, .07, .07, .07, .07, .07, .07, .07],
                 m_core=[.055, .06, .07, .075, .08, .08, .08, .08, .08, .08],
                 cx_cloud=[.70, .60, .50, .40, .35, .30, .30, .30, .30, .30],
                 tg=0.005, roic=0.08, haircut=0.50),
    # BASE: no formal guidance exists (dossier S3). Cloud decelerates from +45% to 35% and fades, below the
    # mgmt US$100bn-external-cloud-by-2030 target; cloud EBITA 11.6% (Q1) drifting to 13% (mgmt '20% gross
    # margin' caps it); non-cloud recovers from Q1 FY27 9.8% as quick commerce reaches profit (mgmt: FY29)
    # and AI Labs losses narrow (mgmt) - to 14%, still below FY25's ~16-17%; capex per the RMB380bn plan
    # remainder + placing (~165-180bn/yr) then intensity fades to 25% of cloud revenue.
    "BASE": dict(g_cloud=[.35, .30, .25, .20, .15, .12, .10, .08, .06, .05],
                 g_core=[.03, .03, .03, .03, .025, .025, .02, .02, .02, .02],
                 m_cloud=[.115, .12, .125, .13, .13, .13, .13, .13, .13, .13],
                 m_core=[.085, .105, .125, .135, .14, .14, .14, .14, .14, .14],
                 cx_cloud=[.65, .50, .40, .33, .28, .25, .25, .25, .25, .25],
                 tg=0.015, roic=0.12, haircut=0.30),
    # BULL: mgmt cloud target met (CNY ~668bn external by 2030; 9 quarters of accelerating growth; price rises
    # on renewals; 38.1% China AI-cloud share, Omdia); cloud EBITA to 15.5% (just under the 20% GM visibility);
    # non-cloud back to the FY25 level ~17.5% (quick commerce profitable FY29, AliExpress already profitable,
    # CMR like-for-like back to the March-quarter +8%); capex intensity falls faster (2.5-yr payback claim).
    "BULL": dict(g_cloud=[.45, .40, .35, .30, .25, .18, .14, .10, .08, .06],
                 g_core=[.05, .05, .045, .04, .04, .035, .03, .03, .025, .025],
                 m_cloud=[.12, .13, .14, .15, .155, .155, .155, .155, .155, .155],
                 m_core=[.095, .12, .145, .165, .175, .175, .175, .175, .175, .175],
                 cx_cloud=[.60, .45, .35, .28, .24, .22, .22, .22, .22, .22],
                 tg=0.0167, roic=0.16, haircut=0.15),
}


def build(s, wacc=None, tax=None, sbc=None, core_cx=None, k=None, cloud0=None, inv_mult=1.0, nc_mult=1.0):
    wacc = WACC if wacc is None else wacc
    tax = TAX if tax is None else tax
    sbc = SBC_PCT if sbc is None else sbc
    core_cx = CORE_CX if core_cx is None else core_cx
    k = DEP_K if k is None else k
    rc = CLOUD0 if cloud0 is None else cloud0
    rk = REV0 - rc
    d_prev, cx_prev, rev_prev = D0, CAPEX0, REV0
    g, em, dp, cp, diag = [], [], [], [], []
    for i in range(N):
        rc *= 1 + s["g_cloud"][i]
        rk *= 1 + s["g_core"][i]
        rv = rc + rk
        eb = rc * s["m_cloud"][i] + rk * s["m_core"][i] - sbc * rv
        cx = rc * s["cx_cloud"][i] + rk * core_cx
        d = d_prev + (cx_prev - d_prev) * k
        g.append(rv / rev_prev - 1)
        em.append((eb + d) / rv)
        dp.append(d / rv)
        cp.append(cx / rv)
        diag.append(dict(cloud=rc, core=rk, ebit_m=eb / rv, cloud_share=rc / rv))
        rev_prev, d_prev, cx_prev = rv, d, cx
    claims = -(NET_CASH_ADJ * nc_mult + INV_BOOK * inv_mult * (1 - s["haircut"]))
    kw = dict(base_revenue=REV0, growth=g, ebitda_margin=em, capex_pct=cp, da_pct=dp, tax=tax, wacc=wacc,
              net_debt=claims, shares=SH, terminal_growth=s["tg"], terminal_roic=s["roic"],
              mid_year=True, stub_years=STUB)
    return kw, diag


RES = {}
for name, s in SCEN.items():
    kw, diag = build(s)
    r = dcf(**kw)
    RES[name] = (r, kw, diag)
    print(f"\n[{name} inputs]")
    for lab, key, f in (("cloud growth", "g_cloud", "{:>+7.0%}"), ("non-cloud growth", "g_core", "{:>+7.1%}"),
                        ("cloud EBITA %", "m_cloud", "{:>7.1%}"), ("non-cloud EBITA %", "m_core", "{:>7.1%}"),
                        ("cloud capex % cloud rev", "cx_cloud", "{:>7.0%}")):
        print(f"  {lab:<24}" + "".join(f.format(x) for x in s[key]))
    print(f"  tax {TAX:.1%} | SBC {SBC_PCT:.2%} of rev deducted | non-cloud capex {CORE_CX:.1%} | dep roll 1/6 | "
          f"g_T {s['tg']:.2%} | ROIC_T {s['roic']:.0%} | investments haircut {s['haircut']:.0%} | WACC {WACC:.2%}")
    print(f"{'Yr':<5}{'g':>7}{'Revenue':>11}{'cloud%':>7}{'EBIT%':>7}{'D&A%':>6}{'EBITDA%':>8}{'Capex':>9}"
          f"{'Capex%':>7}{'FCF':>9}{'FCF%':>7}{'PV':>9}")
    for (y, rv, ebd, ebi, d_, cx, fc, pv), gg, dg in zip(r.rows, kw["growth"], diag):
        print(f"{YRS[y-1]:<5}{gg:>+7.1%}{rv:>11,.0f}{dg['cloud_share']:>7.0%}{ebi/rv:>7.1%}{d_/rv:>6.1%}"
              f"{ebd/rv:>8.1%}{cx:>9,.0f}{cx/rv:>7.1%}{fc:>9,.0f}{fc/rv:>+7.1%}{pv:>9,.0f}")
    flag = "  <-- TV > 75% OF EV: FLAG" if r.terminal_share > 0.75 else ""
    rv10 = r.rows[-1][1]
    nm_t = r.rows[-1][3] * (1 - TAX) / rv10
    print(f"10-yr revenue CAGR {(rv10/REV0)**0.1-1:+.2%} | Y10 revenue {rv10:,.0f} | terminal NOPAT margin {nm_t:.1%}, "
          f"FCF margin after g/ROIC reinvestment {nm_t*(1-s['tg']/s['roic']):.1%}")
    print(f"PV explicit {r.pv_explicit:,.0f} | PV terminal {r.pv_terminal:,.0f} ({r.terminal_share:.0%} of EV){flag}")
    print(f"EV {r.enterprise_value:,.0f} + net cash/investments {-kw['net_debt']:,.0f} = equity {r.equity_value:,.0f}"
          f" -> CNY {r.per_share:.2f}/share = US${to_ads(r.per_share):.2f}/ADS = S${to_sgd(to_ads(r.per_share)):.2f}"
          f"/ADS vs US${P_USD:.2f} ({r.upside(P_CNY):+.1%}); vs close {r.per_share/P_CNY_CLOSE-1:+.1%}")
    op_only = r.enterprise_value / SH
    print(f"  decomposition per ADS: operations US${to_ads(op_only):.2f} | adj. net cash US${to_ads(NET_CASH_ADJ/SH):.2f}"
          f" | investments US${to_ads(INV_BOOK*(1-s['haircut'])/SH):.2f}")
b0, bkw, bdg = RES["BASE"]
print(f"\nFCF-margin anchor: BASE Y6-Y10 FCF margin avg {avg([x[6]/x[1] for x in b0.rows[5:]]):.1%}; terminal "
      f"{b0.rows[-1][3]*(1-TAX)*(1-.015/.12)/b0.rows[-1][1]:.1%} vs 5-yr (FY22-26) avg {avg(FCFM5):.1%}, FY21-25 avg "
      f"{avg([f / r for f, r in zip(fcf[0:5], rev[0:5])]):.1%}")
print(f"Base Y10 cloud revenue {bdg[-1]['cloud']:,.0f} vs mgmt 2030 external-cloud target US$100bn = CNY {100000/FX:,.0f} "
      f"(base reaches it in {next((YRS[i] for i, d in enumerate(bdg) if d['cloud'] >= 100000/FX), 'never')})")
bull_dg = RES["BULL"][2]
print(f"Bull cloud reaches CNY {100000/FX:,.0f} in {next((YRS[i] for i, d in enumerate(bull_dg) if d['cloud'] >= 100000/FX), 'never')}")
print(f"Base Y1 revenue {b0.rows[0][1]:,.0f} (Jul-26..Jun-27) vs CONSENSUS FY27E (Apr-26..Mar-27) 1,118,300 - "
      f"comparison only, different period: {b0.rows[0][1]/1118300-1:+.1%}")
print(f"Base cumulative FCF Y1-Y3 {sum(x[6] for x in b0.rows[:3]):,.0f} vs adjusted net cash {NET_CASH_ADJ:,.0f}")

# =============================================================== 8. reverse DCF
hdr(f"8. REVERSE DCF (what must be true at US${P_USD:.2f} = CNY {P_CNY:.2f}/share)")
strip = lambda kw: {k: v for k, v in kw.items() if k not in ("base_revenue", "growth")}
g_imp = reverse_dcf(price=P_CNY, base_revenue=REV0, years=N, **strip(bkw))
print(f"BASE margin/D&A/capex paths held by year, WACC {WACC:.2%}, g 1.5%, ROIC 12%, investments @70%: implied "
      f"constant 10-yr revenue CAGR {g_imp:+.2%} (Y10 revenue {REV0*(1+g_imp)**10:,.0f}) vs base path "
      f"{(b0.rows[-1][1]/REV0)**0.1-1:+.2%}, FY21-26 actual {REV_CAGR:.2%}")
g_imp_c = reverse_dcf(price=P_CNY_CLOSE, base_revenue=REV0, years=N, **strip(bkw))
print(f"  at close price: {g_imp_c:+.2%}")
for lab, hc in (("investments at 0", None), ("investments at 100% of book", 0.0)):
    s2 = dict(SCEN["BASE"])
    if hc is None:
        kw2, _ = build(s2, inv_mult=0.0)
    else:
        s2["haircut"] = hc
        kw2, _ = build(s2)
    print(f"  {lab}: implied CAGR {reverse_dcf(price=P_CNY, base_revenue=REV0, years=N, **strip(kw2)):+.2%}")
kw_cny = {**strip(bkw), "wacc": max(WACC_IRP, WACC_CNY_FLOOR)}
print(f"  at CNY-consistent WACC {kw_cny['wacc']:.2%}: implied CAGR "
      f"{reverse_dcf(price=P_CNY, base_revenue=REV0, years=N, lo=-0.6, **kw_cny):+.2%}")
for nm in ("BEAR", "BULL"):
    print(f"  at {nm} margin/capex/terminal paths: implied CAGR "
          f"{reverse_dcf(price=P_CNY, base_revenue=REV0, years=N, **strip(RES[nm][1])):+.2%}")
print("  Caveat: early-year FCF is negative (capex); reverse_dcf scales it with growth, so the implied CAGR is "
      "mildly overstated. Hence the two scale solves below (rNPV-style).")


def solve(fn, lo, hi, target=P_CNY, it=60):
    for _ in range(it):
        mid = (lo + hi) / 2
        if fn(mid) < target:
            lo = mid
        else:
            hi = mid
    return mid


def core_m_val(mult):
    s2 = dict(SCEN["BASE"])
    s2["m_core"] = [x * mult for x in s2["m_core"]]
    return dcf(**build(s2)[0]).per_share


mc = solve(core_m_val, 0.0, 2.0)
print(f"Implied non-cloud EBITA path at BASE growth/cloud: base x {mc:.3f} -> steady-state {0.14*mc:.1%} "
      f"(base 14.0%; TTM {CORE_EBITA0/CORE0:.1%}; Q1FY27 9.8%)")


def cloud_g_val(mult):
    s2 = dict(SCEN["BASE"])
    s2["g_cloud"] = [x * mult for x in s2["g_cloud"]]
    return dcf(**build(s2)[0]).per_share


v_cg0 = cloud_g_val(0.0)
if v_cg0 >= P_CNY:
    print(f"Implied cloud growth: NO SOLUTION >= 0. With ZERO cloud growth (cloud flat at {CLOUD0:,.0f}, capex intensity "
          f"path unchanged so cloud capex shrinks with it) BASE = US${to_ads(v_cg0):.2f}/ADS, still >= price. At 13% "
          f"EBITA vs 25-65% capex/revenue, incremental cloud revenue is close to value-neutral in the explicit period; "
          f"the price is carried by the non-cloud margin and the balance sheet, not by cloud growth.")
    for mlt in (0.5, 1.0, 1.5):
        print(f"    cloud growth path x{mlt}: US${to_ads(cloud_g_val(mlt)):.2f}/ADS")
else:
    cg = solve(cloud_g_val, 0.0, 2.0)
    print(f"Implied cloud growth path at BASE everything else: base x {cg:.3f}")


def cloud_m_val(mult):
    s2 = dict(SCEN["BASE"])
    s2["m_cloud"] = [x * mult for x in s2["m_cloud"]]
    return dcf(**build(s2)[0]).per_share


cm = solve(cloud_m_val, -2.0, 3.0)
print(f"Implied cloud EBITA margin at BASE everything else: base x {cm:.3f} -> steady-state {0.13*cm:.1%} (base 13.0%)")

# =============================================================== 9. sensitivity
hdr("9. SENSITIVITY: BASE value by WACC x terminal growth (one grid; all else fixed)")
kw_s = {k: v for k, v in bkw.items() if k not in ("wacc", "terminal_growth")}
W3, G3 = [WACC - .01, WACC, WACC + .01], [0.005, 0.015, 0.025]
grid = sensitivity({"wacc": W3}, {"terminal_growth": G3}, **kw_s)
print("USD per ADS (CNY per share in brackets). g 2.5% breaches the CNY 1.67% cap; WACC 7% is below the 8% floor.")
print(f"{'WACC \\ g':<10}" + "".join(f"{g:>20.1%}" for g in G3))
for w, rr in zip(W3, grid):
    print(f"{w:<10.1%}" + "".join(f"{to_ads(v):>11.2f} ({v:>6.2f})" for v in rr))
W5, G5 = [0.0567, 0.07, 0.08, 0.09, 0.10, 0.11], [0.0, 0.005, 0.01, 0.015, 0.0167, 0.025, 0.035]
grid5 = sensitivity({"wacc": W5}, {"terminal_growth": G5}, **kw_s)
print("\nExtended grid, USD per ADS (5.67% = CNY-consistent rate; 3.5% g = USD-style cap region):")
print(f"{'WACC \\ g':<10}" + "".join(f"{g:>9.2%}" for g in G5))
for w, rr in zip(W5, grid5):
    print(f"{w:<10.2%}" + "".join(f"{to_ads(v):>9.2f}" for v in rr))
print("\nBASE value by WACC x terminal ROIC (g fixed 1.5%), USD per ADS:")
R5 = [0.08, 0.10, 0.12, 0.16, 0.20]
kw_r = {k: v for k, v in bkw.items() if k not in ("wacc", "terminal_roic")}
gridr = sensitivity({"wacc": W3}, {"terminal_roic": R5}, **kw_r)
print(f"{'WACC \\ ROIC':<12}" + "".join(f"{x:>9.0%}" for x in R5))
for w, rr in zip(W3, gridr):
    print(f"{w:<12.1%}" + "".join(f"{to_ads(v):>9.2f}" for v in rr))
print(f"\nOne-input lines on BASE: Ke-only 8.42% -> US${to_ads(dcf(**{**bkw, 'wacc': KE}).per_share):.2f}; "
      f"CNY-consistent {max(WACC_IRP, WACC_CNY_FLOOR):.2%} -> US$"
      f"{to_ads(dcf(**{**bkw, 'wacc': max(WACC_IRP, WACC_CNY_FLOOR)}).per_share):.2f} (WACC only moved)")
for lab, shc in (("GAAP basic + placing", SH_GAAP_BASIC), ("diluted + placing", SH_DIL)):
    print(f"Share-count line (base): {lab} {shc:,}m -> US${to_ads(dcf(**{**bkw, 'shares': shc}).per_share):.2f}/ADS")

Y1_CX_Q1 = 67678 * 4                                          # dossier S3: Q1 FY27 capex x4 (procurement-lumpy)
s_y1 = dict(SCEN["BASE"])
_, dg_y1 = build(s_y1)
need = (Y1_CX_Q1 - CORE_CX * dg_y1[0]["core"]) / dg_y1[0]["cloud"]
s_y1["cx_cloud"] = [need] + SCEN["BASE"]["cx_cloud"][1:]
r_y1 = dcf(**build(s_y1)[0])
r_y1s = dcf(**{**bkw, "capex_pct": build(s_y1)[0]["capex_pct"]})
print(f"Y1 capex at Q1FY27 run-rate {Y1_CX_Q1:,} (cloud intensity Y1 {need:.0%} vs 65%): US${to_ads(r_y1.per_share):.2f}/ADS "
      f"if later D&A (hence implied EBITDA) rises with it via the roll | STRICT, D&A path held = the extra "
      f"{Y1_CX_Q1-b0.rows[0][5]:,.0f} earns nothing: US${to_ads(r_y1s.per_share):.2f}/ADS (Y1 FCF {r_y1s.rows[0][6]:,.0f})")
print("  Model note: EBIT margins are the scenario input, so any change in the D&A path changes implied EBITDA 1:1."
      " Capex tests are therefore shown both ways; the strict (D&A-held) version is the honest one for overruns.")
for lab, m in (("non-cloud EBITA flat at Q1FY27 9.8%", 0.098), ("non-cloud EBITA flat at TTM 5.4%", CORE_EBITA0 / CORE0)):
    s2 = dict(SCEN["BASE"]); s2["m_core"] = [m] * N
    print(f"No-recovery line: {lab}: US${to_ads(dcf(**build(s2)[0]).per_share):.2f}/ADS")
for h in (0.0, 0.5, 1.0):
    s2 = dict(SCEN["BASE"]); s2["haircut"] = h
    print(f"Investment haircut {h:.0%} (base 30%): US${to_ads(dcf(**build(s2)[0]).per_share):.2f}/ADS")

# =============================================================== 10. load-bearing
hdr("10. LOAD-BEARING INPUTS: BASE per-ADS value, each input -10% / +10% (relative), all else fixed")
base_ps = b0.per_share


def val(**ov):
    s2 = dict(SCEN["BASE"])
    bargs = {}
    for k, v in ov.items():
        if k in s2:
            s2[k] = v
        else:
            bargs[k] = v
    kw2, _ = build(s2, **{k: v for k, v in bargs.items() if k not in ('wacc_direct',)})
    if "wacc_direct" in bargs:
        kw2["wacc"] = bargs["wacc_direct"]
    return dcf(**kw2).per_share


S = SCEN["BASE"]
scl = lambda key, m: [x * m for x in S[key]]


def val_cx_strict(cx_list):
    s2 = dict(SCEN["BASE"])
    s2["cx_cloud"] = cx_list
    return dcf(**{**bkw, "capex_pct": build(s2)[0]["capex_pct"]}).per_share


tests = [
    ("WACC 8.0% (inputs/floor)", lambda m: val(wacc_direct=WACC * m)),
    ("Non-cloud EBITA margin path", lambda m: val(m_core=scl("m_core", m))),
    ("Cloud EBITA margin path", lambda m: val(m_cloud=scl("m_cloud", m))),
    ("Cloud revenue growth path", lambda m: val(g_cloud=scl("g_cloud", m))),
    ("Non-cloud revenue growth path", lambda m: val(g_core=scl("g_core", m))),
    ("Cloud capex intensity path", lambda m: val(cx_cloud=scl("cx_cloud", m))),
    ("Cloud capex intensity, D&A held (strict)", lambda m: val_cx_strict(scl("cx_cloud", m))),
    ("Tax rate 22.5% (median ETR)", lambda m: val(tax=TAX * m)),
    ("Terminal growth 1.5%", lambda m: val(tg=S["tg"] * m)),
    ("Terminal ROIC 12%", lambda m: val(roic=S["roic"] * m)),
    ("Investment book value (at 70%)", lambda m: val(inv_mult=m)),
    ("Adjusted net cash", lambda m: val(nc_mult=m)),
    ("Non-cloud capex 2.5% of rev", lambda m: val(core_cx=CORE_CX * m)),
    ("SBC 1.05% of revenue", lambda m: val(sbc=SBC_PCT * m)),
    ("Depreciation catch-up rate 1/6", lambda m: val(k=DEP_K * m)),
    ("TTM cloud revenue base (perimeter)", lambda m: val(cloud0=CLOUD0 * m)),
    ("CNYUSD FX (USD/ADS output only)", lambda m: base_ps * m),
]
out = []
for lab, fn in tests:
    lo_, hi_ = fn(0.9), fn(1.1)
    out.append((lab, lo_, hi_, max(abs(lo_ - base_ps), abs(hi_ - base_ps))))
out.sort(key=lambda x: -x[3])
print(f"BASE = CNY {base_ps:.2f}/share = US${to_ads(base_ps):.2f}/ADS")
print(f"{'#':<3}{'Input':<38}{'-10%':>10}{'+10%':>10}{'swing':>9}   (US$/ADS)")
for i, (lab, lo_, hi_, sw) in enumerate(out, 1):
    print(f"{i:<3}{lab:<38}{to_ads(lo_):>10.2f}{to_ads(hi_):>10.2f}{to_ads(sw):>9.2f}"
          f"   ({lo_/base_ps-1:+.1%} / {hi_/base_ps-1:+.1%})")

# =============================================================== 11. SOTP cross-check
hdr("11. SOTP CROSS-CHECK (Q1 FY27 segment adj EBITA x4 run-rate, dossier S3; multiples from dossier S7)")
ECOM_E, CLOUD_E = 39749 * 4, 5628 * 4
LOSS_E = (-13861 - 3343 - 163 - 681) * 4                      # AI Labs + All others + unallocated + elims
PEER_FWD = st.median(pe_f)
for lab, m_ecom, m_cloud, runoff, hc in (("low", min(pe_f), PEER_FWD, 3.0, 0.50),
                                         ("mid", PEER_FWD, amz["trailing_pe"], 2.0, 0.30),
                                         ("high", st.median(pe_t), amz["forward_pe"], 1.0, 0.15)):
    v_ecom = ECOM_E * (1 - TAX) * m_ecom
    v_cloud = CLOUD_E * (1 - TAX) * m_cloud
    v_loss = LOSS_E * (1 - TAX) * runoff
    v_sbc = -T["sbc_noncash"] * (1 - TAX) * m_ecom
    v_inv = INV_BOOK * (1 - hc)
    tot = v_ecom + v_cloud + v_loss + v_sbc + NET_CASH_ADJ + v_inv
    print(f"[{lab}] e-com {ECOM_E:,} x(1-t) x {m_ecom:.1f} = {v_ecom:,.0f} | cloud {CLOUD_E:,} x(1-t) x {m_cloud:.1f} = "
          f"{v_cloud:,.0f} | AI Labs/others/corp losses {LOSS_E:,} x(1-t) x {runoff:.0f}y runoff = {v_loss:,.0f} | "
          f"SBC {v_sbc:,.0f} | adj net cash {NET_CASH_ADJ:,.0f} | investments @{1-hc:.0%} {v_inv:,.0f}")
    print(f"      = {tot:,.0f} -> CNY {tot/SH:.2f}/share = US${to_ads(tot/SH):.2f}/ADS ({tot/MCAP-1:+.1%} vs price)")
non_cloud_mid = (ECOM_E * (1 - TAX) * PEER_FWD + LOSS_E * (1 - TAX) * 2.0 - T["sbc_noncash"] * (1 - TAX) * PEER_FWD
                 + NET_CASH_ADJ + INV_BOOK * 0.7)
implied_cloud = MCAP - non_cloud_mid
print(f"Market-implied cloud value (mcap - mid SOTP ex-cloud) = {implied_cloud:,.0f} = US${implied_cloud*FX/1e3:.1f}bn "
      f"= {implied_cloud/CLOUD_Q1/4:.2f}x run-rate revenue {CLOUD_Q1*4:,}, {implied_cloud/(CLOUD_E*(1-TAX)):.1f}x "
      f"run-rate NOPAT")
cloud_dcf_share = None
print("Cloud-specific peer multiples: UNKNOWN (dossier S7). AMZN multiples are a whole-company proxy, not AWS.")

# =============================================================== 12. summary
hdr("12. SUMMARY (no probabilities, no verdict - Skeptic's job)")
for nm in ("BEAR", "BASE", "BULL"):
    r = RES[nm][0]
    print(f"{nm:<5} CNY {r.per_share:>7.2f}/share | US${to_ads(r.per_share):>7.2f}/ADS | "
          f"S${to_sgd(to_ads(r.per_share)):>7.2f}/ADS | {r.upside(P_CNY):+.1%} | TV {r.terminal_share:.0%} of EV")
print(f"Price of record US${P_USD:.2f}/ADS (S${to_sgd(P_USD):.2f}); reverse-DCF implied 10-yr revenue CAGR {g_imp:+.2%}")
print(f"ROIC: facts-formula FY26 {roic[5]:.1%} (5-yr avg {avg(roic[L5]):.1%}); operating TTM see section 13 | WACC "
      f"{WACC:.2%}")

# =============================================================== 13. operating ROIC
hdr("13. OPERATING ROIC (invested capital ex cash, treasury and investment book; incl. NCI & mezzanine)")
IC_J = 1049038 + NCI + MEZZ + DEBT_J - LIQ - EQM - OTH_INV    # dossier S1/S2 Jun-26
IC_M = 1060886 + NCI + MEZZ + 259996 - 131530 - 155310 - 479996 - 206803   # Mar-26 (NCI/mezz Jun-26 proxy)
for lab, ebita, sb, icap, g_ in (("TTM Jun-26", EBITA0, T["sbc_noncash"], IC_J, 242456),
                                 ("FY26 Mar-26", 76416, 11180, IC_M, 247378)):
    np_ = (ebita - sb) * (1 - TAX)
    print(f"{lab}: NOPAT (adj EBITA {ebita:,} - SBC {sb:,}) x (1-{TAX:.1%}) = {np_:,.0f} | op IC {icap:,.0f} -> ROIC "
          f"{np_/icap:.1%} | goodwill {g_:,} = {g_/icap:.0%} of IC -> ex-goodwill ROIC {np_/(icap-g_):.1%}")
print(f"FY25 operating ROIC: UNKNOWN (FY25 equity-method balance not in dossier). WACC {WACC:.2%}.")
print(f"Capex - depreciation TTM {CAPEX0-D0:,} = {(CAPEX0-D0)/IC_J:.0%} of Jun-26 operating IC per year (IC growth)")
