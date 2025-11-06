House Price Prediction using Linear Regression

## 📘 Overview
This project predicts house prices based on multiple features such as **area**, **number of bedrooms**, and **number of bathrooms** using the **Linear Regression** algorithm from Scikit-learn.

It demonstrates the complete **machine learning workflow** — from data preparation to model training, evaluation, and visualization.

---

## 🎯 Project Objectives
- Apply **supervised learning (regression)** concepts.
- Split data into **training** and **testing** sets.
- Train a **Linear Regression** model using Scikit-learn.
- Evaluate model performance using:
  - Mean Absolute Error (MAE)
  - R² Score
- Visualize **actual vs predicted** prices using Matplotlib.

---

## 🧠 Concepts Covered
- Data handling using **Pandas** and **NumPy**
- Data visualization with **Matplotlib**
- Linear Regression model theory and practice
- Model evaluation metrics
- Understanding intercepts and coefficients
- Handling small structured datasets

---

## ⚙️ Technologies Used
| Library | Purpose |
|----------|----------|
| **Pandas** | Data manipulation and cleaning |
| **NumPy** | Mathematical operations |
| **Matplotlib** | Data visualization |
| **Scikit-learn** | Machine Learning (Linear Regression) |

---

## 📊 Dataset
A small manually created dataset for demonstration purposes:

| Area (sq.ft) | Bedrooms | Bathrooms | Price |
|---------------|-----------|------------|--------|
| 1500 | 3 | 2 | 300000 |
| 1800 | 4 | 3 | 400000 |
| 2400 | 3 | 2 | 500000 |
| ... | ... | ... | ... |

> In real-world projects, you can replace this with a larger dataset (like Kaggle housing data).

---

## 🧩 How the Model Works
The Linear Regression algorithm fits an equation of the form:

\[
\text{Price} = b_0 + b_1(\text{Area}) + b_2(\text{Bedrooms}) + b_3(\text{Bathrooms})
\]

Where:
- \( b_0 \) = Intercept (base price)
- \( b_1, b_2, b_3 \) = Coefficients showing each feature's influence

---

## 📈 Sample Results
Example model output:

Intercept (Base Price): -31772.160018243943 

Coefficients: [ 190.47316993  24606.15498649 -28581.38109458 ]

Mean Absolute Error (MAE): 23902.74

R² Score: 0.97


📉 **Actual vs Predicted Prices**

The blue dots show predictions, and the red line represents perfect predictions (y = x).  
Closer dots to the line mean better accuracy.

The plot chart is uploaded in the same folder

---

## 🧮 Key Learnings
- Meaning of **intercept** and **coefficients**
- Why feature scaling is important
- What multicollinearity means (when features behave similarly)
- Understanding the difference between **Pandas Series** and **NumPy arrays**
- Importance of train/test splitting for fair evaluation

---

## 🚀 How to Run
1. Clone this repository or copy the script.
2. Make sure Python is installed (version 3.8+).
3. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn matplotlib



