"""Regression tests for the 14 Oct 2026 fixes: each test pins a failure that reached Telegram.

    python3 -m unittest discover -s tests -v

Hermetic: temp dirs, a temp signing key, fake vendor data. No network, no repo state.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "methodologies"))
sys.path.insert(0, str(ROOT))

import discover  # noqa: E402
import pipeline_store  # noqa: E402
import portfolio_ocr  # noqa: E402
import provenance  # noqa: E402
import report_lint  # noqa: E402
import screener  # noqa: E402
import telegram_notifier as tn  # noqa: E402


class OcrParsing(unittest.TestCase):
    """IBKR's pinned Instrument column hid the leading digits of fractional positions."""

    def parse(self, text):
        with mock.patch.object(portfolio_ocr, "_known_symbols", return_value={}):
            return {h["ticker"]: h for h in portfolio_ocr.parse_ibkr_text(text)}

    def test_truncated_fractional_positions_are_unknown_not_thousands(self):
        h = self.parse("VWRA LSEETF .1087\nVXUS NASDAQ.NMS.5925\nTSM NYSE\n2")
        self.assertIsNone(h["VWRA.L"]["shares"])
        self.assertIn("truncated", h["VWRA.L"]["shares_note"])
        self.assertIsNone(h["VXUS"]["shares"])
        self.assertEqual(h["TSM"]["shares"], 2)

    def test_next_line_quantity_keeps_decimals(self):
        self.assertEqual(self.parse("VOO ARCA\n12.5")["VOO"]["shares"], 12.5)
        self.assertEqual(self.parse("SAP IBIS\n1,250")["SAP.DE"]["shares"], 1250)

    def test_exchange_variants(self):
        h = self.parse("MDGL NASDAR.NMS\n10\nBRK B NYSE\n3\n0700 SEHK 100\nMC SBF\n8")
        self.assertEqual(h["MDGL"]["shares"], 10)
        self.assertEqual(h["BRK-B"]["shares"], 3)
        self.assertEqual(h["0700.HK"]["shares"], 100)
        self.assertEqual(h["MC.PA"]["shares"], 8)

    def test_pnl_line_is_not_a_share_count(self):
        h = self.parse("XYZ NYSE\n-69.59")
        self.assertIsNone(h["XYZ"]["shares"])

    def test_known_symbol_inside_text_is_not_a_holding(self):
        with mock.patch.object(portfolio_ocr, "_known_symbols", return_value={"TM": "TM", "MC": "MC.PA"}):
            held = {h["ticker"] for h in portfolio_ocr.parse_ibkr_text("Unrlzd P&L TM brand MC hammer")}
        self.assertEqual(held, set())


class VerdictBlock(unittest.TestCase):
    def check(self, **f):
        base = {"VERDICT": "HOLD", "PRICE": "100.00 USD", "FAIR_VALUE": "110.00 USD", "UPSIDE": "+10.0%",
                "ENTRY_BELOW": "88.00 USD", "EXIT_ABOVE": "143.00 USD"}
        base.update(f)
        return report_lint.check_verdict_block(base, "XYZ", is_fund=False, held={"XYZ"})

    def errors(self, issues):
        return [m for lvl, m in issues if lvl == "ERROR"]

    def test_parse_money(self):
        self.assertEqual(report_lint.parse_money("381.65 EUR"), (381.65, "EUR"))
        self.assertEqual(report_lint.parse_money("$45.40"), (45.40, "USD"))
        self.assertEqual(report_lint.parse_money("1443000 KRW"), (1443000.0, "KRW"))
        self.assertEqual(report_lint.parse_money("4194 GBp"), (41.94, "GBP"))
        self.assertIsNone(report_lint.parse_money("6.30%/yr base 10-yr net return"))

    def test_consistent_block_passes(self):
        self.assertEqual(self.errors(self.check()), [])

    def test_mixed_currencies_fail(self):
        # the old Telegram text compared a USD fair value with a EUR price
        self.assertTrue(self.errors(self.check(PRICE="384.05 EUR", FAIR_VALUE="372.41 USD")))

    def test_upside_must_match(self):
        self.assertTrue(self.errors(self.check(UPSIDE="+25.0%")))

    def test_verdict_must_fit_bands(self):
        self.assertTrue(self.errors(self.check(PRICE="150.00 USD", UPSIDE="-26.7%")))           # HOLD above exit
        self.assertTrue(self.errors(self.check(VERDICT="BUY", PRICE="105.00 USD", UPSIDE="+4.8%")))

    def test_fund_template_is_skipped(self):
        self.assertEqual(report_lint.check_verdict_block({"FAIR_VALUE": "6.30%/yr"}, "VWRA.L", is_fund=True), [])


class Provenance(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.runs = base / "reports" / "runs"
        self.run = self.runs / "ABC_2026-10-14"
        self.run.mkdir(parents=True)
        self.patches = [mock.patch.object(provenance, "RUNS_DIR", self.runs),
                        mock.patch.object(provenance, "PROJECT_ROOT", base),
                        mock.patch.object(provenance, "KEY_FILE", base / "key")]
        for p in self.patches:
            p.start()
        for name, stage in (("01_research.md", "researcher"), ("02_quant.md", "quant"), ("03_skeptic.md", "skeptic")):
            (self.run / name).write_text(f"<!-- pipeline:value-{stage} -->\nbody\n")
        (self.run / "02_model.py").write_text("print(1)\n")
        (self.run / "ABC_report.md").write_text("report\n")
        self.transcripts = base / "t"
        self.transcripts.mkdir()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def finish(self, stage):
        t = self.transcripts / f"{stage}.jsonl"
        t.write_text(json.dumps({"type": "user", "message": {"content": f"TICKER: ABC\nRUN_DIR: {self.run}/\n"}}) + "\n")
        provenance.hook_subagent({"agent_type": stage, "agent_transcript_path": str(t), "agent_id": stage})

    def test_hand_written_files_are_unrecorded_even_with_headers(self):
        self.assertTrue(provenance.stage_problems(self.run))

    def test_hook_records_make_stages_verified(self):
        for s in provenance.STAGES:
            self.finish(s)
        self.assertEqual(provenance.stage_problems(self.run), [])

    def test_editing_after_the_agent_finished_is_detected(self):
        for s in provenance.STAGES:
            self.finish(s)
        (self.run / "02_quant.md").write_text("<!-- pipeline:value-quant -->\nedited\n")
        self.assertEqual(provenance.verify_run(self.run)["files"]["02_quant.md"], "modified")

    def test_wrong_stage_cannot_vouch_for_a_file(self):
        self.finish("value-researcher")
        (self.run / "02_quant.md").write_text("<!-- pipeline:value-quant -->\nby researcher\n")
        provenance._append(self.run, {"file": "02_quant.md", "sha256": provenance.sha256_file(self.run / "02_quant.md"),
                                      "stage": "value-researcher", "method": "hook"})
        self.assertNotEqual(provenance.verify_run(self.run)["files"]["02_quant.md"], "verified")

    def test_forged_record_is_rejected(self):
        rec = {"v": 1, "file": "01_research.md", "stage": "value-researcher", "method": "hook",
               "sha256": provenance.sha256_file(self.run / "01_research.md"), "sig": "0" * 64}
        (self.run / provenance.RECORDS).write_text(json.dumps(rec) + "\n")
        self.assertEqual(provenance.verify_run(self.run)["files"]["01_research.md"], "bad-signature")

    def test_lint_seal_requires_verified_stages(self):
        out = f"\n{self.run}/ABC_report.md  [PASS]\n"
        provenance.hook_lint({"tool_input": {"command": "python3 report_lint.py x"}, "tool_response": {"stdout": out}})
        self.assertEqual(provenance.verify_run(self.run)["report"], "unsealed")
        for s in provenance.STAGES:
            self.finish(s)
        provenance.hook_lint({"tool_input": {"command": "python3 report_lint.py x"}, "tool_response": {"stdout": out}})
        self.assertEqual(provenance.verify_run(self.run)["report"], "sealed")

    def test_quarantine_moves_unverified_files(self):
        self.finish("value-researcher")
        moved = provenance.quarantine(self.run)
        self.assertIn("02_quant.md", moved)
        self.assertNotIn("01_research.md", moved)
        self.assertFalse((self.run / "02_quant.md").exists())


class TelegramDelivery(unittest.TestCase):
    def test_split_keeps_tags_whole(self):
        text = "\n".join(f"<b>row {i}</b> " + "x" * 90 for i in range(300))
        chunks = tn.split_message(text)
        self.assertTrue(all(len(c) <= tn.MAX_LEN for c in chunks))
        self.assertTrue(all(c.count("<b>") == c.count("</b>") for c in chunks))

    def test_verdict_guard(self):
        verified = pipeline_store.PipelineResult(ticker="NVO", status="VERIFIED", verdict="HOLD", as_of=date(2026, 10, 13))
        unverified = pipeline_store.PipelineResult(ticker="INSM", status="UNVERIFIED")
        lookup = {"NVO": verified, "INSM": unverified}
        with mock.patch.object(pipeline_store, "known_tickers", return_value={"NVO", "INSM"}), \
                mock.patch.object(pipeline_store, "latest", side_effect=lambda t, *a: lookup[t]), \
                mock.patch.object(tn, "PROJECT_ROOT", Path(tempfile.gettempdir())):
            self.assertEqual(tn.verdict_guard("NVO HOLD. INSM needs /analyse."), [])
            self.assertTrue(tn.verdict_guard("INSM: TRIM, fair value $28.78"))
            self.assertTrue(tn.verdict_guard("NVO is a BUY"))
            self.assertEqual(tn.verdict_guard("you hold 210 NVO shares"), [])

    def test_unverified_card_shows_no_verdict(self):
        res = pipeline_store.PipelineResult(ticker="INSM", status="UNVERIFIED", verdict="TRIM",
                                            problems=["provenance: 01_research.md: no provenance record: x"],
                                            skipped_runs=["INSM_2026-10-14"])
        card = tn.format_verdict_card(res)
        self.assertNotIn("TRIM", card)
        self.assertIn("/analyse INSM", card)


class Screener(unittest.TestCase):
    def screen(self, preset, **info):
        base = {"currentPrice": 100.0, "currency": "USD", "country": "United Kingdom", "sector": "Industrials",
                "fiftyTwoWeekHigh": 120.0, "marketCap": 1e10, "trailingPE": 15.0, "forwardPE": 12.0,
                "grossMargins": 0.5, "operatingMargins": 0.2, "returnOnEquity": 0.2, "returnOnAssets": 0.1,
                "earningsGrowth": 0.15, "dividendYield": 4.0, "totalCash": 1e9, "totalDebt": 2e9,
                "sharesOutstanding": 1e8, "ebitda": 1e9}
        base.update(info)
        fake = mock.Mock(info=base)
        with mock.patch.object(screener.yf, "Ticker", return_value=fake), \
                mock.patch.object(screener, "fx_to_usd", return_value=1.0):
            return screener.fetch_and_screen_ticker("XYZ.L", preset)

    def test_dividend_yield_is_a_percent(self):
        self.assertAlmostEqual(self.screen("SINGAPORE_INCOME", dividendYield=0.15).dividend_yield_pct, 0.15)
        self.assertFalse(self.screen("SINGAPORE_INCOME", dividendYield=0.15).qualifies)

    def test_growth_and_roe_scaling(self):
        r = self.screen("LYNCH_GARP", earningsGrowth=2.94, returnOnEquity=1.5)
        self.assertAlmostEqual(r.eps_growth_pct, 294.0)
        self.assertIsNone(r.lynch_ratio)                      # one-off spike: no Lynch ratio
        self.assertTrue(any("one-off" in f for f in r.flags))
        self.assertGreater(self.screen("BUFFETT_MOAT", returnOnEquity=1.5).roic_proxy_pct, 50)

    def test_lynch_ratio_threshold(self):
        self.assertFalse(self.screen("LYNCH_GARP", earningsGrowth=0.02, dividendYield=0.5).qualifies)
        self.assertTrue(self.screen("LYNCH_GARP", earningsGrowth=0.15, dividendYield=4.0).qualifies)

    def test_why_text_uses_live_figures_only(self):
        r = self.screen("SINGAPORE_INCOME")
        self.assertIn("yield 4.0%", r.why)


class Discover(unittest.TestCase):
    def test_empty_screen_returns_a_result_and_never_says_deploy(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(discover, "DISCOVERY_DIR", Path(d)), \
                mock.patch.object(discover, "PROJECT_ROOT", Path(d)), \
                mock.patch.object(discover.screener, "run_screen", return_value=[]):
            res = discover.run_discovery_pipeline("BUFFETT_MOAT", universe="EURO_COMPOUNDERS")
            self.assertEqual(res["candidates"], [])
            text = Path(d, res["run_dir"], "01_scout_report.md").read_text()
            for word in ("DEPLOY", "Top-Up", "BUY", "ACCUMULATE"):
                self.assertNotIn(word, text)


class PriceBands(unittest.TestCase):
    def test_band_crossing_asks_for_a_rerun_without_recomputing_the_verdict(self):
        res = pipeline_store.PipelineResult(ticker="X", status="VERIFIED", verdict="HOLD", price=100.0, currency="USD",
                                            fair_value=110.0, entry_below=88.0, exit_above=143.0,
                                            as_of=datetime.now(timezone.utc).date())
        quote = pipeline_store.Quote(price=85.0, currency="USD", fetched_at="now")
        chk = pipeline_store.price_check(res, quote)
        self.assertEqual(chk.band_now, "at or below ENTRY_BELOW")
        self.assertTrue(chk.refresh_reasons)
        self.assertEqual(res.verdict, "HOLD")


class TelegramApp(unittest.TestCase):
    def test_ticker_validation_blocks_shell_text(self):
        import telegram_app
        self.assertTrue(telegram_app.TICKER_RE.fullmatch("BATS.L"))
        self.assertTrue(telegram_app.TICKER_RE.fullmatch("000660.KS"))
        self.assertIsNone(telegram_app.TICKER_RE.fullmatch("$(RM"))


if __name__ == "__main__":
    unittest.main()
