import yfinance as yf
import sys

def get_stock_data(ticker: str) -> str:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        data = f"--- Data for {ticker} ---\n"
        data += f"Name: {info.get('longName', 'N/A')}\n"
        data += f"Sector: {info.get('sector', 'N/A')}\n"
        data += f"Current Price: ${info.get('currentPrice', 'N/A')}\n"
        data += f"Market Cap: ${info.get('marketCap', 'N/A')}\n"
        data += f"Trailing P/E: {info.get('trailingPE', 'N/A')}\n"
        data += f"Forward P/E: {info.get('forwardPE', 'N/A')}\n"
        data += f"PEG Ratio: {info.get('pegRatio', 'N/A')}\n"
        data += f"Dividend Yield: {info.get('dividendYield', 'N/A')}\n"
        data += f"Return on Equity (ROE): {info.get('returnOnEquity', 'N/A')}\n"
        data += f"Debt to Equity: {info.get('debtToEquity', 'N/A')}\n"
        data += f"Free Cash Flow: ${info.get('freeCashflow', 'N/A')}\n"
        
        news = stock.news
        if news:
            data += "\n--- Recent News ---\n"
            for item in news[:3]:
                data += f"- {item.get('title', '')} ({item.get('publisher', '')})\n"
        
        return data
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"

if __name__ == "__main__":
    tickers = sys.argv[1:]
    for t in tickers:
        print(get_stock_data(t))
        print("="*40)
