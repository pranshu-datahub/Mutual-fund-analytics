import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = df["transaction_type"].str.strip()

df = df[df["amount_inr"] > 0]

print("Unique Transaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nInvestor Transactions cleaned successfully")
print(df.shape)