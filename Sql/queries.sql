-- Top 5 Funds by AUM
SELECT * FROM fact_aum ORDER BY aum_crore DESC LIMIT 5;

-- Average NAV
SELECT AVG(nav) FROM fact_nav;

-- Monthly NAV
SELECT substr(date,1,7), AVG(nav)
FROM fact_nav
GROUP BY substr(date,1,7);

-- State-wise Transactions
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1
SELECT expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Transaction Type Count
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Gender Distribution
SELECT gender, COUNT(*)
FROM fact_transactions
GROUP BY gender;

-- City Tier Distribution
SELECT city_tier, COUNT(*)
FROM fact_transactions
GROUP BY city_tier;

-- Risk Grade Distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- Fund Category Count
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;