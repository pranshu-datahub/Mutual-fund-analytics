import pandas as pd

df = pd.read_csv("Data/Raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())