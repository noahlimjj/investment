"""Gemini LLM Multi-Agent Real-Time Analysis Engine.

Powers the 3-Agent Value Investing pipeline (Researcher -> Quant -> Skeptic)
and multimodal IBKR screenshot vision using Gemini 2.5 Flash.

Requires:
  GEMINI_API_KEY in .env or environment
"""
from __future__ import annotations

import base64
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

def get_gemini_api_key() -> str | None:
    """Retrieve GEMINI_API_KEY from environment or .env."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key and ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line.startswith("GEMINI_API_KEY="):
                key = line.split("=", 1)[1].strip().strip("\"'")
                break
    return key

def call_gemini(
    prompt: str,
    system_instruction: str = "",
    image_path: Path | None = None,
    model: str = "gemini-2.5-flash",
    temperature: float = 0.2
) -> str:
    """Execute a real-time call to the Google Gemini API."""
    api_key = get_gemini_api_key()
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured. Add GEMINI_API_KEY to your .env file.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    parts: list[dict[str, Any]] = []

    # If image attached, add inlineData
    if image_path and image_path.exists():
        mime_type = "image/png"
        if image_path.suffix.lower() in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        elif image_path.suffix.lower() == ".webp":
            mime_type = "image/webp"

        img_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        parts.append({
            "inlineData": {
                "mimeType": mime_type,
                "data": img_b64
            }
        })

    parts.append({"text": prompt})

    payload: dict[str, Any] = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": 4096
        }
    }

    if system_instruction:
        payload["systemInstruction"] = {
            "parts": [{"text": system_instruction}]
        }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode())
        candidates = result.get("candidates", [])
        if not candidates:
            raise RuntimeError(f"Gemini returned no candidates: {result}")
        content = candidates[0].get("content", {})
        text_parts = [p.get("text", "") for p in content.get("parts", [])]
        return "\n".join(text_parts).strip()

def gemini_parse_ibkr_screenshot(image_path: Path) -> list[dict[str, Any]]:
    """Use Gemini Multimodal Vision to extract portfolio holdings from IBKR screenshot."""
    prompt = (
        "You are a financial OCR specialist. Inspect this Interactive Brokers (IBKR) portfolio screenshot.\n"
        "Extract every stock and ETF position from the table.\n"
        "Map each instrument to its proper Yahoo Finance ticker symbol:\n"
        "- US listings (NYSE, NASDAQ): standard ticker (e.g., TSM, ZBH, SYK, LAD, BABA, TM, PRAX, INCY, CELC, MDGL, INSM, ACAD, NVO)\n"
        "- UK / London listings (LSE, LSEETF): append .L (e.g., VWRA -> VWRA.L, BATS -> BATS.L)\n"
        "- Euronext Paris (SBF, PAR): append .PA (e.g., MC -> MC.PA, BN -> BN.PA)\n"
        "- Korea Exchange (KRX): append .KS (e.g., 000660 -> 000660.KS, 402340 -> 402340.KS)\n"
        "- Tokyo Stock Exchange (TSEJ): append .T (e.g., 7974 -> 7974.T, 4063 -> 4063.T)\n"
        "- Singapore Exchange (SGX): append .SI (e.g., D05 -> D05.SI)\n\n"
        "Return ONLY a valid JSON array of objects with these keys:\n"
        "[\n"
        "  {\"ticker\": \"TSM\", \"name\": \"Taiwan Semiconductor\", \"shares\": 2, \"unrealized_pnl_pct\": 9.33},\n"
        "  ...\n"
        "]\n"
        "Do NOT wrap in markdown backticks. Return raw JSON."
    )
    raw = call_gemini(prompt, system_instruction="You extract financial portfolio data accurately as raw JSON.", image_path=image_path)
    clean_json = raw.strip()
    if clean_json.startswith("```json"):
        clean_json = clean_json[7:]
    if clean_json.startswith("```"):
        clean_json = clean_json[3:]
    if clean_json.endswith("```"):
        clean_json = clean_json[:-3]
    return json.loads(clean_json.strip())

def run_realtime_3agent_deepdive(ticker: str, data_summary: dict[str, Any]) -> dict[str, Any]:
    """Execute the full 3-Agent value investing debate in real-time using Gemini."""
    
    # -------------------------------------------------------------------------
    # AGENT 1: VALUE RESEARCHER
    # -------------------------------------------------------------------------
    researcher_sys = (
        "You are the Value Researcher agent in an institutional value investing pipeline. "
        "Your task is to analyze business model quality, Warren Buffett moat durability, pricing power, "
        "and capital allocation history using empirical data. Be objective, rigorous, and cite numbers."
    )
    researcher_prompt = f"""
Analyze the target company: {ticker}
Financial Data Snapshot:
{json.dumps(data_summary, indent=2)}

Provide:
1. Business Model & Core Revenue Drivers
2. Economic Moat Rating (Wide / Narrow / None) and evidence (gross margin stability, ROIC vs WACC)
3. Peter Lynch Classification (Fast Grower, Stalwart, Slow Grower, Cyclical, Turnaround, Asset Play)
4. Capital Allocation Score (A to F) based on buyback timing, debt discipline, and M&A track record.
"""
    research_output = call_gemini(researcher_prompt, system_instruction=researcher_sys)

    # -------------------------------------------------------------------------
    # AGENT 2: VALUE QUANT
    # -------------------------------------------------------------------------
    quant_sys = (
        "You are the Value Quant agent. Your task is to calculate intrinsic valuation, "
        "run reverse DCF to determine what growth the current price discounts, and establish Bear/Base/Bull scenarios."
    )
    quant_prompt = f"""
Target: {ticker}
Researcher Dossier:
{research_output}

Financial Data:
{json.dumps(data_summary, indent=2)}

Provide:
1. Intrinsic Fair Value estimate and Margin of Safety (%)
2. Reverse DCF Analysis: What revenue/earnings growth rate is already priced in by the current tape? Is it realistic?
3. Scenario Matrix: Bear Value ($ / prob %), Base Value ($ / prob %), Bull Value ($ / prob %)
4. SBC-adjusted Owner Earnings yield and EV/EBITDA fair multiple range.
"""
    quant_output = call_gemini(quant_prompt, system_instruction=quant_sys)

    # -------------------------------------------------------------------------
    # AGENT 3: VALUE SKEPTIC (Devil's Advocate Pre-Mortem)
    # -------------------------------------------------------------------------
    skeptic_sys = (
        "You are the Value Skeptic — an adversarial institutional risk manager and devil's advocate. "
        "Your sole job is to destroy the bullish thesis, detect value traps, and conduct an independent Pre-Mortem. "
        "You evaluate specifically for a Singapore Tax Resident (0% CGT, 30% US dividend WHT, 26 USC §2104 US estate tax)."
    )
    skeptic_prompt = f"""
Target: {ticker}
Quant Valuation:
{quant_output}

Financial Data:
{json.dumps(data_summary, indent=2)}

Provide:
1. Blind Pre-Mortem: What is the single most likely structural reason this company is worth 50%+ less in 5 years?
2. Value Trap Check: Are peak margins masquerading as low P/E? Is debt refinancing a wall?
3. Singapore Tax Efficiency: Assess 30% US dividend withholding tax drag and US estate tax situs risks.
4. Final Closed-Vocabulary Verdict: Exactly ONE of [BUY, ACCUMULATE, HOLD, TRIM, SELL, PASS] with Conviction [LOW, MEDIUM, HIGH].
5. Key Downside Risk (one punchy sentence).
"""
    skeptic_output = call_gemini(skeptic_prompt, system_instruction=skeptic_sys)

    return {
        "ticker": ticker,
        "research": research_output,
        "quant": quant_output,
        "skeptic": skeptic_output
    }
