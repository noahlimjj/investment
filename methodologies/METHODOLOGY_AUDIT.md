# Methodology Audit — Buffett/Lynch Stock Analysis Pipeline

**Date:** 28 August 2026
**Scope:** `.agents/AGENTS.md`, `multi_stock_analyzer.py`, `deep_fetch.py`, `scratch_fetch.py`, `stock_data.json`, `batch_deep.json`, `batch1_deep.json`, 37 reports in `reports/detailed/`, plus both master summaries.

**Verdict: the framework is sound; the implementation is not. The numbers are wrong at the source, and the method has a structural long bias. Do not act on the existing 37 reports.**

The single most important finding: **Owner Earnings — Buffett's central metric, and the one the prompt explicitly demands be calculated "with real numbers, not EBITDA as a proxy" — is silently wrong for every stock in the file, by 17–29x, with sign flips.**

---

## PART A — Is the trading method itself any good?

The Buffett-moat + Lynch-GARP combination is a legitimate framework. Six things about *how it is being applied* make it unreliable.

### A1. PEG is load-bearing, and PEG is the most fragile ratio in finance

PEG is the primary valuation gate in Part 5 and the organising principle of the entire Master Report ("PEG < 1.0" = buy, "PEG > 1.5" = hold, "PEG > 3" = terrifying). PEG breaks in precisely the situations this portfolio contains.

**The clearest failure is NVO.** The source data says:

| NVO field | Value |
|---|---|
| Price | $51.58 |
| Trailing P/E | 12.34 |
| Forward P/E | 15.83 |
| PEG | 3.36 |

Forward P/E **above** trailing P/E means earnings are *falling*. This is a stock that has de-rated massively and now trades at 12x trailing earnings. The report calls it:

> *"**Extremely Expensive**. A PEG over 3.0 indicates that the market has extrapolated current hyper-growth far into the future... Margin of Safety: Zero mathematically."*

That is exactly backwards. The PEG is 3.36 because the growth denominator collapsed toward zero, **not** because the price is high. The method cannot distinguish "expensive because price is high" from "high ratio because earnings are shrinking" — and those demand opposite actions. Here it flagged a possible deep-value or value-trap situation as a momentum bubble, and did no cash-flow work to tell which.

The same mechanical failure recurs: PRAX has `PEG: null` → Part 5 reports "N/A" and the framework simply goes quiet on a $8.1B position.

**PEG should be a screening hint, never a verdict driver.**

### A2. Sell-side price targets are being used as intrinsic value

**29 of 37 reports** anchor valuation on `targetMeanPrice`. From MSFT.md:

> *"Target Mean Price: Analysts project $555.76 vs current price of $390.54, implying ~42% upside."* → **"STRONG BUY... Sizing should reflect maximum conviction."**

This is circular: it launders consensus as independent analysis, and it is the specific thing Buffett and Lynch both reject. It is also **structurally bullish** — sell-side mean targets sit above spot essentially always, so the pipeline has a permanent long bias baked into its valuation step.

Worse, `Analyst Rating` (`"strong_buy"`, `"buy"`) is fed directly into the model's context. You are anchoring the analyst on the answer before it reasons.

### A3. The required DCF is almost never done

Part 5 mandates an intrinsic-value cross-check with a stated discount rate and terminal growth. **Only 5 of 37 reports mention a discount rate, WACC, or terminal value at all.** Valuation therefore collapses to PEG + analyst target — two numbers, both flawed, both from the same vendor feed.

### A4. One framework is being applied to incompatible asset classes

The 27-name universe contains an S&P 500 ETF (VOO), an international ETF (VXUS), a conglomerate (BRK-B), three pre-revenue biotechs (PRAX, ACAD, INSM), a Japanese publisher, a French luxury house, and Chinese e-commerce. "Lynch category → moat → PEG → owner earnings" is meaningless for an index fund and for pre-revenue biotech.

The reports concede this rather than solving it — PRAX is dismissed as *"Uninvestable (Buffett/GARP)"*, and the Master Report bins ACAD/INSM/PRAX as *"Leave to specialized hedge funds."* That means **4–6 of 27 positions receive no analysis at all**, only a category rejection. Compare the RVMD work in this repo: clinical-stage names need rNPV/scenario analysis, which is a different tool, not a harder application of the same one.

### A5. There is no portfolio layer

27 standalone verdicts, no view on: overlap (MSFT is held directly *and* inside VOO *and* inside BRK-B), sector concentration (ABT + MDT + SYK + ZBH are all medtech), correlation, position sizing, or currency exposure. The "aggregator" agent only reads the finished prose reports — it never sees the underlying data — so it cannot do this even in principle.

### A6. Verdicts are not decisions, and are not comparable

The spec defines three outcomes: **Buy / Watch / Pass**. The 37 reports produced **17 distinct verdict strings**, including `HOLD FOREVER`, `HOLD / DRIP`, `PASS / SELL`, `AVOID / WATCH`, `BUY (Value/Turnaround)`, and `Verdict from NVO analysis: HOLD/WATCH — stock has fallen -12% from thesis price`.

You cannot rank, screen, backtest, or act on that. And "Drip and ignore" / "Hold forever" are not positions with an exit. There is no sell discipline and no price level attached to most verdicts.

**Also missing entirely: any record of what was predicted versus what happened.** Nothing in this repo tracks whether the method works.

---

## PART B — How it got the numbers (the data layer)

This is where the damage is worst, because the errors are silent.

### B1. 🔴 Owner Earnings is wrong for every stock — proven

In `deep_fetch.py`:

```python
net_income = cash_flow.loc["Net Income"].iloc[0] if "Net Income" in cash_flow.index else 0
...
owner_earnings = net_income + depreciation + capex
```

yfinance's cash-flow index typically labels this row **`Net Income From Continuing Operations`**, not `Net Income`. The lookup misses, `net_income` silently becomes **0**, and the output reduces to `D&A − CapEx`.

Verified against the actual file values:

| Ticker | Reported "Owner Earnings" | D&A − CapEx | Match? | True Owner Earnings | Error |
|---|---|---|---|---|---|
| UNH | $739,000,000 | ~$700,000,000 | ✅ | ~$15.7B | **21x understated** |
| LAD | $64,000,000 | ~$65,000,000 | ✅ | ~$1.07B | **17x understated** |
| RR.L | −$83,000,000 | ~−$100,000,000 | ✅ | ~+$2.4B | **sign flipped** |

Earlier snapshots show the same bug producing absurdities: `TM` Owner Earnings of **−$2,900,829,000,000** (−$2.9 trillion) and `PRAX` at **$84,000**.

**20 of 37 reports cite Owner Earnings.** Every one of those figures is wrong. The PRAX report rationalised its nonsense value rather than rejecting it: *"Owner Earnings: Near zero/negative. Pure cash burn for R&D."*

### B2. 🔴 Bare `except:` blocks hide every failure

`deep_fetch.py` contains two bare `except:` clauses. Any error — a renamed index label, a missing statement, an FX issue — is converted into `"Data unavailable"` or a silently wrong number. Nothing fails loudly. This is why B1 went unnoticed across 37 reports.

### B3. 🔴 No currency normalisation

| Ticker | Price | Market cap | Problem |
|---|---|---|---|
| RR.L | 1529.8 | 126,185,381,888 | Price is in **pence**, market cap in **GBP** — off by 100x |
| 7974.T | 7,994 | 9,216,068,681,728 | Both **JPY**, then compared against USD peers |
| MC.PA, WKL.AS, AERO.SW | — | — | EUR/CHF, same issue |

Six of 27 holdings are non-USD. Nothing in the pipeline converts anything. Any cross-holding comparison, ranking, or "net cash per share" calculation is invalid for those names.

### B4. 🔴 `null` was converted into a positive investment claim

`batch1_deep.json` has Nintendo's `DebtToEquity: None` — **missing**. The Master Report states:

> *"**Nintendo (7974.T)**: ...Zero debt, 15% ROE."*

and lists it as a Pounding-the-Table BUY. Missing data became a stated fact supporting a buy recommendation. (Nintendo does happen to be roughly net-cash — which makes this *worse*, not better: the pipeline got a defensible answer by accident, so the failure mode stays invisible.)

### B5. 🟠 Unit inconsistency in ROE across snapshots

Same field, same ticker, three magnitudes:

| File | RR.L ROE |
|---|---|
| `stock_data.json` | 6.23504 |
| `batch_deep.json` | 1.14485 |
| implied in report | "623%" |

The RR.L report had to hand-patch this in prose: *"reported as 6.23 in the data due to a severely depressed equity base."* A human caught it once. It will not be caught consistently, and Part 4's mechanical "target 15%+" test misfires on any name where equity is small, negative, or restated.

### B6. 🟠 Institutional ownership >100% reported as fact

`LAD: 1.16492`, `PRAX: 1.17553`. The PRAX report renders this as *"Institutional Ownership: >100% (High hedge fund and algorithmic trading involvement)"* — an invented explanation for what is a data artifact, presented as insight.

### B7. 🟠 `heldPercentInsiders` is being misread as insider *trading activity*

The prompt asks for *"Insider buying/selling activity in the last 6-12 months — pull actual data, don't estimate."* The tool provides no transaction data at all. What it provides is `heldPercentInsiders` — a static ownership stock. The reports treat it as flow:

- MSFT: *"Insider Activity: Minimal insider buying (0.00079%)"*
- NVO: *"Insider Activity: Minimal (0.005%)"*
- PRAX: *"Insider Activity: Minimal (0.002%)"*

Three reports, same category error. The prompt asked a question the tool cannot answer, so the model answered it with the nearest-looking number.

### B8. 🟠 Snapshots are undated and mutually contradictory

| Ticker | `stock_data.json` | `batch_deep.json` |
|---|---|---|
| LAD price | $427.48 | $371.04 |
| LAD trailing P/E | 14.92 | — |
| LAD forward P/E | 10.49 | 8.79 |
| RR.L price | 1380.0 | 1529.8 |

Same tickers, ~13% and ~11% price gaps, **no timestamps in either file**, and nothing indicating which is current. **26 of 37 reports carry no date stamp at all**, so a stale report is indistinguishable from a fresh one. (This is how `MSFT.md` sat in the repo priced at $390.54 while the stock traded at $497.)

### B9. 🟠 The same run produced contradictory numbers for the same stock

| Source | MSFT ROE | MSFT PEG |
|---|---|---|
| `reports/detailed/MSFT.md` | 34.01% | 1.21 |
| `reports/Master_Portfolio_Report.md` | 38% | 1.13 |

The aggregator re-derived figures from prose instead of reading the data file. There is no single source of truth.

### B10. 🟠 Ticker collisions and universe drift in the April summary

`portfolio_master_summary_april2026.md` scores 19 rows, of which 7 are not in the 27-name universe (`ADBE`, `KSPI`, `PINS`, `PDD`, plus `MC`/`AERO`/`7974` written without exchange suffixes). It also lists **`JD` (JD.com, NASDAQ, $28.29) and `JD.` (JD Sports Fashion, LSE, £70.47) as separate rows** — two entirely different companies distinguished only by a trailing period.

---

## PART C — The root cause

Everything above is downstream of one design flaw.

**`AGENTS.md` demands roughly 25 distinct data items. `get_stock_data` returns 12 yfinance fields and 3 news headlines. There is no web search, no filings access, no peer data, no insider transactions, no earnings-call transcripts, no clinical trial data.**

And the prompt opens with:

> *"Research current data before answering — don't rely on memorized figures."*

while providing **no research tool**. The model is instructed to do something it has been given no means to do. It has exactly two ways to comply: fabricate, or fall back on pretrained memory. It does both.

**The proof is the NVO report.** The data in front of the model said $51.58 and a 12.3x trailing P/E — a badly de-rated stock. The report describes *"the explosion of GLP-1 drugs,"* *"an absolute Fast Grower, posting massive revenue surges,"* and a *"functional duopoly."* That is a 2023–24 narrative, retrieved from training data, never reconciled against the price on the screen. The PRAX report cites **PRAX-114**, an asset discontinued in 2022.

The qualitative prose in these reports is genuinely good — the moat discussions, the Rolls-Royce turnaround narrative, the RAS/GLP-1 context are all well-written. **That is exactly what makes them dangerous.** Fluent, confident narrative wrapped around silently corrupted numbers is harder to catch than obvious garbage.

### C2. The autonomous loop instruction makes it worse

`AGENTS.md` closes with:

> *"When asked to analyze all stocks autonomously without an API key, use the `schedule` tool with a 1-second timer to loop through the portfolio in batches of 3."*

A 1-second scheduled wake-up is a busy-wait hack to work around a missing API key. It guarantees rushed, unverified passes with no state carried between batches — which is why there are 37 reports in 17 verdict formats with no shared numbers.

---

## PART D — What to fix, in priority order

**Stop-the-line (before any further runs):**

1. **Fix Owner Earnings.** Resolve the cash-flow row by trying `Net Income`, `Net Income From Continuing Operations`, and `Net Income Common Stockholders` in order; **raise** if none match. Re-run every report that cites it.
2. **Delete every bare `except:`.** Fail loudly. A missing field must halt the report, not become a silent zero.
3. **Add an assertion layer** that rejects a record before it reaches the model: `null ≠ 0`; ownership percentages must be 0–1; ROE outside ±100% must be flagged not passed through; `|owner_earnings| > 3× market cap` is impossible; currency must be declared.
4. **Normalise currency.** Store `reportedCurrency` and an FX rate on every record; convert to USD for all cross-holding comparison. Store price and market cap in the same unit (the pence/pounds mismatch on RR.L is a 100x error).
5. **Timestamp everything.** `as_of` on every data file and in every report header, with the price and its date. Auto-flag reports older than 30 days.

**Methodology:**

6. **Demote PEG to a hint.** Never let it drive a verdict. Add a hard rule: if forward P/E > trailing P/E (earnings declining) or the growth estimate is <5%, PEG is void — fall back to FCF yield and a DCF.
7. **Remove `targetMeanPrice` and `recommendationKey` from the model's context entirely.** Use them at most as a post-hoc sanity check, never as a valuation input. This alone removes the pipeline's structural long bias.
8. **Make the DCF mandatory and executable** — a script the agent must run with explicit inputs (as with `msft_dcf.py` / `rvmd_dcf.py` in this folder), not prose. If a DCF cannot be built, the report says so rather than substituting a broker target.
9. **Route by asset class.** ETFs, pre-revenue biotech, and financials/conglomerates each need their own template. Do not run GARP over VOO.
10. **Enforce a closed verdict vocabulary** — exactly `BUY / ACCUMULATE / HOLD / TRIM / SELL / PASS` — plus a required numeric fair value, an entry price, and an exit price. Reject any report that deviates.

**Structural:**

11. **Give the agent a real research tool** (web search + filings) or delete the "research current data" instruction. The current combination is the root cause and cannot be prompted around.
12. **Add a verification pass.** A second agent that sees only the raw data and the finished report, and whose sole job is to check every number in the report against the source and flag unsupported claims.
13. **Kill the 1-second scheduler loop.** Run batches deliberately, with state carried across them.
14. **Start a prediction ledger** — ticker, date, verdict, fair value, actual forward return. Without it there is no way to know whether any of this works.

---

## Bottom line

The framework is fine. The prose is good. **The arithmetic underneath it is broken in ways that are invisible in the output**, and the valuation step is anchored to sell-side consensus, which biases every verdict long.

The correct action is to treat the existing 37 reports as **narrative drafts with unverified numbers** — useful for their qualitative moat and competitive discussion, unusable for any buy/sell decision — and to re-run only after items 1–5 are fixed.
