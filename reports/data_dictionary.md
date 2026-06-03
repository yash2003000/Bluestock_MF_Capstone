# Data Dictionary

## 01_fund_master.csv
- amfi_code → Unique fund code
- fund_house → Mutual fund company name
- scheme_name → Name of scheme
- category → Fund category
- sub_category → Fund sub category
- risk_category → Risk level

## 02_nav_history.csv
- amfi_code → Fund code
- date → NAV date
- nav → Net Asset Value

## 07_scheme_performance.csv
- amfi_code → Fund code
- return_1yr → 1-year return
- return_3yr → 3-year return
- return_5yr → 5-year return
- expense_ratio → Expense ratio %

## 08_investor_transactions.csv
- investor_id → Unique investor ID
- transaction_date → Date of transaction
- transaction_type → SIP/Lumpsum/Redemption
- amount_inr → Investment amount
- state → Investor state
- city → Investor city
- kyc_status → KYC completion status