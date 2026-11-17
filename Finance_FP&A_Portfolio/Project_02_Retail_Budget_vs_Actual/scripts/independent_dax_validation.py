"""
Project 02: Independent DAX & KPI Validation Engine
Independently replicates Power BI DAX calculations using Python/pandas to test filter context and verify mathematical accuracy.
"""

import pandas as pd
import numpy as np
import json
import os

DATA_PATH = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/data/processed/retail_performance_cleaned.csv'
POWERBI_DIR = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/powerbi'
DOC_DIR = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/documentation'
os.makedirs(POWERBI_DIR, exist_ok=True)
os.makedirs(DOC_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

def calculate_dax_kpis(subset):
    b_rev = subset['Budgeted_Revenue'].sum()
    a_rev = subset['Actual_Revenue'].sum()
    rev_var = a_rev - b_rev
    rev_var_pct = rev_var / b_rev if b_rev != 0 else 0.0
    
    b_exp = subset['Budgeted_Expenses'].sum()
    a_exp = subset['Actual_Expenses'].sum()
    exp_var = a_exp - b_exp
    exp_var_pct = exp_var / b_exp if b_exp != 0 else 0.0
    
    b_prof = b_rev - b_exp
    a_prof = a_rev - a_exp
    prof_var = a_prof - b_prof
    
    a_margin = a_prof / a_rev if a_rev != 0 else 0.0
    b_margin = b_prof / b_rev if b_rev != 0 else 0.0
    
    rev_achieve = a_rev / b_rev if b_rev != 0 else 0.0
    cost_alert = "Cost Overrun" if a_exp > b_exp else "On Track"
    profit_status = "Above Budget" if a_prof >= b_prof else "Below Budget"
    
    if prof_var > 0:
        var_status = "Favourable"
    elif prof_var < 0:
        var_status = "Unfavourable"
    else:
        var_status = "On Plan"
        
    return {
        'Total Budget Revenue': b_rev,
        'Total Actual Revenue': a_rev,
        'Revenue Variance': rev_var,
        'Revenue Variance %': rev_var_pct,
        'Total Budget Expenses': b_exp,
        'Total Actual Expenses': a_exp,
        'Expense Variance': exp_var,
        'Expense Variance %': exp_var_pct,
        'Budgeted Profit': b_prof,
        'Actual Profit': a_prof,
        'Profit Variance': prof_var,
        'Actual Profit Margin': a_margin,
        'Budget Profit Margin': b_margin,
        'Revenue Achievement %': rev_achieve,
        'Cost Overrun Alert': cost_alert,
        'Profitability Status': profit_status,
        'Variance Status': var_status
    }

# 1. Overall Company Level KPIs
overall_kpis = calculate_dax_kpis(df)

# 2. Regional Breakdown
regional_kpis = {}
for r in df['Region'].unique():
    regional_kpis[r] = calculate_dax_kpis(df[df['Region'] == r])
df_regional = pd.DataFrame(regional_kpis).T

# 3. Category Breakdown
category_kpis = {}
for c in df['Product_Category'].unique():
    category_kpis[c] = calculate_dax_kpis(df[df['Product_Category'] == c])
df_category = pd.DataFrame(category_kpis).T

# 4. Yearly Breakdown
yearly_kpis = {}
for y in df['Year'].unique():
    yearly_kpis[str(y)] = calculate_dax_kpis(df[df['Year'] == y])
df_yearly = pd.DataFrame(yearly_kpis).T

print("=== OVERALL COMPANY DAX MEASURE AUDIT ===")
for k, v in overall_kpis.items():
    if isinstance(v, float) and '%' in k:
        print(f"  {k}: {v*100:.2f}%")
    elif isinstance(v, (int, float)):
        print(f"  {k}: INR {v:,.2f}")
    else:
        print(f"  {k}: {v}")

print("\n=== REGIONAL PROFITABILITY & MARGINS ===")
print(df_regional[['Total Actual Revenue', 'Actual Profit', 'Actual Profit Margin', 'Revenue Achievement %', 'Variance Status']])

print("\n=== PRODUCT CATEGORY PROFITABILITY ===")
print(df_category[['Total Actual Revenue', 'Actual Profit', 'Actual Profit Margin', 'Revenue Achievement %', 'Cost Overrun Alert']])

# Export validation audit outputs
df_regional.to_csv(f'{POWERBI_DIR}/regional_dax_validation.csv')
df_category.to_csv(f'{POWERBI_DIR}/category_dax_validation.csv')
df_yearly.to_csv(f'{POWERBI_DIR}/yearly_dax_validation.csv')

with open(f'{POWERBI_DIR}/overall_dax_kpis.json', 'w') as f:
    json.dump(overall_kpis, f, indent=2)

print(f"\nDAX measure validation artifacts successfully exported to {POWERBI_DIR}/")
