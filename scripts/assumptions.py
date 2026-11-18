"""
Titan Company Ltd. - Valuation Assumptions & Scenario Framework
Defines Bear, Base, and Bull operational drivers, WACC parameters, and terminal value assumptions.
"""

import json

SCENARIOS = {
    'Base': {
        'Description': 'Consensus expansion: Steady luxury retail market share gain, store additions, 15% fading to 12% growth.',
        'Revenue_Growth': [0.15, 0.14, 0.13, 0.12, 0.12], # FY27E to FY31E
        'Gross_Margin': 0.225,
        'EBITDA_Margin': 0.105,
        'Employee_Exp_Pct': 0.033,
        'Other_OpExp_Pct': 0.087,
        'Depr_Pct_Opening_PPE': 0.180,
        'Capex_Pct_Revenue': 0.025,
        'Tax_Rate': 0.2517,
        'DSO': 5.0,
        'DIO': 205.0,
        'DPO': 42.0,
        'Dividend_Payout': 0.28,
        'Cost_of_Debt_PreTax': 0.075,
        'Rf': 0.070,
        'ERP': 0.070,
        'Beta': 1.15,
        'Terminal_Growth': 0.055,
        'Exit_Multiple': 35.0
    },
    'Bear': {
        'Description': 'Macro slowdown: Gold price volatility, consumer demand moderation, intensified retail competition.',
        'Revenue_Growth': [0.10, 0.09, 0.09, 0.08, 0.08],
        'Gross_Margin': 0.205,
        'EBITDA_Margin': 0.085,
        'Employee_Exp_Pct': 0.036,
        'Other_OpExp_Pct': 0.095,
        'Depr_Pct_Opening_PPE': 0.180,
        'Capex_Pct_Revenue': 0.020,
        'Tax_Rate': 0.2517,
        'DSO': 6.0,
        'DIO': 220.0,
        'DPO': 40.0,
        'Dividend_Payout': 0.25,
        'Cost_of_Debt_PreTax': 0.080,
        'Rf': 0.070,
        'ERP': 0.070,
        'Beta': 1.20,
        'Terminal_Growth': 0.050,
        'Exit_Multiple': 28.0
    },
    'Bull': {
        'Description': 'Accelerated formalization: High wedding season demand, Mia & Caratlane rapid scale, international expansion.',
        'Revenue_Growth': [0.20, 0.18, 0.17, 0.16, 0.15],
        'Gross_Margin': 0.245,
        'EBITDA_Margin': 0.120,
        'Employee_Exp_Pct': 0.030,
        'Other_OpExp_Pct': 0.080,
        'Depr_Pct_Opening_PPE': 0.180,
        'Capex_Pct_Revenue': 0.030,
        'Tax_Rate': 0.2517,
        'DSO': 4.5,
        'DIO': 190.0,
        'DPO': 45.0,
        'Dividend_Payout': 0.30,
        'Cost_of_Debt_PreTax': 0.072,
        'Rf': 0.070,
        'ERP': 0.070,
        'Beta': 1.10,
        'Terminal_Growth': 0.060,
        'Exit_Multiple': 42.0
    }
}

OUTPUT_FILE = 'data/processed/model_assumptions.json'

with open(OUTPUT_FILE, 'w') as f:
    json.dump(SCENARIOS, f, indent=2)

print("Model assumptions and scenario framework saved successfully.")
for s, v in SCENARIOS.items():
    ke = v['Rf'] + v['Beta'] * v['ERP']
    kd_post = v['Cost_of_Debt_PreTax'] * (1 - v['Tax_Rate'])
    print(f"Scenario: {s} | Ke: {ke*100:.2f}% | Kd(after-tax): {kd_post*100:.2f}% | Term Growth: {v['Terminal_Growth']*100:.1f}%")
