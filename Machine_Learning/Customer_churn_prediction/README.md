# Customer Churn Prediction using Logistic Regression

This project predicts whether a customer is likely to **churn (leave a service)** based on their demographic information, subscription type, and service usage.  
The project uses **Python, Pandas, Seaborn, Matplotlib, and Logistic Regression** from Scikit-Learn.

---

## 🚀 Project Overview

Customer churn prediction is important for businesses to identify customers who are likely to leave, so they can take preventive actions.

This machine learning model analyzes:

- Customer demographics  
- Contract type  
- Internet service  
- Monthly charges  
- Customer support calls  

Using these features, the model predicts:

Churn = 1 → Customer is likely to leave
Churn = 0 → Customer is likely to stay


---

## 📂 Dataset Summary

The dataset contains customer records with the following important columns:

- **CustomerID**
- **Gender**
- **Age**
- **Tenure**
- **MonthlyCharges**
- **SupportCalls**
- **ContractType**
- **InternetService**
- **Churn**

After preprocessing, the dataset is transformed using:

- **Label Encoding** (Gender, Churn)
- **One-Hot Encoding** (ContractType, InternetService)

---

## 🧹 Data Preprocessing Steps

1. Loaded the dataset using Pandas  
2. Converted categorical columns to numerical values  
3. Applied one-hot encoding on multi-category features  
4. Visualized:
   - Churn distribution  
   - Gender distribution  
   - Contract type distribution  
5. Selected important numerical features for modeling  
6. Split the data into **training** and **testing** sets

---

## 🤖 Machine Learning Model

A **Logistic Regression** classifier was used because:

- The output is binary (Churn or Not Churn)
- It works well for simple classification tasks
- It is easy to interpret using feature importance

### Model Training Flow:

1. Train-test split (80% train, 20% test)  
2. Fit Logistic Regression model  
3. Predict churn on test data  
4. Evaluate performance using:  
   - Accuracy  
   - Precision  
   - Recall  
   - Confusion Matrix

---

## 📈 Model Evaluation Metrics

The model prints:

- **Accuracy** → How many predictions were correct  
- **Precision** → Out of predicted churns, how many were correct  
- **Recall** → How many actual churns were detected  
- **Confusion Matrix** → TP, TN, FP, FN count  
- **Feature Importance** → Which features impact churn the most  

---

## 📊 Visualizations

The project includes:

- Churn Count Plot  
- Gender Distribution Plot  
- Contract Type Distribution Plot  

These help understand the dataset before training the model.

---

## 🛠️ Technologies Used

| Library | Purpose |
|--------|----------|
| **Pandas** | Data loading & processing |
| **Seaborn** | Beautiful statistical visualizations |
| **Matplotlib** | Custom plotting |
| **Scikit-Learn** | Encoding, ML model, evaluation |
| **NumPy** | Numerical processing |



