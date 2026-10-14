import yfinance as yf
import json
import sys

tickers = sys.argv[1].split(',')
results = {}

for t in tickers:
    stock = yf.Ticker(t)
    info = stock.info
    
    # Financials (5 year proxy using annual)
    income_stmt = stock.financials
    margins = []
    if not income_stmt.empty:
        try:
            gross_margins = (income_stmt.loc["Gross Profit"] / income_stmt.loc["Total Revenue"]).dropna().head(5).tolist()
            op_margins = (income_stmt.loc["Operating Income"] / income_stmt.loc["Total Revenue"]).dropna().head(5).tolist()
            margins = {"Gross": gross_margins, "Operating": op_margins}
        except:
            margins = "Data unavailable"
    
    # Cash flow (Owner earnings proxy)
    cash_flow = stock.cashflow
    owner_earnings = "N/A"
    if not cash_flow.empty:
        try:
            net_income = cash_flow.loc["Net Income"].iloc[0] if "Net Income" in cash_flow.index else 0
            depreciation = cash_flow.loc["Depreciation And Amortization"].iloc[0] if "Depreciation And Amortization" in cash_flow.index else 0
            capex = cash_flow.loc["Capital Expenditure"].iloc[0] if "Capital Expenditure" in cash_flow.index else 0
            owner_earnings = net_income + depreciation + capex # capex is usually negative in yfinance
        except:
            owner_earnings = "Data unavailable"
            
    # Insiders & Institutions
    inst_own = info.get("heldPercentInstitutions", "N/A")
    insider_own = info.get("heldPercentInsiders", "N/A")
    
    results[t] = {
        "Info": {
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
            "MarketCap": info.get("marketCap"),
            "ForwardPE": info.get("forwardPE"),
            "PEG": info.get("pegRatio"),
            "ROE": info.get("returnOnEquity"),
            "DebtToEquity": info.get("debtToEquity"),
            "CurrentPrice": info.get("currentPrice")
        },
        "Margins (Last 5 yrs)": margins,
        "Owner Earnings (TTM)": owner_earnings,
        "Institutions %": inst_own,
        "Insiders %": insider_own,
        "Analyst Target Mean": info.get("targetMeanPrice"),
        "Analyst Rating": info.get("recommendationKey")
    }

with open("batch_deep.json", "w") as f:
    json.dump(results, f, indent=2)

print("Batch deep data fetched.")
