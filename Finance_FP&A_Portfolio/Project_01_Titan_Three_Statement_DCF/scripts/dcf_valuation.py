"""
Titan Company Ltd. - Institutional DCF Valuation Engine
Implements both Normalized Gordon Growth (Steady-State Reinvestment) and EV/EBITDA Exit Multiple methodologies.
"""

import json
import pandas as pd
import numpy as np

# Load parameters
with open('Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/processed/model_assumptions.json', 'r') as f:
    scenarios = json.load(f)

base = scenarios['Base']

# WACC Build-up
rf = base['Rf']
erp = base['ERP']
beta = base['Beta']
ke = rf + beta * erp
kd_pre = base['Cost_of_Debt_PreTax']
tax_rate = base['Tax_Rate']
kd_post = kd_pre * (1 - tax_rate)

shares_cr = 88.778616
cmp = 4910.0
mcap = shares_cr * cmp
debt_fy26 = 30621.0
cash_fy26 = 1917.0
inv_fy26 = 3506.0
net_debt_fy26 = debt_fy26 - cash_fy26 - inv_fy26

tot_cap = mcap + debt_fy26
we = mcap / tot_cap
wd = debt_fy26 / tot_cap
wacc = we * ke + wd * kd_post

years = ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']
sales_base = [100721.6, 114822.6, 129749.6, 145319.5, 162757.9]
ebitda_base = [sales * base['EBITDA_Margin'] for sales in sales_base]
depr_base = [1238.0, 1468.9, 1720.0, 1993.6, 2291.6]
ebit_base = [ebitda - depr for ebitda, depr in zip(ebitda_base, depr_base)]
nopat_base = [ebit * (1 - tax_rate) for ebit in ebit_base]
capex_base = [sales * base['Capex_Pct_Revenue'] for sales in sales_base]

cogs_base = [sales * (1 - base['Gross_Margin']) for sales in sales_base]
rec_base = [sales / 365.0 * base['DSO'] for sales in sales_base]
inv_base = [cogs / 365.0 * base['DIO'] for cogs in cogs_base]
pay_base = [cogs / 365.0 * base['DPO'] for cogs in cogs_base]
owc_base = [r + i - p for r, i, p in zip(rec_base, inv_base, pay_base)]

fy26_cogs = 70307.0
fy26_owc = 916.0 + 42743.0 - (fy26_cogs / 365.0 * 44.3)

delta_owc = []
prev_owc = fy26_owc
for owc in owc_base:
    delta_owc.append(owc - prev_owc)
    prev_owc = owc

ufcf_base = []
for i in range(len(years)):
    ufcf = nopat_base[i] + depr_base[i] - capex_base[i] - delta_owc[i]
    ufcf_base.append(ufcf)

discount_factors = [1 / ((1 + wacc) ** (t + 1)) for t in range(len(years))]
pv_ufcf = [ufcf * df for ufcf, df in zip(ufcf_base, discount_factors)]
sum_pv_ufcf = sum(pv_ufcf)

# Terminal Value Method 1: Normalized Steady-State Gordon Growth
# In terminal state, steady-state reinvestment = g / Terminal ROIC (assuming conservative steady-state ROIC of 20%)
g = base['Terminal_Growth']
terminal_roic = 0.20
reinvestment_rate_term = g / terminal_roic # 0.055 / 0.20 = 27.5%
terminal_nopat = nopat_base[-1] * (1 + g)
terminal_normalized_ufcf = terminal_nopat * (1 - reinvestment_rate_term)
tv_gordon = terminal_normalized_ufcf / (wacc - g)
pv_tv_gordon = tv_gordon * discount_factors[-1]

ev_gordon = sum_pv_ufcf + pv_tv_gordon
equity_val_gordon = ev_gordon - net_debt_fy26
implied_share_price_gordon = equity_val_gordon / shares_cr

# Terminal Value Method 2: EV/EBITDA Exit Multiple
# High-growth consumer discretionary leader in India trades at 35x - 45x EBITDA
exit_multiple = base['Exit_Multiple'] # 35.0x
tv_multiple = ebitda_base[-1] * exit_multiple
pv_tv_multiple = tv_multiple * discount_factors[-1]

ev_multiple = sum_pv_ufcf + pv_tv_multiple
equity_val_multiple = ev_multiple - net_debt_fy26
implied_share_price_multiple = equity_val_multiple / shares_cr

# Exit Multiple at 42.0x (Bull/Consensus High)
tv_multiple_42 = ebitda_base[-1] * 42.0
pv_tv_multiple_42 = tv_multiple_42 * discount_factors[-1]
ev_multiple_42 = sum_pv_ufcf + pv_tv_multiple_42
equity_val_42 = ev_multiple_42 - net_debt_fy26
implied_share_price_42 = equity_val_42 / shares_cr

# Valuation Summary DataFrame
summary_data = {
    'Methodology': [
        'Normalized Gordon Growth (g=5.5%, ROIC=20%)',
        'Exit Multiple (35.0x FY31E EBITDA)',
        'Exit Multiple (42.0x FY31E EBITDA)',
        'Current Market Price (TITAN.NS)'
    ],
    'PV of Forecast UFCF (INR Cr)': [sum_pv_ufcf, sum_pv_ufcf, sum_pv_ufcf, np.nan],
    'Terminal Value (INR Cr)': [tv_gordon, tv_multiple, tv_multiple_42, np.nan],
    'PV of Terminal Value (INR Cr)': [pv_tv_gordon, pv_tv_multiple, pv_tv_multiple_42, np.nan],
    'Enterprise Value (INR Cr)': [ev_gordon, ev_multiple, ev_multiple_42, np.nan],
    'Less: Net Debt (INR Cr)': [net_debt_fy26, net_debt_fy26, net_debt_fy26, np.nan],
    'Implied Equity Value (INR Cr)': [equity_val_gordon, equity_val_multiple, equity_val_42, mcap],
    'Implied Share Price (INR)': [
        round(implied_share_price_gordon, 2),
        round(implied_share_price_multiple, 2),
        round(implied_share_price_42, 2),
        cmp
    ],
    'Premium / (Discount) vs CMP (%)': [
        round((implied_share_price_gordon - cmp) / cmp * 100, 2),
        round((implied_share_price_multiple - cmp) / cmp * 100, 2),
        round((implied_share_price_42 - cmp) / cmp * 100, 2),
        0.0
    ]
}

df_summary = pd.DataFrame(summary_data)
df_summary.to_csv('Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/outputs/valuation_summary.csv', index=False)

print("--- VALUATION SUMMARY TABLE ---")
print(df_summary.to_string())

# 5x5 Sensitivity Matrix for Exit Multiple (WACC vs Exit Multiple)
wacc_steps = [wacc - 0.01, wacc - 0.005, wacc, wacc + 0.005, wacc + 0.01]
multiple_steps = [28.0, 32.0, 35.0, 40.0, 45.0]

sens_matrix = pd.DataFrame(index=[f"WACC {w*100:.2f}%" for w in wacc_steps],
                           columns=[f"{m:.1f}x EBITDA" for m in multiple_steps])

for w_val in wacc_steps:
    dfs = [1 / ((1 + w_val) ** (t + 1)) for t in range(len(years))]
    pv_cash = sum([ufcf * df for ufcf, df in zip(ufcf_base, dfs)])
    for m_val in multiple_steps:
        tv = ebitda_base[-1] * m_val
        pv_tv = tv * dfs[-1]
        ev_s = pv_cash + pv_tv
        eq_s = ev_s - net_debt_fy26
        p_s = eq_s / shares_cr
        sens_matrix.loc[f"WACC {w_val*100:.2f}%", f"{m_val:.1f}x EBITDA"] = round(p_s, 2)

sens_matrix.to_csv('Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/outputs/sensitivity_matrix_exit_multiple.csv')
print("\n--- 5x5 SENSITIVITY MATRIX (WACC vs Exit Multiple) ---")
print(sens_matrix)
