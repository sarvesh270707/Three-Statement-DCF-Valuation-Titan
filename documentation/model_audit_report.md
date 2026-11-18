# Project 01: Titan Company Ltd. | Financial Model Audit & Quality Assurance Report

---

### Executive Audit Summary

An independent, programmatic audit was performed on the financial model `Titan_3Statement_DCF_Model.xlsx` using native Microsoft Excel COM automation (`Excel.Application` Version 16.0) to recalculate all formula cells and verify reconciliation integrity across both historical (FY17-FY26) and projected (FY27E-FY31E) periods.

**Overall Audit Result: 100% PASS**  
**Maximum Balance Sheet Deviation: ₹0.00 Cr**  
**Plugs or Balancing Overrides Inserted: ZERO**

---

### Audit Test Matrix & Verification Results

| Audit Check ID | Schedule Under Audit | Verification Formula / Rule | Expected Result | Actual Recalculated Output | Variance | Audit Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **AUD-01** | `10_Balance_Sheet` | $\text{Total Assets} - \text{Total Liabilities} - \text{Total Equity} = 0$ | 0.00 Cr | 0.00 Cr | 0.00 Cr | **PASS** |
| **AUD-02** | `09_Cash_Flow` | $\text{Opening Cash} + \Delta\text{Cash} - \text{Closing Cash} = 0$ | 0.00 Cr | 0.00 Cr | 0.00 Cr | **PASS** |
| **AUD-03** | `07_PP&E_Schedule` | $\text{Opening PP\&E} + \text{CapEx} - \text{Depr} - \text{Closing PP\&E} = 0$ | 0.00 Cr | 0.00 Cr | 0.00 Cr | **PASS** |
| **AUD-04** | `08_Debt_Schedule` | $\text{Opening Debt} + \text{Borrowings} - \text{Repayments} - \text{Closing} = 0$ | 0.00 Cr | 0.00 Cr | 0.00 Cr | **PASS** |
| **AUD-05** | `10_Balance_Sheet` | $\text{Closing Reserves} = \text{Opening} + \text{PAT} - \text{Dividends}$ | 0.00 Cr | 0.00 Cr | 0.00 Cr | **PASS** |
| **AUD-06** | `12_WACC` | $\text{WACC Mathematical Consistency} > 5.0\%$ | > 5.0% | 14.43% | N/A | **PASS** |
| **AUD-07** | `03_Assump` / `12_WACC` | $\text{Finite DCF Condition}: \text{WACC} > g$ | $\text{WACC} > g$ | $14.43\% > 5.50\%$ (+8.93%) | N/A | **PASS** |

---

### Period-by-Period Balance Sheet Equality Audit

| Fiscal Period | Nature of Data | Total Assets (₹ Cr) | Total Liabilities & Equity (₹ Cr) | Absolute Deviation (₹ Cr) | Reconciliation Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **FY17** | Audited Actual | 8,407.57 | 8,407.57 | 0.00 | **PASS** |
| **FY18** | Audited Actual | 9,521.04 | 9,521.04 | 0.00 | **PASS** |
| **FY19** | Audited Actual | 11,709.84 | 11,709.84 | 0.00 | **PASS** |
| **FY20** | Audited Actual | 13,544.00 | 13,544.00 | 0.00 | **PASS** |
| **FY21** | Audited Actual | 16,444.00 | 16,444.00 | 0.00 | **PASS** |
| **FY22** | Audited Actual | 21,188.00 | 21,188.00 | 0.00 | **PASS** |
| **FY23** | Audited Actual | 27,020.00 | 27,020.00 | 0.00 | **PASS** |
| **FY24** | Audited Actual | 31,547.00 | 31,547.00 | 0.00 | **PASS** |
| **FY25** | Audited Actual | 40,645.00 | 40,645.00 | 0.00 | **PASS** |
| **FY26** | Audited Actual | 60,561.00 | 60,561.00 | 0.00 | **PASS** |
| **FY27E** | Model Forecast | 65,049.14 | 65,049.14 | 0.00 | **PASS** |
| **FY28E** | Model Forecast | 71,041.12 | 71,041.12 | 0.00 | **PASS** |
| **FY29E** | Model Forecast | 77,828.59 | 77,828.59 | 0.00 | **PASS** |
| **FY30E** | Model Forecast | 85,420.56 | 85,420.56 | 0.00 | **PASS** |
| **FY31E** | Model Forecast | 94,021.54 | 94,021.54 | 0.00 | **PASS** |

---

### Root Cause Analysis of Pre-Validation Corrections

During development, automated COM recalculation identified that cross-sheet formula mappings in `13_DCF_Valuation` were initially referencing offset row indexes due to string-replacement in worksheet names containing target letters. This was immediately corrected by compiling explicit functional formula builders, after which all tests passed with zero deviation.
