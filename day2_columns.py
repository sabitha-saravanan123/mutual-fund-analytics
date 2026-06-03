import pandas as pd
files = ["02_nav_history.csv","03_aum_by_fund_house.csv","07_scheme_performance.csv","08_investor_transactions.csv"]
for file in files:
    df = pd.read_csv(f"data/raw/{file}")
    print("\n" + "="*60)
    print(file)
    print("="*60)
    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns.tolist())

    