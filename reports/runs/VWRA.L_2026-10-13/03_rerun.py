"""VWRA.L (Vanguard FTSE All-World UCITS ETF, USD Acc) - FUND template model, as of 2026-10-13.

No DCF of a fund (AGENTS.md routing table). Instead:
  M1  Earnings-yield / CAPE-yield real-return anchor of the underlying index.
  M2  10-year Bogle decomposition, bear/base/bull:
        net return = dividend yield + per-share EPS growth + annualised P/E change
                     - TER - US dividend withholding leakage - tracking residual
      and the "hurdle-equivalent value" = price at which that scenario earns exactly k.
  M3  Value-driver justified P/E of the index (perpetual; same steady-state formula as
      valuation.dcf() terminal: payout = 1 - g/ROE), used for the reverse solve and the
      discount-rate x terminal-growth sensitivity grid.

Every input is tagged with its source. ASSUMPTION = Quant-chosen, not sourced; the Skeptic
should challenge those first. UNKNOWN inputs are set to a neutral value and swept.
Run: python3 reports/runs/VWRA.L_2026-10-13/03_rerun.py  (Skeptic re-run of 02_model.py; rf corrected, Section 8 added)
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "methodologies"))
from valuation import peg_is_valid  # noqa: E402

RUN = pathlib.Path(__file__).resolve().parent
facts = json.loads((RUN / "facts.json").read_text())
fund = json.loads((ROOT / "data" / "fundamentals.json").read_text())["records"]["VWRA.L"]

# ---------------------------------------------------------------- sourced inputs
PRICE = facts["price"]                                   # facts: price (yfinance close 2026-10-13)
NAV, NAV_DATE = facts["nav"]["value"], facts["nav"]["date"]   # facts: nav (Vanguard UK, 12 Oct)
PE0 = facts["index_valuation"]["pe"]                     # facts: index_valuation.pe 21.0 (Vanguard, 31 Aug)
PB0 = facts["index_valuation"]["pb"]                     # facts: index_valuation.pb 3.6 (Vanguard, 31 Aug)
PE_YF = fund["trailing_pe"]                              # fundamentals.json trailing_pe 20.97
TER = facts["ter_pct"] / 100                             # facts: ter_pct 0.14
US_W = facts["country_pct"]["US"] / 100                  # facts: country_pct.US 61.68
DY_MSCI = facts["index_valuation"]["proxy_msci_acwi"]["div_yield_pct"] / 100   # PROXY 1.59%, MSCI ACWI 31 Jul
DY_ISH = 0.0140                                          # dossier §8: iShares ACWI trailing yield 1.40% (PROXY)
CAPE_PROXY = facts["index_valuation"]["proxy_global_cape_siblis"]["value"]    # PROXY 29.12, Siblis global
PE_MSCI = facts["index_valuation"]["proxy_msci_acwi"]["pe"]                   # PROXY 23.24
FPE_MSCI = facts["index_valuation"]["proxy_msci_acwi"]["fwd_pe"]              # PROXY 17.13
WHT_US = 0.15      # dossier §9: 15% treaty rate on US dividends for Irish fund - user-stated premise, unverified
N = 10             # horizon, years

# ---------------------------------------------------------------- discount rate
RF_10Y = 0.0522  # SKEPTIC CORRECTION: FRED DGS10 2026-10-08 = 5.22% (fredgraph.csv?id=DGS10, fetched 2026-10-13); was None -> 8% floor
ERP, BETA = 0.05, 1.0   # stated ERP; beta of a cap-weighted all-world index to the world market = 1.0
FLOOR_USD = 0.08


def cost_of_equity(rf):
    return max(FLOOR_USD, rf + BETA * ERP) if rf is not None else FLOOR_USD


K = cost_of_equity(RF_10Y)

# ---------------------------------------------------------------- derived look-through figures
EY = 1 / PE0                       # earnings yield
ROE = PB0 / PE0                    # look-through ROE = E/B = (P/B)/(P/E), same vendor/date
PAYOUT = DY_MSCI * PE0             # dividend payout (mixed vendor: MSCI yield x FTSE P/E)
G_SUST_HI = ROE * (1 - PAYOUT)     # all non-dividend earnings reinvested at current ROE
G_SUST_LO = (1 - PAYOUT) * EY      # all non-dividend earnings spent on buybacks at E/P


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


hr("0. INPUTS")
print(f"Price (13 Oct close)            {PRICE:8.2f} USD   [facts: price]")
print(f"NAV ({NAV_DATE})               {NAV:8.2f} USD   [facts: nav]")
print(f"Price vs NAV (dates differ)     {PRICE / NAV - 1:+8.2%}       indicative only, 1-day date mismatch")
print(f"Index trailing P/E (Vanguard)   {PE0:8.2f}x      [facts]; yfinance {PE_YF:.2f}x [fundamentals.json]")
print(f"Index P/B (Vanguard)            {PB0:8.2f}x      [facts]")
print(f"TER                             {TER:8.2%}       [facts]")
print(f"US weight                       {US_W:8.2%}       [facts]")
print(f"Dividend yield (PROXY MSCI ACWI){DY_MSCI:8.2%}       [facts proxy]; alt iShares ACWI {DY_ISH:.2%} [dossier §8]")
print(f"CAPE (PROXY Siblis global)      {CAPE_PROXY:8.2f}x      [facts proxy]")
print(f"10y yield (FRED DGS10 2026-10-08) {RF_10Y:6.2%}  -> CAPM cost of equity rf+ERP = {K:.2%}")
print(f"data warnings (fundamentals.json): {fund['warnings']}")

hr("1. LOOK-THROUGH QUALITY & YIELDS (M1)")
print(f"Earnings yield 1/PE             {EY:8.2%}")
print(f"CAPE yield 1/CAPE (proxy)       {1 / CAPE_PROXY:8.2%}")
print(f"Look-through ROE = PB/PE        {ROE:8.2%}   vs cost of equity {K:.2%}  spread {ROE - K:+.2%}")
print(f"Payout = DY x PE (mixed vendor) {PAYOUT:8.2%}")
print(f"Sustainable g, all reinvested   {G_SUST_HI:8.2%}   (upper envelope, constant ROE)")
print(f"Sustainable g, all bought back  {G_SUST_LO:8.2%}   (lower envelope, zero organic growth)")
print(f"Trailing PE / CAPE gap (cross-vendor): CAPE/PE = {CAPE_PROXY / PE0:.2f}x (FTSE PE), "
      f"{CAPE_PROXY / PE_MSCI:.2f}x (MSCI PE)")
WHT_DRAG = DY_MSCI * US_W * WHT_US
for lbl, ey in (("1/PE", EY), ("1/CAPE proxy", 1 / CAPE_PROXY)):
    print(f"Real-return anchor {lbl:13s}: gross {ey:6.2%}  net of TER+US WHT {ey - TER - WHT_DRAG:6.2%}"
          f"   nominal = this + inflation (UNKNOWN)")
ok, why = peg_is_valid(PE0, facts["index_valuation"]["forward_pe"], None)
print(f"peg_is_valid(PE={PE0}, fwd=None, growth=None) -> {ok}, '{why}'  => PEG VOID, not cited")


# ---------------------------------------------------------------- M2 Bogle decomposition
def bogle(dy, g, pe_end, pe0=PE0, ter=TER, wht=WHT_US, us_w=US_W, td_resid=0.0, n=N):
    v = (pe_end / pe0) ** (1 / n) - 1
    wht_drag = dy * us_w * wht
    gross = (1 + g) * (1 + v) - 1 + dy
    net = gross - ter - wht_drag - td_resid
    return dict(v=v, wht_drag=wht_drag, gross=gross, net=net)


def hurdle_value(net, k=K, price=PRICE, n=N):
    """Price today at which this scenario's net return equals the hurdle k."""
    return price * ((1 + net) / (1 + k)) ** n


SCEN = {
    #        dividend yield      per-share EPS g (ASSUMPTION)   exit P/E yr10 (ASSUMPTION)
    "Bear": dict(dy=DY_ISH,  g=0.030, pe_end=15.0),
    "Base": dict(dy=DY_MSCI, g=0.050, pe_end=PE0),
    "Bull": dict(dy=DY_MSCI, g=0.075, pe_end=24.0),
}

hr("2. 10-YEAR SCENARIOS (M2, nominal USD, net of TER and US dividend WHT)")
print(f"{'':6s}{'DY':>7s}{'EPS g':>8s}{'PE0':>7s}{'PE10':>7s}{'val chg/yr':>11s}{'WHT':>7s}{'TER':>7s}"
      f"{'gross':>8s}{'NET':>8s}{'price yr10':>11s}{'hurdle-eq val':>14s}{'vs px':>8s}")
results = {}
for name, s in SCEN.items():
    r = bogle(**s)
    p10 = PRICE * (1 + r["net"]) ** N
    hv = hurdle_value(r["net"])
    results[name] = (r, p10, hv)
    print(f"{name:6s}{s['dy']:7.2%}{s['g']:8.2%}{PE0:7.1f}{s['pe_end']:7.1f}{r['v']:11.2%}{r['wht_drag']:7.2%}"
          f"{TER:7.2%}{r['gross']:8.2%}{r['net']:8.2%}{p10:11.2f}{hv:14.2f}{hv / PRICE - 1:+8.1%}")
print(f"hurdle k = {K:.2%} (CAPM, rf 5.22%). 'hurdle-eq val' = price at which scenario returns exactly k.")
print("No terminal value in M2: 100% of return is earned inside the 10-yr window; exit P/E carries the"
      " terminal assumption.")
r_base = results["Base"][0]
print(f"Base return composition: DY {SCEN['Base']['dy']:.2%} + EPS g {SCEN['Base']['g']:.2%} + "
      f"re-rating {r_base['v']:.2%} - costs {TER + r_base['wht_drag']:.2%}")

hr("3. REVERSE SOLVES ('what must be true?')")
# (a) 10-yr: per-share EPS growth needed for net return = k, for a range of exit P/Es
print("(a) 10-yr per-share EPS growth needed to earn the hurdle, base dividend yield & costs")
for pe_end in (15.0, 18.0, PE0, 24.0):
    v = (pe_end / PE0) ** (1 / N) - 1
    need = (K + TER + DY_MSCI * US_W * WHT_US - DY_MSCI + 1) / (1 + v) - 1
    print(f"    exit P/E {pe_end:5.1f}x -> needed EPS g {need:6.2%}/yr")


# (b) perpetual value-driver: trailing PE = (1 - g/ROE) (1+g) / (k - g)
def justified_pe(k, g, roe):
    return (1 - g / roe) * (1 + g) / (k - g)


def implied_g(k, roe, pe=PE0):
    lo, hi = -0.05, k - 1e-4
    for _ in range(200):
        mid = (lo + hi) / 2
        if justified_pe(k, mid, roe) < pe:
            lo = mid
        else:
            hi = mid
    return mid


print("(b) perpetual nominal growth implied by trailing P/E 21.0x (value-driver, payout = 1 - g/ROE)")
for k in (0.07, 0.08, 0.09, 0.10):
    row = "    k={:.0%}: ".format(k) + "  ".join(
        f"ROE {roe:5.1%} -> g {implied_g(k, roe):6.2%}" for roe in (0.10, 0.13, ROE, 0.25))
    print(row)
print(f"    terminal-growth cap = min(4%, 10y yield 5.22%) -> 4% used as cap")


# ---------------------------------------------------------------- M3 sensitivity grid
def value_ps(k, g, roe=ROE):
    return PRICE * justified_pe(k, g, roe) / PE0


hr("4. SENSITIVITY: value per share = price x justified PE / 21.0  (ROE held at look-through %.1f%%)" % (ROE * 100))
gs = (0.02, 0.03, 0.04, 0.05)
print("k \\ g      " + "".join(f"{g:>10.0%}" for g in gs) + "    (5% column exceeds the 4% cap; shown for reference)")
for k in (0.07, 0.08, 0.09):
    print(f"{k:<10.0%} " + "".join(f"{value_ps(k, g):10.2f}" for g in gs))
print("justified trailing P/E:")
for k in (0.07, 0.08, 0.09):
    print(f"{k:<10.0%} " + "".join(f"{justified_pe(k, g, ROE):9.1f}x" for g in gs))

hr("5. 10-YR NET RETURN GRID (M2): exit P/E x per-share EPS growth, base DY & costs")
pes = (15.0, 18.0, 21.0, 24.0, 27.0)
print("g \\ exitPE " + "".join(f"{p:>9.0f}x" for p in pes))
for g in (0.02, 0.03, 0.04, 0.05, 0.06, 0.075):
    print(f"{g:<10.1%} " + "".join(f"{bogle(DY_MSCI, g, p)['net']:10.2%}" for p in pes))

hr("6. COST & UNKNOWN SWEEPS on base (annual net return; hurdle-eq value)")
for lbl, kw in (("TER 0.14% (base)", {}),
                ("drag = indicative TD 0.02% instead of TER", dict(ter=0.0002)),
                ("stale TER 0.19% (conflict)", dict(ter=0.0019)),
                ("+0.30% unexplained tracking residual", dict(td_resid=0.003)),
                ("US WHT 30% (US-domiciled equivalent)", dict(wht=0.30)),
                ("US WHT 0%", dict(wht=0.0)),
                ("DY 1.40% (iShares proxy)", dict(dy=DY_ISH))):
    s = {**SCEN["Base"], **kw}
    r = bogle(**s)
    print(f"  {lbl:44s} net {r['net']:6.2%}   hurdle-eq {hurdle_value(r['net']):7.2f}")
print("  SGD investor: USD/SGD drift UNKNOWN; each +/-1%/yr of USD move = +/-1%/yr SGD return,"
      f" i.e. 10-yr x{1.01 ** 10:.3f} / x{0.99 ** 10:.3f}")
for rf in (0.02, 0.03, 0.04, 0.05):
    k = cost_of_equity(rf)
    print(f"  HYPOTHETICAL 10y = {rf:.0%}: k = {k:.2%}  base hurdle-eq value {hurdle_value(r_base['net'], k=k):7.2f}")

hr("7. LOAD-BEARING INPUTS: +/-10% of each input, base case")
base_net = r_base["net"]
base_hv = hurdle_value(base_net)
print(f"base: net {base_net:.2%}/yr, hurdle-eq value {base_hv:.2f}, perpetual value {value_ps(K, 0.04):.2f} (k {K:.2%}, g 4%)")


def m2(**over):
    s = dict(dy=DY_MSCI, g=0.05, pe_end=PE0, pe0=PE0, ter=TER, wht=WHT_US, us_w=US_W)
    s.update(over)
    return bogle(**s)["net"]


rows = []
for name, key, base_val in (("exit P/E (yr 10)", "pe_end", PE0),
                            ("starting P/E (measurement)", "pe0", PE0),
                            ("per-share EPS growth", "g", 0.05),
                            ("dividend yield", "dy", DY_MSCI),
                            ("TER", "ter", TER),
                            ("US WHT rate", "wht", WHT_US),
                            ("US weight", "us_w", US_W)):
    lo = m2(**{key: base_val * 0.9})
    hi = m2(**{key: base_val * 1.1})
    rows.append((name, lo, hi, hurdle_value(lo), hurdle_value(hi)))
for name, lo, hi, hvlo, hvhi in sorted(rows, key=lambda x: -abs(x[4] - x[3])):
    print(f"  {name:28s} -10%: net {lo:6.2%} val {hvlo:7.2f} ({hvlo / base_hv - 1:+6.1%})   "
          f"+10%: net {hi:6.2%} val {hvhi:7.2f} ({hvhi / base_hv - 1:+6.1%})")
for k in (K * 0.9, K * 1.1):
    print(f"  hurdle k {k:.2%}           value {hurdle_value(base_net, k=k):7.2f} "
          f"({hurdle_value(base_net, k=k) / base_hv - 1:+6.1%})")
pv = value_ps(K, 0.04)
for lbl, v in (("ROE -10% (perpetual M3)", value_ps(K, 0.04, ROE * 0.9)),
               ("ROE +10% (perpetual M3)", value_ps(K, 0.04, ROE * 1.1)),
               ("terminal g -10% (3.6%)", value_ps(K, 0.036)),
               ("terminal g +10% (4.4%)", value_ps(K, 0.044))):
    print(f"  {lbl:28s} perpetual value {v:7.2f} ({v / pv - 1:+6.1%})")


# ============================================================================ SKEPTIC ADDITIONS
hr("8. SKEPTIC: implied ERP, bond-parity reverse, probabilities, extra sweeps")
RF = RF_10Y
print(f"rf (US 10y, FRED DGS10 2026-10-08) = {RF:.2%}; CAPM k = rf + {ERP:.0%} ERP = {K:.2%}; 8% floor no longer binds")

print("\n(a) Implied equity risk premium = 10-yr net return - 10y UST yield")
for name, (r, p10, hv) in results.items():
    print(f"    {name:5s} net {r['net']:6.2%}  ERP {r['net'] - RF:+6.2%}")

print("\n(b) EPS growth needed (base DY & costs) for net return = target, by exit P/E")
for tgt_lbl, tgt in (("= UST 5.22% (ERP 0)", RF), ("= UST + 3%", RF + 0.03),
                     ("= UST + 4%", RF + 0.04), ("= CAPM k", K)):
    cells = []
    for pe_end in (15.0, 18.0, PE0, 24.0):
        v = (pe_end / PE0) ** (1 / N) - 1
        need = (tgt + TER + DY_MSCI * US_W * WHT_US - DY_MSCI + 1) / (1 + v) - 1
        cells.append(f"{pe_end:4.0f}x {need:6.2%}")
    print(f"    target {tgt_lbl:20s}: " + "  ".join(cells))


def implied_k(pe, g, roe):
    """Market-implied perpetual k from trailing PE = (1-g/ROE)(1+g)/(k-g)."""
    return (1 - g / roe) * (1 + g) / pe + g


print("\n(c) Perpetual market-implied k and ERP at trailing P/E 21.0x (M3 identity)")
for roe in (0.13, ROE):
    for g in (0.03, 0.04):
        k_imp = implied_k(PE0, g, roe)
        print(f"    ROE {roe:5.1%}  g {g:.0%}: implied k {k_imp:6.2%}  implied ERP {k_imp - RF:+6.2%}")

print("\n(d) M3 justified trailing P/E and value at the corrected k (ROE 17.1%)")
for k in (RF + 0.04, K):
    for g in (0.03, 0.04):
        jp = justified_pe(k, g, ROE)
        print(f"    k {k:6.2%} g {g:.0%}: justified P/E {jp:5.1f}x  value {value_ps(k, g):7.2f}"
              f"  ({value_ps(k, g) / PRICE - 1:+6.1%} vs price)")
print(f"    Quant centre (k 8%, g 4%): {value_ps(0.08, 0.04):7.2f}")

print("\n(e) Probability-weighted outcomes (Skeptic weights)")
PROBS = {"Bear": 0.25, "Base": 0.55, "Bull": 0.20}
for lbl, probs in (("Skeptic 25/55/20", PROBS),
                   ("alt 20/60/20", {"Bear": 0.20, "Base": 0.60, "Bull": 0.20}),
                   ("alt 30/50/20", {"Bear": 0.30, "Base": 0.50, "Bull": 0.20})):
    ew = sum(probs[n] * results[n][1] for n in probs)            # expected yr-10 wealth (price)
    er_w = (ew / PRICE) ** (1 / N) - 1                           # annualised from expected wealth
    er_r = sum(probs[n] * results[n][0]["net"] for n in probs)   # probability-weighted annual return
    print(f"  {lbl:17s}: E[price yr10] {ew:7.2f} -> {er_w:6.2%}/yr (wealth-wtd); {er_r:6.2%}/yr (return-wtd);"
          f" ERP {er_w - RF:+.2%}")
print("  Informational only (FUND verdict does not use MoS): EV of hurdle-equivalent values")
for k_lbl, k in (("CAPM k 10.22%", K), ("Quant floor 8%", 0.08), ("bond parity 5.22%", RF)):
    hv = {n: hurdle_value(results[n][0]["net"], k=k) for n in PROBS}
    ev = sum(PROBS[n] * hv[n] for n in PROBS)
    bear = hv["Bear"]
    asym = "no downside to bear" if bear >= PRICE else f"{(ev - PRICE) / (PRICE - bear):+.2f}"
    print(f"    {k_lbl:18s}: bear {bear:7.2f} base {hv['Base']:7.2f} bull {hv['Bull']:7.2f}  EV {ev:7.2f}"
          f"  MoS {1 - PRICE / ev:+7.1%}  asymmetry {asym}")

print("\n(f) Extra sweeps on the base (net return / ERP)")
sweeps = (
    ("DY 1.32% (Vanguard unlabeled 30 Sep figure)", dict(dy=0.0132)),
    ("extra non-US WHT leakage +0.10%/yr (illustrative)", dict(td_resid=0.0010)),
    ("earnings 10% above trend, reset over 10y", dict(g=(1.05 * 0.90 ** 0.1) - 1)),
    ("exit P/E 19x (partial rate de-rating)", dict(pe_end=19.0)),
    ("earnings reset 10% AND exit 19x", dict(g=(1.05 * 0.90 ** 0.1) - 1, pe_end=19.0)),
)
for lbl, kw in sweeps:
    s = {**SCEN["Base"], **kw}
    r = bogle(**s)
    print(f"    {lbl:50s} net {r['net']:6.2%}  ERP {r['net'] - RF:+6.2%}")

print("\n(g) Starting-P/E measurement test (vendor definition), done consistently")
for pe0 in (PE0, PE_MSCI):
    rb = bogle(DY_MSCI, 0.05, pe0, pe0=pe0)            # base = no re-rating: exit tracks the same definition
    rbe = bogle(DY_ISH, 0.03, 15.0, pe0=pe0)           # bear exit 15x is an absolute level
    print(f"    PE0 {pe0:5.2f}x: base net {rb['net']:6.2%} (unchanged by definition)  bear(15x) net {rbe['net']:6.2%}")
