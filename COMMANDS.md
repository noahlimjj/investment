# Commands

Two engines, built on Buffett and Lynch principles for a Singapore tax resident (SGD base):

1. **`/analyse` (the 3-agent pipeline):** `value-researcher` → `value-quant` → `value-skeptic`.
   The only source of verdicts.
2. **`/discover` (opportunity discovery):** a screen plus three review stages that produce
   *candidates* for `/analyse`. Never verdicts.

A verdict counts only when its run is **verified**: `report_lint.py` passes, every stage file matches
what its subagent wrote (provenance hook), and the report is sealed. Check any ticker with
`python3 methodologies/pipeline_store.py TICKER`.

---

## 0. Telegram

```bash
./run_app.sh       # the bot: fixed commands, verified output only
./run_bridge.sh    # the same commands, plus free-form chat forwarded to the Antigravity agent
```
Start it **from the Antigravity agent** ("run ./run_bridge.sh and leave it running"): `/analyse` runs
on Gemini through Antigravity's local agent API, which only works in a process Antigravity started.
Either script stops any earlier bot for this project first, so it also serves as the restart. Only
chat IDs in `.env` (`TELEGRAM_CHAT_ID`, optionally `TELEGRAM_ALLOWED_CHAT_IDS`) can use the bot.

| Command | What happens |
|---|---|
| `/analyse TICKER` | Verified card (verdict, EV, bands, live price vs bands, key risk, bear thesis) if a verified run from the last 14 days exists. Otherwise it starts the real pipeline through headless Claude Code, posts each stage as its provenance is recorded, and sends the verified card at the end (20–60 min). If the run fails verification, it says so and shows no verdict. |
| `/analyse TICKER fresh` | Re-run even if a recent verified run exists. |
| `/portfolio` | Audit of `data/portfolio.json` holdings from verified runs, with live prices and "re-run advised" flags when the price has crossed a run's bands or moved ≥15%. |
| `/opportunities` | The 4-preset screen. Candidates and their pipeline status only. |
| Send a screenshot | IBKR Positions screenshot → preview of what was read (with a diff and warnings) → `/confirm` saves it, `/cancel` drops it. |
| `/status` | Running and queued jobs, and the pipeline engine. |
| `/selftest` | Starts a tiny test conversation in Antigravity to check the Gemini engine works. |

**Pipeline engine.** Default `PIPELINE_ENGINE=antigravity`: `methodologies/antigravity_pipeline.py`
runs Researcher, Quant, Skeptic and the report as four separate Gemini conversations
(`PIPELINE_GEMINI_MODEL`, default `pro`). Each stage ends with a one-time completion code; the
script then checks the stage (sections, sources, the model runs, no other stage's files touched),
records its provenance, lints and seals the report, and writes the ledger row itself. If Antigravity
asks for approval before terminal commands, allow auto-execution for this workspace or stages will
wait. `PIPELINE_ENGINE=claude` uses `claude -p --permission-mode dontAsk` instead (Claude quota).
Other `.env` settings: `PIPELINE_STAGE_TIMEOUT_MIN` (60), `PIPELINE_TIMEOUT_MIN` (240), `CLAUDE_BIN`,
`PIPELINE_MAX_BUDGET_USD`, `TELEGRAM_APP_BOT_TOKEN` (to run the app on its own bot).

From a script or agent:
```bash
python3 methodologies/telegram_notifier.py --verdict NVO        # verified card
python3 methodologies/telegram_notifier.py --portfolio          # audit
python3 methodologies/telegram_notifier.py --msg-file - <<'EOF'
free text (quoted heredoc: $ and backticks survive)
EOF
```
Free text that pairs a ticker with a verdict the verified run didn't give is refused (exit code 3).

---

## 1. Finding opportunities (`/discover`)

In Claude Code, `/discover` runs Scout → Vetter → Skeptic → Strategist and ends with the
`/analyse` hand-off. The screen on its own (Stage 1):

```bash
python3 methodologies/discover.py --all                     # every preset → reports/discovery/MASTER_OPPORTUNITIES_<DATE>.md (+ .json)
python3 methodologies/discover.py --preset SINGAPORE_INCOME --universe DIVIDEND_NON_US
python3 methodologies/discover.py --preset BUFFETT_MOAT --tickers ASML.AS,NESN.SW,OR.PA,RACE
```

| Preset | Rule (`screener.py` `SCREEN_RULES`) |
|---|---|
| `BUFFETT_MOAT` | return blend (0.6 ROE + 0.4 ROA) ≥ 12%, operating margin ≥ 12%, net debt/EBITDA ≤ 3.5x (financials: ROE ≥ 12%) |
| `LYNCH_GARP` | 0 < forward P/E ≤ 25 and Lynch ratio (EPS growth % + yield %) / P/E ≥ 1.0 |
| `NET_CASH_BARGAIN` | non-financial, net cash ≥ 10% of market cap, forward P/E ≤ 20 |
| `SINGAPORE_INCOME` | non-US domicile, dividend yield ≥ 3%, net debt/EBITDA ≤ 3.5x (financials: ROE ≥ 10%) |

Universes: `DIVIDEND_NON_US` · `EURO_COMPOUNDERS` · `ASIA_COMPOUNDERS` · `FALLEN_STALWARTS` ·
`GLOBAL_QUALITY` · `SP500_DEFENSIVE`. Screen hits the pipeline has already rated are shown with that
verdict, not re-pitched.

---

## 2. Valuing a security (`/analyse TICKER`)

Run it in Claude Code (or from Telegram). The skill does the steps below. You run them by hand
only when debugging.

```bash
python3 methodologies/fundamentals.py TICKER                         # validated data layer
python3 methodologies/run_inputs.py TICKER reports/runs/TICKER_DATE/ # rates, FX, official close
python3 methodologies/provenance.py quarantine reports/runs/TICKER_DATE/
```
1. **Researcher** → `01_research.md`, `facts.json` (sourced facts, no opinions).
2. **Quant** → `02_quant.md`, executed `02_model.py` (DCF scenarios, reverse DCF, sensitivity).
3. **Skeptic** → `03_skeptic.md` (blind pre-mortem, number audit, probabilities, verdict recommendation).
4. **Report** → `TICKER_report.md` with the closed-vocabulary verdict block
   (`BUY · ACCUMULATE · HOLD · TRIM · SELL · PASS`).
5. **Lint** (`report_lint.py`): must pass. Inside Claude Code that also seals the report.
6. **Ledger**: a row in `reports/prediction_ledger.csv`, written with Python's `csv` module.

---

## 3. Verification

```bash
python3 methodologies/report_lint.py reports/runs/*/*_report.md   # lint + provenance, every run
python3 methodologies/provenance.py verify                         # stage-file provenance only
python3 methodologies/pipeline_store.py --ledger                   # which ledger rows are verified
python3 -m unittest discover -s tests                              # guard tests
```

---

## 4. Singapore investor constraints
- **Capital gains tax:** 0%.
- **US dividend withholding:** 30% on US-domiciled distributions, with no Singapore credit.
- **US estate tax:** US-situs assets above US$60,000 are exposed (26 USC §2104(a)). Shares of
  non-US companies on their home exchanges, and Irish UCITS funds, are not. ADRs are unsettled.
- **ADRs:** prefer the primary listing (e.g. `BATS.L` over `BTI`) to avoid depositary fees.
