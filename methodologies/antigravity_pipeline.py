"""Run the 3-agent /analyse pipeline on Gemini inside Antigravity.

Each stage runs in its OWN Antigravity conversation (`agentapi new-conversation`), started and
checked by this script, never by a model:

  0. setup (code): quarantine or supersede old files, fundamentals.py, run_inputs.py, holding status
  1-3. value-researcher -> value-quant -> value-skeptic. Each gets its agent file
       (.claude/agents/value-*.md) as instructions, a fresh conversation and a one-time nonce. A
       stage ends by running `antigravity_pipeline.py stage-done RUN_DIR STAGE NONCE`. This script
       then checks the stage's files (required sections, sources, the model runs, no other stage's
       file touched) and only then records provenance (method "orchestrator").
  4. a synthesis conversation writes the report; this script lints it, seals it, and appends the
     ledger row itself with the csv module.

Why (14 Oct 2026): one Antigravity conversation told to "enforce the 3-agent pipeline" wrote all
three stage files itself in about two minutes. Separate conversations, a nonce per stage and
code-side gates are what make a Gemini run a pipeline run.

It must run in a process started from Antigravity, because agentapi needs Antigravity's local
session in the environment (ANTIGRAVITY_LS_ADDRESS and its token). The Telegram bridge launched by
the Antigravity agent is such a process.

    python3 methodologies/antigravity_pipeline.py selftest
    python3 methodologies/antigravity_pipeline.py run TICKER [--fresh] [--model pro|flash]
    python3 methodologies/antigravity_pipeline.py stage-done RUN_DIR STAGE NONCE   # stage agents only
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import provenance  # noqa: E402
import report_lint  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "reports" / "runs"
AGENTS_DIR = PROJECT_ROOT / ".claude" / "agents"
SKILL = PROJECT_ROOT / ".claude" / "skills" / "analyse" / "SKILL.md"
LEDGER = PROJECT_ROOT / "reports" / "prediction_ledger.csv"
SELFTEST_DIR = PROJECT_ROOT / "data" / ".antigravity_selftest"
DONE_DIR = ".stage_done"
AGENTAPI = Path(os.environ.get("ANTIGRAVITY_AGENTAPI") or Path.home() / ".gemini/antigravity-ide/bin/agentapi")
STAGE_TIMEOUT_MIN = int(os.environ.get("PIPELINE_STAGE_TIMEOUT_MIN") or 60)
FIX_ROUNDS = 2                        # follow-up messages per stage before giving up
POLL_S = 10


@dataclass(frozen=True)
class Stage:
    name: str                         # provenance stage name
    label: str
    owns: tuple[str, ...]             # files this stage may write
    main: str                         # the file its gates check
    sections: tuple[str, ...]         # regexes of required "## " headings


STAGES = (
    Stage("value-researcher", "1/3 Researcher", ("01_research.md", "facts.json"), "01_research.md",
          tuple(rf"^##\s*{n}\." for n in range(11)) + (r"^##\s*Sources",)),
    Stage("value-quant", "2/3 Quant", ("02_quant.md", "02_model.py"), "02_quant.md",
          tuple(rf"^##\s*{c}\." for c in "ABCDEFGH")),
    Stage("value-skeptic", "3/3 Skeptic", ("03_skeptic.md", "03_rerun.py"), "03_skeptic.md",
          tuple(rf"^##\s*{n}\." for n in range(1, 9))),
)
SYNTHESIS = "synthesis"


class AgentApiError(RuntimeError):
    pass


def log(msg: str) -> None:
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


# --------------------------------------------------------------------------- #
# agentapi
# --------------------------------------------------------------------------- #
def antigravity_available() -> str | None:
    """None if agentapi can be used from this process, else the reason it can't."""
    if not os.environ.get("ANTIGRAVITY_LS_ADDRESS"):
        return ("this process wasn't started from Antigravity (no ANTIGRAVITY_LS_ADDRESS). Start the "
                "bot from the Antigravity agent: ask it to run ./run_bridge.sh")
    if not AGENTAPI.exists():
        return f"agentapi not found at {AGENTAPI}"
    return None


def _agentapi(*args: str, timeout: int = 120) -> dict:
    res = subprocess.run([str(AGENTAPI), *args], capture_output=True, text=True, timeout=timeout)
    out = (res.stdout or "").strip()
    try:
        data = json.loads(out) if out else {}
    except json.JSONDecodeError:
        if res.returncode:
            raise AgentApiError((out or res.stderr or "agentapi failed").strip()[:400])
        return {"raw": out}
    if isinstance(data, dict) and data.get("error"):
        raise AgentApiError(str(data["error"])[:400])
    return data


def find_conversation_id(data) -> str | None:
    """agentapi's success payload isn't documented: take an id-like key, else the first UUID."""
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, str) and re.search(r"(conversation|cascade|trajectory)_?id$|^id$", k, re.I):
                    yield v
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)
    for v in walk(data):
        if re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", v):
            return v
    m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", json.dumps(data))
    return m.group(0) if m else None


def new_conversation(prompt: str, title: str, model: str) -> str:
    data = _agentapi("new-conversation", f"--model={model}", f"--title={title[:60]}", prompt)
    cid = find_conversation_id(data)
    if not cid:
        raise AgentApiError(f"new-conversation returned no conversation id: {json.dumps(data)[:300]}")
    return cid


def send_message(conv_id: str, text: str, title: str = "pipeline") -> None:
    _agentapi("send-message", f"--title={title[:60]}", conv_id, text)


# --------------------------------------------------------------------------- #
# completion signal (run by the stage agent)
# --------------------------------------------------------------------------- #
def stage_done(run_dir: str, stage: str, nonce: str) -> int:
    d = Path(run_dir)
    d = (d if d.is_absolute() else PROJECT_ROOT / d).resolve()
    if d.parent != RUNS_DIR.resolve() or not d.is_dir():
        print(f"stage-done: {run_dir} is not a run folder under reports/runs/")
        return 2
    if stage not in {s.name for s in STAGES} | {SYNTHESIS}:
        print(f"stage-done: unknown stage {stage}")
        return 2
    (d / DONE_DIR).mkdir(exist_ok=True)
    (d / DONE_DIR / f"{stage}.json").write_text(json.dumps({
        "stage": stage, "nonce_sha256": sha(nonce), "at": datetime.now(timezone.utc).isoformat(),
        "conversation_env": os.environ.get("ANTIGRAVITY_CONVERSATION_ID"),
        "trajectory_env": os.environ.get("ANTIGRAVITY_TRAJECTORY_ID")}))
    print("Recorded. The orchestrator checks your files now. Stop here and wait: if anything is "
          "missing it will message you in this conversation.")
    return 0


def wait_for_done(run_dir: Path, stage: str, nonce: str, conv_id: str | None, deadline: float) -> dict | None:
    path = run_dir / DONE_DIR / f"{stage}.json"
    while time.time() < deadline:
        if path.exists():
            try:
                rec = json.loads(path.read_text())
            except json.JSONDecodeError:
                rec = {}
            path.unlink(missing_ok=True)                  # a signal is consumed exactly once
            if rec.get("nonce_sha256") != sha(nonce):
                log(f"{stage}: ignored a completion signal with the wrong nonce")
                continue
            env_cid = rec.get("conversation_env")
            if conv_id and env_cid and env_cid != conv_id:
                log(f"{stage}: ignored a completion signal from conversation {env_cid}, expected {conv_id}")
                continue
            return rec
        time.sleep(POLL_S)
    return None


# --------------------------------------------------------------------------- #
# prompts
# --------------------------------------------------------------------------- #
def agent_body(stage: Stage) -> str:
    text = (AGENTS_DIR / f"{stage.name}.md").read_text()
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S).strip()


def stage_prompt(stage: Stage, ticker: str, run_dir: Path, today: str, context: str, nonce: str) -> str:
    rel = run_dir.relative_to(PROJECT_ROOT)
    return f"""You are one stage of the value-investing pipeline: the **{stage.name}** ({stage.label}).
This conversation was started by methodologies/antigravity_pipeline.py. The other stages run in
separate conversations, and you can't see or talk to them. Work in {PROJECT_ROOT}.

TICKER: {ticker}
RUN_DIR: {rel}/
Today: {today}
{context}

Rules for this run (they add to your instructions below):
- Your instructions were written for Claude Code subagents. Where they name WebSearch, WebFetch or
  Bash, use your own web search, browsing and terminal tools.
- Write ONLY these files in RUN_DIR: {", ".join(stage.owns)}. Never create or edit another stage's
  files, the report, reports/prediction_ledger.csv or any .provenance.jsonl. The orchestrator checks
  file hashes and rejects the run if you do.
- Every number needs a source and a date, or it is UNKNOWN (.agents/AGENTS.md RULE 0).
- When your file is complete, and not before, run exactly this command, then stop:
    python3 {PROJECT_ROOT}/methodologies/antigravity_pipeline.py stage-done {rel} {stage.name} {nonce}
  The orchestrator then checks your work. If something is missing it will message you here.

==================== your instructions ====================
{agent_body(stage)}
"""


def synthesis_prompt(ticker: str, run_dir: Path, today: str, context: str, nonce: str) -> str:
    rel = run_dir.relative_to(PROJECT_ROOT)
    skill = SKILL.read_text()
    m = re.search(r"^## 2\. Synthesize.*?(?=^## 3\. )", skill, re.M | re.S)
    spec = m.group(0) if m else skill
    return f"""You write the final report of the value-investing pipeline for {ticker}. The three stages
already ran in separate conversations and their files are verified. Work in {PROJECT_ROOT}.

TICKER: {ticker}
RUN_DIR: {rel}/
Today: {today}
{context}

Rules:
- Read RUN_DIR/01_research.md, 02_quant.md (and run nothing that changes them), 03_skeptic.md, and
  03_rerun.py if present. Write ONLY RUN_DIR/{ticker}_report.md. Don't edit the stage files, the
  ledger or any .provenance.jsonl (the orchestrator logs the ledger row itself).
- Introduce no number that isn't in those files. Where the Skeptic corrected the Quant, use the
  corrected figure and say so.
- Keep PRICE, FAIR_VALUE, ENTRY_BELOW and EXIT_ABOVE in the quote currency, and make
  UPSIDE = FAIR_VALUE / PRICE - 1. The orchestrator runs report_lint.py on your file.
- When the report is complete, run exactly this command, then stop:
    python3 {PROJECT_ROOT}/methodologies/antigravity_pipeline.py stage-done {rel} {SYNTHESIS} {nonce}

==================== report specification (analyse skill) ====================
{spec}
"""


# --------------------------------------------------------------------------- #
# gates (code, not judgement)
# --------------------------------------------------------------------------- #
def _sections(text: str) -> dict[str, str]:
    parts = re.split(r"(?m)^(##\s.*)$", text)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def check_stage(stage: Stage, run_dir: Path, before: dict[str, str | None]) -> list[str]:
    """Problems with a finished stage. Empty means it may be recorded."""
    problems = []
    main = run_dir / stage.main
    if not main.exists():
        return [f"{stage.main} is missing"]
    text = main.read_text()
    if not text.startswith(f"<!-- pipeline:{stage.name} -->"):
        problems.append(f"{stage.main} must start with the line <!-- pipeline:{stage.name} -->")
    secs = _sections(text)
    for pat in stage.sections:
        hit = [body for head, body in secs.items() if re.match(pat, head)]
        if not hit:
            problems.append(f"{stage.main} is missing the section matching '{pat.strip('^')}'")
        elif len(re.sub(r"\s+", " ", hit[0]).strip()) < 40:
            problems.append(f"section '{pat.strip('^')}' in {stage.main} is empty or a placeholder")
    if stage.name == "value-researcher":
        src = next((b for h, b in secs.items() if re.match(r"^##\s*Sources", h)), "")
        n = len(re.findall(r"https?://|\d{10}-\d{2}-\d{6}", src))
        if n < 5:
            problems.append(f"Sources lists {n} URLs or accession numbers; at least 5 primary sources are needed")
    if stage.name == "value-quant":
        model = run_dir / "02_model.py"
        if not model.exists():
            problems.append("02_model.py is missing: the valuation must be executed code")
        else:
            res = subprocess.run([sys.executable, str(model)], cwd=PROJECT_ROOT, capture_output=True,
                                 text=True, timeout=300)
            if res.returncode:
                problems.append(f"02_model.py fails to run: {(res.stderr or res.stdout).strip()[-300:]}")
    if stage.name == "value-skeptic":
        audit = next((b for h, b in secs.items() if re.match(r"^##\s*2\.", h)), "")
        rows = [l for l in audit.splitlines() if l.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", l.strip())]
        if len(rows) - 1 < 8:
            problems.append(f"the number audit table has {max(len(rows) - 1, 0)} rows; check at least 8 load-bearing inputs")
        verdict = next((b for h, b in secs.items() if re.match(r"^##\s*8\.", h)), "")
        if not re.search(r"\b(BUY|ACCUMULATE|HOLD|TRIM|SELL|PASS)\b", verdict):
            problems.append("section 8 gives no verdict recommendation from the closed vocabulary")
    problems += isolation_problems(stage, run_dir, before)
    return problems


def snapshot(run_dir: Path) -> dict[str, str | None]:
    names = {f for s in STAGES for f in s.owns} | {provenance.report_name(run_dir)}
    return {n: (provenance.sha256_file(run_dir / n) if (run_dir / n).is_file() else None) for n in names}


def isolation_problems(stage: Stage, run_dir: Path, before: dict[str, str | None]) -> list[str]:
    after = snapshot(run_dir)
    shared = {"facts.json"}                   # later stages may refresh the Researcher's facts
    return [f"{name} was {'created' if before.get(name) is None else 'changed'} by the {stage.name} stage, "
            "which doesn't own it"
            for name, h in after.items()
            if h != before.get(name) and name not in stage.owns and name not in shared]


def record_stage(stage: Stage, run_dir: Path, conv_id: str | None, model: str) -> None:
    for name in stage.owns + ("facts.json",):
        path = run_dir / name
        if path.is_file():
            provenance._append(run_dir, {"file": name, "sha256": provenance.sha256_file(path), "stage": stage.name,
                                         "method": "orchestrator", "engine": f"antigravity:{model}",
                                         "conversation_id": conv_id})


# --------------------------------------------------------------------------- #
# ledger (code writes it, from the verified verdict block)
# --------------------------------------------------------------------------- #
def ledger_row(report: Path, inputs: dict, template: str | None) -> dict:
    f = report_lint.parse_verdict_block(report.read_text())
    price, fv = report_lint.parse_money(f.get("PRICE")), report_lint.parse_money(f.get("FAIR_VALUE"))
    entry, exit_ = report_lint.parse_money(f.get("ENTRY_BELOW")), report_lint.parse_money(f.get("EXIT_ABOVE"))
    ccy = (price or (0, None))[1] or inputs.get("quote_currency") or "USD"
    fx = 1.0 if ccy == "USD" else (inputs.get("fx_spot_to_usd") or {}).get(f"{ccy}USD")
    usd = (lambda m: f"{m[0] * fx:.2f}" if m and fx else "")
    as_of = (f.get("AS_OF") or "")[:10]
    review = (date.fromisoformat(as_of) + timedelta(days=91)).isoformat() if as_of else ""
    is_fund = (template or "").upper().startswith("FUND") or "%" in (f.get("FAIR_VALUE") or "").split("(")[0]
    fund_ret = re.match(r"\s*([\d.]+)\s*%", f.get("FAIR_VALUE") or "")
    return {"as_of": as_of, "ticker": report.stem[:-len("_report")], "verdict": (f.get("VERDICT") or "").upper(),
            "price_usd": usd(price), "fair_value": (fund_ret.group(1) if is_fund and fund_ret else usd(fv)),
            "upside_pct": "" if is_fund else (f.get("UPSIDE") or "").rstrip("%").lstrip("+"),
            "entry_below": "" if is_fund else usd(entry), "exit_above": "" if is_fund else usd(exit_),
            "conviction": f.get("CONVICTION", ""), "key_risk": f.get("KEY_RISK", ""),
            "data_warnings": f.get("DATA_WARNINGS", ""), "review_date": review, "actual_price_at_review": "",
            "outcome": "", "template": template or ""}


def append_ledger(row: dict) -> None:
    fields = next(csv.reader(LEDGER.open()))
    with LEDGER.open("a", newline="") as fh:
        csv.DictWriter(fh, fieldnames=fields).writerow({k: row.get(k, "") for k in fields})


# --------------------------------------------------------------------------- #
# the run
# --------------------------------------------------------------------------- #
def setup(ticker: str, fresh: bool) -> tuple[Path, str, str]:
    today = datetime.now().strftime("%Y-%m-%d")
    run_dir = RUNS_DIR / f"{ticker}_{today}"
    if run_dir.exists():
        moved = provenance.supersede(run_dir) if fresh else provenance.quarantine(run_dir)
        if moved:
            log(f"moved {', '.join(moved)} out of {run_dir.name} ({'superseded' if fresh else 'unverified'})")
    run_dir.mkdir(parents=True, exist_ok=True)
    py = sys.executable
    subprocess.run([py, str(PROJECT_ROOT / "methodologies" / "fundamentals.py"), ticker], cwd=PROJECT_ROOT,
                   capture_output=True, text=True, timeout=600)
    rec = json.loads((PROJECT_ROOT / "data" / "fundamentals.json").read_text()).get("records", {}).get(ticker, {})
    if rec.get("errors"):
        raise RuntimeError(f"BLOCKED: data layer errors for {ticker}: {rec['errors']}")
    subprocess.run([py, str(PROJECT_ROOT / "methodologies" / "run_inputs.py"), ticker, str(run_dir)],
                   cwd=PROJECT_ROOT, capture_output=True, text=True, timeout=600)
    held = ticker in report_lint.held_tickers()
    context = (f"Holding status: {'CURRENT HOLDING' if held else 'not held'} (data/portfolio.json). "
               f"Vendor quote type: {rec.get('quoteType') or rec.get('quote_type') or 'UNKNOWN'}. Shared rates, FX "
               f"and the official close are in RUN_DIR/00_inputs.json; data-layer warnings: "
               f"{len(rec.get('warnings', []))} (data/fundamentals.json).")
    return run_dir, today, context


def run_stage(stage_name: str, label: str, prompt_for, run_dir: Path, ticker: str, model: str,
              check, deadline_min: int) -> str:
    nonce = secrets.token_hex(12)
    before = snapshot(run_dir)
    conv = new_conversation(prompt_for(nonce), f"{ticker} {label}", model)
    log(f"{label}: started Antigravity conversation {conv} ({model})")
    for round_ in range(FIX_ROUNDS + 1):
        rec = wait_for_done(run_dir, stage_name, nonce, conv, time.time() + deadline_min * 60)
        if rec is None:
            raise RuntimeError(f"{label}: no completion signal within {deadline_min} min (conversation {conv})")
        problems = check(before)
        if not problems:
            return conv
        log(f"{label}: {len(problems)} problem(s): {'; '.join(problems)}")
        if round_ == FIX_ROUNDS:
            raise RuntimeError(f"{label} failed its checks: {'; '.join(problems)}")
        send_message(conv, "The orchestrator checked your files and they aren't accepted yet:\n- "
                     + "\n- ".join(problems) + "\nFix these, then run the same stage-done command again "
                     "(same nonce).", title=f"{ticker} {label} fixes")
    raise RuntimeError(f"{label}: unreachable")


def run(ticker: str, fresh: bool = False, model: str | None = None) -> int:
    reason = antigravity_available()
    if reason:
        log(f"cannot run: {reason}")
        return 2
    model = model or os.environ.get("PIPELINE_GEMINI_MODEL") or "pro"
    ticker = ticker.strip().upper()
    run_dir, today, context = setup(ticker, fresh)
    log(f"setup done: {run_dir.relative_to(PROJECT_ROOT)}")
    for stage in STAGES:
        status = provenance.verify_run(run_dir)["files"]
        if all(status.get(f) == "verified" for f in stage.owns if f in provenance.REQUIRED):
            log(f"{stage.label}: already verified in this run folder (an earlier attempt), skipped")
            continue
        conv = run_stage(stage.name, stage.label,
                         lambda n, s=stage: stage_prompt(s, ticker, run_dir, today, context, n),
                         run_dir, ticker, model,
                         lambda before, s=stage: check_stage(s, run_dir, before), STAGE_TIMEOUT_MIN)
        record_stage(stage, run_dir, conv, model)
        log(f"{stage.label}: verified and recorded")

    report = run_dir / f"{ticker}_report.md"

    def check_report(before):
        if not report.exists():
            return [f"{report.name} is missing"]
        issues = report_lint.lint(report, report_lint.load_warnings())
        changed = [n for n, h in snapshot(run_dir).items() if n != report.name and h != before.get(n)]
        return ([f"lint: {m}" for lvl, m in issues if lvl == "ERROR"]
                + [f"{n} was changed during synthesis; only the report may be written" for n in changed])

    run_stage(SYNTHESIS, "report", lambda n: synthesis_prompt(ticker, run_dir, today, context, n),
              run_dir, ticker, model, check_report, STAGE_TIMEOUT_MIN)
    provenance._append(run_dir, {"file": report.name, "sha256": provenance.sha256_file(report),
                                 "stage": "orchestrator", "method": "lint-seal", "via": "antigravity_pipeline"})
    tmpl = re.search(r"Template\s+([A-Za-z-]+)", report.read_text())
    inputs = json.loads((run_dir / "00_inputs.json").read_text()) if (run_dir / "00_inputs.json").exists() else {}
    append_ledger(ledger_row(report, inputs, tmpl.group(1) if tmpl else None))
    log(f"report linted, sealed and logged to the ledger: {report.relative_to(PROJECT_ROOT)}")
    return 0


# --------------------------------------------------------------------------- #
# selftest
# --------------------------------------------------------------------------- #
def ping(nonce: str) -> int:
    SELFTEST_DIR.mkdir(parents=True, exist_ok=True)
    (SELFTEST_DIR / f"{sha(nonce)[:16]}.json").write_text(json.dumps(
        {"conversation_env": os.environ.get("ANTIGRAVITY_CONVERSATION_ID"), "at": datetime.now().isoformat()}))
    print("pong")
    return 0


def selftest(model: str = "flash_lite", wait_s: int = 240) -> tuple[bool, str]:
    reason = antigravity_available()
    if reason:
        return False, f"Gemini engine unavailable: {reason}"
    nonce = secrets.token_hex(8)
    try:
        conv = new_conversation(
            "Automated connectivity test from the investment pipeline orchestrator. Run exactly this one "
            f"terminal command, then reply DONE and stop. Don't edit any files:\n"
            f"python3 {PROJECT_ROOT}/methodologies/antigravity_pipeline.py ping {nonce}",
            "pipeline selftest", model)
    except Exception as exc:
        return False, f"agentapi new-conversation failed: {exc}"
    path = SELFTEST_DIR / f"{sha(nonce)[:16]}.json"
    deadline = time.time() + wait_s
    while time.time() < deadline and not path.exists():
        time.sleep(5)
    if not path.exists():
        return False, (f"conversation {conv} was created but its command didn't run within {wait_s}s. "
                       "Antigravity may be asking for approval before terminal commands: allow auto-execution "
                       "for this workspace, then re-run the self-test.")
    env_cid = json.loads(path.read_text()).get("conversation_env")
    path.unlink(missing_ok=True)
    match = "matches" if env_cid == conv else ("absent" if not env_cid else f"differs ({env_cid})")
    return True, f"OK: conversation {conv} ran the command; conversation id in its environment {match}."


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="3-agent pipeline on Gemini in Antigravity")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("ticker")
    r.add_argument("--fresh", action="store_true")
    r.add_argument("--model", choices=("pro", "flash", "flash_lite"))
    d = sub.add_parser("stage-done")
    d.add_argument("run_dir")
    d.add_argument("stage")
    d.add_argument("nonce")
    sub.add_parser("selftest")
    pg = sub.add_parser("ping")
    pg.add_argument("nonce")
    a = p.parse_args(argv[1:])
    if a.cmd == "stage-done":
        return stage_done(a.run_dir, a.stage, a.nonce)
    if a.cmd == "ping":
        return ping(a.nonce)
    if a.cmd == "selftest":
        ok, msg = selftest()
        print(msg)
        return 0 if ok else 1
    try:
        return run(a.ticker, fresh=a.fresh, model=a.model)
    except Exception as exc:
        log(f"FAILED: {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
