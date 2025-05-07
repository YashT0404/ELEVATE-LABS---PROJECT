
# 🦈 Shark Tank India Investment Analysis

This project provides an end-to-end exploratory analysis of startup investment patterns in the Indian version of *Shark Tank*, using Python for data cleaning and Tableau for rich interactive visualizations.

## 📁 Project Structure

```
.
├── data/
│   └── shark_tank_india_raw.csv           # Original dataset from Kaggle
│
├── notebooks/
│   └── data_cleaning.ipynb                # Python notebook for preprocessing
│
├── tableau/
│   └── Shark_Tank_India_Dashboard.twb     # Tableau Public workbook with all visualizations
│
├── output/
│   └── Shark_Tank_India_Report.pdf        # Final PDF report from Tableau
│
├── README.md                              # Project documentation
```

---

## 🧹 Step 1: Data Cleaning in Python

Using `pandas`, we handled the following preprocessing steps:

- Removed or filled **null values** in key columns (`Valuation`, `Deal Amount`, `Founders`, etc.).
- **Standardized industry names** and investor spellings.
- Extracted new columns such as:
  - `Gender Type` from founder names
  - `City` and `State` from pitch locations
- Converted data types (e.g., dates, floats, currency formatting).
- Saved the cleaned data to a new CSV for Tableau input.

Libraries used:
```python
pandas, numpy, re, matplotlib (optional for quick EDA)
```

---

## 📊 Step 2: Visualization in Tableau

### ✅ Visuals Created:
1. **Industry-wise Investment Overview**  
   → Bar chart showing total deal amount by industry.

2. **Investment Over Time**  
   → Line chart tracking number of startups and total investments by air date.

3. **Founder Gender vs Deal Success**  
   → Stacked bar chart showing deal success by gender grouping.

4. **City-Wise Deal Count**  
   → Horizontal bar chart of pitch counts per city.

5. **Investor Popularity**  
   → Bar chart displaying number of deals per shark.

6. **Valuation Requested vs Received**  
   → Scatter plot comparing valuation asked vs actual deal amount.

---

## 🖥️ Step 3: Creating a Dashboard

In Tableau Public:

- Combined all six worksheets into a **single dashboard**.
- Used **Tiled layout** for structured placement.
- Applied consistent **color schemes**, fonts, and filters.
- Exported dashboard to PDF and `.twb` format.

---

## 📄 Final Report

A PDF report summarizing key insights was generated from the dashboard visuals and exported for sharing/presentation.

---

## 📌 Tools Used

- **Python** (Pandas, Jupyter Notebooks)
- **Tableau Public**
- **Kaggle Dataset** ([Shark Tank India Dataset](https://www.kaggle.com/datasets/datadiscoveryproject/shark-tank-india-dataset))

---

## 📈 Outcomes

This project highlights:
- Investment trends by industry and geography
- Gender diversity in founder teams
- Investor behavior and deal patterns
- Gaps between requested vs received funding

---

## ✅ Future Enhancements

- Add filters (e.g., by season, investor).
- Integrate web scraping to fetch updated Shark Tank India data.
- Deploy interactive Tableau dashboard via Tableau Public or embed in a web app.

---
