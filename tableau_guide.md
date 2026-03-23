# Tableau Dashboard Guide
## Global Superstore Sales Analysis

> Step-by-step instructions to build the full dashboard in Tableau Public (free).

---

## Setup

1. Download **Tableau Public** (free): https://public.tableau.com/en-us/s/download
2. Run the Python cleaning script first: `python data_cleaning.py`
3. Open Tableau Public
4. Click **Connect > Text File** and load `output/superstore_cleaned.csv`

---

## Dashboard 1: Sales Overview

### Chart 1 - KPI Summary Cards
- **Sheet name**: KPI Cards
- Drag `Sales` to Text -> right-click -> Measure -> SUM
- Duplicate for `Profit`, `Quantity`, `Order_ID` (COUNT DISTINCT)
- Use **Show Me > Text Table** layout
- Format numbers as currency

### Chart 2 - Monthly Sales Trend (Line Chart)
- **Sheet name**: Monthly Trend
- Drag `Order_Date` to Columns -> right-click -> select **Month**
- Drag `Sales` to Rows -> SUM
- Change mark type to **Line**
- Add `Profit` as a second axis (dual axis) -> right-click axis -> Synchronize Axis
- Color lines: Sales = Blue, Profit = Green

### Chart 3 - Sales by Region (Map)
- **Sheet name**: Regional Map
- Drag `Country` to the canvas -> Tableau auto-generates a map
- Drag `Sales` to **Color** (SUM)
- Drag `Profit` to **Size**
- Select color palette: **Blue-Teal**
- Add `Region` to **Label**

---

## Dashboard 2: Product & Category Analysis

### Chart 4 - Sales & Profit by Category (Bar Chart)
- **Sheet name**: Category Analysis
- Drag `Category` to Rows
- Drag `Sales` to Columns (SUM) -> Blue bars
- Drag `Profit` to Columns again -> right-click -> Dual Axis
- Change Profit to a **Line** mark
- Sort bars by Sales descending

### Chart 5 - Sub-Category Profit (Highlight Loss-makers)
- **Sheet name**: Sub-Category Profit
- Drag `Sub_Category` to Rows
- Drag `Profit` to Columns (SUM)
- Sort ascending (loss-makers on top)
- Drag `Profit` to **Color**
- Set color: Red for negative, Green for positive (diverging palette)

### Chart 6 - Top 10 Products by Profit (Horizontal Bar)
- **Sheet name**: Top Products
- Drag `Product_Name` to Rows
- Drag `Profit` to Columns (SUM)
- Right-click `Product_Name` -> Sort -> By Field -> Profit -> Descending
- Add filter: Top 10 by Profit
- Color bars green

### Chart 7 - Category Treemap
- **Sheet name**: Category Treemap
- Drag `Category` and `Sub_Category` to **Label**
- Drag `Sales` to **Size** (SUM)
- Drag `Profit` to **Color**
- Show Me -> **Treemap**
- Use diverging color (Red = Loss, Blue = Profit)

---

## Dashboard 3: Customer & Discount Analysis

### Chart 8 - Sales by Customer Segment (Pie/Donut)
- **Sheet name**: Customer Segment
- Drag `Segment` to **Color** and **Label**
- Drag `Sales` to **Angle** (SUM)
- Show Me -> **Pie Chart**
- Add % of total label

### Chart 9 - Discount vs Profit (Scatter Plot)
- **Sheet name**: Discount Impact
- Drag `Discount` to Columns (AVG)
- Drag `Profit` to Rows (SUM)
- Drag `Category` to **Color**
- Drag `Sub_Category` to **Detail**
- Add a **Trend Line**: Analytics panel -> Trend Line -> Linear
- This clearly shows how high discounts lead to losses

### Chart 10 - Yearly Sales Growth (Bar Chart)
- **Sheet name**: Yearly Growth
- Drag `Order_Year` to Columns
- Drag `Sales` to Rows (SUM)
- Drag `Profit` to Rows (SUM) -> Dual Axis
- Add `Profit_Margin_Pct` as a reference line
- Color Sales = Blue, Profit = Coral

---

## Assembling the Final Dashboard

1. Click the **New Dashboard** button (bottom tab)
2. Set size: **1200 x 800** (Desktop)
3. Drag sheets onto the dashboard canvas:
   - Top row: KPI Cards (full width)
   - Middle left: Monthly Trend | Middle right: Regional Map
   - Bottom left: Category Analysis | Bottom right: Customer Segment
4. Add **Filters** panel (Order_Year, Region, Category) as drop-downs
5. Make filters apply to all sheets: right-click filter -> Apply to Worksheets -> All
6. Add a **Title**: 'Global Superstore Sales Dashboard'
7. Add your name in a text box

---

## Publishing to Tableau Public

1. File -> Save to Tableau Public
2. Sign in with your free Tableau Public account
3. Name your workbook: 'Global Superstore Sales Analysis'
4. After publishing, copy the public URL
5. Add the Tableau Public link to your GitHub README

---

## Tips for a Professional Dashboard

- Use a consistent color palette (Blue + Coral work well)
- Add tooltips with extra info (right-click -> Edit Tooltip)
- Use calculated fields for metrics like Profit Ratio
- Add a date range filter for interactivity
- Test all filters work correctly before publishing
