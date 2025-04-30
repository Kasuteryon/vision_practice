import numpy as np
import matplotlib.pyplot as plt
# Librerias para RNA
from keras import backend
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import split_dataset

df = pd.read_csv("./brain_body.txt", delim_whitespace=True)

x = df[['Body']]
y = df['Brain']

# Crea un tf.data.Dataset
ds = tf.data.Dataset.from_tensor_slices((x, y))

# “Parte” el dataset en 80% / 20%
train_ds, val_ds = split_dataset(ds, 0.8, 0.2)

# Limpiar sesion
backend.clear_session()

# Crea un modelo
model = Sequential()

# Modelo.add(Dense(x,...)) dense es una capa y el primer parametro es la cantidad de neuronas que tiene
# (1, ) queda vacio porque solo tomo el primer valor de la tupla, tengo entendido que al ser arreglo de arreglos, solo esperas el primer valor?
model.add(Dense(1, use_bias=True, activation='linear', input_shape=(1,)))

# Optimizador (para minimizar o maximizar una variable)
adam = optimizers.Adam(learning_rate=0.01, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

# Descenso de gradiente, por medio de mean_squared_error, asignacion de pesos sinapticos
# Loss seria funcion costo para minimizar
# Accuracy es la metrica de evaluacion
model.compile(loss='mean_squared_error', optimizer=adam, metrics=['mean_absolute_error'])

# Verbose = Descriptor, verbose=0 es ningun descriptor
# En modelo.fit(x,y, epoch= ....) se utiliza el 80% de los datos y con el 20% se valida
model.fit(train_ds, epochs=200, verbose=0, validation_data=val_ds)

# Indica las capas del modelo
model.summary()

score = model.evaluate(x, y, verbose=0)

print('Loss y metric (Score):', score)

# En una recta tenemos y=mx + b
# Kernel es la pendiente (m) coeficiente de recta de regresion
# Bias seria b 
# Pesos: índice 0 = kernel, índice 1 = bias
kernel, bias = model.get_weights()
print('Kernel:', kernel)
print('Bias:', bias)

# print('Predicción para x=7:', model.predict(np.array([[7]])))