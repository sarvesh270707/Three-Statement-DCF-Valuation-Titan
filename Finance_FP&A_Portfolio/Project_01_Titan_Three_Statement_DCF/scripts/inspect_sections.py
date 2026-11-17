import openpyxl

wb = openpyxl.load_workbook('Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/raw/Titan_Company_Screener_Raw.xlsx', data_only=True)
ws = wb['Data Sheet']

sections = []
current_section = "HEADER"
print(f"Total rows in Data Sheet: {ws.max_row}")

for r in range(1, ws.max_row + 1):
    c1 = ws.cell(row=r, column=1).value
    c2 = ws.cell(row=r, column=2).value
    if c1 is not None:
        c1_str = str(c1).strip()
        if c1_str in ['META', 'PROFIT & LOSS', 'Quarters', 'BALANCE SHEET', 'CASH FLOW:', 'PRICE:', 'DERIVED:']:
            print(f"\n--- Section: {c1_str} starting at row {r} ---")
            current_section = c1_str
        else:
            # Print sample values for 2025 and 2026
            col_2025 = ws.cell(row=r, column=10).value
            col_2026 = ws.cell(row=r, column=11).value
            print(f"Row {r:02d} [{current_section}]: {c1_str} | Col10(FY25): {col_2025} | Col11(FY26): {col_2026}")
