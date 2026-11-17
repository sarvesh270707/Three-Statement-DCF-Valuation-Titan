"""
Titan Company Ltd. - Supporting Schedules Generator
Extracts and summarizes Working Capital, PP&E, and Debt schedules for reporting.
"""

import pandas as pd
import openpyxl

MODEL_PATH = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/model/Titan_3Statement_DCF_Model.xlsx'
OUTPUT_DIR = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/outputs'

wb = openpyxl.load_workbook(MODEL_PATH, data_only=True)

def read_sheet_to_df(sheet_name, start_row, end_row, start_col=2, end_col=8):
    ws = wb[sheet_name]
    headers = [ws.cell(row=4, column=c).value for c in range(start_col, end_col + 1)]
    data = []
    for r in range(start_row, end_row + 1):
        row_vals = [ws.cell(row=r, column=c).value for c in range(start_col, end_col + 1)]
        if any(v is not None for v in row_vals):
            data.append(row_vals)
    return pd.DataFrame(data, columns=headers)

df_wc = read_sheet_to_df('06_Working_Capital', 5, 9)
df_ppe = read_sheet_to_df('07_PP&E_Schedule', 5, 9)
df_debt = read_sheet_to_df('08_Debt_Schedule', 5, 10)

df_wc.to_csv(f'{OUTPUT_DIR}/working_capital_schedule_summary.csv', index=False)
df_ppe.to_csv(f'{OUTPUT_DIR}/ppe_schedule_summary.csv', index=False)
df_debt.to_csv(f'{OUTPUT_DIR}/debt_schedule_summary.csv', index=False)

print("Supporting schedules successfully exported to CSV.")
print("\nWorking Capital Schedule Summary:")
print(df_wc.to_string())
print("\nPP&E Schedule Summary:")
print(df_ppe.to_string())
print("\nDebt Schedule Summary:")
print(df_debt.to_string())
