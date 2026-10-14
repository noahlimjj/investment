"""Telegram bridge: the Telegram app's commands, plus free-form chat with the Antigravity agent.

Commands (/analyse, /portfolio, /opportunities, /status, screenshots, /confirm) are handled
exactly as in telegram_app.py: verified pipeline output only, and /analyse runs the real
3-agent pipeline through headless Claude Code. Only free-form chat is forwarded to the
Antigravity IDE conversation (via `agentapi send-message`).
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from telegram_app import HELP, PROJECT_ROOT, TelegramApp, acquire_poller_lock, esc, load_config, COMPANY_ALIASES

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


def find_agentapi(cand: str | None = None) -> Path | None:
    if cand:
        p = Path(cand)
        if p.exists():
            return p
    w = shutil.which("agentapi")
    if w:
        return Path(w)
    home = Path.home()
    candidates = [
        home / ".gemini/antigravity-ide/bin/agentapi",
        home / ".gemini/antigravity-ide/bin/agentapi.bat",
        home / ".gemini/antigravity-cli/bin/agentapi",
        home / ".gemini/antigravity-cli/bin/agentapi.bat",
        home / ".gemini/antigravity/bin/agentapi",
        home / ".gemini/antigravity/bin/agentapi.bat",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def get_latest_conversation() -> str | None:
    ide_dir = Path.home() / ".gemini" / "antigravity-ide"
    activity: dict[str, float] = {}

    brain_dir = ide_dir / "brain"
    if brain_dir.exists():
        for t in brain_dir.glob("*/.system_generated/logs/transcript.jsonl"):
            cid = t.parents[2].name
            try:
                activity[cid] = max(activity.get(cid, 0), t.stat().st_mtime)
            except Exception:
                pass

    conv_dir = ide_dir / "conversations"
    if conv_dir.exists():
        for f in conv_dir.glob("*.db*"):
            cid = f.name.split(".")[0]
            try:
                activity[cid] = max(activity.get(cid, 0), f.stat().st_mtime)
            except Exception:
                pass

    if activity:
        return max(activity, key=activity.get)
    return None


def update_env_conversation_id(new_id: str) -> None:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        text = env_path.read_text(encoding="utf-8")
        if "CONVERSATION_ID=" in text:
            text = re.sub(r"CONVERSATION_ID=.*", f"CONVERSATION_ID={new_id}", text)
        else:
            text += f"\nCONVERSATION_ID={new_id}\n"
        env_path.write_text(text, encoding="utf-8")


class AntigravityBridge(TelegramApp):
    label = "bridge"

    def __init__(self, token, allowed, get):
        super().__init__(token, allowed, get)
        self.conv_id = get("CONVERSATION_ID")
        self.agentapi = find_agentapi(get("ANTIGRAVITY_AGENTAPI"))

    def send_agent_message(self, text: str) -> None:
        """Send message via agentapi, auto-healing stale conversation IDs."""
        if not self.agentapi or not self.agentapi.exists():
            raise RuntimeError("Antigravity agentapi binary not found.")

        if not self.conv_id or self.conv_id in ("latest", "auto"):
            latest = get_latest_conversation()
            if latest:
                self.conv_id = latest
                update_env_conversation_id(latest)
            else:
                raise RuntimeError("No active conversation ID configured or found.")

        cmd = [str(self.agentapi), "send-message", f"--title=Telegram: {text[:30]}",
               self.conv_id, BRIDGE_INSTRUCTION.format(text=text)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            err = (res.stderr or res.stdout or "").strip()
            # If trajectory not found or invalid session, auto-detect the current active conversation
            if "trajectory not found" in err.lower() or "not found" in err.lower():
                latest = get_latest_conversation()
                if latest and latest != self.conv_id:
                    print(f"[{self.label}] auto-updating stale conversation ID {self.conv_id} -> {latest}")
                    self.conv_id = latest
                    update_env_conversation_id(latest)
                    cmd[3] = latest
                    res2 = subprocess.run(cmd, capture_output=True, text=True)
                    if res2.returncode == 0:
                        return
                    err = (res2.stderr or res2.stdout or "").strip()
            raise RuntimeError(err or f"exit status {res.returncode}")

    def handle_free_text(self, chat_id: int, text: str) -> None:
        cleaned = text.strip()
        lower = cleaned.lower()

        # 1. Natural language analyse: e.g. "analyse google", "analyze apple", "analyse TSLA"
        for prefix in ("analyse ", "analyze ", "/analyse ", "/analyze "):
            if lower.startswith(prefix):
                target = cleaned[len(prefix):].strip()
                if target:
                    print(f"[{self.label}] routed natural language query '{text}' -> handle_analyse({target})")
                    self.handle_analyse(chat_id, target)
                    return

        # 2. Check if intent matches known ticker cards
        if self.route_intent(chat_id, text):
            return

        # 3. Relay free-form text to Antigravity IDE agent
        if not (self.agentapi and self.agentapi.exists()):
            self.send(chat_id, "Free-form chat needs the Antigravity agentapi binary. "
                               "Commands still work.\n\n" + HELP, keyboard=True)
            return

        try:
            self.send_agent_message(text)
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
