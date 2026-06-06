import pandas as pd
df = pd.read_csv("data/raw/01_fund_master.csv")

# Ensure amfi_code numeric and valid
df["amfi_code"] = pd.to_numeric(df["amfi_code"], errors="coerce")
df = df.dropna(subset=["amfi_code"])
df["amfi_code"] = df["amfi_code"].astype(int)

#Trim text fields and normalize
text_cols = ["fund_house", "scheme_name", "category", "sub_category", "risk_category"]
for c in text_cols:
    if c in df.columns:
        df[c] = df[c].astype(str).str.strip()

#Remove exact duplicates on amfi_code(keep first)
df = df.drop_duplicates(subset=["amfi_code"])

df = df.sort_values("amfi_code").reset_index(drop=True)

df.to_csv("data/processed/fund_master_clean.csv", index=False)

print("Fund master cleaned Successfully")
print(df.shape)