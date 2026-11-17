"""
Titan Company Ltd. - Institutional Financial Model Builder
Builds the complete 17-sheet Three-Statement DCF Financial Model in Excel using institutional IB standards.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import json
import os

OUTPUT_DIR = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/model'
os.makedirs(OUTPUT_DIR, exist_ok=True)
FILE_PATH = os.path.join(OUTPUT_DIR, 'Titan_3Statement_DCF_Model.xlsx')

wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default sheet

# Color palette & fonts
FONT_NAME = "Calibri"
COLOR_NAVY = "0A2540"
COLOR_ACCENT = "1E3A8A"
COLOR_HEADER_BG = "0A2540"
COLOR_SUBHEADER_BG = "E2E8F0"
COLOR_ROW_HIGHLIGHT = "F1F5F9"
COLOR_SUCCESS = "0D9488"
COLOR_ERROR = "B91C1C"

# Styles
font_title = Font(name=FONT_NAME, size=16, bold=True, color="FFFFFF")
font_section = Font(name=FONT_NAME, size=11, bold=True, color="0A2540")
font_header = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
font_bold = Font(name=FONT_NAME, size=10, bold=True, color="000000")
font_input = Font(name=FONT_NAME, size=10, color="0000FF") # Blue for inputs
font_formula = Font(name=FONT_NAME, size=10, color="000000") # Black for intra-sheet
font_external = Font(name=FONT_NAME, size=10, color="008000") # Green for cross-sheet
font_warning = Font(name=FONT_NAME, size=10, bold=True, color=COLOR_ERROR)
font_pass = Font(name=FONT_NAME, size=10, bold=True, color=COLOR_SUCCESS)

fill_title = PatternFill(start_color=COLOR_HEADER_BG, end_color=COLOR_HEADER_BG, fill_type="solid")
fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
fill_sub = PatternFill(start_color=COLOR_SUBHEADER_BG, end_color=COLOR_SUBHEADER_BG, fill_type="solid")
fill_zebra = PatternFill(start_color=COLOR_ROW_HIGHLIGHT, end_color=COLOR_ROW_HIGHLIGHT, fill_type="solid")

thin_border_side = Side(border_style="thin", color="CBD5E1")
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
thick_bottom = Border(bottom=Side(border_style="medium", color="0A2540"))
total_border = Border(top=Side(border_style="thin", color="0A2540"), bottom=Side(border_style="double", color="0A2540"))

align_left = Alignment(horizontal="left", vertical="center")
align_right = Alignment(horizontal="right", vertical="center")
align_center = Alignment(horizontal="center", vertical="center")

FMT_CURRENCY = "_-₹* #,##0.00_-;_-₹* (#,##0.00)_-;_-₹* \"-\"??_-;_-@_-"
FMT_NUMBER = "_-* #,##0.00_-;_-* (#,##0.00)_-;_-* \"-\"??_-;_-@_-"
FMT_INT = "_-* #,##0_-;_-* (#,##0)_-;_-* \"-\"_-;_-@_-"
FMT_PCT = "0.0%"
FMT_MULTIPLE = "0.0\"x\""

print("Initializing Excel model build...")

# Load historical standardized datasets
PROCESSED_DIR = 'Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/processed'
import pandas as pd
df_pnl = pd.read_csv(f'{PROCESSED_DIR}/income_statement_standardized.csv', index_col=0)
df_bs = pd.read_csv(f'{PROCESSED_DIR}/balance_sheet_standardized.csv', index_col=0)
df_cf = pd.read_csv(f'{PROCESSED_DIR}/cash_flow_historical.csv', index_col=0)
with open(f'{PROCESSED_DIR}/company_metadata.json', 'r') as f:
    meta = json.load(f)
with open(f'{PROCESSED_DIR}/model_assumptions.json', 'r') as f:
    assump = json.load(f)

# Helper function to style table headers
def style_table_header(ws, row, start_col, end_col, title=None):
    for c in range(start_col, end_col + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = fill_header
        cell.font = font_header
        cell.alignment = align_center
        cell.border = thin_border
    if title:
        ws.cell(row=row, column=start_col).value = title

# Helper to autofit columns
def autofit_cols(ws, max_cols=12):
    for col in range(1, max_cols + 1):
        col_letter = get_column_letter(col)
        max_len = 0
        for row in range(1, ws.max_row + 1):
            val = ws.cell(row=row, column=col).value
            if val is not None and not str(val).startswith("="):
                max_len = max(max_len, len(str(val)))
        ws.column_dimensions[col_letter].width = max(max_len + 3, 14)
    ws.column_dimensions['A'].width = 4
    ws.column_dimensions['B'].width = 38

# ==========================================
# 01_COVER
# ==========================================
print("Building 01_Cover...")
ws_cov = wb.create_sheet(title="01_Cover")
ws_cov.views.sheetView[0].showGridLines = True

ws_cov.merge_cells("B2:J3")
c = ws_cov["B2"]
c.value = "TITAN COMPANY LIMITED"
c.font = Font(name=FONT_NAME, size=18, bold=True, color="FFFFFF")
c.fill = fill_title
c.alignment = align_center

ws_cov.merge_cells("B4:J4")
c = ws_cov["B4"]
c.value = "CONSOLIDATED THREE-STATEMENT FINANCIAL MODEL & DCF VALUATION"
c.font = Font(name=FONT_NAME, size=12, bold=True, color="FFFFFF")
c.fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
c.alignment = align_center

metadata_rows = [
    ("Ticker / Exchange", "TITAN.NS / TITAN.BO (NSE / BSE)"),
    ("Industry / Sector", "Consumer Discretionary / Gems, Jewellery & Watches"),
    ("Currency / Reporting Unit", "INR (₹) in Crore"),
    ("Historical Period", "FY17 - FY26 (10 Audited Fiscal Years)"),
    ("Forecast Horizon", "FY27E - FY31E (5-Year Forecast Horizon)"),
    ("Model Author", "Sarvesh Padmanabhan | Financial Analyst"),
    ("Date of Execution", "November 2026"),
    ("Current Market Price (CMP)", 4910.00),
    ("Diluted Shares Outstanding (Cr)", 88.78),
    ("Market Capitalization (INR Cr)", "=C13*C14"),
    ("DCF Implied Value - Exit Multiple", "='13_DCF_Valuation'!D28"),
    ("DCF Implied Value - Gordon Growth", "='13_DCF_Valuation'!D20"),
    ("Implied Upside / (Downside)", "=(C16-C13)/C13"),
    ("Balance Sheet Check Status", "='16_Model_Checks'!D6")
]

for idx, (label, val) in enumerate(metadata_rows, start=6):
    ws_cov.cell(row=idx, column=2, value=label).font = font_bold
    ws_cov.cell(row=idx, column=2).border = thin_border
    target = ws_cov.cell(row=idx, column=3, value=val)
    target.border = thin_border
    if isinstance(val, (int, float)):
        target.font = font_input
        target.number_format = FMT_CURRENCY if "Price" in label else FMT_NUMBER
        target.alignment = align_right
    elif str(val).startswith("="):
        target.font = font_external
        if "Upside" in label:
            target.number_format = FMT_PCT
        elif "Value" in label or "Price" in label or "Capitalization" in label:
            target.number_format = FMT_CURRENCY
        target.alignment = align_right
    else:
        target.font = font_formula
        target.alignment = align_left

ws_cov.freeze_panes = "B6"

# ==========================================
# 02_HISTORICAL_DATA
# ==========================================
print("Building 02_Historical_Data...")
ws_hist = wb.create_sheet(title="02_Historical_Data")
ws_hist.views.sheetView[0].showGridLines = True

ws_hist.cell(row=2, column=2, value="TITAN COMPANY LIMITED - 10-YEAR HISTORICAL FINANCIAL STATEMENTS (INR Cr)").font = font_section

hist_years = ['FY17', 'FY18', 'FY19', 'FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26']
style_table_header(ws_hist, 4, 2, 12, "Financial Metric / Consolidated Line Item")
for idx, y in enumerate(hist_years, start=3):
    ws_hist.cell(row=4, column=idx, value=y)

curr_row = 5
ws_hist.cell(row=curr_row, column=2, value="INCOME STATEMENT HISTORY").font = font_bold
curr_row += 1

pnl_row_map = {}
for metric in df_pnl.index:
    ws_hist.cell(row=curr_row, column=2, value=metric).font = font_formula
    ws_hist.cell(row=curr_row, column=2).border = thin_border
    pnl_row_map[metric] = curr_row
    for c_idx, y in enumerate(hist_years, start=3):
        val = float(df_pnl.loc[metric, y])
        cell = ws_hist.cell(row=curr_row, column=c_idx, value=val)
        cell.font = font_input
        cell.number_format = FMT_NUMBER
        cell.alignment = align_right
        cell.border = thin_border
    curr_row += 1

curr_row += 1
ws_hist.cell(row=curr_row, column=2, value="BALANCE SHEET HISTORY").font = font_bold
curr_row += 1

bs_row_map = {}
for metric in df_bs.index:
    ws_hist.cell(row=curr_row, column=2, value=metric).font = font_formula
    ws_hist.cell(row=curr_row, column=2).border = thin_border
    bs_row_map[metric] = curr_row
    for c_idx, y in enumerate(hist_years, start=3):
        val = float(df_bs.loc[metric, y])
        cell = ws_hist.cell(row=curr_row, column=c_idx, value=val)
        cell.font = font_input
        cell.number_format = FMT_NUMBER
        cell.alignment = align_right
        cell.border = thin_border
    curr_row += 1

curr_row += 1
ws_hist.cell(row=curr_row, column=2, value="CASH FLOW STATEMENT HISTORY").font = font_bold
curr_row += 1

for metric in df_cf.index:
    ws_hist.cell(row=curr_row, column=2, value=metric).font = font_formula
    ws_hist.cell(row=curr_row, column=2).border = thin_border
    for c_idx, y in enumerate(hist_years, start=3):
        val = float(df_cf.loc[metric, y])
        cell = ws_hist.cell(row=curr_row, column=c_idx, value=val)
        cell.font = font_input
        cell.number_format = FMT_NUMBER
        cell.alignment = align_right
        cell.border = thin_border
    curr_row += 1

ws_hist.freeze_panes = "C5"
autofit_cols(ws_hist, 12)

# ==========================================
# 03_ASSUMPTIONS_DRIVERS
# ==========================================
print("Building 03_Assumptions_Drivers...")
ws_assump = wb.create_sheet(title="03_Assumptions_Drivers")
ws_assump.views.sheetView[0].showGridLines = True

ws_assump.cell(row=2, column=2, value="FORECAST ASSUMPTIONS & OPERATING DRIVERS").font = font_section

headers_sc = ["Operational Driver / Financial Parameter", "Bear Case", "Base Case (Active)", "Bull Case", "Notes & Source Guidance"]
for c_idx, h in enumerate(headers_sc, start=2):
    cell = ws_assump.cell(row=4, column=c_idx, value=h)
    cell.fill = fill_header
    cell.font = font_header
    cell.alignment = align_center
    cell.border = thin_border

driver_rows = [
    ("Revenue Growth Rate - FY27E", 0.10, 0.15, 0.20, FMT_PCT, "Base case 15% consensus retail expansion; Bull 20%"),
    ("Revenue Growth Rate - FY28E", 0.09, 0.14, 0.18, FMT_PCT, "Store additions across Tier 2/3 markets"),
    ("Revenue Growth Rate - FY29E", 0.09, 0.13, 0.17, FMT_PCT, "Mia & Caratlane digital omnichannel expansion"),
    ("Revenue Growth Rate - FY30E", 0.08, 0.12, 0.16, FMT_PCT, "Maturing retail network and international scaling"),
    ("Revenue Growth Rate - FY31E", 0.08, 0.12, 0.15, FMT_PCT, "Terminal forecast year growth fading towards steady state"),
    ("Gross Margin (% of Revenue)", 0.205, 0.225, 0.245, FMT_PCT, "Historical average ~22.5%; higher studded jewellery mix"),
    ("Employee Cost (% of Revenue)", 0.036, 0.033, 0.030, FMT_PCT, "Historical range 3.0% - 4.7%; retail store staffing"),
    ("Other Operating Exp (% of Revenue)", 0.095, 0.087, 0.080, FMT_PCT, "Store lease, franchise marketing, logistics"),
    ("EBITDA Margin (% of Revenue)", "=(C10-C11-C12)", "=(D10-D11-D12)", "=(E10-E11-E12)", FMT_PCT, "Formula: Gross Margin - Employee - Other OpEx"),
    ("Depreciation (% of Opening PP&E)", 0.180, 0.180, 0.180, FMT_PCT, "Historical range 16% - 20% on retail store fit-outs"),
    ("CapEx (% of Revenue)", 0.020, 0.025, 0.030, FMT_PCT, "New store fitouts, lab diamond tech, logistics hubs"),
    ("Effective Tax Rate (%)", 0.2517, 0.2517, 0.2517, FMT_PCT, "Statutory corporate tax rate (Sec 115BAA: 22% + 10% + 4%)"),
    ("Receivable Days (DSO)", 6.0, 5.0, 4.5, FMT_NUMBER, "High proportion of cash/card retail sales"),
    ("Inventory Days (DIO)", 220.0, 205.0, 190.0, FMT_NUMBER, "Gold & diamond holding across 3,000+ stores"),
    ("Payable Days (DPO)", 40.0, 42.0, 45.0, FMT_NUMBER, "Vendor credit terms on bullion & component supply"),
    ("Dividend Payout Ratio (%)", 0.25, 0.28, 0.30, FMT_PCT, "Historical payout average ~28% of Net Income"),
    ("Pre-Tax Cost of Debt (Kd)", 0.080, 0.075, 0.072, FMT_PCT, "Commercial paper & short-term banking credit"),
    ("Risk-Free Rate (Rf)", 0.070, 0.070, 0.070, FMT_PCT, "India 10-Year Benchmark G-Sec yield"),
    ("Equity Risk Premium (ERP)", 0.070, 0.070, 0.070, FMT_PCT, "India market equity risk premium (Prof. Damodaran)"),
    ("Beta", 1.20, 1.15, 1.10, FMT_NUMBER, "Consumer discretionary luxury goods beta"),
    ("Terminal Growth Rate (g)", 0.050, 0.055, 0.060, FMT_PCT, "Long-term GDP growth and inflation anchor"),
    ("Exit Multiple (EV/EBITDA)", 28.0, 35.0, 42.0, FMT_MULTIPLE, "Peer multiples: Kalyan, Senco, Tribhovandas Bhimji")
]

for idx, (label, bear, base, bull, fmt, note) in enumerate(driver_rows, start=5):
    ws_assump.cell(row=idx, column=2, value=label).font = font_bold
    ws_assump.cell(row=idx, column=2).border = thin_border
    
    for c_idx, val in [(3, bear), (4, base), (5, bull)]:
        cell = ws_assump.cell(row=idx, column=c_idx, value=val)
        cell.border = thin_border
        cell.alignment = align_right
        cell.number_format = fmt
        if isinstance(val, (int, float)):
            cell.font = font_input
        else:
            cell.font = font_formula
            
    note_cell = ws_assump.cell(row=idx, column=6, value=note)
    note_cell.font = font_formula
    note_cell.border = thin_border
    note_cell.alignment = align_left

ws_assump.freeze_panes = "C5"
autofit_cols(ws_assump, 6)

print("Setup assumptions completed.")
