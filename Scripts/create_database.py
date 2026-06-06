import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

fund = pd.read_csv("data/processed/fund_master_clean.csv")
nav = pd.read_csv("data/processed/nav_history_clean.csv")
txn = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")
aum = pd.read_csv("data/processed/aum_by_fund_house_clean.csv")
category = pd.read_csv("data/processed/category_inflows_clean.csv")
industry = pd.read_csv("data/processed/industry_folio_count_clean.csv")
portfolio = pd.read_csv("data/processed/portfolio_holdings_clean.csv")
benchmark = pd.read_csv("data/processed/benchmark_indices_clean.csv")
monthly_sip = pd.read_csv("data/processed/monthly_sip_inflows_clean.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce").dt.strftime("%Y-%m-%d")
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"], errors="coerce").dt.strftime("%Y-%m-%d")
aum["report_date"] = pd.to_datetime(aum["date"], errors="coerce").dt.strftime("%Y-%m-%d")
aum = aum.drop(columns=["date"])

benchmark["date"] = pd.to_datetime(benchmark["date"], errors="coerce").dt.strftime("%Y-%m-%d")
portfolio["portfolio_date"] = pd.to_datetime(portfolio["portfolio_date"], errors="coerce").dt.strftime("%Y-%m-%d")

for df in [monthly_sip, category, industry]:
    df["month"] = (
        pd.to_datetime(df["month"], format="%Y-%m", errors="coerce")
        .dt.to_period("M")
        .dt.to_timestamp()
        .dt.strftime("%Y-%m-%d")
    )

date_series = pd.concat(
    [
        nav["date"],
        txn["transaction_date"],
        aum["report_date"],
        benchmark["date"],
        portfolio["portfolio_date"],
        monthly_sip["month"],
        category["month"],
        industry["month"],
    ],
    ignore_index=True,
).dropna().drop_duplicates()

date_series = pd.to_datetime(date_series, errors="coerce").dropna().sort_values()

dim_date = pd.DataFrame(
    {
        "date": date_series.dt.strftime("%Y-%m-%d"),
        "year": date_series.dt.year,
        "quarter": date_series.dt.quarter,
        "month": date_series.dt.month,
        "month_name": date_series.dt.month_name(),
        "day": date_series.dt.day,
        "weekday": date_series.dt.day_name(),
    }
)

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
category.to_sql("fact_category_inflows", engine, if_exists="replace", index=False)
industry.to_sql("fact_industry_folio_count", engine, if_exists="replace", index=False)
portfolio.to_sql("fact_portfolio_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark_indices", engine, if_exists="replace", index=False)
monthly_sip.to_sql("fact_monthly_sip_inflows", engine, if_exists="replace", index=False)

with engine.connect() as conn:
    for name, df in [
        ("dim_date", dim_date),
        ("dim_fund", fund),
        ("fact_nav", nav),
        ("fact_transactions", txn),
        ("fact_performance", perf),
        ("fact_aum", aum),
        ("fact_category_inflows", category),
        ("fact_industry_folio_count", industry),
        ("fact_portfolio_holdings", portfolio),
        ("fact_benchmark_indices", benchmark),
        ("fact_monthly_sip_inflows", monthly_sip),
    ]:
        print(f"{name} rows in CSV:", len(df))
        rows = conn.execute(text(f"SELECT COUNT(*) FROM {name}")).scalar_one()
        print(f"{name} rows in DB:", rows)

print("Database Created Successfully")