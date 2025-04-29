import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3]])
y = np.array([2,3.5, 5.5])

# Fi (letra griega) significa ajustado

model = linear_model.LinearRegression()

model.fit(x,y)

value = np.array([[2]])
value1 = np.array([[3.75]])

print(model.predict(value))

print(model.predict(value1))

print("Mean Square Error (Funcion Costo)")
print(mean_squared_error(y_true=y, y_pred=model.predict(x)))


print("R2 Score")
print(r2_score(y, model.predict(x)))