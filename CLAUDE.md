# Investment research workspace

## Stock analysis: always the three-agent pipeline
Any request to analyse, value, review, or decide on buying/holding/selling a security runs the
`analyse` skill (`.claude/skills/analyse/SKILL.md`). The skill runs
`value-researcher` → `value-quant` → `value-skeptic` (`.claude/agents/`), then synthesises the
report, lints it, and logs it to `reports/prediction_ledger.csv`. Don't answer these requests
from memory or with a single agent.

## Only verified runs count
A run is verified when `report_lint.py` passes it now and a Claude Code session has sealed the
report. Lint includes provenance: each stage file must match the hash its subagent's
`SubagentStop` hook recorded (`methodologies/provenance.py`, hooks in `.claude/settings.json`).
`methodologies/pipeline_store.py` is the only place downstream code (portfolio audit, Telegram)
reads verdicts from, and a run that fails is shown as unverified, never as a verdict.

On 14 Oct 2026 an agent outside Claude Code had written look-alike stage files (typed headers
included) into 13 of 22 run folders. Never create, copy, restore or edit stage files, reports,
`.provenance.jsonl` or ledger rows by hand. A run that fails provenance is re-run, not patched
(`.agents/AGENTS.md` RULE 4).

## Binding rules
`.agents/AGENTS.md` (v2): never state an unverified number, use the validated data layer,
no sell-side price targets or ratings, route by asset class, the closed verdict vocabulary,
provenance (RULE 4) and Telegram delivery (RULE 5).
`methodologies/METHODOLOGY_AUDIT.md` explains why each rule exists.

## Privacy (applies to every agent)
Never put the user's name, email, or other personal details in a web request, a header, or a
URL. For SEC EDGAR, use the generic contact string `value-research-script research@example.com`,
or `$SEC_USER_AGENT` if it's set. A pilot Skeptic sent the user's email once; this rule exists
because of that.

## Tools
- `methodologies/fundamentals.py`: validated yfinance snapshot → `data/fundamentals.json`
- `methodologies/sec_facts.py`: primary SEC XBRL financials with accession numbers (US + 20-F filers)
- `methodologies/valuation.py`: `dcf`, `reverse_dcf`, `sensitivity`, `peg_is_valid`
- `methodologies/report_lint.py`: verification gate for every report (incl. provenance and verdict arithmetic)
- `methodologies/provenance.py`: `verify`, `quarantine`, `supersede` for run folders
- `methodologies/pipeline_store.py`: latest verified verdict per ticker; `--ledger` audits the ledger
- `methodologies/portfolio_analyser.py`: portfolio audit from verified runs only
- `methodologies/discover.py` / `screener.py`: the screen (Stage 1 of `/discover`): candidates, never verdicts

Run outputs live in `reports/runs/<TICKER>_<YYYY-MM-DD>/`. Reports in `reports/detailed/`
dated before 28 Aug 2026 fail lint and are not to be acted on. `legacy/` holds retired v1
scripts that bypass the pipeline; don't run them.

## Telegram
`telegram_app.py` (or `telegram_bridge.py`, the same commands plus free-form chat with the
Antigravity agent) serves only verified output. `/analyse TICKER` runs the pipeline when no
verified run from the last 14 days exists: by default on Gemini in Antigravity
(`methodologies/antigravity_pipeline.py`, one conversation per stage, checked and recorded by
code; the bot must be started by the Antigravity agent), or with `PIPELINE_ENGINE=claude` through
headless Claude Code. Agents send free text with `telegram_notifier.py --msg-file -` and a quoted
heredoc, never `--msg "..."`.
