import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3]])
y = np.array([2,3.5, 5.5])

# Fi (letra griega) significa ajustado

model = linear_model.LinearRegression()

model.fit(x,y)

plt.scatter(x,y)

plt.plot(x, model.predict(x), 'r')

plt.show()