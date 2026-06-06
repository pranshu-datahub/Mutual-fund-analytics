import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["aum_lakh_crore"] = pd.to_numeric(df["aum_lakh_crore"], errors="coerce")
df["aum_crore"] = pd.to_numeric(df["aum_crore"], errors="coerce")
df["num_schemes"] = pd.to_numeric(df["num_schemes"], errors="coerce")

df = df.dropna(subset=["date", "fund_house"])
df["fund_house"] = df["fund_house"].astype(str).str.strip()

df = df.sort_values(["fund_house", "date"]).drop_duplicates(subset=["fund_house", "date"])
df = df.reset_index(drop=True)

df.to_csv("data/processed/aum_by_fund_house_clean.csv", index=False)
print("Aum By Fund House Cleaned successfully")
print(df.shape)