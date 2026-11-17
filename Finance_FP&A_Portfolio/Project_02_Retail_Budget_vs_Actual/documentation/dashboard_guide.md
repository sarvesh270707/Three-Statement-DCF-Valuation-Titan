# User Guide: Retail Budget vs. Actual Power BI Analytics Platform

## 1. Overview & File Specifications

- **File Name**: `Retail_BvA_Dashboard.pbix`
- **Location**: `Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/powerbi/Retail_BvA_Dashboard.pbix`
- **Underlying Dataset**: `Retail_Sector_Financial_Analysis.xlsx` (Star Schema)
- **Target Application**: Microsoft Power BI Desktop (May 2024 / Version 2.129+ or newer)
- **Canvas Resolution**: 16:9 Widescreen (1280 $\times$ 720 px)
- **Palette & Design System**: Financial Executive Theme (Deep Navy `#1E293B`, Slate Gray `#64748B`, Emerald Positive `#10B981`, Crimson Adverse `#EF4444`, Amber Neutral `#F59E0B`).

---

## 2. Dashboard Navigation & Page Hierarchy

The analytics suite is structured into three dedicated reporting views designed for cross-functional corporate finance stakeholders:

```
+---------------------------------------------------------------------------------+
|                        RETAIL BvA POWER BI SUITE                                |
+---------------------------------------------------------------------------------+
|  [Page 1] Executive Summary       --> High-level KPI Scorecard & Trend Trajectory|
|  [Page 2] Variance Analysis       --> Bridge Waterfall & Multi-Dimensional Cuts |
|  [Page 3] Profitability & Margins --> Unit Economics, Channel ROAS & Store P&L   |
+---------------------------------------------------------------------------------+
```

---

## 3. Page-by-Page Feature Matrix

### Page 1: Executive Summary Dashboard (`executive_dashboard.png`)
Designed for C-suite leadership (CEO, CFO) to rapidly evaluate company-wide health against plan.
- **Top Metric Ribbon (KPI Cards)**:
  - **Actual Revenue**: Displayed with dynamic variance indicator vs. Budget (`+₹25.18 Cr / +4.18%`).
  - **Gross Profit**: Realized gross profit with Gross Margin % badge (`₹314.95 Cr / 50.17%`).
  - **EBITDA**: Operating profitability with budget delta (`₹144.38 Cr / +4.76%`).
  - **Store Conversion Rate**: Pan-India conversion efficiency (`20.18%`).
- **Visuals**:
  1. *Monthly Revenue Performance*: Clustered column & line chart comparing Actual Revenue (Navy bars) vs. Budget Revenue (Amber line) across CY2024–CY2025.
  2. *Regional Contribution*: Donut chart depicting revenue contribution by region (West 30%, South 28%, North 25%, East 17%).
  3. *Channel Breakdown*: Horizontal bar chart ranking channels by transaction volume and revenue yield.

### Page 2: Variance Analysis Dashboard (`variance_dashboard.png`)
Designed for Senior FP&A Managers and Operations Directors to dissect the root causes of financial deviations.
- **Top Metric Ribbon**:
  - Total Revenue Variance (`+₹25.18 Cr`).
  - Volume Variance (`+₹14.85 Cr` favorable).
  - Price/ASP Realization Variance (`+₹10.33 Cr` favorable).
  - Net OPEX Savings / Overrun (`-₹7.39 Cr` overspend).
- **Visuals**:
  1. *EBITDA Variance Waterfall*: Step-by-step bridge starting at Budget EBITDA (₹137.82 Cr), adding Revenue Volume impact, Price impact, COGS impact, OPEX changes, arriving at Actual EBITDA (₹144.38 Cr).
  2. *Category Variance Matrix*: Stacked bar chart showing favorable (Emerald) vs. unfavorable (Crimson) variance across all 6 product categories.
  3. *Regional Heatmap*: Matrix visual tracking regional performance by month with conditional green/red formatting.

### Page 3: Profitability & Unit Economics Dashboard (`profitability_dashboard.png`)
Designed for Commercial Category Managers and Channel Heads.
- **Top Metric Ribbon**:
  - Average Order Value (AOV): Pan-India average basket size.
  - Average Selling Price (ASP): Category-weighted unit price.
  - OPEX to Revenue Ratio: Operating cost discipline metric (`27.17%`).
  - Store EBITDA per Square Foot: Regional operational productivity.
- **Visuals**:
  1. *Channel Profitability Matrix*: Scatter plot analyzing Gross Margin % vs. Channel OPEX % to highlight digital margin dilution vs. EBO strength.
  2. *Product Margin Ranking*: Tornado chart comparing Target Gross Margin % vs. Actual Realized Gross Margin %.
  3. *Footfall vs. Conversion Correlation*: Dual-axis trend tracking seasonal footfall spikes (festive Q4) against cashier conversion rates.

---

## 4. Slicers & Dynamic Filtering

Global slicers located in the header/filter pane allow seamless slicing across all three pages:
- **Date / Fiscal Year**: Multi-select dropdown filtering CY2024, CY2025, or individual quarters (Q1-Q4).
- **Region**: Filter by North, South, East, West, or Pan-India view.
- **Product Category**: Filter by Jewellery, Watches, Eyewear, Wearables, Fragrances, Accessories.
- **Sales Channel**: Toggle between Exclusive Brand Outlets (EBO), Large Format Stores (LFS), and E-Commerce.

---

## 5. Refreshing & Deploying in Power BI Desktop / Service

1. Open `Retail_BvA_Dashboard.pbix` in **Microsoft Power BI Desktop**.
2. If Excel file paths have shifted on your local environment:
   - Go to `Home` > `Transform Data` > `Data Source Settings`.
   - Update file path to point to your local `Retail_Sector_Financial_Analysis.xlsx`.
   - Click `Apply Changes`.
3. To publish to Power BI Service (Cloud):
   - Click `Home` > `Publish`.
   - Select your corporate or personal Power BI Workspace.
   - Configure scheduled daily/monthly refresh linked to the underlying Excel workbook or SQL database.
