# Analysis pipeline (v2)

Rebuilt 28 Aug 2026 after the audit in [`METHODOLOGY_AUDIT.md`](METHODOLOGY_AUDIT.md); hardened
14 Oct 2026 after look-alike run files from outside Claude Code reached the ledger and Telegram.
**Do not act on any report in `reports/detailed/` dated before 28 Aug 2026: all 37 fail
`report_lint.py`.**

## Run order

Analyses run as the three-agent `/analyse` skill in Claude Code (see `../CLAUDE.md`). The skill
calls these tools; you rarely need them by hand:

```bash
python3 methodologies/fundamentals.py TICKER               # 1. validated data -> data/fundamentals.json
python3 methodologies/run_inputs.py TICKER RUN_DIR         # 2. shared rates, FX, official close
# 3. value-researcher -> value-quant -> value-skeptic (subagents; hooks record provenance)
python3 methodologies/report_lint.py RUN_DIR/TICKER_report.md   # 4. verification gate
```

Step 4 is not optional. A report that fails lint is not finished.

## Files

| File | Role |
|---|---|
| `fundamentals.py` | Hardened data layer. Correct Owner Earnings, FX normalisation, null preservation, bounds validation, timestamps. |
| `sec_facts.py` | Primary SEC XBRL financials with accession numbers. |
| `run_inputs.py` | One set of rates, FX and the official close per run (`00_inputs.json`), in major currency units. |
| `valuation.py` | `dcf()`, `reverse_dcf()`, `sensitivity()`, `peg_is_valid()`. Part 5 must **run** these. |
| `report_lint.py` | Verification: banned inputs, verdict schema and arithmetic, staleness, DCF evidence, PEG gate, data warnings, stage headers and **provenance**. |
| `provenance.py` | HMAC-signed hashes of each stage file (from Claude hooks or the Gemini orchestrator); `verify`, `quarantine`, `supersede`, `backfill`. |
| `antigravity_pipeline.py` | The pipeline on Gemini in Antigravity: one conversation per stage, checked and recorded by code. |
| `pipeline_store.py` | The latest *verified* verdict per ticker, live price vs the run's bands, ledger audit. The only verdict source for downstream code. |
| `portfolio_analyser.py` | Portfolio audit from verified runs only. |
| `screener.py`, `discover.py` | The screen (Stage 1 of `/discover`). Candidates, never verdicts. |
| `portfolio_ocr.py` | IBKR screenshot → preview → confirmed save to `data/portfolio.json`. |
| `telegram_notifier.py` | Telegram formatting/delivery from verified data, plus the free-text verdict guard. |
| `msft_dcf.py`, `rvmd_dcf.py` | Worked examples: a capex-heavy compounder and a clinical-stage rNPV. |
| `METHODOLOGY_AUDIT.md` | What was broken and why. |
| `../.agents/AGENTS.md` | Binding rules (v2). v1 preserved as `AGENTS.md.bak`. |
| `../reports/prediction_ledger.csv` | Every verdict, with a review date. The only way to learn whether this works. |

## The five defects that mattered (Aug 2026)

1. **Owner Earnings was wrong for every stock.** `cash_flow.loc["Net Income"]` misses — yfinance labels it `Net Income From Continuing Operations` — so net income silently became 0 and the metric collapsed to `D&A − CapEx`. UNH understated 18x ($739M vs $13.55B), LAD 17x, RR.L sign-flipped. Now resolved against a candidate list that **raises** on failure.
2. **Bare `except:`** turned every failure into a plausible-looking number. Removed; errors are typed and block the report.
3. **No currency handling.** RR.L quotes in GBp but reports in GBP (100x); TM quotes USD but reports JPY (159x). Both now normalised, with a USD translation on every record.
4. **`null` read as `0`.** Nintendo's missing debt-to-equity became "Zero debt" inside a BUY thesis. Nulls are preserved and flagged.
5. **Sell-side targets used as intrinsic value** in 29 of 37 reports — circular, and structurally long-biased. `targetMeanPrice` and `recommendationKey` are now withheld from the model entirely.

## What broke in Oct 2026, and the fix

| Defect | Fix |
|---|---|
| An agent outside Claude Code wrote look-alike stage files (with typed headers) into 13 of 22 runs, and lint passed them | `provenance.py` + `SubagentStop` hook; lint checks hashes |
| Telegram portfolio dossier was hard-coded text (fixed prices, € on USD values, invented figures) | `portfolio_analyser.py` + `telegram_notifier.py` build everything from verified runs |
| Screen hits sent to Telegram as "DEPLOY CAPITAL" (ASML.AS, rated PASS by the pipeline the same day) | `discover.py` produces candidates and shows the pipeline verdict |
| Screener: hard-coded theses with frozen numbers; yield and growth scaling wrong for yfinance 1.7 | Factual "why it passed"; corrected scaling |
| OCR read truncated fractional positions as 1,087 and 5,925 shares | Truncation detected, preview and `/confirm` before saving |
| `00_inputs.json` stored LSE closes in pence labelled GBP | Normalised to major units |
| Replies sent as `--msg "<text>"` lost `$`-amounts to shell expansion | `--msg-file -` with a quoted heredoc, plus a verdict guard |

## Known limitations

- yfinance is a single, unaudited vendor. For anything you will actually trade, verify against the 10-K/10-Q.
- `fundamentals.py` has no insider **transaction** data. The prompt requires `UNKNOWN` rather than substituting the ownership percentage.
- FX is spot only; no historical translation for multi-year margin series.
- The lint is regex-based. It catches structural and known-defect failures, not subtle reasoning errors. That is what the human review is for.
- Provenance proves *which agent* wrote a file, not that the agent was right.
