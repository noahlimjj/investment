"""Telegram delivery for the value-investing pipeline.

Everything with a verdict or a valuation number in it is formatted here from verified pipeline
data (pipeline_store): never typed by an agent into a shell string, never hard-coded.

Why it was rewritten (14 Oct 2026): the portfolio dossier was ~70 lines of fixed text (prices,
"€" labels on USD values, an "11 HOLDINGS" trim list) sent whatever the data said; discovery
cards said "DEPLOY CAPITAL" for screen hits the pipeline had rated PASS; messages were cut every
4000 characters, sometimes inside an HTML tag, and the failed chunk was dropped; and replies sent
as `--msg "<text>"` lost every "$4" in "$45.40" to shell expansion.

Usage:
  python3 methodologies/telegram_notifier.py --test
  python3 methodologies/telegram_notifier.py --verdict NVO          # verified card, or why there's none
  python3 methodologies/telegram_notifier.py --portfolio            # audit from verified runs
  python3 methodologies/telegram_notifier.py --report reports/discovery/MASTER_OPPORTUNITIES_<DATE>.md
  python3 methodologies/telegram_notifier.py --file <path> --caption "..."
  python3 methodologies/telegram_notifier.py --msg-file - <<'EOF'      # free text: quoted heredoc
  <text>
  EOF

Free text goes through a guard: a message that pairs a known ticker with a verdict word
(BUY/ACCUMULATE/HOLD/TRIM/SELL/PASS) is refused unless it matches that ticker's verified run.
Don't use --msg "<text>" for anything containing $ or backticks.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
MAX_LEN = 3900                     # Telegram allows 4096; leave room for entities
CAPTION_MAX = 1000                 # Telegram allows 1024
VERDICT_WORDS = ("BUY", "ACCUMULATE", "HOLD", "TRIM", "SELL", "PASS")
esc = lambda x: html.escape(str(x), quote=False)  # noqa: E731


# --------------------------------------------------------------------------- #
# credentials and transport
# --------------------------------------------------------------------------- #
def load_env() -> dict[str, str]:
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip("\"'")
    return env


def get_credentials() -> tuple[str | None, str | None]:
    env = load_env()
    return (os.environ.get("TELEGRAM_BOT_TOKEN") or env.get("TELEGRAM_BOT_TOKEN"),
            os.environ.get("TELEGRAM_CHAT_ID") or env.get("TELEGRAM_CHAT_ID"))


def _resolve(token: str | None, chat_id: str | int | None) -> tuple[str | None, str | None]:
    t, c = get_credentials()
    return token or t, str(chat_id) if chat_id is not None else c


def _api(token: str, method: str, data: bytes, content_type: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/{method}", data=data,
                                 headers={"Content-Type": content_type})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:          # Telegram puts the reason in the body
        try:
            return json.loads(exc.read().decode())
        except Exception:
            return {"ok": False, "description": f"HTTP {exc.code}"}


def html_to_plain(text: str) -> str:
    return html.unescape(re.sub(r"</?[a-zA-Z][^>]*>", "", text))


def split_message(text: str, limit: int = MAX_LEN) -> list[str]:
    """Split on line boundaries so no HTML tag is cut in half (only a single line longer than
    the limit is split mid-line, at a space)."""
    chunks, cur = [], ""
    for line in text.split("\n"):
        while len(line) > limit:
            cut = line.rfind(" ", 0, limit)
            cut = cut if cut > limit // 2 else limit
            if cur:
                chunks.append(cur)
                cur = ""
            chunks.append(line[:cut])
            line = line[cut:].lstrip()
        if cur and len(cur) + 1 + len(line) > limit:
            chunks.append(cur)
            cur = line
        else:
            cur = f"{cur}\n{line}" if cur else line
    if cur.strip():
        chunks.append(cur)
    return chunks


def send_telegram_message(text: str, parse_mode: str | None = "HTML",
                          disable_web_page_preview: bool = True, *,
                          token: str | None = None, chat_id: str | int | None = None,
                          reply_markup: dict | None = None) -> bool:
    """Send text, split on line boundaries. A chunk Telegram can't parse as HTML is re-sent as
    plain text rather than lost. `reply_markup` goes on the last chunk."""
    token, chat_id = _resolve(token, chat_id)
    if not token or not chat_id:
        print("[telegram warning] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not configured.")
        return False
    ok_all = True
    chunks = split_message(text)
    for n, chunk in enumerate(chunks):
        payload = {"chat_id": chat_id, "text": chunk, "disable_web_page_preview": disable_web_page_preview}
        if reply_markup and n == len(chunks) - 1:
            payload["reply_markup"] = reply_markup
        if parse_mode:
            payload["parse_mode"] = parse_mode
        res = _api(token, "sendMessage", json.dumps(payload).encode(), "application/json")
        if not res.get("ok") and parse_mode and "parse" in str(res.get("description", "")).lower():
            payload.pop("parse_mode")
            payload["text"] = html_to_plain(chunk)
            res = _api(token, "sendMessage", json.dumps(payload).encode(), "application/json")
        if not res.get("ok"):
            print(f"[telegram error] sendMessage failed: {res.get('description')}")
            ok_all = False
    return ok_all


def send_telegram_document(file_path: Path, caption: str = "", *, token: str | None = None,
                           chat_id: str | int | None = None) -> bool:
    token, chat_id = _resolve(token, chat_id)
    if not token or not chat_id:
        print("[telegram warning] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not configured.")
        return False
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"[telegram error] File not found: {file_path}")
        return False
    boundary = "----ValuePipelineBoundary7MA4YWxkTrZu0gW"
    filename = re.sub(r'["\r\n]', "_", file_path.name)
    body = bytearray()
    for name, value in (("chat_id", str(chat_id)), ("caption", caption[:CAPTION_MAX])):
        if value:
            body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n"
                     f"{value}\r\n").encode()
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"document\"; "
             f"filename=\"{filename}\"\r\nContent-Type: application/octet-stream\r\n\r\n").encode()
    body += file_path.read_bytes() + f"\r\n--{boundary}--\r\n".encode()
    res = _api(token, "sendDocument", bytes(body), f"multipart/form-data; boundary={boundary}", timeout=60)
    if not res.get("ok"):
        print(f"[telegram error] sendDocument failed: {res.get('description')}")
    return bool(res.get("ok"))


# --------------------------------------------------------------------------- #
# verified cards
# --------------------------------------------------------------------------- #
def summarise_problems(problems: list[str]) -> list[str]:
    """Collapse the per-file provenance errors into one line; keep everything else as is."""
    prov = [m.group(1) for p in problems if (m := re.match(r"provenance: (\S+): no provenance record", p))]
    rest = [p for p in problems if not re.match(r"provenance: \S+: no provenance record", p)]
    if prov:
        rest.insert(0, f"no provenance record for {', '.join(prov)}: not written by the pipeline's agents")
    return rest

def format_verdict_card(res, check=None) -> str:
    """HTML card for one ticker from pipeline_store data. Unverified runs get the reasons, not
    their verdict."""
    from portfolio_analyser import ev_text, fmt_amount, fmt_pct
    if not res.verified:
        lines = [f"❔ <b>{esc(res.ticker)}: no verified pipeline verdict</b>"]
        if res.skipped_runs:
            lines.append(f"Run(s) {esc(', '.join(res.skipped_runs))} failed verification, so nothing "
                         "from them is shown:")
        lines += [f"• {esc(p)}" for p in summarise_problems(res.problems)[:4]]
        lines.append(f"Send <code>/analyse {esc(res.ticker)}</code> to run the 3-agent pipeline.")
        return "\n".join(lines)
    age = f"{res.age_days} day{'s' if res.age_days != 1 else ''} old" if res.age_days is not None else "age unknown"
    lines = [f"🎯 <b>{esc(res.ticker)}: {esc(res.name or '')}</b>",
             f"<b>Verdict: {esc(res.verdict)}</b> ({esc(res.conviction)} conviction) · verified run "
             f"{esc(res.as_of)} ({age})"]
    if res.is_fund:
        lines.append(f"Run price {esc(fmt_amount(res.price, res.currency))} · expected return: "
                     f"{esc(res.fair_value_text)}")
    else:
        lines.append(f"Run price {esc(fmt_amount(res.price, res.currency))} · EV "
                     f"{esc(ev_text(res))} ({esc(fmt_pct(res.upside_pct))})")
        lines.append(f"Entry below {esc(fmt_amount(res.entry_below, res.currency))} · exit above "
                     f"{esc(fmt_amount(res.exit_above, res.currency))}")
    if check and check.quote:
        q = check.quote
        live = f"Live {esc(fmt_amount(q.price, q.currency))}"
        if check.change_pct is not None:
            live += f" ({esc(fmt_pct(check.change_pct))} since the run)"
        if check.upside_now_pct is not None:
            live += f" · EV vs live {esc(fmt_pct(check.upside_now_pct))}"
        if check.band_now:
            live += f" · {esc(check.band_now)}"
        lines.append(live)
    if check and check.refresh_reasons:
        lines.append("⚠️ <b>Re-run advised:</b> " + esc("; ".join(check.refresh_reasons))
                     + f" (<code>/analyse {esc(res.ticker)} fresh</code>)")
    if res.key_risk:
        lines.append(f"<b>Key risk:</b> {esc(res.key_risk)}")
    if res.bear_thesis:
        lines.append(f"<b>Bear thesis:</b> <i>{esc(res.bear_thesis)}</i>")
    lines.append(f"📄 <code>{esc(res.report_path.relative_to(PROJECT_ROOT))}</code>")
    return "\n".join(lines)


def verdict_message(ticker: str, live: bool = True) -> tuple[str, Path | None]:
    import pipeline_store
    res = pipeline_store.latest(ticker)
    check = pipeline_store.price_check(res, pipeline_store.live_quote(ticker) if live else None) \
        if res.verified else None
    return format_verdict_card(res, check), (res.report_path if res.verified else None)


def format_portfolio_messages(audit) -> list[str]:
    from portfolio_analyser import VERDICT_ORDER, ev_text, fmt_amount, fmt_pct
    groups = audit.by_verdict()
    snap = audit.snapshot
    head = [f"📊 <b>Portfolio audit ({esc(audit.generated[:10])})</b>",
            "<i>Verified 3-agent pipeline runs only (lint + provenance + seal). Holdings snapshot "
            f"{esc(snap.get('source_file') or 'UNKNOWN')}.</i>",
            f"Holdings {len(audit.rows)} · verified verdicts {len(audit.verified)} · "
            f"need /analyse {len(audit.unverified)}"]
    icons = {"SELL": "🔴", "TRIM": "🟠", "HOLD": "🟡", "PASS": "⚪️", "ACCUMULATE": "🟢", "BUY": "🟢"}
    for v in VERDICT_ORDER:
        if v in groups:
            head.append(f"{icons[v]} <b>{v}</b> ({len(groups[v])}): "
                        + ", ".join(f"<code>{esc(t)}</code>" for t in groups[v]))
    if audit.unverified:
        head.append("❔ <b>No verified verdict</b> (" + str(len(audit.unverified)) + "): "
                    + ", ".join(f"<code>{esc(r.ticker)}</code>" for r in audit.unverified))
    if audit.refresh:
        head.append("⚠️ <b>Re-run advised</b>: " + ", ".join(f"<code>{esc(r.ticker)}</code>" for r in audit.refresh))
    msgs = ["\n".join(head)]

    body = ["<b>Verified verdicts</b> (run price → live · EV · EV vs live)"]
    for r in sorted(audit.verified, key=lambda r: VERDICT_ORDER.index(r.result.verdict)
                    if r.result.verdict in VERDICT_ORDER else 9):
        res, chk = r.result, r.check
        live = f" → {fmt_amount(chk.quote.price, chk.quote.currency)}" if chk and chk.quote else ""
        line = (f"• <b>{esc(r.ticker)}</b> {esc(res.verdict)} ({esc(res.conviction)}) · {esc(res.as_of)} · "
                f"{esc(fmt_amount(res.price, res.currency))}{esc(live)} · EV {esc(ev_text(res))}")
        if chk and chk.upside_now_pct is not None:
            line += f" ({esc(fmt_pct(chk.upside_now_pct))})"
        if chk and chk.band_now:
            line += f" · {esc(chk.band_now)}"
        body.append(line)
        if chk and chk.refresh_reasons:
            body.append(f"   ⚠️ {esc('; '.join(chk.refresh_reasons))}")
    msgs.append("\n".join(body))

    if audit.unverified:
        lines = ["<b>No verified verdict: run /analyse</b>"]
        for r in audit.unverified:
            why = (summarise_problems(r.result.problems) or ["no pipeline run on file"])[0]
            lines.append(f"• <b>{esc(r.ticker)}</b>: {esc(why)}")
        msgs.append("\n".join(lines))
    notes = [f"• <b>{esc(r.ticker)}</b>: {esc(r.shares_note)}" for r in audit.rows if r.shares_note]
    if notes:
        msgs.append("<b>Data notes</b>\n" + "\n".join(notes))
    return msgs


def send_portfolio_telegram_dossier(report_file: Path | None = None, *, live: bool = True,
                                    token: str | None = None, chat_id: str | int | None = None) -> bool:
    """Rebuild the audit from verified runs, send the summary, attach the markdown report."""
    import portfolio_analyser
    audit = portfolio_analyser.build_audit(live=live)
    report_file = Path(report_file) if report_file else portfolio_analyser.write_report(audit)
    ok = all([send_telegram_message(m, token=token, chat_id=chat_id) for m in format_portfolio_messages(audit)])
    return send_telegram_document(report_file, caption=f"Portfolio audit {audit.generated[:10]} (verified runs only)",
                                  token=token, chat_id=chat_id) and ok


# --------------------------------------------------------------------------- #
# discovery
# --------------------------------------------------------------------------- #
def format_discovery_messages(data: dict) -> list[str]:
    msgs = [f"🔍 <b>Opportunity screen ({esc(data.get('as_of', '')[:10])})</b>\n"
            "<i>Screen results from quantitative filters on vendor data, not recommendations. A "
            "buy/hold/sell view only comes from the 3-agent pipeline: /analyse TICKER.</i>"]
    for p in data.get("presets", []):
        lines = [f"<b>{esc(p['preset'])}</b> on {esc(p['universe'])}: {p.get('qualified', 0)} of "
                 f"{p.get('screened', 0)} passed" + (f", {len(p.get('failures', []))} failed to fetch"
                                                     if p.get("failures") else "")]
        for c in p.get("candidates", [])[:3]:
            lines.append(_candidate_line(c))
        if not p.get("candidates"):
            lines.append("• no new candidates passed")
        msgs.append("\n".join(lines))
    held = [c for p in data.get("presets", []) for c in p.get("held_hits", [])]
    analysed = [c for p in data.get("presets", []) for c in p.get("analysed", [])]
    if held or analysed:
        lines = ["<b>Screen hits that already have a pipeline view or are held</b>"]
        seen = set()
        for c in held + analysed:
            if c["ticker"] in seen:
                continue
            seen.add(c["ticker"])
            lines.append(_candidate_line(c, short=True))
        msgs.append("\n".join(lines))
    return msgs


def _candidate_line(c: dict, short: bool = False) -> str:
    pipe = c.get("pipeline") or {}
    if pipe.get("status") == "VERIFIED":
        view = (f"pipeline: <b>{esc(pipe['verdict'])}</b> ({esc(pipe.get('conviction'))}, "
                f"{esc(pipe.get('as_of'))}), EV {esc(pipe.get('fair_value_text'))}")
    else:
        view = f"no verified verdict → <code>/analyse {esc(c['ticker'])}</code>"
    held = " · <i>held</i>" if c.get("held") else ""
    if short:
        return f"• <b>{esc(c['ticker'])}</b> {esc(c.get('name', ''))}{held}: {view}"
    return (f"• <b>{esc(c['ticker'])}</b> {esc(c.get('name', ''))} ({esc(c.get('country', ''))}){held}\n"
            f"   {esc(c.get('metrics', ''))}\n"
            f"   Screened on: {esc(c.get('why', ''))}\n"
            + (f"   Flags: {esc('; '.join(c.get('flags', [])))}\n" if c.get("flags") else "")
            + f"   {view}")


def send_discovery_telegram_dossier(master_file: Path, *, token: str | None = None,
                                    chat_id: str | int | None = None) -> bool:
    master_file = Path(master_file)
    sidecar = master_file.with_suffix(".json")
    if not sidecar.exists():
        print(f"[telegram error] {sidecar.name} missing: re-run methodologies/discover.py --all")
        return False
    data = json.loads(sidecar.read_text())
    ok = all([send_telegram_message(m, token=token, chat_id=chat_id) for m in format_discovery_messages(data)])
    return send_telegram_document(master_file, caption="Opportunity screen (candidates for /analyse, "
                                  "not recommendations)", token=token, chat_id=chat_id) and ok


# --------------------------------------------------------------------------- #
# guard for agent-written free text
# --------------------------------------------------------------------------- #
def verdict_guard(text: str) -> list[str]:
    """Problems with verdict claims in free text. A known ticker next to a verdict word must
    match that ticker's verified run; anything else is a claim the pipeline didn't make."""
    import pipeline_store
    known = pipeline_store.known_tickers()
    try:
        known |= set(json.loads((PROJECT_ROOT / "data" / "portfolio.json").read_text()).get("tickers", []))
    except (OSError, json.JSONDecodeError):
        pass
    problems, claims = [], {}
    for line in html_to_plain(text).splitlines():
        mentions = []                                   # (start, end, ticker), longest match wins
        for t in sorted(known, key=len, reverse=True):
            for m in re.finditer(rf"(?<![A-Za-z0-9.]){re.escape(t)}(?![A-Za-z0-9])", line):
                if not any(s <= m.start() < e for s, e, _ in mentions):
                    mentions.append((m.start(), m.end(), t))
        if not mentions:
            continue
        for v in re.finditer(rf"\b({'|'.join(VERDICT_WORDS)})\b", line):
            dist, t = min((min(abs(v.start() - e), abs(s - v.end())), t) for s, e, t in mentions)
            if dist <= 40:                              # a verdict word belongs to its nearest ticker
                claims.setdefault(t, set()).add(v.group(1))
    for t, claimed in sorted(claims.items()):
        res = pipeline_store.latest(t)
        if not res.verified:
            problems.append(f"{t}: text states {'/'.join(sorted(claimed))} but {t} has no verified pipeline verdict")
        elif res.verdict not in claimed:
            problems.append(f"{t}: text states {'/'.join(sorted(claimed))} but the verified run "
                            f"({res.as_of}) says {res.verdict}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Telegram delivery for verified pipeline output")
    parser.add_argument("--test", action="store_true", help="test the bot connection")
    parser.add_argument("--msg", type=str, help="free text (unsafe in double quotes: prefer --msg-file -)")
    parser.add_argument("--msg-file", type=str, help="free text from a file, or - for stdin")
    parser.add_argument("--verdict", type=str, metavar="TICKER", help="send the verified card for a ticker")
    parser.add_argument("--portfolio", nargs="?", const="", default=None,
                        help="send the portfolio audit (optionally attach an existing report)")
    parser.add_argument("--report", type=str, help="send a discovery master file (needs its .json sidecar)")
    parser.add_argument("--file", type=str, help="send a file attachment")
    parser.add_argument("--caption", type=str, default="")
    parser.add_argument("--no-live", action="store_true", help="skip live prices")
    args = parser.parse_args()

    token, chat_id = get_credentials()
    if not token or not chat_id:
        print("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env (see COMMANDS.md).")
        return 2
    if args.test:
        return 0 if send_telegram_message("✅ <b>Value pipeline bot connected.</b>") else 1
    if args.verdict:
        card, report = verdict_message(args.verdict.strip().upper(), live=not args.no_live)
        ok = send_telegram_message(card)
        if report:
            ok = send_telegram_document(report, caption=f"{args.verdict.upper()} verified pipeline report") and ok
        return 0 if ok else 1
    if args.portfolio is not None:
        return 0 if send_portfolio_telegram_dossier(Path(args.portfolio) if args.portfolio else None,
                                                    live=not args.no_live) else 1
    if args.report:
        return 0 if send_discovery_telegram_dossier(Path(args.report)) else 1
    if args.file:
        return 0 if send_telegram_document(Path(args.file), caption=args.caption) else 1
    if args.msg is not None or args.msg_file:
        text = args.msg if args.msg is not None else (
            sys.stdin.read() if args.msg_file == "-" else Path(args.msg_file).read_text())
        problems = verdict_guard(text)
        if problems:
            print("[telegram guard] NOT SENT: the message states verdicts the verified pipeline didn't make:",
                  file=sys.stderr)
            for p in problems:
                print(f"  - {p}", file=sys.stderr)
            print("Use --verdict TICKER for verified figures, or /analyse TICKER to run the pipeline.",
                  file=sys.stderr)
            return 3
        return 0 if send_telegram_message(text) else 1
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
