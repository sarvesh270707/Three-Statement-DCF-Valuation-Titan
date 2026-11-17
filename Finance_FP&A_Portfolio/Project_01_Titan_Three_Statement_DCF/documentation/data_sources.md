# Project 01: Titan Company Ltd. | Data Sources Register & Regulatory Disclosures

---

### Primary Data Sources Register

All historical financial inputs utilized in the model have been reconciled against audited consolidated regulatory filings.

| Source ID | Regulatory Entity / Source Name | URL / Portal | Primary Data Extracted | Verification Authority | Retrieval Timestamp |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **SRC-01** | Titan Investor Relations Portal | [titancompany.in/investors](https://www.titancompany.in/investors) | FY17-FY26 Consolidated Annual Reports, Investor Presentations, Audited Financial Statements | Board of Directors / Statutory Auditors (B S R & Co. LLP) | 2026-11-17 |
| **SRC-02** | National Stock Exchange of India (NSE) | [nseindia.com (TITAN)](https://www.nseindia.com/get-quotes/equity?symbol=TITAN) | Share Price, Market Capitalization, Float, Free-float Beta | National Stock Exchange Regulatory Filings | 2026-11-17 |
| **SRC-03** | Bombay Stock Exchange (BSE) | [bseindia.com (500114)](https://www.bseindia.com/stock-share-price/titan-company-ltd/titan/500114/) | Corporate Action Register, Dividend Declarations, Shareholding Pattern | Bombay Stock Exchange Corporate Announcements | 2026-11-17 |
| **SRC-04** | Screener.in Consolidated Database | [screener.in/company/TITAN/consolidated/](https://www.screener.in/company/TITAN/consolidated/) | Standardized 10-Year Consolidated Financial Statement History | Screener Financial Intelligence Platform | 2026-11-17 |
| **SRC-05** | Reserve Bank of India (RBI) / CCIL | [ccilindia.com](https://www.ccilindia.com) | Benchmark 10-Year Government of India Bond Yield (7.00% - 7.15%) | Clearing Corporation of India / RBI Public Debt Office | 2026-11-17 |
| **SRC-06** | Damodaran Online (NYU Stern) | [pages.stern.nyu.edu/~adamodar/](https://pages.stern.nyu.edu/~adamodar/) | India Country Risk Premium (CRP) & Equity Risk Premium (ERP: 7.00%) | Prof. Aswath Damodaran Research Data | 2026-11-17 |

---

### Reporting Unit & Accounting Taxonomy Disclosures

1. **Reporting Basis**: All historical numbers reflect **Consolidated Financial Statements** prepared in accordance with Indian Accounting Standards (Ind AS) notified under Section 133 of the Companies Act, 2013. Standalone figures have been excluded to preserve holistic corporate reporting.
2. **Monetary Unit**: Indian Rupees (₹) in **Crore** (1 Crore = 10 Million INR = 10,000,000 INR).
3. **Fiscal Year Definition**: April 1 to March 31. For example, FY26 represents the twelve months ended March 31, 2026.
4. **Data Verification Register**: A complete audit ledger containing 310 individual verified historical line items is persisted in [`data/source_register/source_register.csv`](file:///c:/Users/DELL/Desktop/DCF-Valuation-Model/Finance_FP%26A_Portfolio/Project_01_Titan_Three_Statement_DCF/data/source_register/source_register.csv) and worksheet `17_Source_Register` within the Excel model.
