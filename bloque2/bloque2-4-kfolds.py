#%%
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Cargar el conjunto de datos
iris = load_iris()
X = iris.data
y = iris.target

# Crear el modelo de regresión logística
model = LogisticRegression()

# Realizar validación cruzada k-fold con k=5
scores = cross_val_score(model, X, y, cv=5)

# Imprimir los resultados de cada fold y el promedio
print("Scores por fold:", scores)
print("Promedio de los scores:", scores.mean())

# %%
