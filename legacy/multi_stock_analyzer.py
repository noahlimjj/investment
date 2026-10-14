import sys
import os
import asyncio
import json
from typing import List
from google.antigravity import Agent, LocalAgentConfig

# Add current directory to path so methodologies can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from methodologies.valuation import dcf, reverse_dcf, peg_is_valid, fcf_yield

def get_stock_data(ticker: str) -> str:
    """Fetches validated fundamentals for a ticker from the local data layer."""
    path = os.path.join(os.path.dirname(__file__), "data", "fundamentals.json")
    if not os.path.exists(path):
        return ("ERROR: data/fundamentals.json missing. Run "
                "`python3 methodologies/fundamentals.py --universe` first. "
                "Do not proceed from memory.")
    with open(path) as fh:
        payload = json.load(fh)
    rec = payload.get("records", {}).get(ticker)
    if rec is None:
        return f"ERROR: {ticker} not in the validated data file. Do not invent figures."

    if rec.get("errors"):
        return (f"BLOCKED: {ticker} has unresolved data errors: {rec['errors']}. "
                "Per RULE 1, do not write a report.")

    def fmt(v, pct=False, money=False):
        if v is None:
            return "UNKNOWN (missing - not zero)"
        if pct:
            return f"{v:.2%}"
        if money:
            return f"${v/1e9:,.2f}B"
        return f"{v:,.4g}"

    out = [f"--- VALIDATED DATA for {ticker} (as_of {rec['as_of']}) ---",
           f"Name: {rec.get('name')}",
           f"Type: {rec.get('quote_type')}   Sector: {rec.get('sector')}",
           f"Quote ccy: {rec.get('quote_currency')}  Financial ccy: {rec.get('financial_currency')}",
           f"Price: {fmt(rec.get('price'))} {rec.get('quote_currency')}  "
           f"(= {fmt(rec.get('price_usd'))} USD)",
           f"Market cap: {fmt(rec.get('market_cap_usd'), money=True)}",
           f"Trailing P/E: {fmt(rec.get('trailing_pe'))}   Forward P/E: {fmt(rec.get('forward_pe'))}",
           f"PEG: {fmt(rec.get('peg'))}   PEG_VALID: {rec.get('peg_valid')}",
           f"ROE: {fmt(rec.get('roe'), pct=True)}   Debt/Equity: {fmt(rec.get('debt_to_equity'))}",
           f"Owner Earnings (NI + D&A - CapEx): {fmt(rec.get('owner_earnings_usd'), money=True)}",
           f"Free Cash Flow: {fmt(rec.get('fcf_usd'), money=True)}",
           f"Gross margins (recent): {rec.get('gross_margins')}",
           f"Operating margins (recent): {rec.get('operating_margins')}",
           f"Institutional %: {fmt(rec.get('institutional_pct'), pct=True)}",
           f"Insider HOLDINGS % (NOT trading activity): {fmt(rec.get('insider_pct'), pct=True)}"]

    warns = rec.get("warnings") or []
    out.append(f"\n--- DATA WARNINGS ({len(warns)}) - you MUST address these in the report ---")
    out.extend(f"  ! {w}" for w in warns) if warns else out.append("  (none)")
    out.append("\nNOTE: analyst price targets and ratings are deliberately withheld. "
               "Derive fair value yourself with the provided valuation tools.")
    return "\n".join(out)

def run_dcf(base_revenue: float, growth_rate: float, ebitda_margin: float,
            capex_pct: float, da_pct: float, tax: float, wacc: float,
            net_debt: float, shares: float, terminal_growth: float,
            terminal_roic: float, years: int = 5) -> str:
    """Run a standard explicit DCF model with constant margins over the explicit period.
    Returns the intrinsic per-share value and a summary of the model.
    """
    try:
        growth = [growth_rate] * years
        ebitda_m = [ebitda_margin] * years
        capex_p = [capex_pct] * years
        da_p = [da_pct] * years
        
        result = dcf(
            base_revenue=base_revenue, growth=growth, ebitda_margin=ebitda_m,
            capex_pct=capex_p, da_pct=da_p, tax=tax, wacc=wacc, net_debt=net_debt,
            shares=shares, terminal_growth=terminal_growth, terminal_roic=terminal_roic
        )
        return f"DCF Per Share Value: ${result.per_share:.2f} (Terminal Share of EV: {result.terminal_share:.1%})"
    except Exception as e:
        return f"DCF Error: {e}"

def run_reverse_dcf(price: float, base_revenue: float, years: int, 
                    ebitda_margin: float, capex_pct: float, da_pct: float,
                    tax: float, wacc: float, net_debt: float, shares: float,
                    terminal_growth: float, terminal_roic: float) -> str:
    """Run a reverse DCF to find the implied revenue growth rate priced into the current stock price."""
    try:
        implied_g = reverse_dcf(
            price=price, base_revenue=base_revenue, years=years,
            ebitda_margin=[ebitda_margin]*years, capex_pct=[capex_pct]*years,
            da_pct=[da_pct]*years, tax=tax, wacc=wacc, net_debt=net_debt,
            shares=shares, terminal_growth=terminal_growth, terminal_roic=terminal_roic
        )
        return f"Implied Revenue CAGR for {years} years: {implied_g:.2%}"
    except Exception as e:
        return f"Reverse DCF Error: {e}"

def check_peg(trailing_pe: float, forward_pe: float, growth: float) -> str:
    """Check if the PEG ratio is valid for a given stock. Returns True if valid, False if void."""
    try:
        valid, msg = peg_is_valid(trailing_pe, forward_pe, growth)
        return f"PEG Valid: {valid}. Message: {msg}"
    except Exception as e:
        return f"Error: {e}"

def get_fcf_yield(fcf: float, market_cap: float) -> str:
    """Calculate the free cash flow yield."""
    try:
        y = fcf_yield(fcf, market_cap)
        return f"FCF Yield: {y:.2%}"
    except Exception as e:
        return f"Error calculating FCF Yield: {e}"

def load_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), ".agents", "AGENTS.md")
    try:
        with open(prompt_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a senior equity analyst."

def get_prior_narrative(ticker: str) -> str:
    """Load the v1 report for qualitative context."""
    path = os.path.join(os.path.dirname(__file__), "reports", "detailed", f"{ticker}.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            text = f.read()
            return f"\n--- PRIOR NARRATIVE DRAFT FOR {ticker} ---\n{text}\n\n(Use the above ONLY for qualitative context like Moat, Management, Bull/Bear points. DO NOT trust any of its numbers or its verdict.)"
    return ""

async def analyze_stock(ticker: str, system_instruction: str, sem: asyncio.Semaphore) -> str:
    async with sem:
        config = LocalAgentConfig(
            tools=[get_stock_data, run_dcf, run_reverse_dcf, check_peg, get_fcf_yield],
            system_instructions=system_instruction,
            temperature=0.1
        )
        
        async with Agent(config) as agent:
            print(f"[{ticker}] Starting deep dive...")
            narrative = get_prior_narrative(ticker)
            prompt = (
                f"Analyze {ticker}. First call `get_stock_data` for validated figures.\n"
                f"{narrative}\n"
                "Follow .agents/AGENTS.md exactly: route by asset class, address every DATA WARNING, "
                "run a real DCF and a reverse-DCF using your tools (if applicable to the asset class), "
                "and close with the mandatory VERDICT block. "
                "Do not substitute sell-side targets for fair value. "
                "Write UNKNOWN for anything you cannot verify."
            )
            response = await agent.chat(prompt)
            text = await response.text()
            
            # Save the individual report
            os.makedirs("reports/detailed", exist_ok=True)
            report_path = f"reports/detailed/{ticker}.md"
            with open(report_path, "w") as f:
                f.write(text)
            
            print(f"[{ticker}] Analysis complete. Saved to {report_path}.")
            return f"\n{'='*40}\nANALYSIS FOR {ticker}\n{'='*40}\n{text}\n"

async def aggregate_reports(reports: List[str]) -> str:
    config = LocalAgentConfig(
        system_instructions=(
            "You are a Lead Portfolio Manager. Build an Executive Action Summary table from "
            "the analysts' reports. CRITICAL: never restate or re-derive a number - quote "
            "figures verbatim from the reports, which are themselves bound to data/fundamentals.json. "
            "If two reports disagree on a figure, flag the contradiction rather than picking one. "
            "Use only the closed verdict vocabulary: BUY/ACCUMULATE/HOLD/TRIM/SELL/PASS. "
            "Also assess PORTFOLIO-level issues v1 ignored: position overlap (e.g. a name held "
            "directly and inside an index fund), sector concentration, and currency exposure."
        ),
        temperature=0.1
    )
    
    combined_reports = "\n\n".join(reports)
    prompt = f"Here are the deep-dive reports from your analysts:\n\n{combined_reports}\n\nPlease generate a final Executive Action Summary table, and then include the detailed reports below it."
    
    async with Agent(config) as agent:
        print("\n[Aggregator] Compiling final Executive Summary...")
        response = await agent.chat(prompt)
        text = await response.text()
        print("[Aggregator] Done.")
        return text

async def main():
    tickers = sys.argv[1:]
    if not tickers:
        print("Usage: python multi_stock_analyzer.py TICKER1 TICKER2 ... or --universe")
        sys.exit(1)
        
    if "--universe" in tickers:
        try:
            with open("data/fundamentals.json") as f:
                data = json.load(f)
            tickers = list(data.get("records", {}).keys())
        except Exception as e:
            print(f"Failed to load universe: {e}")
            sys.exit(1)
            
    print(f"Starting Multi-Agent Stock Analysis for {len(tickers)} tickers: {', '.join(tickers)}")
    system_instruction = load_prompt()
    
    sem = asyncio.Semaphore(3)
    tasks = [analyze_stock(ticker, system_instruction, sem) for ticker in tickers]
    reports = await asyncio.gather(*tasks)
    
    final_report = await aggregate_reports(reports)
    
    report_filename = f"reports/portfolio_master_summary_aug2026.md"
    os.makedirs("reports", exist_ok=True)
    with open(report_filename, "w") as f:
        f.write(final_report)
        
    print(f"\nReport successfully saved to {report_filename}")

if __name__ == "__main__":
    asyncio.run(main())
