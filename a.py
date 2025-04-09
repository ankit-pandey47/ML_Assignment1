import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#take data from the excel file
data = pd.read_csv('student_exam_data.csv')
#print(data.head())

x = data.drop("Pass/Fail", axis=1) 
y = data["Pass/Fail"]

#we have to split the data in two parts one is use for training the model and other is used for testing(for this we need to import....)

from sklearn.model_selection import train_test_split

X_train , X_test , Y_train , Y_test = train_test_split(x ,y, test_size=0.2)

#To create a model we first import LinearRegression

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train , Y_train)

print("Ankit")

from sklearn.metrics import r2_score

# Get predictions
Y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error (MSE):", mse)

from sklearn.metrics import r2_score
r2 = r2_score(Y_test, Y_pred)
print("R² Score:", r2)




