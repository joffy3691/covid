import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn import tree
regressor = tree.DecisionTreeRegressor()
regressor.fit(X, y)

for i in range(1,100):
    X_test = sc.transform([[0,0,i/100,0,0,0,0,0,0,0,0,0,0,0]])
    y_pred = regressor.predict(X_test)
    plt.plot(i,y_pred,'ro')
    print(i,y_pred)
plt.show()