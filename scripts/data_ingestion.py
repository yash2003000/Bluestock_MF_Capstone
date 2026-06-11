"""
Bluestock Mutual Fund Capstone

Purpose:
Downloads and ingests raw mutual fund
datasets for further processing.
Author: Yash Chowdhary
"""

import pandas as pd
import os

folder = "Data/Raw"

for file in os.listdir(folder):

    if file.endswith(".csv") or file.endswith(".xlsx"):

        print("=" * 60)
        print("FILE:", file)

        path = os.path.join(folder, file)

        if file.endswith(".csv"):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
        print("\n" + "="*50)
print("FUND MASTER EXPLORATION")
print("="*50)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Grades:")
print(fund_master["risk_category"].unique())





print("\n" + "="*50)
print("AMFI CODE VALIDATION")
print("="*50)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("✅ All AMFI codes exist in nav_history")
else:
    print("❌ Missing AMFI codes:")
    print(missing_codes)