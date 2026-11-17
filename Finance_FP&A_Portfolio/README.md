# Institutional Finance & FP&A Engineering Portfolio

[![Financial Modeling](https://img.shields.io/badge/Financial%20Modeling-Three--Statement%20%7C%20DCF-blue.svg)](#project-01-titan-company-ltd-three-statement-financial-model--dcf-valuation)
[![Power BI](https://img.shields.io/badge/Power%20BI-Star%20Schema%20%7C%20DAX-yellow.svg)](#project-02-retail-budget-vs-actual-variance--profitability-dashboard)
[![Audit Status](https://img.shields.io/badge/Model%20Audit-100%25%20Verified%20%7C%20Zero%20Plugs-brightgreen.svg)](#master-quality-assurance--audit-status)
[![Python Engine](https://img.shields.io/badge/Python-3.12%20Automation-darkblue.svg)](#reproduction--automation-instructions)

---

## Executive Overview

This master repository showcases two institutional-grade corporate finance and business intelligence projects developed with rigorous mathematical and accounting fidelity:

1. **Project 01: Titan Company Ltd. Three-Statement Financial Model & DCF Valuation**
   - 10 Years of Audited Consolidated Historicals (FY17–FY26) + 5-Year Explicit Forecast Horizon (FY27E–FY31E).
   - 17-Worksheet Institutional Excel Model with dynamic scenario switching (Bear, Base, Bull).
   - Fully linked Balance Sheet with **₹0.00 Cr deviation across all 16 periods** (Zero Plugs).
   - Dual-Methodology DCF Valuation (Exit Multiple: **₹3,257.67 / share**; Gordon Growth: **₹368.40 / share**) alongside dual $5 \times 5$ sensitivity matrices.

2. **Project 02: Multi-Channel Retail Budget vs. Actual Variance & Profitability Dashboard**
   - Production Star Schema Data Model (1,728 grain records spanning 24 months, 4 regions, 6 categories, 3 channels).
   - Compiled Microsoft Power BI (`.pbix`) report with 3 interactive executive reporting pages.
   - 17 explicit DAX measures covering multi-factor variance decomposition (Volume, Price, Mix, OPEX) and retail unit economics.
   - 100% verified against independent Python data validation gates.

---

## Repository Directory Architecture

```
Finance_FP&A_Portfolio/
│
├── README.md                                   # Master Portfolio Documentation (This File)
│
├── Project_01_Titan_Three_Statement_DCF/       # Equity Research & Corporate Valuation Suite
│   ├── data/
│   │   ├── raw/                                # Raw audited financial statement extracts
│   │   ├── processed/                          # Standardized income statements, balance sheets, cash flows
│   │   └── source_register/                    # Source register tracking 310 data points
│   ├── model/
│   │   └── Titan_3Statement_DCF_Model.xlsx     # 17-Sheet Integrated Financial & DCF Model
│   ├── scripts/                                # 9 Automated Python Extraction & Modeling Engines
│   │   ├── data_extraction.py                  # Section-indexed parser for audited filings
│   │   ├── data_cleaning.py                    # Standardization & Ind AS 116 alignment
│   │   ├── historical_financials.py            # Historical trend & ratio analytics
│   │   ├── assumptions.py                      # Multi-scenario operational drivers (Bear/Base/Bull)
│   │   ├── financial_model.py                  # Integrated three-statement logic
│   │   ├── supporting_schedules.py             # Working Capital, PP&E, and Debt schedules
│   │   ├── dcf_valuation.py                    # UFCF, WACC, and Dual-Terminal valuation engine
│   │   ├── sensitivity_analysis.py             # Dual 5x5 matrices & visual generator
│   │   └── model_validation.py                 # Automated COM-based accounting audit
│   ├── documentation/                          # Institutional Equity Research Documentation
│   │   ├── methodology.md                      # Detailed modeling & valuation methodology
│   │   ├── assumptions_register.md             # Granular driver assumptions & citations
│   │   ├── data_sources.md                     # Data lineage, filings, and audit disclosures
│   │   ├── model_audit_report.md               # Complete audit report with zero-plug attestation
│   │   └── investment_thesis.md                # Equity research investment recommendation
│   ├── outputs/                                # Analytical Outputs & Raw Matrices
│   │   ├── valuation_summary.csv               # Baseline valuation metrics & parameters
│   │   ├── sensitivity_matrix.csv              # 5x5 WACC vs. Terminal Growth / Multiple grids
│   │   ├── model_validation_report.csv         # Period-by-period audit proof
│   │   └── valuation_charts/                   # High-resolution presentation charts
│   └── assets/                                 # Visual Model Proofs & Previews
│       ├── financial_model_preview.png         # Full model interface capture
│       ├── valuation_summary.png               # Valuation football field chart
│       └── sensitivity_analysis.png            # Sensitivity heatmaps
│
├── Project_02_Retail_Budget_vs_Actual/         # Corporate FP&A & Power BI Analytics Suite
│   ├── data/
│   │   ├── raw/                                # Raw transaction seed parameters
│   │   ├── processed/                          # Star schema dimension & fact tables
│   │   └── Retail_Sector_Financial_Analysis.xlsx # Multi-tab Kimball Star Schema Workbook
│   ├── powerbi/
│   │   ├── Retail_BvA_Dashboard.pbix           # Compiled 3-Page Power BI Report Package
│   │   ├── dax_measures.md                     # Complete library of 17 DAX formulas
│   │   └── data_dictionary.md                  # Comprehensive dimensional data dictionary
│   ├── scripts/                                # Python Data Engineering & DAX Verifiers
│   │   ├── generate_retail_dataset.py          # Realistic retail variance dataset generator
│   │   ├── data_validation.py                  # 8-gate automated data quality checker
│   │   └── independent_dax_validation.py       # Independent mathematical verification of DAX
│   ├── documentation/                          # Strategic FP&A Documentation
│   │   ├── project_methodology.md              # Kimball modeling & variance mathematics
│   │   ├── business_insights.md                # C-suite diagnostic & strategic recommendations
│   │   ├── dashboard_guide.md                  # Power BI navigation & deployment guide
│   │   └── data_quality_report.md              # 8-point data quality signoff report
│   └── assets/                                 # High-Resolution Dashboard Screenshots
│       ├── executive_dashboard.png             # Page 1: Executive KPI Overview
│       ├── variance_dashboard.png              # Page 2: EBITDA Variance Waterfall & Diagnostics
│       └── profitability_dashboard.png         # Page 3: Channel & Category Unit Economics
│
└── shared/                                     # Cross-Project Assets & Standards
    ├── requirements.txt                        # Unified Python dependencies
    ├── validation_summary.md                   # Consolidated audit results & quality gates
    └── source_disclosures.md                   # Compliance, standards, and data disclosures
```

---

## Project 01: Titan Company Ltd. Financial Model & DCF Highlights

### Visual Proofs & Deliverables

#### 1. Integrated Financial Model Architecture
![Financial Model Preview](Project_01_Titan_Three_Statement_DCF/assets/financial_model_preview.png)

#### 2. Valuation Football Field & DCF Summary
![Valuation Football Field](Project_01_Titan_Three_Statement_DCF/assets/valuation_summary.png)

#### 3. Dual-Methodology Sensitivity Matrix
![Sensitivity Analysis](Project_01_Titan_Three_Statement_DCF/assets/sensitivity_analysis.png)

### Key Analytical Findings
- **WACC Formulation**: Calculated at **14.43%** ($R_f=7.0\%$, Equity Beta $\beta=1.15$, Market Risk Premium $=7.0\%$, Cost of Debt $K_d=7.50\%$, Tax Rate $=25.17\%$).
- **Valuation Divergence Analysis**:
  - **Exit Multiple Implied Target Price**: **₹3,257.67 / share** (at 35.0x FY31E EBITDA), aligning with market pricing of Titan's dominant 8%+ jewellery market share and brand runway.
  - **Gordon Growth Implied Target Price**: **₹368.40 / share** (at 5.5% terminal growth, normalized steady-state reinvestment rate $\text{RR} = g/\text{ROIC} = 27.5\%$).
  - **Balance Sheet Check**: **₹0.00 Cr deviation** across all 16 historical and forecast periods.

---

## Project 02: Retail Budget vs. Actual Power BI Highlights

### Visual Proofs & Deliverables

#### 1. Executive KPI Scorecard & Trend Trajectory
![Executive Dashboard](Project_02_Retail_Budget_vs_Actual/assets/executive_dashboard.png)

#### 2. EBITDA Variance Waterfall & Multidimensional Diagnostics
![Variance Dashboard](Project_02_Retail_Budget_vs_Actual/assets/variance_dashboard.png)

#### 3. Channel Economics & Unit Profitability
![Profitability Dashboard](Project_02_Retail_Budget_vs_Actual/assets/profitability_dashboard.png)

### Key FP&A Metrics (CY2024–CY2025)
- **Top-Line Performance**: Actual Revenue **₹627.77 Cr** vs. Budget **₹602.59 Cr** (+₹25.18 Cr / **+4.18% Favorable**).
- **Operating Profitability**: Actual EBITDA **₹144.38 Cr (23.00%)** vs. Budget **₹137.82 Cr (22.87%)** (+₹6.57 Cr / **+4.76% Favorable**).
- **Channel Economic Disparity**:
  - Exclusive Brand Outlets (EBO): 27.3% EBITDA margin, ₹12,450 AOV.
  - E-Commerce: 13.8% EBITDA margin, impacted by 12.5% CAC and return logistics.

---

## Master Quality Assurance & Audit Status

Both models have been subjected to exhaustive automated programmatic testing:

| Check Domain | Audit Metric | Required Threshold | Result |
| :--- | :--- | :--- | :--- |
| **Titan Balance Sheet** | Total Assets - (Total Liab + Equity) | ₹0.00 Cr | **PASSED (₹0.00 Cr)** |
| **Titan Cash Flow** | Cash Flow Ending Cash - Balance Sheet Cash | ₹0.00 Cr | **PASSED (₹0.00 Cr)** |
| **Titan Schedules** | PP&E, Debt, Retained Earnings Roll-Forward | ₹0.00 Cr | **PASSED (₹0.00 Cr)** |
| **Retail Data Quality** | Null values, Duplicate keys, Referential integrity | 0 violations | **PASSED (8/8 Gates)** |
| **Retail DAX Integrity**| Python vs. DAX Variance Reconciliation | Matching to ₹0.00 | **PASSED (17/17 Measures)** |

---

## Reproduction & Automation Instructions

To execute the data pipelines, audit checks, and models from source:

```bash
# 1. Clone repository
git clone https://github.com/sarvesh270707/Three-Statement-DCF-Valuation-Titan.git
cd Three-Statement-DCF-Valuation-Titan

# 2. Install dependencies
pip install -r Finance_FP&A_Portfolio/shared/requirements.txt

# 3. Execute Project 01 (Titan Model & COM Audit)
python Finance_FP&A_Portfolio/Project_01_Titan_Three_Statement_DCF/scripts/model_validation.py

# 4. Execute Project 02 (Retail Data Validation & DAX Engine)
python Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/scripts/data_validation.py
python Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/scripts/independent_dax_validation.py
```
