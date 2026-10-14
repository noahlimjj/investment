"""RVMD risk-adjusted DCF. Revolution Medicines, as of 28 Aug 2026.
Daraxonrasib (RASONQUE) approved 26 Aug 2026 for mPDAC 2L+ / 1L-unfit.
Base data: Q2-26 10-Q + 8-K, US PI, Royalty Pharma agreement."""

PRICE   = 221.15
SHARES0 = 214.336          # M, outstanding 31 Jul 2026
CASH    = 3_938            # $M, 30 Jun 2026 (incl. Apr-26 raise + RP tranche 2)
CONVERTS= 500              # $M, 0.50% due 2033
RP_AVAIL= 1_500            # $M committed but undrawn (not counted as cash)
TAX     = 0.21
NOL     = 3_400            # $M accumulated deficit sheltering early profit

# Royalty Pharma synthetic royalty, tiered on daraxonrasib WW net sales ($B)
RP_TIERS = [(2.0, 0.0455), (4.0, 0.0250), (8.0, 0.0100), (999, 0.0)]
def rp_royalty(sales_bn):
    owed, lo = 0.0, 0.0
    for hi, rate in RP_TIERS:
        if sales_bn <= lo: break
        owed += (min(sales_bn, hi) - lo) * rate
        lo = hi
    return owed * 1000       # $M

def ramp(peak, start_yr, peak_yr, first_val, loe_yr, decay, years):
    """S-curve to peak, flat, then LOE erosion."""
    out = {}
    for y in years:
        if y < start_yr:            v = 0.0
        elif y == start_yr:         v = first_val
        elif y <= peak_yr:
            f = (y - start_yr) / (peak_yr - start_yr)
            v = first_val + (peak - first_val) * (f ** 0.75)
        elif y < loe_yr:            v = peak
        else:                       v = peak * (decay ** (y - loe_yr + 1))
        out[y] = v
    return out

YEARS = list(range(2026, 2046))

def run(label, peak, first_val, peak_yr, rd_peak, sga_peak, wacc, tgr,
        loe_yr=2043, decay=0.70, extra_shares=0.0, cogs=0.11):
    """R&D and SG&A both flex with the revenue base — a company facing a patent
    cliff cuts spend, it does not keep burning peak R&D into a collapsing top line.
    Terminal value is set to zero: the LOE erosion is modelled explicitly inside
    the horizon, so a growing perpetuity on top would double-count."""
    rev = ramp(peak, 2026, peak_yr, first_val, loe_yr, decay, YEARS)
    nol, pv, rows = NOL, 0.0, []
    for i, y in enumerate(YEARS):
        r = rev[y]
        # R&D builds to a plateau, then scales back with the post-LOE revenue base
        rd_plateau = min(rd_peak, 1_550 + (rd_peak - 1_550) * min(1, (y - 2026) / 6)) if y > 2026 else 1_550
        rd  = rd_plateau * (1.0 if y < loe_yr else max(0.40, r / peak))
        sga = 430 + (sga_peak - 430) * min(1.0, r / peak) if peak else 430
        roy = rp_royalty(r / 1000)
        ebit = r - r * cogs - roy - rd - sga
        if ebit > 0 and nol > 0:                     # NOLs shelter early profits
            shielded = min(ebit, nol); nol -= shielded
            tax = (ebit - shielded) * TAX
        else:
            tax = ebit * TAX if ebit > 0 else 0.0
        fcf = ebit - tax                              # capex/WC ~ negligible for oral small molecule
        df  = 1 / (1 + wacc) ** (i + 0.5)
        pv += fcf * df
        rows.append((y, r, rd, sga, roy, ebit, fcf))
    pv_tv = 0.0
    ev  = pv
    eq  = ev + CASH - CONVERTS
    # Floor: management would halt discretionary R&D rather than burn equity to zero.
    # Downside is bounded near net cash plus whatever the approved product is worth.
    eq  = max(eq, CASH - CONVERTS)
    ps  = eq / (SHARES0 + extra_shares)
    return dict(label=label, rows=rows, ev=ev, eq=eq, ps=ps, pv_tv=pv_tv, peak=peak)

S = [
  # label   peak$M  2026  peakYr  R&D    SG&A   wacc   tgr   LOE   decay  dil
  # Bear: 2L PDAC only. 1L (RASolute 303) and NSCLC (RASolve 301) both miss.
  run("BEAR",  4_000,  150, 2033,  1_750, 1_050, 0.110, 0.00, 2042, 0.65, 30.0),
  # Base: PDAC franchise established across 2L + partial 1L, one NSCLC indication wins.
  run("BASE", 11_000,  180, 2034,  2_300, 1_650, 0.095, 0.01, 2043, 0.70, 12.0),
  # Bull: full RAS franchise - PDAC all lines + adjuvant, G12C/G12D NSCLC, CRC.
  run("BULL", 18_000,  210, 2033,  2_600, 2_150, 0.085, 0.02, 2044, 0.75,  5.0),
]

print(f"RVMD @ ${PRICE}  |  shares {SHARES0:.1f}M  |  mkt cap ${PRICE*SHARES0/1000:,.1f}B")
print(f"Cash ${CASH/1000:.2f}B  converts ${CONVERTS/1000:.1f}B  =>  EV ${(PRICE*SHARES0-CASH+CONVERTS)/1000:,.1f}B")
print(f"Undrawn Royalty Pharma capital: ${RP_AVAIL/1000:.1f}B\n")

for s in S:
    print(f"--- {s['label']}  (peak WW sales ${s['peak']/1000:.1f}B) ---")
    print(f"{'Yr':<6}{'Revenue':>9}{'R&D':>7}{'SG&A':>7}{'RPRoy':>7}{'EBIT':>9}{'FCF':>9}")
    for y, r, rd, sga, roy, ebit, fcf in s['rows']:
        if y % 2 == 0 or y < 2032:
            print(f"{y:<6}{r:>9,.0f}{rd:>7,.0f}{sga:>7,.0f}{roy:>7,.0f}{ebit:>9,.0f}{fcf:>9,.0f}")
    print(f"EV ${s['ev']/1000:,.1f}B (explicit horizon to 2045, no terminal) | "
          f"Equity ${s['eq']/1000:,.1f}B | VALUE/SHARE ${s['ps']:,.0f} => {s['ps']/PRICE-1:+.0%}\n")

wt = {'BEAR': .25, 'BASE': .45, 'BULL': .30}
blend = sum(s['ps'] * wt[s['label']] for s in S)
print(f"Probability-weighted (25/45/30): ${blend:,.0f} => {blend/PRICE-1:+.0%}\n")

# reverse DCF: peak sales implied by today's price, base-case structure
lo, hi = 1_000.0, 40_000.0
for _ in range(70):
    mid = (lo + hi) / 2
    r = run("solve", mid, 180, 2034, 2_300, 1_650, 0.095, 0.01, 2043, 0.70, 12.0)
    if r['ps'] < PRICE: lo = mid
    else: hi = mid
print(f"REVERSE DCF: ${PRICE} implies ~${mid/1000:.1f}B of peak worldwide sales")
print(f"  (vs sell-side: $5.0-7.6B PDAC consensus; RBC ~$11.5B all-indication peak)\n")

print("Sensitivity — base-case value/share by peak sales x WACC")
peaks = [5_000, 8_000, 11_000, 15_000, 20_000]
print(f"{'WACC':<8}" + "".join(f"{p/1000:>9.1f}B" for p in peaks))
for w in (0.075, 0.085, 0.095, 0.105, 0.115):
    row = f"{w:<8.1%}"
    for p in peaks:
        row += f"{run('s', p, 180, 2034, 2_300, 1_650, w, 0.01, 2043, 0.70, 12.0)['ps']:>10,.0f}"
    print(row)

print("\nRoyalty Pharma drag at various sales levels:")
for sb in (2, 4, 6, 8, 12):
    print(f"  ${sb}B sales -> ${rp_royalty(sb):,.0f}M royalty ({rp_royalty(sb)/(sb*1000):.2%} blended)")
