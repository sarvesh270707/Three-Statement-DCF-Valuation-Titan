"""
Project 02: Retail FP&A Budget vs Actual Dataset Generator
Generates realistic, granular, seasonal 24-month synthetic retail performance dataset.
"""

import numpy as np
import pandas as pd
import datetime
import os

OUTPUT_DIR = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/data'
PROCESSED_DIR = os.path.join(OUTPUT_DIR, 'processed')
RAW_DIR = os.path.join(OUTPUT_DIR, 'raw')
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

np.random.seed(42)

# Dimensions
regions = ['North', 'South', 'East', 'West']
categories = [
    'Electronics & Gadgets',
    'Fashion & Apparel',
    'Home & Living',
    'Footwear & Accessories',
    'Beauty & Personal Care',
    'Sports & Fitness'
]
channels = ['Flagship Store', 'High-Street Retail', 'Regional Mall Store']

# 24 Months: Jan 2025 to Dec 2026
dates = pd.date_range(start='2025-01-01', end='2026-12-31', freq='MS')

records = []
txn_id = 10001

# Category base metrics (Monthly revenue base, typical gross margin, expense structure)
cat_params = {
    'Electronics & Gadgets': {'base_rev': 4500000, 'gm': 0.18, 'mkt_pct': 0.04, 'dist_pct': 0.03, 'volatility': 0.08},
    'Fashion & Apparel': {'base_rev': 3800000, 'gm': 0.42, 'mkt_pct': 0.08, 'dist_pct': 0.04, 'volatility': 0.12},
    'Home & Living': {'base_rev': 2800000, 'gm': 0.35, 'mkt_pct': 0.05, 'dist_pct': 0.06, 'volatility': 0.09},
    'Footwear & Accessories': {'base_rev': 2200000, 'gm': 0.38, 'mkt_pct': 0.06, 'dist_pct': 0.04, 'volatility': 0.10},
    'Beauty & Personal Care': {'base_rev': 1900000, 'gm': 0.45, 'mkt_pct': 0.10, 'dist_pct': 0.03, 'volatility': 0.07},
    'Sports & Fitness': {'base_rev': 1600000, 'gm': 0.32, 'mkt_pct': 0.05, 'dist_pct': 0.04, 'volatility': 0.11}
}

# Regional multipliers
reg_multipliers = {
    'North': 1.15,
    'South': 1.10,
    'West': 1.20,
    'East': 0.85
}

# Monthly seasonality multipliers (Festive season in Oct/Nov/Dec, Summer wedding surge in May)
seasonality = {
    1: 0.90,  # Jan
    2: 0.88,  # Feb
    3: 0.95,  # Mar
    4: 1.00,  # Apr
    5: 1.08,  # May
    6: 0.92,  # Jun
    7: 0.94,  # Jul
    8: 1.02,  # Aug
    9: 1.05,  # Sep
    10: 1.35, # Oct (Diwali / Festive)
    11: 1.40, # Nov (Festive / Wedding)
    12: 1.25  # Dec (Year-end holiday)
}

for d in dates:
    year = d.year
    month = d.month
    season_factor = seasonality[month]
    # YoY organic growth in 2026 (+8%)
    yoy_factor = 1.08 if year == 2026 else 1.00
    
    for r in regions:
        reg_factor = reg_multipliers[r]
        for c in categories:
            cp = cat_params[c]
            for ch in channels:
                channel_factor = 1.25 if ch == 'Flagship Store' else (1.0 if ch == 'Regional Mall Store' else 0.85)
                
                # Base Budget calculation
                budget_rev = cp['base_rev'] * reg_factor * season_factor * yoy_factor * channel_factor
                # Add minor realistic planning variation
                budget_rev = round(budget_rev * np.random.uniform(0.97, 1.03), -2)
                
                # Budgeted Expenses
                budget_cogs = budget_rev * (1 - cp['gm'])
                budget_mkt = budget_rev * cp['mkt_pct']
                budget_personnel = budget_rev * 0.11
                budget_dist = budget_rev * cp['dist_pct']
                budget_other = budget_rev * 0.05
                budget_exp = round(budget_cogs + budget_mkt + budget_personnel + budget_dist + budget_other, -2)
                
                # Actual Performance Simulation
                # Introduce realistic FP&A variances:
                # 1. Festive months Oct-Nov beat revenue (+5% to +15%)
                # 2. Fashion in Q1 faced inventory discounting (-8% revenue, higher COGS)
                # 3. Electronics in Q3 2025 had supply chain freight cost overrun (+18% distribution)
                # 4. East region suffered monsoon disruption in July/Aug (-12% revenue)
                noise_rev = np.random.normal(0.01, cp['volatility'])
                if month in [10, 11]:
                    noise_rev += 0.06 # Festive outperformance
                elif month in [1, 2] and c == 'Fashion & Apparel':
                    noise_rev -= 0.07 # Discounting
                elif r == 'East' and month in [7, 8]:
                    noise_rev -= 0.08 # Monsoon drag
                    
                actual_rev = round(max(budget_rev * (1 + noise_rev), 100000), -2)
                
                # Actual Expenses Simulation
                cogs_noise = np.random.normal(0.01, 0.03)
                mkt_noise = np.random.normal(0.02, 0.06)
                dist_noise = np.random.normal(0.01, 0.05)
                
                # Specific cost overrun scenarios
                if c == 'Electronics & Gadgets' and year == 2025 and month in [7, 8, 9]:
                    dist_noise += 0.22 # Supply chain freight spike
                if month in [10, 11]:
                    mkt_noise += 0.15 # Festive ad campaign spend
                    
                actual_cogs = round(actual_rev * (1 - cp['gm']) * (1 + cogs_noise), -2)
                actual_mkt = round(budget_mkt * (1 + mkt_noise), -2)
                actual_personnel = round(budget_personnel * np.random.uniform(0.98, 1.04), -2)
                actual_dist = round(budget_dist * (actual_rev / budget_rev) * (1 + dist_noise), -2)
                actual_other = round(budget_other * np.random.uniform(0.97, 1.05), -2)
                actual_exp = actual_cogs + actual_mkt + actual_personnel + actual_dist + actual_other
                
                # Units and ASP
                asp = 25000 if c == 'Electronics & Gadgets' else (1800 if c == 'Fashion & Apparel' else (4500 if c == 'Home & Living' else (2200 if c == 'Footwear & Accessories' else (950 if c == 'Beauty & Personal Care' else 3200))))
                units_sold = int(round(actual_rev / asp))
                
                records.append({
                    'Transaction_ID': f"TXN-{txn_id}",
                    'Date': d.strftime('%Y-%m-%d'),
                    'Year': year,
                    'Month': month,
                    'Month_Name': d.strftime('%B'),
                    'Quarter': f"Q{d.quarter}",
                    'Region': r,
                    'Product_Category': c,
                    'Retail_Channel': ch,
                    'Units_Sold': units_sold,
                    'Average_Selling_Price': asp,
                    'Budgeted_Revenue': budget_rev,
                    'Actual_Revenue': actual_rev,
                    'Budgeted_Expenses': budget_exp,
                    'Actual_Expenses': actual_exp,
                    'Product_Cost_COGS': actual_cogs,
                    'Marketing_Expenses': actual_mkt,
                    'Personnel_Expenses': actual_personnel,
                    'Distribution_Expenses': actual_dist,
                    'Other_Operating_Expenses': actual_other,
                    'Budgeted_Profit': budget_rev - budget_exp,
                    'Actual_Profit': actual_rev - actual_exp,
                    'Revenue_Variance': actual_rev - budget_rev,
                    'Expense_Variance': actual_exp - budget_exp,
                    'Profit_Variance': (actual_rev - actual_exp) - (budget_rev - budget_exp)
                })
                txn_id += 1

df = pd.DataFrame(records)

# Save Raw and Processed Datasets
raw_file = os.path.join(RAW_DIR, 'retail_performance_raw.csv')
processed_file = os.path.join(PROCESSED_DIR, 'retail_performance_cleaned.csv')
excel_file = os.path.join(OUTPUT_DIR, 'Retail_Sector_Financial_Analysis.xlsx')

df.to_csv(raw_file, index=False)
df.to_csv(processed_file, index=False)

# Export to clean Excel
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='FactRetailPerformance', index=False)
    
    # Dimension Tables for Star Schema
    # DimDate
    dim_date = df[['Date', 'Year', 'Month', 'Month_Name', 'Quarter']].drop_duplicates().sort_values('Date')
    dim_date.to_excel(writer, sheet_name='DimDate', index=False)
    
    # DimRegion
    dim_region = pd.DataFrame({
        'Region': regions,
        'Regional_Director': ['Vikram Sharma', 'Ananya Sundaram', 'Amitava Ghosh', 'Rajesh Kulkarni'],
        'Regional_HQ': ['New Delhi', 'Bengaluru', 'Kolkata', 'Mumbai'],
        'Market_Tier': ['Tier 1 Core', 'Tier 1 Core', 'Tier 2 Emerging', 'Tier 1 Core']
    })
    dim_region.to_excel(writer, sheet_name='DimRegion', index=False)
    
    # DimProductCategory
    dim_cat = pd.DataFrame({
        'Product_Category': categories,
        'Division': ['Consumer Tech', 'Apparel & Lifestyle', 'Homegoods', 'Footwear', 'Health & Beauty', 'Activewear'],
        'Category_Lead': ['Rohan Mehra', 'Pooja Kapoor', 'Siddharth Nair', 'Kavita Reddy', 'Deepika Verma', 'Arjun Saxena'],
        'Target_Margin_Pct': [0.18, 0.42, 0.35, 0.38, 0.45, 0.32]
    })
    dim_cat.to_excel(writer, sheet_name='DimProductCategory', index=False)
    
    # Disclosures Sheet
    disclosures = pd.DataFrame({
        'Metadata Attribute': [
            'Dataset Nature', 'Simulated Timeframe', 'Transaction Count', 'Regions Covered',
            'Categories Covered', 'Reporting Unit', 'Methodology Notice', 'Primary Objective'
        ],
        'Specification': [
            'SYNTHETIC DEMONSTRATION DATA (Reproducible FP&A Portfolio Benchmark)',
            '24 Months (2025-01-01 to 2026-12-31)',
            f'{len(df)} Granular Records',
            '4 Geographical Zones (North, South, East, West)',
            '6 Retail Product Segments',
            'INR (₹) in Full Values',
            'Generated via Monte Carlo Gaussian distribution with seasonal multipliers',
            'Budget vs Actual Variance Analysis, Power BI Star-Schema Modeling & DAX Calculation'
        ]
    })
    disclosures.to_excel(writer, sheet_name='Data_Disclosures', index=False)

# Also mirror to data/Retail_Sector_Financial_Analysis.xlsx
os.makedirs('data', exist_ok=True)
import shutil
shutil.copyfile(excel_file, 'data/Retail_Sector_Financial_Analysis.xlsx')

print(f"Retail dataset successfully generated and saved:")
print(f"  Rows: {len(df)}")
print(f"  Excel Deliverable: {excel_file}")
print(f"  Total Budget Revenue: INR {df['Budgeted_Revenue'].sum():,.2f}")
print(f"  Total Actual Revenue: INR {df['Actual_Revenue'].sum():,.2f}")
print(f"  Total Revenue Variance: INR {df['Revenue_Variance'].sum():,.2f}")
print(f"  Total Actual Profit: INR {df['Actual_Profit'].sum():,.2f}")
