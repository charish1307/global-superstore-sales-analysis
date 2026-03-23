# =============================================================
# Global Superstore Sales Analysis - Data Cleaning & EDA
# Author: Charish Yadavali
# Dataset: Global Superstore (Kaggle)
# Visualization: Tableau Public
# =============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
import sys
warnings.filterwarnings('ignore')


def load_data(filepath='data/Global_Superstore.csv'):
    if not os.path.exists(filepath):
        print('ERROR: Dataset file not found!')
        print('Download from: https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset')
        print('See data/README.md for full instructions.')
        sys.exit(1)
    print('Loading data...')
    for enc in ['utf-8', 'latin-1', 'cp1252']:
        try:
            df = pd.read_csv(filepath, encoding=enc)
            print(f'Loaded with encoding: {enc}')
            break
        except UnicodeDecodeError:
            continue
    print(f'Shape: {df.shape}')
    return df


def clean_data(df):
    print('\n=== Data Cleaning ===')
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_')
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) > 0:
        print(f'Missing values:\n{missing}')
        df.dropna(subset=['Sales', 'Profit', 'Order_Date'], inplace=True)
    dupes = df.duplicated().sum()
    if dupes > 0:
        df.drop_duplicates(inplace=True)
        print(f'Removed {dupes} duplicates.')
    date_cols = [c for c in df.columns if 'Date' in c or 'date' in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
    if 'Order_Date' in df.columns:
        df['Order_Year']    = df['Order_Date'].dt.year
        df['Order_Month']   = df['Order_Date'].dt.month
        df['Order_Quarter'] = df['Order_Date'].dt.quarter
        df['Month_Name']    = df['Order_Date'].dt.strftime('%b')
    for col in ['Sales', 'Profit', 'Discount', 'Quantity']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    if 'Sales' in df.columns and 'Profit' in df.columns:
        df['Profit_Margin_Pct'] = (df['Profit'] / df['Sales'].replace(0, np.nan) * 100).round(2)
    print(f'Cleaned shape: {df.shape}')
    return df


def perform_eda(df):
    print('\n=== EDA ===')
    os.makedirs('plots', exist_ok=True)
    total_sales  = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['Order_ID'].nunique() if 'Order_ID' in df.columns else len(df)
    print(f'Total Sales   : ${total_sales:,.2f}')
    print(f'Total Profit  : ${total_profit:,.2f}')
    print(f'Total Orders  : {total_orders:,}')
    if 'Region' in df.columns:
        region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        region_sales.plot(kind='bar', color='steelblue', edgecolor='white')
        plt.title('Total Sales by Region', fontsize=14, fontweight='bold')
        plt.xlabel('Region')
        plt.ylabel('Total Sales ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('plots/sales_by_region.png', dpi=150)
        plt.close()
    if 'Category' in df.columns:
        cat_data = df.groupby('Category')[['Sales', 'Profit']].sum()
        cat_data.plot(kind='bar', figsize=(8, 5), color=['steelblue', 'coral'], edgecolor='white')
        plt.title('Sales & Profit by Category', fontsize=14, fontweight='bold')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('plots/sales_profit_by_category.png', dpi=150)
        plt.close()
    if 'Order_Year' in df.columns and 'Order_Month' in df.columns:
        monthly = df.groupby(['Order_Year', 'Order_Month'])['Sales'].sum().reset_index()
        monthly['Date'] = pd.to_datetime(monthly[['Order_Year', 'Order_Month']].assign(day=1))
        plt.figure(figsize=(14, 5))
        plt.plot(monthly['Date'], monthly['Sales'], color='steelblue', linewidth=2, marker='o', markersize=3)
        plt.fill_between(monthly['Date'], monthly['Sales'], alpha=0.15, color='steelblue')
        plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Sales ($)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig('plots/monthly_sales_trend.png', dpi=150)
        plt.close()
    if 'Product_Name' in df.columns:
        top_products = df.groupby('Product_Name')['Profit'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(10, 6))
        top_products.plot(kind='barh', color='mediumseagreen', edgecolor='white')
        plt.title('Top 10 Products by Profit', fontsize=14, fontweight='bold')
        plt.xlabel('Total Profit ($)')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig('plots/top10_products_profit.png', dpi=150)
        plt.close()
    if 'Sub_Category' in df.columns:
        subcat = df.groupby('Sub_Category')['Profit'].sum().sort_values()
        colors = ['crimson' if x < 0 else 'steelblue' for x in subcat]
        plt.figure(figsize=(10, 6))
        subcat.plot(kind='barh', color=colors, edgecolor='white')
        plt.title('Profit by Sub-Category (Red = Loss)', fontsize=14, fontweight='bold')
        plt.xlabel('Total Profit ($)')
        plt.tight_layout()
        plt.savefig('plots/profit_by_subcategory.png', dpi=150)
        plt.close()
    if 'Segment' in df.columns:
        seg = df.groupby('Segment')['Sales'].sum()
        plt.figure(figsize=(6, 6))
        plt.pie(seg, labels=seg.index, autopct='%1.1f%%',
                colors=['#4C72B0', '#DD8452', '#55A868'], startangle=90)
        plt.title('Sales by Customer Segment', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('plots/sales_by_segment.png', dpi=150)
        plt.close()
    if 'Discount' in df.columns:
        sample = df.sample(min(5000, len(df)), random_state=42)
        plt.figure(figsize=(8, 5))
        plt.scatter(sample['Discount'], sample['Profit'], alpha=0.3, color='steelblue', s=10)
        plt.axhline(0, color='red', linestyle='--', linewidth=1)
        plt.title('Discount vs Profit', fontsize=14, fontweight='bold')
        plt.xlabel('Discount')
        plt.ylabel('Profit ($)')
        plt.tight_layout()
        plt.savefig('plots/discount_vs_profit.png', dpi=150)
        plt.close()
    print('All EDA plots saved to plots/ folder.')


def export_for_tableau(df):
    print('\n=== Exporting Clean Data for Tableau ===')
    os.makedirs('output', exist_ok=True)
    output_path = 'output/superstore_cleaned.csv'
    df.to_csv(output_path, index=False)
    print(f'Clean data saved to: {output_path}')
    print(f'Rows: {len(df):,} | Columns: {len(df.columns)}')
    print('Load this file into Tableau Public to build your dashboards!')


if __name__ == '__main__':
    df = load_data('data/Global_Superstore.csv')
    df = clean_data(df)
    perform_eda(df)
    export_for_tableau(df)
    print('\nPipeline complete! Now open Tableau and load output/superstore_cleaned.csv')
    print('Follow tableau_guide.md to build your dashboards.')
