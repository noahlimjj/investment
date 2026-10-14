# Opportunity screen (2026-10-14)

> Screen results from quantitative filters on vendor data (yfinance). These are candidates for the 3-agent `/analyse` pipeline, not recommendations. A buy, hold or sell view only comes from a verified pipeline run.
> Holdings used for the overlap check: 19 (data/portfolio.json).

## SINGAPORE_INCOME: Non-US dividend payers (0% WHT for a Singapore resident)

Universe DIVIDEND_NON_US · screened 17 · qualified 10

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **BATS.L** | BRITISH AMERICAN TOBACCO | 42.25 GBP · -21.3% vs 52w high · P/E (ttm/fwd) 14.6x/10.9x · EV/EBITDA 11.1x · yield 5.8% | yield 5.8%, net debt/EBITDA 2.9x, return blend 10.1% | net debt/EBITDA 2.9x | UK: 0% dividend WHT | none verified: `/analyse BATS.L` |
| **D05.SI** | DBS | 74.06 SGD · -6.3% vs 52w high · P/E (ttm/fwd) 12.3x/16.7x · EV/EBITDA n/a · yield 4.3% | yield 4.3%, ROE 16.2% | financial: judged on ROE, not EV/EBITDA or net cash; forward P/E 16.7 > trailing 12.3: earnings expected to fall | Singapore: 0% dividend WHT (one-tier) | none verified: `/analyse D05.SI` |
| **RIO.L** | RIO TINTO PLC ORD 10P | 69.97 GBP · -23.3% vs 52w high · P/E (ttm/fwd) 12.7x/11.3x · EV/EBITDA 5.8x · yield 4.9% | yield 4.9%, net debt/EBITDA 0.6x, return blend 14.8% | none | UK: 0% dividend WHT | none verified: `/analyse RIO.L` |
| **GSK.L** | GSK PLC ORD 31 1/4P | 17.53 GBP · -23.2% vs 52w high · P/E (ttm/fwd) 14.9x/9.2x · EV/EBITDA 7.9x · yield 3.8% | yield 3.8%, net debt/EBITDA 1.4x, return blend 24.0% | none | UK: 0% dividend WHT | none verified: `/analyse GSK.L` |
| **ULVR.L** | UNILEVER PLC ORD 3.5P | 47.10 GBP · -15.0% vs 52w high · P/E (ttm/fwd) 12.8x/16.2x · EV/EBITDA 11.9x · yield 3.5% | yield 3.5%, net debt/EBITDA 2.4x, return blend 22.4% | forward P/E 16.2 > trailing 12.8: earnings expected to fall | UK: 0% dividend WHT | none verified: `/analyse ULVR.L` |

## BUFFETT_MOAT: High-return European compounders

Universe EURO_COMPOUNDERS · screened 11 · qualified 8 · fetch failures: ROG.SW: no price from vendor

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **ASML.AS** | ASML HOLDING | 1,509.60 EUR · -13.3% vs 52w high · P/E (ttm/fwd) 54.8x/28.7x · EV/EBITDA 42.6x · yield 0.5% | return blend 38.9% (0.6 ROE + 0.4 ROA), operating margin 37.1%, net debt/EBITDA -0.4x, -13.3% from 52w high | none | Netherlands: local dividend WHT (check treaty rate) | none verified: `/analyse ASML.AS` |
| **RACE** | Ferrari N.V. | 391.60 USD · -10.4% vs 52w high · P/E (ttm/fwd) 36.4x/31.8x · EV/EBITDA 28.6x · yield 1.1% | return blend 32.7% (0.6 ROE + 0.4 ROA), operating margin 31.1%, net debt/EBITDA 0.7x, -10.4% from 52w high | none | Italy: local dividend WHT (check treaty rate); US-listed ADR: depositary fees, estate-tax treatment unsettled (primary listing avoids both) | none verified: `/analyse RACE` |
| **NOVN.SW** | NOVARTIS N | 119.30 CHF · -10.1% vs 52w high · P/E (ttm/fwd) 22.9x/14.5x · EV/EBITDA 11.6x · yield 3.1% | return blend 22.3% (0.6 ROE + 0.4 ROA), operating margin 34.6%, net debt/EBITDA 1.8x, -10.1% from 52w high | none | Switzerland: local dividend WHT (check treaty rate) | none verified: `/analyse NOVN.SW` |
| **SAP.DE** | SAP SE                   | 197.28 EUR · -19.2% vs 52w high · P/E (ttm/fwd) 28.5x/23.6x · EV/EBITDA 19.3x · yield 1.3% | return blend 14.8% (0.6 ROE + 0.4 ROA), operating margin 27.6%, net debt/EBITDA -0.1x, -19.2% from 52w high | none | Germany: local dividend WHT (check treaty rate) | none verified: `/analyse SAP.DE` |
| **ITX.MC** | INDUSTRIA DE DISE...O TE | 54.14 EUR · -8.9% vs 52w high · P/E (ttm/fwd) 26.4x/22.9x · EV/EBITDA 16.8x · yield 1.2% | return blend 28.0% (0.6 ROE + 0.4 ROA), operating margin 18.9%, net debt/EBITDA -0.4x, -8.9% from 52w high | none | Spain: local dividend WHT (check treaty rate) | none verified: `/analyse ITX.MC` |

## LYNCH_GARP: Lynch growth at a reasonable price / fallen stalwarts

Universe FALLEN_STALWARTS · screened 17 · qualified 2

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **7974.T** | NINTENDO CO LTD | 8,250.00 JPY · -43.6% vs 52w high · P/E (ttm/fwd) 20.1x/24.2x · EV/EBITDA 16.1x · yield 2.7% | Lynch ratio 2.38 = (55.0% EPS growth, latest quarter YoY + 2.7% yield) / 24.2x P/E; forward P/E 24.2x | forward P/E 24.2 > trailing 20.1: earnings expected to fall; -44% from 52w high: find out why before anything else | Japan: 15.315% dividend WHT | none verified: `/analyse 7974.T` |
| **BN.PA** | DANONE | 58.74 EUR · -26.7% vs 52w high · P/E (ttm/fwd) 19.5x/13.9x · EV/EBITDA 10.4x · yield 3.8% | Lynch ratio 1.17 = (12.4% EPS growth, latest quarter YoY + 3.8% yield) / 13.9x P/E; forward P/E 13.9x | none | France: local dividend WHT (check treaty rate) | none verified: `/analyse BN.PA` |

## NET_CASH_BARGAIN: Cash-rich Asian companies

Universe ASIA_COMPOUNDERS · screened 10 · qualified 1

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **4063.T** | SHIN-ETSU CHEMICAL CO | 6,180.00 JPY · -22.1% vs 52w high · P/E (ttm/fwd) 24.5x/18.7x · EV/EBITDA 11.4x · yield 1.9% | net cash 12.4% of price, forward P/E 18.7x, net-cash-adjusted P/E 21.4x | none | Japan: 15.315% dividend WHT | none verified: `/analyse 4063.T` |

## Held positions that passed a screen

Passing a screen is not a reason to add. The pipeline verdict decides.

| Ticker | Company | Metrics | Why it passed | Data flags | Tax (SG resident) | Pipeline |
|---|---|---|---|---|---|---|
| **MC.PA** | LVMH | 384.05 EUR · -41.3% vs 52w high · P/E (ttm/fwd) 17.5x/15.9x · EV/EBITDA 10.8x · yield 3.4% | return blend 13.0% (0.6 ROE + 0.4 ROA), operating margin 22.5%, net debt/EBITDA 1.2x, -41.3% from 52w high | -41% from 52w high: find out why before anything else | France: local dividend WHT (check treaty rate) | HOLD (MEDIUM, 2026-10-13) |

## Next step

Run the 3-agent pipeline on a candidate before any decision:

- `/analyse BATS.L`
- `/analyse ASML.AS`
- `/analyse 7974.T`
- `/analyse 4063.T`
