"""
Bluestock Mutual Fund Capstone

Purpose:
Cleans, transforms, and processes
raw mutual fund datasets and stores
them in SQLite database.
Author: Yash Chowdhary
"""
import pandas as pd
import os
from sqlalchemy import create_engine

# =====================================================
# FOLDERS
# =====================================================

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"
DB_PATH = "data/db/bluestock_mf.db"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("=" * 60)
print("DAY 2 ETL PIPELINE STARTED")
print("=" * 60)

# =====================================================
# 1. CLEAN NAV HISTORY
# =====================================================

print("\nCleaning nav_history.csv")
print("=" * 60)

nav = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

# Fix dates
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only positive NAV
nav = nav[nav["nav"] > 0]

# Save
nav.to_csv(
    f"{PROCESSED_PATH}/cleaned_nav_history.csv",
    index=False
)

print("✅ NAV cleaned successfully")

# =====================================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================================

# =====================================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================================

print("\nCleaning investor_transactions.csv")
print("=" * 60)

txn = pd.read_csv(
    f"{RAW_PATH}/08_investor_transactions.csv"
)

print("\nColumns found:")
print(txn.columns)

print("\nInitial Shape:")
print(txn.shape)

# Convert transaction date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Valid transaction types
valid_types = [
    "SIP",
    "LUMPSUM",
    "REDEMPTION"
]

txn = txn[
    txn["transaction_type"]
    .isin(valid_types)
]

print("\nAfter transaction type filter:")
print(txn.shape)

# Amount > 0
txn["amount_inr"] = pd.to_numeric(
    txn["amount_inr"],
    errors="coerce"
)

txn = txn[
    txn["amount_inr"] > 0
]

print("\nAfter amount filter:")
print(txn.shape)

# Clean KYC status
txn["kyc_status"] = (
    txn["kyc_status"]
    .astype(str)
    .str.strip()
)

# Only remove blanks/nulls
txn = txn[
    txn["kyc_status"].notna()
]

print("\nAfter KYC cleaning:")
print(txn.shape)

# Remove duplicates
txn = txn.drop_duplicates()

print("\nFinal Shape:")
print(txn.shape)

# Save cleaned file
txn.to_csv(
    f"{PROCESSED_PATH}/cleaned_investor_transactions.csv",
    index=False
)

print(
    "✅ Investor transactions cleaned successfully"
)

# =====================================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================================

print("\nCleaning scheme_performance.csv")
print("=" * 60)

performance = pd.read_csv(
    f"{RAW_PATH}/07_scheme_performance.csv"
)

# Convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct"
]

for col in numeric_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Remove nulls
performance = performance.dropna(
    subset=numeric_cols
)

# Expense ratio validation
performance = performance[
    (performance["expense_ratio_pct"] >= 0.1)
    &
    (performance["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
performance = performance.drop_duplicates()

# Save
performance.to_csv(
    f"{PROCESSED_PATH}/cleaned_scheme_performance.csv",
    index=False
)

print("✅ Scheme performance cleaned successfully")

# =====================================================
# 4. CLEAN REMAINING DATASETS
# =====================================================

print("\nCleaning remaining datasets")
print("=" * 60)

files_to_clean = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files_to_clean:
    try:
        df = pd.read_csv(f"{RAW_PATH}/{file}")

        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing values
        df = df.ffill()

        # Save cleaned version
        cleaned_name = (
            "cleaned_" + file
        )

        df.to_csv(
            f"{PROCESSED_PATH}/{cleaned_name}",
            index=False
        )

        print(f"✅ {file} cleaned")

    except Exception as e:
        print(f"❌ Error in {file}: {e}")

print("\n✅ All datasets cleaned and saved!")

# =====================================================
# 5. LOAD INTO SQLITE
# =====================================================

print("\nLoading data into SQLite")
print("=" * 60)

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

# Load tables
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

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("✅ SQLite database created successfully")

# =====================================================
# 6. VERIFY ROW COUNTS
# =====================================================

print("\nVerification")
print("=" * 60)

print(f"NAV rows: {len(nav)}")
print(f"Transaction rows: {len(txn)}")
print(f"Performance rows: {len(performance)}")

print("\n🎉 DAY 2 ETL COMPLETED SUCCESSFULLY!")