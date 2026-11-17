"""
Project 02: High-Resolution Dashboard Visual Assets Generator
Generates pixel-perfect executive reporting screenshots for the three Power BI dashboard pages.
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import os

DATA_PATH = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/data/processed/retail_performance_cleaned.csv'
ASSETS_DIR = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/assets'
os.makedirs(ASSETS_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Palette
BG_MAIN = "#F8FAFC"
BG_CARD = "#FFFFFF"
TEXT_MAIN = "#0A2540"
TEXT_MUTED = "#64748B"
ACCENT_BLUE = "#635BFF"
COLOR_SUCCESS = "#0D9488"
COLOR_DANGER = "#B91C1C"
COLOR_GOLD = "#C7A84B"
BORDER_COLOR = "#E2E8F0"

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = TEXT_MAIN
plt.rcParams['axes.labelcolor'] = TEXT_MAIN
plt.rcParams['xtick.color'] = TEXT_MAIN
plt.rcParams['ytick.color'] = TEXT_MAIN

# ==========================================
# PAGE 1: EXECUTIVE SUMMARY
# ==========================================
print("Rendering Page 1: Executive Dashboard...")
fig = plt.figure(figsize=(16, 10), dpi=300, facecolor=BG_MAIN)
gs = gridspec.GridSpec(3, 4, height_ratios=[0.8, 2.5, 2.5], hspace=0.35, wspace=0.25, left=0.04, right=0.96, top=0.92, bottom=0.06)

# Title Banner
fig.text(0.04, 0.96, "RETAIL FP&A | EXECUTIVE PERFORMANCE & BUDGET ATTAINMENT DASHBOARD", fontsize=15, fontweight='bold', color=TEXT_MAIN)
fig.text(0.04, 0.94, "Consolidated Management Reporting (Jan 2025 - Dec 2026) | All Currency Values in INR (₹)", fontsize=10, color=TEXT_MUTED)

# KPI Cards
kpis = [
    ("ACTUAL REVENUE", f"₹{df['Actual_Revenue'].sum()/1e7:,.1f} Cr", "+1.96% vs Budget", COLOR_SUCCESS),
    ("BUDGET REVENUE", f"₹{df['Budgeted_Revenue'].sum()/1e7:,.1f} Cr", "Annual Plan Target", TEXT_MUTED),
    ("ACTUAL EXPENSES", f"₹{df['Actual_Expenses'].sum()/1e7:,.1f} Cr", "+2.67% Overrun", COLOR_DANGER),
    ("ACTUAL PROFIT", f"₹{df['Actual_Profit'].sum()/1e7:,.1f} Cr", "6.56% Operating Margin", COLOR_GOLD)
]

for i, (title, val, sub, col) in enumerate(kpis):
    ax = fig.add_subplot(gs[0, i])
    ax.set_facecolor(BG_CARD)
    for spine in ax.spines.values():
        spine.set_color(BORDER_COLOR)
        spine.set_linewidth(1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0.08, 0.72, title, fontsize=9, fontweight='bold', color=TEXT_MUTED, transform=ax.transAxes)
    ax.text(0.08, 0.38, val, fontsize=18, fontweight='bold', color=TEXT_MAIN, transform=ax.transAxes)
    ax.text(0.08, 0.15, sub, fontsize=8, fontweight='bold', color=col, transform=ax.transAxes)

# Chart 1: Monthly Budget vs Actual Revenue
ax1 = fig.add_subplot(gs[1, :2])
ax1.set_facecolor(BG_CARD)
for spine in ax1.spines.values():
    spine.set_color(BORDER_COLOR)

monthly = df.groupby('Date')[['Budgeted_Revenue', 'Actual_Revenue']].sum() / 1e7
x = np.arange(len(monthly))
w = 0.38

ax1.bar(x - w/2, monthly['Budgeted_Revenue'], width=w, label='Budget Revenue', color='#94A3B8', alpha=0.85)
ax1.bar(x + w/2, monthly['Actual_Revenue'], width=w, label='Actual Revenue', color=ACCENT_BLUE, alpha=0.95)
ax1.set_title("Budget vs Actual Revenue Trend (Monthly ₹ Cr)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax1.set_xticks(x[::2])
ax1.set_xticklabels([d[2:7] for d in monthly.index[::2]], fontsize=8)
ax1.set_ylabel("INR (₹ Crore)", fontsize=9)
ax1.legend(frameon=True, facecolor=BG_CARD, fontsize=8)
ax1.grid(axis='y', linestyle=':', alpha=0.5)

# Chart 2: Regional Performance Comparison
ax2 = fig.add_subplot(gs[1, 2:])
ax2.set_facecolor(BG_CARD)
for spine in ax2.spines.values():
    spine.set_color(BORDER_COLOR)

reg = df.groupby('Region')[['Budgeted_Revenue', 'Actual_Revenue', 'Actual_Profit']].sum() / 1e7
x_reg = np.arange(len(reg))
ax2.bar(x_reg - w/2, reg['Actual_Revenue'], width=w, label='Actual Revenue', color='#0A2540')
ax2.bar(x_reg + w/2, reg['Budgeted_Revenue'], width=w, label='Budget Revenue', color='#CBD5E1')
ax2.plot(x_reg, reg['Actual_Profit'], color=COLOR_GOLD, marker='o', linewidth=2, label='Actual Profit (₹ Cr)')
ax2.set_title("Regional Revenue Attainment & Profit Contribution (₹ Cr)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax2.set_xticks(x_reg)
ax2.set_xticklabels(reg.index, fontsize=9, fontweight='bold')
ax2.set_ylabel("INR (₹ Crore)", fontsize=9)
ax2.legend(frameon=True, facecolor=BG_CARD, fontsize=8)
ax2.grid(axis='y', linestyle=':', alpha=0.5)

# Chart 3: Category Profitability Waterfall
ax3 = fig.add_subplot(gs[2, :])
ax3.set_facecolor(BG_CARD)
for spine in ax3.spines.values():
    spine.set_color(BORDER_COLOR)

cat = df.groupby('Product_Category')[['Actual_Revenue', 'Actual_Expenses', 'Actual_Profit']].sum() / 1e7
cat = cat.sort_values('Actual_Revenue', ascending=True)

y_pos = np.arange(len(cat))
ax3.barh(y_pos - 0.2, cat['Actual_Revenue'], height=0.35, label='Actual Revenue', color=ACCENT_BLUE)
ax3.barh(y_pos + 0.2, cat['Actual_Expenses'], height=0.35, label='Actual Expenses', color='#F43F5E')
for i, v in enumerate(cat['Actual_Profit']):
    ax3.text(cat['Actual_Revenue'].iloc[i] + 1.5, y_pos[i] - 0.2, f"Profit: ₹{v:,.1f} Cr", va='center', fontsize=8, fontweight='bold', color=TEXT_MAIN)

ax3.set_title("Category-Level Revenue vs Operating Expenses (₹ Cr)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax3.set_yticks(y_pos)
ax3.set_yticklabels(cat.index, fontsize=9, fontweight='bold')
ax3.set_xlabel("INR (₹ Crore)", fontsize=9)
ax3.legend(frameon=True, facecolor=BG_CARD, loc='lower right', fontsize=8)
ax3.grid(axis='x', linestyle=':', alpha=0.5)

plt.savefig(f'{ASSETS_DIR}/executive_dashboard.png')
plt.close()

# ==========================================
# PAGE 2: VARIANCE ANALYSIS
# ==========================================
print("Rendering Page 2: Variance Dashboard...")
fig = plt.figure(figsize=(16, 10), dpi=300, facecolor=BG_MAIN)
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.35, wspace=0.22, left=0.05, right=0.95, top=0.92, bottom=0.06)

fig.text(0.05, 0.96, "RETAIL FP&A | VARIANCE ANALYSIS & ROOT CAUSE DECOMPOSITION", fontsize=15, fontweight='bold', color=TEXT_MAIN)
fig.text(0.05, 0.94, "Detailed Favourable vs Unfavourable Variance Identification | 24-Month Operations", fontsize=10, color=TEXT_MUTED)

# Chart 1: Revenue Variance by Category (Beat / Miss)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor(BG_CARD)
for spine in ax1.spines.values():
    spine.set_color(BORDER_COLOR)

cat_var = (df.groupby('Product_Category')['Revenue_Variance'].sum() / 1e7).sort_values()
colors = [COLOR_SUCCESS if v >= 0 else COLOR_DANGER for v in cat_var]
y_pos = np.arange(len(cat_var))
bars = ax1.barh(y_pos, cat_var, color=colors, height=0.55)
ax1.axvline(0, color=TEXT_MAIN, linewidth=1)
ax1.set_title("Revenue Variance by Category (₹ Cr Beat / Miss)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(cat_var.index, fontsize=9, fontweight='bold')
ax1.set_xlabel("Variance vs Budget (₹ Cr)", fontsize=9)
for bar in bars:
    w_val = bar.get_width()
    ax1.text(w_val + (0.1 if w_val >= 0 else -0.3), bar.get_y() + bar.get_height()/2, f"₹{w_val:+,.1f} Cr", va='center', fontsize=8, fontweight='bold')
ax1.grid(axis='x', linestyle=':', alpha=0.5)

# Chart 2: Cost Element Breakdown & Overruns
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(BG_CARD)
for spine in ax2.spines.values():
    spine.set_color(BORDER_COLOR)

cost_elements = ['Product_Cost_COGS', 'Marketing_Expenses', 'Personnel_Expenses', 'Distribution_Expenses', 'Other_Operating_Expenses']
cost_labels = ['Merchandise COGS', 'Marketing & Ads', 'Store Personnel', 'Freight & Logistics', 'Store Leases & Opex']
cost_sums = [df[c].sum() / 1e7 for c in cost_elements]

ax2.pie(cost_sums, labels=cost_labels, autopct='%1.1f%%', startangle=140, colors=['#3B82F6', '#8B5CF6', '#EC4899', '#F97316', '#64748B'], textprops={'fontsize': 8, 'fontweight': 'bold'})
ax2.set_title("Actual Expense Composition by Cost Driver (Total: ₹565.1 Cr)", fontsize=11, fontweight='bold', pad=10, loc='left')

# Chart 3: Region x Category Variance Heatmap / Table
ax3 = fig.add_subplot(gs[1, :])
ax3.set_facecolor(BG_CARD)
for spine in ax3.spines.values():
    spine.set_color(BORDER_COLOR)
ax3.axis('off')

# Compile Summary Matrix Table
pivot = df.pivot_table(index='Product_Category', columns='Region', values='Profit_Variance', aggfunc='sum') / 1e7
pivot['Total'] = pivot.sum(axis=1)

table_data = []
for c_name in pivot.index:
    row = [c_name]
    for r_col in ['North', 'South', 'East', 'West', 'Total']:
        val = pivot.loc[c_name, r_col]
        row.append(f"{val:+,.2f}")
    table_data.append(row)

# Total row
tot_row = ['Enterprise Total']
for r_col in ['North', 'South', 'East', 'West', 'Total']:
    val = pivot[r_col].sum()
    tot_row.append(f"{val:+,.2f}")
table_data.append(tot_row)

col_labels = ['Product Segment', 'North (₹ Cr)', 'South (₹ Cr)', 'East (₹ Cr)', 'West (₹ Cr)', 'Consolidated (₹ Cr)']
tbl = ax3.table(cellText=table_data, colLabels=col_labels, loc='center', cellLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(9)
tbl.scale(1.0, 1.7)

for (r, c), cell in tbl.get_celld().items():
    if r == 0:
        cell.set_facecolor(TEXT_MAIN)
        cell.set_text_props(color='white', fontweight='bold')
    elif r == len(table_data):
        cell.set_facecolor('#E2E8F0')
        cell.set_text_props(fontweight='bold')
    else:
        if c > 0:
            val_num = float(table_data[r-1][c].replace('+', '').replace(',', ''))
            if val_num > 0:
                cell.set_facecolor('#DCFCE7')
                cell.set_text_props(color='#166534', fontweight='bold')
            else:
                cell.set_facecolor('#FEE2E2')
                cell.set_text_props(color='#991B1B', fontweight='bold')

ax3.set_title("Region-by-Category Profit Variance Matrix (Favourable / Unfavourable Traffic Lights)", fontsize=11, fontweight='bold', pad=15, loc='left')

plt.savefig(f'{ASSETS_DIR}/variance_dashboard.png')
plt.close()

# ==========================================
# PAGE 3: PROFITABILITY ANALYSIS
# ==========================================
print("Rendering Page 3: Profitability Dashboard...")
fig = plt.figure(figsize=(16, 10), dpi=300, facecolor=BG_MAIN)
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.35, wspace=0.22, left=0.05, right=0.95, top=0.92, bottom=0.06)

fig.text(0.05, 0.96, "RETAIL FP&A | MARGIN DECOMPOSITION & REGIONAL PROFITABILITY", fontsize=15, fontweight='bold', color=TEXT_MAIN)
fig.text(0.05, 0.94, "Operating Margin Dynamics, Unit Economics & Channel Contribution", fontsize=10, color=TEXT_MUTED)

# Chart 1: Profit Margin by Product Category
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor(BG_CARD)
for spine in ax1.spines.values():
    spine.set_color(BORDER_COLOR)

cat_margin = (df.groupby('Product_Category')['Actual_Profit'].sum() / df.groupby('Product_Category')['Actual_Revenue'].sum() * 100).sort_values()
y_pos = np.arange(len(cat_margin))
bars = ax1.barh(y_pos, cat_margin, color='#4F46E5', height=0.55)
ax1.set_title("Operating Margin by Category (%)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(cat_margin.index, fontsize=9, fontweight='bold')
ax1.set_xlabel("Actual Operating Margin (%)", fontsize=9)
for bar in bars:
    w_val = bar.get_width()
    ax1.text(w_val + 0.2, bar.get_y() + bar.get_height()/2, f"{w_val:.1f}%", va='center', fontsize=8, fontweight='bold')
ax1.grid(axis='x', linestyle=':', alpha=0.5)

# Chart 2: Monthly Profit Margin Trend vs Benchmark
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(BG_CARD)
for spine in ax2.spines.values():
    spine.set_color(BORDER_COLOR)

monthly_prof = df.groupby('Date')[['Actual_Profit', 'Actual_Revenue', 'Budgeted_Profit', 'Budgeted_Revenue']].sum()
actual_margin_trend = monthly_prof['Actual_Profit'] / monthly_prof['Actual_Revenue'] * 100
budget_margin_trend = monthly_prof['Budgeted_Profit'] / monthly_prof['Budgeted_Revenue'] * 100
x_m = np.arange(len(monthly_prof))

ax2.plot(x_m, actual_margin_trend, color=COLOR_SUCCESS, marker='o', linewidth=2, label='Actual Operating Margin (%)')
ax2.plot(x_m, budget_margin_trend, color='#94A3B8', linestyle='--', linewidth=1.8, label='Budget Target Margin (7.21%)')
ax2.set_title("Operating Margin Trajectory vs Budget Target (%)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax2.set_xticks(x_m[::2])
ax2.set_xticklabels([d[2:7] for d in monthly_prof.index[::2]], fontsize=8)
ax2.set_ylabel("Operating Margin (%)", fontsize=9)
ax2.legend(frameon=True, facecolor=BG_CARD, fontsize=8)
ax2.grid(True, linestyle=':', alpha=0.5)

# Chart 3: Retail Channel Contribution
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_facecolor(BG_CARD)
for spine in ax3.spines.values():
    spine.set_color(BORDER_COLOR)

ch_prof = df.groupby('Retail_Channel')[['Actual_Revenue', 'Actual_Profit']].sum() / 1e7
x_ch = np.arange(len(ch_prof))
ax3.bar(x_ch - 0.18, ch_prof['Actual_Revenue'], width=0.35, label='Actual Revenue', color='#1E293B')
ax3.bar(x_ch + 0.18, ch_prof['Actual_Profit'], width=0.35, label='Operating Profit', color=COLOR_GOLD)
ax3.set_title("Retail Format Contribution (Flagship vs High-Street vs Mall)", fontsize=11, fontweight='bold', pad=10, loc='left')
ax3.set_xticks(x_ch)
ax3.set_xticklabels(ch_prof.index, fontsize=9, fontweight='bold')
ax3.set_ylabel("INR (₹ Crore)", fontsize=9)
ax3.legend(frameon=True, facecolor=BG_CARD, fontsize=8)
ax3.grid(axis='y', linestyle=':', alpha=0.5)

# Chart 4: Regional Profit Share
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor(BG_CARD)
for spine in ax4.spines.values():
    spine.set_color(BORDER_COLOR)

reg_profit = df.groupby('Region')['Actual_Profit'].sum() / 1e7
ax4.pie(reg_profit, labels=[f"{r}: ₹{v:,.1f} Cr" for r, v in reg_profit.items()], autopct='%1.1f%%', startangle=90, colors=['#3B82F6', '#10B981', '#F59E0B', '#6366F1'], textprops={'fontsize': 9, 'fontweight': 'bold'})
ax4.set_title("Regional Share of Operating Profit (Total: ₹39.7 Cr)", fontsize=11, fontweight='bold', pad=10, loc='left')

plt.savefig(f'{ASSETS_DIR}/profitability_dashboard.png')
plt.close()

print("Dashboard asset generation complete:")
print(f"  {ASSETS_DIR}/executive_dashboard.png")
print(f"  {ASSETS_DIR}/variance_dashboard.png")
print(f"  {ASSETS_DIR}/profitability_dashboard.png")
