# Retired scripts: do not run

These are v1 tools (Jul–Aug 2026) and an unused Gemini prototype. Each one produces analysis
outside the 3-agent `/analyse` pipeline, so running any of them would bypass it:

| File | What it did | Why it's retired |
|---|---|---|
| `multi_stock_analyzer.py` | single-agent analysis that wrote reports | no Researcher → Quant → Skeptic, no provenance |
| `inject_data.py`, `generate_summary.py` | wrote numbers and summaries straight into `reports/` | hand-assembled reports |
| `deep_fetch.py`, `scratch_fetch.py`, `fetch_batch.py`, `get_csv_data.py`, `update_tickers.py`, `*.json` | ad-hoc yfinance fetches | replaced by `methodologies/fundamentals.py` (see METHODOLOGY_AUDIT.md) |
| `gemini_engine.py` | a "3-agent" Gemini call that asked a model for fair values from a data snapshot | unsourced numbers, no lint, no provenance; never called |

Kept for reference only. Imports and paths inside them are not maintained.
