import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

rawdata=pd.read_csv("DailyTemperatures.csv")
X=rawdata.drop(columns=['AvgTemperature','Region','Country','City'])
y=rawdata['AvgTemperature']

model=DecisionTreeRegressor()
model.fit(X,y)
joblib.dump(model,'TemperatureMLModel.joblib')