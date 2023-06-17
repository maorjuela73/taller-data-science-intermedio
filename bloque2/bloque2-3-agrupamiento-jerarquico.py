#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from scipy.cluster.hierarchy import dendrogram, linkage

# Generar datos de ejemplo
X, y = make_moons(n_samples=200, noise=0.05)

# Realizar el clustering jerárquico
linkage_matrix = linkage(X, method='ward')

# Graficar el dendrograma
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix)
plt.xlabel('Índice de muestra')
plt.ylabel('Distancia')
plt.title('Dendrograma - Clustering Jerárquico')
plt.show()

# %%
