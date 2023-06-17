#%%
# Importar librerías
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import numpy as np

#%%
# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data
y = iris.target

#%%
# Gráfica de dispersión para visualizar las características
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y], palette="Set2")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

#%%
# Regresión Logística
logistic_regression = LogisticRegression()
logistic_regression.fit(X, y)

# Árbol de Decisión
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X, y)

# Máquina de Soporte Vectorial (SVM)
svm = SVC()
svm.fit(X, y)

# %%
# Gráfica de dispersión de la regresión logística
# Con los datos de prueba se obtienen las predicciones y se grafican
# para visualizar la frontera de decisión
import numpy as np

# Generar una cuadrícula de puntos en el espacio de características
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# %%

# Obtener las predicciones para cada punto en la cuadrícula
Z = svm.predict(np.c_[xx.ravel(), yy.ravel(),xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# %%
# Graficar la cuadrícula de puntos y la frontera de decisión
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y], palette="Set2")
plt.contourf(xx, yy, Z, alpha=0.3)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
# %%

import numpy as np

arr = Z
unique, counts = np.unique(arr, return_counts=True)
print(dict(zip(unique, counts)))
# %%
