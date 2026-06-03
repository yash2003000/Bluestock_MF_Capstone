import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

# ======================================================
# PATHS
# ======================================================

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"
DB_PATH = "data/db/bluestock_mf.db"

os.makedirs(PROCESSED_PATH, exist_ok=True)
os.makedirs("data/db", exist_ok=True)

print("=" * 50)
print("Cleaning nav_history.csv")
print("=" * 50)

# ======================================================
# 1. CLEAN NAV HISTORY
# ======================================================

nav = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

# Parse date column
if "date" in nav.columns:
    nav["date"] = pd.to_datetime(nav["date"])
elif "nav_date" in nav.columns:
    nav["date"] = pd.to_datetime(nav["nav_date"])

# Sort data
if "amfi_code" in nav.columns:
    nav = nav.sort_values(by=["amfi_code", "date"])
else:
    nav = nav.sort_values(by=["date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV
if "nav" in nav.columns:
    nav["nav"] = nav["nav"].ffill()

# Validate NAV > 0
if "nav" in nav.columns:
    nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(f"{PROCESSED_PATH}/cleaned_nav_history.csv", index=False)

print("✅ NAV cleaned successfully")

# ======================================================
# 2. CLEAN INVESTOR TRANSACTIONS
# ======================================================

print("=" * 50)
print("Cleaning investor_transactions.csv")
print("=" * 50)

txn = pd.read_csv(f"{RAW_PATH}/08_investor_transactions.csv")

print("\nColumns found:")
print(txn.columns)

# Fix date column automatically
date_column = None

possible_dates = [
    "date",
    "transaction_date",
    "txn_date",
    "investment_date"
]

for col in possible_dates:
    if col in txn.columns:
        date_column = col
        break

if date_column:
    txn[date_column] = pd.to_datetime(
        txn[date_column],
        errors="coerce"
    )

# Standardize transaction type
possible_txn_cols = [
    "transaction_type",
    "txn_type",
    "type"
]

txn_col = None

for col in possible_txn_cols:
    if col in txn.columns:
        txn_col = col
        break

if txn_col:
    txn[txn_col] = (
        txn[txn_col]
        .astype(str)
        .str.strip()
        .str.upper()
    )

# Validate amount > 0
possible_amount_cols = [
    "amount",
    "transaction_amount",
    "investment_amount"
]

amount_col = None

for col in possible_amount_cols:
    if col in txn.columns:
        amount_col = col
        break

if amount_col:
    txn = txn[txn[amount_col] > 0]

# Remove duplicates
txn = txn.drop_duplicates()

# Save cleaned file
txn.to_csv(
    f"{PROCESSED_PATH}/cleaned_investor_transactions.csv",
    index=False
)

print("✅ Investor transactions cleaned successfully")

# ======================================================
# 3. CLEAN SCHEME PERFORMANCE
# ======================================================

print("=" * 50)
print("Cleaning scheme_performance.csv")
print("=" * 50)

perf = pd.read_csv(f"{RAW_PATH}/07_scheme_performance.csv")

# Convert numeric columns
numeric_cols = perf.select_dtypes(include=np.number).columns

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio validation
if "expense_ratio" in perf.columns:
    anomalies = perf[
        (perf["expense_ratio"] < 0.1)
        | (perf["expense_ratio"] > 2.5)
    ]

    print("\nExpense Ratio anomalies:")
    print(anomalies.shape[0])

# Save cleaned file
perf.to_csv(
    f"{PROCESSED_PATH}/cleaned_scheme_performance.csv",
    index=False
)

print("✅ Scheme performance cleaned successfully")

# ======================================================
# 4. LOAD INTO SQLITE DATABASE
# ======================================================

print("=" * 50)
print("Loading data into SQLite")
print("=" * 50)

engine = create_engine(f"sqlite:///{DB_PATH}")

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("✅ SQLite database created successfully")

# ======================================================
# 5. VERIFY ROW COUNTS
# ======================================================

print("=" * 50)
print("Verification")
print("=" * 50)

print("NAV rows:", len(nav))
print("Transaction rows:", len(txn))
print("Performance rows:", len(perf))

print("\n🎉 DAY 2 ETL COMPLETED SUCCESSFULLY!")