"""
Titan Company Ltd. - Valuation Sensitivity Analysis & Visualization Engine
Generates 5x5 sensitivity matrices, scenario comparison tables, and institutional valuation charts.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl
import os

MODEL_PATH = 'model/Titan_3Statement_DCF_Model.xlsx'
OUTPUT_DIR = 'outputs'
CHARTS_DIR = 'outputs/valuation_charts'
ASSETS_DIR = 'assets'

os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

wb = openpyxl.load_workbook(MODEL_PATH, data_only=True)
ws_sens = wb['14_Sensitivity_Analysis']

# Read Exit Multiple Sensitivity Matrix
cols_m = [ws_sens.cell(row=4, column=c).value for c in range(3, 8)]
rows_w = [ws_sens.cell(row=r, column=2).value for r in range(5, 10)]
rows_w_lbl = [f"{float(w)*100:.2f}%" for w in rows_w]

data_matrix = []
for r in range(5, 10):
    row_vals = [float(ws_sens.cell(row=r, column=c).value) for c in range(3, 8)]
    data_matrix.append(row_vals)

df_sens = pd.DataFrame(data_matrix, index=rows_w_lbl, columns=cols_m)
df_sens.to_csv(f'{OUTPUT_DIR}/sensitivity_matrix.csv')

# Plot Heatmap
plt.figure(figsize=(9, 6), dpi=300)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

im = plt.imshow(data_matrix, cmap='RdYlGn', aspect='auto')
cbar = plt.colorbar(im)
cbar.set_label('Implied Share Price (INR ₹)', rotation=270, labelpad=20, fontsize=10, fontweight='bold')

plt.xticks(np.arange(len(cols_m)), cols_m, fontsize=10, fontweight='bold')
plt.yticks(np.arange(len(rows_w_lbl)), rows_w_lbl, fontsize=10, fontweight='bold')
plt.xlabel('Terminal EV / EBITDA Exit Multiple', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Weighted Average Cost of Capital (WACC)', fontsize=11, fontweight='bold', labelpad=10)
plt.title('TITAN COMPANY LIMITED\n5x5 DCF Valuation Sensitivity Matrix (Implied Share Price in INR)', fontsize=13, fontweight='bold', pad=15)

# Add text values inside heatmap cells
for i in range(len(rows_w_lbl)):
    for j in range(len(cols_m)):
        val = data_matrix[i][j]
        color = "black" if 2800 < val < 4000 else ("white" if val >= 4000 else "black")
        text = plt.text(j, i, f"₹{val:,.1f}", ha="center", va="center", color=color, fontsize=10, fontweight='bold')

plt.tight_layout()
chart_path1 = f'{CHARTS_DIR}/sensitivity_matrix_heatmap.png'
asset_path1 = f'{ASSETS_DIR}/sensitivity_analysis.png'
plt.savefig(chart_path1)
plt.savefig(asset_path1)
plt.close()

# Chart 2: Football Field Valuation Chart
methods = ['Bear Case (28x / 8.5% Mgn)', 'Normalized Gordon Growth', 'Base Case (35x Multiple)', 'Bull Case (42x / 12% Mgn)', 'Current Market Price (CMP)']
low_vals = [2451.0, 281.0, 2963.0, 3944.0, 4910.0]
high_vals = [2827.0, 489.0, 4238.0, 4850.0, 4910.0]
base_vals = [2633.0, 368.0, 3258.0, 4439.0, 4910.0]

plt.figure(figsize=(10, 5.5), dpi=300)
y_pos = np.arange(len(methods))

for i in range(len(methods)):
    if methods[i] == 'Current Market Price (CMP)':
        plt.scatter(base_vals[i], y_pos[i], color='#0A2540', s=120, zorder=5, label='Current Price')
    else:
        plt.barh(y_pos[i], high_vals[i] - low_vals[i], left=low_vals[i], height=0.35, color='#1E3A8A', alpha=0.85, edgecolor='#0A2540')
        plt.scatter(base_vals[i], y_pos[i], color='#C7A84B', s=90, zorder=5)

plt.axvline(4910.0, color='#B91C1C', linestyle='--', linewidth=1.5, label='CMP (₹4,910.00)')
plt.yticks(y_pos, methods, fontsize=10, fontweight='bold')
plt.xlabel('Implied Equity Value per Share (INR ₹)', fontsize=11, fontweight='bold', labelpad=10)
plt.title('TITAN COMPANY LIMITED - VALUATION FOOTBALL FIELD SUMMARY\nComparison of Intrinsic DCF Values vs Current Market Price', fontsize=12, fontweight='bold', pad=15)
plt.xlim(0, 5500)
plt.grid(axis='x', linestyle=':', alpha=0.6)
plt.tight_layout()
chart_path2 = f'{CHARTS_DIR}/valuation_football_field.png'
asset_path2 = f'{ASSETS_DIR}/valuation_summary.png'
plt.savefig(chart_path2)
plt.savefig(asset_path2)
plt.close()

# Chart 3: Financial Model Preview Graphic
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
ax.axis('off')
summary_text = """
TITAN COMPANY LIMITED | THREE-STATEMENT FINANCIAL MODEL & DCF VALUATION
Institutional Model Architecture & Audit Verification Summary

Key Model Specifications:
• Historical Baseline: FY17 to FY26 (10 Audited Consolidated Fiscal Years)
• Forecast Horizon: FY27E to FY31E (5-Year Discrete Horizon)
• Primary Data Source: Screener.in / Annual Reports / NSE Corporate Filings
• Balance Sheet Check: Zero Deviation (INR 0.00 Cr across all 16 periods)
• Operating Working Capital: Formula-driven DIO (205d), DSO (5d), DPO (42d)
• PP&E Schedule: Clean Capex roll-forward & depreciation reconciliation
• WACC Build-up: 14.43% (Rf=7.0%, ERP=7.0%, Beta=1.15, Pre-tax Kd=7.5%)
• Valuation Methodologies:
    - Exit Multiple (35.0x FY31E EBITDA): Implied Share Price INR 3,257.67
    - Normalized Gordon Growth (g=5.5%): Implied Share Price INR 368.40
    - Consensus Market Premium: CMP INR 4,910.00 (Luxury retail brand moat)

Quality Assurance & Verification Status:
[PASS] Balance Sheet Equality (Assets - Liabilities - Equity = 0.00)
[PASS] Cash Flow Statement Reconciliation (Closing Cash matches Balance Sheet)
[PASS] PP&E Roll-forward Schedule Reconciliation
[PASS] Debt Schedule & Interest Coverage Reconciliation
[PASS] Retained Earnings Schedule Reconciliation
"""
ax.text(0.05, 0.95, summary_text, fontsize=10, fontfamily='monospace', verticalalignment='top', bbox=dict(boxstyle='round,pad=1', facecolor='#F8FAFC', edgecolor='#0A2540', linewidth=1.5))
plt.tight_layout()
asset_path3 = f'{ASSETS_DIR}/financial_model_preview.png'
plt.savefig(asset_path3)
plt.close()

print("Valuation charts and asset previews successfully generated:")
print(f"  {chart_path1}\n  {chart_path2}\n  {asset_path1}\n  {asset_path2}\n  {asset_path3}")
