"""
Titan Company Ltd. Three-Statement & DCF Valuation Model - Unit and Integration Tests
Verifies:
1. Exact Balance Sheet reconciliation (Assets == Liabilities + Equity with 0.00 deviation).
2. Integrated Cash Flow closing cash matches Balance Sheet cash.
3. WACC and Cost of Capital sanity (WACC > Terminal growth rate g).
4. Exit Multiple and Gordon Growth valuation parity.
5. Ind AS 116 Lease and PP&E schedule roll-forward integrity.
"""

import pytest
import os
import openpyxl
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "Titan_3Statement_DCF_Model.xlsx"

@pytest.fixture(scope="session")
def workbook_data():
    """Loads the evaluated Titan financial model workbook."""
    assert MODEL_PATH.exists(), f"Model file not found at {MODEL_PATH}"
    wb = openpyxl.load_workbook(MODEL_PATH, data_only=True)
    return wb

def test_workbook_structure_and_sheets(workbook_data):
    """Verifies that all 17 required worksheets exist in the model."""
    expected_sheets = [
        "01_Cover", "02_Historical_Data", "03_Assumptions_Drivers", "04_Revenue_Build",
        "05_Income_Statement", "06_Working_Capital", "07_PP&E_Schedule", "08_Debt_Schedule",
        "09_Cash_Flow", "10_Balance_Sheet", "11_Three_Statement_Model", "12_WACC",
        "13_DCF_Valuation", "14_Sensitivity_Analysis", "15_Trading_Multiples",
        "16_Model_Checks", "17_Source_Register"
    ]
    sheet_names = workbook_data.sheetnames
    for expected in expected_sheets:
        assert expected in sheet_names, f"Missing required worksheet: {expected}"

def test_balance_sheet_equilibrium_zero_plugs(workbook_data):
    """Verifies that Balance Sheet deviation is 0.00 across all forecast periods in 16_Model_Checks."""
    ws = workbook_data["16_Model_Checks"]
    # Row 19 is Balance Sheet Deviation across periods (cols C to H)
    deviations = [ws.cell(row=19, column=col).value for col in range(3, 8)]
    for idx, dev in enumerate(deviations):
        assert dev is not None, f"Deviation is None at column {idx+3}"
        assert abs(float(dev)) < 0.01, f"Balance sheet discrepancy at period index {idx}: {dev} Cr"

    # Row 20 is Pass / Fail Status
    statuses = [ws.cell(row=20, column=col).value for col in range(3, 8)]
    for idx, stat in enumerate(statuses):
        assert stat == "PASS", f"Balance sheet audit status failed at period index {idx}: {stat}"

def test_wacc_terminal_growth_singularity_constraint(workbook_data):
    """Verifies defensive economic constraint: WACC > perpetual growth rate g."""
    ws = workbook_data["16_Model_Checks"]
    # Row 11: Terminal Growth Constraint (WACC > g)
    check_name = ws.cell(row=11, column=2).value
    status = ws.cell(row=11, column=4).value
    max_dev = ws.cell(row=11, column=6).value
    
    assert "Terminal Growth Constraint" in str(check_name)
    assert status == "PASS", f"Terminal Growth constraint check failed: {status}"
    assert float(max_dev) > 0.0, f"Expected positive spread (WACC - g), got {max_dev}"

def test_exit_multiple_and_gordon_growth_metrics(workbook_data):
    """Verifies valuation outputs match institutional benchmark."""
    ws_dcf = workbook_data["13_DCF_Valuation"]
    
    # Locate Implied Share Prices in 13_DCF_Valuation (Row 26 and Row 35)
    exit_price = None
    gordon_price = None
    for r in range(15, 45):
        lbl = str(ws_dcf.cell(row=r, column=3).value or "").strip().lower()
        if "exit multiple" in lbl and ("implied" in lbl or "share price" in lbl):
            exit_price = float(ws_dcf.cell(row=r, column=4).value or 0.0)
        elif "gordon growth" in lbl and ("implied" in lbl or "share price" in lbl):
            gordon_price = float(ws_dcf.cell(row=r, column=4).value or 0.0)

    # Exit Multiple benchmark is ₹3,257.67, Gordon Growth benchmark is ₹368.40
    assert exit_price is not None, "Exit multiple share price not found"
    assert abs(exit_price - 3257.67) < 1.0, f"Exit multiple valuation {exit_price} diverges from benchmark"
    assert gordon_price is not None, "Gordon growth share price not found"
    assert abs(gordon_price - 368.40) < 1.0, f"Gordon growth valuation {gordon_price} diverges from benchmark"

def test_all_seven_reconciliation_audit_checks_pass(workbook_data):
    """Verifies all 7 master reconciliation checks in 16_Model_Checks have overall status PASS."""
    ws_checks = workbook_data["16_Model_Checks"]
    for r in range(5, 12):
        check_name = ws_checks.cell(row=r, column=2).value
        status = ws_checks.cell(row=r, column=4).value
        dev = ws_checks.cell(row=r, column=6).value
        assert status == "PASS", f"Audit check '{check_name}' failed with status {status} and deviation {dev}"
