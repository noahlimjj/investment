---
name: discover
description: Find new investment candidates using Buffett and Peter Lynch screens, tailored for a Singapore tax resident. Runs as a four-stage pipeline (opportunity-scout → opportunity-vetter → opportunity-skeptic → allocation-strategist) that screens global universes, finds out why each candidate is cheap, red-teams the survivors, checks Singapore tax/situs fit and portfolio overlap, and hands the best one or two to /analyse. Produces candidates, never verdicts.
argument-hint: "[preset: BUFFETT_MOAT | LYNCH_GARP | NET_CASH_BARGAIN | SINGAPORE_INCOME | all] [universe | custom tickers]"
---

# Opportunity discovery (/discover)

Use it when the user asks for new ideas: "find me opportunities", "where should new capital go",
"screen for cheap compounders / GARP stocks / non-US dividend payers".

**Discovery produces candidates, never verdicts.** No stage writes BUY, ACCUMULATE, HOLD, TRIM,
SELL, PASS, "deploy capital", "top up" or a price target. The only action it recommends is running
`/analyse` on the top one or two candidates. On 14 Oct 2026 the old programmatic version labelled
ASML.AS "DEPLOY CAPITAL" the same day the pipeline rated it PASS, and that went to Telegram.

Request: $ARGUMENTS

## 0. Set up (you, the orchestrator)
1. Preset and universe from the request; for "all", run every preset (`discover.py --all` maps each
   preset to its universe). The thresholds live in `methodologies/screener.py` (`SCREEN_RULES`);
   quote them from there:

   | Preset | Rule |
   |---|---|
   | BUFFETT_MOAT | return blend (0.6 ROE + 0.4 ROA) ≥ 12%, operating margin ≥ 12%, net debt/EBITDA ≤ 3.5x (financials: ROE ≥ 12%) |
   | LYNCH_GARP | 0 < forward P/E ≤ 25 and Lynch ratio (EPS growth % + yield %) / P/E ≥ 1.0 |
   | NET_CASH_BARGAIN | non-financial, net cash ≥ 10% of market cap, forward P/E ≤ 20 |
   | SINGAPORE_INCOME | non-US domicile, dividend yield ≥ 3%, net debt/EBITDA ≤ 3.5x (financials: ROE ≥ 10%) |

   The "return blend" is not ROIC; call it what it is.
2. `DATE=$(date +%F)`, `RUN_DIR=reports/discovery/run_<DATE>_<PRESET>/`.
3. Holdings come from `data/portfolio.json`. Count them; don't assume a number.

Every subagent starts with no history, so each delegation prompt carries `PRESET`, the line
`RUN_DIR: reports/discovery/run_<DATE>_<PRESET>/`, `DATE`, the holdings list, and any user focus.

## 1. Scout (`opportunity-scout`) → `01_scout_report.md`
Runs `python3 methodologies/discover.py --preset <PRESET> --universe <UNIVERSE>` (or `--tickers`).
That writes `screened.json` and a factual `01_scout_report.md`, cross-references each candidate with
the verified pipeline, and moves any older Stage 2–4 files into `_superseded/`. The Scout then checks
the shortlist for vendor-data artifacts.
**Gate:** fewer than 2 new candidates → tell the user. Don't loosen thresholds without asking.

## 2. Vetter (`opportunity-vetter`) → `02_vetted_theses.md`
Why is it cheap (temporary vs structural)? Is the moat visible in five years of margins and
returns? Capital allocation and the debt wall. Each candidate is ADVANCED or DISQUALIFIED with a
sourced reason.

## 3. Skeptic (`opportunity-skeptic`) → `03_skeptic_critique.md`
Red-teams what the Vetter advanced: value-trap tests, red flags, a pre-mortem, one falsification
metric, and a severity rating per candidate.

## 4. Strategist (`allocation-strategist`) → `04_allocation_recommendation.md`
Singapore tax and estate-situs fit, overlap with current holdings, ranking, and the hand-off: the
top one or two candidates for `/analyse`.

## Rules for every stage
- `.agents/AGENTS.md` RULE 0–2 bind: every number has a source and a date, or it's `UNKNOWN`. No
  sell-side targets or ratings.
- First line of each stage file: `<!-- pipeline:<agent-name> -->`. A file at that path without it
  came from outside the pipeline: move it to `RUN_DIR/_external_unverified/` and start fresh.
- Before ranking anything, check `python3 methodologies/pipeline_store.py <TICKER>`. A VERIFIED
  pipeline verdict outranks anything discovery thinks: a candidate the pipeline rated PASS stays
  PASS until a new `/analyse` run says otherwise. Runs that fail verification don't count.
- Gate each hand-off: read the stage's summary, and stop if it reports data artifacts that make the
  shortlist meaningless.

## 5. Reply to the user
The ranked candidates, each with: the one-line reason it survived, the Skeptic's main hazard and
falsification metric, the tax fit, and its pipeline status. End with the suggested
`/analyse TICKER` for the top one or two. No verdict words. Link `04_allocation_recommendation.md`.
