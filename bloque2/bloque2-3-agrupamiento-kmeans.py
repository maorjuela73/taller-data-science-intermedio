#%%

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos de ejemplo
X, y = make_blobs(n_samples=200, centers=4, random_state=0)

# Crear el modelo de k-means
kmeans = KMeans(n_clusters=4, random_state=0)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

# Obtener las coordenadas de los centroides
centroids = kmeans.cluster_centers_

# Graficar los puntos de datos y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red', s=200)
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.title('k-means Clustering')
plt.show()

# %%
