import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\Admin\Desktop\mygame\customer_churn_dummy.csv")

print("=== First five rows of the data ===")
print(data.head())

print("\n=== Data Info ===")
print(data.info())

data["Churn"] = data["Churn"].map({"Yes": 1, "No": 0})
data["Gender"] = data["Gender"].map({"Male": 1, "Female": 0})

plt.figure(figsize=(8,5))
sns.countplot(x="Churn", data=data)
plt.title("Churn Count (0 = No, 1 = Yes)")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=data)
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="ContractType", data=data)
plt.title("Contract Type Distribution")
plt.show()

data = pd.get_dummies(data, columns=["ContractType", "InternetService"], drop_first=True)

print("\n=== Data after encoding ===")
print(data.head())

from sklearn.model_selection import train_test_split

X = data[[
    "Gender",
    "MonthlyCharges",
    "ContractType_One year",
    "ContractType_Two year",
    "InternetService_Fiber Optic"
]]


Y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

importance = model.coef_[0]
feature_names = X.columns

print("\n=== Feature Importance ===")
for name, score in zip(feature_names, importance):
    print(name, "→", score)
