"""
Titan Company Ltd. - Financial Model Validation & Native Recalculation Engine
Uses Microsoft Excel COM automation to recalculate all formula cells and audit reconciliation checks.
"""

import win32com.client
import os
import pandas as pd
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
MODEL_PATH = os.path.join(ROOT_DIR, 'model', 'Titan_3Statement_DCF_Model.xlsx')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Opening Excel workbook for native recalculation:\n{MODEL_PATH}")

excel = win32com.client.DispatchEx("Excel.Application")
excel.Visible = False
excel.DisplayAlerts = False

validation_records = []

try:
    wb = excel.Workbooks.Open(MODEL_PATH)
    excel.CalculateFull() # Force full formula recalculation across entire workbook
    
    # 1. Audit 16_Model_Checks
    ws_checks = wb.Worksheets("16_Model_Checks")
    print("\n--- AUDIT CHECKS STATUS ---")
    for r in range(5, 12):
        check_name = ws_checks.Cells(r, 2).Value
        sched = ws_checks.Cells(r, 3).Value
        status = ws_checks.Cells(r, 4).Value
        tol = ws_checks.Cells(r, 5).Value
        dev = ws_checks.Cells(r, 6).Value
        rule = ws_checks.Cells(r, 7).Value
        
        print(f"[{status}] {check_name} | Max Dev: {dev} | Sched: {sched}")
        validation_records.append({
            'Test Category': 'Reconciliation Check',
            'Test Name': check_name,
            'Schedule': sched,
            'Period': 'All Periods (FY26-FY31E)',
            'Expected Result': 0.00 if tol == 0.01 else 'PASS',
            'Actual Result': dev if tol == 0.01 else status,
            'Difference': dev if tol == 0.01 else 0.00,
            'Pass/Fail Status': status,
            'Audit Criteria': rule,
            'Timestamp': datetime.datetime.now().isoformat()
        })
        
    # 2. Period-by-period Balance Sheet equality
    print("\n--- PERIOD-BY-PERIOD BALANCE SHEET EQUALITY AUDIT ---")
    years = ['FY26', 'FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']
    for idx, y in enumerate(years, start=3):
        tot_assets = ws_checks.Cells(17, idx).Value
        tot_liab_eq = ws_checks.Cells(18, idx).Value
        dev = ws_checks.Cells(19, idx).Value
        status = ws_checks.Cells(20, idx).Value
        
        print(f"{y}: Total Assets = {tot_assets:,.2f} | Liab & Eq = {tot_liab_eq:,.2f} | Dev = {dev:.2f} | Status = {status}")
        validation_records.append({
            'Test Category': 'Balance Sheet Balance',
            'Test Name': f'Balance Sheet Equality ({y})',
            'Schedule': '10_Balance_Sheet',
            'Period': y,
            'Expected Result': round(tot_assets, 2),
            'Actual Result': round(tot_liab_eq, 2),
            'Difference': round(dev, 2),
            'Pass/Fail Status': status,
            'Audit Criteria': 'Assets - Liabilities - Equity == 0.00',
            'Timestamp': datetime.datetime.now().isoformat()
        })
        
    # 3. Read Core Valuation Outputs from Cover
    ws_cov = wb.Worksheets("01_Cover")
    cmp_val = ws_cov.Cells(13, 3).Value
    mcap_val = ws_cov.Cells(15, 3).Value
    wacc_val = ws_cov.Cells(16, 3).Value
    dcf_multiple_val = ws_cov.Cells(18, 3).Value
    dcf_gordon_val = ws_cov.Cells(19, 3).Value
    upside_val = ws_cov.Cells(20, 3).Value
    
    print("\n--- CORE VALUATION OUTPUTS FROM EXCEL ---")
    print(f"Current Market Price: INR {cmp_val:,.2f}")
    print(f"Market Capitalization: INR {mcap_val:,.2f} Cr")
    print(f"WACC: {wacc_val*100:.2f}%")
    print(f"DCF Exit Multiple Implied Price: INR {dcf_multiple_val:,.2f}")
    print(f"DCF Gordon Growth Implied Price: INR {dcf_gordon_val:,.2f}")
    print(f"Implied Upside (Exit Multiple): {upside_val*100:.2f}%")
    
    # Save recalculated workbook
    wb.Save()
    print("Recalculated workbook saved successfully.")
    
finally:
    wb.Close(SaveChanges=True)
    excel.Quit()

df_val = pd.DataFrame(validation_records)
report_path = os.path.join(OUTPUT_DIR, 'model_validation_report.csv')
df_val.to_csv(report_path, index=False)
print(f"Model validation report saved to:\n{report_path}")
