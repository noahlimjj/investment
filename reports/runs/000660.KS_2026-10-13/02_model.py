"""SK hynix (000660.KS, KRX) valuation model, as of 2026-10-13. Quant stage of the pipeline.

Units: KRW millions ("M") unless stated; "T" = KRW trillion. Per-share values are KRW per
COMMON share on 728,866,596 shares outstanding (facts: derived.shares_outstanding = 730,492,365
issued - 1,625,769 treasury, post-ADS, before any of the Aug-Nov 2026 buyback).
Sources inline: (facts: ...) = facts.json, (dossier §n) = 01_research.md,
(fund: ...) = data/fundamentals.json, (inputs: ...) = 00_inputs.json.
ASSUMPTION = Quant judgement, always labelled and always sensitivity-tested in section G.

Template: FULL, Lynch Cyclical (dossier §0). Value on MID-CYCLE economics, not peak.
Base period: balance sheet 2026-06-30; revenue base = Q2-26 annualised run-rate (the 6/30
receivables/inventory/net cash are already sized to that run-rate, so using TTM revenue as the
base would double-count a working-capital build). Model year Y1 = Jul-2026..Jun-2027, etc.
Valuation date = price date 2026-10-13 -> stub 105/365 yr, mid-year discounting.

Run:  python3 reports/runs/000660.KS_2026-10-13/02_model.py
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from methodologies.valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
F = json.loads((RUN / "facts.json").read_text())
INP = json.loads((RUN / "00_inputs.json").read_text())
FUND = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["000660.KS"]
A, I, T, D, M = F["annual"], F["interim"], F["ttm"], F["derived"], F["market"]


def hr(t):
    print(f"\n{'=' * 6} {t} {'=' * max(4, 84 - len(t))}")


def tn(x):          # KRW M -> KRW T string
    return f"{x / 1e6:,.1f}T"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


# ------------------------------------------------------------------------------------ 0. units
hr("0. Price, shares, market cap, data-layer status")
PRICE = M["price_krw"]                                  # 1,443,000 (facts: market.price_krw, KRX close 10-13)
assert PRICE == INP["price"] == FUND["price"]
SHARES_M = D["shares_outstanding"] / 1e6                # 728.866596 M (facts: derived.shares_outstanding)
MCAP = PRICE * SHARES_M                                 # KRW M
KRW_PER_USD = 1 / INP["fx_spot_to_usd"]["KRWUSD"]       # (inputs: fx_spot_to_usd)
KRW_PER_SGD = KRW_PER_USD * INP["fx_spot_to_usd"]["SGDUSD"]
TAX = 40_056_711 / 174_325_213                          # H1-26 tax / PBT = 23.0% (dossier §2)
STUB = 105 / 365                                        # 2026-06-30 -> 2026-10-13
print(f"Price KRW {PRICE:,.0f} | shares {SHARES_M:,.6f}M | mcap {tn(MCAP)} "
      f"(facts {tn(D['mcap_krw_m'])}) | US${MCAP / KRW_PER_USD / 1e3:,.1f}B")
print(f"KRW/USD {KRW_PER_USD:,.2f} | KRW/SGD {KRW_PER_SGD:,.2f} | price = S${PRICE / KRW_PER_SGD:,.0f}/share")
print(f"Vendor shares (fund) {FUND['market_cap_usd'] / FUND['price_usd'] / 1e6:,.1f}M vs 728.9M used "
      f"(dossier §10.2: vendor count is pre-ADS)")
print(f"fundamentals.json warnings: {FUND['warnings'] or 'none'} | errors: {FUND['errors'] or 'none'}")
print(f"Tax rate used {pc(TAX)} (H1-26 effective, dossier §2) | stub {STUB:.4f} yr")
print(f"12m price change {M['chg_12m_pct']}% | 52w high {M['52w_high_krw']:,} -> price is "
      f"{PRICE / M['52w_high_krw'] - 1:+.1%} vs high")

# ------------------------------------------------------------------------------------ 1. history
hr("A1. History (KRW T) and margins")
YRS = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
REV = {y: A[y]["revenue"] for y in YRS}
OI = {y: A[y]["operating_income"] for y in YRS}
NI = {y: A[y]["net_income"] for y in YRS}
GM = {"FY2021": None, "FY2022": FUND["gross_margins"][3]}     # (fund: gross_margins, FY2022 = idx 3)
for y in YRS[2:]:
    GM[y] = A[y]["gross_profit"] / REV[y]
CAPEX = {y: A[y]["capex_ppe"] + A[y]["capex_intangibles"] for y in YRS[2:]}
DA = {y: A[y]["d_and_a"] for y in YRS[2:]}
FCF = {y: A[y]["fcf"] for y in YRS[2:]}
# FY2021-22 OCF/capex exist only as an aggregator search snippet (facts: FY2022.note) -> [SNIPPET]
SNIP = {"FY2021": (19_797_648, 12_486_635), "FY2022": (14_780_517, 19_010_261)}
for y, (o, c) in SNIP.items():
    CAPEX[y], FCF[y] = c, o - c
Q2 = I["Q2_2026"]
H1 = I["H1_2026"]
RR_REV = Q2["revenue"] * 4                               # Q2-26 annualised run-rate
TTM_REV, TTM_EBIT, TTM_DA = T["revenue"], T["operating_income"], T["d_and_a"]
TTM_CAPEX, TTM_FCF = T["capex_ppe_plus_intangibles"], T["fcf"]

print(f"{'':<8}{'Rev':>8}{'GM':>8}{'EBIT m':>8}{'NI m':>8}{'D&A%':>7}{'Capex%':>8}{'FCF m':>8}"
      f"{'EBITDA m':>9}{'Capex/DA':>9}")
for y in YRS:
    da = DA.get(y)
    tag = " [SNIPPET capex/FCF]" if y in SNIP else ""
    print(f"{y:<8}{REV[y] / 1e6:>8.1f}{(pc(GM[y]) if GM[y] is not None else 'UNKN'):>8}"
          f"{pc(OI[y] / REV[y]):>8}{pc(NI[y] / REV[y]):>8}"
          f"{(pc(da / REV[y]) if da else 'UNKN'):>7}{pc(CAPEX[y] / REV[y]):>8}{pc(FCF[y] / REV[y]):>8}"
          f"{(pc((OI[y] + da) / REV[y]) if da else 'UNKN'):>9}"
          f"{(f'{CAPEX[y] / da:.2f}' if da else 'UNKN'):>9}{tag}")
print(f"{'TTM6/26':<8}{TTM_REV / 1e6:>8.1f}{pc(T['gross_profit'] / TTM_REV):>8}{pc(TTM_EBIT / TTM_REV):>8}"
      f"{pc(T['net_income'] / TTM_REV):>8}{pc(TTM_DA / TTM_REV):>7}{pc(TTM_CAPEX / TTM_REV):>8}"
      f"{pc(TTM_FCF / TTM_REV):>8}{pc((TTM_EBIT + TTM_DA) / TTM_REV):>9}{TTM_CAPEX / TTM_DA:>9.2f}")
print(f"{'Q2-26':<8}{Q2['revenue'] / 1e6:>8.1f}{pc(Q2['gross_profit'] / Q2['revenue']):>8}"
      f"{pc(Q2['operating_income'] / Q2['revenue']):>8}{pc(Q2['net_income'] / Q2['revenue']):>8}"
      f"   (quarter; x4 run-rate revenue {tn(RR_REV)})")

ebit_m5 = [OI[y] / REV[y] for y in YRS]
OPM_SIMPLE = sum(ebit_m5) / 5
OPM_RW = sum(OI.values()) / sum(REV.values())
FCF_SIMPLE5 = sum(FCF[y] / REV[y] for y in YRS) / 5
FCF_RW5 = sum(FCF.values()) / sum(REV.values())
FCF_SIMPLE3 = sum(FCF[y] / REV[y] for y in YRS[2:]) / 3
FCF_RW3 = sum(FCF[y] for y in YRS[2:]) / sum(REV[y] for y in YRS[2:])
CAPEX_RW3 = sum(CAPEX[y] for y in YRS[2:]) / sum(REV[y] for y in YRS[2:])
print(f"\nEBIT margin FY21-25: min {pc(min(ebit_m5))} (FY2023), max {pc(max(ebit_m5))} (FY2025), "
      f"simple avg {pc(OPM_SIMPLE)}, revenue-weighted {pc(OPM_RW)}")
print(f"TTM EBIT margin {pc(TTM_EBIT / TTM_REV)} and Q2-26 {pc(Q2['operating_income'] / Q2['revenue'])} "
      f"are ABOVE the 5-yr max -> peak/near-peak of the cycle")
print(f"GM range FY22-TTM: {pc(GM['FY2023'])} .. {pc(Q2['gross_profit'] / Q2['revenue'])} (Q2-26)")
print(f"FCF margin FY21-25 (FY21-22 [SNIPPET]): simple {pc(FCF_SIMPLE5)}, rev-wtd {pc(FCF_RW5)} | "
      f"FY23-25 primary only: simple {pc(FCF_SIMPLE3)}, rev-wtd {pc(FCF_RW3)} | TTM {pc(TTM_FCF / TTM_REV)}")
print(f"Capex/revenue FY23-25 rev-wtd {pc(CAPEX_RW3)}")

hr("A2. Growth and Lynch category")
cagr_rev4 = (REV["FY2025"] / REV["FY2021"]) ** 0.25 - 1
cagr_ni4 = (NI["FY2025"] / NI["FY2021"]) ** 0.25 - 1
print("5-yr CAGR: UNKNOWN (FY2020 not in facts.json). 4-yr FY2021->FY2025 used instead:")
print(f"  revenue CAGR {pc(cagr_rev4)} | net income CAGR {pc(cagr_ni4)} (FY2021 EPS UNKNOWN -> NI used)")
for a_, b_ in zip(YRS[:-1], YRS[1:]):
    print(f"  {b_}: revenue {REV[b_] / REV[a_] - 1:+.1%}, EBIT {tn(OI[a_])} -> {tn(OI[b_])}")
print(f"  TTM vs FY2025 revenue {TTM_REV / REV['FY2025'] - 1:+.1%}; H1-26 vs H1-25 "
      f"{H1['revenue'] / I['H1_2025']['revenue'] - 1:+.1%}")

# Log-linear revenue trend FY2021-25 (x = years from mid-2021); cycle factor = revenue / trend
xs = list(range(5))
ys = [math.log(REV[y]) for y in YRS]
mx, my = sum(xs) / 5, sum(ys) / 5
SLOPE_LOG = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
INTER = my - SLOPE_LOG * mx
TREND_G = math.exp(SLOPE_LOG) - 1                        # fitted trend growth
TREND_FY25 = math.exp(INTER + SLOPE_LOG * 4)             # fitted trend level at FY2025 (KRW M)


def trend_fit(x):
    return math.exp(INTER + SLOPE_LOG * x)


print(f"\nLog-linear trend FY2021-25: fitted growth {pc(TREND_G)}/yr; fitted FY2025 level {tn(TREND_FY25)}")
print(f"{'period':<9}{'revenue':>9}{'trend':>8}{'factor':>8}{'EBIT m':>8}")
for x, y in zip(xs, YRS):
    print(f"{y:<9}{REV[y] / 1e6:>9.1f}{trend_fit(x) / 1e6:>8.1f}{REV[y] / trend_fit(x):>8.2f}{pc(OI[y] / REV[y]):>8}")
for lab, x, r, o in (("TTM6/26", 4.5, TTM_REV, TTM_EBIT), ("Q2-26 RR", 4.875, RR_REV, Q2["operating_income"] * 4)):
    print(f"{lab:<9}{r / 1e6:>9.1f}{trend_fit(x) / 1e6:>8.1f}{r / trend_fit(x):>8.2f}{pc(o / r):>8}")
ON_TREND_PRE = OI["FY2022"] / REV["FY2022"]               # factor 1.04, pre-HBM
ON_TREND_HBM = OI["FY2024"] / REV["FY2024"]               # factor 1.03, HBM era
print(f"On-trend margins (factor ~1.03): FY2022 {pc(ON_TREND_PRE)} (pre-HBM) vs FY2024 {pc(ON_TREND_HBM)} "
      f"(HBM era): +{(ON_TREND_HBM - ON_TREND_PRE) * 100:.1f}pp; at factor ~1.23: FY2021 "
      f"{pc(OI['FY2021'] / REV['FY2021'])} vs FY2025 {pc(OI['FY2025'] / REV['FY2025'])}")

hr("A3. Lynch metrics (each with formula)")
EPS_TTM_BASIC = T["basic_eps_won"]                       # 229,700 (facts: ttm.basic_eps_won)
PE_TTM = PRICE / EPS_TTM_BASIC
NOPAT_TTM = TTM_EBIT * (1 - TAX)
PE_OPER = MCAP / NOPAT_TTM
CONS_EPS26, CONS_EPS27 = 355_219, 470_324                # CONSENSUS (Yahoo via yfinance, dossier §9)
PE_FWD = PRICE / CONS_EPS27
print(f"Trailing P/E (reported) = price / TTM basic EPS = {PRICE:,} / {EPS_TTM_BASIC:,} = {PE_TTM:.2f}x "
      f"(TTM NI includes H1-26 finance income {tn(H1['finance_income'])})")
print(f"Trailing P/E (operating) = mcap / (TTM EBIT x (1-t)) = {tn(MCAP)} / {tn(NOPAT_TTM)} = {PE_OPER:.2f}x")
print(f"Forward P/E = price / CONSENSUS FY2027 EPS {CONS_EPS27:,} = {PE_FWD:.2f}x "
      f"(fund forward_pe {FUND['forward_pe']:.2f}x)")
g_cons = CONS_EPS27 / CONS_EPS26 - 1
g_hist = cagr_ni4
g_peg = min(g_cons, g_hist)
ok, why = peg_is_valid(PE_TTM, PE_FWD, g_peg)
print(f"PEG growth = lower of historical NI CAGR {pc(g_hist)} and CONSENSUS FY26->FY27 EPS {pc(g_cons)} "
      f"= {pc(g_peg)}; peg_is_valid -> {ok} ({why})")
if ok:
    print(f"  PEG = {PE_TTM:.2f} / {g_peg * 100:.1f} = {PE_TTM / (g_peg * 100):.2f} (reported P/E); "
          f"{PE_OPER / (g_peg * 100):.2f} (operating P/E). Peak-cycle EPS -> not a verdict driver for a cyclical.")
DPS_TTM = 3_000                                          # 375+1,875+375+375 paid over 12m (dossier §1)
DY = DPS_TTM / PRICE
print(f"Dividend yield = 3,000 / {PRICE:,} = {pc(DY, 2)} (fixed KRW 1,500/yr policy 2025-27 -> {pc(1500 / PRICE, 2)})")
print(f"Lynch ratio = (EPS growth % + yield %) / P/E = ({g_peg * 100:.1f} + {DY * 100:.2f}) / {PE_TTM:.2f} = "
      f"{(g_peg * 100 + DY * 100) / PE_TTM:.2f} (reported) | / {PE_OPER:.2f} = "
      f"{(g_peg * 100 + DY * 100) / PE_OPER:.2f} (operating)")
TREND_NOW = TREND_FY25 * (1 + TREND_G)                   # fitted trend revenue at base-period end (x=5.0)
EPS_MID = TREND_NOW * OPM_RW * (1 - TAX) / SHARES_M      # KRW/share, mid-cycle (29.0% EBIT on trend revenue)
PE_MID = PRICE / EPS_MID
print(f"Mid-cycle EPS = trend revenue {tn(TREND_NOW)} x mid-cycle EBIT {pc(OPM_RW)} x (1-t) / {SHARES_M:.1f}M = "
      f"KRW {EPS_MID:,.0f} -> mid-cycle P/E {PE_MID:.1f}x")
print(f"Lynch ratio on mid-cycle P/E with base trend growth 10% (Y4 fade target) = (10 + {DY * 100:.2f}) / "
      f"{PE_MID:.1f} = {(10 + DY * 100) / PE_MID:.2f}")

# --------------------------------------------------------------------------- EV bridge (6/30 BS)
hr("A4. EV bridge / net cash (KRW M) -- IFRS 16: leases IN net debt, FCF pre-lease")
CASH_ST = H1["cash_plus_st_fin_plus_st_inv"]             # 87,957,923
BORR = H1["borrowings_total"]                            # 18,586,634
LEASE = H1["lease_liabilities"]                          # 2,526,505
CUR_TAX = H1["current_tax_liabilities"]                  # 31,958,025 unpaid (orchestrator note)
ADR_NET_USD_M = 26_200                                   # US$26.2B est. net, received after 6/30 (dossier §1/§5)
ADR_KRW = ADR_NET_USD_M * KRW_PER_USD                    # converted at today's spot (conservative)
ADR_KRW_ISSUE = ADR_NET_USD_M * 1_504.9                  # at the issue-date rate (dossier §1)
LT_INV = H1["long_term_investment_assets"]               # 85,309,524 FV (Kioxia-related share UNKNOWN)
LT_FIN = H1["long_term_fin_instruments"]                 # 7,101,803
NCI = 312_618                                            # dossier §2
DIV_Q2 = 273_324.80175                                   # Q2 dividend KRW 375, record 8/31: buyer today won't get it
LT_HAIRCUT = 0.30                                        # ASSUMPTION: tax on gain (DTL 7.84T), single-stake, marked at cycle peak


def bridge(haircut=LT_HAIRCUT, adr=ADR_KRW, lt_inv=LT_INV):
    return (CASH_ST - BORR - LEASE - CUR_TAX + adr + lt_inv * (1 - haircut) + LT_FIN - NCI - DIV_Q2)


NET_CASH_CO = CASH_ST - BORR                             # company definition 69.4T
BRIDGE = bridge()
for lab, v in (("+ cash, ST fin. instr., ST investment assets", CASH_ST), ("- borrowings", -BORR),
               ("- lease liabilities (IFRS 16)", -LEASE), ("- current tax liabilities (unpaid)", -CUR_TAX),
               ("+ ADS net proceeds US$26.2B at spot", ADR_KRW),
               (f"+ LT investment assets x (1-{LT_HAIRCUT:.0%})", LT_INV * (1 - LT_HAIRCUT)),
               ("+ LT financial instruments", LT_FIN), ("- non-controlling interest", -NCI),
               ("- Q2 dividend declared (ex 8/28)", -DIV_Q2)):
    print(f"  {lab:<48}{v:>14,.0f}")
print(f"  {'= non-operating net assets (NET_CASH for DCF)':<48}{BRIDGE:>14,.0f}  = KRW {BRIDGE / SHARES_M:,.0f}/share")
print(f"Company net cash (cash+ST - borrowings) {NET_CASH_CO:,.0f} = KRW {NET_CASH_CO / SHARES_M:,.0f}/share")
OPER_EV = MCAP - BRIDGE
print(f"Operating EV implied by price = mcap - bridge = {tn(OPER_EV)} (facts simple EV {tn(D['ev_krw_m_simple'])})")
print(f"Net-cash-adjusted P/E = (price - net cash/sh) / EPS: company net cash -> "
      f"({PRICE:,} - {NET_CASH_CO / SHARES_M:,.0f}) / {EPS_TTM_BASIC:,} = "
      f"{(PRICE - NET_CASH_CO / SHARES_M) / EPS_TTM_BASIC:.2f}x | full bridge on operating EPS "
      f"{NOPAT_TTM / SHARES_M:,.0f} -> {(PRICE - BRIDGE / SHARES_M) / (NOPAT_TTM / SHARES_M):.2f}x")

hr("A5. Inventory / receivables vs sales; debt")
inv = {"FY2023": A["FY2023"]["inventories"], "FY2024": A["FY2024"]["inventories"],
       "FY2025": A["FY2025"]["inventories"], "6/30/26": H1["inventories"]}
rec = {"FY2023": A["FY2023"]["trade_receivables"], "FY2024": A["FY2024"]["trade_receivables"],
       "FY2025": A["FY2025"]["trade_receivables"], "6/30/26": H1["trade_receivables"]}
for a_, b_ in (("FY2023", "FY2024"), ("FY2024", "FY2025")):
    print(f"{a_}->{b_}: inventories {inv[b_] / inv[a_] - 1:+.1%}, receivables {rec[b_] / rec[a_] - 1:+.1%}, "
          f"revenue {REV[b_] / REV[a_] - 1:+.1%}")
h2_25_ann = (REV["FY2025"] - I["H1_2025"]["revenue"]) * 2
print(f"12/31/25->6/30/26: inventories {inv['6/30/26'] / inv['FY2025'] - 1:+.1%}, receivables "
      f"{rec['6/30/26'] / rec['FY2025'] - 1:+.1%}; revenue run-rate H2-25 ann. {tn(h2_25_ann)} -> Q2-26 ann. "
      f"{tn(RR_REV)} = {RR_REV / h2_25_ann - 1:+.1%}; TTM vs FY2025 {TTM_REV / REV['FY2025'] - 1:+.1%}")
cogs_h2_25 = (REV["FY2025"] - A["FY2025"]["gross_profit"]) - (I["H1_2025"]["revenue"] - I["H1_2025"]["gross_profit"])
print(f"DSO: 12/31/25 on H2-25 run-rate {rec['FY2025'] / h2_25_ann * 365:.0f} d -> 6/30/26 on Q2 run-rate "
      f"{rec['6/30/26'] / RR_REV * 365:.0f} d | DIO: {inv['FY2025'] / (cogs_h2_25 * 2) * 365:.0f} d -> "
      f"{inv['6/30/26'] / ((Q2['revenue'] - Q2['gross_profit']) * 4) * 365:.0f} d")
print(f"Debt 6/30/26: borrowings {tn(BORR)} (current {tn(H1['borrowings_current'])}) + leases {tn(LEASE)} vs "
      f"cash+ST {tn(CASH_ST)}; maturity ladder 2027-31 UNKNOWN; interest expense UNKNOWN")

# ------------------------------------------------------------------------------------ B. quality
hr("B1. ROIC = NOPAT / (equity + debt incl. leases - cash&ST), period-end, tax 23.0%")
BS = {"FY2023": (A["FY2023"]["equity_total"], A["FY2023"]["borrowings_total"] + A["FY2023"]["lease_liabilities"],
                 A["FY2023"]["cash_plus_st_fin_plus_st_inv"]),
      "FY2024": (A["FY2024"]["equity_total"], A["FY2024"]["borrowings_total"] + A["FY2024"]["lease_liabilities"],
                 A["FY2024"]["cash_plus_st_fin_plus_st_inv"]),
      "FY2025": (A["FY2025"]["equity_total"], A["FY2025"]["borrowings_total"] + A["FY2025"]["lease_liabilities"],
                 A["FY2025"]["cash_plus_st_fin_plus_st_inv"]),
      "TTM6/26": (H1["equity_total"], D["total_debt_incl_leases_6_30"], CASH_ST)}
ROIC = {}
for k, (eq, dt, cs) in BS.items():
    ebit = OI[k] if k in OI else TTM_EBIT
    ic = eq + dt - cs
    ROIC[k] = ebit * (1 - TAX) / ic
    print(f"{k:<8} NOPAT {tn(ebit * (1 - TAX)):>8} / IC {tn(ic):>8} = {pc(ROIC[k])}")
ic_ex = H1["equity_total"] + D["total_debt_incl_leases_6_30"] - CASH_ST - LT_INV - LT_FIN
print(f"TTM ex non-operating LT investments (IC {tn(ic_ex)}): {pc(NOPAT_TTM / ic_ex)}")
ROIC_CYC = sum(ROIC[k] for k in ("FY2023", "FY2024", "FY2025")) / 3
print(f"Through-cycle ROIC FY2023-25 simple avg {pc(ROIC_CYC)} | goodwill UNKNOWN -> ex-goodwill test not possible")
print(f"(fund: roe {FUND['roe']:.3f} is not reproducible from filings: FY2025 NI/equity = "
      f"{NI['FY2025'] / A['FY2025']['equity_total']:.3f}; not used)")

hr("B2. Owner earnings = NI + D&A - capex (AGENTS.md)")
OE_FY25 = NI["FY2025"] + DA["FY2025"] - CAPEX["FY2025"]
OE_TTM = T["net_income"] + TTM_DA - TTM_CAPEX
OE_TTM_ADJ = NOPAT_TTM + TTM_DA - TTM_CAPEX               # NI replaced by EBIT x (1-t): strips finance gains
SBC_TTM = 282_445                                         # dossier §2
print(f"FY2025: {tn(NI['FY2025'])} + {tn(DA['FY2025'])} - {tn(CAPEX['FY2025'])} = {tn(OE_FY25)} "
      f"(fund owner_earnings {tn(FUND['owner_earnings'] / 1e6)}) -> yield {pc(OE_FY25 / MCAP)}")
print(f"TTM reported: {tn(T['net_income'])} + {tn(TTM_DA)} - {tn(TTM_CAPEX)} = {tn(OE_TTM)} -> yield {pc(OE_TTM / MCAP)} "
      f"(inflated by non-operating gains)")
print(f"TTM adjusted (NI -> EBIT x (1-t)): {tn(NOPAT_TTM)} + {tn(TTM_DA)} - {tn(TTM_CAPEX)} = {tn(OE_TTM_ADJ)} "
      f"-> yield {pc(OE_TTM_ADJ / MCAP)}")
print(f"SBC: already expensed in NI/EBIT (CF add-back TTM {tn(SBC_TTM)} = {pc(SBC_TTM / TTM_REV, 2)} of revenue); "
      f"SBC-adjusted OE = OE (no add-back to remove). SBC-adj. FCF = FCF - SBC = {tn(TTM_FCF - SBC_TTM)}")
DIVREC = H1["dividends_received_in_ocf"]
TAX_BUILD = H1["current_tax_liabilities"] - 7_023_813     # current tax 12/31/25 7,023,813 (dossier §2)
FCF_ADJ = TTM_FCF - DIVREC - TAX_BUILD
print(f"TTM FCF {tn(TTM_FCF)}; less dividends received in OCF {tn(DIVREC)} and current-tax build {tn(TAX_BUILD)} "
      f"= adjusted {tn(FCF_ADJ)}")

# ------------------------------------------------------------------------------ C. multiples matrix
hr("C. Multiples matrix (current; 5-yr own avg UNKNOWN: no historical prices in dossier; peers = dossier §7)")
EBITDA_TTM = TTM_EBIT + TTM_DA
EBIT_RR = Q2["operating_income"] * 4
EBIT_MID_NOW = TREND_NOW * OPM_RW
print(f"EV/EBITDA TTM: operating EV {tn(OPER_EV)} / {tn(EBITDA_TTM)} = {OPER_EV / EBITDA_TTM:.2f}x | "
      f"facts simple EV {tn(D['ev_krw_m_simple'])} -> {D['ev_krw_m_simple'] / EBITDA_TTM:.2f}x")
print(f"EV/EBIT run-rate (Q2 x4 {tn(EBIT_RR)}): {OPER_EV / EBIT_RR:.2f}x | EV/EBIT mid-cycle "
      f"({tn(EBIT_MID_NOW)} = trend x 29.0%): {OPER_EV / EBIT_MID_NOW:.1f}x")
print(f"P/E trailing reported {PE_TTM:.2f}x | operating {PE_OPER:.2f}x | forward (CONSENSUS FY27) {PE_FWD:.2f}x | "
      f"mid-cycle {PE_MID:.1f}x")
SBC_FCF = TTM_FCF - SBC_TTM
print(f"P/FCF TTM {MCAP / TTM_FCF:.1f}x | SBC-adj {MCAP / SBC_FCF:.1f}x | adjusted FCF {tn(FCF_ADJ)} -> "
      f"{MCAP / FCF_ADJ:.1f}x")
print(f"FCF yield TTM {pc(fcf_yield(TTM_FCF, MCAP))} | SBC-adj {pc(fcf_yield(SBC_FCF, MCAP))} | adjusted "
      f"{pc(fcf_yield(FCF_ADJ, MCAP))} | FY2025 {pc(fcf_yield(FCF['FY2025'], MCAP))}")
print(f"Owner-earnings yield: TTM adjusted {pc(OE_TTM_ADJ / MCAP)} | TTM reported {pc(OE_TTM / MCAP)} | "
      f"FY2025 {pc(OE_FY25 / MCAP)}")
PEERS = {"005930.KS": (6.03, None, 3.21, 0.022), "MU": (9.93, 12.6, 4.55, 0.002), "SNDK": (16.90, 19.6, 5.43, 0.055),
         "285A.T": (10.55, 18.2, None, 0.014), "2408.TW": (12.86, 18.2, 4.07, 0.003)}   # dossier §7 (vendor)


def med(v):
    v = sorted(x for x in v if x is not None)
    n = len(v)
    return (v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2), n


OWN_VENDOR = ("6.68", "null", f"{FUND['forward_pe']:.2f}", "2.4% (FY2025 FCF)")      # dossier §7 row
for i, lab in enumerate(("EV/EBITDA (vendor)", "Trailing P/E (vendor)", "Forward P/E (vendor)", "FCF yield (vendor)")):
    m_, n_ = med([p_[i] for p_ in PEERS.values()])
    print(f"Peer median {lab}: {m_:.3f} (n={n_}) | SK hynix vendor: {OWN_VENDOR[i]}")

# ----------------------------------------------------------------------------- D. discount rate
hr("D. Discount rate (CAPM + after-tax debt, market-value weights)")
RF = INP["risk_free_10y"]["KRW"]["value_pct"] / 100       # 4.369% KTB 10y 2026-10-06
RF_OECD = INP["risk_free_10y"]["KRW_oecd_monthly"]["value_pct"] / 100
ERP = INP["equity_risk_premium_pct"] / 100                # 5.0%
BETA_RAW = FUND["beta"]                                   # 2.391 (fund: beta)
BETA = 0.67 * BETA_RAW + 0.33                             # Blume
KD_PRE = RF + 0.01                                        # ASSUMPTION: interest expense not in dossier
DEBT_W = (BORR + LEASE) / (MCAP + BORR + LEASE)           # book debt as proxy for market value


def wacc_of(beta=BETA, rf=RF, kd=KD_PRE):
    ke = rf + beta * ERP
    w = (1 - DEBT_W) * ke + DEBT_W * kd * (1 - TAX)
    return max(w, rf + 0.04), ke


WACC, KE = wacc_of()
FLOOR = RF + 0.04
print(f"rf {pc(RF, 3)} (inputs: KRW KTB 10y 2026-10-06) | ERP {pc(ERP)} | raw beta {BETA_RAW} (fund) -> "
      f"Blume 0.67x{BETA_RAW}+0.33 = {BETA:.3f}")
print(f"Ke = {pc(RF, 3)} + {BETA:.3f} x {pc(ERP)} = {pc(KE, 2)} | Kd pre-tax {pc(KD_PRE, 2)} (ASSUMPTION rf+1%) "
      f"after-tax {pc(KD_PRE * (1 - TAX), 2)}")
print(f"Weights: E {tn(MCAP)}, D {tn(BORR + LEASE)} -> D/(D+E) {pc(DEBT_W, 2)}")
print(f"WACC = {pc(WACC, 2)} | floor (KRW 10y + 4%) {pc(FLOOR, 2)} -> floor binding: {WACC <= FLOOR + 1e-12}")
for lab, kw in (("rf = OECD Aug monthly 4.286%", dict(rf=RF_OECD)), ("beta = 1.0 (no vendor beta)", dict(beta=1.0)),
                ("raw beta 2.391 (no Blume)", dict(beta=BETA_RAW)), ("Kd = rf + 3%", dict(kd=RF + 0.03))):
    print(f"  WACC if {lab:<30} {pc(wacc_of(**kw)[0], 2)}")

# ---------------------------------------------------------------------------- E. DCF scenarios
N = 10
BASE_REV = RR_REV
WC = 0.15            # ASSUMPTION: d(inventories+receivables)/d(revenue): FY23->24 18.7%, FY24->25 19.9%,
#                      FY25->6/30/26 vs run-rate 15.1% (payables UNKNOWN, so gross); 15% used
DA0, CAPEX0 = TTM_DA, TTM_CAPEX
DA_CONV = 6.0        # D&A_t = D&A_{t-1} + (capex_{t-1} - D&A_{t-1}) / 6 ; calibrated below

hr("E0. D&A rule calibration and base-period anchors")
for a_, b_ in (("FY2023", "FY2024"), ("FY2024", "FY2025")):
    pred = DA[a_] + (CAPEX[a_] - DA[a_]) / DA_CONV
    print(f"D&A {b_}: rule {tn(pred)} vs actual {tn(DA[b_])} ({pred / DA[b_] - 1:+.1%})")
print(f"Base revenue = Q2-26 x4 = {tn(BASE_REV)} (TTM {tn(TTM_REV)}); WC {pc(WC)} of delta revenue; tax {pc(TAX)}")
print("SBC: margins are reported EBIT (SBC expensed); dcf() adds no SBC back -> SBC treated as a cost, "
      "share count held at 728.87M (not grown). Never both.")
print("Acquired-intangible amortisation: D&A < capex (FY25 13.9T vs 28.6T) -> acq_amort_pct not used, no D&A fade.")


def trend_path(p):
    """Trend revenue at the centre of Y1..Y10. x=4 is mid-2025 (fitted FY2025 level).
    Y1 centre x=5.5. r[0] covers x 4->5.5 (1.5 yr), r[1..3] cover Y1->Y2->Y3->Y4, then g5_10."""
    lvl = TREND_FY25 * p.get("trend_scale", 1.0)
    r = p["trend_r"]
    out = [lvl * (1 + r[0]) ** 1.5]
    for k in range(1, 4):
        out.append(out[-1] * (1 + r[k]))
    for g in p["g5_10"]:
        out.append(out[-1] * (1 + g))
    return out


def build(p, peak_years=1):
    """Return (dcf kwargs, table rows). revenue_t = factor_t x trend_t; Y1 set absolutely.
    Capex Y1-Y4 absolute (board commitments/guidance); Y5+ = D&A + (g/ROIC) x trend-NOPAT - dWC,
    i.e. capacity reinvestment consistent with the terminal ROIC (no free growth)."""
    tr = trend_path(p)
    f1 = p["y1_rev"] / tr[0]
    factors = ([f1] * peak_years + [p["f2"], p["f3"]] + [1.0] * N)[:N]
    margins = ([p["m1"]] * peak_years + [p["m2"], p["m3"]] + [p["m_mid"]] * N)[:N]
    rev = [factors[i] * tr[i] for i in range(N)]
    rev[0] = p["y1_rev"]
    da_prev, cap_prev, prev_rev = DA0, CAPEX0, BASE_REV
    g_l, eb_l, cx_l, da_l, rows = [], [], [], [], []
    for i in range(N):
        da = da_prev + (cap_prev - da_prev) / DA_CONV
        if i < 4:
            cap = p["capex_abs"][i] * p.get("capex_scale", 1.0)
        else:
            g_tr = tr[i] / tr[i - 1] - 1
            nopat_tr = tr[i] * p["m_mid"] * (1 - p.get("tax", TAX))
            cap = da + g_tr / p["roic"] * nopat_tr - WC * (rev[i] - rev[i - 1])
        g_l.append(rev[i] / prev_rev - 1)
        eb_l.append(margins[i] + da / rev[i])
        cx_l.append(cap / rev[i])
        da_l.append(da / rev[i])
        rows.append((i + 1, rev[i], factors[i], margins[i], da, cap))
        da_prev, cap_prev, prev_rev = da, cap, rev[i]
    kw = dict(base_revenue=BASE_REV, growth=g_l, ebitda_margin=eb_l, capex_pct=cx_l, da_pct=da_l,
              tax=p.get("tax", TAX), wacc=p.get("wacc", WACC),
              net_debt=-bridge(haircut=p.get("lt_haircut", LT_HAIRCUT), lt_inv=LT_INV * p.get("lt_scale", 1.0)),
              shares=SHARES_M, terminal_growth=p["g_term"], terminal_roic=p["roic"],
              wc_pct_of_delta_rev=WC, mid_year=True, stub_years=STUB)
    return kw, rows


def value(p, **kw):
    k, _ = build(p, **kw)
    return dcf(**k).per_share


# Scenario parameters. Y = Jul..Jun years. Margins are EBIT (post-SBC) margins.
BASE = dict(
    label="BASE",
    y1_rev=RR_REV,                     # Q2-26 x4: guided Q3 DRAM bits +~10% offset by KRW -12.8% (dossier §3, §10.8)
    m1=0.70,                           # between TTM 68.0% and Q2-26 76.3% (FX headwind on KRW revenue)
    f2=2.0, m2=0.55,                   # 'tight ... for a considerable period' (dossier §3): still 2x trend in Y2
    f3=0.80, m3=0.05,                  # downturn trough Y3 (FY2023 trough was factor 0.62 at -23.6%)
    m_mid=OPM_RW,                      # mid-cycle EBIT = FY2021-25 revenue-weighted average 29.0%
    trend_r=[TREND_G, 0.17, 0.135, 0.10],   # fitted 22.4% to Y1, fading to 10% by Y4
    g5_10=[0.09, 0.08, 0.07, 0.06, 0.05, 0.04],
    capex_abs=[55e6, 60e6, 45e6, 40e6],      # 2026 guide 'high-40T' (H1 19.0T done), Y2/M17/P&T7 commitments
    roic=0.15,                         # ~FY2023-25 average ROIC 15.5%
    g_term=0.03,
)
BULL = dict(
    label="BULL",
    y1_rev=RR_REV * 1.10 * 1.10,       # Q3 DRAM bits +10% guided; H2 bits > H1 guided; +10% ASP ASSUMPTION
    m1=Q2["operating_income"] / Q2["revenue"],   # Q2-26 actual 76.3%
    f2=2.6, m2=T["operating_income"] / T["revenue"],  # TTM actual 68.0%
    f3=1.20, m3=0.45,                  # soft landing at FY2025-like factor (1.23 -> 48.6%)
    m_mid=(OI["FY2024"] / REV["FY2024"] + OI["FY2025"] / REV["FY2025"]) / 2,  # HBM-era avg FY24-25 42.0%
    trend_r=[TREND_G] * 4,             # fitted 22.4% trend holds to Y4
    g5_10=[0.15, 0.13, 0.11, 0.09, 0.07, 0.05],
    capex_abs=[60e6, 70e6, 60e6, 55e6],
    roic=0.25,                         # between FY2024 21.2% and FY2025 32.9%
    g_term=0.04,                       # cap = min(4%, KRW 10y 4.369%)
)
BEAR = dict(
    label="BEAR",
    y1_rev=RR_REV * 0.75,              # downturn starts in Y1: price reversal + KRW -12.8%
    m1=0.55,
    f2=REV["FY2023"] / trend_fit(2), m2=OI["FY2023"] / REV["FY2023"],   # FY2023 trough factor 0.62 and margin -23.6%
    f3=0.85, m3=0.05,
    m_mid=OPM_SIMPLE,                  # FY2021-25 simple average 21.0% (incl. the loss year)
    trend_r=[0.05] * 4,                # ASSUMPTION: 5% trend growth (lowest positive year FY2022 +3.8%)
    g5_10=[0.05, 0.05, 0.04, 0.04, 0.03, 0.03],
    capex_abs=[50e6, 30e6, 25e6, 25e6],  # FY2023-style cut (FY22->FY23 capex -54% [SNIPPET])
    roic=0.10,                         # below WACC: growth destroys value at mid-cycle
    g_term=0.02,
)
SCN = [BEAR, BASE, BULL]
RES = {}

hr("E1. Scenario inputs and outputs (KRW T; per-share KRW)")
for s in SCN:
    kw, rows = build(s)
    r = dcf(**kw)
    RES[s["label"]] = (r, kw, rows)
    print(f"\n--- {s['label']}: WACC {pc(kw['wacc'], 2)}, g_term {pc(s['g_term'])}, terminal ROIC {pc(s['roic'])}, "
          f"mid-cycle EBIT {pc(s['m_mid'])}, trend r {[round(x, 3) for x in s['trend_r']]} ---")
    print(f"{'Y':<4}{'Rev':>8}{'growth':>8}{'factor':>7}{'EBIT m':>8}{'EBITDA m':>9}{'D&A':>7}{'Capex':>7}"
          f"{'Cpx%':>7}{'FCF':>8}{'FCF m':>7}{'PV FCF':>8}")
    for (yr, rev, fac, m, da, cap), row, g in zip(rows, r.rows, kw["growth"]):
        fcf, pvf = row[6], row[7]
        print(f"Y{yr:<3}{rev / 1e6:>8.1f}{g:>+8.1%}{fac:>7.2f}{pc(m):>8}{pc(kw['ebitda_margin'][yr - 1]):>9}"
              f"{da / 1e6:>7.1f}{cap / 1e6:>7.1f}{pc(cap / rev):>7}{fcf / 1e6:>8.1f}{pc(fcf / rev):>7}{pvf / 1e6:>8.1f}")
    fm_mid = sum(row[6] / row[1] for row in r.rows[4:]) / 6
    y10 = r.rows[-1]
    nopat10 = y10[3] * (1 - kw["tax"])
    reinv10 = (y10[5] - y10[4] + WC * (y10[1] - r.rows[-2][1])) / nopat10
    print(f"Avg FCF margin Y5-Y10 {pc(fm_mid)} (5-yr hist: simple {pc(FCF_SIMPLE5)}, rev-wtd {pc(FCF_RW5)}) | "
          f"Y10 reinvestment {pc(reinv10)} of NOPAT vs terminal g/ROIC {pc(s['g_term'] / s['roic'])}")
    flag = "  <-- TV > 75% of EV" if r.terminal_share > 0.75 else ""
    print(f"PV explicit {tn(r.pv_explicit)} + PV terminal {tn(r.pv_terminal)} = EV {tn(r.enterprise_value)} | "
          f"TV share {pc(r.terminal_share)}{flag}")
    print(f"+ non-operating net assets {tn(-kw['net_debt'])} = equity {tn(r.equity_value)} / {SHARES_M:.3f}M sh")
    print(f">>> {s['label']} VALUE/SHARE KRW {r.per_share:,.0f}  vs price {PRICE:,} => {r.upside(PRICE):+.1%} | "
          f"S${r.per_share / KRW_PER_SGD:,.0f} | of which net assets KRW {-kw['net_debt'] / SHARES_M:,.0f}")
    y4 = r.rows[3]
    print(f"    implied: EV / mid-cycle Y4 EBIT {r.enterprise_value / y4[3]:.1f}x; price / Y4 NOPAT-per-share "
          f"{PRICE / (y4[3] * (1 - kw['tax']) / SHARES_M):.1f}x")

base_r, base_kw, base_rows = RES["BASE"]
print("\nSummary (KRW per share, 728,866,596 shares):")
for lab in ("BEAR", "BASE", "BULL"):
    r = RES[lab][0]
    print(f"  {lab:<5} KRW {r.per_share:>10,.0f}  ({r.upside(PRICE):+.1%})  TV share {pc(r.terminal_share)}  "
          f"EV {tn(r.enterprise_value)}")

hr("E2. Downstream: SK Square look-through and buyback / bridge variants")
SKSQ = 146_100_000                                        # SK Square direct holding (dossier §6)
for lab in ("BEAR", "BASE", "BULL"):
    ps = RES[lab][0].per_share
    print(f"  SK Square stake 146,100,000 sh x {lab} KRW {ps:,.0f} = {tn(SKSQ * ps / 1e6)} "
          f"(at price: {tn(SKSQ * PRICE / 1e6)})")
BB_SH = 24.07                                             # M shares cap (dossier §5)
for lab in ("BEAR", "BASE", "BULL"):
    r = RES[lab][0]
    for px in (PRICE, 1_662_000):
        spend = BB_SH * px
        ps = (r.equity_value - spend) / (SHARES_M - BB_SH)
        print(f"  {lab}: buyback fully executed (24.07M sh at KRW {px:,}, {tn(spend)}) -> KRW {ps:,.0f}/sh "
              f"({ps / r.per_share - 1:+.1%} vs no buyback)")
for hc in (0.0, 0.30, 0.50, 1.0):
    v = value({**BASE, "lt_haircut": hc})
    print(f"  BASE with LT investment haircut {hc:.0%}: KRW {v:,.0f}")
print(f"  ADS proceeds at issue rate 1,504.9 instead of spot: +KRW {(ADR_KRW_ISSUE - ADR_KRW) / SHARES_M:,.0f}/share")
print(f"  Profit-share accruals (LT employee benefits 2.88T + rise in other non-trade payables 5.52T, "
      f"dossier §8) if debt-like: -KRW {(2_881_930 + 11_800_979 - 6_283_111) / SHARES_M:,.0f}/share (not deducted)")

# ----------------------------------------------------------------- F. reverse DCF & sensitivity
hr("F1. Reverse DCF: what must be true at KRW 1,443,000?")
rkw = {k: v for k, v in base_kw.items() if k not in ("base_revenue", "growth")}
g_rr = reverse_dcf(price=PRICE, base_revenue=BASE_REV, years=N, **rkw)
g_ttm = reverse_dcf(price=PRICE, base_revenue=TTM_REV, years=N, **rkw)
print(f"reverse_dcf (BASE margin/capex/D&A % paths, WACC {pc(WACC, 2)}, g 3%, ROIC 15%):")
print(f"  from Q2-26 run-rate {tn(BASE_REV)}: constant revenue CAGR {pc(g_rr)} for 10 yrs "
      f"(Y10 revenue {tn(BASE_REV * (1 + g_rr) ** 10)})")
print(f"  from TTM {tn(TTM_REV)}: constant revenue CAGR {pc(g_ttm)} (Y10 revenue {tn(TTM_REV * (1 + g_ttm) ** 10)})")


def solve(fn, lo, hi, target=PRICE, it=80):
    flo = fn(lo) - target
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = fn(mid) - target
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def solve_or_none(fn, lo, hi):
    """Bisection only if the price is bracketed; otherwise None (never report a search bound)."""
    if (fn(lo) - PRICE) * (fn(hi) - PRICE) > 0:
        return None
    return solve(fn, lo, hi)


m_req = solve_or_none(lambda m: value({**BASE, "m_mid": m}), 0.0, 0.95)
m_req2 = solve_or_none(lambda m: value({**BASE, "m_mid": m, "roic": BASE["roic"] * m / OPM_RW}), 0.05, 0.95)
s_req = solve(lambda s: value({**BASE, "trend_scale": s}), 0.1, 10.0)
irr = solve(lambda w: value({**BASE, "wacc": w}), 0.031, 0.40)
print("Holding BASE revenue path, ROIC fixed 15%: required mid-cycle EBIT margin (Y4-Y10 + terminal) = "
      + (f"NOT REACHED at <=95% (value at 95%: KRW {value({**BASE, 'm_mid': 0.95}):,.0f})" if m_req is None
         else pc(m_req)) + f" (base {pc(OPM_RW)}, 5-yr max {pc(max(ebit_m5))})")
print("Same, with ROIC co-moving with margin (capital per unit of revenue fixed at BASE): required margin = "
      + ("NOT REACHED at <=95%" if m_req2 is None else
         f"{pc(m_req2)} (implied terminal ROIC {pc(BASE['roic'] * m_req2 / OPM_RW)})"))
print(f"Holding BASE margins: required trend/mid-cycle revenue scale = {s_req:.2f}x base "
      f"(Y4 mid-cycle revenue {tn(trend_path(BASE)[3] * s_req)} vs base {tn(trend_path(BASE)[3])})")
print(f"Implied IRR on BASE cash flows at today's price = {pc(irr, 2)} (vs WACC {pc(WACC, 2)})")
print("Years the Y1 peak (run-rate revenue, 70% EBIT) must persist before the BASE downturn/mid-cycle:")
for k in range(1, 7):
    v = value(BASE, peak_years=k)
    print(f"  peak {k} yr(s): KRW {v:,.0f} ({v / PRICE - 1:+.1%})")
k_req = None
for k in range(1, 9):
    if value(BASE, peak_years=k) >= PRICE:
        k_req = k
        break
print(f"  -> price is first covered at peak_years = {k_req}")

D_PCT_SS = base_rows[-1][4] / base_rows[-1][1]          # BASE Y10 D&A / revenue


def through_cycle(g, m=OPM_RW, roic=BASE["roic"]):
    """Look through the cycle: trend revenue at the base-period end, mid-cycle EBIT every year,
    capex = D&A + (g/ROIC) x NOPAT - dWC (value-driver consistent). Custom use of dcf()."""
    cx = D_PCT_SS + g / roic * m * (1 - TAX) - WC * g / (1 + g)
    return dcf(base_revenue=TREND_NOW, growth=[g] * N, ebitda_margin=[m + D_PCT_SS] * N, capex_pct=[cx] * N,
               da_pct=[D_PCT_SS] * N, tax=TAX, wacc=WACC, net_debt=-BRIDGE, shares=SHARES_M,
               terminal_growth=BASE["g_term"], terminal_roic=roic, wc_pct_of_delta_rev=WC,
               mid_year=True, stub_years=STUB).per_share


print(f"\nThrough-cycle view (no peak cash): trend revenue {tn(TREND_NOW)}, EBIT {pc(OPM_RW)} every year, "
      f"D&A {pc(D_PCT_SS)}, value/share by constant growth x ROIC:")
GS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]
print(f"{'ROIC':<8}" + "".join(f"{g:>11.0%}" for g in GS))
for rc in (0.15, 0.25, 0.40):
    print(f"{rc:<8.0%}" + "".join(f"{through_cycle(g, roic=rc):>11,.0f}" for g in GS))

hr("F2. Sensitivity: BASE value/share (KRW) by WACC x terminal growth")
W_GRID = [WACC - 0.02, WACC - 0.01, WACC, WACC + 0.01, WACC + 0.02]
G_GRID = [0.02, 0.025, 0.03, 0.035, 0.04]
grid = sensitivity({"wacc": W_GRID}, {"terminal_growth": G_GRID}, **base_kw)
print(f"{'WACC \\ g':<10}" + "".join(f"{g:>11.1%}" for g in G_GRID))
for w, row in zip(W_GRID, grid):
    print(f"{w:<10.2%}" + "".join(f"{v:>11,.0f}" for v in row))
W_B1 = wacc_of(beta=1.0)[0]
print(f"BASE at beta 1.0 (WACC {pc(W_B1, 2)}): KRW {value({**BASE, 'wacc': W_B1}):,.0f} | "
      f"at OECD rf (WACC {pc(wacc_of(rf=RF_OECD)[0], 2)}): KRW {value({**BASE, 'wacc': wacc_of(rf=RF_OECD)[0]}):,.0f}")

hr("F3. Sensitivity: BASE value/share by mid-cycle EBIT margin x trend-growth path (all else BASE)")
MM = [OPM_SIMPLE, (ON_TREND_PRE + ON_TREND_HBM) / 2, OPM_RW, ON_TREND_HBM, BULL["m_mid"]]
TR = (("bear trend 5%", dict(trend_r=BEAR["trend_r"], g5_10=BEAR["g5_10"])),
      ("base fade", dict(trend_r=BASE["trend_r"], g5_10=BASE["g5_10"])),
      ("fitted 22.4% held", dict(trend_r=BULL["trend_r"], g5_10=BULL["g5_10"])))
print(f"{'margin':<8}" + "".join(f"{lab:>20}" for lab, _ in TR))
for m in MM:
    print(f"{pc(m):<8}" + "".join(f"{value({**BASE, **o, 'm_mid': m}):>20,.0f}" for _, o in TR))
print("Same grid at beta 1.0 WACC:")
for m in MM:
    print(f"{pc(m):<8}" + "".join(f"{value({**BASE, **o, 'm_mid': m, 'wacc': W_B1}):>20,.0f}" for _, o in TR))

# -------------------------------------------------------------------------- G. load-bearing
hr("G. Load-bearing inputs: BASE value/share with each input x0.9 / x1.1 (one at a time)")
V0 = base_r.per_share


def scale_list(key, f):
    return [x * f for x in BASE[key]]


TESTS = [
    ("WACC 13.83% (beta-driven)", lambda f: {"wacc": WACC * f}, "inputs rf + fund beta (Blume) + ERP"),
    ("Raw beta 2.391", lambda f: {"wacc": wacc_of(beta=0.67 * BETA_RAW * f + 0.33)[0]}, "fund: beta"),
    ("Mid-cycle EBIT margin 29.0% (ROIC fixed)", lambda f: {"m_mid": OPM_RW * f}, "facts FY21-25 rev-wtd"),
    ("Mid-cycle margin + ROIC together", lambda f: {"m_mid": OPM_RW * f, "roic": 0.15 * f},
     "facts; capital/revenue fixed"),
    ("Y3 trough cycle factor 0.80x", lambda f: {"f3": 0.80 * f}, "ASSUMPTION (FY2023 0.62)"),
    ("Trend revenue level (FY25 fit 78.9T)", lambda f: {"trend_scale": f}, "facts FY21-25 log fit"),
    ("Trend growth path (22.4%->10%, 9%->4%)", lambda f: {"trend_r": scale_list("trend_r", f),
                                                         "g5_10": scale_list("g5_10", f)}, "ASSUMPTION"),
    ("Y1 revenue 317.3T", lambda f: {"y1_rev": RR_REV * f}, "facts Q2-26 x4"),
    ("Y1 EBIT margin 70%", lambda f: {"m1": 0.70 * f}, "ASSUMPTION (TTM 68.0 / Q2 76.3)"),
    ("Y2 cycle factor 2.0x", lambda f: {"f2": 2.0 * f}, "ASSUMPTION"),
    ("Y2 EBIT margin 55%", lambda f: {"m2": 0.55 * f}, "ASSUMPTION"),
    ("Capex Y1-Y4 (55/60/45/40T)", lambda f: {"capex_scale": f}, "dossier §3 guide + 6-K commitments"),
    ("Terminal/incremental ROIC 15%", lambda f: {"roic": 0.15 * f}, "facts FY23-25 avg ROIC"),
    ("Terminal growth 3%", lambda f: {"g_term": 0.03 * f}, "ASSUMPTION <= min(4%, rf)"),
    ("Tax rate 23.0%", lambda f: {"tax": TAX * f}, "dossier §2 H1-26 effective"),
    ("LT investment assets 85.3T", lambda f: {"lt_scale": f}, "facts H1 LT inv. assets"),
]
out = []
for lab, fn, src in TESTS:
    lo_, hi_ = value({**BASE, **fn(0.9)}), value({**BASE, **fn(1.1)})
    out.append((max(abs(lo_ - V0), abs(hi_ - V0)), lab, lo_, hi_, src))
out.sort(reverse=True)
print(f"BASE = KRW {V0:,.0f}")
print(f"{'input':<42}{'x0.9':>11}{'x1.1':>11}{'max |d|':>10}  source")
for d_, lab, lo_, hi_, src in out:
    print(f"{lab:<42}{lo_:>11,.0f}{hi_:>11,.0f}{d_ / V0:>9.1%}  {src}")
print("\nDiscrete inputs (not +/-10%):")
for lab, v in (("Peak duration 1 -> 2 yrs", value(BASE, peak_years=2)),
               ("Beta 1.932 -> 1.0 (WACC 9.27%)", value({**BASE, "wacc": W_B1})),
               ("LT investment haircut 30% -> 0%", value({**BASE, "lt_haircut": 0.0})),
               ("LT investment haircut 30% -> 100%", value({**BASE, "lt_haircut": 1.0}))):
    print(f"  {lab:<36} KRW {v:>10,.0f} ({v / V0 - 1:+.1%})")
