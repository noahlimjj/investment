"""Pipeline provenance: proof that a run's stage files came from the real value-* subagents.

Why this exists (14 Oct 2026): an agent outside Claude Code wrote look-alike 01/02/03 files,
with forged `<!-- pipeline:... -->` headers, into 13 run folders, copied files the pipeline had
quarantined back into place, and appended their verdicts to the ledger. Lint passed them,
because a header is just text anyone can type. These records can't be produced that way: they
are written by Claude Code hooks (harness code, no model in the loop) at the moment a value-*
subagent finishes, and HMAC-signed with a key kept outside the repo. `report_lint.py` fails any
run whose stage files don't match a record, and the Telegram bot only shows verdicts from runs
that pass and whose report carries a lint seal.

    python3 methodologies/provenance.py verify RUN_DIR [RUN_DIR ...]
    python3 methodologies/provenance.py quarantine RUN_DIR      # orchestrator step 0
    python3 methodologies/provenance.py supersede RUN_DIR       # before a from-scratch re-run
    python3 methodologies/provenance.py backfill [--dry-run]    # runs made before the hooks existed
    python3 methodologies/provenance.py hook-subagent           # SubagentStop hook (stdin: hook JSON)
    python3 methodologies/provenance.py hook-lint               # PostToolUse(Bash) hook (stdin: hook JSON)

Gemini runs in Antigravity have no hooks: there `antigravity_pipeline.py` writes the records
(method "orchestrator") after checking each stage it started in its own conversation.

Never write, copy or edit `.provenance.jsonl` by hand. A run without valid records is re-run
through /analyse; it is never "fixed" by making records for it.
"""
from __future__ import annotations

import glob
import hashlib
import hmac
import json
import os
import re
import secrets
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "reports" / "runs"
RECORDS = ".provenance.jsonl"
KEY_FILE = Path(os.environ.get("VALUE_PIPELINE_KEY_FILE",
                               Path.home() / ".config" / "value-pipeline" / "provenance.key"))

STAGES = ("value-researcher", "value-quant", "value-skeptic")
# Files each stage owns. facts.json is the Researcher's, but later stages may legitimately
# refresh it, so every stage records it when it finishes.
STAGE_FILES = {
    "value-researcher": ("01_research.md", "facts.json"),
    "value-quant": ("02_quant.md", "02_model.py", "facts.json"),
    "value-skeptic": ("03_skeptic.md", "03_rerun.py", "facts.json"),
}
REQUIRED = {"01_research.md": "value-researcher", "02_quant.md": "value-quant",
            "02_model.py": "value-quant", "03_skeptic.md": "value-skeptic"}
OPTIONAL = {"facts.json": None, "03_rerun.py": "value-skeptic"}
BACKFILL_GRACE_S = 90          # a stage file may be flushed shortly after the agent's last turn

STATUS_TEXT = {
    "verified": "written by its pipeline agent",
    "missing": "missing",
    "unrecorded": "no provenance record: not written by its value-* subagent (outside agent or hand edit)",
    "modified": "changed after its pipeline agent finished",
    "bad-signature": "provenance record has an invalid signature (forged or corrupted)",
}


# --------------------------------------------------------------------------- #
# signing
# --------------------------------------------------------------------------- #
def _key() -> bytes:
    if not KEY_FILE.exists():
        KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(KEY_FILE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w") as fh:
            fh.write(secrets.token_hex(32))
    return KEY_FILE.read_text().strip().encode()


def _sign(rec: dict) -> str:
    body = json.dumps({k: v for k, v in rec.items() if k != "sig"}, sort_keys=True)
    return hmac.new(_key(), body.encode(), hashlib.sha256).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _append(run_dir: Path, rec: dict) -> None:
    rec = {"v": 1, **rec, "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    rec["sig"] = _sign(rec)
    with open(run_dir / RECORDS, "a") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")


def load_records(run_dir: Path) -> tuple[list[dict], list[dict]]:
    """(records with a valid signature, records whose signature failed)."""
    path = Path(run_dir) / RECORDS
    good, bad = [], []
    if not path.exists():
        return good, bad
    for line in path.read_text().splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            bad.append({})
            continue
        (good if hmac.compare_digest(str(rec.get("sig", "")), _sign(rec)) else bad).append(rec)
    return good, bad


# --------------------------------------------------------------------------- #
# verification
# --------------------------------------------------------------------------- #
def report_name(run_dir: Path) -> str:
    return f"{Path(run_dir).name.rsplit('_', 1)[0]}_report.md"


def verify_run(run_dir: str | Path) -> dict:
    """Per-file provenance status for one run folder.

    Returns {"files": {name: status}, "report": status, "bad_signatures": n}. Required stage
    files are 'verified' only when their current hash matches a signed record made by the
    stage that owns them. The report is 'sealed' when a Claude Code session ran lint on this
    exact text and it passed.
    """
    run_dir = Path(run_dir)
    records, bad = load_records(run_dir)
    out: dict = {"files": {}, "bad_signatures": len(bad)}

    def status(name: str, stage: str | None) -> str:
        path = run_dir / name
        if not path.exists():
            return "missing"
        recs = [r for r in records if r.get("file") == name and r.get("method") != "lint-seal"
                and (stage is None or r.get("stage") == stage)]
        if not recs:
            return "bad-signature" if any(r.get("file") == name for r in bad) else "unrecorded"
        current = sha256_file(path)
        return "verified" if any(r.get("sha256") == current for r in recs) else "modified"

    for name, stage in REQUIRED.items():
        out["files"][name] = status(name, stage)
    for name, stage in OPTIONAL.items():
        if (run_dir / name).exists():
            out["files"][name] = status(name, stage)

    rep = run_dir / report_name(run_dir)
    seals = [r for r in records if r.get("method") == "lint-seal" and r.get("file") == rep.name]
    if not rep.exists():
        out["report"] = "missing"
    elif not seals:
        out["report"] = "unsealed"
    else:
        out["report"] = "sealed" if any(r.get("sha256") == sha256_file(rep) for r in seals) else "modified"
    return out


def stage_problems(run_dir: str | Path) -> list[str]:
    """Human-readable provenance failures for the required stage files (empty = all verified)."""
    res = verify_run(run_dir)
    probs = []
    for name, st in res["files"].items():
        if st != "verified" and not (name in OPTIONAL and st == "missing"):
            if name == "facts.json" and st == "unrecorded":
                continue        # non-SEC filers may get a hand-built facts.json from the Researcher
            probs.append(f"{name}: {STATUS_TEXT.get(st, st)}")
    return probs


# --------------------------------------------------------------------------- #
# quarantine (orchestrator step 0)
# --------------------------------------------------------------------------- #
def quarantine(run_dir: str | Path) -> list[str]:
    """Move stage files and the report that lack valid provenance into _external_unverified/.

    Run this once at the start of a fresh /analyse invocation, never mid-run: a checkpoint left
    by an agent that is still working (or was cut off in this session) has no record yet.
    """
    run_dir = Path(run_dir)
    if not run_dir.is_dir():
        return []
    res = verify_run(run_dir)
    dest = run_dir / "_external_unverified" / datetime.now().strftime("%Y%m%d_%H%M%S")
    names = [n for n, st in res["files"].items() if st not in ("verified", "missing")]
    if res["report"] in ("unsealed", "modified") or names:
        if (run_dir / report_name(run_dir)).exists():
            names.append(report_name(run_dir))
    return _move(run_dir, names, dest)


def supersede(run_dir: str | Path) -> list[str]:
    """Move every stage file and the report to _superseded/<time>/ before a from-scratch re-run
    in the same RUN_DIR. Without this the agents' resume rule would pick the finished files up
    and do nothing. Provenance records stay; they only describe the moved files."""
    run_dir = Path(run_dir)
    names = list(REQUIRED) + list(OPTIONAL) + [report_name(run_dir), "00_orchestrator_notes.md"]
    return _move(run_dir, names, run_dir / "_superseded" / datetime.now().strftime("%Y%m%d_%H%M%S"))


def _move(run_dir: Path, names: list[str], dest: Path) -> list[str]:
    moved = []
    for name in names:
        src = run_dir / name
        if src.exists():
            dest.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest / name))
            moved.append(name)
    return moved


# --------------------------------------------------------------------------- #
# transcripts (hooks + backfill)
# --------------------------------------------------------------------------- #
def _projects_dir() -> Path:
    base = Path(os.environ.get("CLAUDE_CONFIG_DIR", Path.home() / ".claude"))
    return base / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(PROJECT_ROOT))


def _first_prompt(transcript: Path) -> str:
    try:
        with open(transcript) as fh:
            for line in fh:
                e = json.loads(line)
                if e.get("type") != "user":
                    continue
                c = e.get("message", {}).get("content", "")
                if isinstance(c, list):
                    c = " ".join(b.get("text", "") for b in c if isinstance(b, dict))
                return c
    except (OSError, json.JSONDecodeError):
        pass
    return ""


def _stage_from(agent_type: str, prompt: str) -> str | None:
    if agent_type in STAGES:
        return agent_type
    # analyse skill fallback: a general-purpose agent told to follow .claude/agents/value-x.md
    m = re.search(r"\.claude/agents/(value-(?:researcher|quant|skeptic))\.md", prompt)
    return m.group(1) if m else None


def _run_dir_from(prompt: str, cwd: str | None = None) -> Path | None:
    # The separator class must not include "/", or an absolute path loses its leading slash.
    m = re.search(r"RUN_DIR[\s:=*`'\"]{0,6}([^\s`'\"]*reports/runs/[^\s`'\"/]+)", prompt)
    if not m:
        return None
    p = Path(m.group(1))
    if not p.is_absolute():
        p = Path(cwd or PROJECT_ROOT) / p
    p = p.resolve()
    return p if p.parent == RUNS_DIR.resolve() and p.is_dir() else None


def _stamp(s: str) -> float:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


# --------------------------------------------------------------------------- #
# hooks
# --------------------------------------------------------------------------- #
def hook_subagent(payload: dict) -> int:
    """SubagentStop: record the hashes of the files the finishing stage owns."""
    transcript = Path(os.path.expanduser(payload.get("agent_transcript_path") or ""))
    prompt = _first_prompt(transcript) if transcript.is_file() else ""
    stage = _stage_from(payload.get("agent_type") or "", prompt)
    if not stage:
        return 0
    run_dir = _run_dir_from(prompt, payload.get("cwd"))
    if run_dir is None:
        print(f"[provenance] {stage} finished but no RUN_DIR found in its prompt; nothing recorded",
              file=sys.stderr)
        return 0
    for name in STAGE_FILES[stage]:
        path = run_dir / name
        if path.is_file():
            _append(run_dir, {"file": name, "sha256": sha256_file(path), "stage": stage,
                              "method": "hook", "agent_id": payload.get("agent_id"),
                              "session_id": payload.get("session_id")})
    return 0


def hook_lint(payload: dict) -> int:
    """PostToolUse(Bash): seal reports that report_lint.py passed inside a Claude Code session."""
    cmd = (payload.get("tool_input") or {}).get("command", "")
    if "report_lint.py" not in cmd:
        return 0
    resp = payload.get("tool_response")
    out = resp.get("stdout", "") if isinstance(resp, dict) else str(resp or "")
    _seal_from_lint_output(out, payload.get("cwd"), method="lint-seal",
                           extra={"session_id": payload.get("session_id")})
    return 0


def _seal_from_lint_output(out: str, cwd: str | None, *, method: str, extra: dict,
                           not_after: float | None = None, dry_run: bool = False) -> list[str]:
    sealed = []
    for m in re.finditer(r"^(\S+_report\.md)\s+\[(PASS|warn)\]", out, re.M):
        rep = Path(m.group(1))
        if not rep.is_absolute():
            rep = Path(cwd or PROJECT_ROOT) / rep
        rep = rep.resolve()
        run_dir = rep.parent
        if run_dir.parent != RUNS_DIR.resolve() or not rep.is_file():
            continue
        if not_after is not None and rep.stat().st_mtime > not_after:
            continue            # the report changed after that lint run
        if stage_problems(run_dir):
            continue            # never seal a report whose stage files aren't verified
        current = sha256_file(rep)
        records, _ = load_records(run_dir)
        if any(r.get("method") == "lint-seal" and r.get("sha256") == current for r in records):
            continue
        if not dry_run:
            _append(run_dir, {"file": rep.name, "sha256": current, "stage": "orchestrator",
                              "method": "lint-seal", "via": method, **extra})
        try:
            sealed.append(str(rep.relative_to(PROJECT_ROOT.resolve())))
        except ValueError:
            sealed.append(str(rep))
    return sealed


# --------------------------------------------------------------------------- #
# backfill: runs created before the hooks existed
# --------------------------------------------------------------------------- #
def backfill(dry_run: bool = False) -> dict:
    """Record provenance for pre-hook runs from Claude Code transcripts.

    A stage file is backfilled only if a subagent of the owning stage ran with that RUN_DIR
    (per its transcript and .meta.json) and the file has not been modified since that agent's
    last transcript entry. A report is sealed only if a Claude Code session ran report_lint.py
    on it, the lint passed, and the report hasn't changed since. Files written or restored by
    anything outside Claude Code fail both tests.
    """
    agents: dict[tuple[Path, str], list[float]] = {}
    pdir = _projects_dir()
    for jf in glob.glob(str(pdir / "*" / "subagents" / "agent-*.jsonl")):
        meta_path = Path(jf[:-len(".jsonl")] + ".meta.json")
        try:
            agent_type = json.loads(meta_path.read_text()).get("agentType", "")
        except (OSError, json.JSONDecodeError):
            continue
        prompt = _first_prompt(Path(jf))
        stage = _stage_from(agent_type, prompt)
        run_dir = _run_dir_from(prompt) if stage else None
        if not run_dir:
            continue
        stamps = []
        with open(jf) as fh:
            for line in fh:
                try:
                    ts = json.loads(line).get("timestamp")
                except json.JSONDecodeError:
                    continue
                if ts:
                    stamps.append(_stamp(ts))
        if stamps:
            agents.setdefault((run_dir, stage), []).append(max(stamps))

    report = {"recorded": [], "sealed": [], "skipped": []}
    for (run_dir, stage), ends in sorted(agents.items()):
        last_end = max(ends)
        records, _ = load_records(run_dir)
        for name in STAGE_FILES[stage]:
            path = run_dir / name
            if not path.is_file():
                continue
            rel = f"{run_dir.name}/{name}"
            if path.stat().st_mtime > last_end + BACKFILL_GRACE_S:
                report["skipped"].append(f"{rel} (modified after {stage} finished)")
                continue
            current = sha256_file(path)
            if any(r.get("file") == name and r.get("sha256") == current for r in records):
                continue
            if not dry_run:
                _append(run_dir, {"file": name, "sha256": current, "stage": stage,
                                  "method": "backfill", "agent_end": datetime.fromtimestamp(
                                      last_end, timezone.utc).isoformat(timespec="seconds")})
            report["recorded"].append(rel)

    # lint seals from main-session transcripts
    for jf in glob.glob(str(pdir / "*.jsonl")):
        calls: dict[str, str] = {}
        with open(jf) as fh:
            for line in fh:
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                content = e.get("message", {}).get("content")
                if not isinstance(content, list):
                    continue
                for b in content:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_use" and b.get("name") == "Bash" and \
                            "report_lint.py" in (b.get("input") or {}).get("command", ""):
                        calls[b.get("id")] = (b.get("input") or {}).get("command", "")
                    elif b.get("type") == "tool_result" and b.get("tool_use_id") in calls:
                        res = e.get("toolUseResult")
                        out = res.get("stdout", "") if isinstance(res, dict) else ""
                        if not out:
                            c = b.get("content")
                            out = c if isinstance(c, str) else " ".join(
                                x.get("text", "") for x in (c or []) if isinstance(x, dict))
                        cwd = e.get("cwd") or str(PROJECT_ROOT)
                        when = _stamp(e["timestamp"]) if e.get("timestamp") else None
                        report["sealed"] += _seal_from_lint_output(
                            out, cwd, method="backfill", extra={"session_id": e.get("sessionId")},
                            not_after=(when + 5) if when else None, dry_run=dry_run)
    return report


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, args = argv[1], argv[2:]
    if cmd in ("hook-subagent", "hook-lint"):
        try:
            payload = json.load(sys.stdin)
            return (hook_subagent if cmd == "hook-subagent" else hook_lint)(payload)
        except Exception as exc:            # a hook must never break the session
            print(f"[provenance] {cmd} failed: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 0
    if cmd == "verify":
        bad = 0
        for d in args or sorted(glob.glob(str(RUNS_DIR / "*"))):
            if not Path(d).is_dir():
                continue
            res, probs = verify_run(d), stage_problems(d)
            bad += bool(probs)
            print(f"{Path(d).name:<24} stages={'OK' if not probs else 'FAIL'}  report={res['report']}"
                  + (f"  bad_signatures={res['bad_signatures']}" if res["bad_signatures"] else ""))
            for p in probs:
                print(f"    {p}")
        return 1 if bad else 0
    if cmd in ("quarantine", "supersede"):
        where = "_external_unverified/" if cmd == "quarantine" else "_superseded/"
        for d in args:
            moved = (quarantine if cmd == "quarantine" else supersede)(d)
            print(f"{d}: " + (f"moved {', '.join(moved)} to {where}" if moved else "nothing to move"))
        return 0
    if cmd == "backfill":
        rep = backfill(dry_run="--dry-run" in args)
        for k in ("recorded", "sealed", "skipped"):
            print(f"{k}: {len(rep[k])}")
            for x in rep[k]:
                print(f"    {x}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
