CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date TEXT,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL
);

CREATE TABLE fact_aum (
    fund_house TEXT,
    aum_crore REAL
);