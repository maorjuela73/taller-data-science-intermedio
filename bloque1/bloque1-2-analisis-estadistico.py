import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lectura de la tabla desde el archivo Excel
datos = pd.read_excel('archivo.xlsx')

# Cálculo de la media de la columna 'Edad'
media_edad = datos['Edad'].mean()

# Cálculo de la mediana de la columna 'Edad'
mediana_edad = datos['Edad'].median()

# Cálculo de la moda de la columna 'Ciudad'
moda_ciudad = datos['Ciudad'].mode()

# Cálculo de la varianza de la columna 'Edad'
varianza_edad = datos['Edad'].var()

# Cálculo de la desviación estándar de la columna 'Edad'
desviacion_estandar_edad = datos['Edad'].std()

# Cálculo del rango intercuartílico de la columna 'Edad'
rango_intercuartilico_edad = datos['Edad'].quantile(0.75) - datos['Edad'].quantile(0.25)

# Impresión de los resultados
print("Medidas de Tendencia Central:")
print("Media de la edad:", media_edad)
print("Mediana de la edad:", mediana_edad)
print("Moda de la ciudad:", moda_ciudad)

print("\nMedidas de Dispersión:")
print("Varianza de la edad:", varianza_edad)
print("Desviación estándar de la edad:", desviacion_estandar_edad)
print("Rango intercuartílico de la edad:", rango_intercuartilico_edad)

# Histograma de la edad
plt.figure(figsize=(8, 6))
sns.histplot(data=datos, x='Edad', bins=10, kde=True)
plt.title('Histograma de la Edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Boxplot de la edad
plt.figure(figsize=(8, 6))
sns.boxplot(data=datos, y='Edad')
plt.title('Boxplot de la Edad')
plt.ylabel('Edad')
plt.show()

# Cálculo de la media de la columna 'Edad' por ciudad
media_edad_por_ciudad = datos.groupby('Ciudad')['Edad'].mean()

# Gráfico de barras del promedio de la edad por ciudad
plt.figure(figsize=(8, 6))
sns.barplot(x=media_edad_por_ciudad.index, y=media_edad_por_ciudad.values)
plt.title('Promedio de la Edad por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Promedio de Edad')
plt.show()
