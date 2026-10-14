import os
import glob

# Parse all markdown files in reports/ (except summary)
report_files = glob.glob("reports/*_report.md")
report_files.sort()

table_rows = []
full_reports = []

for file_path in report_files:
    ticker = os.path.basename(file_path).split('_')[0]
    with open(file_path, "r") as f:
        content = f.read()
        full_reports.append(content)
        
        # Extract fields
        lines = content.split('\n')
        name = ticker
        verdict = ""
        sizing = ""
        classification = ""
        moat = ""
        
        for line in lines:
            if line.startswith("# "):
                name = line.replace("# ", "").replace(" - Stock Analysis", "").strip()
            elif line.startswith("**Classification:**"):
                classification = line.replace("**Classification:**", "").strip()
            elif line.startswith("**Moat Strength:**"):
                moat = line.replace("**Moat Strength:**", "").strip()
            elif line.startswith("**Verdict:**"):
                verdict = line.replace("**Verdict:**", "").strip()
            elif line.startswith("**Position Sizing:**"):
                sizing = line.replace("**Position Sizing:**", "").strip()
        
        table_rows.append(f"| {ticker} | {name} | {verdict} | {sizing} | {classification} | {moat} |")

summary_header = """# Executive Action Summary: 27-Stock Portfolio

| Ticker | Company Name | Verdict | Position Sizing | Lynch Classification | Moat Strength |
|---|---|---|---|---|---|
"""

summary = summary_header + "\n".join(table_rows) + "\n\n---\n\n# Detailed Analyst Reports\n\n" + "\n\n---\n\n".join(full_reports)

with open("reports/multi_stock_summary_ALL.md", "w") as f:
    f.write(summary)

print("Consolidated report generated successfully.")
