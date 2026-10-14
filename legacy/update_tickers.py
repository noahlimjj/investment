import re

with open('scratch_fetch.py', 'r') as f:
    content = f.read()

# Current string: "LAD UNH RR.L ... EXE ... JD ... 7974.T,MDGL,RVMD,CELC"
# Let's just redefine the whole string.

new_tickers = "LAD UNH RR.L SYK NVO AES ZBH VEEV BRK-B VOO MDT MC.PA ACAD WKL.AS ABT AERO.SW PFE VXUS CNQ INSM PRAX BABA TM MSFT 7974.T MDGL RVMD CELC"
content = re.sub(r'tickers = ".*"\.split\(\)', f'tickers = "{new_tickers}".split()', content)

with open('scratch_fetch.py', 'w') as f:
    f.write(content)

