# Value Investing Analysis Pipeline & Telegram Bot

An automated, disciplined value-investing research and portfolio management pipeline adhering to Warren Buffett and Peter Lynch principles, tailored for a Singapore tax resident (SGD base).

---

## 🏛 Architecture

### 1. The Three-Agent `/analyse` Pipeline
Analyses strictly run across three specialized subagents in sequence to prevent confirmation bias and hallucinatory multiples:
1. **`value-researcher` (Facts & Ground Truth)**: Extracts primary source data, SEC facts, and fundamental metrics without narrative spin. Enforces RULE 0: never state a number not verified in primary source data.
2. **`value-quant` (Valuation & Mechanics)**: Runs discounted cash flow (DCF), reverse DCF (market implied expectations), sensitivity grids, mid-cycle earnings adjustments for cyclicals, and rNPV models for clinical-stage biotechs.
3. **`value-skeptic` (Pre-Mortem & Red Teaming)**: Writes an independent blind pre-mortem identifying structural thesis killers, audits quant figures, evaluates management capital allocation (Buffett $1 test, SBC dilution), and checks Singapore investor fit (30% US dividend withholding tax and US estate tax situs under 26 USC §2104(a)).

### 2. Cryptographic Provenance & Linting
- **Anti-tamper guarantees**: Every stage file (`01_research.md`, `02_quant.md`, `03_skeptic.md`) is HMAC-signed at completion by harness hooks (`methodologies/provenance.py`).
- **Closed vocabulary verdicts**: Exactly one of `BUY · ACCUMULATE · HOLD · TRIM · SELL · PASS`.
- **Lint seal**: Reports must pass `methodologies/report_lint.py` before verdicts can be logged to `reports/prediction_ledger.csv` or displayed by the Telegram bot.

### 3. Telegram Front-End & Bridge
- **`telegram_app.py`**: Standalone bot handling commands (`/analyse`, `/portfolio`, `/opportunities`, `/status`, IBKR screenshots).
- **`telegram_bridge.py`**: Runs the Telegram bot commands while relaying free-form chat to the Antigravity agent.

---

## 🚀 Setup & Installation (Always-On Deployment)

### Prerequisites
- Python 3.10+
- Node.js (v20+ recommended)
- Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)

### 1. Clone the Repository
```bash
git clone https://github.com/noahlimjj/investment.git
cd investment
```

### 2. Install Python Dependencies
```bash
pip install -r <(cat <<'EOF'
yfinance
pandas
numpy
scipy
pytest
pytest-asyncio
EOF
)
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Fill in your credentials:
```env
TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
TELEGRAM_CHAT_ID=<your_telegram_chat_id>
CONVERSATION_ID=<your_antigravity_conversation_id>
PIPELINE_ENGINE=claude
```

### 4. Transfer Provenance Signing Key (Optional but Recommended)
Existing verified runs were signed using an HMAC key stored outside the repository at `~/.config/value-pipeline/provenance.key`. To retain verification of existing run records on a new machine, copy that key file:
```bash
mkdir -p ~/.config/value-pipeline
# Copy provenance.key from the source machine to ~/.config/value-pipeline/provenance.key
chmod 600 ~/.config/value-pipeline/provenance.key
```
*(If no key exists, a new 256-bit key will automatically be generated for new runs).*

---

## ⚙️ Running the Telegram Bridge

Start the bridge process:
```bash
./run_bridge.sh
```
The script automatically cleans up previous pollers on the same token and launches the bot with locking to prevent split updates.

---

## 🧪 Testing & Verification

Run the test suite to verify pipeline guards and invariants:
```bash
pytest
```

Run a manual report lint:
```bash
python3 methodologies/report_lint.py reports/runs/<TICKER_YYYY-MM-DD>/<TICKER>_report.md
```

Verify provenance records:
```bash
python3 methodologies/provenance.py verify reports/runs/<TICKER_YYYY-MM-DD>
```

Generate a live portfolio audit:
```bash
python3 methodologies/portfolio_analyser.py
```
