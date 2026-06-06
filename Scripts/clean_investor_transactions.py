import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

type_map = {
    "sip": "SIP",
    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",
    "redemption": "Redemption",
}

df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map(type_map)
)
allowed_kyc = {"Verified", "Pending", "Failed", "Unable to Verify"}
df["kyc_status"] = ( df["kyc_status"].astype(str).str.strip().str.title()
)

invalid_types = df["transaction_type"].isna().sum()
invalid_kyc = set(df["kyc_status"]) - allowed_kyc

print("Invalid Transaction type rows:", invalid_types)
print("Invalid KYC Status values:", invalid_kyc)

df = df[df["amount_inr"] > 0]
df = df[df["transaction_type"].notna()]
df = df[df["transaction_date"].notna()]

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