
import pandas as pd

from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('ML/covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
x=dataset.iloc[:, 2]

regressor = LinearRegression(normalize=True)
regressor.fit(X,y)


