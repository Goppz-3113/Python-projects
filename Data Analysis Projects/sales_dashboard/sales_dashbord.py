import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("sales_data.csv")    # loads dataset

print("===Sales Data Preview===")     # loads dataset
print(data.head()) # print first 5 rows

print("\n===Data Info===")            # display info summary
print(data.info())


data["Total_Sales"] = data["Quantity"] * data["Price"]
print("\n===Data with Full Sales Colomn===")
print(data[["OrderID","Product","Quantity","Price","Total_Sales"]])

sales_by_category= data.groupby("Category")["Total_Sales"].sum().reset_index()  # group rows that share the same category and add up the total sales # reset_index is used to print the output into a colomn 
print("\n===Total Sales By Category===")
print(sales_by_category)

sales_by_region= data.groupby("Region")["Total_Sales"].sum().reset_index()
print("\n===Total Sales By Region===")
print(sales_by_region)


plt.figure(figsize=(8,5))
plt.bar(sales_by_category["Category"], sales_by_category["Total_Sales"])
plt.title("Total Sales By Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")  # saves the chart image in the same folder
plt.show()


plt.figure(figsize=(8,5))
plt.bar(sales_by_region["Region"], sales_by_region["Total_Sales"])
plt.title("Total Sales By Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

sales_by_products=data.groupby("Product")["Total_Sales"].sum().reset_index()

top_products= sales_by_products.sort_values(by= "Total_Sales", ascending=False)

print("\n=== Top Products by Sales ===")
print(top_products)


plt.figure(figsize=(8,7))
plt.barh(top_products["Product"],top_products["Total_Sales"],color="lightgreen")  # barh is same as bar but in horizontal view
plt.title("Top Products by Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Products")
plt.tight_layout
plt.show()




data["Date"] = pd.to_datetime(data["Date"])      # Convert the 'Date' column from plain text (string) to proper datetime format,This allows Pandas to understand it as an actual date, not just text


data["Month"] = data["Date"].dt.month_name()    # Extract the month name (like January, February, etc.) from each date


monthly_sales = data.groupby("Month")["Total_Sales"].sum().reset_index()   # Group the data by 'Month' and calculate the total sales for each month

# Create a custom list of months in the correct chronological order, This helps fix the issue where Pandas sorts months alphabetically (April before February)
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Convert the 'Month' column into a special Categorical type
# This tells Pandas the exact order that months should appear in
# 'ordered=True' ensures sorting follows our custom order list
monthly_sales["Month"] = pd.Categorical(monthly_sales["Month"],categories=month_order,ordered=True)  


monthly_sales = monthly_sales.sort_values("Month")

print("\n=== Monthly Sales Summary ===")
print(monthly_sales)


plt.figure(figsize=(8, 5))


# Plot the monthly sales data as a line chart.(plt.plot=line chart)
plt.plot(monthly_sales["Month"], monthly_sales["Total_Sales"], marker='o', color='orange', linewidth=2)    # 'marker="o"' adds small circles on each data point.
                                                                                                           # 'linewidth=2' makes the line thicker and more readable.

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")

plt.grid(True, linestyle="--", alpha=0.6)     # Add dotted grid lines for better readability,'alpha=0.6' makes them semi-transparent.

plt.tight_layout()
plt.show()











