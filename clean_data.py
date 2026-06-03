import pandas as pd
import os
os.makedirs("data/processed", exist_ok=True)
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
nav.to_csv("data/processed/02_nav_history_cleaned.csv",index=False)
tx = pd.read_csv("data/raw/08_investor_transactions.csv")
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce")
tx["amount_inr"] = pd.to_numeric(
    tx["amount_inr"],
    errors="coerce")
tx = tx[tx["amount_inr"] > 0]
tx["transaction_type"] = (
    tx["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title())
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"]
tx = tx[tx["transaction_type"].isin(valid_types)]
tx["kyc_status"] = (
    tx["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper())
valid_kyc = ["YES","NO","PENDING"]
tx = tx[tx["kyc_status"].isin(valid_kyc)]
tx.to_csv("data/processed/08_investor_transactions_cleaned.csv",index=False)
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"]
for col in return_cols:
    perf[col] = pd.to_numeric(perf[col],errors="coerce")
perf["expense_ratio_pct"] = pd.to_numeric(perf["expense_ratio_pct"],errors="coerce")
anomalies = perf[(perf["expense_ratio_pct"] < 0.1)|(perf["expense_ratio_pct"] > 2.5)]
print("\nExpense Ratio Anomalies")
print(anomalies[["scheme_name","expense_ratio_pct"]])
perf.to_csv("data/processed/07_scheme_performance_cleaned.csv",index=False)
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum["date"] = pd.to_datetime(aum["date"],errors="coerce")
aum.to_csv("data/processed/03_aum_by_fund_house_cleaned.csv",index=False)
print("\nCleaning Complete")