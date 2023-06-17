#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

#%%
# Cargar el conjunto de datos de cáncer de mama
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

#%%
# Crear un DataFrame con los datos
df = pd.DataFrame(X, columns=cancer.feature_names)
df['target'] = cancer.target

#%%
# Gráficas de cajas para visualizar características por tipo de cáncer de mama
sns.boxplot(x="target", y="mean radius", data=df,palette="Set2")

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
