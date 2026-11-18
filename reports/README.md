# Finance & FP&A Engineering Portfolio
## Project 01: Titan Company Ltd. Three-Statement Financial Model & DCF Valuation
## Project 02: Multi-Channel Retail Budget vs. Actual Variance & Profitability Dashboard

---

## 🌟 Master Portfolio Overview

This repository hosts a production-grade corporate finance, equity valuation, and financial planning & analysis (FP&A) portfolio developed with institutional rigor, zero accounting plugs, and complete mathematical verification.

The primary master architecture is housed under [`Finance_FP&A_Portfolio/`](Finance_FP&A_Portfolio/README.md):

### 1. [Project 01: Titan Company Ltd. Three-Statement Model & DCF Valuation](Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/)
- **10-Year Audited Historicals (FY17–FY26)** + **5-Year Explicit Forecasts (FY27E–FY31E)**.
- **17-Worksheet Institutional Excel Model** (`Titan_3Statement_DCF_Model.xlsx`) featuring dynamic scenario switching (Bear, Base, Bull).
- **100% Reconciled Balance Sheet**: **₹0.00 Cr deviation across all 16 annual periods**.
- **Dual-Methodology DCF Valuation**:
  - Exit Multiple (35.0x FY31E EBITDA): **₹3,257.67 / share**
  - Gordon Growth (5.5% terminal growth, normalized reinvestment): **₹368.40 / share**
- **Automated Validation**: COM automation audit script (`model_validation.py`), dual 5x5 sensitivity matrices, football field charts, and 5 exhaustive institutional research documents.

### 2. [Project 02: Retail Budget vs. Actual Variance & Profitability Dashboard](Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/)
- **Production Star Schema Data Model**: 1,728 grain records spanning 24 months (CY2024–CY2025), 4 regions, 6 categories, and 3 distribution channels.
- **Compiled Microsoft Power BI Platform** (`Retail_BvA_Dashboard.pbix`): 3-page executive reporting suite (Executive Summary, Variance Decomposition Waterfall, Unit Profitability).
- **17 Production DAX Measures**: Complete time intelligence, volume/price/mix variance engines, and retail operating KPIs (AOV, ASP, Conversion Rate).
- **Independent Validation**: 8 automated data quality gates and zero-defect DAX cross-verification against Python calculations.

---

## 📂 Repository Directory Tree

```
DCF-Valuation-Model/
│
├── Finance_FP&A_Portfolio/                     # Master Enterprise Portfolio Directory
│   ├── README.md                               # Comprehensive Master Portfolio Readme
│   │
│   ├── Project_01_Titan_Three_Statement_DCF/   # Project 01: Titan Equity Valuation Suite
│   │   ├── data/                               # Raw & processed audited financial statements
│   │   ├── model/                              # Titan_3Statement_DCF_Model.xlsx (17 sheets)
│   │   ├── scripts/                            # 9 Python modeling & validation scripts
│   │   ├── documentation/                      # 5 Research & audit reports (methodology, thesis)
│   │   ├── outputs/                            # CSV summaries, sensitivity matrices, charts
│   │   └── assets/                             # High-res model previews & football field charts
│   │
│   ├── Project_02_Retail_Budget_vs_Actual/     # Project 02: Retail FP&A & Power BI Suite
│   │   ├── data/                               # Retail_Sector_Financial_Analysis.xlsx (Star Schema)
│   │   ├── powerbi/                            # Retail_BvA_Dashboard.pbix (3 Pages, 17 DAX)
│   │   ├── scripts/                            # Dataset generation & DAX verification scripts
│   │   ├── documentation/                      # Methodology, insights, dashboard guide, data QA
│   │   └── assets/                             # High-res executive dashboard screenshots
│   │
│   └── shared/                                 # Cross-project requirements & disclosures
│       ├── requirements.txt                    # Master Python package dependencies
│       ├── validation_summary.md               # Audit gates & reconciliation proof
│       └── source_disclosures.md               # Data lineage & compliance disclosures
│
├── data/                                       # Historical seed data
├── output/                                     # Legacy outputs
├── assests/                                    # Legacy visual assets
└── README.md                                   # Root Navigation & Summary
```

---

## 🚀 Quick Execution Guide

```bash
# Clone the repository
git clone https://github.com/sarvesh270707/Three-Statement-DCF-Valuation-Titan.git
cd Three-Statement-DCF-Valuation-Titan

# Install dependencies
pip install -r Finance_FP&A_Portfolio/shared/requirements.txt

# Run Project 01 Excel COM Model Audit
python Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/scripts/model_validation.py

# Run Project 02 Data Quality Audit & DAX Cross-Validation
python Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/scripts/data_validation.py
python Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/scripts/independent_dax_validation.py
```

---

## 📊 Live Portfolio Link
The web portfolio integration is hosted live at [sarveshworks.vercel.app](https://sarveshworks.vercel.app).
