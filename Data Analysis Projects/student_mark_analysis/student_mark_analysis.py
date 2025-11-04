#Student_Mark_Analysis Using Pandas and Matplotlib

import pandas as pd                 # Pandas is used to handle data tables
import matplotlib.pyplot as plt      # It hepls create charts and graphs

data=pd.read_csv("student_marks.csv")
print("Student's Marks Data")
print(data)

print("\n Basic Info: ")    # data.info() shows colomn name, data-types, total rows
print(data.info())

print("\n Summary Statistics")    # data.describe() shows mathematical summary of all number colomns
print(data.describe())

print("\n Average Mark For Each Subjects")
print(data[["Math","Science","English"]].mean())   # select multiple colomns and calculate the mean

data["Total"]= data["Math"]  + data["Science"] + data["English"]  #data["Total"] adds a new colomn
data["Average"] = data["Total"] / 3

print('\n Student Totals And Average: ')
print(data[["Name","Total","Average"]])

top_student= data.loc[data["Average"].idxmax()]   # data.loc[] fetches the full row and data["Average"].idxmax() finds the row index where the average is maximum 
print("\n Top Scorer: ")
print(top_student)

sorted_data = data.sort_values(by="Average", ascending=False)   # sorts.values() sorts the data based on a specific column   # here ascending = false means highest to lowest (simply means in descending order)
print("\n🔢 Students Ranked by Average:")
print(sorted_data[["Name", "Average"]])

plt.figure(figsize=(8, 5))         # set chart size (the size of the figure window)
plt.bar(sorted_data["Name"], sorted_data["Average"], color="skyblue")   #creates a bar chart  plt.bar(X,Y)
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)  # rotates the x labels for readabilty
plt.tight_layout()    # this command adjusts spacing automatically
plt.show()  #displays the chart







