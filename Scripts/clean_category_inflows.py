import pandas as pd
df = pd.read_csv("data/raw/05_category_inflows.csv")

df["month"] = pd.to_datetime(df["month"], format="%Y-%m", errors="coerce")
df["category"] = df["category"].astype(str).str.strip()
df["net_inflow_crore"] = pd.to_numeric(df["net_inflow_crore"], errors="coerce")

df = df.dropna(subset=["month", "category"])
df = df.sort_values(["month", "category"]).drop_duplicates(subset=["month", "category"])
df["month"] = df["month"].dt.strftime("%Y-%m")

df.to_csv("data/processed/category_inflows_clean.csv", index=False)
print("Category Inflows cleaned successfully")