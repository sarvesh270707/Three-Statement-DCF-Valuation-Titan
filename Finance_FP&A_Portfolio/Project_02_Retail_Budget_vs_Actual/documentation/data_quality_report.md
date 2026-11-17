# Project 02: Retail FP&A | Data Quality & Validation Audit Report

---

### Executive Data Quality Summary

An automated data quality and mathematical integrity audit was executed across the 24-month granular retail dataset (`Retail_Sector_Financial_Analysis.xlsx`). 

- **Audit Result**: **100% PASS across all 8 verification gates**
- **Total Records Audited**: 1,728 transactions
- **Time Horizon**: 2025-01-01 to 2026-12-01 (24 continuous monthly cycles)
- **Zero Nulls / Zero Missing Data / Zero Duplicate Keys**

---

### Verification Test Matrix

| Test ID | Audit Check | Scope / Rule | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **CHK-01** | Missing / Null Value Check | Entire Dataset (All Columns) | 0 null values | 0 nulls | **PASS** |
| **CHK-02** | Transaction ID Uniqueness | Primary Key (Transaction_ID) | 0 duplicates | 0 duplicates | **PASS** |
| **CHK-03** | Time Horizon & Monthly Continuity | Date Dimension | 24 distinct months (2025-01-01 to 2026-12-31) | 24 months (2025-01-01 to 2026-12-01) | **PASS** |
| **CHK-04** | Dimensional Coverage (Regions, Categories, Channels) | Categorical Slices | >= 4 Regions, >= 6 Categories, >= 3 Channels | 4 Regions, 6 Categories, 3 Channels | **PASS** |
| **CHK-05** | Actual Expense Additive Consistency | Actual Expenses = COGS + Mkt + Personnel + Dist + Other | Max absolute difference = 0.00 | Max diff = 0.00 | **PASS** |
| **CHK-06** | Actual Profit Mathematical Equality | Actual Profit = Actual Revenue - Actual Expenses | Max absolute difference = 0.00 | Max diff = 0.00 | **PASS** |
| **CHK-07** | Revenue Variance Mathematical Equality | Revenue Variance = Actual Revenue - Budgeted Revenue | Max absolute difference = 0.00 | Max diff = 0.00 | **PASS** |
| **CHK-08** | FP&A Variance Distribution (Beats vs Overruns) | Variance Distribution | Meaningful mix of positive and negative variances | Revenue: 976 beats / 752 misses; Expense: 1071 overruns / 657 savings | **PASS** |

---

### Dataset Summary Statistics

| Financial Metric | Total Budget (₹ Cr) | Total Actual (₹ Cr) | Net Variance (₹ Cr) | Variance (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Gross Revenue** | ₹593.20 Cr | ₹604.80 Cr | +₹11.60 Cr | +1.96% |
| **Total Expenses** | ₹550.42 Cr | ₹565.14 Cr | +₹14.72 Cr | +2.67% |
| **Operating Profit** | ₹42.78 Cr | ₹39.66 Cr | -₹3.12 Cr | -7.30% |
| **Operating Margin** | 7.21% | 6.56% | -0.65% pts | N/A |

---

### Data Cleaning & Handling Decisions

1. **Synthetic Nature Disclosure**: All records were synthetically generated using controlled NumPy random seeds to simulate realistic retail operating conditions, seasonality, and variance behavior for portfolio demonstration.
2. **Granular Additivity**: Verified that actual expenses sum exactly from individual line items (COGS, marketing, payroll, freight, and general administrative overhead) without discrepancies.
3. **No Silent Drops**: Zero records were dropped or imputed; full historical data lineage is preserved.
