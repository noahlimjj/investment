"""Telegram front-end for the value-investing pipeline.

Rules this bot enforces (CLAUDE.md, .agents/AGENTS.md RULE 4-5):
  * Every verdict it shows comes from a VERIFIED /analyse run (methodologies/pipeline_store.py:
    lint pass, stage-file provenance, lint seal). Nothing else is ever displayed as a verdict.
  * /analyse runs the real 3-agent pipeline, by default on Gemini in Antigravity
    (methodologies/antigravity_pipeline.py: one conversation per stage, started and checked by
    code), or with PIPELINE_ENGINE=claude through headless Claude Code (`claude -p`). Stage progress
    is read from provenance records written by code, not from agent claims. There is no heuristic
    fallback and no silent switch between engines: if a run fails, the bot says so.
  * Only chat IDs in .env (TELEGRAM_CHAT_ID, TELEGRAM_ALLOWED_CHAT_IDS) may use it. Previously any
    chat that messaged the bot became TELEGRAM_CHAT_ID, redirecting every report to that chat.
  * One poller per bot token. Two processes polling one token split updates between them at random.

Commands
  /analyse TICKER [fresh]   verified card, or start the pipeline (fresh: re-run even if recent)
  /portfolio                audit of current holdings from verified runs + live prices
  /opportunities            screen candidates (not recommendations) with their pipeline status
  /status                   running and queued jobs, and the pipeline engine
  /selftest                 check that the Gemini engine can reach Antigravity
  photo or image file       IBKR screenshot -> preview -> /confirm saves it -> audit
  /confirm  /cancel         accept or drop the pending screenshot preview

Run: ./run_app.sh. Token: TELEGRAM_APP_BOT_TOKEN, else TELEGRAM_BOT_TOKEN, from .env.
"""
from __future__ import annotations

try:
    import fcntl
except ImportError:
    fcntl = None
import glob
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
import traceback
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "methodologies"))
import antigravity_pipeline  # noqa: E402
import pipeline_store  # noqa: E402
import portfolio_analyser  # noqa: E402
import portfolio_ocr  # noqa: E402
import provenance  # noqa: E402
import telegram_notifier as tn  # noqa: E402
from telegram_notifier import esc  # noqa: E402

DATA_DIR = PROJECT_ROOT / "data"
SCREENSHOTS_DIR = DATA_DIR / "screenshots"
JOBS_DIR = DATA_DIR / "telegram_jobs"
TICKER_RE = re.compile(r"^[A-Z0-9][A-Z0-9.\-]{0,14}$")
ANALYSIS_WORDS = re.compile(
    r"\b(analy[sz]e|analysis|valu(e|ation)|deep[- ]?dive|fair value|intrinsic|buy|sell|hold|trim|"
    r"accumulate|add to|should i|worth|undervalued|overvalued|verdict|re-?check|review)\b", re.I)
STAGE_LABEL = {"value-researcher": "1/3 Researcher", "value-quant": "2/3 Quant", "value-skeptic": "3/3 Skeptic"}

COMPANY_ALIASES: dict[str, str] = {
    "google": "GOOGL",
    "goog": "GOOGL",
    "googl": "GOOGL",
    "alphabet": "GOOGL",
    "apple": "AAPL",
    "aapl": "AAPL",
    "microsoft": "MSFT",
    "msft": "MSFT",
    "amazon": "AMZN",
    "amzn": "AMZN",
    "meta": "META",
    "facebook": "META",
    "fb": "META",
    "tesla": "TSLA",
    "tsla": "TSLA",
    "nvidia": "NVDA",
    "nvda": "NVDA",
    "netflix": "NFLX",
    "nflx": "NFLX",
    "tsmc": "TSM",
    "tsm": "TSM",
    "alibaba": "BABA",
    "baba": "BABA",
    "tencent": "0700.HK",
    "samsung": "005930.KS",
    "novo": "NVO",
    "novo nordisk": "NVO",
    "nvo": "NVO",
    "lvmh": "MC.PA",
    "asml": "ASML",
    "berkshire": "BRK-B",
    "berkshire hathaway": "BRK-B",
}

# Headless pipeline. dontAsk denies anything not listed; nothing waits on a prompt.
PIPELINE_TOOLS = ["Skill", "Agent", "Task", "ToolSearch", "TodoWrite", "Read", "Write", "Edit",
                  "Glob", "Grep", "WebSearch", "WebFetch", "Bash"]
PIPELINE_PROMPT = """/analyse {ticker}

This run was started from the Telegram bot and is non-interactive (claude -p). Nobody can answer
questions, so don't ask any:
- Ticker {ticker}, RUN_DIR {run_dir}, today {date}. If the ticker is ambiguous or unknown, stop
  and say so in your final message.
- Run from scratch. The bot starts a run only when there is no verified run from the last 14 days
  or the user asked for a fresh one, and it has already moved any old files out of RUN_DIR.
- Run each stage in the foreground and wait for it. Don't end your turn until the report is
  written, report_lint.py passes, and the ledger row is appended.
- Your final message isn't shown to the user: the bot builds the card from the verified report.
  Keep it to a few lines (verdict, lint result, anything that blocked the run).
"""
BUTTONS = {
    "📊 portfolio audit": "/portfolio", "📊 deep portfolio analysis": "/portfolio",
    "🔍 opportunity screen": "/opportunities", "🔍 find opportunities": "/opportunities",
    "📸 send ibkr screenshot": "/screenshot", "📸 upload ibkr screenshot": "/screenshot",
    "❓ help": "/help", "❓ help & commands": "/help",
}
KEYBOARD = {"keyboard": [[{"text": "📊 Portfolio audit"}, {"text": "🔍 Opportunity screen"}],
                         [{"text": "📸 Send IBKR screenshot"}, {"text": "❓ Help"}]],
            "resize_keyboard": True, "is_persistent": True}
HELP = (
    "📖 <b>Commands</b>\n"
    "• <code>/analyse TICKER</code>: verified pipeline card, or start the 3-agent pipeline "
    "(20–60 min). Add <code>fresh</code> to re-run a recent one.\n"
    "• <code>/portfolio</code>: audit of your holdings from verified runs and live prices.\n"
    "• <code>/opportunities</code>: screen candidates. Not recommendations; each needs /analyse.\n"
    "• <code>/status</code>: running and queued jobs. <code>/selftest</code>: check the Gemini engine.\n"
    "• Send an IBKR screenshot: I show what I read, and /confirm saves it.\n\n"
    "Every verdict I show comes from a run whose three stages were verified as written by the "
    "Researcher, Quant and Skeptic agents. Anything else is reported as unverified."
)


# --------------------------------------------------------------------------- #
# configuration
# --------------------------------------------------------------------------- #
def load_config(token_vars: tuple[str, ...]) -> dict[str, Any]:
    env = tn.load_env()
    get = lambda k: (os.environ.get(k) or env.get(k) or "").strip()  # noqa: E731
    token = next((get(v) for v in token_vars if get(v)), "")
    allowed = {int(x) for x in re.split(r"[,\s]+", get("TELEGRAM_ALLOWED_CHAT_IDS") + " " + get("TELEGRAM_CHAT_ID"))
               if re.fullmatch(r"-?\d+", x)}
    return {"token": token, "allowed": allowed, "get": get}


def find_claude(get: Callable[[str], str]) -> str | None:
    cand = get("CLAUDE_BIN") or shutil.which("claude")
    if not cand:
        found = sorted(glob.glob(str(Path.home() / ".nvm/versions/node/*/bin/claude")))
        cand = found[-1] if found else None
    return cand if cand and Path(cand).exists() else None


def acquire_poller_lock(token: str):
    """One process per bot token, or Telegram hands each update to whichever poller asks first."""
    bot_id = token.split(":")[0]
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fh = open(DATA_DIR / f".telegram_poller_{bot_id}.lock", "a+")
    try:
        if fcntl:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        elif sys.platform == "win32":
            import msvcrt
            msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
    except (BlockingIOError, OSError):
        fh.seek(0)
        sys.exit(f"Another process ({fh.read().strip() or 'unknown'}) is already polling bot {bot_id}. "
                 "Stop it first: two pollers on one token split your messages between them at random.")
    fh.seek(0)
    fh.truncate()
    fh.write(f"{Path(sys.argv[0]).name} pid {os.getpid()}")
    fh.flush()
    return fh


# --------------------------------------------------------------------------- #
# the bot
# --------------------------------------------------------------------------- #
class TelegramApp:
    label = "app"

    def __init__(self, token: str, allowed: set[int], get: Callable[[str], str]):
        self.token, self.allowed, self.get = token, allowed, get
        self.api_url = f"https://api.telegram.org/bot{token}"
        self.file_url = f"https://api.telegram.org/file/bot{token}"
        self.state_file = DATA_DIR / f"telegram_state_{token.split(':')[0]}.json"
        self.offset = self._load_offset()
        self.pending: dict[int, dict] = {}          # chat_id -> OCR preview awaiting /confirm
        self.jobs: dict[str, dict] = {}             # job id -> job
        self.jobs_lock = threading.Lock()
        self.claude = find_claude(get)
        self.engine = (get("PIPELINE_ENGINE") or "antigravity").lower()
        self.queues = {"pipeline": queue.Queue(), "screen": queue.Queue()}
        for q in self.queues.values():
            threading.Thread(target=self._worker, args=(q,), daemon=True).start()
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        JOBS_DIR.mkdir(parents=True, exist_ok=True)

    # ---- transport ----------------------------------------------------------
    def api(self, method: str, payload: dict | None = None, timeout: int = 35) -> dict:
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(f"{self.api_url}/{method}", data=data,
                                     headers={"Content-Type": "application/json"} if data else {})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            try:
                body = json.loads(exc.read().decode())
            except Exception:
                body = {}
            return {"ok": False, "error_code": exc.code, "description": body.get("description", str(exc))}

    def send(self, chat_id: int, text: str, keyboard: bool = False) -> bool:
        return tn.send_telegram_message(text, token=self.token, chat_id=chat_id,
                                        reply_markup=KEYBOARD if keyboard else None)

    def send_doc(self, chat_id: int, path: Path, caption: str = "") -> bool:
        return tn.send_telegram_document(path, caption=caption, token=self.token, chat_id=chat_id)

    def download(self, file_id: str, dest: Path) -> bool:
        info = self.api("getFile", {"file_id": file_id})
        if not info.get("ok"):
            return False
        try:
            with urllib.request.urlopen(f"{self.file_url}/{info['result']['file_path']}", timeout=60) as r:
                dest.write_bytes(r.read())
            return True
        except Exception as exc:
            print(f"[{self.label}] download failed: {exc}")
            return False

    # ---- state ----------------------------------------------------------------
    def _load_offset(self) -> int:
        try:
            return int(json.loads(self.state_file.read_text()).get("offset", 0))
        except (OSError, ValueError, json.JSONDecodeError):
            return 0

    def _save_offset(self) -> None:
        self.state_file.write_text(json.dumps({"offset": self.offset}))

    # ---- threads and jobs -----------------------------------------------------
    def spawn(self, fn: Callable, chat_id: int, *args) -> None:
        threading.Thread(target=self._safe, args=(fn, chat_id, *args), daemon=True).start()

    def _safe(self, fn: Callable, chat_id: int, *args) -> None:
        try:
            fn(chat_id, *args)
        except Exception as exc:
            traceback.print_exc()
            self.send(chat_id, f"❌ {esc(fn.__name__)} failed: {esc(type(exc).__name__)}: {esc(exc)}")

    def enqueue(self, kind: str, chat_id: int, fn: Callable, **job) -> int:
        jid = f"{kind}-{int(time.time() * 1000)}"
        job.update(id=jid, kind=kind, chat_id=chat_id, status="queued",
                   queued=datetime.now().strftime("%H:%M"), fn=fn)
        with self.jobs_lock:
            self.jobs[jid] = job
            ahead = sum(1 for j in self.jobs.values() if j["kind"] == kind and j["status"] in ("queued", "running")) - 1
        self.queues[kind].put(jid)
        return ahead

    def _worker(self, q: queue.Queue) -> None:
        while True:
            jid = q.get()
            job = self.jobs[jid]
            job["status"], job["started"] = "running", time.time()
            try:
                job["fn"](job)
                job["status"] = job.get("status_final", "done")
            except Exception as exc:
                traceback.print_exc()
                job["status"] = "failed"
                self.send(job["chat_id"], f"❌ Job {esc(jid)} failed: {esc(type(exc).__name__)}: {esc(exc)}")
            finally:
                job["ended"] = time.time()

    def active_job(self, kind: str, ticker: str | None = None) -> dict | None:
        with self.jobs_lock:
            return next((j for j in self.jobs.values() if j["kind"] == kind and j["status"] in ("queued", "running")
                         and (ticker is None or j.get("ticker") == ticker)), None)

    def _save_chat_id_to_env(self, chat_id: int) -> None:
        env_path = PROJECT_ROOT / ".env"
        if env_path.exists():
            text = env_path.read_text()
            if "TELEGRAM_CHAT_ID=" in text:
                text = re.sub(r"TELEGRAM_CHAT_ID=.*", f"TELEGRAM_CHAT_ID={chat_id}", text)
            else:
                text += f"\nTELEGRAM_CHAT_ID={chat_id}\n"
            env_path.write_text(text)
        else:
            env_path.write_text(f"TELEGRAM_BOT_TOKEN={self.token}\nTELEGRAM_CHAT_ID={chat_id}\n")

    # ---- dispatch -------------------------------------------------------------
    def process_update(self, update: dict[str, Any]) -> None:
        msg = update.get("message")
        if not msg:
            return
        chat_id = msg.get("chat", {}).get("id")
        user = msg.get("from", {})
        if chat_id not in self.allowed:
            if not self.allowed:
                # First-time pairing: pair with the first user who messages the bot
                self.allowed.add(chat_id)
                self._save_chat_id_to_env(chat_id)
                print(f"[{self.label}] initial pairing with chat {chat_id} (@{user.get('username')}); saved to .env")
                self.send(chat_id, f"✅ <b>Bot paired successfully!</b>\n\nYour chat ID (<code>{chat_id}</code>) has been saved.\n\n" + HELP, keyboard=True)
                return
            print(f"[{self.label}] ignored message from unauthorised chat {chat_id} (@{user.get('username')})")
            self.send(chat_id, f"🔒 This bot is private.\n\nYour chat ID is <code>{chat_id}</code>. "
                               f"Add <code>TELEGRAM_CHAT_ID={chat_id}</code> to <code>.env</code> to authorise this chat.")
            return
        photos = msg.get("photo")
        doc = msg.get("document") or {}
        if photos or (doc.get("mime_type") or "").startswith("image/"):
            self.spawn(self.handle_photo, chat_id, photos[-1]["file_id"] if photos else doc["file_id"])
            return
        text = (msg.get("text") or "").strip()
        if not text:
            return
        cmd, _, rest = text.partition(" ")
        cmd = BUTTONS.get(text.lower(), cmd.lower().split("@")[0])
        rest = rest.strip()
        if cmd in ("/start", "/help"):
            self.send(chat_id, HELP, keyboard=True)
        elif cmd in ("/analyse", "/analyze"):
            self.handle_analyse(chat_id, rest)
        elif cmd == "/portfolio":
            self.spawn(self.handle_portfolio, chat_id)
        elif cmd in ("/opportunities", "/scan"):
            self.handle_opportunities(chat_id)
        elif cmd == "/status":
            self.handle_status(chat_id)
        elif cmd == "/selftest":
            self.spawn(self.handle_selftest, chat_id)
        elif cmd == "/confirm":
            self.spawn(self.handle_confirm, chat_id)
        elif cmd == "/cancel":
            self.send(chat_id, "Dropped the pending screenshot." if self.pending.pop(chat_id, None)
                      else "Nothing pending.")
        elif cmd == "/screenshot":
            self.send(chat_id, "Send the IBKR Positions screenshot as a photo. Make sure the Position "
                               "column is fully visible (IBKR's pinned Instrument column can hide its first digits).")
        else:
            self.handle_free_text(chat_id, text)

    # ---- free text --------------------------------------------------------------
    def tickers_in(self, text: str) -> list[str]:
        known = pipeline_store.known_tickers() | set(portfolio_analyser.load_portfolio().get("tickers", []))
        out = []
        for tok in re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-]{0,14}", text):
            mapped = COMPANY_ALIASES.get(tok.lower(), tok.upper()).rstrip(".")
            if mapped in known and mapped not in out:
                out.append(mapped)
        return out

    def route_intent(self, chat_id: int, text: str) -> bool:
        """Analysis or buy/sell questions about a known ticker get the verified card (or the
        reason there isn't one), never a free-form answer."""
        tickers = self.tickers_in(text)
        if not (tickers and ANALYSIS_WORDS.search(text)):
            return False
        for t in tickers[:3]:
            card, report = tn.verdict_message(t)
            self.send(chat_id, card)
        self.send(chat_id, "Verdicts only come from the 3-agent pipeline: <code>/analyse TICKER</code> runs it, "
                           "<code>/analyse TICKER fresh</code> re-runs a recent one.")
        return True

    def handle_free_text(self, chat_id: int, text: str) -> None:
        if self.route_intent(chat_id, text):
            return
        self.send(chat_id, "I run fixed commands only, so every number I send is traceable to a "
                           "verified pipeline run.\n\n" + HELP, keyboard=True)

    # ---- /analyse ---------------------------------------------------------------
    def handle_analyse(self, chat_id: int, rest: str) -> None:
        parts = rest.split()
        if not parts:
            self.send(chat_id, "Usage: <code>/analyse TICKER</code> (e.g. <code>/analyse MC.PA</code>)")
            return
        raw_ticker = parts[0].strip()
        ticker = COMPANY_ALIASES.get(raw_ticker.lower(), raw_ticker.upper())
        fresh = any(p.upper() == "FRESH" for p in parts[1:])
        if not TICKER_RE.fullmatch(ticker):
            self.send(chat_id, f"'{esc(ticker)}' doesn't look like a ticker. Use the Yahoo symbol, e.g. BATS.L, 7974.T.")
            return
        res = pipeline_store.latest(ticker)
        if res.verified and not fresh and (res.age_days or 0) <= pipeline_store.REUSE_DAYS:
            card, report = tn.verdict_message(ticker)
            self.send(chat_id, card)
            if report:
                self.send_doc(chat_id, report, caption=f"{ticker} verified pipeline report")
            return
        if self.active_job("pipeline", ticker):
            self.send(chat_id, f"A pipeline run for {esc(ticker)} is already queued or running. /status")
            return
        blocker = self.engine_blocker()
        if blocker:
            self.send(chat_id, f"❌ The pipeline can't run: {esc(blocker)}. I won't substitute anything else.")
            return
        why = ("fresh run requested" if fresh else
               f"latest verified run is {res.age_days} days old" if res.verified else
               "no verified run on file" + (f" ({', '.join(res.skipped_runs)} failed verification)"
                                            if res.skipped_runs else ""))
        ahead = self.enqueue("pipeline", chat_id, self.run_pipeline_job, ticker=ticker, fresh=fresh)
        engine = "Gemini in Antigravity, one conversation per stage" if self.engine == "antigravity" else "Claude Code"
        self.send(chat_id, f"⏳ <b>{esc(ticker)}</b>: starting the 3-agent pipeline ({esc(why)}) on {engine}.\n"
                           "Researcher → Quant → Skeptic, then the report and lint. Usually 20–60 minutes. I'll post "
                           "each stage once it passes its checks and send the verified card at the end."
                           + (f"\nQueue position: {ahead + 1}." if ahead > 0 else ""))

    def engine_blocker(self) -> str | None:
        if self.engine == "antigravity":
            return antigravity_pipeline.antigravity_available()
        if self.engine == "claude":
            return None if self.claude else "Claude Code CLI not found (set CLAUDE_BIN in .env)"
        return f"unknown PIPELINE_ENGINE '{self.engine}' (use antigravity or claude)"

    def handle_selftest(self, chat_id: int) -> None:
        self.send(chat_id, "🔧 Checking the Gemini engine: starting a tiny test conversation in Antigravity…")
        ok, msg = antigravity_pipeline.selftest()
        self.send(chat_id, ("✅ " if ok else "❌ ") + esc(msg))

    def pipeline_command(self, ticker: str, fresh: bool, run_dir: Path, today: str) -> list[str]:
        if self.engine == "antigravity":
            return [sys.executable, str(PROJECT_ROOT / "methodologies" / "antigravity_pipeline.py"), "run", ticker] \
                + (["--fresh"] if fresh else [])
        cmd = [self.claude, "-p", "--output-format", "json",
               "--permission-mode", self.get("PIPELINE_PERMISSION_MODE") or "dontAsk",
               "--allowedTools", ",".join(PIPELINE_TOOLS)]
        if self.get("PIPELINE_MAX_BUDGET_USD"):
            cmd += ["--max-budget-usd", self.get("PIPELINE_MAX_BUDGET_USD")]
        return cmd

    def run_pipeline_job(self, job: dict) -> None:
        ticker, chat_id = job["ticker"], job["chat_id"]
        today = datetime.now().strftime("%Y-%m-%d")
        run_dir = pipeline_store.RUNS_DIR / f"{ticker}_{today}"
        if run_dir.exists() and self.engine == "claude":     # the Gemini orchestrator does this itself
            moved = provenance.supersede(run_dir) if job["fresh"] else provenance.quarantine(run_dir)
            if moved:
                self.send(chat_id, f"Moved {len(moved)} existing file(s) out of {esc(run_dir.name)} "
                                   f"({'superseded' if job['fresh'] else 'unverified'}): {esc(', '.join(moved))}")
        log_path = JOBS_DIR / f"{ticker}_{datetime.now():%Y%m%d_%H%M%S}.log"
        job["log"] = str(log_path.relative_to(PROJECT_ROOT))
        cmd = self.pipeline_command(ticker, job["fresh"], run_dir, today)
        timeout_s = int(self.get("PIPELINE_TIMEOUT_MIN") or 240) * 60
        prompt = PIPELINE_PROMPT.format(ticker=ticker, run_dir=f"reports/runs/{ticker}_{today}/", date=today)
        with open(log_path, "w") as log:
            proc = subprocess.Popen(cmd, cwd=PROJECT_ROOT, stdin=subprocess.PIPE, stdout=log,
                                    stderr=subprocess.STDOUT, text=True)
            if self.engine == "claude":
                proc.stdin.write(prompt)
            proc.stdin.close()
            seen: set[str] = set()
            while proc.poll() is None:
                time.sleep(20)
                for stage in self._recorded_stages(run_dir) - seen:
                    seen.add(stage)
                    self.send(chat_id, f"✅ {esc(ticker)} [{STAGE_LABEL[stage]}] finished and passed its checks.")
                if time.time() - job["started"] > timeout_s:
                    proc.terminate()
                    self.send(chat_id, f"⌛ {esc(ticker)}: stopped after {timeout_s // 60} min.")
                    break
        res = pipeline_store.latest(ticker)
        if res.verified and str(res.as_of) == today:
            card, report = tn.verdict_message(ticker)
            self.send(chat_id, "🏁 Pipeline finished and verified.\n" + card)
            if report:
                self.send_doc(chat_id, report, caption=f"{ticker} verified pipeline report")
            return
        job["status_final"] = "unverified"
        problems = res.problems if res.run_dir and res.run_dir.name.endswith(today) else \
            ["no report from today's run (see the log)"]
        tail = [l for l in log_path.read_text(errors="replace").splitlines() if "FAILED" in l or "problem" in l][-2:]
        self.send(chat_id, f"❌ <b>{esc(ticker)}</b>: the run didn't produce a verified report, so nothing was "
                           "concluded and no verdict is shown.\n" + "\n".join(f"• {esc(p)}" for p in problems[:5])
                           + "".join(f"\n• {esc(l[-300:])}" for l in tail)
                           + f"\nLog: <code>{esc(job['log'])}</code>")

    @staticmethod
    def _recorded_stages(run_dir: Path) -> set[str]:
        records, _ = provenance.load_records(run_dir) if run_dir.exists() else ([], [])
        return {r["stage"] for r in records if r.get("method") in ("hook", "orchestrator") and r.get("stage") in STAGE_LABEL}

    # ---- /portfolio ---------------------------------------------------------------
    def handle_portfolio(self, chat_id: int) -> None:
        self.send(chat_id, "📊 Building the audit from verified pipeline runs and live prices…")
        audit = portfolio_analyser.build_audit(live=True)
        if not audit.rows:
            self.send(chat_id, "No holdings saved yet. Send an IBKR screenshot first.")
            return
        report = portfolio_analyser.write_report(audit)
        for m in tn.format_portfolio_messages(audit):
            self.send(chat_id, m)
        self.send_doc(chat_id, report, caption=f"Portfolio audit {audit.generated[:10]} (verified runs only)")
        if audit.unverified:
            self.send(chat_id, f"{len(audit.unverified)} holdings have no verified verdict. "
                               "<code>/analyse TICKER</code> runs the pipeline for one (they queue, one at a time).",
                      keyboard=True)

    # ---- screenshots ----------------------------------------------------------------
    def handle_photo(self, chat_id: int, file_id: str) -> None:
        self.send(chat_id, "📸 Reading the screenshot…")
        path = SCREENSHOTS_DIR / f"ibkr_{datetime.now():%Y%m%d_%H%M%S}.png"
        if not self.download(file_id, path):
            self.send(chat_id, "❌ Couldn't download the image from Telegram. Please try again.")
            return
        prev = portfolio_ocr.parse_ibkr_screenshot(path, save=False)
        if not prev["holdings"]:
            self.send(chat_id, "⚠️ No positions recognised. Send the IBKR <b>Positions</b> view with the "
                               "Instrument and Position columns visible.")
            return
        self.pending[chat_id] = prev
        lines = [f"📸 Read <b>{len(prev['holdings'])}</b> positions:"]
        for h in prev["holdings"]:
            shares = "⚠️ shares unknown" if h.get("shares") is None else f"{h['shares']:g} sh"
            lines.append(f"• <code>{esc(h['ticker'])}</code> {esc(shares)}")
        d = prev["diff"]
        if d["added"]:
            lines.append("➕ New vs saved: " + esc(", ".join(d["added"])))
        if d["changed"]:
            lines.append("✏️ Changed: " + esc("; ".join(d["changed"])))
        if d["removed"]:
            lines.append(f"➖ <b>Not in this screenshot</b>: {esc(', '.join(d['removed']))}. If the screenshot "
                         "is cut off, /cancel and send all positions; /confirm treats these as sold.")
        if prev["rejected"]:
            lines.append("❔ No vendor price, dropped: " + esc(", ".join(prev["rejected"])))
        for w in prev["warnings"][:6]:
            lines.append(f"⚠️ {esc(w)}")
        lines.append("\nReply /confirm to save this as your portfolio, or /cancel.")
        self.send(chat_id, "\n".join(lines))

    def handle_confirm(self, chat_id: int) -> None:
        prev = self.pending.pop(chat_id, None)
        if not prev:
            self.send(chat_id, "Nothing pending. Send a screenshot first.")
            return
        portfolio_ocr.save_portfolio(prev, via="Telegram /confirm")
        self.send(chat_id, f"✅ Saved {len(prev['holdings'])} holdings.")
        self.handle_portfolio(chat_id)

    # ---- /opportunities ----------------------------------------------------------------
    def handle_opportunities(self, chat_id: int) -> None:
        if self.active_job("screen"):
            self.send(chat_id, "A screen is already running. /status")
            return
        self.enqueue("screen", chat_id, self.run_screen_job)
        self.send(chat_id, "🔍 Running the opportunity screen (4 presets, a few minutes). Results are "
                           "candidates for /analyse, not recommendations.")

    def run_screen_job(self, job: dict) -> None:
        import discover
        master = discover.run_all_presets(top_n=5)
        data = json.loads(master.with_suffix(".json").read_text())
        for m in tn.format_discovery_messages(data):
            self.send(job["chat_id"], m)
        self.send_doc(job["chat_id"], master, caption="Opportunity screen (candidates for /analyse)")

    # ---- /status ------------------------------------------------------------------------
    def handle_status(self, chat_id: int) -> None:
        with self.jobs_lock:
            jobs = sorted(self.jobs.values(), key=lambda j: j["id"])[-10:]
        if not jobs:
            blocker = self.engine_blocker()
            self.send(chat_id, f"No jobs since the bot started. Pipeline engine: {esc(self.engine)}."
                      + (f"\n⚠️ {esc(blocker)}" if blocker else ""))
            return
        lines = [f"<b>Jobs</b> (pipeline engine: {esc(self.engine)})"]
        for j in jobs:
            mins = f"{(time.time() - j['started']) / 60:.0f} min" if j.get("started") and j["status"] == "running" else ""
            stages = ""
            if j["kind"] == "pipeline":
                done = self._recorded_stages(pipeline_store.RUNS_DIR / f"{j['ticker']}_{datetime.now():%Y-%m-%d}")
                stages = f" · stages done: {len(done)}/3"
            lines.append(f"• {esc(j['kind'])} {esc(j.get('ticker', ''))}: {esc(j['status'])} {mins}{stages}")
        self.send(chat_id, "\n".join(lines))

    # ---- loop -------------------------------------------------------------------------
    def run(self) -> None:
        blocker = self.engine_blocker()
        print(f"[{self.label}] polling. Allowed chats: {sorted(self.allowed) or 'NONE (set TELEGRAM_CHAT_ID)'}. "
              f"Pipeline engine: {self.engine}" + (f" (UNAVAILABLE: {blocker})" if blocker else " (ready)"))
        last_conflict = 0.0
        while True:
            try:
                res = self.api("getUpdates", {"timeout": 25, "offset": self.offset + 1} if self.offset
                               else {"timeout": 25}, timeout=40)
                if res.get("error_code") == 409:
                    if time.time() - last_conflict > 60:
                        print(f"[{self.label}] 409 Conflict: another process is polling this bot token. "
                              "Stop it, or each message goes to one of you at random.")
                        last_conflict = time.time()
                    time.sleep(5)
                    continue
                for update in res.get("result", []) if res.get("ok") else []:
                    self.offset = update["update_id"]
                    self._save_offset()               # acknowledged before handling: no replays on crash
                    try:
                        self.process_update(update)
                    except Exception:
                        traceback.print_exc()
            except KeyboardInterrupt:
                print(f"\n[{self.label}] stopped.")
                break
            except Exception as exc:
                print(f"[{self.label}] polling error: {exc}")
                time.sleep(3)


def main() -> None:
    cfg = load_config(("TELEGRAM_APP_BOT_TOKEN", "TELEGRAM_BOT_TOKEN"))
    if not cfg["token"]:
        sys.exit("Set TELEGRAM_BOT_TOKEN (or TELEGRAM_APP_BOT_TOKEN) in .env.")
    _lock = acquire_poller_lock(cfg["token"])  # held for the process lifetime
    TelegramApp(cfg["token"], cfg["allowed"], cfg["get"]).run()


if __name__ == "__main__":
    main()
