import pandas as pd                                          # to handle tabular data
import matplotlib.pyplot as plt                              # for creating charts and visualization
import numpy as np                                           # for mathematical operations
from sklearn.model_selection import train_test_split         # it splits the data for training and testing
from sklearn.linear_model import LinearRegression            # used for making prediction
from sklearn.metrics import mean_absolute_error, r2_score    # to check the model's accuracy

data = {
    "Area": [1500, 1800, 2400, 3000, 3500, 4000, 1200, 2200, 2800, 3200],      # random data as a dictionary
    "Bedrooms": [3, 4, 3, 5, 4, 5, 2, 3, 4, 5],                               # we can also work on csv file by using the pd.read_csv() command
    "Bathrooms": [2, 3, 2, 4, 3, 4, 1, 2, 3, 4],                              
    "Price": [300000, 400000, 500000, 600000, 650000, 700000, 200000, 450000, 550000, 620000] 
}

df=pd.DataFrame(data)    # converts the dictionary "data" into a data frame i.e a spreadsheet

print("Sample House Data")
print(df.head())         # prints the first 5 rows of the data frame

x = df[["Area","Bedrooms","Bathrooms"]]    # values used to make prediction
y= df["Price"]                                 # values that we are trying to predict


# SPLITING THE DATA FOR TESTING AND TRAINING                                           # train_test_split randomly splits the data into two parts
                                                                                       # test_size=0.3 means 70% data tor training and 30% for testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=42)   # random_state with a random number ensure same split everytime

print("\n Data Split Completed")
print(f"\n Training samples: {len(x_train)}")
print(f"\n Teasting samples: {len(x_test)}")

model = LinearRegression()   #creating an instance for easy access

model.fit(x_train,y_train)  # this model will find the best fit line between x and y

print("\n Model Training Completed")

y_pred= model.predict(x_test)

print("\n Predicted Prices:")
print(y_pred)

comparison = pd.DataFrame( { " Actual Price": y_test.values, "Predicted Values": y_pred})

print("\n Actual vs Predicted Price Comparison:")
print(comparison)

mae = mean_absolute_error(y_test,y_pred)  # it show sthe average diff between actual and predicted prices

r2 = r2_score(y_test,y_pred)  # checks the smartness of the model by checking the price variation ( 1= perfect model)

print(f"\n Mean Absolute Error (MAE): {mae:.2f}")
print(f" R² Score: {r2:.2f}")


plt.figure(figsize=(7, 5))   
plt.scatter(y_test, y_pred, color="blue", label="Predicted vs Actual")   # Create a scatter plot chart


plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red", linewidth=2, label="Perfect Prediction")  # adds a red line for the perfect predictions


plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.legend()     # Add legend to explain chart elements
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


print("\n📘 Model Details:")
print("Intercept (Base Price):", model.intercept_)      # The constant (b₀)
print("Coefficients:", model.coef_)                     # Weight of each feature (b₁, b₂, b₃)


# Higher coefficients mean stronger influence on price.
# Example: If area coefficient = 100, then each additional sq.ft adds ₹100 to price.
