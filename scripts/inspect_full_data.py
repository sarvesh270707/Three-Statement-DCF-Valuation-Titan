import openpyxl
import datetime

wb = openpyxl.load_workbook('data/Titan Company.xlsx', data_only=True)
ws = wb['Data Sheet']
print(f"Max rows: {ws.max_row}, Max cols: {ws.max_column}")
for r in range(1, ws.max_row + 1):
    vals = [ws.cell(row=r, column=c).value for c in range(1, ws.max_column + 1)]
    if any(v is not None for v in vals):
        row_str = []
        for v in vals:
            if isinstance(v, datetime.datetime):
                row_str.append(v.strftime('%Y-%m-%d'))
            elif isinstance(v, (int, float)):
                row_str.append(f"{v:,.2f}")
            elif v is not None:
                row_str.append(str(v))
        print(f"R{r:02d}: " + " | ".join(row_str))
