import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./brain_body.txt", delim_whitespace=True)

x = df[['Body']]
y = df['Brain']

# Fi (letra griega) significa ajustado

model = linear_model.LinearRegression()

model.fit(x,y)

## Graficar la predicción

# plt.scatter(x,y)

# plt.plot(x, model.predict(x), 'r')

# plt.show()

## Calcular prediccion a partir de un valor

print(model.predict([[175]]))