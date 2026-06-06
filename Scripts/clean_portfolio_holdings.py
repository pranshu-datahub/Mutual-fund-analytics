import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df["amfi_code"] = pd.to_numeric(df["amfi_code"], errors="coerce").astype("Int64")
df["stock_symbol"] = df["stock_symbol"].astype(str).str.strip()
df["stock_name"] = df["stock_name"].astype(str).str.strip()
df["sector"] = df["sector"].astype(str).str.strip()
df["weight_pct"] = pd.to_numeric(df["weight_pct"], errors="coerce")
df["market_value_cr"] = pd.to_numeric(df["market_value_cr"], errors="coerce")
df["current_price_inr"] = pd.to_numeric(df["current_price_inr"], errors="coerce")
df["portfolio_date"] = pd.to_datetime(df["portfolio_date"], errors="coerce")

df = df.dropna(subset=["amfi_code", "stock_symbol", "portfolio_date"])
df = df.sort_values(["amfi_code", "portfolio_date", "stock_symbol"]).drop_duplicates(
    subset=["amfi_code", "stock_symbol", "portfolio_date"]
)
df.to_csv("data/processed/portfolio_holdings_clean.csv", index=False)
print("portfolio holdings cleaned successfully")