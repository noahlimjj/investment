import csv
import sys

tickers = "LAD UNH RR.L SYK NVO AES ZBH VEEV BRK-B VOO MDT MC.PA ACAD WKL.AS ABT AERO.SW PFE VXUS EXE CNQ INSM JD PRAX BABA TM MSFT 7974.T".split()

csv_file = "data/Valuation Scan for stocks.csv"

# find the projected valuation and peter lynch mapping
pl_mapping = {
    "Less than 1%": "Over value",
    "1% to 1.5%": "fairly value",
    "2% range": "under value",
    "more than 3%": "very undervalue"
}

results = {}
try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or row[0].strip() == "":
                continue
            symbol = row[0].strip()
            if symbol in tickers:
                eps_growth = row[2]
                div_yield = row[3]
                pe = row[4]
                proj_val = row[6]
                
                # estimate PL string based on proj_val
                val_str = ""
                try:
                    val_f = float(proj_val.replace('%', ''))
                    if val_f < 1:
                        val_str = "Over value"
                    elif 1 <= val_f < 2:
                        val_str = "Fairly value"
                    elif 2 <= val_f < 3:
                        val_str = "Under value"
                    elif val_f >= 3:
                        val_str = "Very undervalue"
                except:
                    pass
                    
                results[symbol] = {
                    "EPS Growth (3-5y)": eps_growth,
                    "Projected Val": proj_val,
                    "Peter Lynch Value": val_str
                }
except Exception as e:
    print(e)

import json
print(json.dumps(results, indent=2))
