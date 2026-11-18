"""
Titan Company Ltd. - Historical Financial Analysis & Ratio Computation
Computes historical CAGR, margins, working capital cycle, turnover, and solvency ratios.
"""

import pandas as pd
import numpy as np

OUTPUT_DIR = 'data/processed'

df_pnl = pd.read_csv(f'{OUTPUT_DIR}/income_statement_standardized.csv', index_col=0)
df_bs = pd.read_csv(f'{OUTPUT_DIR}/balance_sheet_standardized.csv', index_col=0)

years = ['FY17', 'FY18', 'FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26']

ratios = pd.DataFrame(index=[
    'Revenue Growth Rate (%)',
    'Gross Profit Margin (%)',
    'EBITDA Margin (%)',
    'EBIT Margin (%)',
    'Net Profit Margin (%)',
    'Effective Tax Rate (%)',
    'Employee Cost (% of Revenue)',
    'Other Operating Exp (% of Revenue)',
    'Depreciation (% of Opening PP&E)',
    'Receivable Days (DSO)',
    'Inventory Days (DIO)',
    'Payable Days (DPO proxy)',
    'Cash Conversion Cycle (days)',
    'Dividend Payout Ratio (%)',
    'Return on Equity (ROE %)',
    'Return on Capital Employed (ROCE %)',
    'Debt to Equity Ratio (x)',
    'Interest Coverage Ratio (x)'
], columns=years)

for i, y in enumerate(years):
    rev = float(df_pnl.loc['Revenue from Operations', y])
    gp = float(df_pnl.loc['Gross Profit', y])
    cogs = float(df_pnl.loc['Cost of Goods Sold (COGS)', y])
    ebitda = float(df_pnl.loc['EBITDA', y])
    ebit = float(df_pnl.loc['EBIT (Operating Profit)', y])
    pbt = float(df_pnl.loc['Profit Before Tax (PBT)', y])
    tax = float(df_pnl.loc['Tax Expense', y])
    pat = float(df_pnl.loc['Net Income (PAT)', y])
    div = float(df_pnl.loc['Dividend Paid', y])
    emp = float(df_pnl.loc['Employee Benefit Expenses', y])
    other_exp = float(df_pnl.loc['Other Operating Expenses', y])
    interest = float(df_pnl.loc['Finance Costs (Interest)', y])
    
    eq = float(df_bs.loc['Total Shareholders Equity', y])
    debt = float(df_bs.loc['Total Borrowings (Debt)', y])
    rec = float(df_bs.loc['Trade Receivables (Debtors)', y])
    inv = float(df_bs.loc['Inventories', y])
    other_liab = float(df_bs.loc['Other Liabilities & Provisions', y])
    net_block = float(df_bs.loc['Property, Plant & Equipment (Net Block)', y])
    depr = float(df_pnl.loc['Depreciation & Amortization', y])
    
    # Revenue Growth
    if i > 0:
        prev_rev = float(df_pnl.loc['Revenue from Operations', years[i-1]])
        ratios.loc['Revenue Growth Rate (%)', y] = round((rev - prev_rev) / prev_rev * 100, 2)
    else:
        ratios.loc['Revenue Growth Rate (%)', y] = None
        
    ratios.loc['Gross Profit Margin (%)', y] = round(gp / rev * 100, 2)
    ratios.loc['EBITDA Margin (%)', y] = round(ebitda / rev * 100, 2)
    ratios.loc['EBIT Margin (%)', y] = round(ebit / rev * 100, 2)
    ratios.loc['Net Profit Margin (%)', y] = round(pat / rev * 100, 2)
    ratios.loc['Effective Tax Rate (%)', y] = round(tax / pbt * 100, 2) if pbt > 0 else 25.17
    ratios.loc['Employee Cost (% of Revenue)', y] = round(emp / rev * 100, 2)
    ratios.loc['Other Operating Exp (% of Revenue)', y] = round(other_exp / rev * 100, 2)
    
    # Depreciation % of opening PP&E
    if i > 0:
        prev_block = float(df_bs.loc['Property, Plant & Equipment (Net Block)', years[i-1]])
        ratios.loc['Depreciation (% of Opening PP&E)', y] = round(depr / prev_block * 100, 2)
    else:
        ratios.loc['Depreciation (% of Opening PP&E)', y] = round(depr / net_block * 100, 2)
        
    # DSO, DIO, DPO
    dso = rec / rev * 365
    dio = inv / cogs * 365 if cogs > 0 else 0
    # Proxy trade payables as ~60% of Other Liabilities
    payables_proxy = other_liab * 0.60
    dpo = payables_proxy / cogs * 365 if cogs > 0 else 0
    
    ratios.loc['Receivable Days (DSO)', y] = round(dso, 1)
    ratios.loc['Inventory Days (DIO)', y] = round(dio, 1)
    ratios.loc['Payable Days (DPO proxy)', y] = round(dpo, 1)
    ratios.loc['Cash Conversion Cycle (days)', y] = round(dso + dio - dpo, 1)
    
    ratios.loc['Dividend Payout Ratio (%)', y] = round(div / pat * 100, 2) if pat > 0 else 0.0
    ratios.loc['Return on Equity (ROE %)', y] = round(pat / eq * 100, 2) if eq > 0 else 0.0
    cap_emp = eq + debt
    ratios.loc['Return on Capital Employed (ROCE %)', y] = round(ebit / cap_emp * 100, 2) if cap_emp > 0 else 0.0
    ratios.loc['Debt to Equity Ratio (x)', y] = round(debt / eq, 2) if eq > 0 else 0.0
    ratios.loc['Interest Coverage Ratio (x)', y] = round(ebit / interest, 2) if interest > 0 else 0.0

ratios.to_csv(f'{OUTPUT_DIR}/historical_financial_ratios.csv')
print("Historical financial ratios computed:")
print(ratios[['FY22', 'FY23', 'FY24', 'FY25', 'FY26']])
