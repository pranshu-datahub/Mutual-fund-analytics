import pandas as pd
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df["month"] = pd.to_datetime(df["month"], format="%Y-%m", errors="coerce")

numeric_cols = ["sip_inflow_crore", "active_sip_accounts_crore", "new_sip_accounts_lakh", "sip_aum_lakh_crore", "yoy_growth_pct"]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    else:
        print(f"Warning: Column '{col}' not found in the dataset.")

#remove missing month rows
df = df.dropna(subset=["month"])

#remove duplicate months if any
df = df.sort_values("month").drop_duplicates(subset=["month"])


df["month"] = df["month"].dt.strftime("%Y-%m")

df.to_csv("data/processed/monthly_sip_inflows_clean.csv", index=False)
print("Monthly SIP Inflows cleaned successfully")
print(df.shape)