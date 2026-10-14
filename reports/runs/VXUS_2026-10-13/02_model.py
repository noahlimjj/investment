"""VXUS (Vanguard Total International Stock ETF, US-domiciled RIC) - FUND template model, as of 2026-10-13.

No DCF of a fund (AGENTS.md routing table). Same structure as the VWRA run
(reports/runs/VWRA.L_2026-10-13/03_rerun.py) so the two are comparable:
  M1  Earnings-yield anchor + look-through ROE of the underlying index.
  M2  10-year Bogle decomposition, bear/base/bull:
        net = dividend yield + per-share EPS growth + annualised P/E change - TER
              - source-country WHT (fund level) - investor-level tax - tracking residual
      run for FOUR holders of the SAME ex-US equity exposure:
        (1) "pre-investor-tax": VXUS with no investor-level tax (e.g. a tax-exempt holder);
        (2) VXUS held by a Singapore resident (30% s.871(a) WHT on the whole distribution);
        (3) the ex-US sleeve inside VWRA (Irish UCITS, accumulating, TER 0.14%);
        (4) the Irish ex-US UCITS (IE0009A5ADV9, accumulating, OCF 0.12%).
  M2b Year-by-year simulation (yield moves with the P/E path) - cross-check of the drag.
  M3  Value-driver justified P/E (payout = 1 - g/ROE, same steady state as valuation.dcf() terminal)
      for the reverse solve and the k x g sensitivity grid.

Key identity used: VXUS's observed cash distribution yield (2.35%) is already NET of source-country
WHT (paid at fund level, 7.48% of the cash dividend, 2024 FTC worksheet) and of the 0.05% TER
(ASSUMPTION: RIC expenses paid out of income). So gross underlying yield
  DY_gross = DY_dist * (1 + f) + TER_VX
is a property of the exposure, common to every vehicle; each vehicle then subtracts its own costs.

Labels: ASSUMPTION = Quant-chosen, not sourced. UNKNOWN = set neutral and swept.
Run: python3 reports/runs/VXUS_2026-10-13/02_model.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import peg_is_valid  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
facts = json.loads((RUN / "facts.json").read_text())
inp = json.loads((RUN / "00_inputs.json").read_text())
fund_rec = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["VXUS"]
F = facts["fund"]

# ---------------------------------------------------------------- sourced inputs
PRICE = round(facts["price"]["close_raw"], 2)             # facts: price.close_raw 84.52 (2026-10-13 close)
PRICE_INTRADAY = inp["price"]                             # 00_inputs: 84.405 intraday (conflict, -0.14%)
NAV = facts["price"]["nav"]                               # facts: price.nav 84.58 (date unstated)
CHG12_PX = facts["price"]["change_12m_price_pct"] / 100   # facts: +15.35%
CHG12_TR = facts["price"]["change_12m_total_return_adj_pct"] / 100  # facts: +18.30%
PE0 = 18.3            # dossier §2: factsheet fund P/E 18.3x (index 18.2x), 2026-06-30
PE_IDX = 18.2         # dossier §2
PE_YF = fund_rec["trailing_pe"]                           # fundamentals.json: 16.14x (definition differs)
PB0 = 2.3             # dossier §2: factsheet P/B 2.3x
ROE_FS = 0.133        # dossier §2: factsheet ROE 13.3%
EPSG_FS = 0.126       # dossier §2: factsheet "EPS growth" 12.6% (trailing, backward-looking, horizon unstated)
DIST = F["ttm_distributions_per_share"]                   # facts: 4 quarterly ex-dates, sum 1.985
DIST_TTM = DIST["sum"]
DY_DIST = DIST_TTM / PRICE                                # 2.35% trailing cash distribution yield
DIST_CY2025 = 0.191 + 0.485 + 0.360 + 1.363               # dossier §5: calendar 2025 = 2.399
Q123_2025 = 0.191 + 0.485 + 0.360                         # dossier §5
Q123_2026 = 0.080 + 0.386 + 0.156                         # dossier §5
TER_VX = F["expense_ratio_pct"] / 100                     # facts: 0.05%
TER_VWRA = facts["vwra"]["ocf_pct"] / 100                 # facts: 0.14%
UC = {u["isin"]: u for u in facts["ucits_alternatives"]}
TER_IE_XUS = UC["IE0009A5ADV9"]["ocf_pct"] / 100          # facts: 0.12% (launched 2026-08-18)
TER_ISH_DM = UC["IE000R4ZNTN3"]["ter_pct"] / 100          # facts: 0.15% (MSCI World ex-USA, developed only)
TER_ISH_EM = UC["IE00BKM4GZ66"]["ter_pct"] / 100          # facts: 0.18% (MSCI EM IMI)
FTAX = F["foreign_tax_paid_pct_of_ordinary_div_2024"] / 100   # facts: 7.48% of ordinary cash dividends (2024)
FSRC = F["foreign_source_income_pct_2024"] / 100          # facts: 88.6575% of Box 1a is foreign-source
US_WHT = facts["us_tax_nonresident"]["s871a_withholding_rate_pct"] / 100   # facts: 30% (no SG treaty, dossier §8)
ESTATE_THRESH = facts["us_tax_nonresident"]["form706na_threshold_usd"]     # facts: 60,000
ESTATE_CREDIT = facts["us_tax_nonresident"]["max_unified_credit_usd"]      # facts: 13,000
US_W_VWRA = facts["vwra"]["us_weight_pct"] / 100          # facts: 61.68%
TD_VX = F["tracking_difference_pp"]                       # facts: fund minus WHT-adjusted index, pp
TD_VWRA = facts["vwra"]["tracking_difference_pp_calendar"]  # facts: fund minus benchmark, calendar, pp
NAV_RET = F["returns_asof_2026-06-30"]["nav"]             # facts
RF = inp["risk_free_10y"]["USD"]["value_pct"] / 100       # 00_inputs: 5.22% (FRED DGS10 2026-10-08)
ERP = inp["equity_risk_premium_pct"] / 100                # 00_inputs: 5.0%
FLOOR = inp["discount_rate_floor"]["USD"] / 100           # 00_inputs: 8.0%
SGDUSD = inp["fx_spot_to_usd"]["SGDUSD"]                  # 00_inputs: 0.7812
BETA_RAW = fund_rec.get("beta")                           # fundamentals.json: null
N = 10
NOTIONAL = 10_000.0   # unit normalisation only (position size UNKNOWN)

# ---------------------------------------------------------------- discount rate
BETA = 0.67 * BETA_RAW + 0.33 if BETA_RAW is not None else 1.0
K = max(FLOOR, RF + BETA * ERP)

# ---------------------------------------------------------------- derived look-through
EY = 1 / PE0
ROE_LT = PB0 / PE0                              # look-through ROE = (P/B)/(P/E), same vendor & date
DY_GROSS = DY_DIST * (1 + FTAX) + TER_VX        # underlying yield before source WHT and fund costs
FTAX_NAV = FTAX * DY_DIST                       # source-country WHT as % of NAV (fund level)
PAYOUT = DY_GROSS * PE0
G_HI = ROE_LT * (1 - PAYOUT)                    # all retained earnings reinvested at look-through ROE
G_LO = (1 - PAYOUT) * EY                        # all retained earnings spent on buybacks at E/P


def justified_pe(k, g, roe=ROE_LT):
    return (1 - g / roe) * (1 + g) / (k - g)


def hr(t):
    print("\n" + "=" * 86 + f"\n{t}\n" + "=" * 86)


hr("0. INPUTS & TAPE CHECK")
print(f"Price 2026-10-13 close           {PRICE:8.2f} USD  [facts]; 00_inputs intraday {PRICE_INTRADAY} "
      f"({PRICE_INTRADAY / PRICE - 1:+.2%}) -> close used")
print(f"NAV (date unstated)              {NAV:8.2f} USD  price/NAV {PRICE / NAV - 1:+.2%} indicative only")
print(f"12m price / total return         {CHG12_PX:+8.2%} / {CHG12_TR:+.2%}  [facts]")
print(f"Fund P/E (factsheet 2026-06-30)  {PE0:8.2f}x  index {PE_IDX}x; yfinance {PE_YF:.2f}x [fundamentals.json]")
print(f"P/B {PB0}x  factsheet ROE {ROE_FS:.1%}  factsheet EPS growth {EPSG_FS:.1%} (backward-looking)")
print(f"TTM distributions                {DIST_TTM:8.3f} USD -> yield {DY_DIST:.3%}  [facts]")
print(f"CY2025 distributions             {DIST_CY2025:8.3f} USD -> {DIST_CY2025 / PRICE:.3%} on today's price")
print(f"Q1-Q3 distributions 2026 vs 2025 {Q123_2026:8.3f} vs {Q123_2025:.3f} ({Q123_2026 / Q123_2025 - 1:+.1%})")
print(f"TER VXUS / VWRA / IE ex-US UCITS {TER_VX:.2%} / {TER_VWRA:.2%} / {TER_IE_XUS:.2%}  [facts]")
print(f"Foreign tax paid (2024)          {FTAX:8.2%} of cash dividends; foreign-source {FSRC:.2%} of Box 1a [facts]")
print(f"US NRA WHT (s.871(a))            {US_WHT:8.0%}  on 100% of the RIC dividend (US-source, dossier §8)")
print(f"rf 10y {RF:.2%} (FRED DGS10 2026-10-08); ERP {ERP:.0%}; beta raw {BETA_RAW} -> beta used {BETA:.2f}"
      f" (no vendor beta); k = max({FLOOR:.0%}, rf + beta*ERP) = {K:.2%}")
print(f"SGDUSD {SGDUSD:.4f} [00_inputs]; data warnings: {fund_rec['warnings']}; errors: {fund_rec['errors']}")
print(f"Tape: earnings yield 1/PE {EY:.2%} vs 10y UST {RF:.2%} -> gap {EY - RF:+.2%} "
      f"(yfinance P/E basis {1 / PE_YF:.2%}, gap {1 / PE_YF - RF:+.2%})")

hr("1. LOOK-THROUGH (M1)")
print(f"Earnings yield 1/PE               {EY:7.2%}")
print(f"Look-through ROE = PB/PE          {ROE_LT:7.2%}  (factsheet ROE {ROE_FS:.1%}); vs k {K:.2%} spread {ROE_LT - K:+.2%}")
print(f"Gross underlying DY = DYdist*(1+f)+TER  {DY_GROSS:7.3%}  (DYdist {DY_DIST:.3%}, f {FTAX:.2%}, TER {TER_VX:.2%})")
print(f"Source-country WHT, % of NAV      {FTAX_NAV:7.3%}  = f x DYdist")
print(f"Payout = DY_gross x PE            {PAYOUT:7.2%}")
print(f"Sustainable g envelope            {G_LO:7.2%} (all buybacks at E/P)  to {G_HI:.2%} (all reinvested at ROE_LT)")
print(f"  with factsheet ROE {ROE_FS:.1%}: upper {ROE_FS * (1 - PAYOUT):.2%}")
ok, why = peg_is_valid(PE0, None, EPSG_FS)
print(f"peg_is_valid(PE={PE0}, fwd=None, growth={EPSG_FS}) -> {ok}, '{why}'  [FUND: PEG not used; growth is backward-looking]")
print(f"Lynch ratio (informational, backward growth): ({EPSG_FS * 100:.1f} + {DY_DIST * 100:.2f}) / {PE0} = "
      f"{(EPSG_FS * 100 + DY_DIST * 100) / PE0:.2f}")
print(f"CAPE of ex-US index: UNKNOWN (not in dossier)")
TOP10 = {"TSMC": 4.3, "Samsung": 2.6, "SK hynix": 2.2, "ASML": 1.7, "Tencent": 0.8, "HSBC": 0.7, "Roche": 0.7,
         "Novartis": 0.7, "Royal Bank of Canada": 0.7, "AstraZeneca": 0.6}          # dossier §2 (factsheet 2026-06-30)
SEMIS = ("TSMC", "Samsung", "SK hynix", "ASML")
print(f"Top-10 sum {sum(TOP10.values()):.1f}% (factsheet 15.0%); of which semis/semicap (TSMC, Samsung, SK hynix, ASML) "
      f"{sum(TOP10[x] for x in SEMIS):.1f}%")
XUS_VWRA = 1 - US_W_VWRA
print(f"VWRA ex-US share {XUS_VWRA:.2%} -> US$ of VWRA needed per US$1 of ex-US exposure {1 / XUS_VWRA:.2f} "
      f"(brings US${(1 - XUS_VWRA) / XUS_VWRA:.2f} of US equity with it): VWRA does NOT replicate an ex-US tilt")

# ---------------------------------------------------------------- tax / cost waterfall
VEH = {
    # name: (TER, source-WHT multiplier vs VXUS, investor-level tax rate on cash distribution)
    "VXUS, pre-investor-tax": (TER_VX, 1.0, 0.0),
    "VXUS, Singapore holder": (TER_VX, 1.0, US_WHT),
    "VWRA ex-US sleeve": (TER_VWRA, 1.0, 0.0),
    "IE ex-US UCITS (0.12%)": (TER_IE_XUS, 1.0, 0.0),
}


def drag_terms(ter, fmult, invtax, dy_dist=DY_DIST, exempt=0.0, grossup=False):
    ftax = FTAX * dy_dist * fmult
    base = dy_dist * (1 + FTAX) if grossup else dy_dist
    inv = invtax * (1 - exempt) * base
    return ter, ftax, inv, ter + ftax + inv


hr("2. COST & TAX WATERFALL on the same ex-US exposure (bp/yr of NAV)")
print(f"{'vehicle':26s}{'TER':>8s}{'src WHT':>9s}{'US WHT':>9s}{'TOTAL':>8s}{'vs VXUS-SG':>12s}")
tot = {name: drag_terms(*VEH[name])[3] for name in VEH}
for name, (ter, fm, it) in VEH.items():
    t, f_, i_, s = drag_terms(ter, fm, it)
    print(f"{name:26s}{t * 1e4:8.1f}{f_ * 1e4:9.1f}{i_ * 1e4:9.1f}{s * 1e4:8.1f}"
          f"{(tot['VXUS, Singapore holder'] - s) * 1e4:12.1f}")
D_VWRA = tot["VXUS, Singapore holder"] - tot["VWRA ex-US sleeve"]
D_IE = tot["VXUS, Singapore holder"] - tot["IE ex-US UCITS (0.12%)"]
print(f"Annual drag difference: VXUS-SG minus VWRA sleeve = {D_VWRA * 1e4:.1f} bp; minus IE ex-US UCITS = {D_IE * 1e4:.1f} bp")
print(f"Of which US 30% WHT {US_WHT * DY_DIST * 1e4:.1f} bp, TER advantage of VXUS {(TER_VX - TER_VWRA) * 1e4:+.1f} bp "
      f"(vs VWRA) / {(TER_VX - TER_IE_XUS) * 1e4:+.1f} bp (vs IE ex-US)")
print(f"Source-country WHT ({FTAX_NAV * 1e4:.1f} bp) is unusable for a SG holder in EVERY wrapper; base assumes the Irish"
      f" funds suffer the same rate (UNKNOWN) -> 0 bp differential. A US taxpayer recovers it via the FTC.")
tax_gross = DY_DIST * (1 + FTAX)
print(f"Effective total tax on underlying dividends (pre-TER): VXUS-SG {(FTAX_NAV + US_WHT * DY_DIST) / tax_gross:.1%}"
      f" vs Irish wrapper {FTAX_NAV / tax_gross:.1%}")
print(f"Breakevens: VXUS-SG = VWRA sleeve if effective US WHT <= {(TER_VWRA - TER_VX) / DY_DIST:.2%} "
      f"or distribution yield <= {(TER_VWRA - TER_VX) / US_WHT:.3%}; vs IE ex-US: WHT <= "
      f"{(TER_IE_XUS - TER_VX) / DY_DIST:.2%} or yield <= {(TER_IE_XUS - TER_VX) / US_WHT:.3%}")
lo_blend, hi_blend = min(TER_ISH_DM, TER_ISH_EM), max(TER_ISH_DM, TER_ISH_EM)
print(f"iShares two-fund (World ex-USA {TER_ISH_DM:.2%} + EM IMI {TER_ISH_EM:.2%}): blended TER {lo_blend:.2%}-{hi_blend:.2%}"
      f" (weights UNKNOWN) -> drag diff {(US_WHT * DY_DIST - (hi_blend - TER_VX)) * 1e4:.1f}-"
      f"{(US_WHT * DY_DIST - (lo_blend - TER_VX)) * 1e4:.1f} bp")


# ---------------------------------------------------------------- M2 Bogle decomposition
def bogle(dy_dist, g, pe_end, pe0=PE0, ter=TER_VX, fmult=1.0, invtax=0.0, exempt=0.0, grossup=False,
          td_resid=0.0, ter_in_income=True, n=N):
    v = (pe_end / pe0) ** (1 / n) - 1
    dy_gross = dy_dist * (1 + FTAX) + (TER_VX if ter_in_income else 0.0)
    _, ftax, inv, _ = drag_terms(ter, fmult, invtax, dy_dist, exempt, grossup)
    gross = (1 + g) * (1 + v) - 1 + dy_gross
    net = gross - ter - ftax - inv - td_resid
    return dict(v=v, dy_gross=dy_gross, ftax=ftax, inv=inv, gross=gross, net=net)


def hev(net, k=K, price=PRICE, n=N):
    """Hurdle-equivalent value: price today at which this net return equals k. NOT a fair value."""
    return price * ((1 + net) / (1 + k)) ** n


PE_BEAR = justified_pe(0.08, 0.02)   # same rule as VWRA run: bear exit = M3 justified at k 8% / g 2%
PE_BULL = justified_pe(0.08, 0.05)   # same rule as VWRA run: bull exit ~ M3 justified at k 8% / g 5%
SCEN = {
    #        distribution yield  per-share EPS g (ASSUMPTION)        exit P/E yr10
    "Bear": dict(dy_dist=DY_DIST, g=0.030, pe_end=round(PE_BEAR, 1)),
    "Base": dict(dy_dist=DY_DIST, g=0.050, pe_end=PE0),
    "Bull": dict(dy_dist=DY_DIST, g=round(G_HI, 4), pe_end=round(PE_BULL, 1)),
}

hr("3. 10-YEAR SCENARIOS (M2, nominal USD, additive decomposition as in the VWRA run)")
print(f"Exit P/E rule (VWRA-comparable): bear = justified(k 8%, g 2%, ROE {ROE_LT:.2%}) = {PE_BEAR:.2f}x; "
      f"bull = justified(k 8%, g 5%) = {PE_BULL:.2f}x; base = no re-rating")
print(f"{'':5s}{'DYdist':>7s}{'EPS g':>7s}{'PE10':>6s}{'v/yr':>7s}{'DYgross':>8s}{'gross':>7s} | "
      f"{'pre-tax':>8s}{'VXUS-SG':>8s}{'VWRAslv':>8s}{'IE xUS':>8s} | {'diff bp':>7s}{'ERP SG':>7s}{'ERP VW':>7s}")
RES = {}
for nm, s in SCEN.items():
    rr = {v: bogle(**s, ter=VEH[v][0], fmult=VEH[v][1], invtax=VEH[v][2]) for v in VEH}
    RES[nm] = rr
    a, b, c, d = (rr[v]["net"] for v in VEH)
    print(f"{nm:5s}{s['dy_dist']:7.2%}{s['g']:7.2%}{s['pe_end']:6.1f}{rr['VXUS, pre-investor-tax']['v']:7.2%}"
          f"{rr['VXUS, pre-investor-tax']['dy_gross']:8.2%}{rr['VXUS, pre-investor-tax']['gross']:7.2%} | "
          f"{a:8.2%}{b:8.2%}{c:8.2%}{d:8.2%} | {(c - b) * 1e4:7.1f}{b - RF:+7.2%}{c - RF:+7.2%}")
b = RES["Base"]
print(f"Base composition (VXUS-SG): DYgross {b['VXUS, Singapore holder']['dy_gross']:.2%} + EPS g 5.00% + re-rating 0.00% "
      f"- TER {TER_VX:.2%} - source WHT {FTAX_NAV:.2%} - US WHT {US_WHT * DY_DIST:.2%} = {b['VXUS, Singapore holder']['net']:.2%}")
print(f"Base composition (VWRA sleeve): DYgross {b['VWRA ex-US sleeve']['dy_gross']:.2%} + 5.00% + 0.00% "
      f"- TER {TER_VWRA:.2%} - source WHT {FTAX_NAV:.2%} = {b['VWRA ex-US sleeve']['net']:.2%}")

hr(f"3b. 10-YR WEALTH per US${NOTIONAL:,.0f} (and per S${NOTIONAL:,.0f} at constant spot FX {SGDUSD:.4f})")
print(f"{'':5s}{'VXUS-SG':>10s}{'VWRA slv':>10s}{'IE xUS':>10s}{'pre-tax':>10s} | {'VW-SG $':>8s}{'IE-SG $':>8s}"
      f"{'VW-SG %':>8s} | {'VW-SG S$':>9s} | {'HEV SG':>7s}{'HEV VW':>7s}")
for nm in SCEN:
    w = {v: NOTIONAL * (1 + RES[nm][v]["net"]) ** N for v in VEH}
    sg, vw, ie, pt = w["VXUS, Singapore holder"], w["VWRA ex-US sleeve"], w["IE ex-US UCITS (0.12%)"], w["VXUS, pre-investor-tax"]
    print(f"{nm:5s}{sg:10,.0f}{vw:10,.0f}{ie:10,.0f}{pt:10,.0f} | {vw - sg:8,.0f}{ie - sg:8,.0f}{vw / sg - 1:8.2%} | "
          f"{(vw - sg):9,.0f} | {hev(RES[nm]['VXUS, Singapore holder']['net']):7.2f}{hev(RES[nm]['VWRA ex-US sleeve']['net']):7.2f}")
print("S$ column: a S$10,000 stake = US$" f"{NOTIONAL * SGDUSD:,.0f}; at constant FX the S$ gap equals the US$ gap per 10,000 "
      "units (FX drift UNKNOWN, identical for both USD wrappers, so the DIFFERENCE is FX-neutral).")
print(f"SGD holder: USD/SGD drift UNKNOWN; each +/-1%/yr of USD move scales the absolute 10-yr SGD outcome by "
      f"x{1.01 ** N:.3f} / x{0.99 ** N:.3f} for BOTH wrappers")
print(f"Lost wealth from the drag alone (base): {1 - ((1 + b['VXUS, Singapore holder']['net']) / (1 + b['VWRA ex-US sleeve']['net'])) ** N:.2%}"
      f" of the VWRA-sleeve outcome over 10y; {1 - ((1 + b['VXUS, Singapore holder']['net']) / (1 + b['VXUS, pre-investor-tax']['net'])) ** N:.2%}"
      f" vs a holder with no investor-level tax")
print(f"HEV = price at which the scenario earns exactly k {K:.2%}; NOT a fair value (NAV is). Terminal share 100% by construction.")
erp_vw = b["VWRA ex-US sleeve"]["net"] - RF
print(f"Base implied ERP: VWRA sleeve {erp_vw:+.2%}, VXUS-SG {b['VXUS, Singapore holder']['net'] - RF:+.2%} -> the "
      f"{D_VWRA * 1e4:.1f} bp drag consumes {D_VWRA / erp_vw:.0%} of the ex-US equity premium")


# ---------------------------------------------------------------- M2b year-by-year simulation
def simulate(g, pe_end, ter, invtax, dy0=DY_DIST, pe0=PE0, n=N, fmult=1.0, exempt=0.0):
    """Dividends grow with EPS; P/E moves geometrically; net cash distribution reinvested at year-end price."""
    w = 1.0
    r = (pe_end / pe0) ** (1 / n)
    for t in range(1, n + 1):
        pe_prev, pe_t = pe0 * r ** (t - 1), pe0 * r ** t
        p = (1 + g) * pe_t / pe_prev - 1
        dist = dy0 * (1 + g) ** 1 * pe0 / pe_prev        # VXUS cash dist on start-of-year price
        ftax = FTAX * dist
        y_gross = dist + ftax + TER_VX
        net = p + y_gross - ter - ftax * fmult - invtax * (1 - exempt) * dist
        w *= 1 + net
    return w ** (1 / n) - 1, w


hr("4. CROSS-CHECK (M2b): year-by-year, yield moves with the P/E path, dividends grow with EPS")
for nm, s in SCEN.items():
    sg, wsg = simulate(s["g"], s["pe_end"], TER_VX, US_WHT)
    vw, wvw = simulate(s["g"], s["pe_end"], TER_VWRA, 0.0)
    ie, wie = simulate(s["g"], s["pe_end"], TER_IE_XUS, 0.0)
    print(f"{nm:5s} VXUS-SG {sg:6.2%}  VWRA sleeve {vw:6.2%}  IE xUS {ie:6.2%}  diff {(vw - sg) * 1e4:5.1f} bp / "
          f"{(ie - sg) * 1e4:5.1f} bp   10y wealth gap per US$10k {NOTIONAL * (wvw - wsg):6,.0f} / {NOTIONAL * (wie - wsg):6,.0f}")

hr("5. REVERSE SOLVES ('what must be true?')")
print("(a) per-share EPS growth needed for the after-tax net return to hit a target (base yield, costs)")
for tgt_lbl, tgt in (("UST 5.22% (ERP 0)", RF), ("UST + 3%", RF + 0.03), ("UST + 4%", RF + 0.04), (f"CAPM k {K:.2%}", K)):
    cells = []
    for pe_end in (round(PE_BEAR, 1), PE_YF, PE0, round(PE_BULL, 1)):
        v = (pe_end / PE0) ** (1 / N) - 1
        need_sg = (tgt - DY_DIST * (1 - US_WHT) + 1) / (1 + v) - 1
        need_vw = (tgt - (DY_DIST + TER_VX - TER_VWRA) + 1) / (1 + v) - 1
        cells.append(f"{pe_end:5.1f}x SG {need_sg:5.2%} VW {need_vw:5.2%}")
    print(f"  {tgt_lbl:18s}: " + " | ".join(cells))
print(f"  -> holding VXUS instead of the VWRA sleeve needs ~{D_VWRA / 1:.2%}/yr more EPS growth for the same outcome")


def implied_g(k, roe, pe=PE0):
    lo, hi = -0.05, k - 1e-4
    for _ in range(200):
        mid = (lo + hi) / 2
        if justified_pe(k, mid, roe) < pe:
            lo = mid
        else:
            hi = mid
    return mid


print(f"(b) perpetual nominal growth implied by P/E {PE0}x (value-driver, payout = 1 - g/ROE)")
for k in (0.08, RF + 0.04, K, K + 0.01):
    print(f"  k={k:6.2%}: " + "  ".join(f"ROE {roe:5.2%} -> g {implied_g(k, roe):6.2%}"
                                      for roe in (0.10, ROE_LT, ROE_FS, 0.16)))
print(f"  terminal-growth cap = min(4%, 10y {RF:.2%}) = 4%")
print(f"(c) market-implied perpetual k at {PE0}x (ROE_LT {ROE_LT:.2%}): "
      + "  ".join(f"g {g:.0%} -> k {(1 - g / ROE_LT) * (1 + g) / PE0 + g:6.2%} (ERP {(1 - g / ROE_LT) * (1 + g) / PE0 + g - RF:+.2%})"
                  for g in (0.03, 0.04)))


def value_ps(k, g, roe=ROE_LT):
    return PRICE * justified_pe(k, g, roe) / PE0


hr(f"6. SENSITIVITY (M3, index level, pre-investor-tax): value/share = price x justified PE / {PE0}  (ROE {ROE_LT:.2%})")
gs = (0.02, 0.03, 0.04, 0.05)
print("k \\ g        " + "".join(f"{g:>10.0%}" for g in gs) + "    (5% column exceeds the 4% cap; reference only)")
for k in (0.08, K - 0.01, K, K + 0.01):
    tag = " (VWRA-run comparability)" if k == 0.08 else ""
    print(f"{k:<12.2%} " + "".join(f"{value_ps(k, g):10.2f}" for g in gs) + tag)
print("justified P/E:")
for k in (0.08, K - 0.01, K, K + 0.01):
    print(f"{k:<12.2%} " + "".join(f"{justified_pe(k, g):9.1f}x" for g in gs))

hr("7. 10-YR AFTER-TAX NET RETURN GRID, VXUS-SG (M2): exit P/E x per-share EPS growth; [VWRA-sleeve = +diff]")
pes = (round(PE_BEAR, 1), PE_YF, PE0, round(PE_BULL, 1), 24.0)
print("g \\ exitPE  " + "".join(f"{p:>9.1f}x" for p in pes))
for g in (0.02, 0.03, 0.04, 0.05, 0.06, round(G_HI, 4)):
    print(f"{g:<11.2%} " + "".join(f"{bogle(DY_DIST, g, p, invtax=US_WHT)['net']:10.2%}" for p in pes))

hr("8. SWEEPS on the DRAG DIFFERENTIAL (VXUS-SG minus VWRA sleeve, base) and VXUS-SG base net")
base_sg = RES["Base"]["VXUS, Singapore holder"]["net"]


def diff(sg_kw=None, vw_kw=None, s=None):
    s = s or SCEN["Base"]
    a = bogle(**{**s, "invtax": US_WHT, "ter": TER_VX, **(sg_kw or {})})["net"]
    c = bogle(**{**s, "ter": TER_VWRA, **(vw_kw or {})})["net"]
    return (c - a), a


sweeps = [
    ("base", {}, {}, None),
    ("yield 2.84% (CY2025 dists on today's price)", {}, {}, {**SCEN["Base"], "dy_dist": DIST_CY2025 / PRICE}),
    ("yield -10% (2.11%)", {}, {}, {**SCEN["Base"], "dy_dist": DY_DIST * 0.9}),
    ("10% of payout s.871(k)-exempt (HYPOTHETICAL)", {"exempt": 0.10}, {}, None),
    ("25% of payout s.871(k)-exempt (HYPOTHETICAL)", {"exempt": 0.25}, {}, None),
    ("30% also withheld on s.853 FTC gross-up (UNKNOWN)", {"grossup": True}, {}, None),
    ("Irish source WHT 50% higher than VXUS's (UNKNOWN)", {}, {"fmult": 1.5}, None),
    ("Irish source WHT 50% lower than VXUS's (UNKNOWN)", {}, {"fmult": 0.5}, None),
    ("VXUS expenses NOT paid from income", {"ter_in_income": False}, {"ter_in_income": False}, None),
    ("vehicle cost = TD: VXUS 10y TD 0.00, VWRA mean cal. TD", {"ter": 0.0},
     {"ter": -sum(TD_VWRA.values()) / len(TD_VWRA) / 100}, None),
    ("vehicle cost = TD: VXUS 5y TD +0.14 (beat index)", {"ter": -TD_VX["5y"] / 100},
     {"ter": -sum(TD_VWRA.values()) / len(TD_VWRA) / 100}, None),
    ("vs IE ex-US UCITS 0.12% instead of VWRA", {}, {"ter": TER_IE_XUS}, None),
    ("vs IE ex-US + 0.10% unknown TD residual", {}, {"ter": TER_IE_XUS, "td_resid": 0.001}, None),
    ("small-cap return gap +/-0.10%/yr (UNKNOWN), per 0.10", {}, {"td_resid": 0.001}, None),
]
for lbl, skw, vkw, s in sweeps:
    d, a = diff(skw, vkw, s)
    print(f"  {lbl:55s} diff {d * 1e4:6.1f} bp   VXUS-SG net {a:6.2%}   10y gap/US$10k "
          f"{NOTIONAL * ((1 + a + d) ** N - (1 + a) ** N):6,.0f}")
print(f"  VWRA calendar TD mean 2020-25 = {sum(TD_VWRA.values()) / len(TD_VWRA):+.3f} pp (fund-benchmark); VXUS TD "
      f"1/3/5/10y = {TD_VX['1y']:+.2f}/{TD_VX['3y']:+.2f}/{TD_VX['5y']:+.2f}/{TD_VX['10y']:+.2f} pp vs a WHT-adjusted index."
      " Benchmarks' WHT bases differ, so TD rows are indicative only.")

hr("9. ONE-OFF SWITCH COST PAYBACK and $ drag (switch costs UNKNOWN; HYPOTHETICAL grid)")
for c in (0.0010, 0.0025, 0.0050, 0.0100):
    print(f"  one-off cost {c * 1e4:5.0f} bp -> payback {c / D_VWRA:5.2f} yrs vs VWRA sleeve, {c / D_IE:5.2f} yrs vs IE ex-US")
print(f"  annual US WHT paid per US$10,000 of VXUS at today's yield: US${NOTIONAL * DY_DIST * US_WHT:,.2f}; "
      f"net drag vs VWRA sleeve: US${NOTIONAL * D_VWRA:,.2f}")
print(f"  Estate: VXUS is US-situs (dossier §8). Form 706-NA if US-situs > US${ESTATE_THRESH:,}; credit US${ESTATE_CREDIT:,}."
      " Rate schedule UNKNOWN, position size UNKNOWN, aggregate US-situs holdings UNKNOWN -> not in the bp figures.")

hr("10. LOAD-BEARING INPUTS (+/-10%, one at a time, everything else fixed)")
print(f"(a) on VXUS-SG base after-tax net {base_sg:.2%} and HEV {hev(base_sg):.2f} (k {K:.2%})")


def sg_net(**over):
    s = dict(dy_dist=DY_DIST, g=0.05, pe_end=PE0, pe0=PE0, ter=TER_VX, invtax=US_WHT)
    s.update(over)
    return bogle(**s)["net"]


rows = []
for name, key, bv in (("exit P/E (yr 10)", "pe_end", PE0), ("per-share EPS growth", "g", 0.05),
                      ("distribution yield", "dy_dist", DY_DIST), ("US WHT rate", "invtax", US_WHT),
                      ("TER (VXUS)", "ter", TER_VX)):
    lo, hi = sg_net(**{key: bv * 0.9}), sg_net(**{key: bv * 1.1})
    rows.append((name, lo, hi))
for name, lo, hi in sorted(rows, key=lambda x: -abs(hev(x[2]) - hev(x[1]))):
    print(f"  {name:24s} -10%: net {lo:6.2%} HEV {hev(lo):6.2f} ({hev(lo) / hev(base_sg) - 1:+6.1%})   "
          f"+10%: net {hi:6.2%} HEV {hev(hi):6.2f} ({hev(hi) / hev(base_sg) - 1:+6.1%})")
for kk in (K * 0.9, K * 1.1):
    print(f"  hurdle k {kk:6.2%}            HEV {hev(base_sg, k=kk):6.2f} ({hev(base_sg, k=kk) / hev(base_sg) - 1:+6.1%})  net unchanged")
pe_meas = bogle(DY_DIST, 0.05, PE_YF, pe0=PE_YF, invtax=US_WHT)["net"]
pe_meas_bear = bogle(DY_DIST, 0.03, round(PE_BEAR, 1), pe0=PE_YF, invtax=US_WHT)["net"]
print(f"  starting P/E measurement {PE0}x -> {PE_YF:.2f}x (exit follows definition): base {pe_meas:6.2%} (unchanged); "
      f"bear (absolute {round(PE_BEAR, 1)}x exit) {pe_meas_bear:6.2%} vs {RES['Bear']['VXUS, Singapore holder']['net']:6.2%}")
pv = value_ps(K, 0.04)
for lbl, v in (("ROE_LT -10% (M3)", value_ps(K, 0.04, ROE_LT * 0.9)), ("ROE_LT +10% (M3)", value_ps(K, 0.04, ROE_LT * 1.1)),
               ("terminal g 3.6% (M3)", value_ps(K, 0.036)), ("terminal g 4.4% (M3)", value_ps(K, 0.044))):
    print(f"  {lbl:24s} M3 value {v:6.2f} ({v / pv - 1:+6.1%}) vs centre {pv:.2f} (k {K:.2%}, g 4%)")
print(f"(b) on the DRAG DIFFERENTIAL, base {D_VWRA * 1e4:.1f} bp (vs VWRA sleeve)")
for name, skw_lo, skw_hi, vkw_lo, vkw_hi, s_lo, s_hi in (
        ("distribution yield", {}, {}, {}, {}, {**SCEN["Base"], "dy_dist": DY_DIST * 0.9}, {**SCEN["Base"], "dy_dist": DY_DIST * 1.1}),
        ("US WHT rate", {"invtax": US_WHT * 0.9}, {"invtax": US_WHT * 1.1}, {}, {}, None, None),
        ("TER VWRA", {}, {}, {"ter": TER_VWRA * 0.9}, {"ter": TER_VWRA * 1.1}, None, None),
        ("TER VXUS", {"ter": TER_VX * 0.9}, {"ter": TER_VX * 1.1}, {}, {}, None, None),
        ("Irish source-WHT ratio", {}, {}, {"fmult": 0.9}, {"fmult": 1.1}, None, None),
        ("EPS growth", {}, {}, {}, {}, {**SCEN["Base"], "g": 0.045}, {**SCEN["Base"], "g": 0.055}),
        ("exit P/E", {}, {}, {}, {}, {**SCEN["Base"], "pe_end": PE0 * 0.9}, {**SCEN["Base"], "pe_end": PE0 * 1.1})):
    lo, _ = diff(skw_lo, vkw_lo, s_lo)
    hi, _ = diff(skw_hi, vkw_hi, s_hi)
    print(f"  {name:24s} -10%: {lo * 1e4:6.1f} bp   +10%: {hi * 1e4:6.1f} bp")
print("  (additive M2 holds the yield constant, so exit P/E and EPS growth leave the bp gap unchanged; M2b §4 shows the"
      " de-rating path raises the gap)")
