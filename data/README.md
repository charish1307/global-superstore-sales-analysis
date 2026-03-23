# Data Folder

> The dataset is NOT included in this repo. Download it from Kaggle (free account required).

---

## How to Download

### Option 1 - Manual
1. Go to: https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset
2. Click Download
3. Unzip and place `Global_Superstore.csv` in this `data/` folder

### Option 2 - Kaggle API
```bash
pip install kaggle
kaggle datasets download -d apoorvaappz/global-super-store-dataset -p data/ --unzip
```

---

## Dataset Details

| Property | Value |
|----------|-------|
| File | `Global_Superstore.csv` |
| Rows | ~51,000 orders |
| Columns | 24 (Order ID, Date, Region, Category, Sales, Profit, etc.) |
| Years | 2011 - 2014 |
| Markets | 7 global regions |
| License | Free for educational use |

---

## Expected Folder Structure

```
data/
├── README.md             <- This file
└── Global_Superstore.csv <- Download from Kaggle
```
