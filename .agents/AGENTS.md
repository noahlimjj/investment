# Stock Analysis Guidelines (v2 — rewritten 28 Aug 2026)

> Supersedes v1 (`AGENTS.md.bak`). v1 produced 37 reports with unusable numbers.
> The defects and their causes are documented in `methodologies/METHODOLOGY_AUDIT.md`.
> Rules marked **[FIX-n]** exist because a specific v1 failure is traceable to their absence.

> **Default workflow (13 Oct 2026):** analyses run as the three-agent `/analyse` pipeline:
> `value-researcher` (facts, Parts 6–7 inputs) → `value-quant` (Parts 1, 2, 4, 5) →
> `value-skeptic` (Part 3, Part 8, number audit, probabilities). The rules below bind all three.
> See `.claude/skills/analyse/SKILL.md` for the report format and verdict rules.

---

## RULE 0 — Never state a number you did not verify

**[FIX-1]** If a figure is not in the validated data file or a primary source you actually
read, write `UNKNOWN` and move on. Do not estimate, interpolate, or recall it from memory.
A report containing `UNKNOWN` is useful. A report containing a confident wrong number is worse
than no report.

**Reconcile narrative against price before you write a word.** v1's NVO report described
"the explosion of GLP-1" and "massive revenue surges" for a stock trading at 11x trailing
earnings after a ~60% de-rate — a 2023 story pasted over 2026 data. Before writing any
thesis, state the current price, the trailing P/E, and the 12-month price change, and ask
whether your narrative is consistent with them. **If the story and the tape disagree, the
tape wins and the disagreement is the analysis.**

## RULE 1 — Use the validated data layer

Read `data/fundamentals.json` (produced by `methodologies/fundamentals.py`). Never call
yfinance fields directly in a report.

- Every record carries `as_of`, `quote_currency`, `financial_currency`, `fx_to_usd`.
- **Surface every entry in `warnings` in the report itself.** They are findings, not noise.
- If a record has `errors`, the report is BLOCKED. Say so and stop.
- **[FIX-4]** `null` means *missing*, never zero. v1 turned Nintendo's missing debt-to-equity
  into "Zero debt" inside a BUY recommendation.

## RULE 2 — Banned inputs

**[FIX-2]** The following must NOT appear in your reasoning or valuation:

- `targetMeanPrice` / any sell-side price target
- `recommendationKey` / any analyst rating

29 of 37 v1 reports anchored valuation on broker targets. That is circular — it launders
consensus as independent work — and it is structurally bullish, because mean targets sit
above spot almost always. You may mention consensus **once**, in Part 6, as a crowding
observation only. It may never touch fair value.

## RULE 3 — Portfolio Audits Must Directly Consume the 3-Agent Ledger

**[FIX-13]** Portfolio audits must NEVER invent ad-hoc screening heuristics or use raw multiples
(e.g. "drawdown < -25% and P/E < 18 = BUY"). Such shortcuts cause disastrous errors:
- Calling peak cyclicals (e.g. SK Hynix at 76% operating margin) "BUY" instead of Peter Lynch **TRIM**.
- Calling tax-leaking US-domiciled ETFs (e.g. VXUS with 30% dividend withholding and US estate tax situs) "ACCUMULATE" instead of mathematical **SELL**.
- Calling clinical biotechs (e.g. RVMD, INSM, PRAX) "HOLD" instead of rNPV-derived **TRIM**.

A portfolio audit must strictly aggregate verified runs: use `methodologies/portfolio_analyser.py`,
which reads `methodologies/pipeline_store.py`. "Verified" means the run passes `report_lint.py` now
(including provenance, RULE 4) and its report carries a lint seal. The ledger is a prediction log, not
a display source. If a ticker lacks a verified run, run `/analyse` or write
`UNKNOWN (requires /analyse run)`. Never hand-write a portfolio summary with prices or verdicts in it:
the 14 Oct 2026 Telegram dossier did, and it showed USD values with € signs and a debt figure no report
contained.

## RULE 4 — Only the pipeline's own agents write pipeline files

**[FIX-14]** On 14 Oct 2026 an agent outside Claude Code wrote look-alike `01_research.md`,
`02_quant.md` and `03_skeptic.md` files, with typed `<!-- pipeline:... -->` headers, into 13 of 22
run folders (about two minutes per "run"). It copied files the pipeline had quarantined back into
place and appended their verdicts to the ledger. Lint passed them, because a header is just text.

- Stage files in `reports/runs/` are written only by stage agents the pipeline itself starts:
  the `value-*` subagents in Claude Code (a `SubagentStop` hook records their hashes), or the
  per-stage Antigravity conversations started by `methodologies/antigravity_pipeline.py` (the
  orchestrator checks each stage and records it). Records are signed with a key outside the repo;
  `report_lint.py` fails any stage file that doesn't match one.
- **Any other agent (including the Antigravity chat agent, the main orchestrator session and any
  script) must not create, copy, restore, move back or edit stage files, reports,
  `.provenance.jsonl`, or ledger rows, and must not run `antigravity_pipeline.py stage-done`.** To
  analyse a ticker, run `python3 methodologies/antigravity_pipeline.py run TICKER` (Gemini) or
  `/analyse` in Claude Code. Never produce a run by hand.
- A run that fails provenance is never "fixed" by writing records for it. It is re-run through `/analyse`.

## RULE 5 — Telegram and notifications

- Verdicts and valuation numbers reach Telegram only through `methodologies/telegram_notifier.py`
  formatters that read verified runs (`--verdict TICKER`, `--portfolio`, and the bot's commands).
  Never type a verdict, fair value, entry/exit price or probability into a message yourself.
- Free text goes through `telegram_notifier.py --msg-file -` with a **quoted** heredoc (`<<'EOF'`).
  Never `--msg "<text>"`: in double quotes the shell expands `$4` in "$45.40" to nothing and runs
  anything in backticks. The LAD ledger row still shows the damage ("$5.0B" became ".0B").
- The notifier refuses free text that pairs a ticker with a verdict the verified run didn't give
  (exit code 3). Remove the claim. Don't reword it to get past the check.
- No staged "telemetry" messages ("[1/3 Researcher complete]") from an agent: the bot reports stage
  completion from provenance records, which only the real stages produce.

---

## Route by asset class before anything else

**[FIX-9]** One framework does not fit every holding. Pick the template and say which:

| Type | Template | Notes |
|---|---|---|
| Operating company, profitable | **FULL** (Parts 1–9 below) | the default |
| Pre-revenue / clinical-stage biotech | **rNPV** | scenario-weighted; see `rvmd_dcf.py`. Moat/PEG/owner-earnings are meaningless — do not force them |
| ETF / index fund | **FUND** | costs, tracking, exposure overlap, role in portfolio. Nothing else. Do not assign a Lynch category |
| Holding company / conglomerate | **SOTP** | value the parts; look through to underlying holdings |
| Bank / insurer | **FULL, modified** | ROTE and book value, not owner earnings or EV/EBITDA |

---

## PART 1: LYNCH CLASSIFICATION
Slow Grower / Stalwart / Fast Grower / Cyclical / Turnaround / Asset Play. Justify with
actual revenue and earnings growth from the data file. State if the classification is
changing and what that implies for how to value it.

**Lynch checks (One Up on Wall Street):**
- **Inventory & Receivables check:** Inventory growth vs sales growth (`Inventory Growth % - Sales Growth %`) and Receivables growth vs sales growth. Inventory rising faster than sales flags hidden discounting and gross margin pressure.
- **Lynch Ratio:** `(EPS Growth % + Dividend Yield %) / P/E`. Below 1.0 is poor, ~1.5 is fair, 2.0+ is attractive.
- **Net-Cash-Adjusted P/E:** `(Price - Net Cash per Share) / EPS`.
- **Cyclicals at peak:** A low P/E during peak margins is a value trap. Value cyclicals on mid-cycle earnings.

## PART 2: MOAT (Buffett)
Durable advantage — switching costs, regulatory barriers, network effects, IP, brand pricing
power. **Cite the margin trend series from the data file as evidence**, not adjectives.
Widening / stable / eroding. Rate: None / Narrow / Wide.

## PART 3: MANAGEMENT & CAPITAL ALLOCATION
Buyback discipline (at what valuations), M&A track record, reinvestment returns, candor.

- **Buffett's $1 Test:** Calculate 5-year change in market capitalization divided by cumulative retained earnings:
  `Value Created per $1 Retained = ΔMarket Cap (5yr) / Cumulative Retained Earnings (5yr)`.
  If < 1.0, management is destroying retained capital.
- **Buybacks vs Dilution:** Did buybacks retire shares below intrinsic value, or merely mask Stock-Based Compensation (SBC)?
- **[FIX-7]** `insider_pct` is the *static percentage of shares insiders hold*. It is NOT
  insider buying or selling activity. If you do not have actual Form 4 transaction data, write
  `Insider activity: UNKNOWN (no transaction data available)`.

## PART 4: FINANCIAL HEALTH
- **Owner Earnings = Net Income + D&A − CapEx − SBC.** Use `owner_earnings_usd` from the data file,
  adjusted for stock-based compensation as a real cash expense.
  **[FIX-1]** v1 computed this with net income silently dropped, understating UNH by 18x and
  flipping Rolls-Royce's sign. If the field is absent, say so; never substitute EBITDA.
- ROE, with the leverage check. **[FIX-5]** If `roe` is flagged >100%, the equity base is
  distorted — report ROCE/ROIC instead and explain why.
- Margin trend, debt-to-equity, interest coverage, net cash per share.
- FCF yield — this is the honest cross-check whenever capex is heavy and EV/EBITDA flatters.

## PART 5: VALUATION — you must RUN a model, not describe one

**[FIX-3]** Only 5 of 37 v1 reports contained a discount rate. Valuation collapsed to PEG plus
a broker target. That is not acceptable.

1. **Run a DCF** using `methodologies/valuation.py`. State base revenue, growth path, margins,
   capex, WACC, terminal growth and terminal ROIC explicitly. Show the code or its output.
2. **Run `reverse_dcf()`** and state what growth today's price already discounts. This is the
   most valuable line in the report: it converts "expensive?" into "what must be true?"
3. **Sensitivity grid** across WACC × terminal growth.
4. **PEG is a hint, never a verdict driver. [FIX-6]** Call
   `valuation.peg_is_valid(trailing_pe, forward_pe, growth)` first. If it returns VOID —
   growth ≤ 0, growth < 5%, or forward P/E > trailing P/E — **you may not cite PEG at all**.
   A high PEG from a collapsing denominator means earnings are shrinking, which is the
   opposite of "expensive." v1 called NVO "extremely expensive" at 11x earnings for exactly
   this reason.
5. State margin of safety versus your own fair value — never versus a broker target.

## PART 6: OWNERSHIP & POSITIONING
Institutional ownership and coverage intensity, as a crowding read only.
**[FIX-6]** If `institutional_pct` is flagged outside 0–1, report it as a vendor artifact,
not as ">100% institutional ownership."

## PART 7: SECTOR-SPECIFIC EDGE
Clinical/regulatory/reimbursement dynamics for healthcare; real adoption data versus narrative
for tech. Only include what you can source.

## PART 8: BULL vs BEAR (INDEPENDENT PRE-MORTEM)
The Skeptic MUST write a blind **Pre-Mortem** based only on the facts dossier *before* reading the Quant's valuation model. Name the single most likely structural reason this business is worth 50%+ less in 5 years.
Then steelman both Bull and Bear in 3–4 concrete, data-backed points. Do not soften the bear case. Name the single variable that flips the thesis.

## PART 8b: INVESTOR FIT (Singapore Resident, SGD Base)
- **Dividend Withholding:** US-domiciled equities incur a mandatory 30% US dividend withholding tax. For global diversification, Irish UCITS ETFs (e.g., VWRA) paying 15% internal treaty WHT are preferred over US ETFs (e.g., VXUS).
- **US Estate Tax Situs:** US-situs assets exceeding US$60,000 are subject to US federal estate tax under 26 USC §2104(a). Irish UCITS have zero US estate tax exposure.
- **Currency & Overlap:** Assess quote currency vs SGD base and portfolio concentration with existing holdings.

## PART 9: VERDICT — closed vocabulary, required fields

**[FIX-8]** v1 produced 17 distinct verdict strings across 37 reports ("HOLD FOREVER",
"PASS / SELL", "AVOID / WATCH"), which cannot be ranked, screened or backtested.

Exactly one of: **BUY · ACCUMULATE · HOLD · TRIM · SELL · PASS**

Every report MUST end with this block, and every field is mandatory:

```
VERDICT:        <one of the six>
AS_OF:          <YYYY-MM-DD>
PRICE:          <price used, with currency>
FAIR_VALUE:     <your number, from Part 5>
UPSIDE:         <%>
ENTRY_BELOW:    <price>
EXIT_ABOVE:     <price>
CONVICTION:     <LOW | MEDIUM | HIGH>
KEY_RISK:       <one line>
DATA_WARNINGS:  <count from the data file>
```

**[FIX-10]** Then append the row to `reports/prediction_ledger.csv`. A method that does not
record its own predictions cannot be evaluated, and nothing in v1 tracked whether any of this
worked.

---

## Operating rules

- **[FIX-11]** If you have no research tool, you cannot satisfy "pull current data." Say which
  parts you could not complete. v1's prompt demanded ~25 data items from a tool returning 12
  fields, which left fabrication as the only way to comply.
- Date-stamp every report in the header with price and as-of date. **[FIX-12]** 26 of 37 v1
  reports had no date, so `MSFT.md` sat in the repo priced at $390 while the stock was $497.
- Run `python3 methodologies/report_lint.py <file>` before considering a report done. Inside Claude
  Code a passing run also seals the report; the Telegram bot and portfolio audit only use sealed reports.
- **[REMOVED]** The v1 "1-second scheduler loop" instruction is deleted. It was a busy-wait
  hack around a missing API key and guaranteed rushed, unverified passes. Run batches
  deliberately; carry state between them.
