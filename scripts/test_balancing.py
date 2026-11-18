"""
Three-Statement Model Simulation and Balancing Engine
Verifies non-circular accounting integration and zero balance-sheet deviation.
"""

import json
import pandas as pd
import numpy as np

OUTPUT_DIR = 'data/processed'

with open(f'{OUTPUT_DIR}/model_assumptions.json', 'r') as f:
    scenarios = json.load(f)

base = scenarios['Base']

# Historical FY26 starting balances (in INR Cr)
fy26_sales = 87584.0
fy26_cogs = 70307.0
fy26_rec = 916.0
fy26_inv = 42743.0
fy26_cash = 1917.0
fy26_other_assets = 4438.0
fy26_net_block = 6878.0
fy26_cwip = 163.0
fy26_investments = 3506.0
fy26_tot_assets = 60561.0

fy26_share_cap = 89.0
fy26_reserves = 15614.0
fy26_tot_eq = 15703.0
fy26_debt = 30621.0
fy26_other_liab = 14237.0
# Split other liab into Operating Payables (44.3 days DPO proxy = ~8,533) and Non-Operating Other Liab (~5,704)
dpo_initial = 44.3
fy26_op_payables = round(fy26_cogs / 365.0 * dpo_initial, 2)
fy26_non_op_liab = fy26_other_liab - fy26_op_payables
fy26_tot_liab_eq = fy26_tot_eq + fy26_debt + fy26_other_liab

print(f"FY26 Initial Balance Check: Assets={fy26_tot_assets}, Liab&Eq={fy26_tot_liab_eq}, Diff={fy26_tot_assets - fy26_tot_liab_eq}")

forecast_years = ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']

sim_results = {}

for sc_name, p in scenarios.items():
    print(f"\n=================== RUNNING SCENARIO: {sc_name} ===================")
    rows_pnl = []
    rows_bs = []
    rows_cf = []
    
    # State tracking
    prev_sales = fy26_sales
    prev_rec = fy26_rec
    prev_inv = fy26_inv
    prev_pay = fy26_op_payables
    prev_cash = fy26_cash
    prev_net_block = fy26_net_block
    prev_reserves = fy26_reserves
    prev_debt = fy26_debt
    other_inc = 450.0
    
    for i, y in enumerate(forecast_years):
        g = p['Revenue_Growth'][i]
        sales = prev_sales * (1 + g)
        cogs = sales * (1 - p['Gross_Margin'])
        gp = sales - cogs
        emp_exp = sales * p['Employee_Exp_Pct']
        other_opex = sales * p['Other_OpExp_Pct']
        tot_opex = emp_exp + other_opex
        ebitda = gp - tot_opex
        
        # PP&E Schedule
        depr = prev_net_block * p['Depr_Pct_Opening_PPE']
        capex = sales * p['Capex_Pct_Revenue']
        net_block = prev_net_block + capex - depr
        
        ebit = ebitda - depr
        other_inc = other_inc * 1.05
        
        # Debt & Interest Schedule (Stable debt / refinancing)
        debt = prev_debt # stable capital structure
        interest = prev_debt * p['Cost_of_Debt_PreTax']
        
        pbt = ebit + other_inc - interest
        tax = pbt * p['Tax_Rate']
        pat = pbt - tax
        dividends = pat * p['Dividend_Payout']
        retained = pat - dividends
        
        # Working Capital Schedule
        rec = sales / 365.0 * p['DSO']
        inv = cogs / 365.0 * p['DIO']
        pay = cogs / 365.0 * p['DPO']
        
        delta_rec = rec - prev_rec
        delta_inv = inv - prev_inv
        delta_pay = pay - prev_pay
        delta_wc = delta_rec + delta_inv - delta_pay
        
        # Cash Flow Statement
        # OCF = PAT + Depr - delta_rec - delta_inv + delta_pay
        cfo = pat + depr - delta_rec - delta_inv + delta_pay
        # ICF = -Capex
        cfi = -capex
        # CFF = -Dividends + Net Borrowing (0)
        cff = -dividends
        net_cash_flow = cfo + cfi + cff
        closing_cash = prev_cash + net_cash_flow
        
        # Balance Sheet
        # Assets
        tot_assets = closing_cash + rec + inv + fy26_other_assets + net_block + fy26_cwip + fy26_investments
        
        # Equity & Liab
        reserves = prev_reserves + retained
        tot_eq = fy26_share_cap + reserves
        tot_liab_eq = tot_eq + debt + pay + fy26_non_op_liab
        
        bs_check = tot_assets - tot_liab_eq
        
        print(f"{y}: Sales={sales:,.0f}, EBITDA={ebitda:,.0f}, PAT={pat:,.0f}, CFO={cfo:,.0f}, Cash={closing_cash:,.0f}, BS Check={bs_check:.2f}")
        assert abs(bs_check) < 0.01, f"Balance sheet does not balance in {y}! Diff={bs_check}"
        
        # Update state for next year
        prev_sales = sales
        prev_rec = rec
        prev_inv = inv
        prev_pay = pay
        prev_cash = closing_cash
        prev_net_block = net_block
        prev_reserves = reserves
        prev_debt = debt
