# Titan Company Ltd - 3-Statement Financial Model & DCF Valuation

A comprehensive 3-Statement Financial Model and Discounted Cash Flow (DCF) Valuation for **Titan Company Ltd**.

## Project Overview
- **Data Source:** Screener.in extract (`data/Titan Company.xlsx`)
- **Generated Model:** Multi-tab Excel financial model (`output/Titan_3Statement_DCF_Model.xlsx`)
  - **Cover & Summary:** Current market price, implied intrinsic value, and upside/downside summary.
  - **Historical Data:** Historical financial statement inputs (P&L, Balance Sheet, Cash Flow).
  - **Assumptions & Drivers:** Operational assumptions (revenue growth rate, margin drivers, working capital days).
  - **3-Statement Model:** Integrated forecast across Income Statement, Balance Sheet, and Cash Flow Statement with balance checks.
  - **Supporting Schedules:** Working capital, PPE/Depreciation, and Debt schedules.
  - **WACC & DCF:** Discounted Cash Flow model calculating Cost of Equity (CAPM), WACC, Terminal Value, and Implied Intrinsic Value per share.

## Project Structure
```
DCF-Valuation-Model/
├── data/
│   └── Titan Company.xlsx               # Raw financial statement export
├── output/
│   └── Titan_3Statement_DCF_Model.xlsx  # Generated 3-Statement & DCF workbook
├── assests/                             # Charts, screenshots, and visual assets
├── pdf/                                 # Exported reports and summaries
├── build_model.py                       # Python build script using openpyxl & pandas
└── README.md
```

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas openpyxl
   ```
2. Run the build script:
   ```bash
   python build_model.py
   ```
