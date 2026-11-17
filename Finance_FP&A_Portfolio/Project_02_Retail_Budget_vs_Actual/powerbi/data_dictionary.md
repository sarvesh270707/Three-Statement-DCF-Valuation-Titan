# Project 02: Retail FP&A | Power BI Data Dictionary & Schema Specification

---

### Star-Schema Architecture

The Power BI data model adheres strictly to Kimberly-Star Schema architecture consisting of one central Fact table and three surrounding Dimension tables:

```
                  +-----------------------+
                  |        DimDate        |
                  +-----------------------+
                  | Date (PK)             |
                  | Year                  |
                  | Month                 |
                  | Month_Name            |
                  | Quarter               |
                  +-----------+-----------+
                              | 1
                              | 
                              | *
+--------------------+   +----+--------------------+   +-----------------------+
|     DimRegion      |   |   FactRetailPerformance |   |   DimProductCategory  |
+--------------------+   +-------------------------+   +-----------------------+
| Region (PK)        |<--| Transaction_ID (PK)     |-->| Product_Category (PK) |
| Regional_Director  | 1 | Date (FK)               | * | Division              |
| Regional_HQ        | * | Region (FK)             | 1 | Category_Lead         |
| Market_Tier        |   | Product_Category (FK)   |   | Target_Margin_Pct     |
+--------------------+   | Retail_Channel          |   +-----------------------+
                         | Units_Sold              |
                         | Average_Selling_Price   |
                         | Budgeted_Revenue        |
                         | Actual_Revenue          |
                         | Budgeted_Expenses       |
                         | Actual_Expenses         |
                         | Product_Cost_COGS       |
                         | Marketing_Expenses      |
                         | Personnel_Expenses      |
                         | Distribution_Expenses   |
                         | Other_Operating_Expenses|
                         +-------------------------+
```

---

### Table Specifications

#### 1. FactRetailPerformance (Central Fact Table)
- **Granularity**: One record per Month × Region × Product Category × Retail Channel.
- **Total Records**: 1,728 rows (24 months from Jan 2025 to Dec 2026).

| Column Name | Data Type | Key Type | Sample Value | Description & Business Logic |
| :--- | :--- | :---: | :--- | :--- |
| `Transaction_ID` | Text | Primary Key | `TXN-10001` | Unique transaction grain identifier. |
| `Date` | Date | Foreign Key | `2025-01-01` | First day of reporting calendar month. |
| `Region` | Text | Foreign Key | `North` | Geographical sales territory. |
| `Product_Category` | Text | Foreign Key | `Electronics & Gadgets` | Product merchandise hierarchy. |
| `Retail_Channel` | Text | Attribute | `Flagship Store` | Distribution store format. |
| `Units_Sold` | Whole Number | Measure Base | `184` | Physical units transacted. |
| `Average_Selling_Price` | Currency | Attribute | `₹25,000` | Realized blended price per unit. |
| `Budgeted_Revenue` | Currency | Fact | `₹4,600,000` | Target revenue baseline. |
| `Actual_Revenue` | Currency | Fact | `₹4,642,800` | Realized gross revenue. |
| `Budgeted_Expenses` | Currency | Fact | `₹4,186,000` | Approved operational budget. |
| `Actual_Expenses` | Currency | Fact | `₹4,235,100` | Realized operational costs. |
| `Product_Cost_COGS` | Currency | Fact | `₹3,755,200` | Direct merchandise acquisition cost. |
| `Marketing_Expenses` | Currency | Fact | `₹184,000` | Promotion, digital ads, and POS branding. |
| `Personnel_Expenses` | Currency | Fact | `₹506,000` | Store staff payroll and commissions. |
| `Distribution_Expenses`| Currency | Fact | `₹138,000` | Logistics, warehousing, and freight. |
| `Other_Operating_Expenses` | Currency | Fact | `₹230,000` | Store rent, utilities, and insurance. |

#### 2. DimDate (Date Dimension Table)
- **Marked as Date Table**: Yes
- **Range**: 2025-01-01 to 2026-12-01 (24 Months)

| Column Name | Data Type | Key Type | Sample Value | Description |
| :--- | :--- | :---: | :--- | :--- |
| `Date` | Date | Primary Key | `2025-01-01` | Unique date key. |
| `Year` | Whole Number | Attribute | `2025` | Calendar year. |
| `Month` | Whole Number | Attribute | `1` | Calendar month index (1-12). |
| `Month_Name` | Text | Attribute | `January` | Full English month name. |
| `Quarter` | Text | Attribute | `Q1` | Calendar quarter designation. |

#### 3. DimRegion (Geographical Dimension)
- **Cardinality**: 4 Rows

| Column Name | Data Type | Key Type | Sample Value | Description |
| :--- | :--- | :---: | :--- | :--- |
| `Region` | Text | Primary Key | `North` | Primary territory code. |
| `Regional_Director` | Text | Attribute | `Vikram Sharma` | Senior executive territory owner. |
| `Regional_HQ` | Text | Attribute | `New Delhi` | Administrative office center. |
| `Market_Tier` | Text | Attribute | `Tier 1 Core` | Economic maturity classification. |

#### 4. DimProductCategory (Merchandise Hierarchy)
- **Cardinality**: 6 Rows

| Column Name | Data Type | Key Type | Sample Value | Description |
| :--- | :--- | :---: | :--- | :--- |
| `Product_Category` | Text | Primary Key | `Fashion & Apparel` | Segment descriptor. |
| `Division` | Text | Attribute | `Apparel & Lifestyle` | High-level business unit. |
| `Category_Lead` | Text | Attribute | `Pooja Kapoor` | FP&A category lead owner. |
| `Target_Margin_Pct` | Percentage | Attribute | `42.0%` | Baseline target gross margin. |
