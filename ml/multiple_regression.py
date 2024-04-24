import pandas as pd
from sklearn import linear_model

df = pd.read_csv("./ml/data.csv")

x = df[["Weight", "Volume"]]
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(x, y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm³:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
print(regr.coef_)
