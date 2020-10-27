import pandas as pd

dataset = pd.read_csv('ML/covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X = sc.fit_transform(X)
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X, y)

def priority(breathing,pneumonia,age,pregnant,diabetes,copd,asthma,immsupr,hypertension,other,cardio,obesity,renal,smoker):
    y_pred = regressor.predict([[breathing,pneumonia,age/100,pregnant,diabetes,copd,asthma,immsupr,hypertension,other,cardio,obesity,renal,smoker]])
    return y_pred
