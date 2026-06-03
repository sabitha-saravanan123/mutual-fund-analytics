import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing_codes = master_codes - nav_codes

print("Fund Master Codes :", len(master_codes))
print("NAV History Codes :", len(nav_codes))
print("Missing Codes :", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes are present in NAV history.")