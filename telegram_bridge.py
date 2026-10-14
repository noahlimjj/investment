"""Telegram bridge: the Telegram app's commands, plus free-form chat with the Antigravity agent.

Commands (/analyse, /portfolio, /opportunities, /status, screenshots, /confirm) are handled
exactly as in telegram_app.py: verified pipeline output only, and /analyse runs the real
3-agent pipeline through headless Claude Code. Only free-form chat is forwarded to the
Antigravity IDE conversation (via `agentapi send-message`).

Why the split (14 Oct 2026): this bridge used to forward everything to Antigravity, which runs
outside Claude Code and cannot start the value-researcher / value-quant / value-skeptic
subagents. Asked to "enforce the 3-agent pipeline" and to stream "[1/3 Researcher Complete]"
telemetry, it wrote look-alike run folders in about two minutes each (13 of 22 runs), restored
files the pipeline had quarantined, and logged their verdicts to the ledger. Its replies were
sent as `telegram_notifier.py --msg "<text>"`, where the shell turned "$45.40" into "5.40".
Analysis and buy/sell questions about known tickers are now answered from verified runs before
anything reaches Antigravity, and the instructions it receives forbid writing pipeline files.

Run: ./run_bridge.sh. Needs TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID and CONVERSATION_ID in .env.
Don't run it at the same time as telegram_app.py on the same token (the second one exits).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from telegram_app import HELP, TelegramApp, acquire_poller_lock, esc, load_config

BRIDGE_INSTRUCTION = """[TELEGRAM MESSAGE from the authorised user, via telegram_bridge.py]
{text}

Binding rules for your reply (.agents/AGENTS.md RULE 4 and 5):
1. You run outside Claude Code and cannot run the 3-agent pipeline. Don't create, copy, restore or
   edit anything under reports/runs/, reports/prediction_ledger*.csv, data/portfolio.json,
   .agents/rules/active_portfolio.md, or any .provenance.jsonl file.
2. Don't state a verdict, fair value, entry/exit price or scenario probability yourself. For
   verified figures on a ticker, run:  python3 methodologies/telegram_notifier.py --verdict TICKER
   (it sends the verified card itself, or explains why there is none).
3. If the user wants an analysis or a buy/hold/sell decision, tell them to send
   /analyse TICKER in Telegram. The bot runs the real pipeline (one Antigravity conversation per
   stage, started by code) and reports back. Never run `antigravity_pipeline.py stage-done` yourself.
4. Send your reply with a quoted heredoc, so the shell can't touch $ amounts or backticks:
     python3 methodologies/telegram_notifier.py --msg-file - <<'EOF'
     <your reply, Telegram HTML>
     EOF
   Never use --msg "<text>". If the notifier refuses the message (exit code 3), it stated a
   verdict the verified pipeline didn't make: remove the claim, don't rephrase around it.
"""


class AntigravityBridge(TelegramApp):
    label = "bridge"

    def __init__(self, token, allowed, get):
        super().__init__(token, allowed, get)
        self.conv_id = get("CONVERSATION_ID")
        self.agentapi = Path(get("ANTIGRAVITY_AGENTAPI") or Path.home() / ".gemini/antigravity-ide/bin/agentapi")

    def handle_free_text(self, chat_id: int, text: str) -> None:
        if self.route_intent(chat_id, text):
            return
        if not (self.conv_id and self.agentapi.exists()):
            self.send(chat_id, "Free-form chat needs CONVERSATION_ID in .env and the Antigravity agentapi "
                               "binary. Commands still work.\n\n" + HELP, keyboard=True)
            return
        try:
            subprocess.run([str(self.agentapi), "send-message", f"--title=Telegram: {text[:30]}",
                            self.conv_id, BRIDGE_INSTRUCTION.format(text=text)],
                           capture_output=True, text=True, check=True, timeout=60)
        except Exception as exc:
            self.send(chat_id, f"❌ Couldn't reach the Antigravity agent: {esc(exc)}")
            return
        self.send(chat_id, "💬 Sent to the Antigravity agent (free-form chat). It can't issue verdicts. "
                           "For those use <code>/analyse TICKER</code> or <code>/portfolio</code>.")


def main() -> None:
    cfg = load_config(("TELEGRAM_BOT_TOKEN",))
    if not cfg["token"]:
        sys.exit("Set TELEGRAM_BOT_TOKEN in .env.")
    _lock = acquire_poller_lock(cfg["token"])  # held for the process lifetime
    AntigravityBridge(cfg["token"], cfg["allowed"], cfg["get"]).run()


if __name__ == "__main__":
    main()
