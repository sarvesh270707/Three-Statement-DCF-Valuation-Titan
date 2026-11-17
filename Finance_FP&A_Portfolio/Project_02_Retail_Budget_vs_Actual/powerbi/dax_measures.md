# Project 02: Retail FP&A | Comprehensive DAX Measure Catalog

---

### Executive Overview

This repository document contains the complete, production-grade Data Analysis Expressions (DAX) measure suite developed for the **Retail Budget vs. Actual Variance & Profitability Dashboard** (`Retail_BvA_Dashboard.pbix`).

All measures are architected to strictly adhere to enterprise Power BI best practices:
1. **Dynamic Context Sensitivity**: Measures evaluate correctly across all slicer combinations (Date, Region, Product Category, Retail Channel).
2. **Defensive Division**: All division operations utilize the `DIVIDE(numerator, denominator, alternateResult)` pattern to eliminate `NaN` or `#DIV/0!` runtime exceptions.
3. **Consistent Accounting Logic**:
   - Favourable variance: Actual Revenue > Budget Revenue; Actual Expenses < Budget Expenses; Actual Profit > Budget Profit.
   - Unfavourable variance: Actual Revenue < Budget Revenue; Actual Expenses > Budget Expenses; Actual Profit < Budget Profit.

---

### 1. Revenue Measures

#### 1.1 Total Budget Revenue
```dax
Total Budget Revenue = 
SUM(FactRetailPerformance[Budgeted_Revenue])
```
*Description*: Calculates the aggregate planned revenue across the active filter context.  
*Format*: Currency (`₹#,##0`)

#### 1.2 Total Actual Revenue
```dax
Total Actual Revenue = 
SUM(FactRetailPerformance[Actual_Revenue])
```
*Description*: Calculates the aggregate gross actual revenue realized across stores and channels.  
*Format*: Currency (`₹#,##0`)

#### 1.3 Revenue Variance
```dax
Revenue Variance = 
[Total Actual Revenue] - [Total Budget Revenue]
```
*Description*: Measures the absolute rupee surplus or shortfall against planned top-line targets.  
*Format*: Currency (`₹#,##0`)

#### 1.4 Revenue Variance %
```dax
Revenue Variance % = 
DIVIDE(
    [Revenue Variance],
    [Total Budget Revenue],
    0.0
)
```
*Description*: Relative percentage deviation against planned revenue baseline.  
*Format*: Percentage (`0.0%`)

#### 1.5 Revenue Achievement %
```dax
Revenue Achievement % = 
DIVIDE(
    [Total Actual Revenue],
    [Total Budget Revenue],
    0.0
)
```
*Description*: Budget attainment percentage (values > 100% indicate target outperformance).  
*Format*: Percentage (`0.0%`)

---

### 2. Expense & Cost Management Measures

#### 2.1 Total Budget Expenses
```dax
Total Budget Expenses = 
SUM(FactRetailPerformance[Budgeted_Expenses])
```
*Description*: Aggregate operating expenses budgeted across categories and regions.  
*Format*: Currency (`₹#,##0`)

#### 2.2 Total Actual Expenses
```dax
Total Actual Expenses = 
SUM(FactRetailPerformance[Actual_Expenses])
```
*Description*: Aggregate actual costs incurred (COGS + Marketing + Personnel + Freight + Other).  
*Format*: Currency (`₹#,##0`)

#### 2.3 Expense Variance
```dax
Expense Variance = 
[Total Actual Expenses] - [Total Budget Expenses]
```
*Description*: Absolute rupee overrun (positive) or savings (negative) vs plan.  
*Format*: Currency (`₹#,##0`)

#### 2.4 Expense Variance %
```dax
Expense Variance % = 
DIVIDE(
    [Expense Variance],
    [Total Budget Expenses],
    0.0
)
```
*Description*: Percentage cost deviation. In FP&A convention, positive denotes an overrun (unfavourable).  
*Format*: Percentage (`0.0%`)

#### 2.5 Cost Overrun Alert
```dax
Cost Overrun Alert = 
IF(
    [Total Actual Expenses] > [Total Budget Expenses],
    "Cost Overrun",
    "On Track"
)
```
*Description*: Conditional alert indicator flagging operational cost creep.

---

### 3. Profitability & Margin Measures

#### 3.1 Budgeted Profit
```dax
Budgeted Profit = 
[Total Budget Revenue] - [Total Budget Expenses]
```
*Description*: Target operating profit modeled during annual operational planning.  
*Format*: Currency (`₹#,##0`)

#### 3.2 Actual Profit
```dax
Actual Profit = 
[Total Actual Revenue] - [Total Actual Expenses]
```
*Description*: Realized operating profit before corporate overhead and tax allocations.  
*Format*: Currency (`₹#,##0`)

#### 3.3 Profit Variance
```dax
Profit Variance = 
[Actual Profit] - [Budgeted Profit]
```
*Description*: Net bottom-line impact. Positive denotes bottom-line expansion (favourable).  
*Format*: Currency (`₹#,##0`)

#### 3.4 Actual Profit Margin
```dax
Actual Profit Margin = 
DIVIDE(
    [Actual Profit],
    [Total Actual Revenue],
    0.0
)
```
*Description*: Operating profit margin realized on actual net sales.  
*Format*: Percentage (`0.0%`)

#### 3.5 Budget Profit Margin
```dax
Budget Profit Margin = 
DIVIDE(
    [Budgeted Profit],
    [Total Budget Revenue],
    0.0
)
```
*Description*: Benchmark operating margin target.  
*Format*: Percentage (`0.0%`)

#### 3.6 Profitability Status
```dax
Profitability Status = 
IF(
    [Actual Profit] >= [Budgeted Profit],
    "Above Budget",
    "Below Budget"
)
```
*Description*: High-level performance status badge for executive reporting.

#### 3.7 Variance Status
```dax
Variance Status = 
SWITCH(
    TRUE(),
    [Profit Variance] > 0, "Favourable",
    [Profit Variance] < 0, "Unfavourable",
    "On Plan"
)
```
*Description*: Multi-condition variance classification driving matrix traffic-light formatting.

---

### 4. Independent Validation Cross-Reference

Every measure was independently calculated and cross-verified via Python in `independent_dax_validation.py`. At the aggregate enterprise level:
- **Total Budget Revenue**: ₹5,93,19,76,900 (₹593.20 Cr)
- **Total Actual Revenue**: ₹6,04,79,61,200 (₹604.80 Cr)
- **Revenue Variance**: +₹11,59,84,300 (+1.96% | Favourable)
- **Total Actual Expenses**: ₹5,65,13,77,800 (₹565.14 Cr vs Budget ₹550.42 Cr)
- **Expense Variance**: +₹14,72,08,700 (+2.67% | Cost Overrun)
- **Actual Profit**: ₹39,65,83,400 (6.56% margin vs Budget 7.21%)
- **Profit Variance**: -₹3,12,24,400 (-7.30% | Unfavourable due to supply chain freight spikes)
