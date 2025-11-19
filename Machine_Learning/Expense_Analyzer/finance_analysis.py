import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_csv(r"C:\Users\Admin\Desktop\mygame\expenses.csv")   # read csv file
print("First five rows of the data:")
print(data.head())  # prints the five five rows

print("Missing values in each rows:")
print(data.isnull().sum())   # checks for any empty values in any colomns

data["Date"] = pd.to_datetime(data["Date"])   # converts date colomn into actual date format

data["Category"] =data["Category"].replace({"Transportation": "Transport"})     # fixing spelling mistakes in category

print("\n Data after cleaning:")
print(data.info())

data["Month"]= data["Date"].dt.month_name()   # extract month name
data["Year"]= data["Date"].dt.year            # extract year
data["Month numbers"]= data["Date"].dt.month  # extract month number
data["Week numbers"]= data["Date"].dt.isocalendar().week  
data["Day"]= data["Date"].dt.day_name()

print("\n Data after adding Month, Year, Week, Day columns:")
print(data.head())

print("\n===Spending Analysis===")

total_spent = data["Amount"].sum()                # total spending
print(f"\n Total Money Spent: {total_spent}")

spend_by_category= data.groupby("Category")["Amount"].sum()   # spending by category
print("\n Spending by category")
print(spend_by_category)

max_category= spend_by_category.idxmax()     # most expensive category
max_value= spend_by_category.max()
print(f"\n Highest Spending Category: {max_category} (₹{max_value})")

spending_by_month= data.groupby("Month")["Amount"].sum()  #spending per month
print("\n Spending by month")
print(spending_by_month)

spending_by_day= data.groupby("Day")["Amount"].sum()  #spending per day
print("\n Spending by day")
print(spending_by_day)

avg_daily= data["Amount"].mean()   # average daily spending
print(f"\n Average amount spend per transaction: {avg_daily:.2f}")

#===BAR CHART FOR SPENDING BY CATEGORY===

plt.figure(figsize=(8,5))
plt.bar(spend_by_category.index, spend_by_category.values)
plt.title("Total Spending By Category")
plt.xlabel("Category")
plt.ylabel("Amount(₹)")
plt.xticks(rotation=45)  # roatates names for readability
plt.tight_layout()          # avoid intersecting
plt.show()


#===LINE CHART FOR MONTHLY SPENDING====

sorted_months=data.groupby("Month numbers")["Amount"].sum()
plt.figure(figsize=(8,5))
plt.plot(sorted_months.index,sorted_months.values, marker="o")
plt.title("Monthle spending trend")
plt.xlabel("Month number")
plt.ylabel("Amount")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#===PIE CHART FOR CATEGORY SPENDING SHARE===

colorss = ["#F73737", "#66B2FF", "#99FF99", "#FFCC99", "#C299FF"]

plt.figure(figsize=(8,5))
plt.pie(
        spend_by_category.values, 
        labels=spend_by_category.index,
        autopct="%1.1f%%",  # show percentage
        startangle=90,       # rotate start point
        colors=colorss
        )
plt.title("Spending Share by Category")
plt.show()

#===Expense prediction===

from sklearn.linear_model import LinearRegression

monthly= data.groupby("Month numbers")["Amount"].sum().reset_index()
X= monthly["Month numbers"].values.reshape(-1,1)
Y=monthly["Amount"].values

model=LinearRegression()
model.fit(X,Y)

next_month= np.array([[monthly["Month numbers"].max()+1]])
predicted_amount=model.predict(next_month)[0]

print("\n Predicted Spending for Next Month:")
print(f"Estimated Expense: ₹{predicted_amount:.2f}")
