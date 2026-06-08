import pandas as pd

files = [
    "01_fund_master.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(f"data/raw/{file}")

    output = file.replace(".csv", "_cleaned.csv")

    df.to_csv(
        f"data/processed/{output}",
        index=False
    )

    print(output, "saved")