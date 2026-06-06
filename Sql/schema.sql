CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name TEXT,
    day INTEGER,
    weekday TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    PRIMARY KEY(amfi_code, date),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date) REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    PRIMARY KEY(investor_id, amfi_code, transaction_date),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(transaction_date) REFERENCES dim_date(date)
);

CREATE TABLE fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    report_date TEXT,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER,
    FOREIGN KEY(report_date) REFERENCES dim_date(date)
);

CREATE TABLE fact_category_inflows (
    month TEXT,
    category TEXT,
    net_inflow_crore REAL,
    PRIMARY KEY(month, category),
    FOREIGN KEY(month) REFERENCES dim_date(date)
);

CREATE TABLE fact_industry_folio_count (
    month TEXT PRIMARY KEY,
    total_folios_crore REAL,
    equity_folios_crore REAL,
    debt_folios_crore REAL,
    hybrid_folios_crore REAL,
    others_folios_crore REAL,
    FOREIGN KEY(month) REFERENCES dim_date(date)
);

CREATE TABLE fact_portfolio_holdings (
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date TEXT,
    PRIMARY KEY(amfi_code, stock_symbol, portfolio_date),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(portfolio_date) REFERENCES dim_date(date)
);

CREATE TABLE fact_benchmark_indices (
    date TEXT,
    index_name TEXT,
    close_value REAL,
    PRIMARY KEY(date, index_name),
    FOREIGN KEY(date) REFERENCES dim_date(date)
);

CREATE TABLE fact_monthly_sip_inflows (
    month TEXT,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL,
    new_sip_accounts_lakh REAL,
    sip_aum_lakh_crore REAL,
    yoy_growth_pct REAL,
    PRIMARY KEY(month),
    FOREIGN KEY(month) REFERENCES dim_date(date)
);