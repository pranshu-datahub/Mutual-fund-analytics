import pandas as pd
df = pd.read_csv("data/raw/06_industry_folio_count.csv")
df["month"] = pd.to_datetime(df["month"], format="%Y-%m", errors="coerce")
numeric_cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["month"])
    df = df.sort_values("month").drop_duplicates(subset=["month"])
df["month"] = df["month"].dt.strftime("%Y-%m")

df.to_csv("data/processed/industry_folio_count_clean.csv", index=False)
print("Industry Folio Count cleaned successfully")