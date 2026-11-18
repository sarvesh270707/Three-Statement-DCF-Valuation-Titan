# Project 01: Titan Company Ltd. | Three-Statement Financial Model & DCF Valuation
## Financial Engineering & Valuation Methodology

---

### Executive Summary

Titan Company Limited (NSE: `TITAN`, BSE: `500114`), a joint venture between the Tata Group and TIDCO, represents India's preeminent consumer lifestyle company with market leadership across jewellery (*Tanishq*, *Mia*, *Zoya*, *Caratlane*), watches and wearables (*Titan*, *Fastrack*, *Sonata*), eyewear (*Titan Eyeplus*), and emerging fashion segments (*Taneira*, *Skinn*).

This project develops an integrated, audited, non-circular institutional Three-Statement Financial Model and Discounted Cash Flow (DCF) valuation for Titan Company Limited covering ten historical audited fiscal years (**FY17 - FY26**) and a five-year discrete forecast horizon (**FY27E - FY31E**).

---

### 1. Architectural Principles & Standard Conventions

The financial model was constructed adhering to institutional investment banking guidelines:

1. **Strict Accounting Integrity**: Assets minus Total Liabilities and Equity equals ₹0.00 across all 16 historical and forecast periods without artificial balancing plugs or circular references.
2. **Professional Color Coding**:
   - **Blue font (`#0000FF`)**: Hardcoded user inputs and operational drivers.
   - **Black font (`#000000`)**: Intra-sheet dynamic mathematical formulas.
   - **Green font (`#008000`)**: Cross-sheet linked formulas.
   - **Red bold (`#B91C1C`)**: Reconciliation warnings and error thresholds.
3. **Number Formatting**:
   - Currency: `_-₹* #,##0.00_-;_-₹* (#,##0.00)_-;_-₹* "-"??_-;_-@_-`
   - Multiples: `0.0"x"`
   - Percentage: `0.0%`
   - Negative numbers formatted in standard investment banking parentheses.

---

### 2. Operational Revenue Build & Driver Methodology

Historical analysis reveals that jewellery represents ~88% of consolidated revenue, followed by watches (~8%), eyewear (~2%), and emerging businesses (~2%).

#### Forecast Revenue Trajectory:
- **FY27E**: ₹1,00,721.60 Cr (+15.0% YoY) driven by consumer demand expansion following the July 2024 customs duty reduction on gold imports from 15% to 6%, accelerating formalization.
- **FY28E**: ₹1,14,822.58 Cr (+14.0% YoY) through accelerated store expansion across Tier 2 and Tier 3 Indian cities.
- **FY29E**: ₹1,29,749.52 Cr (+13.0% YoY) scaling omnichannel digitally native acquisitions (Caratlane) and international store roll-outs (GCC and North America).
- **FY30E**: ₹1,45,319.46 Cr (+12.0% YoY) sustained market share capture from the unorganized jewellery sector.
- **FY31E**: ₹1,62,757.79 Cr (+12.0% YoY) terminal discrete forecast period, transitioning toward mature long-term growth.

---

### 3. Integrated Supporting Schedules

#### 3.1 Working Capital Schedule
- **Accounts Receivable**: Driven by Days Sales Outstanding (DSO) of 5.0 days, reflecting the predominantly immediate cash, credit card, and digital consumer payment structure.
- **Inventories**: Driven by Days Inventory Outstanding (DIO) of 205.0 days, reflecting substantial physical holding of gold, precious gems, and diamond jewellery across 3,000+ retail stores.
- **Trade Payables & Operating Liabilities**: Driven by Days Payable Outstanding (DPO) of 42.0 days against cost of goods sold.
- **Operating Working Capital (OWC)**: Calculated as Receivables + Inventory - Payables. Change in OWC directly reconciles with Operating Cash Flow.

#### 3.2 Property, Plant & Equipment (PP&E) Schedule
- **Opening Net Block**: Linked directly from preceding year's closing net block.
- **Capital Expenditure (CapEx)**: Modeled at 2.5% of revenue (Base Case), funding retail store fitouts, high-tech diamond grading laboratories, and automated manufacturing facilities.
- **Depreciation**: Calculated at 18.0% of opening net block, aligning with historical asset turnover and statutory depreciation rates.
- **Closing Net Block**: $\text{Opening PP\&E} + \text{CapEx} - \text{Depreciation} - \text{Disposals}$.

#### 3.3 Debt Financing Schedule
- Modeled to maintain Titan's target capital structure while financing working capital credit requirements through commercial paper and short-term bank credit lines.
- Interest expense calculated at 7.50% pre-tax borrowing cost applied to average outstanding debt.

---

### 4. Cash Flow Statement Integration

1. **Operating Cash Flow (CFO)**:
   $$\text{CFO} = \text{Net Income (PAT)} + \text{Depreciation} - \Delta\text{Receivables} - \Delta\text{Inventories} + \Delta\text{Payables}$$
2. **Investing Cash Flow (CFI)**:
   $$\text{CFI} = -\text{CapEx} + \text{Other Investing Cash Flows}$$
3. **Financing Cash Flow (CFF)**:
   $$\text{CFF} = \text{New Borrowings} - \text{Debt Repayments} - \text{Dividends Paid}$$
4. **Closing Cash Balance**:
   $$\text{Closing Cash}_t = \text{Closing Cash}_{t-1} + \text{Net Change in Cash}_t$$

---

### 5. Cost of Capital (WACC) Build-Up

Using the Capital Asset Pricing Model (CAPM):
- **Risk-Free Rate ($R_f$)**: **7.00%**, benchmarked to the India 10-Year Government Bond Yield (G-Sec).
- **Equity Risk Premium (ERP)**: **7.00%**, reflecting the Indian market risk premium (Prof. Aswath Damodaran estimates).
- **Beta ($\beta$)**: **1.15**, 5-year regression against Nifty 50.
- **Cost of Equity ($K_e$)**:
  $$K_e = 7.00\% + 1.15 \times 7.00\% = 15.05\%$$
- **Pre-Tax Cost of Debt ($K_d$)**: 7.50%
- **Marginal Corporate Tax Rate ($t$)**: 25.17% (Section 115BAA)
- **After-Tax Cost of Debt ($K_d \times (1-t)$)**:
  $$7.50\% \times (1 - 0.2517) = 5.61\%$$
- **Capital Structure Weights**:
  - Market Value of Equity: ₹4,35,909.80 Cr (93.44%)
  - Total Debt: ₹30,621.00 Cr (6.56%)
- **WACC**:
  $$\text{WACC} = (93.44\% \times 15.05\%) + (6.56\% \times 5.61\%) = \mathbf{14.43\%}$$

---

### 6. DCF Valuation & Terminal Value Methodologies

#### Method 1: EV/EBITDA Exit Multiple Method (Primary)
- FY31E EBITDA: ₹17,089.57 Cr
- Target Exit Multiple: **35.0x** (historical peer group multiple for Indian consumer luxury leaders)
- Terminal Value: ₹5,98,135.12 Cr
- PV of Terminal Value: ₹3,04,852.25 Cr
- Enterprise Value: ₹3,14,422.17 Cr
- Less Net Debt (Debt ₹30,621 Cr - Cash ₹1,917 Cr - Investments ₹3,506 Cr): ₹25,198.00 Cr
- Implied Equity Value: ₹2,89,224.17 Cr
- **Implied Share Price**: **₹3,257.67 per share**

#### Method 2: Normalized Gordon Growth Method
- Terminal growth rate ($g$): **5.50%**
- Steady-state reinvestment rate: $g / \text{ROIC} = 5.5\% / 20.0\% = 27.5\%$
- Normalized Terminal UFCF: ₹8,467.43 Cr
- Terminal Value: ₹94,839.87 Cr
- Implied Share Price: **₹368.40 per share**

---

### 7. Sensitivity Analysis Framework

A dual $5 \times 5$ sensitivity matrix was constructed testing:
1. **WACC (13.43% to 15.43%) vs. Exit Multiple (28.0x to 45.0x)**:
   - Yields an implied valuation range from **₹2,451.63** (Bearish macro slowdown) to **₹4,439.26** (Premium luxury valuation).
2. **WACC (13.43% to 15.43%) vs. Terminal Growth (5.00% to 6.00%)**:
   - Yields a fundamental steady-state intrinsic range from **₹281.11** to **₹489.67**.
