#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression

# Cargar el dataset de ejemplo de sklearn
data = load_linnerud()

# Obtener las características y la variable objetivo
X = data.data[:, np.newaxis, 0]  # Utilizamos la primera característica (Chins)
y = data.target[:, np.newaxis, 0]  # Variable objetivo (Peso)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X, y)

# Realizar predicciones
y_pred = regression.predict(X)

# Graficar los resultados
plt.scatter(X, y, color='blue', label='Valores reales')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Chins (Expectativa de vida)')
plt.ylabel('Peso')
plt.legend()
plt.show()
# %%

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_linnerud
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Cargar el dataset de ejemplo de sklearn
data = load_linnerud()

# Obtener las características y la variable objetivo
X = data.data[:, np.newaxis, 0]  # Utilizamos la primera característica (Chins)
y = data.target[:, np.newaxis, 0]  # Variable objetivo (Peso)

# Crear el objeto de transformación polinómica de grado 2
polynomial_features = PolynomialFeatures(degree=2)
X_poly = polynomial_features.fit_transform(X)

# Crear el modelo de regresión lineal
regression = LinearRegression()

#%%
# Ajustar el modelo a los datos polinómicos
regression.fit(X_poly, y)

#%%
# Realizar predicciones con los datos polinómicos
y_pred = regression.predict(X_poly)

#%%
# Ordenar los puntos para graficar la línea polinómica
sort_indices = np.argsort(X, axis=0)
X_sorted = X[sort_indices]
X_sorted_arr = np.float64([[x[0][0]] for x in X_sorted])
y_pred_sorted = y_pred[sort_indices]
y_pred_sorted_arr = np.float64([[y[0][0]] for y in y_pred_sorted])
#%%
# Graficar los resultados
plt.scatter(X, y, color='blue', label='Valores reales')
plt.plot(X_sorted_arr, y_pred_sorted_arr, color='red', linewidth=2, label='Regresión Polinómica')
plt.xlabel('Chins (Expectativa de vida)')
plt.ylabel('Peso')
plt.legend()
plt.show()

# %%
