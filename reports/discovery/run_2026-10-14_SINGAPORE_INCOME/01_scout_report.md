<!-- pipeline:discover-screen -->
# Discovery Stage 1: screen, SINGAPORE_INCOME on DIVIDEND_NON_US (2026-10-14)

> Quantitative screen on vendor data. Candidates for `/analyse`, not recommendations.
> Rules: {'min_yield': 3.0, 'max_nd_ebitda': 3.5, 'min_fin_roe': 10.0}. Screened 17, qualified 10, fetch failures 0.

## New candidates

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **BATS.L** | BRITISH AMERICAN TOBACCO | 42.25 GBP · -21.3% vs 52w high · P/E (ttm/fwd) 14.6x/10.9x · EV/EBITDA 11.1x · yield 5.8% | yield 5.8%, net debt/EBITDA 2.9x, return blend 10.1% | net debt/EBITDA 2.9x | UK: 0% dividend WHT | none verified: `/analyse BATS.L` |
| **D05.SI** | DBS | 74.06 SGD · -6.3% vs 52w high · P/E (ttm/fwd) 12.3x/16.7x · EV/EBITDA n/a · yield 4.3% | yield 4.3%, ROE 16.2% | financial: judged on ROE, not EV/EBITDA or net cash; forward P/E 16.7 > trailing 12.3: earnings expected to fall | Singapore: 0% dividend WHT (one-tier) | none verified: `/analyse D05.SI` |
| **RIO.L** | RIO TINTO PLC ORD 10P | 69.97 GBP · -23.3% vs 52w high · P/E (ttm/fwd) 12.7x/11.3x · EV/EBITDA 5.8x · yield 4.9% | yield 4.9%, net debt/EBITDA 0.6x, return blend 14.8% | none | UK: 0% dividend WHT | none verified: `/analyse RIO.L` |
| **GSK.L** | GSK PLC ORD 31 1/4P | 17.53 GBP · -23.2% vs 52w high · P/E (ttm/fwd) 14.9x/9.2x · EV/EBITDA 7.9x · yield 3.8% | yield 3.8%, net debt/EBITDA 1.4x, return blend 24.0% | none | UK: 0% dividend WHT | none verified: `/analyse GSK.L` |
| **ULVR.L** | UNILEVER PLC ORD 3.5P | 47.10 GBP · -15.0% vs 52w high · P/E (ttm/fwd) 12.8x/16.2x · EV/EBITDA 11.9x · yield 3.5% | yield 3.5%, net debt/EBITDA 2.4x, return blend 22.4% | forward P/E 16.2 > trailing 12.8: earnings expected to fall | UK: 0% dividend WHT | none verified: `/analyse ULVR.L` |
