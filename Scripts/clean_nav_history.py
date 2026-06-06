import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df = df.set_index(["amfi_code", "date"]).sort_index()

df = (df.groupby(level=0)
      .apply(lambda g: g.droplevel(0).resample("D").ffill())
)

df.index = df.index.set_names(["amfi_code", "date"])
df = df.reset_index()

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History cleaned successfully")
print(df.shape)