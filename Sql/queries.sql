-- 1. Top 5 funds by latest AUM
SELECT fund_house, aum_crore
FROM fact_aum
WHERE report_date = (
    SELECT MAX(report_date) FROM fact_aum
)
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT substr(date, 1, 7) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP YoY growth count
SELECT substr(transaction_date, 1, 4) AS year,
       SUM(CASE WHEN transaction_type = 'SIP' THEN 1 ELSE 0 END) AS sip_count
FROM fact_transactions
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) AS txn_count
FROM fact_transactions
GROUP BY state
ORDER BY txn_count DESC
LIMIT 10;

-- 5. Funds with expense_ratio between 0.1 and 2.5
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct BETWEEN 0.1 AND 2.5
ORDER BY expense_ratio_pct;

-- 6. Transaction type distribution
SELECT transaction_type, COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Gender distribution in transactions
SELECT gender, COUNT(*) AS count
FROM fact_transactions
GROUP BY gender;

-- 8. City tier distribution
SELECT city_tier, COUNT(*) AS count
FROM fact_transactions
GROUP BY city_tier;

-- 9. Fund category count
SELECT category, COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;

-- 10. Top 5 funds by 1-year return
SELECT f.scheme_name, p.return_1yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.return_1yr_pct DESC
LIMIT 5;