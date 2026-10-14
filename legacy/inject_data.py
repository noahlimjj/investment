import json
import os
import glob
import re
import csv

# 1. Load Deep Fetch Data
with open("batch_deep.json", "r") as f:
    deep_data = json.load(f)

# 2. Load CSV Data
csv_file = "data/Valuation Scan for stocks.csv"
csv_data = {}
try:
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or row[0].strip() == "":
                continue
            symbol = row[0].strip()
            eps_growth = row[2]
            proj_val = row[6]
            
            val_str = "N/A"
            try:
                val_f = float(proj_val.replace('%', ''))
                if val_f < 1:
                    val_str = "Overvalued"
                elif 1 <= val_f < 2:
                    val_str = "Fairly Valued"
                elif 2 <= val_f < 3:
                    val_str = "Undervalued"
                elif val_f >= 3:
                    val_str = "Very Undervalued"
            except:
                pass
                
            csv_data[symbol] = {
                "EPS Growth (3-5y)": eps_growth,
                "Projected Val": proj_val,
                "Peter Lynch Value": val_str
            }
except Exception as e:
    print(f"Error reading CSV: {e}")

# 3. Inject Data into Reports
report_files = glob.glob("reports/*_report.md")

for filepath in report_files:
    ticker = os.path.basename(filepath).split('_')[0]
    
    if ticker not in deep_data:
        print(f"Skipping {ticker}, no deep data found.")
        continue
        
    stock_data = deep_data[ticker]
    stock_csv = csv_data.get(ticker, {})
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Format the injection strings
    
    # Financial Health Inject
    oe = stock_data.get("Owner Earnings (TTM)", "N/A")
    if isinstance(oe, (int, float)):
        oe_str = f"${oe:,.2f}"
    else:
        oe_str = str(oe)
        
    margins = stock_data.get("Margins (Last 5 yrs)", "N/A")
    margin_str = ""
    if isinstance(margins, dict):
        try:
            gross = [f"{m*100:.1f}%" for m in margins.get("Gross", [])]
            op = [f"{m*100:.1f}%" for m in margins.get("Operating", [])]
            margin_str = f"Gross Margins: {', '.join(gross)} | Operating Margins: {', '.join(op)}"
        except:
            margin_str = str(margins)
    else:
        margin_str = str(margins)
        
    financial_inject = f"\n* **[UPDATED DATA] Owner Earnings (TTM):** {oe_str}\n* **[UPDATED DATA] 5-Year Margin Trend:** {margin_str}\n"
    content = content.replace("## PART 5: VALUATION", financial_inject + "\n## PART 5: VALUATION")
    
    # Valuation Inject
    pl_val = stock_csv.get("Peter Lynch Value", "Not found in CSV scan")
    proj_val = stock_csv.get("Projected Val", "N/A")
    eps_gwth = stock_csv.get("EPS Growth (3-5y)", "N/A")
    target = stock_data.get("Analyst Target Mean", "N/A")
    rating = stock_data.get("Analyst Rating", "N/A")
    
    val_inject = f"\n* **[UPDATED DATA] Peter Lynch Fair Value:** {pl_val} (Projected: {proj_val}, EPS Growth: {eps_gwth})\n* **[UPDATED DATA] Analyst Target Mean:** ${target} ({rating})\n"
    content = content.replace("## PART 6: OWNERSHIP & POSITIONING", val_inject + "\n## PART 6: OWNERSHIP & POSITIONING")
    
    # Ownership Inject
    inst = stock_data.get("Institutions %", "N/A")
    ins = stock_data.get("Insiders %", "N/A")
    if isinstance(inst, (int, float)): inst = f"{inst*100:.2f}%"
    if isinstance(ins, (int, float)): ins = f"{ins*100:.2f}%"
        
    own_inject = f"\n* **[UPDATED DATA] Institutional Ownership:** {inst}\n* **[UPDATED DATA] Insider Ownership:** {ins}\n"
    content = content.replace("## PART 7: SECTOR-SPECIFIC EDGE", own_inject + "\n## PART 7: SECTOR-SPECIFIC EDGE")
    
    with open(filepath, "w") as f:
        f.write(content)

print("Data successfully injected into all reports.")
