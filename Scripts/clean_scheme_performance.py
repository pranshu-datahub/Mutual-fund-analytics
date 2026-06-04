import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Expense Ratio Validation
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    & (df["expense_ratio_pct"] <= 2.5)
]

# Return Columns Check
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Missing Return Values:")
print(df[return_cols].isnull().sum())

print("\nExpense Ratio Range:")
print(df["expense_ratio_pct"].min())
print(df["expense_ratio_pct"].max())

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nScheme Performance cleaned successfully")
print(df.shape)