-- Top 5 funds by AUM
SELECT * 
FROM 03_aum_by_fund_house
LIMIT 5;

-- Average NAV per month
SELECT strftime('%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- Transactions by state
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Funds with expense ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Top cities by investments
SELECT city,
SUM(amount_inr)
FROM fact_transactions
GROUP BY city
ORDER BY SUM(amount_inr) DESC
LIMIT 5;

-- SIP transactions count
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Redemption count
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='REDEMPTION';

-- Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- Category wise fund count
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- Monthly NAV trend
SELECT date,
AVG(nav)
FROM fact_nav
GROUP BY date;