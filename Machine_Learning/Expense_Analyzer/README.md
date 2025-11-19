Expense Analyzer — Personal Finance Insights + Monthly Spending Prediction

## 🔍 Overview
This project analyzes personal expenses using **Python, Pandas, Matplotlib, NumPy, and Scikit-Learn**.  
It performs data cleaning, feature extraction, statistical summaries, visualizations, and finally uses a **Linear Regression Model** to predict next month’s total spending.

This project demonstrates practical skills in:
- Data preprocessing & cleaning  
- Feature engineering (Month, Year, Week, Day)  
- Exploratory Data Analysis  
- Visualization techniques  
- Basic machine learning forecasting  
- Writing clean, structured analysis code  

---

# 🧪 Project Workflow

## ✔ 1. Data Cleaning
The raw `Date` column is converted to a datetime object using `pd.to_datetime()`, allowing extraction of:
- **Month**
- **Year**
- **Week Number**
- **Day Name**

The script ensures:
- Missing values are identified  
- Incorrect formats are corrected  
- All numerical values are ready for analysis  

---

## ✔ 2. Feature Engineering
New columns are added to make analysis easier:

| New Column | Description |
|------------|-------------|
| Month | Extracted month name |
| Year | Extracted year |
| Day | Day of the week |
| Week Number | Week of the year |
| Month_Number | Numerical month (1–12) |

These features help group expenses and detect spending patterns clearly.

---

## ✔ 3. Exploratory Data Analysis (EDA)

### 🔸 Category-wise Spending
Groups total expenses by category to determine:
- Highest spending category  
- Lowest spending category  
- Essential vs non-essential distribution  

### 🔸 Monthly Spending Trend
Aggregates monthly totals, allowing easy identification of:
- High-spend months  
- Seasonal spending behaviour  

### 🔸 Day-Wise Spending
Identifies:
- Which day of the week you spend the most  
- Weekly habits (weekend overspending, etc.)

---

## ✔ 4. Visualizations

### 📌 Category-Wise Spending (Bar Chart)
Shows how much money is spent in each category.

### 📌 Category Percentage Share (Pie Chart)
Displays how each category contributes to total spending.

### 📌 Monthly Spending Trend (Line Chart)
Plots month-over-month spending to reveal growth or decline patterns.

All charts are saved automatically as PNG files.

---

## ✔ 5. Machine Learning — Predicting Next Month Spending

### 🔍 Why Linear Regression?
Linear Regression is used because:
- It identifies trends in numerical data  
- Perfect for forecasting monthly expenses  
- Simple and interpretable  
- Requires minimal data to work  

### 🔍 How It Works
The model learns a line:
spending = m * month_number + c


Where:
- **m** = slope (how fast spending increases each month)
- **c** = intercept (base spending)

After training, the model predicts spending for:
next_month = last_month + 1


This helps in budgeting and financial planning.

---




## 📂 Data Used
A CSV file containing:
- Date  
- Category  
- Amount  

A sample dataset is uploaded.  
The complete dataset can be generated manually.

---

## 🛠 Tools & Libraries
- **Pandas** → data cleaning, grouping, feature extraction  
- **NumPy** → numerical operations  
- **Matplotlib** → 2D visualization  
- **Scikit-Learn** → machine learning (Linear Regression)  

---

## 🔍 Key Insights Expected
- Which category consumes most of the budget  
- Month-over-month spending trend  
- Weekly spending behaviour  
- Spending spikes (festivals / shopping seasons)  
- Future spending estimate  

---

## 📌 Why This Project Is Valuable
- Demonstrates **data analytics**, **visualization**, and **machine learning** skills  
- Very useful for GitHub (shows real work)  
- Interview-friendly — easy to explain and extend  
- Shows the ability to build a full data pipeline  
- Highly relevant to **Data Science**, **Business Analytics**, and **Statistical Modeling** roles  

---

 






