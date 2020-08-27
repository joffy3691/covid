import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
from sklearn.preprocessing import StandardScaler
xyz = 3

sc = StandardScaler()
X = sc.fit_transform(X)
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X, y)

for i in range(1,100):
    X_test = sc.transform([[1,0,i/100,1,0,1,0,1,0,1,0,1,0,1]])
    y_pred = regressor.predict(X_test)
    print(y_pred,i)
    plt.plot(i,y_pred,'ro')
plt.show()