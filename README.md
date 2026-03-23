# Global Superstore Sales Analysis

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Tableau](https://img.shields.io/badge/Tableau-Public-orange?logo=tableau)
![Pandas](https://img.shields.io/badge/Pandas-2.1-green?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **Financial Data Analysis of Global Superstore Sales** using Python for data cleaning & EDA, and Tableau Public for interactive dashboards.

---

## Overview

This project performs an end-to-end data analysis on the Global Superstore dataset — a real-world retail dataset covering 51,000+ orders across 7 global markets from 2011-2014. The goal is to uncover actionable business insights about sales performance, profitability, discount impact, and regional trends.

---

## Key Business Questions Answered

- Which regions and countries drive the most revenue?
- Which product categories and sub-categories are most/least profitable?
- How do discounts affect profit margins?
- What is the monthly/yearly sales trend?
- Which customer segments generate the most sales?
- Which products are loss-makers and why?

---

## Dashboard Previews

| Dashboard | Description |
|-----------|-------------|
| Sales Overview | KPI cards, Monthly trend, Regional map |
| Product Analysis | Category bars, Sub-category profit, Top 10 products, Treemap |
| Customer & Discount | Segment pie, Discount vs Profit scatter, Yearly growth |

> After building in Tableau Public, add your dashboard link here:
> **Tableau Public Link**: [Add your link after publishing]

---

## Project Structure

```
global-superstore-sales-analysis/
|
|-- data_cleaning.py       # Python: data cleaning, EDA, export for Tableau
|-- tableau_guide.md       # Step-by-step Tableau dashboard building guide
|-- requirements.txt       # Python dependencies
|-- .gitignore
|
|-- data/
|   |-- README.md          # Instructions to download dataset from Kaggle
|   `-- Global_Superstore.csv  # Download from Kaggle (NOT in git)
|
|-- output/                # Auto-created by data_cleaning.py
|   `-- superstore_cleaned.csv  # Load this into Tableau
|
`-- plots/                 # Auto-created EDA charts
    |-- sales_by_region.png
    |-- monthly_sales_trend.png
    |-- sales_profit_by_category.png
    |-- profit_by_subcategory.png
    |-- top10_products_profit.png
    |-- sales_by_segment.png
    `-- discount_vs_profit.png
```

---

## Quick Start

### Step 1 - Clone & Install
```bash
git clone https://github.com/charish1307/global-superstore-sales-analysis.git
cd global-superstore-sales-analysis
pip install -r requirements.txt
```

### Step 2 - Download Dataset
```bash
# Kaggle API
pip install kaggle
kaggle datasets download -d apoorvaappz/global-super-store-dataset -p data/ --unzip
```
Or manually download from: https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset

### Step 3 - Run Data Cleaning & EDA
```bash
python data_cleaning.py
```
This generates:
- `output/superstore_cleaned.csv` (load into Tableau)
- `plots/` folder with 7 EDA charts

### Step 4 - Build Tableau Dashboard
- Download Tableau Public (free): https://public.tableau.com/en-us/s/download
- Load `output/superstore_cleaned.csv`
- Follow `tableau_guide.md` step-by-step to build all 10 charts across 3 dashboards

---

## Dataset

| Property | Value |
|----------|-------|
| Source | Kaggle - Global Super Store Dataset |
| Rows | ~51,000 orders |
| Columns | 24 features |
| Time Period | 2011 - 2014 |
| Markets | 7 (Africa, APAC, Canada, EMEA, EU, LATAM, US) |
| Categories | Furniture, Office Supplies, Technology |

---

## Python EDA Charts Generated

- Sales by Region (bar chart)
- Sales & Profit by Category (grouped bar)
- Monthly Sales Trend (line chart with fill)
- Top 10 Products by Profit (horizontal bar)
- Profit by Sub-Category with loss highlighting (red/blue)
- Sales by Customer Segment (pie chart)
- Discount vs Profit relationship (scatter plot)

---

## Tableau Dashboard Charts

- KPI Summary Cards (Total Sales, Profit, Orders, Avg Margin)
- Monthly Sales & Profit Trend (dual-axis line)
- Sales by Country/Region (filled map)
- Sales & Profit by Category (dual-axis bar + line)
- Sub-Category Profit with diverging color (red = loss)
- Top 10 Products by Profit (sorted bar)
- Category/Sub-Category Treemap
- Customer Segment Pie Chart
- Discount vs Profit Scatter with trend line
- Yearly Sales Growth (bar chart)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9+ | Data cleaning & EDA |
| Pandas | Data manipulation |
| Matplotlib & Seaborn | Python visualizations |
| Tableau Public | Interactive dashboards |
| Kaggle | Dataset source |

---

## Author

**Charish Yadavali**
- GitHub: [@charish1307](https://github.com/charish1307)
- LinkedIn: [linkedin.com/in/charishyadavali](https://www.linkedin.com/in/charishyadavali)

---

## License

This project is licensed under the MIT License.

---

## If you found this useful, please star the repo!
