import numpy as np

def sigmoide(x):
  s = 1 / (1 + np.exp(-x))
  return s

np.random.seed(40)
x = np.array([0.5, 1.3, -0.9])
w = np.random.rand(3) #pesos aleatorios
t = 0.65
b = 1
delta_w = np.zeros(3)
n = 0.001

for epocas in range(50):
  h = np.dot(x,w) + b
  y = sigmoide(h)

  error = -(t - y) * (y * (1 - y))
  delta_w = delta_w + error * x
  w = w + n * delta_w
  print (y)
print (w)