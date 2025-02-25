import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#take data from the excel file
data = pd.read_csv('linear_regression_dataset.csv')
#print(data.head())

#we have to split the data in two parts one is use for training the model and other is used for testing(for this we need to import....)

from sklearn.model_selection import train_test_split

X_train , X_test , Y_train , Y_test = train_test_split(data[['Feature']] , data[['Target']] , test_size=0.2)

#To create a model we first import LinearRegression

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train , Y_train)


#now we have trained the model , now we check the value of y by giving the value X of test data

Y_pred = model.predict([[0.654]])
print(Y_pred)




# Scatter() This function is used to create a scatter plot, which displays individual data points as dots on a 2D grid.
# plot() This function is used to create a line plot, which connects a series of data points with lines. It's typically used to show the relationship between two variables.

#plotting the training data
plt.figure(figsize=(10,6))
plt.scatter(X_train , Y_train , color="blue" , label="Training Data")
plt.plot(X_train , model.predict(X_train) , color="red" ,linewidth=2)
plt.title("Linear Regression - Training data")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.show()





#plotting the testing data
plt.figure(figsize=(10,6))
plt.scatter(X_test , Y_test , color="blue" , label="Training Data")
plt.plot(X_test , model.predict(X_test) , color="red" ,linewidth=2)
plt.title("Linear Regression - Testing data")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.show()