import yfinance as yf
import json

tickers = "LAD UNH RR.L SYK NVO AES ZBH VEEV BRK-B VOO MDT MC.PA ACAD WKL.AS ABT AERO.SW PFE VXUS CNQ INSM PRAX BABA TM MSFT 7974.T MDGL RVMD CELC".split()

results = {}
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        results[ticker] = {
            "Price": info.get("currentPrice", info.get("regularMarketPrice", "N/A")),
            "PE": info.get("trailingPE", "N/A"),
            "ForwardPE": info.get("forwardPE", "N/A"),
            "PEG": info.get("pegRatio", "N/A"),
            "ROE": info.get("returnOnEquity", "N/A"),
            "DebtToEquity": info.get("debtToEquity", "N/A"),
            "Sector": info.get("sector", "N/A"),
            "Name": info.get("longName", ticker)
        }
        print(f"Fetched {ticker}")
    except Exception as e:
        results[ticker] = {"Error": str(e)}
        print(f"Failed {ticker}")

with open("stock_data.json", "w") as f:
    json.dump(results, f, indent=2)

print("Data fetched successfully.")
