"""
Project 02: Power BI .pbix Generator Engine
Compiles a valid Power BI Desktop file (.pbix) containing Star-Schema DataModelSchema, 17 DAX measures, and 3 report pages.
"""

import zipfile
import json
import os
import shutil

OUTPUT_DIR = 'Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/powerbi'
PBIX_PATH = os.path.join(OUTPUT_DIR, 'Retail_BvA_Dashboard.pbix')

EXCEL_SOURCE = os.path.abspath('Finance_FP&A_Portfolio/Project_02_Retail_Budget_vs_Actual/data/Retail_Sector_Financial_Analysis.xlsx')

print(f"Compiling Power BI package: {PBIX_PATH}")

# 1. Version string
version_content = "2.159.1231.0".encode('utf-16le')

# 2. [Content_Types].xml
content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="" />
  <Default Extension="xml" ContentType="" />
  <Override PartName="/Version" ContentType="" />
  <Override PartName="/Settings" ContentType="" />
  <Override PartName="/DataModelSchema" ContentType="" />
  <Override PartName="/Report/Layout" ContentType="" />
  <Override PartName="/DiagramLayout" ContentType="" />
</Types>"""

# 3. Settings
settings_obj = {
    "version": "2.159.1231.0",
    "displaySettings": {
        "showGridlines": True,
        "snapToGrid": True
    },
    "queryEditorSettings": {
        "formulaBarEnabled": True
    }
}
settings_content = json.dumps(settings_obj).encode('utf-16le')

# 4. DataModelSchema (TMSL - Tabular Model Scripting Language)
data_model_schema = {
    "name": "Retail_BvA_Model",
    "compatibilityLevel": 1550,
    "model": {
        "culture": "en-US",
        "dataAccessOptions": {
            "legacyRedirects": True,
            "returnErrorValuesAsNull": True
        },
        "defaultPowerBIDataSourceVersion": "powerBI_V3",
        "tables": [
            {
                "name": "FactRetailPerformance",
                "columns": [
                    {"name": "Transaction_ID", "dataType": "string", "sourceColumn": "Transaction_ID"},
                    {"name": "Date", "dataType": "dateTime", "sourceColumn": "Date", "formatString": "yyyy-mm-dd"},
                    {"name": "Year", "dataType": "int64", "sourceColumn": "Year"},
                    {"name": "Month", "dataType": "int64", "sourceColumn": "Month"},
                    {"name": "Month_Name", "dataType": "string", "sourceColumn": "Month_Name"},
                    {"name": "Quarter", "dataType": "string", "sourceColumn": "Quarter"},
                    {"name": "Region", "dataType": "string", "sourceColumn": "Region"},
                    {"name": "Product_Category", "dataType": "string", "sourceColumn": "Product_Category"},
                    {"name": "Retail_Channel", "dataType": "string", "sourceColumn": "Retail_Channel"},
                    {"name": "Units_Sold", "dataType": "int64", "sourceColumn": "Units_Sold"},
                    {"name": "Average_Selling_Price", "dataType": "decimal", "sourceColumn": "Average_Selling_Price", "formatString": "\\$#,0;(\\$#,0);\\$#,0"},
                    {"name": "Budgeted_Revenue", "dataType": "decimal", "sourceColumn": "Budgeted_Revenue", "formatString": "₹#,##0"},
                    {"name": "Actual_Revenue", "dataType": "decimal", "sourceColumn": "Actual_Revenue", "formatString": "₹#,##0"},
                    {"name": "Budgeted_Expenses", "dataType": "decimal", "sourceColumn": "Budgeted_Expenses", "formatString": "₹#,##0"},
                    {"name": "Actual_Expenses", "dataType": "decimal", "sourceColumn": "Actual_Expenses", "formatString": "₹#,##0"},
                    {"name": "Product_Cost_COGS", "dataType": "decimal", "sourceColumn": "Product_Cost_COGS", "formatString": "₹#,##0"},
                    {"name": "Marketing_Expenses", "dataType": "decimal", "sourceColumn": "Marketing_Expenses", "formatString": "₹#,##0"},
                    {"name": "Personnel_Expenses", "dataType": "decimal", "sourceColumn": "Personnel_Expenses", "formatString": "₹#,##0"},
                    {"name": "Distribution_Expenses", "dataType": "decimal", "sourceColumn": "Distribution_Expenses", "formatString": "₹#,##0"},
                    {"name": "Other_Operating_Expenses", "dataType": "decimal", "sourceColumn": "Other_Operating_Expenses", "formatString": "₹#,##0"}
                ],
                "measures": [
                    {"name": "Total Budget Revenue", "expression": "SUM(FactRetailPerformance[Budgeted_Revenue])", "formatString": "₹#,##0"},
                    {"name": "Total Actual Revenue", "expression": "SUM(FactRetailPerformance[Actual_Revenue])", "formatString": "₹#,##0"},
                    {"name": "Revenue Variance", "expression": "[Total Actual Revenue] - [Total Budget Revenue]", "formatString": "₹#,##0"},
                    {"name": "Revenue Variance %", "expression": "DIVIDE([Revenue Variance], [Total Budget Revenue], 0)", "formatString": "0.0%"},
                    {"name": "Revenue Achievement %", "expression": "DIVIDE([Total Actual Revenue], [Total Budget Revenue], 0)", "formatString": "0.0%"},
                    {"name": "Total Budget Expenses", "expression": "SUM(FactRetailPerformance[Budgeted_Expenses])", "formatString": "₹#,##0"},
                    {"name": "Total Actual Expenses", "expression": "SUM(FactRetailPerformance[Actual_Expenses])", "formatString": "₹#,##0"},
                    {"name": "Expense Variance", "expression": "[Total Actual Expenses] - [Total Budget Expenses]", "formatString": "₹#,##0"},
                    {"name": "Expense Variance %", "expression": "DIVIDE([Expense Variance], [Total Budget Expenses], 0)", "formatString": "0.0%"},
                    {"name": "Budgeted Profit", "expression": "[Total Budget Revenue] - [Total Budget Expenses]", "formatString": "₹#,##0"},
                    {"name": "Actual Profit", "expression": "[Total Actual Revenue] - [Total Actual Expenses]", "formatString": "₹#,##0"},
                    {"name": "Profit Variance", "expression": "[Actual Profit] - [Budgeted Profit]", "formatString": "₹#,##0"},
                    {"name": "Actual Profit Margin", "expression": "DIVIDE([Actual Profit], [Total Actual Revenue], 0)", "formatString": "0.0%"},
                    {"name": "Budget Profit Margin", "expression": "DIVIDE([Budgeted Profit], [Total Budget Revenue], 0)", "formatString": "0.0%"},
                    {"name": "Cost Overrun Alert", "expression": "IF([Total Actual Expenses] > [Total Budget Expenses], \"Cost Overrun\", \"On Track\")"},
                    {"name": "Profitability Status", "expression": "IF([Actual Profit] >= [Budgeted Profit], \"Above Budget\", \"Below Budget\")"},
                    {"name": "Variance Status", "expression": "SWITCH(TRUE(), [Profit Variance] > 0, \"Favourable\", [Profit Variance] < 0, \"Unfavourable\", \"On Plan\")"}
                ],
                "partitions": [
                    {
                        "name": "FactRetailPerformance-Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": f'let Source = Excel.Workbook(File.Contents("{EXCEL_SOURCE}"), null, true), Fact_Sheet = Source{{[Item="FactRetailPerformance",Kind="Sheet"]}}[Data] in Fact_Sheet'
                        }
                    }
                ]
            },
            {
                "name": "DimDate",
                "dataCategory": "Time",
                "columns": [
                    {"name": "Date", "dataType": "dateTime", "isKey": True, "sourceColumn": "Date", "formatString": "yyyy-mm-dd"},
                    {"name": "Year", "dataType": "int64", "sourceColumn": "Year"},
                    {"name": "Month", "dataType": "int64", "sourceColumn": "Month"},
                    {"name": "Month_Name", "dataType": "string", "sourceColumn": "Month_Name"},
                    {"name": "Quarter", "dataType": "string", "sourceColumn": "Quarter"}
                ],
                "partitions": [
                    {
                        "name": "DimDate-Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": f'let Source = Excel.Workbook(File.Contents("{EXCEL_SOURCE}"), null, true), Date_Sheet = Source{{[Item="DimDate",Kind="Sheet"]}}[Data] in Date_Sheet'
                        }
                    }
                ]
            },
            {
                "name": "DimRegion",
                "columns": [
                    {"name": "Region", "dataType": "string", "isKey": True, "sourceColumn": "Region"},
                    {"name": "Regional_Director", "dataType": "string", "sourceColumn": "Regional_Director"},
                    {"name": "Regional_HQ", "dataType": "string", "sourceColumn": "Regional_HQ"},
                    {"name": "Market_Tier", "dataType": "string", "sourceColumn": "Market_Tier"}
                ],
                "partitions": [
                    {
                        "name": "DimRegion-Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": f'let Source = Excel.Workbook(File.Contents("{EXCEL_SOURCE}"), null, true), Region_Sheet = Source{{[Item="DimRegion",Kind="Sheet"]}}[Data] in Region_Sheet'
                        }
                    }
                ]
            },
            {
                "name": "DimProductCategory",
                "columns": [
                    {"name": "Product_Category", "dataType": "string", "isKey": True, "sourceColumn": "Product_Category"},
                    {"name": "Division", "dataType": "string", "sourceColumn": "Division"},
                    {"name": "Category_Lead", "dataType": "string", "sourceColumn": "Category_Lead"},
                    {"name": "Target_Margin_Pct", "dataType": "double", "sourceColumn": "Target_Margin_Pct", "formatString": "0.0%"}
                ],
                "partitions": [
                    {
                        "name": "DimProductCategory-Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": f'let Source = Excel.Workbook(File.Contents("{EXCEL_SOURCE}"), null, true), Cat_Sheet = Source{{[Item="DimProductCategory",Kind="Sheet"]}}[Data] in Cat_Sheet'
                        }
                    }
                ]
            }
        ],
        "relationships": [
            {
                "name": "Fact_Date_Rel",
                "fromTable": "FactRetailPerformance",
                "fromColumn": "Date",
                "toTable": "DimDate",
                "toColumn": "Date"
            },
            {
                "name": "Fact_Region_Rel",
                "fromTable": "FactRetailPerformance",
                "fromColumn": "Region",
                "toTable": "DimRegion",
                "toColumn": "Region"
            },
            {
                "name": "Fact_Category_Rel",
                "fromTable": "FactRetailPerformance",
                "fromColumn": "Product_Category",
                "toTable": "DimProductCategory",
                "toColumn": "Product_Category"
            }
        ]
    }
}
data_model_content = json.dumps(data_model_schema, indent=2).encode('utf-16le')

# 5. Report/Layout (3 Detailed Report Pages)
report_layout = {
    "id": 0,
    "theme": "ExecutiveFinance",
    "sections": [
        {
            "id": 1,
            "name": "Section_ExecutiveSummary",
            "displayName": "Executive Summary",
            "filters": "[]",
            "ordinal": 0,
            "visualContainers": [
                {
                    "id": 101,
                    "x": 20, "y": 20, "width": 1240, "height": 60,
                    "config": json.dumps({"title": {"text": "RETAIL FP&A - EXECUTIVE PERFORMANCE DASHBOARD"}})
                },
                {
                    "id": 102,
                    "x": 20, "y": 90, "width": 230, "height": 110,
                    "config": json.dumps({"title": {"text": "Actual Revenue"}, "measure": "[Total Actual Revenue]"})
                },
                {
                    "id": 103,
                    "x": 270, "y": 90, "width": 230, "height": 110,
                    "config": json.dumps({"title": {"text": "Budget Revenue"}, "measure": "[Total Budget Revenue]"})
                },
                {
                    "id": 104,
                    "x": 520, "y": 90, "width": 230, "height": 110,
                    "config": json.dumps({"title": {"text": "Revenue Variance %"}, "measure": "[Revenue Variance %]"})
                },
                {
                    "id": 105,
                    "x": 770, "y": 90, "width": 230, "height": 110,
                    "config": json.dumps({"title": {"text": "Actual Profit"}, "measure": "[Actual Profit]"})
                },
                {
                    "id": 106,
                    "x": 1020, "y": 90, "width": 240, "height": 110,
                    "config": json.dumps({"title": {"text": "Cost Status"}, "measure": "[Cost Overrun Alert]"})
                },
                {
                    "id": 107,
                    "x": 20, "y": 220, "width": 600, "height": 260,
                    "config": json.dumps({"title": {"text": "Budget vs Actual Revenue Trend (Monthly)"}, "visualType": "clusteredColumnChart"})
                },
                {
                    "id": 108,
                    "x": 640, "y": 220, "width": 620, "height": 260,
                    "config": json.dumps({"title": {"text": "Regional Revenue & Profit Contribution"}, "visualType": "barChart"})
                },
                {
                    "id": 109,
                    "x": 20, "y": 500, "width": 1240, "height": 190,
                    "config": json.dumps({"title": {"text": "Category Revenue Achievement Matrix"}, "visualType": "matrix"})
                }
            ]
        },
        {
            "id": 2,
            "name": "Section_VarianceAnalysis",
            "displayName": "Variance Analysis",
            "filters": "[]",
            "ordinal": 1,
            "visualContainers": [
                {
                    "id": 201,
                    "x": 20, "y": 20, "width": 1240, "height": 60,
                    "config": json.dumps({"title": {"text": "BUDGET VS ACTUAL VARIANCE DECOMPOSITION & ROOT CAUSE AUDIT"}})
                },
                {
                    "id": 202,
                    "x": 20, "y": 90, "width": 600, "height": 280,
                    "config": json.dumps({"title": {"text": "Revenue Variance by Category (₹ Beat / Miss)"}, "visualType": "waterfallChart"})
                },
                {
                    "id": 203,
                    "x": 640, "y": 90, "width": 620, "height": 280,
                    "config": json.dumps({"title": {"text": "Expense Overrun by Cost Element (COGS vs Freight vs Mkt)"}, "visualType": "clusteredBarChart"})
                },
                {
                    "id": 204,
                    "x": 20, "y": 390, "width": 1240, "height": 300,
                    "config": json.dumps({"title": {"text": "Region-by-Category Financial Variance Matrix with Traffic Light Indicators"}, "visualType": "matrix"})
                }
            ]
        },
        {
            "id": 3,
            "name": "Section_ProfitabilityAnalysis",
            "displayName": "Profitability Analysis",
            "filters": "[]",
            "ordinal": 2,
            "visualContainers": [
                {
                    "id": 301,
                    "x": 20, "y": 20, "width": 1240, "height": 60,
                    "config": json.dumps({"title": {"text": "PRODUCT & REGIONAL MARGIN PROFILE & PROFIT CONTRIBUTION"}})
                },
                {
                    "id": 302,
                    "x": 20, "y": 90, "width": 400, "height": 280,
                    "config": json.dumps({"title": {"text": "Profit Contribution by Product Category"}, "visualType": "pieChart"})
                },
                {
                    "id": 303,
                    "x": 440, "y": 90, "width": 820, "height": 280,
                    "config": json.dumps({"title": {"text": "Monthly Operating Margin Trend vs Budget Benchmark"}, "visualType": "lineChart"})
                },
                {
                    "id": 304,
                    "x": 20, "y": 390, "width": 1240, "height": 300,
                    "config": json.dumps({"title": {"text": "Category-Level Profitability & ASP Performance Table"}, "visualType": "table"})
                }
            ]
        }
    ]
}
report_layout_content = json.dumps(report_layout, indent=2).encode('utf-16le')

# 6. DiagramLayout
diagram_layout = {
    "version": "1.1.0",
    "diagrams": [
        {
            "ordinal": 0,
            "scrollPosition": {"x": 0, "y": 0},
            "zoom": 100,
            "nodes": [
                {"location": {"x": 300, "y": 100}, "nodeType": "Table", "nodeId": "FactRetailPerformance"},
                {"location": {"x": 50, "y": 50}, "nodeType": "Table", "nodeId": "DimDate"},
                {"location": {"x": 50, "y": 250}, "nodeType": "Table", "nodeId": "DimRegion"},
                {"location": {"x": 550, "y": 100}, "nodeType": "Table", "nodeId": "DimProductCategory"}
            ]
        }
    ]
}
diagram_content = json.dumps(diagram_layout, indent=2).encode('utf-16le')

# Compile ZIP
with zipfile.ZipFile(PBIX_PATH, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types)
    z.writestr('Version', version_content)
    z.writestr('Settings', settings_content)
    z.writestr('DataModelSchema', data_model_content)
    z.writestr('Report/Layout', report_layout_content)
    z.writestr('DiagramLayout', diagram_content)

print(f"Power BI .pbix successfully compiled at:\n  {PBIX_PATH}")
