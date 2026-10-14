"""RVMD (Revolution Medicines) rNPV model -- Quant stage, as of 2026-10-13.

Template: rNPV (routing in 01_research.md section 0), structured on methodologies/rvmd_dcf.py
but with every input re-derived from 01_research.md (dossier), facts.json (facts) and
data/fundamentals.json (fund). NO scenario probabilities here (Skeptic's job).

Changes vs the 28-Aug template (rvmd_dcf.py), each deliberate:
  1. Cash is the 30-Jun-2026 balance, so only H2-2026 flows are modelled for 2026
     (the template charged full-year 2026 opex against 30-Jun cash = H1 burn counted twice).
  2. H2-2026 opex is derived from FY26 guidance minus H1 actual opex (dossier s2, s3).
  3. NOL: no sourced NOL figure exists. Accumulated deficit (facts) used as an UPPER-BOUND
     proxy; NOL=0 case shown in the load-bearing table.
  4. Peak sales: NO sourced figure exists (dossier s9: consensus peak sales UNKNOWN, prior
     sell-side numbers banned/unverified). Segment peaks below are QUANT ASSUMPTIONS, labelled
     as such; the reverse solve (implied peak) is the primary output.
  5. Royalty-sale liability ($548.5M) is NOT deducted as debt: the royalty cash flows are
     modelled explicitly; deducting both would double-count.
  6. One discount rate (CAPM build) across scenarios; scenario differences are in cash flows.
  7. SBC treatment: GAAP opex (which includes SBC) is treated as cash cost. Share count is
     NOT grown for SBC. (Deduct, never both, never neither.)
"""
from __future__ import annotations

import json
import pathlib
import sys

RUN = pathlib.Path(__file__).resolve().parent
ROOT = RUN.parents[2]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import dcf, reverse_dcf, sensitivity, peg_is_valid, fcf_yield  # noqa: E402

facts = json.loads((RUN / "facts.json").read_text())
fund = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["RVMD"]
M = 1e6

# ----------------------------------------------------------------------------- inputs
PRICE = fund["price"]                                         # fund: 193.95
SHARES = facts["shares_outstanding_latest"]["val"] / M        # facts: 214.336M (10-Q cover 31 Jul 26)
MCAP = PRICE * SHARES                                         # $M
bs = facts["balance_sheet_2026_06_30"]
CASH = bs["cash_plus_ms"]                                     # facts: 3,937.969
CONVERTS = bs["convertible_notes_2033_principal"]             # facts: 500.0
ROY_LIAB = bs["liability_related_to_sale_of_future_royalties"]  # facts: 548.542 (NOT deducted, see note 5)
WARRANTS = bs["warrant_liability"]                            # facts: 185.253 (debt-like claim)
EQUITY_BV = bs["equity"]                                      # facts: 2,606.238
ACC_DEFICIT = bs["accumulated_deficit"]                       # facts: 3,967.289 -> NOL upper-bound proxy
US10Y = facts["market"]["us10y_pct"]["value"] / 100           # facts: 5.20% (yfinance ^TNX, not cross-checked)

H1_26_OPEX = 950.4                                            # dossier s2 (10-Q)
FY26_OPEX_GUIDE = (2_100.0, 2_200.0)                          # dossier s3 (8-K ex99.1)
FY26_SBC_GUIDE = (270.0, 290.0)                               # dossier s3
H1_26_CFO = facts["quarter_q2_2026"]["h1_2026_cfo"]           # facts: -741.484
Q3_REV_CONSENSUS = 24.1                                       # dossier s3/s9, labelled CONSENSUS
WAC_30D = 39_800.0                                            # dossier s8, $ per 30-day supply
TERM_LOAN_SPREAD, SOFR_FLOOR = 0.0575, 0.035                  # dossier s3 (10-Q note 8-9)

# Royalty Pharma tiers after tranches 1-2 (dossier s3): annual WW net sales, $B
RP_TIERS = [(2.0, 0.0455), (4.0, 0.0250), (8.0, 0.0100), (1e9, 0.0)]

# ---- QUANT ASSUMPTIONS (unsourced; each appears in section G of 02_quant.md) ----
TAX = 0.21           # US federal statutory; state tax UNKNOWN
COGS = 0.10          # COGS % net sales: UNKNOWN (no product COGS reported yet)
DA_CAPEX = 0.01      # D&A = capex = 1% of revenue (FY25 capex 16, D&A 8-17 on zero revenue)
LOE_DARAX = 2042     # daraxonrasib loss of exclusivity: patent expiry UNKNOWN in dossier
LOE_NEXT = 2046      # zoldonrasib / elironrasib / other: UNKNOWN
DECAY = 0.70         # post-LOE annual revenue retention (oral small molecule generic erosion)
SGA_FIXED, SGA_VAR = 450.0, 0.15   # SG&A = fixed + var x revenue (Q2-26 G&A 110/qtr x4 = 441)
RD_2027 = 1_800.0    # ~75% of H2-26 annualised opex (Q2-26 R&D share was 78%)
LAST_YEAR = 2050
TODAY_ROLL_DAYS = 105  # 2026-06-30 -> 2026-10-13

# ----------------------------------------------------------------------------- discount rate
ERP, BETA = 0.05, 1.0                                 # ERP stated; beta unsourced -> 1.0
KE = US10Y + BETA * ERP
KD_PRE = SOFR_FLOOR + TERM_LOAN_SPREAD                # marginal secured cost (term-loan floor rate)
KD_TAX = 0.0                                          # no taxable income -> no current tax shield
D_MKT = CONVERTS + ROY_LIAB                           # converts at principal + royalty liability carrying
WACC_RAW = (MCAP * KE + D_MKT * KD_PRE * (1 - KD_TAX)) / (MCAP + D_MKT)
WACC = max(WACC_RAW, 0.08)                            # USD floor 8%


def rp_royalty(sales_m: float, scale: float = 1.0) -> float:
    owed, lo, s = 0.0, 0.0, sales_m / 1000
    for hi, rate in RP_TIERS:
        if s <= lo:
            break
        owed += (min(s, hi) - lo) * rate * scale
        lo = hi
    return owed * 1000


def seg_rev(y, peak, launch, ytp, loe, first=None, decay=DECAY):
    """Ramp to peak over ytp years after launch, flat, then post-LOE geometric erosion."""
    if y < launch:
        return 0.0
    if y == launch:
        return first if first is not None else peak * 0.25 / ytp
    if y >= loe:
        return peak * decay ** (y - loe + 1)
    f = min(1.0, (y - launch) / ytp)
    return peak * f ** 0.85


# Segment peaks, $M WW net sales: QUANT ASSUMPTIONS (no sourced figure exists).
# (name, launch year, years-to-peak, LOE, {bear, base, bull} peak)
SEGMENTS = [
    ("2L+ mPDAC (approved)",          2026, 5, LOE_DARAX, {"BEAR": 1_500, "BASE": 2_500, "BULL": 3_000}),
    ("1L mPDAC (RASolute 303/305)",   2028, 6, LOE_DARAX, {"BEAR": 0,     "BASE": 3_500, "BULL": 5_000}),
    ("2L RAS NSCLC (RASolve 301)",    2028, 5, LOE_DARAX, {"BEAR": 0,     "BASE": 1_500, "BULL": 2_500}),
    ("1L G12C/G12D NSCLC (307/308)",  2030, 6, LOE_NEXT,  {"BEAR": 0,     "BASE": 2_000, "BULL": 3_000}),
    ("Adjuvant PDAC / CRC / other",   2030, 6, LOE_NEXT,  {"BEAR": 0,     "BASE": 0,     "BULL": 2_000}),
]
Q4_MULT = {"BEAR": 1.0, "BASE": 2.0, "BULL": 3.0}       # Q4-26 revenue = k x Q3 consensus
# R&D path: (2027 level, plateau, plateau year, post-failure R&D as % of revenue, cut year)
# BEAR: Ph3s already running are committed through 2028; after 1L-PDAC and NSCLC failures the
# company resizes R&D to 30% of revenue (min $400M) -- opex flexes, per valuation.py docstring.
RD = {"BEAR": (RD_2027, 1_800, 2027, 0.30, 2029),
      "BASE": (RD_2027, 2_300, 2029, None, None),
      "BULL": (RD_2027, 2_800, 2030, None, None)}


def run(sc, *, wacc=WACC, peak_scale=1.0, cogs=COGS, rd_scale=1.0, sga_fixed=SGA_FIXED,
        sga_var=SGA_VAR, loe_shift=0, decay=DECAY, ytp_scale=1.0, tax=TAX, nol0=ACC_DEFICIT,
        roy_scale=1.0, cash=CASH, shares=SHARES, h2_opex=None, floor=True):
    h2_opex = h2_opex if h2_opex is not None else sum(FY26_OPEX_GUIDE) / 2 - H1_26_OPEX
    years = list(range(2026, LAST_YEAR + 1))
    rows, pv, nol, bal, trough = [], 0.0, nol0, cash - 0.0, (cash, 2026)
    peak_total = 0.0
    revs = {}
    for y in years:
        r = 0.0
        for name, launch, ytp, loe, peaks in SEGMENTS:
            p = peaks[sc] * peak_scale
            if p == 0:
                continue
            first = (Q3_REV_CONSENSUS * (1 + Q4_MULT[sc])) if launch == 2026 else None  # consensus-anchored, not scaled
            r += seg_rev(y, p, launch, max(1, round(ytp * ytp_scale)), loe + loe_shift, first, decay)
        revs[y] = r
        peak_total = max(peak_total, r)
    for y in years:
        r = revs[y]
        if y == 2026:
            rd_sga = h2_opex                                   # GAAP opex incl SBC, H2 only
            rd = sga = None
        else:
            r0, plat, plat_y, cut, cut_y = RD[sc]
            if cut is not None and y >= cut_y:
                rd = max(400.0, cut * r)
            elif y >= plat_y:
                rd = plat
            else:
                rd = r0 + (plat - r0) * (y - 2027) / max(1, plat_y - 2027)
            # post-LOE wind-down: with TV = 0 no successor products are credited, so spend
            # that would create them is not charged either; R&D and fixed SG&A flex with revenue
            wind = min(1.0, r / peak_total) if (peak_total and y >= LOE_DARAX + loe_shift) else 1.0
            rd *= wind * rd_scale
            sga = sga_fixed * wind + sga_var * r
            rd_sga = rd + sga
        roy = rp_royalty(r, roy_scale)
        ebit = r - r * cogs - roy - rd_sga
        if ebit < 0:
            nol += -ebit
            tx = 0.0
        else:
            used = min(ebit, nol)
            nol -= used
            tx = (ebit - used) * tax
        fcf = ebit - tx                                        # D&A ~= capex; WC ignored (stated)
        t = 0.25 if y == 2026 else (y - 2026)
        df = 1 / (1 + wacc) ** t
        pv += fcf * df
        bal += fcf
        if bal < trough[0]:
            trough = (bal, y)
        rows.append((y, r, rd, sga, rd_sga, roy, ebit, tx, fcf, fcf * df, bal))
    net_cash = cash - CONVERTS - WARRANTS
    eq_raw = pv + net_cash
    eq = max(eq_raw, net_cash) if floor else eq_raw
    roll = (1 + wacc) ** (TODAY_ROLL_DAYS / 365)
    return dict(sc=sc, rows=rows, revs=revs, pv=pv, eq=eq, eq_raw=eq_raw,
                ps=eq * roll / shares, ps_raw=eq_raw * roll / shares,
                peak=peak_total, trough=trough, net_cash=net_cash)


def hdr(t):
    print("\n" + "=" * 92 + f"\n{t}\n" + "=" * 92)


# ============================================================================= 1. snapshot
hdr("1. SNAPSHOT AND EV BUILD (USD M)")
print(f"Price ${PRICE:.2f} (fund) x shares {SHARES:.3f}M (facts) = market cap ${MCAP:,.1f}M")
ev_plain = MCAP - CASH + CONVERTS
ev_full = ev_plain + ROY_LIAB + WARRANTS
print(f"EV (mcap - cash&MS {CASH:,.1f} + converts {CONVERTS:.1f})              = ${ev_plain:,.1f}M")
print(f"EV incl. royalty liability {ROY_LIAB:.1f} + warrant liability {WARRANTS:.1f} = ${ev_full:,.1f}M")
nc = CASH - CONVERTS
print(f"Net cash (cash&MS - converts) = ${nc:,.1f}M = ${nc / SHARES:.2f}/sh "
      f"({nc / SHARES / PRICE:.1%} of price); after warrants ${(nc - WARRANTS) / SHARES:.2f}/sh")
print(f"Market pays for the franchise (price - net cash after warrants): "
      f"${PRICE - (nc - WARRANTS) / SHARES:.2f}/sh = ${MCAP - (nc - WARRANTS):,.0f}M")
print(f"P/B = {MCAP / EQUITY_BV:.2f}x (book equity {EQUITY_BV:,.1f}, facts 30 Jun 26)")

# ============================================================================= 2. Lynch / Buffett metrics
hdr("2. LYNCH / BUFFETT METRICS (mostly not meaningful: zero revenue, losses)")
ok, why = peg_is_valid(fund["trailing_pe"], fund["forward_pe"], facts["revenue_cagr"])
print(f"peg_is_valid(trailing={fund['trailing_pe']}, forward={fund['forward_pe']:.2f}, "
      f"growth={facts['revenue_cagr']}) -> {ok}: {why}  => PEG VOID")
ann = facts["annual"]
v = lambda k, y: ann[k][f"{y}-12-31"]["val"] / M
ni25, da25_f, cx25 = v("net_income", 2025), v("d_and_a", 2025), v("capex", 2025)
oe_facts = ni25 + da25_f - cx25
oe_fund = fund["owner_earnings_usd"] / M
print(f"FY25 owner earnings (NI + D&A - capex): facts D&A {da25_f:.2f} -> {oe_facts:,.1f}; "
      f"fund D&A {fund['d_and_a'] / M:.2f} -> {oe_fund:,.1f}  [D&A tag conflict]")
print(f"FY25 OE already deducts SBC (NI is post-SBC); SBC {v('sbc', 2025):.1f}")
print(f"OE yield on mcap: {oe_fund / MCAP:.2%} (fund) / {oe_facts / MCAP:.2%} (facts)")
ttm = facts["ttm"]
oe_ttm = (ttm["net_income"]["val"] + ttm["d_and_a"]["val"] - ttm["capex"]["val"]) / M
print(f"TTM-Jun26 OE: {oe_ttm:,.1f} (includes non-cash warrant remeasurement; Q2 alone 151.0) "
      f"-> yield {oe_ttm / MCAP:.2%}")
fcf25 = facts["derived"]["2025-12-31"]["fcf"] / M
sfcf25 = facts["derived"]["2025-12-31"]["sbc_adjusted_fcf"] / M
print(f"FY25 FCF {fcf25:,.1f} -> FCF yield {fcf_yield(fcf25, MCAP):.2%}; SBC-adj FCF {sfcf25:,.1f} "
      f"-> {fcf_yield(sfcf25, MCAP):.2%}")
fcf_ttm = (ttm["ocf"]["val"] - ttm["capex"]["val"]) / M
sbc_ttm = ttm["sbc"]["val"] / M
print(f"TTM FCF {fcf_ttm:,.1f} (yield {fcf_ttm / MCAP:.2%}); SBC-adj {fcf_ttm - sbc_ttm:,.1f} "
      f"(yield {(fcf_ttm - sbc_ttm) / MCAP:.2%})")
ic = EQUITY_BV + bs["convertible_notes_carrying"] + ROY_LIAB - CASH
print(f"Invested capital 30 Jun 26 = equity {EQUITY_BV:,.1f} + converts {bs['convertible_notes_carrying']:.1f}"
      f" + royalty liab {ROY_LIAB:.1f} - cash&MS {CASH:,.1f} = {ic:,.1f} -> ROIC not meaningful")
print(f"Goodwill 14.6 / |IC| trivial; ROIC ex-goodwill also n/m")
burn_h1 = -H1_26_CFO * 2
h2_opex_mid = sum(FY26_OPEX_GUIDE) / 2 - H1_26_OPEX
print(f"Runway at H1-26 CFO run-rate ({burn_h1:,.0f}/yr): {CASH / burn_h1:.2f} yrs (zero revenue)")
print(f"H2-26 GAAP opex implied by guidance: {FY26_OPEX_GUIDE[0] - H1_26_OPEX:,.1f} - "
      f"{FY26_OPEX_GUIDE[1] - H1_26_OPEX:,.1f} (mid {h2_opex_mid:,.1f}; annualised {2 * h2_opex_mid:,.0f})")
print(f"Diluted share CAGR 2020-25 (facts): {facts['diluted_share_cagr']:.1%}")

# ============================================================================= 3. WACC
hdr("3. DISCOUNT RATE")
print(f"Ke = rf {US10Y:.2%} + beta {BETA:.1f} x ERP {ERP:.1%} = {KE:.2%}")
print(f"Kd = SOFR floor {SOFR_FLOOR:.2%} + {TERM_LOAN_SPREAD:.2%} = {KD_PRE:.2%} pre-tax; tax shield 0 "
      f"(no taxable income) -> {KD_PRE:.2%}")
print(f"Weights (market): E {MCAP:,.0f} ({MCAP / (MCAP + D_MKT):.1%}), D {D_MKT:,.1f} "
      f"({D_MKT / (MCAP + D_MKT):.1%})")
print(f"WACC = {WACC_RAW:.3%}; 8% USD floor binding? {WACC_RAW < 0.08} -> WACC used {WACC:.2%}")

# ============================================================================= 4. rNPV scenarios
hdr("4. rNPV SCENARIOS (explicit H2-2026..2050, decline modelled, terminal value = 0)")
print("Segment peak WW net sales ($M) -- QUANT ASSUMPTIONS, unsourced:")
print(f"  {'segment':<32}{'launch':>7}{'ytp':>5}{'LOE':>6}{'BEAR':>8}{'BASE':>8}{'BULL':>8}")
for name, launch, ytp, loe, pk in SEGMENTS:
    print(f"  {name:<32}{launch:>7}{ytp:>5}{loe:>6}{pk['BEAR']:>8,}{pk['BASE']:>8,}{pk['BULL']:>8,}")
print(f"  {'TOTAL of segment peaks':<50}"
      + "".join(f"{sum(s[4][k] for s in SEGMENTS):>8,}" for k in ("BEAR", "BASE", "BULL")))
NET_PY_WAC = WAC_30D * 365 / 30 / M                         # $M per patient-year at WAC
print(f"Translation: WAC ${WAC_30D:,.0f}/30d = ${NET_PY_WAC * 1e3:,.0f}K per patient-year gross; "
      f"gross-to-net UNKNOWN")

RES = {sc: run(sc) for sc in ("BEAR", "BASE", "BULL")}
for sc, s in RES.items():
    print(f"\n--- {sc}: modelled peak revenue ${s['peak']:,.0f}M ---")
    print(f"{'Yr':<6}{'Revenue':>9}{'R&D':>8}{'SG&A':>8}{'RPRoy':>7}{'EBIT':>9}{'Tax':>7}"
          f"{'FCF':>9}{'PV':>8}{'CashBal':>9}")
    for (y, r, rd, sga, opx, roy, ebit, tx, fcf, pvf, bal) in s["rows"]:
        if y <= 2036 or y % 2 == 0:
            yl = "2026H2" if y == 2026 else str(y)
            rds = f"{rd:>8,.0f}" if rd is not None else f"{'(opex':>8}"
            sgs = f"{sga:>8,.0f}" if sga is not None else f"{opx:>7,.0f})"
            print(f"{yl:<6}{r:>9,.0f}{rds}{sgs}{roy:>7,.0f}{ebit:>9,.0f}{tx:>7,.0f}{fcf:>9,.0f}"
                  f"{pvf:>8,.0f}{bal:>9,.0f}")
    print(f"PV flows ${s['pv']:,.0f}M + net cash after converts & warrants ${s['net_cash']:,.0f}M "
          f"= equity ${s['eq_raw']:,.0f}M (floor applied: {s['eq'] != s['eq_raw']})")
    print(f"PER SHARE (rolled to 2026-10-13): ${s['ps']:,.2f}  vs price {s['ps'] / PRICE - 1:+.1%}"
          f" | unfloored ${s['ps_raw']:,.2f} | TV share 0%")
    tb, ty = s["trough"]
    print(f"Cumulative cash trough (no new financing): ${tb:,.0f}M in {ty}"
          f"{'  <-- FUNDING GAP' if tb < 0 else ''}")

# ============================================================================= 5. going-concern dcf() variant
hdr("5. GOING-CONCERN VARIANT via valuation.dcf(): 10 yrs 2027-36 + Gordon TV (pipeline renews)")
TG, TROIC = 0.01, 0.15


def gc_kwargs(sc, wacc=WACC):
    s = run(sc, wacc=wacc)
    rows = {r[0]: r for r in s["rows"]}
    base_rev = rows[2026][1]
    growth, margin = [], []
    prev = base_rev
    for y in range(2027, 2037):
        r = rows[y][1]
        growth.append(r / prev - 1)
        margin.append(rows[y][6] / r + DA_CAPEX)               # EBIT margin + D&A -> EBITDA margin
        prev = r
    end26_net_cash = s["net_cash"] + rows[2026][8]             # 30-Jun net cash + H2-26 FCF
    return dict(base_revenue=base_rev, growth=growth, ebitda_margin=margin,
                capex_pct=[DA_CAPEX] * 10, da_pct=[DA_CAPEX] * 10, tax=TAX, wacc=wacc,
                net_debt=-end26_net_cash, shares=SHARES, terminal_growth=TG, terminal_roic=TROIC)


ROLL_GC = lambda w: (1 + w) ** (-79 / 365)                     # dcf() values at 31-Dec-26; back to 13-Oct
GC = {}
for sc in ("BEAR", "BASE", "BULL"):
    kw = gc_kwargs(sc)
    r = dcf(**kw)
    GC[sc] = (r, kw)
    flag = "  <-- TV > 75% of EV" if r.terminal_share > 0.75 else ""
    print(f"{sc}: EV ${r.enterprise_value:,.0f}M (PV explicit {r.pv_explicit:,.0f}, PV TV "
          f"{r.pv_terminal:,.0f}) | TV share {r.terminal_share:.1%}{flag} | per share "
          f"${r.per_share * ROLL_GC(WACC):,.2f} ({r.per_share * ROLL_GC(WACC) / PRICE - 1:+.1%})")
print(f"(g={TG:.0%} <= min(4%, 10y {US10Y:.2%}); terminal ROIC {TROIC:.0%}; tax on losses = credit, "
      f"a rough NOL proxy; D&A=capex=1% rev)")

# ============================================================================= 6. reverse
hdr("6. REVERSE DCF")
lo, hi = 0.05, 10.0
for _ in range(80):
    mid = (lo + hi) / 2
    if run("BASE", peak_scale=mid)["ps"] < PRICE:
        lo = mid
    else:
        hi = mid
rs = run("BASE", peak_scale=mid)
print(f"rNPV (base structure: segments, timing, R&D, cost ratios, WACC {WACC:.2%}, LOE {LOE_DARAX}):")
print(f"  ${PRICE} requires segment peaks x{mid:.3f} -> modelled peak WW net sales ${rs['peak']:,.0f}M")
print(f"  = {rs['peak'] / NET_PY_WAC:,.0f} patient-years on drug per year at full WAC; "
      f"{rs['peak'] / (NET_PY_WAC * 0.8):,.0f} at an assumed 80% gross-to-net")
r27, r34 = rs["revs"][2027], rs["revs"][2034]
print(f"  implied revenue path: 2027 ${r27:,.0f}M -> 2034 ${r34:,.0f}M = CAGR {(r34 / r27) ** (1 / 7) - 1:.1%}")
for sc in ("BEAR", "BULL"):
    lo2, hi2 = 0.05, 40.0
    for _ in range(80):
        m2 = (lo2 + hi2) / 2
        if run(sc, peak_scale=m2)["ps"] < PRICE:
            lo2 = m2
        else:
            hi2 = m2
    print(f"  (same solve on {sc} structure: x{m2:.3f} -> peak ${run(sc, peak_scale=m2)['peak']:,.0f}M)")

kw = gc_kwargs("BASE")
kw_r = {k: v for k, v in kw.items() if k not in ("base_revenue", "growth")}
target = PRICE / ROLL_GC(WACC)
lo_test = dcf(base_revenue=kw["base_revenue"], growth=[0.0] * 10, **kw_r).per_share
hi_test = dcf(base_revenue=kw["base_revenue"], growth=[1.5] * 10, **kw_r).per_share
g_impl = reverse_dcf(price=target, base_revenue=kw["base_revenue"], years=10, lo=0.0, hi=1.5, **kw_r)
print(f"valuation.reverse_dcf() on going-concern base (margin path fixed at base-case years 2027-36,"
      f" g {TG:.0%}, ROIC {TROIC:.0%}):")
print(f"  monotonic check: CAGR 0% -> ${lo_test:,.0f}/sh, CAGR 150% -> ${hi_test:,.0f}/sh")
print(f"  implied constant revenue CAGR from FY26E ${kw['base_revenue']:,.0f}M: {g_impl:.1%} for 10 yrs "
      f"-> 2036 revenue ${kw['base_revenue'] * (1 + g_impl) ** 10:,.0f}M")
print(f"  (base-case 2036 revenue for comparison: ${RES['BASE']['revs'][2036]:,.0f}M)")
print("  CAVEAT: dcf() takes a fixed margin LIST, so scaling revenue also scales the negative 2027-29")
print("  margins (bigger losses); this overstates the required CAGR. Structure-consistent solve below.")


def gc_scaled(scale, wacc=WACC):
    s = run("BASE", wacc=wacc, peak_scale=scale)
    rows = {r[0]: r for r in s["rows"]}
    prev, growth, margin = rows[2026][1], [], []
    for y in range(2027, 2037):
        growth.append(rows[y][1] / prev - 1); margin.append(rows[y][6] / rows[y][1] + DA_CAPEX); prev = rows[y][1]
    r = dcf(base_revenue=rows[2026][1], growth=growth, ebitda_margin=margin, capex_pct=[DA_CAPEX] * 10,
            da_pct=[DA_CAPEX] * 10, tax=TAX, wacc=wacc, net_debt=-(s["net_cash"] + rows[2026][8]),
            shares=SHARES, terminal_growth=TG, terminal_roic=TROIC)
    return r.per_share * ROLL_GC(wacc), s


lo, hi = 0.05, 10.0
for _ in range(80):
    m3 = (lo + hi) / 2
    if gc_scaled(m3)[0] < PRICE:
        lo = m3
    else:
        hi = m3
_, s3 = gc_scaled(m3)
print(f"Going-concern structure, cost structure re-derived at each scale: x{m3:.3f} -> 2036 revenue "
      f"${s3['revs'][2036]:,.0f}M; 2027->2036 CAGR {(s3['revs'][2036] / s3['revs'][2027]) ** (1 / 9) - 1:.1%}")

# ============================================================================= 7. sensitivity
hdr("7. SENSITIVITY")
peaks = [0.5, 0.75, 1.0, 1.5, 2.0, 2.5]
print(f"rNPV BASE per share: WACC x segment-peak scale (base total peaks "
      f"{sum(s[4]['BASE'] for s in SEGMENTS):,}M = 1.0x)")
print("(UNFLOORED values; the valuation.py net-cash floor would lift any value below it to ~$15.6)")
print(f"{'WACC':<8}" + "".join(f"{p:>9.2f}x" for p in peaks))
for w in (WACC - 0.02, WACC - 0.01, WACC, WACC + 0.01, WACC + 0.02):
    print(f"{w:<8.2%}" + "".join(f"{run('BASE', wacc=w, peak_scale=p)['ps_raw']:>10,.0f}" for p in peaks))

print(f"\nGoing-concern BASE per share (valuation.sensitivity): WACC +/-1% x terminal growth +/-1%")
ws = [WACC - 0.01, WACC, WACC + 0.01]
gs = [TG - 0.01, TG, TG + 0.01]
grid = []
for w in ws:   # cash flows re-derived at each WACC (rNPV PV path depends on WACC only via discounting)
    kw_w = gc_kwargs("BASE", wacc=w)
    grid.append(sensitivity({"wacc": [w]}, {"terminal_growth": gs}, **kw_w)[0])
print(f"{'WACC':<8}" + "".join(f"{'g=' + format(g, '.0%'):>10}" for g in gs))
for w, row in zip(ws, grid):
    print(f"{w:<8.2%}" + "".join(f"{x * ROLL_GC(w):>10,.0f}" for x in row))

print("\nrNPV BASE per share: WACC x LOE year of daraxonrasib (patent expiry UNKNOWN)")
shifts = [-4, -2, 0, 2, 4]
print(f"{'WACC':<8}" + "".join(f"{LOE_DARAX + s:>9}" for s in shifts))
for w in (WACC - 0.01, WACC, WACC + 0.01):
    print(f"{w:<8.2%}" + "".join(f"{run('BASE', wacc=w, loe_shift=s)['ps']:>9,.0f}" for s in shifts))

# ============================================================================= 8. load-bearing
hdr("8. LOAD-BEARING INPUTS: effect of +/-10% on BASE rNPV per share")
base_ps = RES["BASE"]["ps"]
tests = [
    ("Segment peak sales (all)",        lambda f: run("BASE", peak_scale=f)),
    ("WACC",                            lambda f: run("BASE", wacc=WACC * f)),
    ("R&D spend path",                  lambda f: run("BASE", rd_scale=f)),
    ("SG&A variable % of revenue",      lambda f: run("BASE", sga_var=SGA_VAR * f)),
    ("SG&A fixed",                      lambda f: run("BASE", sga_fixed=SGA_FIXED * f)),
    ("COGS % of sales",                 lambda f: run("BASE", cogs=COGS * f)),
    ("Years to peak (+/-1 yr)",      lambda f: run("BASE", ytp_scale=f)),
    ("Post-LOE retention (decay)",      lambda f: run("BASE", decay=min(0.99, DECAY * f))),
    ("Tax rate",                        lambda f: run("BASE", tax=TAX * f)),
    ("NOL opening balance",             lambda f: run("BASE", nol0=ACC_DEFICIT * f)),
    ("Royalty Pharma tier rates",       lambda f: run("BASE", roy_scale=f)),
    ("Cash & MS (30 Jun)",              lambda f: run("BASE", cash=CASH * f)),
    ("Share count",                     lambda f: run("BASE", shares=SHARES * f)),
    ("H2-26 opex",                      lambda f: run("BASE", h2_opex=h2_opex_mid * f)),
]
out = []
for name, fn in tests:
    dn, up = fn(0.9)["ps"], fn(1.1)["ps"]
    out.append((max(abs(dn - base_ps), abs(up - base_ps)), name, dn, up))
print(f"Base ${base_ps:,.2f}")
print(f"{'input':<32}{'-10%':>10}{'+10%':>10}{'max |d|':>10}")
for d, name, dn, up in sorted(out, reverse=True):
    print(f"{name:<32}{dn:>10,.2f}{up:>10,.2f}{d:>10,.2f}")
for s in (-2, 2):
    print(f"LOE year {LOE_DARAX + s} (+/-2 yrs, not 10%): ${run('BASE', loe_shift=s)['ps']:,.2f}")
print(f"NOL = 0 (no usable NOL, e.g. s.382 limits): ${run('BASE', nol0=0)['ps']:,.2f}")
print(f"WACC at 8% floor: ${run('BASE', wacc=0.08)['ps']:,.2f}; at 12%: ${run('BASE', wacc=0.12)['ps']:,.2f}")

# ============================================================================= 9. side calcs
hdr("9. SIDE CALCULATIONS")
print("Royalty Pharma drag (tranches 1-2 tiers):")
for sb in (1, 2, 4, 8, 12, 16):
    print(f"  ${sb}B sales -> ${rp_royalty(sb * 1000):,.0f}M ({rp_royalty(sb * 1000) / (sb * 1000):.2%} blended)")
print("Convertible notes (conversion price UNKNOWN): extra claim above $500M par if in the money "
      "= 500 x (P/Conv - 1); per-share hit, illustrative only:")
for conv in (100.0, 150.0, 193.95):
    extra = max(0.0, CONVERTS * (PRICE / conv - 1))
    print(f"  hypothetical conv. price ${conv:.0f}: extra claim ${extra:,.0f}M = ${extra / SHARES:.2f}/sh")
print(f"Option/RSU overhang UNKNOWN: +5% diluted shares -> base ${run('BASE', shares=SHARES * 1.05)['ps']:,.2f}"
      f" (from ${base_ps:,.2f})")
lease_pv = sum(32.0 * 1.03 ** (y - 2028) / (1 + WACC) ** (y - 2026) for y in range(2028, 2043))
print(f"New HQ lease ~$32M/yr +3%/yr 2028-2042 (dossier s5): PV ${lease_pv:,.0f}M = ${lease_pv / SHARES:.2f}/sh "
      f"(not separately deducted; assumed inside opex)")
print(f"Term loan tranche 1 ($250M, draw status UNKNOWN): cash +250 / debt +250 -> NAV-neutral ex 2% fee "
      f"(${250 * 0.02:.0f}M = ${5 / SHARES:.3f}/sh); coupon >= {KD_PRE:.2%} vs WACC {WACC:.2%}")
print(f"Royalty-sale liability ${ROY_LIAB:.1f}M if ALSO deducted (double count): "
      f"-${ROY_LIAB / SHARES:.2f}/sh")
for sc, s in RES.items():
    tot = sum(r[9] for r in s["rows"] if r[0] >= 2042)
    print(f"{sc}: PV of flows 2042+ (post-LOE tail) ${tot:,.0f}M = {tot / s['pv'] if s['pv'] else 0:.1%} of PV flows")
for sc, s in RES.items():
    r36 = [r for r in s["rows"] if r[0] == 2036][0]
    print(f"{sc}: 2036 EBIT margin {r36[6] / r36[1]:.1%} on revenue ${r36[1]:,.0f}M")
_q4 = dict(Q4_MULT)
for k in (1.0, 3.0):
    Q4_MULT["BASE"] = k
    print(f"2026 anchor: BASE with Q4-26 = {k:.0f}x Q3 consensus -> ${run('BASE')['ps']:,.2f} (vs ${base_ps:,.2f})")
Q4_MULT.update(_q4)
