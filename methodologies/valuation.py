"""Reusable valuation engine. Part 5 of the framework must RUN this, not narrate it.

Two entry points:
  dcf()          - explicit-horizon FCF DCF with a reinvestment-linked terminal value
  reverse_dcf()  - what growth does today's price already discount?

Design rules learned from the audit and from msft_dcf.py / rvmd_dcf.py:
  * Terminal value uses reinvestment = g / ROIC, never a plucked exit multiple.
  * If a decline phase is modelled explicitly, terminal value is ZERO -- a growing
    perpetuity stacked on a modelled cliff double-counts (this produced a NEGATIVE
    terminal value in the first RVMD run).
  * Opex must flex with revenue. Holding R&D flat through a decline manufactures
    fake distress.
  * Equity value is floored at net cash: management stops spending before it burns
    the balance sheet to zero.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DCFResult:
    per_share: float
    equity_value: float
    enterprise_value: float
    pv_explicit: float
    pv_terminal: float
    terminal_share: float
    rows: list[tuple]

    def upside(self, price: float) -> float:
        return self.per_share / price - 1.0


def dcf(*, base_revenue: float, growth: list[float], ebitda_margin: list[float],
        capex_pct: list[float], da_pct: list[float], tax: float, wacc: float,
        net_debt: float, shares: float, terminal_growth: float,
        terminal_roic: float, wc_pct_of_delta_rev: float = 0.0,
        terminal_value: bool = True, acq_amort_pct: list[float] | None = None,
        mid_year: bool = False, stub_years: float = 0.0) -> DCFResult:
    """Free-cash-flow-to-firm DCF. All rate lists must be the same length (years).

    Options added after the Oct 2026 pilot (defaults reproduce the old results exactly):
      acq_amort_pct  amortisation of ACQUIRED intangibles, as % of revenue, already included in
                     da_pct. It is non-cash and does not recur, so it is added back to EBIT
                     for the terminal year. Otherwise an acquisition-heavy company (ZBH: D&A
                     $1.1B vs capex $0.3B) gets a terminal NOPAT understated by the amortisation.
      mid_year       discount each year's FCF at t-0.5 (cash arrives through the year).
      stub_years     years between the base-period end and the valuation (price) date. EV is
                     rolled forward by (1+wacc)**stub_years (TSM: 30 Jun base vs 13 Oct price).
    """
    n = len(growth)
    if not all(len(x) == n for x in (ebitda_margin, capex_pct, da_pct)):
        raise ValueError("growth/ebitda_margin/capex_pct/da_pct must be equal length")
    if terminal_value and wacc <= terminal_growth:
        raise ValueError(f"wacc ({wacc}) must exceed terminal growth ({terminal_growth})")

    rev, pv, rows = base_revenue, 0.0, []
    for i in range(n):
        prev = rev
        rev *= (1 + growth[i])
        ebitda = rev * ebitda_margin[i]
        da = rev * da_pct[i]
        ebit = ebitda - da
        nopat = ebit * (1 - tax)
        capex = rev * capex_pct[i]
        dwc = wc_pct_of_delta_rev * (rev - prev)
        fcf = nopat + da - capex - dwc
        df = 1 / (1 + wacc) ** (i + (0.5 if mid_year else 1.0))
        pv += fcf * df
        rows.append((i + 1, rev, ebitda, ebit, da, capex, fcf, fcf * df))

    pv_tv = 0.0
    if terminal_value:
        ebit_t = rows[-1][3] + (rows[-1][1] * acq_amort_pct[-1] if acq_amort_pct else 0.0)
        nopat_t = ebit_t * (1 - tax) * (1 + terminal_growth)
        fcf_t = nopat_t * (1 - terminal_growth / terminal_roic)
        pv_tv = (fcf_t / (wacc - terminal_growth)) / (1 + wacc) ** n

    ev = (pv + pv_tv) * (1 + wacc) ** stub_years
    pv, pv_tv = pv * (1 + wacc) ** stub_years, pv_tv * (1 + wacc) ** stub_years
    eq = max(ev - net_debt, -net_debt)          # floor: never below net cash
    return DCFResult(per_share=eq / shares, equity_value=eq, enterprise_value=ev,
                     pv_explicit=pv, pv_terminal=pv_tv,
                     terminal_share=(pv_tv / ev if ev else 0.0), rows=rows)


def reverse_dcf(*, price: float, base_revenue: float, years: int, lo: float = -0.20,
                hi: float = 0.60, **kw) -> float:
    """Constant revenue CAGR that makes the DCF equal today's price.

    This is the single most useful discipline in the whole framework: it converts
    'is it expensive?' into 'what would have to be true?', which is falsifiable.
    """
    for _ in range(80):
        mid = (lo + hi) / 2
        got = dcf(base_revenue=base_revenue, growth=[mid] * years, **kw).per_share
        if got < price:
            lo = mid
        else:
            hi = mid
    return mid


def sensitivity(param_a: dict, param_b: dict, **kw) -> list[list[float]]:
    """Grid of per-share values over two swept parameters.
    e.g. sensitivity({'wacc': [...]}, {'terminal_growth': [...]}, **base_kwargs)"""
    (ka, va), (kb, vb) = next(iter(param_a.items())), next(iter(param_b.items()))
    return [[dcf(**{**kw, ka: a, kb: b}).per_share for b in vb] for a in va]


def fcf_yield(fcf: float, market_cap: float) -> float:
    """The honest cross-check on any capex-heavy business, where EV/EBITDA flatters."""
    return fcf / market_cap


def peg_is_valid(trailing_pe: float | None, forward_pe: float | None,
                 growth: float | None) -> tuple[bool, str]:
    """Gate PEG before it is allowed to drive anything. The NVO failure was a PEG of
    3.36 read as 'extremely expensive' when it actually meant earnings were shrinking."""
    if growth is None or trailing_pe is None:
        return False, "missing growth or P/E"
    if growth <= 0:
        return False, f"growth {growth:.1%} <= 0: PEG undefined"
    if growth < 0.05:
        return False, f"growth {growth:.1%} < 5%: PEG unstable, denominator near zero"
    if forward_pe is not None and forward_pe > trailing_pe:
        return False, (f"forward P/E {forward_pe:.1f} > trailing {trailing_pe:.1f}: "
                       "earnings declining, PEG meaningless")
    return True, "ok"
