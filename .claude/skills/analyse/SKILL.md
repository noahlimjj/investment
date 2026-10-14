---
name: analyse
description: Value-investing analysis of a stock, ETF or other listed security using Buffett and Peter Lynch principles, run as a three-agent pipeline (value-researcher → value-quant → value-skeptic). Use whenever the user asks to analyse/analyze, value, evaluate, review, deep-dive or re-check a ticker or company, or asks whether to buy, hold, add to, trim or sell one, even if they don't say "analyse".
argument-hint: "[TICKER ...] [optional focus]"
---

# Value Investing Orchestrator

Every analysis request runs **all three agents, in order**, for each ticker. No single-agent
shortcut and no answering from memory, even for "quick" questions. If the user wants
something lighter, say the pipeline is the standard and offer to stop after the Researcher.

Request: $ARGUMENTS

## 0. Set up (you, the orchestrator)
1. Resolve each ticker to its exchange symbol: `.L`, `.PA`, `.T`, `.KS`, and so on. If it is
   ambiguous (e.g. `JD` vs `JD.`), ask.
2. `DATE=$(date +%F)`, `RUN_DIR=reports/runs/<TICKER>_<DATE>/`. If a **verified** run from the
   last 14 days exists (`python3 methodologies/pipeline_store.py <TICKER>`), tell the user and ask
   whether to reuse its dossier or re-run from scratch. A run that fails verification doesn't count.
   To re-run from scratch in an existing RUN_DIR, first run
   `python3 methodologies/provenance.py supersede RUN_DIR`; otherwise the agents resume from the
   finished files and do nothing. In a non-interactive run (`claude -p`, e.g. from the Telegram bot)
   don't ask anything: follow the instructions in the prompt.
3. Refresh the data layer, then write the shared inputs. Run these **sequentially, before
   launching any agent**:
   `python3 methodologies/fundamentals.py <TICKERS...>`, then for each ticker
   `python3 methodologies/run_inputs.py <TICKER> RUN_DIR`. This writes `00_inputs.json` (the
   sourced 10y yields and FX every agent must use).
4. Check whether it's a current holding (`data/portfolio.json`, also summarised in
   `.agents/rules/active_portfolio.md`, and the investor-profile memory). That decides
   HOLD/TRIM/SELL vs BUY/ACCUMULATE/PASS.
5. `python3 methodologies/provenance.py quarantine RUN_DIR`. It moves stage files that no pipeline
   agent wrote into `RUN_DIR/_external_unverified/`. Run it here, at the start, and never mid-run:
   a checkpoint from an agent that was cut off in this session has no record yet.

## 1. Run the pipeline, sequentially per ticker
Every subagent starts with **no conversation history**, so each delegation prompt must contain
`TICKER`, `RUN_DIR`, today's date, the routing/holding status, and any user focus. Write the run
folder as a line `RUN_DIR: reports/runs/<TICKER>_<DATE>/`, exactly like that. When the agent
finishes, the provenance hook reads that line to find the files to record; without it the stage
can't be verified and the run fails lint.

1. **`value-researcher`**: writes `01_research.md` + `facts.json`.
   **Gate:** if it reports a blocking issue (fundamentals `errors`, an unresolved currency
   ambiguity, no usable financials), stop and tell the user. Don't run the Quant on bad data.
2. **`value-quant`**: writes `02_quant.md` + `02_model.py` (executed).
   **Gate:** `02_model.py` must exist and must run. Check with `python3 RUN_DIR/02_model.py`.
3. **`value-skeptic`**: writes `03_skeptic.md` (+ `03_rerun.py` if it corrected inputs).

If the `value-*` agent types aren't registered (they load at session start, so a session
that predates the files won't have them), run each stage as `general-purpose` with the same
`model` as the definition file. Have it read `.claude/agents/<name>.md` first and treat
everything below the frontmatter as its instructions, including the tool limits (e.g. no web
access for the Quant).

**Mid-run corrections.** If you find a data-layer bug or a wrong input between stages (it
happened 4 times in the pilot), append it to `RUN_DIR/00_orchestrator_notes.md` and tell the
next stage to read that file. Fix the tool too, and re-fetch other tickers it affects.

**Gate every hand-off:** read the agent's summary and check that its load-bearing numbers
don't conflict with `00_inputs.json` or the data layer before you launch the next stage.

**Dependencies:** when one ticker is mostly another one (a holdco and its listed subsidiary,
e.g. SK Square → SK hynix), finish the underlying ticker's Skeptic first. The holdco's Quant
then uses that value, not a fresh one, and its Skeptic addresses whether owning both is redundant.

**Batch size:** keep at most **4–5 tickers' chains in flight**. In the pilot, 14 parallel
Researchers hit the plan's session limit together and all 14 died mid-task. If an agent fails
on a usage limit, relaunch it once the limit resets, telling it to resume from whatever is
already in `RUN_DIR`. Don't redo finished stages.

For several tickers, run the separate tickers' chains in parallel (e.g. all Researchers at
once), but within a ticker the stages always run in order. Relay each stage's short summary
to the user as it lands.

## 2. Synthesize: `RUN_DIR/<TICKER>_report.md`
Write the final report yourself from the three files. Before using them, run
`python3 methodologies/provenance.py verify RUN_DIR`: every stage file must show as verified (its
hash matches what its subagent wrote). A typed `<!-- pipeline:value-... -->` header alone proves
nothing. If a stage fails, re-run that stage's agent; never write, copy or restore a stage file
yourself (AGENTS.md RULE 4). Do not introduce any number that is not
in them. Where the Skeptic corrected the Quant, use the corrected figure and say so. Where they
disagree, show both. Keep it to about 2 pages; the detail stays in the run folder.

```markdown
# Equity Analysis: <TICKER> — <Name>
As of <YYYY-MM-DD> · Price <x.xx CCY> · Template <FULL|rNPV|FUND|SOTP|FULL-bank> · Run: `RUN_DIR`

## 0. Two-Minute Drill (Lynch)
Lynch category · why own it · what has to happen · what could go wrong. 4 sentences, plain English.

## 1. Executive Summary & Expected Value
- **Current Price:** · **12-mo change:**
- **Bear / Base / Bull:** $x (p%) / $x (p%) / $x (p%)
- **Expected Value (probability-weighted):** $x → margin of safety x%
- **SBC-adjusted Expected Value:** $x
- **Price implies (reverse DCF):** x% revenue CAGR for 10 yrs. Plausible? one line
- **Asymmetry (upside to EV : downside to bear):** x : 1
- **Recommendation:** <VERDICT> (<CONVICTION> conviction)

## 2. Business Quality (Buffett)
Moat: <None|Narrow|Wide>, <widening|stable|eroding>, with margin/ROIC evidence ·
Circle of competence / predictability · ROIC vs WACC

## 3. GARP & Valuation Matrix
| Metric | Current | 5-Yr Own Avg | Peer Median |
| :--- | :--- | :--- | :--- |
| EV/EBITDA | | | |
| P/E (ttm / fwd) | | | |
| P/FCF (SBC-adjusted) | | | |
| FCF Yield / Owner-Earnings Yield | | | |
| PEG (or VOID + reason) | | | |
| Lynch ratio (g + yield) / PE | | | |
| ROIC vs WACC | | | |
| Net debt / Owner earnings | | | |
`UNKNOWN` where it couldn't be sourced. Never leave a blank.

## 4. DCF Scenarios
WACC build and terminal growth in one line. Sensitivity range (WACC ±1%, g ±1%).
- **Bear (p%):** $x. Rationale
- **Base (p%):** $x. Rationale
- **Bull (p%):** $x. Rationale

## 5. The Skeptic's Audit
- **Number audit:** n checked, n corrected, effect on fair value
- **Capital Allocation Grade:** <A–F>. Buybacks vs value, \$1 retained-earnings test, M&A record
- **Quality of Earnings:** SBC, accruals, working capital, adjusted-vs-GAAP gap
- **Bear thesis:** the single most likely structural decline path
- **Primary Downside Catalysts:** top 2, each with a signpost to watch
- **Unresolved disagreements (Quant vs Skeptic):** table, or "none"

## 6. Investor Fit (Singapore resident, SGD base)
Listing currency and FX exposure · dividend withholding (30% on US-domiciled dividends) ·
US-situs estate exposure if US-listed (US$60k threshold) · overlap with current holdings ·
already held? at what weight?

## 7. Sources
Numbered. Accession numbers / URLs, carried over from the run files.

VERDICT:        <BUY|ACCUMULATE|HOLD|TRIM|SELL|PASS>
AS_OF:          <YYYY-MM-DD>
PRICE:          <price + ccy>
FAIR_VALUE:     <probability-weighted EV>
UPSIDE:         <%>
ENTRY_BELOW:    <price>
EXIT_ABOVE:     <price>
CONVICTION:     <LOW|MEDIUM|HIGH>
KEY_RISK:       <one line>
DATA_WARNINGS:  <count from data/fundamentals.json for this ticker>
```

## Verdict rules (Buffett margin of safety, Lynch sell discipline)
Use the required margin of safety (MoS) for the business type:
- **20%** for a Wide moat with predictable earnings
- **30%** for a Narrow moat
- **40%** for no moat, Cyclical, Turnaround, or rNPV

When the labels conflict (e.g. a Wide moat but Cyclical), **the higher MoS wins**. Buffett's
margin of safety exists for the case where you're wrong about predictability.

Then, with EV = probability-weighted fair value:

| Condition | Not held | Held |
|---|---|---|
| price ≤ EV × (1 − MoS) and capital allocation ≥ C | BUY | BUY (add) |
| EV × (1 − MoS) < price ≤ EV | ACCUMULATE if moat ≥ Narrow, else PASS | ACCUMULATE / HOLD |
| EV < price ≤ EV × 1.3 | PASS | HOLD |
| price > EV × 1.3, or the bear thesis is already showing in the numbers | PASS | TRIM |
| thesis broken (capital allocation F, solvency risk, or moat demonstrably gone) | PASS | SELL |
| outside circle of competence ("too hard") | PASS | flag for review |

**FUND template: don't use the table above.** A broad index fund isn't a margin-of-safety
bet; Buffett's own advice to most investors is a low-cost index fund held for decades.
Judge it on:
1. **Cost and structure:** TER, tracking difference, domicile and withholding tax, estate-tax situs.
2. **Its role:** overlap and concentration against the other holdings.
3. **Expected return vs the risk-free rate:** the 10-year return decomposition minus the 10-year
   government yield gives the implied equity risk premium. Report it, and say plainly when it's thin.

Verdicts:
- **HOLD/BUY:** the core holding while cost and structure are best-in-class.
- **TRIM:** reserved for a better-structured substitute or an allocation decision, never for
  "the index looks expensive" alone.
- **SELL:** only for a structural defect.

FAIR_VALUE is the base-case 10-year net annualised return (e.g. `6.3%/yr`). ENTRY_BELOW and
EXIT_ABOVE are `n/a`.

ENTRY_BELOW = EV × (1 − MoS). EXIT_ABOVE = EV × 1.3. CONVICTION drops a level for each of:
more than 2 corrected load-bearing inputs, a terminal-value share above 75%, an unresolved
Quant/Skeptic disagreement worth more than 15% of fair value, or stale or non-primary financials.

## 3. Verify, record, report
1. `python3 methodologies/report_lint.py RUN_DIR/<TICKER>_report.md`. Fix every ERROR. A
   report that fails lint is not finished. Lint also checks stage-file provenance and the verdict
   block's arithmetic: one currency throughout, UPSIDE = FAIR_VALUE / PRICE − 1, the entry/exit
   rules, and a verdict consistent with the price bands. When it passes inside Claude Code, a hook
   seals the report, and only sealed reports reach the portfolio audit and Telegram. Edit the
   report after that and you must lint it again.
2. Append a row to `reports/prediction_ledger.csv` with python's `csv` module, never through a
   shell string (in double quotes `$5.0B` becomes `.0B`). Columns: as_of,
   ticker, verdict, price_usd, fair_value, upside_pct, entry_below, exit_above, conviction,
   key_risk, data_warnings, review_date (as_of + 3 months), actual_price_at_review, outcome,
   template. Keep the numeric columns numeric. For FUND, fair_value is the expected 10-yr
   annual return as a number (e.g. `6.30`), and upside, entry and exit are left blank.
3. Reply to the user with: the verdict block, the two-minute drill, EV vs price, the bear
   thesis, any Quant/Skeptic disagreement, and a link to the report file. Don't paste the
   whole report.

Don't pitch tickers the user has said they dislike (see memory).
