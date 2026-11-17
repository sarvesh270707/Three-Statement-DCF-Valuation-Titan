# Project Methodology: Retail Budget vs. Actual Variance & Profitability Analysis

## 1. Executive Summary & Objective

This project provides an enterprise-grade Financial Planning & Analysis (FP&A) architecture and Power BI intelligence platform designed for a multi-channel Indian retail corporation operating across 4 geographic regions (North, South, East, West), 6 product categories (Jewellery, Watches, Eyewear, Wearables, Fragrances, Accessories), and 3 distribution channels (Exclusive Brand Outlets - EBO, Large Format Stores - LFS, and E-Commerce).

The objective of this modeling suite is to bridge corporate budget targets with granular operational reality through:
1. **Star Schema Data Architecture**: High-performance dimensional model with strict single-direction 1-to-many relationships.
2. **Variance Decomposition Engine**: Mathematically rigorous separation of revenue variances into volume, price, and mix drivers, alongside gross margin and OPEX variances.
3. **Automated DAX Logic**: 17 production DAX measures implementing time intelligence (YTD, MTD, Prior Year), dynamic waterfall drivers, and store-level contribution margins.
4. **Interactive BI Architecture**: 3-tier visual reporting hierarchy covering Executive Overview, Granular Variance Diagnostics, and Unit Economics / Profitability.

---

## 2. Dimensional Data Architecture (Star Schema)

The analytical data foundation is built on an industry-standard Kimball Star Schema, implemented within `Retail_Sector_Financial_Analysis.xlsx` and imported into `Retail_BvA_Dashboard.pbix`.

```
                    +--------------------+
                    |      Dim_Date      |
                    | (Date, Year, Month)|
                    +---------+----------+
                              | 1
                              |
                              | *
+-------------------+       +-----------------------+       +---------------------+
|     Dim_Store     | 1   * |    Fact_Financials    | *   1 |     Dim_Product     |
| (Store_ID, Region)|-------| (Date, Store, Product,|-------| (Product_ID, Cat.,  |
|                   |       |  Channel, Rev, Bud,   |       |  Target Margin %)   |
+-------------------+       |  COGS, OPEX, Footfall)|       +---------------------+
                            +-----------+-----------+
                                        | *
                                        |
                                        | 1
                            +-----------+-----------+
                            |      Dim_Channel      |
                            |  (Channel_ID, Name)   |
                            +-----------------------+
```

### Table Specifications:
- **`Fact_Financials`** (1,728 rows): Grain is Month $\times$ Store $\times$ Product Category $\times$ Channel over 24 calendar months (January 2024 to December 2025). Contains both Budget targets and Actual performance metrics for Revenue, Footfall, Transaction Counts, Units Sold, Cost of Goods Sold (COGS), and Operating Expenses (OPEX).
- **`Dim_Date`** (731 rows): Daily continuous date table spanning 2024-01-01 to 2025-12-31, enriched with Month Name, Fiscal Period, Quarter, and Day of Week attributes.
- **`Dim_Store`** (4 rows): Master metadata for geographic hubs (STR-01 North / Delhi NCR, STR-02 South / Bengaluru, STR-03 West / Mumbai MMR, STR-04 East / Kolkata).
- **`Dim_Product`** (6 rows): Master metadata for product categories (Jewellery, Watches, Eyewear, Wearables, Fragrances, Accessories) with benchmark target gross margin percentages.
- **`Dim_Channel`** (3 rows): Master channel attributes (CH-01 EBO, CH-02 LFS, CH-03 E-Commerce).

---

## 3. Mathematical Variance Decomposition Framework

To avoid surface-level variance reporting, the model applies formal multi-factor variance decomposition:

### 3.1 Revenue Variance ($V_{\text{Rev}}$)
$$\Delta \text{Revenue} = \text{Actual Revenue} - \text{Budget Revenue}$$

Broken down into:
1. **Price Variance**: Impact of price realization differences at actual unit volume:
   $$\text{Price Variance} = (\text{Actual ASP} - \text{Budget ASP}) \times \text{Actual Volume}$$
2. **Volume Variance**: Impact of volume expansion/contraction at budgeted price:
   $$\text{Volume Variance} = (\text{Actual Volume} - \text{Budget Volume}) \times \text{Budget ASP}$$
3. **Mix Variance**: Impact of sales distribution shifting between high-ASP (e.g., Jewellery) and lower-ASP categories (e.g., Accessories):
   $$\text{Mix Variance} = \sum \left( (\text{Actual Mix \%} - \text{Budget Mix \%}) \times (\text{Category Budget ASP} - \text{Overall Budget ASP}) \right) \times \text{Total Actual Volume}$$

### 3.2 Profitability & Margin Variances
- **COGS Variance**: $\text{Budget COGS} - \text{Actual COGS}$ (favorable when actual cost is lower than budget).
- **Gross Profit Variance**: $\text{Actual Gross Profit} - \text{Budget Gross Profit}$.
- **OPEX Variance**: $\text{Budget OPEX} - \text{Actual OPEX}$ (split into Marketing, Store Labor, Lease/Rent, Logistics, and Corporate Overhead).
- **EBITDA Variance**: $\text{Actual EBITDA} - \text{Budget EBITDA} = \Delta \text{Gross Profit} + \Delta \text{OPEX Savings}$.

---

## 4. Retail Operating Metrics & Unit Economics

The dataset incorporates operational retail drivers linking footfall to cash flow:
1. **Store Conversion Rate**:
   $$\text{Conversion Rate} = \frac{\text{Total Transactions}}{\text{Store Footfall}}$$
2. **Average Order Value (AOV)**:
   $$\text{AOV} = \frac{\text{Gross Revenue}}{\text{Total Transactions}}$$
3. **Average Selling Price (ASP)**:
   $$\text{ASP} = \frac{\text{Gross Revenue}}{\text{Units Sold}}$$
4. **Items Per Transaction (IPT) / Basket Size**:
   $$\text{Units Per Transaction} = \frac{\text{Units Sold}}{\text{Total Transactions}}$$
5. **Operating Profit Margin**:
   $$\text{EBITDA Margin \%} = \frac{\text{EBITDA}}{\text{Actual Revenue}}$$

---

## 5. DAX Engineering & Calculation Architecture

All calculations are encapsulated in modular DAX measures. Key modeling standards implemented:
- **No Implicit Measures**: Raw columns are hidden; all aggregations are defined explicitly with `DIVIDE()` to handle division-by-zero errors gracefully.
- **Strict Relationship Filter Flow**: Measures utilize `RELATED()` across 1-to-many dimensional links and avoid bidirectional filtering to maintain low memory footprint and sub-second visual rendering.
- **Time Intelligence Safety**: Time intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`) are strictly bound to `Dim_Date[Date]` rather than fact table transaction dates.

---

## 6. Model Verification & Quality Control Gates

The data preparation and DAX measures underwent a two-stage independent validation:
1. **Python Script Data Audit (`data_validation.py`)**:
   - Zero null values across primary keys, foreign keys, and monetary metrics.
   - Referential integrity: 100% of foreign keys in `Fact_Financials` map to dimension tables.
   - Boundary checks: Gross margins within 15%–65%; Conversion rates within 10%–35%.
2. **Independent DAX Verification (`independent_dax_validation.py`)**:
   - Total Actual Revenue: ₹627,770,300 across 24 months.
   - Total Budget Revenue: ₹602,593,200.
   - Net Revenue Variance: +₹25,177,100 (+4.18% beat).
   - Total Actual EBITDA: ₹144,383,270 vs Budget EBITDA: ₹137,816,500 (+₹6,566,770 beat).
   - Variance reconciliation passed: $\Delta \text{Revenue} - \Delta \text{COGS} - \Delta \text{OPEX} \equiv \Delta \text{EBITDA}$ with 0.00 rounding discrepancy.
