import numpy as np
import matplotlib.pyplot as plt

y_values = []

def train():
  
    np.random.seed(40)

    x = np.array([0.5, 1.7, -0.9])
    w = np.random.rand(3)
    t = 0.65
    b = 1
    alpha = 0.01

    for epoch in range(100):
        h = np.dot(w, x) + b
        y = relu(h)

        error = t - y
        gradient = error * y * (1 - y)

        deltaW = alpha * gradient * x
        w = w + deltaW

        print(f"Epoch {epoch+1}, y = {y:.5f}")
        y_values.append(y)

    print("Final weights:")
    print(w)

    return y_values

def plot_outputs(y_vals):
    plt.plot(range(1, len(y_vals) + 1), y_vals, marker='o')
    plt.title("Entrenamiento con Relu")
    plt.xlabel("Época")
    plt.ylabel("Salida y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def escalon(x):
    if x < 0:
        return 0
    else:
        return 1
    
def relu(x):
    if x < 0:
        return 0
    else:
        return x
    
def run():
    train()
    plot_outputs(y_values)

run()