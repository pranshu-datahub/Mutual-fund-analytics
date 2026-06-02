import pandas as pd

fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

print("\nMissing Values:")
print(fund_master.isnull().sum())

print("\nDuplicate Rows:")
print(fund_master.duplicated().sum())

missing_codes = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

print("\nMissing AMFI Codes:")
print(missing_codes)

print("\nTotal Missing Codes:", len(missing_codes))