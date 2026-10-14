"""MSFT DCF — base FY2026 actuals from 10-K (FYE 30 June 2026). $M."""

REV26, EBIT26, DA26, CAPEX26, OCF26 = 331_839, 155_237, 38_534, 115_948, 182_935
SHARES = 7_453           # diluted weighted avg
PRICE = 496.88
TAX = 0.19
# Net debt: bonds 40,294 + finance leases 66,594 + operating leases 21,925 - cash&STI 76,843
NET_DEBT = 40_294 + 66_594 + 21_925 - 76_843
EBITDA26 = EBIT26 + DA26

def dcf(growth, ebitda_m, capex_pct, da_pct, wacc, g_term, roic_term, label):
    """growth/ebitda_m/capex_pct/da_pct are per-year lists for FY27..FY36."""
    n = len(growth)
    rev, pv, rows = REV26, 0.0, []
    for i in range(n):
        rev *= (1 + growth[i])
        ebitda = rev * ebitda_m[i]
        da     = rev * da_pct[i]
        ebit   = ebitda - da
        nopat  = ebit * (1 - TAX)
        capex  = rev * capex_pct[i]
        # unearned revenue is a structural cash source; credit 4% of incremental revenue
        dwc    = -0.04 * (rev - rev / (1 + growth[i]))
        fcf    = nopat + da - capex - dwc
        df     = 1 / (1 + wacc) ** (i + 1)
        pv    += fcf * df
        rows.append((2027 + i, rev, ebitda, ebit, da, capex, fcf, fcf * df))
    # terminal: steady state, reinvestment = g / ROIC
    nopat_t = rows[-1][3] * (1 - TAX) * (1 + g_term)
    fcf_t   = nopat_t * (1 - g_term / roic_term)
    tv      = fcf_t / (wacc - g_term)
    pv_tv   = tv * (1 / (1 + wacc) ** n)
    ev      = pv + pv_tv
    eq      = ev - NET_DEBT
    ps      = eq / SHARES
    return dict(label=label, rows=rows, pv_exp=pv, pv_tv=pv_tv, ev=ev, eq=eq, ps=ps,
                tv_share=pv_tv / ev, wacc=wacc, g=g_term)

N = 10
def L(*v):  # expand (value, count) shorthand into exactly N years, padding with the last value
    out = []
    for val, cnt in v: out += [val] * cnt
    while len(out) < N: out.append(out[-1])
    return out[:N]

# Capex paths are anchored on guidance: FY26 cash capex $115.9B; mgmt guided FY27 capex up YoY
# with Q1 FY27 alone >$50B (total, incl. finance leases) => FY27 cash capex ~$160B = ~42% of revenue.
# Each scenario then fades capex/revenue back toward a post-buildout steady state.

# ---------------- BASE ----------------
BASE_G     = L((.16,1),(.14,1),(.125,1),(.11,1),(.10,1),(.09,1),(.08,1),(.07,1),(.06,1),(.05,1))
BASE_EBITD = L((.585,1),(.585,1),(.59,1),(.595,1),(.60,1),(.60,4))
BASE_CAPEX = L((.42,1),(.38,1),(.33,1),(.28,1),(.245,1),(.225,1),(.21,1),(.20,1),(.195,3))
BASE_DA    = L((.145,1),(.180,1),(.200,1),(.210,1),(.210,1),(.205,1),(.20,1),(.195,3))
base = dcf(BASE_G, BASE_EBITD, BASE_CAPEX, BASE_DA,
           wacc=0.085, g_term=0.040, roic_term=0.18, label="BASE")

# ---------------- BULL ----------------
bull = dcf(
    growth   = L((.18,1),(.17,1),(.155,1),(.14,1),(.125,1),(.11,1),(.095,1),(.08,1),(.07,1),(.06,1)),
    ebitda_m = L((.595,1),(.605,1),(.615,1),(.625,1),(.635,1),(.64,4)),
    capex_pct= L((.41,1),(.36,1),(.305,1),(.255,1),(.215,1),(.195,1),(.185,1),(.18,3)),
    da_pct   = L((.14,1),(.175,1),(.19,1),(.195,1),(.195,1),(.19,1),(.185,4)),
    wacc=0.080, g_term=0.045, roic_term=0.24, label="BULL")

# ---------------- BEAR ----------------
# AI capex proves largely value-destroying: Azure growth halves, AI gross margins never scale,
# and a full depreciation wave lands on a decelerating revenue base.
bear = dcf(
    growth   = L((.13,1),(.095,1),(.07,1),(.055,1),(.05,1),(.045,1),(.04,4)),
    ebitda_m = L((.565,1),(.550,1),(.535,1),(.530,1),(.530,1),(.535,4)),
    capex_pct= L((.43,1),(.38,1),(.325,1),(.275,1),(.245,1),(.225,1),(.215,1),(.21,3)),
    da_pct   = L((.15,1),(.195,1),(.225,1),(.24,1),(.245,1),(.24,1),(.235,4)),
    wacc=0.095, g_term=0.030, roic_term=0.14, label="BEAR")

print(f"FY26 actuals: rev {REV26:,} | EBITDA {EBITDA26:,} ({EBITDA26/REV26:.1%}) | "
      f"EBIT margin {EBIT26/REV26:.1%} | capex/rev {CAPEX26/REV26:.1%} | FCF {OCF26-CAPEX26:,}")
print(f"Net debt {NET_DEBT:,} | Mkt cap {PRICE*SHARES/1000:,.0f}B | "
      f"EV {(PRICE*SHARES+NET_DEBT)/1000:,.0f}B | EV/EBITDA {(PRICE*SHARES+NET_DEBT)/EBITDA26:.1f}x\n")

for s in (bear, base, bull):
    print(f"--- {s['label']}  (WACC {s['wacc']:.1%}, g {s['g']:.1%}) ---")
    print(f"{'FY':<6}{'Revenue':>10}{'EBITDA':>10}{'EBIT':>10}{'D&A':>9}{'Capex':>10}{'FCF':>10}")
    for y, rev, ebitda, ebit, da, capex, fcf, _ in s['rows']:
        print(f"{y:<6}{rev/1000:>10,.0f}{ebitda/1000:>10,.0f}{ebit/1000:>10,.0f}"
              f"{da/1000:>9,.0f}{capex/1000:>10,.0f}{fcf/1000:>10,.0f}")
    print(f"PV explicit {s['pv_exp']/1000:,.0f}B | PV terminal {s['pv_tv']/1000:,.0f}B "
          f"({s['tv_share']:.0%} of EV)")
    print(f"EV {s['ev']/1000:,.0f}B | Equity {s['eq']/1000:,.0f}B | "
          f"VALUE/SHARE ${s['ps']:,.0f}  vs ${PRICE} => {s['ps']/PRICE-1:+.0%}\n")

wt = {'BEAR': .25, 'BASE': .50, 'BULL': .25}
blend = sum(s['ps'] * wt[s['label']] for s in (bear, base, bull))
print(f"Probability-weighted (25/50/25): ${blend:,.0f}  =>  {blend/PRICE-1:+.0%} vs ${PRICE}")

# ---- sensitivity on BASE ----
print("\nBASE sensitivity — value/share by WACC x terminal g")
print(f"{'':<8}" + "".join(f"{g:>9.1%}" for g in (.030,.035,.040,.045,.050)))
for w in (.075,.080,.085,.090,.095):
    row = f"{w:<8.1%}"
    for g in (.030,.035,.040,.045,.050):
        r = dcf(BASE_G, BASE_EBITD, BASE_CAPEX, BASE_DA, w, g, 0.18, "s")
        row += f"{r['ps']:>9,.0f}"
    print(row)

print("\nBASE sensitivity — value/share by WACC x terminal ROIC (g fixed 4.0%)")
print(f"{'':<8}" + "".join(f"{r:>9.0%}" for r in (.12,.15,.18,.22,.26)))
for w in (.075,.080,.085,.090,.095):
    row = f"{w:<8.1%}"
    for rc in (.12,.15,.18,.22,.26):
        row += f"{dcf(BASE_G, BASE_EBITD, BASE_CAPEX, BASE_DA, w, .04, rc, 's')['ps']:>9,.0f}"
    print(row)

# ---- reverse DCF: what growth does $496.88 imply? ----
print("\nReverse DCF — solve for constant revenue CAGR at BASE margins/capex path, WACC 8.5%, g 4%")
lo, hi = 0.0, 0.30
for _ in range(60):
    mid = (lo + hi) / 2
    r = dcf([mid]*N, BASE_EBITD, BASE_CAPEX, BASE_DA, 0.085, 0.04, 0.18, "rev")
    if r['ps'] < PRICE: lo = mid
    else: hi = mid
print(f"Market is discounting a ~{mid:.1%} 10-yr revenue CAGR (FY36 revenue ~${REV26*(1+mid)**10/1000:,.0f}B)")

# ---------------- Sum-of-parts floor: what is non-AI Microsoft worth? ----------------
print("\n--- SOTP sanity floor (FY26 segment operating income, taxed at 19%) ---")
segs = [("Productivity & Business Processes", 83_879, 22, "M365/Office/LinkedIn/Dynamics; asset-light, wide moat"),
        ("More Personal Computing",           14_386, 14, "Windows/Xbox/Search; ex-growth, cash generative"),
        ("Intelligent Cloud",                 56_972, 20, "Azure + server; the capex sink")]
tot = 0
for name, oi, mult, note in segs:
    v = oi * (1 - TAX) * mult
    tot += v
    print(f"{name:<36} OI {oi/1000:>6.1f}B  NOPAT {oi*(1-TAX)/1000:>6.1f}B  x{mult}  = {v/1000:>7,.0f}B   {note}")
core = segs[0][1] * (1-TAX) * segs[0][2] + segs[1][1] * (1-TAX) * segs[1][2]
print(f"\nNon-cloud floor (PBP + MPC only), less net debt: ${(core - NET_DEBT)/SHARES:,.0f}/share")
print(f"Full SOTP, less net debt:                          ${(tot - NET_DEBT)/SHARES:,.0f}/share")
print(f"Equity stakes not in SOTP: OpenAI ~27% (carried in $36.3B equity investments); "
      f"marked at $135B in Oct-25 recap = ${135_000/SHARES:,.0f}/share if marked to that round")
