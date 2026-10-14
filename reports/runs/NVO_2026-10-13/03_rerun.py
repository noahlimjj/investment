"""03_rerun.py - Skeptic re-run of the Quant's 02_model.py (NVO, as of 2026-10-13).

Loads 02_model.py UNCHANGED (its stdout suppressed) and reuses its build()/dcf()/reverse_dcf()
mechanics, so every difference from the Quant is an explicit, named override below.
DKK millions unless stated. Run: python3 reports/runs/NVO_2026-10-13/03_rerun.py

AUDIT CORRECTIONS (number-audit failures: inputs, not judgement)
  A1 Price of record USD 38.015 (orchestrator note: 2026-10-13 close per fundamentals.json) instead of
     38.415 (00_inputs intraday 13:52Z). yfinance daily history pulled 2026-10-14 shows the final
     2026-10-13 close as 38.06 (fundamentals.json 38.015 is stamped 18:32Z, before the 20:00Z close);
     the 0.1% gap is shown, not used.
  A2 Claims + Dec-25 marketable securities DKK 498m (6-K 0000353278-26-000023 balance-sheet comparative;
     Quant had UNKNOWN). Trivial.
  A3 Discount rate. (i) DKK 10y: 00_inputs uses the OECD Aug-26 monthly average 3.01% (FRED still has no
     later print, checked 2026-10-14). Latest available print: 3.17% on 1 Sep 2026 (Trading Economics,
     secondary) -> DKK floor 7.17%. (ii) Currency: the model holds FX flat on DKK cash flows of which
     51.3% of sales are US (H1-26 adjusted US Operations 76,254 / 148,551, 6-K). Discounting USD-earned
     flows held at spot FX with a DKK rate understates their required return by the USD-DKK rate gap.
     Rate = 51.3% x USD floor 8.00% + 48.7% x DKK floor 7.17% = 7.60%. Pure-DKK (7.17%) and pure-USD
     (8.00%) values are shown too.
  (FY25 340B exclusion is 2,649 per the Q2-26 6-K reconciliation, not 2,600: 0.02% of base revenue,
   immaterial, not changed.)

SKEPTIC JUDGEMENT (disagreements with the Quant; each shown separately, then combined)
  J1 Semaglutide LOE depth (BASE): FY32-33 growth -9%/-9% instead of -1%/-1%. Evidence: 20-F patent
     table (US 2032; EU, Japan 2031; China 2026); semaglutide = 73.9% of FY25 sales (Ozempic 127,089 +
     Wegovy 79,106 + Rybelsus 22,093); US + EUCAN semaglutide = 62.6% of FY25 sales; liraglutide
     (Victoza) sales -44.9% in 2025 (5,482 -> 3,020) after US compound-patent expiry in 2023.
     -9%/-9% = pipeline/lifecycle offsets about half of the loss (midpoint of the Quant's own -1%/-1%
     full-offset base and its -18%/-18% no-offset stress).
  J2 WAC-cut provision unwind in FY27 (company: the 1 Jan 2027 list-price cut "is expected to impact
     Novo Nordisk's cash flow in 2027"): 25% (BASE) / 50% (BEAR) / 10% (BULL) of the Jun-26 current
     sales-deduction provision (140,201) paid out net in FY27, pre-tax (deductions were tax-deducted
     on accrual). Same magnitudes as the Quant's own stress test, moved into the scenarios. It
     REPLACES the Quant's FY27 cash gap (BASE 2.76%, BEAR 6.17%, BULL 0%), which was partly its proxy
     for the same WAC-cut hit, so there is no double count.
  J3 BD / bolt-on M&A allowance 3.0% of revenue FY27+ (Quant 1.45% = median FY21-24 intangibles only,
     which ignores business acquisitions). FY20-25 intangibles + acquisitions ex-Catalent = 7.25% of
     revenue; ex-Catalent and ex-Akero = 4.90%. 3.0% is a deliberately conservative middle.
"""
import contextlib
import io
import pathlib
import runpy

RUN = pathlib.Path(__file__).resolve().parent
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    M = runpy.run_path(str(RUN / "02_model.py"), run_name="quant_model")

build, dcf, reverse_dcf = M["build"], M["dcf"], M["reverse_dcf"]
SCEN, CLAIMS_Q, SH, FX = M["SCEN"], M["CLAIMS"], M["SH"], M["FX"]
ADJ_REV25, WACC_Q, P_DKK_Q = M["ADJ_REV25"], M["WACC"], M["P_DKK"]
N = 10


def hdr(t):
    print("\n" + "=" * 96 + f"\n{t}\n" + "=" * 96)


def ps(scen, **over):
    return dcf(**build(**{**scen, **over})).per_share


def res(scen, **over):
    return dcf(**build(**{**scen, **over}))


# ------------------------------------------------------------------ 0. reproduce the Quant
hdr("0. REPRODUCE QUANT (02_model.py, unchanged)")
Q = {k: ps(SCEN[k]) for k in ("BEAR", "BASE", "BULL")}
for k, v in Q.items():
    print(f"{k:<5} DKK {v:7.1f}  USD {v*FX:6.2f}   (02_quant.md: 156.6 / 347.3 / 554.1)")

# ------------------------------------------------------------------ 1. deterministic number audit
hdr("1. NUMBER AUDIT RECOMPUTATIONS (python, from facts.json / primary filings)")
A, RA = M["A"], M["RA"]
chk = []


def c(name, quant, verified, tol=0.005):
    ok = abs(quant - verified) <= tol * max(1, abs(verified))
    chk.append((name, quant, verified, "PASS" if ok else "FAIL"))


c("Shares outstanding (m) 4,465,000,000 - 51,889,876", SH, (4465000000 - 51889876) / 1e6)
c("Net debt Dec-25 = borrowings - cash", M["ND_DEC25"], 130958 - 26464)
c("Claims = ND Dec-25 + 35,312 + 3.75 x sh + 10,558.9", CLAIMS_Q,
  104494 + 35312 + 3.75 * SH + 10558.876422)
c("Net debt Jun-26 = 121,794 + 18,333 - 44,482 - 500", M["ND_JUN26"], 121794 + 18333 - 44482 - 500)
c("Base revenue FY25 adj (Quant 340B 2,600 vs 6-K 2,649)", ADJ_REV25, 309064 - 2649, tol=0.001)
c("Base EBIT FY25 adj = 127,658 - 340B + impairments 7,316", M["ADJ_EBIT25"], 127658 - 2649 + 7316,
  tol=0.001)
c("FY26 BASE EBIT margin = 132,374 x 0.95 / 294,205", M["Y1"]["BASE"]["m"],
  (132374 * 0.95) / (306464 * 0.96), tol=0.001)
c("D&A FY26 = (13,840 - 6,328) x 2", M["DA26_ABS"], (13840 - 6328) * 2)
c("BD allowance = median FY21-24 intangibles/revenue", M["BD_PCT"],
  sorted([1050 / 140800, 2607 / 176954, 13090 / 232261, 4145 / 290403])[1:3][0] / 2 +
  sorted([1050 / 140800, 2607 / 176954, 13090 / 232261, 4145 / 290403])[1:3][1] / 2)
c("ROIC FY25 = 127,658 x (1-21.53%) / (194,047 + 130,958 - 26,464)", M["roic"][5],
  127658 * (1 - 0.2153) / (194047 + 130958 - 26464), tol=0.01)
c("FCF FY25 OCF - PP&E (identity)", M["fcf_co"][5], 119102 - 60140)
c("Market EV (DKK) = mcap + ND Jun-26", M["EV_MKT"], P_DKK_Q * SH + 95145)
c("Semaglutide share of sales (Quant Q2 floor 68.9% vs FY25 20-F 73.9%)", 54077 / 78488,
  (127089 + 79106 + 22093) / 309064, tol=0.02)
for n_, q_, v_, s_ in chk:
    print(f"{s_:<5} {n_:<64} quant {q_:>12,.4f}  verified {v_:>12,.4f}")
print("TV share of EV (BEAR/BASE/BULL): " + " / ".join(
    f"{res(SCEN[k]).terminal_share:.0%}" for k in ("BEAR", "BASE", "BULL")) + "  (flag at > 75%)")

# ------------------------------------------------------------------ 2. audit corrections
hdr("2. AUDIT CORRECTIONS A1-A3 (inputs)")
P_USD = 38.015
P_USD_FINAL = 38.06
P_DKK = P_USD / FX
CLAIMS = CLAIMS_Q - 498                       # A2: Dec-25 marketable securities (cash-like)
RF_DKK_NOW = 0.0317                           # A3(i)
FLOOR_DKK = RF_DKK_NOW + 0.04
US_W = 76254 / 148551                         # A3(ii)
WACC_BL = round(US_W * 0.08 + (1 - US_W) * FLOOR_DKK, 4)
print(f"A1 price USD {P_USD} = DKK {P_DKK:.2f} (final close {P_USD_FINAL} = DKK {P_USD_FINAL/FX:.2f}); "
      f"Quant used USD 38.415 = DKK {P_DKK_Q:.2f}")
print(f"A2 claims {CLAIMS_Q:,.0f} - 498 = {CLAIMS:,.0f}  ({-(-498)/SH:+.2f} DKK/share)")
print(f"A3 DKK floor {FLOOR_DKK:.2%}; US weight {US_W:.1%}; blended rate {WACC_BL:.2%} "
      f"(Quant {WACC_Q:.2%})")
STEP = {}
for k in ("BEAR", "BASE", "BULL"):
    s = SCEN[k]
    STEP[k] = {
        "quant": Q[k],
        "A2 claims": ps(s, claims=CLAIMS),
        "A3i DKK rf 3.17% (7.17%)": ps(s, claims=CLAIMS, wacc=FLOOR_DKK),
        "blend on stale rf (7.52%)": ps(s, claims=CLAIMS, wacc=round(US_W * 0.08 + (1 - US_W) * 0.0701, 4)),
        "A3 blended 7.60%": ps(s, claims=CLAIMS, wacc=WACC_BL),
        "pure USD 8.00%": ps(s, claims=CLAIMS, wacc=0.08),
    }
print(f"{'step':<28}" + "".join(f"{k:>18}" for k in ("BEAR", "BASE", "BULL")))
for st_ in STEP["BASE"]:
    print(f"{st_:<28}" + "".join(f"{STEP[k][st_]:>9.1f} ({STEP[k][st_]*FX:5.2f})" for k in
                                 ("BEAR", "BASE", "BULL")))
d_audit = STEP["BASE"]["A3 blended 7.60%"] / Q["BASE"] - 1
print(f"Audit-corrected BASE vs Quant BASE: {d_audit:+.1%}  (> 5% threshold -> rerun required)")

# ------------------------------------------------------------------ 3. judgement overrides
hdr("3. SKEPTIC JUDGEMENT J1-J3 on top of A1-A3 (each incremental, then combined)")
SALES_DED = 140201
UNWIND = {"BEAR": 0.50, "BASE": 0.25, "BULL": 0.10}
BD_SK = 0.030


def j_over(k, j1=True, j2=True, j3=True):
    s = SCEN[k]
    g = list(s["g"])
    if j1 and k == "BASE":
        g[6], g[7] = -0.09, -0.09
    gap = list(s["gap"])
    if j2:   # REPLACES the Quant's FY27 cash gap (its proxy for the WAC-cut hit), no double count
        rev27 = ADJ_REV25 * (1 + g[0]) * (1 + g[1])
        gap[1] = UNWIND[k] * SALES_DED / rev27
    bd = [s["bd"][0]] + [BD_SK] * 9 if j3 else list(s["bd"])
    return dict(g=g, gap=gap, bd=bd, claims=CLAIMS, wacc=WACC_BL)


SK = {}
for k in ("BEAR", "BASE", "BULL"):
    a3 = STEP[k]["A3 blended 7.60%"]
    v1 = ps(SCEN[k], **j_over(k, True, False, False))
    v2 = ps(SCEN[k], **j_over(k, True, True, False))
    v3 = ps(SCEN[k], **j_over(k, True, True, True))
    SK[k] = v3
    print(f"{k:<5} A1-A3 {a3:6.1f} | +J1 LOE {v1:6.1f} ({v1-a3:+5.1f}) | +J2 unwind {v2:6.1f} ({v2-v1:+5.1f})"
          f" | +J3 BD 3% {v3:6.1f} ({v3-v2:+5.1f}) => DKK {v3:6.1f} = USD {v3*FX:5.2f}")
for k in ("BEAR", "BASE", "BULL"):
    r = res(SCEN[k], **j_over(k))
    print(f"  {k} TV share {r.terminal_share:.0%}; FY27 FCF {r.rows[1][6]:,.0f}; FY35 revenue {r.rows[-1][1]:,.0f}")
print("Single-change effects on the Quant BASE (Quant WACC 7.01%):")
for lab, over in (("J1 only (LOE -9/-9)", dict(g=SCEN['BASE']['g'][:6] + [-0.09, -0.09] + SCEN['BASE']['g'][8:])),
                  ("J2 only (25% unwind)", dict(gap=[SCEN['BASE']['gap'][0],
                                                     0.25 * SALES_DED / (ADJ_REV25 * 0.96 * 0.97)] + [0.0] * 8)),
                  ("J3 only (BD 3%)", dict(bd=[SCEN['BASE']['bd'][0]] + [BD_SK] * 9)),
                  ("A3 only (blended 7.60%)", dict(wacc=WACC_BL))):
    v = ps(SCEN["BASE"], **over)
    print(f"  {lab:<26} DKK {v:6.1f} ({v/Q['BASE']-1:+.1%})")

# LOE depth sweep at the corrected rate (the thesis-flipping variable)
print("LOE depth sweep, BASE with A1-A3 + J2 + J3 (FY32-33 growth each year):")
for d in (0.025, -0.01, -0.05, -0.09, -0.13, -0.18):
    o = j_over("BASE")
    o["g"] = o["g"][:6] + [d, d] + o["g"][8:]
    v = ps(SCEN["BASE"], **o)
    print(f"  FY32-33 {d:+.1%}/{d:+.1%}: DKK {v:6.1f}  USD {v*FX:5.2f}  vs price {v/P_DKK-1:+.0%}")

# ------------------------------------------------------------------ 4. SBC
hdr("4. SBC: model already treats SBC as a cash cost (IFRS 2 expense inside EBIT, never added back)")
SBC_PCT = 1435 / 306464
v_sbc_back = ps(SCEN["BASE"], **{**j_over("BASE"),
                                 "ebit_m": [m + SBC_PCT for m in SCEN["BASE"]["ebit_m"]]})
print(f"SBC FY25 1,435 = {SBC_PCT:.2%} of revenue, {1435/119102:.2%} of OCF")
print(f"Skeptic BASE, SBC as cash (as modelled): DKK {SK['BASE']:.1f} (USD {SK['BASE']*FX:.2f}); "
      f"SBC added back as non-cash: DKK {v_sbc_back:.1f} (USD {v_sbc_back*FX:.2f}), "
      f"{v_sbc_back/SK['BASE']-1:+.1%}")

# ------------------------------------------------------------------ 5. reverse DCF at corrected rate
hdr("5. REVERSE DCF at the corrected price and rate")
strip = lambda kw: {k: v for k, v in kw.items() if k not in ("base_revenue", "growth")}
for lab, w in (("Quant 7.01%", WACC_Q), ("DKK 7.17%", FLOOR_DKK), ("blended 7.60%", WACC_BL),
               ("USD 8.00%", 0.08)):
    kw = build(**{**SCEN["BASE"], "claims": CLAIMS, "wacc": w})
    gi = reverse_dcf(price=P_DKK, base_revenue=ADJ_REV25, years=N, **strip(kw))
    print(f"  BASE margins/capex, {lab:<14}: implied constant 10-yr revenue CAGR {gi:+.2%}")
kw = build(**{**SCEN["BASE"], **j_over("BASE")})
gi = reverse_dcf(price=P_DKK, base_revenue=ADJ_REV25, years=N, **strip(kw))
print(f"  Skeptic BASE (A1-A3 + J2 + J3 costs), blended 7.60%: implied CAGR {gi:+.2%}")
lo, hi = 0.03, 0.20
for _ in range(60):
    w = (lo + hi) / 2
    v = ps(SCEN["BASE"], **{**j_over("BASE"), "wacc": w})
    lo, hi = (w, hi) if v > P_DKK else (lo, w)
print(f"  IRR implied by price on the Skeptic BASE cash flows: {w:.2%}")

# ------------------------------------------------------------------ 6. probabilities and EV
hdr("6. PROBABILITIES, EXPECTED VALUE, MARGIN OF SAFETY")
PROB = {"BEAR": 0.30, "BASE": 0.50, "BULL": 0.20}
assert abs(sum(PROB.values()) - 1) < 1e-9


def ev_block(lab, vals):
    ev = sum(PROB[k] * vals[k] for k in PROB)
    ev_usd = ev * FX
    mos = 1 - P_USD / ev_usd
    bear_usd = vals["BEAR"] * FX
    asym = "no downside to bear" if bear_usd >= P_USD else f"{(ev_usd-P_USD)/(P_USD-bear_usd):.2f}"
    print(f"{lab:<34} BEAR {vals['BEAR']*FX:6.2f} BASE {vals['BASE']*FX:6.2f} BULL {vals['BULL']*FX:6.2f} | "
          f"EV DKK {ev:6.1f} = USD {ev_usd:5.2f} | MoS {mos:+.1%} | asymmetry {asym} | "
          f"entry (30% MoS) {ev_usd*0.70:5.2f} | exit (x1.3) {ev_usd*1.3:5.2f}")
    return ev_usd


print(f"Probabilities: {PROB}; price USD {P_USD}")
ev_q = ev_block("Quant values (7.01%)", Q)
ev_a = ev_block("Audit-corrected (A1-A3)", {k: STEP[k]["A3 blended 7.60%"] for k in PROB})
ev_s = ev_block("Skeptic (A1-A3 + J1-J3)", SK)
ev_s_dkk = ev_block("Skeptic, pure-DKK 7.17% variant",
                    {k: ps(SCEN[k], **{**j_over(k), "wacc": FLOOR_DKK}) for k in PROB})
ev_s_usd = ev_block("Skeptic, pure-USD 8.00% variant",
                    {k: ps(SCEN[k], **{**j_over(k), "wacc": 0.08}) for k in PROB})
for alt in ({"BEAR": 0.40, "BASE": 0.45, "BULL": 0.15}, {"BEAR": 0.20, "BASE": 0.55, "BULL": 0.25}):
    ev = sum(alt[k] * SK[k] for k in alt) * FX
    print(f"  probability sensitivity {alt}: EV USD {ev:.2f}, MoS {1-P_USD/ev:+.1%}")

# ------------------------------------------------------------------ 7. capital allocation numbers
hdr("7. CAPITAL ALLOCATION: buyback price proxy and Buffett $1 test (DKK)")
# Annual mean NOVO-B.CO close, yfinance history (split-adjusted), pulled 2026-10-14. Proxy for the
# average repurchase price (Novo does not disclose it by year in the sources read). 2026 = actual 6-K.
AVGP = {2020: 211.78, 2021: 280.65, 2022: 387.38, 2023: 584.36, 2024: 850.63, 2025: 433.90, 2026: 278.97}
BB = {2020: 16855, 2021: 19447, 2022: 24086, 2023: 29924, 2024: 20181, 2025: 1388, 2026: 10558.876}
sh_bought = {y: BB[y] / AVGP[y] for y in BB}
tot_sp, tot_sh = sum(BB.values()), sum(sh_bought.values())
for y in BB:
    print(f"  {y}: spent {BB[y]:>9,.0f} at ~DKK {AVGP[y]:>7.2f} -> ~{sh_bought[y]:5.1f}m shares; "
          f"price paid / today's DKK {P_DKK:.0f} = {AVGP[y]/P_DKK:4.2f}x; / Skeptic EV DKK {ev_s/FX:.0f} = "
          f"{AVGP[y]/(ev_s/FX):4.2f}x")
print(f"  2020-26 total {tot_sp:,.0f} for ~{tot_sh:,.0f}m shares (avg ~DKK {tot_sp/tot_sh:.0f}); worth "
      f"{tot_sh*P_DKK:,.0f} at today's price ({tot_sh*P_DKK/tot_sp-1:+.0%})")
print(f"  2023-24 alone: {BB[2023]+BB[2024]:,.0f} at ~{(BB[2023]+BB[2024])/(sh_bought[2023]+sh_bought[2024]):.0f}"
      f" avg -> worth {(sh_bought[2023]+sh_bought[2024])*P_DKK:,.0f} today")
# $1 test. NI and dividends: facts.json (FY) and 6-K 0000353278-26-000023 (H1-26).
NI = {2021: 47757, 2022: 55525, 2023: 83683, 2024: 100988, 2025: 102434, "H1-26": 69546}
DV = {2021: 21517, 2022: 25303, 2023: 31767, 2024: 44140, 2025: 51763, "H1-26": 35312}
BBX = {2021: 19447, 2022: 24086, 2023: 29924, 2024: 20181, 2025: 1388, "H1-26": 5899}
# Window A: fiscal Dec-2020 -> Dec-2025 (B-share closes 213.325 / 325.25; diluted shares FY20 2,340m
# pre-split x2 = 4,680m, FY25 4,447.7m).
mA0, mA1 = 213.325 * 4680.0, 325.25 * 4447.7
retA = sum(NI[y] - DV[y] for y in range(2021, 2026))
retA_bb = retA - sum(BBX[y] for y in range(2021, 2026))
# Window B: to date, 2021-10-13 -> 2026-10-13 (B close 322.0 x FY21 diluted 4,606.2m; end = ADR close
# in DKK x 4,413.1m). Retained = FY22-FY25 + H1-26 (Q4-21 and Q3-26 not available: noted).
mB0, mB1 = 322.0 * 4606.2, P_DKK * SH
ksB = [2022, 2023, 2024, 2025, "H1-26"]
retB = sum(NI[y] - DV[y] for y in ksB)
retB_bb = retB - sum(BBX[y] for y in ksB)
for lab, m0, m1, r_, rbb in (("A Dec-20 -> Dec-25", mA0, mA1, retA, retA_bb),
                             ("B Oct-21 -> Oct-26", mB0, mB1, retB, retB_bb)):
    print(f"  $1 test {lab}: mcap {m0:,.0f} -> {m1:,.0f} (delta {m1-m0:+,.0f}); retained NI-div {r_:,.0f} "
          f"-> {(m1-m0)/r_:+.2f} per DKK; (retained after buybacks {rbb:,.0f} -> {(m1-m0)/rbb:+.2f})")
print("  Share count: diluted FY20 4,680m (split-adj) -> FY25 4,447.7m (-5.0%); outstanding Oct-26 "
      f"{SH:,.1f}m. SBC FY25 1,435 vs buybacks 2020-24 avg {sum(BB[y] for y in range(2020,2025))/5:,.0f}/yr "
      "-> buybacks far exceed SBC (not merely offsetting).")
