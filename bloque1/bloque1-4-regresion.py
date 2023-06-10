import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos desde el archivo Excel
data = pd.read_excel('bloque1-data-imc.xlsx')

# Regresión lineal simple: Predicción del peso en función de la estatura
X_simple = data[['Estatura']]
y_simple = data['Peso']

# Crear el modelo de regresión lineal simple
regression_simple = LinearRegression()
regression_simple.fit(X_simple, y_simple)

# Imprimir los coeficientes del modelo
print("Regresión lineal simple:")
print("Coeficiente (pendiente):", regression_simple.coef_[0])
print("Intercepto:", regression_simple.intercept_)

# Regresión lineal múltiple: Predicción del peso en función de la estatura y la edad
X_multiple = data[['Estatura', 'Edad']]
y_multiple = data['Peso']

# Crear el modelo de regresión lineal múltiple
regression_multiple = LinearRegression()
regression_multiple.fit(X_multiple, y_multiple)

# Imprimir los coeficientes del modelo
print("\nRegresión lineal múltiple:")
print("Coeficientes:", regression_multiple.coef_)
print("Intercepto:", regression_multiple.intercept_)
