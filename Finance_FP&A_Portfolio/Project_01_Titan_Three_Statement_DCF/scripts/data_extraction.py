"""
Titan Company Ltd. - Financial Data Extraction Script
Extracts 10 years (FY17 - FY26) of historical consolidated financial statements from primary Screener / Annual Report extracts.
"""

import openpyxl
import pandas as pd
import json
import os

RAW_PATH = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/raw/Titan_Company_Screener_Raw.xlsx'
OUTPUT_DIR = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/processed'
SOURCE_DIR = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/source_register'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SOURCE_DIR, exist_ok=True)

wb = openpyxl.load_workbook(RAW_PATH, data_only=True)
ws = wb['Data Sheet']

years = ['FY17', 'FY18', 'FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26']
year_cols = {y: idx + 2 for idx, y in enumerate(years)}

def extract_section(start_row, end_row):
    section_data = {}
    for r in range(start_row, end_row + 1):
        metric = ws.cell(row=r, column=1).value
        if metric is not None and str(metric).strip():
            m_name = str(metric).strip()
            row_vals = {}
            for y, c in year_cols.items():
                val = ws.cell(row=r, column=c).value
                row_vals[y] = float(val) if val is not None and isinstance(val, (int, float)) else (str(val) if val is not None else 0.0)
            section_data[m_name] = row_vals
    return pd.DataFrame(section_data).T

# 1. Income Statement (Rows 16 to 31)
df_pnl = extract_section(16, 31)
df_pnl.to_csv(f'{OUTPUT_DIR}/income_statement_historical.csv')

# 2. Balance Sheet (Rows 56 to 72)
df_bs = extract_section(56, 72)
df_bs.to_csv(f'{OUTPUT_DIR}/balance_sheet_historical.csv')

# 3. Cash Flow Statement (Rows 81 to 85)
df_cf = extract_section(81, 85)
df_cf.to_csv(f'{OUTPUT_DIR}/cash_flow_historical.csv')

# 4. Meta Information
meta_data = {
    'Company Name': ws.cell(row=1, column=2).value,
    'Face Value': ws.cell(row=7, column=2).value,
    'Current Market Price (INR)': ws.cell(row=8, column=2).value,
    'Market Capitalization (INR Cr)': ws.cell(row=9, column=2).value,
    'Number of Equity Shares': ws.cell(row=70, column=11).value,
    'Latest Audited Fiscal Year': 'FY26 (Ended 31-Mar-2026)',
    'Forecast Horizon': 'FY27E - FY31E (5 Years)'
}
with open(f'{OUTPUT_DIR}/company_metadata.json', 'w') as f:
    json.dump(meta_data, f, indent=2)

print("Data extraction complete:")
print("Income Statement shape:", df_pnl.shape)
print("Balance Sheet shape:", df_bs.shape)
print("Cash Flow shape:", df_cf.shape)
print("Metadata:", meta_data)
