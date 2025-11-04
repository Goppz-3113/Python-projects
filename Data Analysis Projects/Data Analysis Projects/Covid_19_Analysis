#covid_19_data-analysis
import pandas as pd  #pandas help handle data in table format
import matplotlib.pyplot as plt  # helps in creating graphs

data = pd.read_csv("compact.csv")  #.read_csv reads a csv file

print("The first 5 rows of the dataset: ")
print(data.head())  #.heads shows the first 5 rows 

print("\nDataset Info:")
print(data.info())

print("\nMissing Values: ")
print(data.isnull().sum())

print("\nSummary Statistics: ")
print(data .describe())

cases_by_country= data.groupby("country")["total_cases"].sum().sort_values(ascending=False)
print("\nTop 5 countries by total confirmed cases: ")
print(cases_by_country.head())

cases_by_country.head(10).plot(kind="bar")
plt.title("Top 10 countries with highest number of cases")
plt.xlabel("country")
plt.ylabel("Total Cases")
plt.show()









