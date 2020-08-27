import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importing the dataset
dataset = pd.read_csv('covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
x=dataset.iloc[:, 2]


# Splitting the dataset into the Training set and Test set

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#print(X_train)
#print(X_test)

# Fitting Multiple Linear Regression to the Training set

regressor = LinearRegression(normalize=True)
regressor.fit(X,y)

for i in range(1,100):
    y_pred = regressor.predict([[1,1,i,1,1,1,1,1,1,1,1,1,1,1]])
    print(i,y_pred)
#plt.scatter(x, y)
#plt.show()