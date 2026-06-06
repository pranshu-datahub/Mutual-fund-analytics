import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["index_name"] = df["index_name"].astype(str).str.strip()
df["close_value"] = pd.to_numeric(df["close_value"], errors="coerce")

df = df.dropna(subset=["date", "index_name"])
df = df.sort_values(["index_name", "date"]).drop_duplicates(subset=["index_name", "date"])
df.to_csv("data/processed/benchmark_indices_clean.csv", index=False)
print("benchmark indices cleaned successfully")