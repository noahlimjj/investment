"""RVMD Skeptic re-run (03) -- as of 2026-10-13.

Loads the Quant's 02_model.py unchanged (stdout suppressed), then re-implements its run() with
extra switches so every adjustment is isolated and auditable:

  dil  : treasury-stock dilution from VESTED options only (10-Q 30 Jun 26: 9,741,603 vested,
         WAEP $25.62). Unvested options / RSUs are NOT added: their future expense already sits in
         the GAAP opex path the Quant charges (adding both would double count).
  ira  : IRA Medicare negotiation haircut (omitted in 02). Current law (EPIC Act not enacted per
         Apr-2026 source): small molecule eligible for selection 7 yrs post approval; daraxonrasib
         approved 2026-08-26 -> selected Feb-2034 -> negotiated price from 2036. Later molecules
         (zoldonrasib/elironrasib, launch 2030 in 02) -> from 2040. Haircut = US share 65% x
         Medicare share of US 55% x net price cut 25% = 8.9% of segment revenue. ALL THREE
         PARAMETERS ARE SKEPTIC ASSUMPTIONS (unsourced), labelled as such.
  rf   : 10y UST 5.22% (FRED DGS10 2026-10-08, orchestrator-supplied) vs 5.20% (^TNX).
  sbc_cash=False : flattering view -- SBC (13.0% of FY26 opex guide: 280/2,150) removed from opex,
         share count not grown. Shown only to size SBC; never used for fair value.
  peaks : segment-peak override (Skeptic ALT, epidemiology bracket; judgement, NOT an error fix).

Check: with all switches off it must reproduce 02's $15.60 / $63.38 / $130.49.
"""
from __future__ import annotations

import contextlib
import io
import pathlib
import runpy

RUN = pathlib.Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    Q = runpy.run_path(str(RUN / "02_model.py"), run_name="quant02")
G = Q["run"].__globals__            # live namespace of the Quant model

SEGMENTS, RD, Q4_MULT = G["SEGMENTS"], G["RD"], G["Q4_MULT"]
seg_rev, rp_royalty = G["seg_rev"], G["rp_royalty"]
CASH, CONVERTS, WARRANTS, SHARES0 = G["CASH"], G["CONVERTS"], G["WARRANTS"], G["SHARES"]
H1_26_OPEX, FY26 = G["H1_26_OPEX"], G["FY26_OPEX_GUIDE"]
PRICE, MCAP, ROY_LIAB = G["PRICE"], G["MCAP"], G["ROY_LIAB"]

# ---- verified from 10-Q accn 0001193125-26-335104 (fetched from EDGAR 2026-10-13) ----
VESTED_OPT, VESTED_K = 9.741603, 25.62     # M shares, $ WAEP (vested & exercisable 30 Jun 26)
ALL_OPT, ALL_K, RSU = 18.361684, 40.42, 5.078440
CONV_PRICE = 198.80                         # 5.0302 sh per $1,000
# ---- Skeptic assumptions (unsourced, labelled) ----
IRA_HAIRCUT = 0.65 * 0.55 * 0.25
IRA_START = {G["LOE_DARAX"]: 2036, G["LOE_NEXT"]: 2040}
SBC_SHARE_OPEX = 280.0 / 2150.0


def wacc_for(rf):
    ke = rf + 0.05
    d = CONVERTS + ROY_LIAB
    return max((MCAP * ke + d * 0.0925) / (MCAP + d), 0.08)


def run2(sc, *, rf=0.052, ira=False, dil=False, sbc_cash=True, peaks=None, floor=True,
         rd_cut_year=None):
    wacc = wacc_for(rf)
    h2_opex = sum(FY26) / 2 - H1_26_OPEX
    opx_mult = 1.0 if sbc_cash else (1 - SBC_SHARE_OPEX)
    segs = [(n, l, y, loe, (peaks or {}).get(n, pk)) for (n, l, y, loe, pk) in SEGMENTS]
    years = list(range(2026, 2051))
    revs, peak_total = {}, 0.0
    for yr in years:
        r = 0.0
        for name, launch, ytp, loe, pk in segs:
            p = pk[sc]
            if p == 0:
                continue
            first = (G["Q3_REV_CONSENSUS"] * (1 + Q4_MULT[sc])) if launch == 2026 else None
            v = seg_rev(yr, p, launch, ytp, loe, first, G["DECAY"])
            if ira and IRA_START[loe] <= yr < loe:
                v *= (1 - IRA_HAIRCUT)
            r += v
        revs[yr] = r
        peak_total = max(peak_total, r)
    pv, nol, bal, trough = 0.0, G["ACC_DEFICIT"], CASH, (CASH, 2026)
    for yr in years:
        r = revs[yr]
        if yr == 2026:
            rd_sga = h2_opex * opx_mult
        else:
            r0, plat, plat_y, cut, cut_y = RD[sc]
            if rd_cut_year is not None and sc == "BEAR":
                cut_y = rd_cut_year
            if cut is not None and yr >= cut_y:
                rd = max(400.0, cut * r)
            elif yr >= plat_y:
                rd = plat
            else:
                rd = r0 + (plat - r0) * (yr - 2027) / max(1, plat_y - 2027)
            wind = min(1.0, r / peak_total) if (peak_total and yr >= G["LOE_DARAX"]) else 1.0
            rd *= wind
            sga = G["SGA_FIXED"] * wind + G["SGA_VAR"] * r
            rd_sga = (rd + sga) * opx_mult
        roy = rp_royalty(r)
        ebit = r - r * G["COGS"] - roy - rd_sga
        if ebit < 0:
            nol += -ebit
            tx = 0.0
        else:
            used = min(ebit, nol)
            nol -= used
            tx = (ebit - used) * G["TAX"]
        fcf = ebit - tx
        t = 0.25 if yr == 2026 else (yr - 2026)
        pv += fcf / (1 + wacc) ** t
        bal += fcf
        trough = min(trough, (bal, yr))
    net_cash = CASH - CONVERTS - WARRANTS
    eq_raw = pv + net_cash
    eq = max(eq_raw, net_cash) if floor else eq_raw
    roll = (1 + wacc) ** (G["TODAY_ROLL_DAYS"] / 365)
    sh = SHARES0
    if dil:                                   # fixed-point treasury-stock method at intrinsic value
        for _ in range(50):
            v = eq * roll / sh
            sh = SHARES0 + VESTED_OPT * max(0.0, 1 - VESTED_K / v) if v > 0 else SHARES0
    return dict(ps=eq * roll / sh, ps_raw=eq_raw * roll / sh, shares=sh, wacc=wacc, pv=pv,
                peak=peak_total, trough=trough, revs=revs)


def line(t):
    print("\n" + "=" * 96 + f"\n{t}\n" + "=" * 96)


SC = ("BEAR", "BASE", "BULL")

line("0. REPRODUCTION CHECK (all switches off must equal 02_model.py)")
q = {s: G["RES"][s]["ps"] for s in SC}
r0 = {s: run2(s)["ps"] for s in SC}
for s in SC:
    print(f"{s:5}  02: ${q[s]:7.2f}   03 replica: ${r0[s]:7.2f}   diff {r0[s] - q[s]:+.4f}")
assert all(abs(r0[s] - q[s]) < 0.01 for s in SC), "replica does not reproduce 02"

line("1. ISOLATED ADJUSTMENTS (per share, vs 02)")
steps = [("rf 5.22% (FRED)", dict(rf=0.0522)),
         ("vested-option TSM dilution", dict(dil=True)),
         ("IRA Medicare negotiation haircut", dict(ira=True)),
         ("ALL THREE (= Skeptic corrected)", dict(rf=0.0522, dil=True, ira=True))]
for name, kw in steps:
    vals = {s: run2(s, **kw) for s in SC}
    print(f"{name:34}" + "".join(f"  {s} ${vals[s]['ps']:7.2f} ({vals[s]['ps'] / q[s] - 1:+.1%})" for s in SC))
COR = {s: run2(s, rf=0.0522, dil=True, ira=True) for s in SC}
COR_RAW = {s: run2(s, rf=0.0522, dil=True, ira=True, floor=False)["ps_raw"] for s in SC}
print(f"WACC used: {COR['BASE']['wacc']:.3%}; diluted shares at base value: {COR['BASE']['shares']:.3f}M "
      f"(+{COR['BASE']['shares'] / SHARES0 - 1:.2%})")
print(f"Bear unfloored (corrected): ${COR_RAW['BEAR']:.2f}")
print(f"Bear with R&D cut one year earlier (2028, failures known 2027): "
      f"${run2('BEAR', rf=0.0522, dil=True, ira=True, rd_cut_year=2028, floor=False)['ps_raw']:.2f} unfloored")

line("2. SBC: cash-cost view (02 and here) vs flattering add-back view")
for s in SC:
    a = run2(s, rf=0.0522, dil=True, ira=True)["ps"]
    b = run2(s, rf=0.0522, dil=True, ira=True, sbc_cash=False)["ps"]
    print(f"{s:5}  SBC as cash cost ${a:7.2f}   SBC added back (no dilution) ${b:7.2f}   gap ${b - a:6.2f} ({b / a - 1:+.0%})")

line("3. SEGMENT-LEVEL INCREMENTAL VALUE (corrected, BASE costs; remove one segment at a time)")
full = COR["BASE"]["ps"]
for name, *_ , pk in SEGMENTS:
    if pk["BASE"] == 0:
        continue
    alt = {name: {**pk, "BASE": 0}}
    v = run2("BASE", rf=0.0522, dil=True, ira=True, peaks=alt, floor=False)["ps_raw"]
    print(f"  {name:30} contributes ${full - v:6.2f}/sh (base without it ${v:6.2f})")
pdac_only = {n: {**pk, "BASE": 0} for (n, _, _, _, pk) in SEGMENTS if "NSCLC" in n}
v_mid = run2("BASE", rf=0.0522, dil=True, ira=True, peaks=pdac_only, floor=False)["ps_raw"]
print(f"  MID scenario (2L+ and 1L PDAC succeed, all NSCLC fails, base R&D kept): ${v_mid:6.2f}")
RD["MIDX"] = (1800.0, 1800.0, 2027, None, None)
Q4_MULT["MIDX"] = 2.0
mid_peaks = {n: {**pk, "MIDX": (pk["BASE"] if "PDAC" in n and "Adjuvant" not in n else 0)}
             for (n, _, _, _, pk) in SEGMENTS}
v_mid2 = run2("MIDX", rf=0.0522, dil=True, ira=True, peaks=mid_peaks, floor=False)["ps_raw"]
print(f"  MID scenario with R&D held at 1,800 (no NSCLC expansion spend): ${v_mid2:6.2f}")

line("4. SKEPTIC ALT: PDAC peaks re-anchored on an epidemiology bracket (JUDGEMENT, not an error fix)")
DEATHS = 52_740           # ACS 2026 US pancreatic cancer deaths (cancer.org key statistics, via search)
PY = G["WAC_30D"] * 365 / 30 / 1e6   # $M per patient-year at WAC (dossier WAC $39,800/30d)
GTN = 0.80                # assumption
chain = {  # (treated share of annual US deaths, mean DoT yrs, ex-US uplift)  -- ALL ASSUMPTIONS
    "2L+ only": {"BEAR": (0.20, 0.40, 0.20), "BASE": (0.30, 0.50, 0.30), "BULL": (0.40, 0.60, 0.40)},
    "all lines (1L approved)": {"BEAR": (0.0, 0.0, 0.0), "BASE": (0.45, 0.70, 0.30), "BULL": (0.55, 0.85, 0.40)},
}
ww = {}
for k, d in chain.items():
    ww[k] = {s: DEATHS * a * b * PY * GTN * (1 + c) for s, (a, b, c) in d.items()}
    print(f"  {k:24}" + "".join(f"  {s} ${ww[k][s]:8,.0f}M" for s in SC))
alt_peaks = {
    "2L+ mPDAC (approved)": {s: round(ww["2L+ only"][s], -2) for s in SC},
    "1L mPDAC (RASolute 303/305)": {"BEAR": 0, **{s: round(ww["all lines (1L approved)"][s] - ww["2L+ only"][s], -2)
                                               for s in ("BASE", "BULL")}},
}
for n, p in alt_peaks.items():
    print(f"  ALT peak {n:30} {p}")
ALT = {s: run2(s, rf=0.0522, dil=True, ira=True, peaks=alt_peaks) for s in SC}
ALT_RAW_BEAR = run2("BEAR", rf=0.0522, dil=True, ira=True, peaks=alt_peaks, floor=False)["ps_raw"]
for s in SC:
    print(f"  ALT {s:5} peak ${ALT[s]['peak']:8,.0f}M -> ${ALT[s]['ps']:7.2f}/sh (corrected 02 structure: ${COR[s]['ps']:7.2f})")
print(f"  ALT bear unfloored ${ALT_RAW_BEAR:.2f}")

line("5. PROBABILITIES, EXPECTED VALUE, MoS, ASYMMETRY")
P = {"BEAR": 0.15, "BASE": 0.65, "BULL": 0.20}
assert abs(sum(P.values()) - 1) < 1e-9


def ev_block(label, vals, bear_for_asym):
    ev = sum(P[s] * vals[s] for s in SC)
    mos = 1 - PRICE / ev
    asym = "no downside to bear" if bear_for_asym >= PRICE else f"{(ev - PRICE) / (PRICE - bear_for_asym):+.2f}"
    print(f"{label:46} EV ${ev:7.2f}  MoS {mos:+.0%}  asymmetry {asym}")
    return ev


ev_q = ev_block("Quant 02 values (unchanged)", q, q["BEAR"])
cor_vals = {s: COR[s]["ps"] for s in SC}
ev_c = ev_block("Skeptic corrected (rf, dilution, IRA)", cor_vals, COR_RAW["BEAR"])
cor_vals_unf = {**cor_vals, "BEAR": COR_RAW["BEAR"]}
ev_cu = ev_block("Skeptic corrected, bear unfloored", cor_vals_unf, COR_RAW["BEAR"])
alt_vals = {s: ALT[s]["ps"] for s in SC}
ev_a = ev_block("Skeptic ALT (PDAC epidemiology re-anchor)", alt_vals, ALT_RAW_BEAR)
print(f"Probabilities used: {P}")
# what bull probability would justify the price on ALT values (bear fixed 15%)?
for lab, vals in (("corrected", cor_vals), ("ALT", alt_vals)):
    need = (PRICE - 0.15 * vals["BEAR"] - 0.85 * vals["BASE"]) / (vals["BULL"] - vals["BASE"])
    print(f"Bull weight needed for EV = price ({lab}, bear 15%): {need:.0%}"
          + ("  (>85%: impossible with bear at 15%)" if need > 0.85 else ""))

line("6. ENTRY / EXIT anchors")
print(f"Corrected EV ${ev_c:.2f}; ALT EV ${ev_a:.2f}; corrected bull ${cor_vals['BULL']:.2f}; ALT bull ${alt_vals['BULL']:.2f}")
print(f"Corrected base ${cor_vals['BASE']:.2f}; ALT base ${alt_vals['BASE']:.2f}")

line("7. FINANCING COST: Royalty Pharma tranches 1-2 ($250M Jun-25 + $250M May-26) implied IRR to RP")


def irr(flows):
    lo, hi = -0.99, 2.0
    for _ in range(200):
        m = (lo + hi) / 2
        npv = sum(cf / (1 + m) ** t for t, cf in flows)
        lo, hi = (m, hi) if npv > 0 else (lo, m)
    return m


for s in SC:
    revs = run2(s, rf=0.0522, ira=True)["revs"]
    flows = [(-1.0, -250.0), (-0.1, -250.0)] + [((0.5 if y == 2026 else y - 2026 + 0.5) - 0.5, rp_royalty(revs[y])) for y in revs]
    print(f"  {s:5}: royalty paid 2026-50 ${sum(rp_royalty(revs[y]) for y in revs):,.0f}M on $500M -> IRR {irr(flows):.1%}")
print(f"  Converts: 0.50% coupon, conversion ${CONV_PRICE} = {CONV_PRICE / 142 - 1:.0%} premium to the $142 April-26 offer price")
print(f"  At price ${PRICE}: converts {'in' if PRICE > CONV_PRICE else 'out of'} the money; "
      f"if converted, {500 / CONV_PRICE:.3f}M shares")
