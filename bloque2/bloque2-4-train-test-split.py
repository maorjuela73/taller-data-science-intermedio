#%%
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Cargar el conjunto de datos
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Evaluar el modelo con los datos de prueba
accuracy = model.score(X_test, y_test)
print("Exactitud del modelo:", accuracy)
