#%%
# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
#%%

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

#%%
# Load the California Housing dataset
california = fetch_california_housing()

# Extract the features and the target variable
X = california.data  # Features
y = california.target  # Target variable

#%%
# Select a single feature (e.g., average number of rooms)
feature_index = 5
X_single = X[:, feature_index].reshape(-1, 1)

# Create the linear regression model
regression = LinearRegression()

# Fit the model to the data
regression.fit(X_single, y)

# Make predictions
y_pred = regression.predict(X_single)
#%%
# Plot the results
plt.scatter(X_single, y, color='blue', label='Actual Values')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Median House Value')
plt.legend()
plt.show()
#%%
# Plot the results using plotly (interactive) 
import plotly.express as px
fig = px.scatter(x=X_single[:, 0], y=y, color=y_pred)
fig.show()

#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Cargar el conjunto de datos de viviendas de California
california = fetch_california_housing()

# Extraer las características y la variable objetivo
X = california.data  # Características
y = california.target  # Variable objetivo

# Seleccionar una variable más lineal (e.g., ingreso medio)
feature_index = 0
X_single = X[:, feature_index].reshape(-1, 1)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X_single, y)

# Realizar predicciones
y_pred = regression.predict(X_single)

# Graficar los resultados
plt.scatter(X_single, y, color='blue', label='Valores reales')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.xlabel('Ingreso Medio')
plt.ylabel('Valor Medio de la Vivienda')
plt.legend()
plt.show()

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Cargar el dataset California Housing
california = fetch_california_housing()

# Obtener las características y la variable de salida
X = california.data  # Características
y = california.target  # Variable de salida

# Seleccionar una variable con relación más lineal (población media)
feature_index = 3
X_single = X[:, feature_index].reshape(-1, 1)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X_single, y)

# Realizar predicciones
y_pred = regression.predict(X_single)

# Graficar los resultados
plt.scatter(X_single, y, color='blue', label='Valores reales')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Población Media')
plt.ylabel('Valor Mediano de la Vivienda')
plt.legend()
plt.show()

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Cargar el dataset de California Housing
california = fetch_california_housing()

# Obtener las características y la variable de salida
X = california.data  # Características
y = california.target  # Variable de salida

# Seleccionar una variable lineal (AveBedrms)
feature_index = 3
X_single = X[:, feature_index].reshape(-1, 1)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X_single, y)

# Realizar predicciones
y_pred = regression.predict(X_single)

# Graficar los resultados
plt.scatter(X_single, y, color='blue', label='Valores reales')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.xlabel('AveBedrms')
plt.ylabel('Precio Mediano de la Vivienda')
plt.legend()
plt.show()

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Cargar el dataset California Housing
california = fetch_california_housing()

# Obtener las características y la variable objetivo
X = california.data  # Características
y = california.target  # Variable objetivo

# Seleccionar una variable diferente (e.g., variable 1: latitud)
feature_index = 1
X_single = X[:, feature_index].reshape(-1, 1)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X_single, y)

# Realizar predicciones
y_pred = regression.predict(X_single)

# Graficar los resultados
plt.scatter(X_single, y, color='blue', label='Valores reales')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Latitud')
plt.ylabel('Valor Mediano de las Viviendas')
plt.legend()
plt.show()

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Cargar el dataset California Housing
california = fetch_california_housing()

# Obtener las características y la variable objetivo
X = california.data  # Características
y = california.target  # Variable objetivo

# Seleccionar una variable diferente (e.g., la variable 2: average number of bedrooms)
feature_index = 2
X_single = X[:, feature_index].reshape(-1, 1)

# Crear el modelo de regresión lineal
regression = LinearRegression()

# Ajustar el modelo a los datos
regression.fit(X_single, y)

# Realizar predicciones
y_pred = regression.predict(X_single)

# Graficar los resultados
plt.scatter(X_single, y, color='blue', label='Valores reales')
plt.plot(X_single, y_pred, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Número promedio de dormitorios')
plt.ylabel('Valor Mediano de las Viviendas')
plt.legend()
plt.show()

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Cargar el dataset California Housing
california = fetch_california_housing()

# Crear un DataFrame a partir de las características
df = pd.DataFrame(california.data, columns=california.feature_names)

# Agregar la variable objetivo al DataFrame
df['MedianHouseValue'] = california.target

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Crear un mapa de calor del correlograma
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlograma - California Housing')
plt.show()

# %%
