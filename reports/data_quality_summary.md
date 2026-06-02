# Day 1 Data Quality Summary

## Dataset Validation Summary

- Successfully loaded all 10 provided datasets.
- Checked shape, data types, and first 5 rows for all files.
- No major missing file issues found.
- Fund houses, categories, sub-categories, and risk categories were explored from fund_master dataset.
- AMFI code validation completed successfully.
- All AMFI codes in fund_master exist in nav_history dataset.
- Live NAV data fetched successfully from mfapi.in for:
  - HDFC Top 100 Direct
  - SBI Bluechip
  - ICICI Bluechip
  - Nippon Large Cap
  - Axis Bluechip
  - Kotak Bluechip

## Observations
- Dataset structure appears consistent.
- AMFI mapping integrity is maintained.
- Data is ready for cleaning and SQL database design in Day 2.