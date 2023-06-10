import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind

# Cargar los datos desde el archivo Excel
data = pd.read_excel('bloque1-data-imc.xlsx')

# Prueba de hipótesis para la estatura media
valor_especifico = 170  # Valor específico para comparar con la media
alpha = 0.05  # Nivel de significancia

# Prueba t de una muestra para la estatura media
t_stat, p_valor = ttest_1samp(data['Estatura'], valor_especifico)

if p_valor < alpha:
    print(f"Rechazamos la hipótesis nula. La estatura media es significativamente diferente de {valor_especifico}.")
else:
    print(f"No hay suficiente evidencia para rechazar la hipótesis nula. La estatura media no es significativamente diferente de {valor_especifico}.")

# Prueba de hipótesis para la diferencia de medias entre hombres y mujeres
alpha = 0.05  # Nivel de significancia

# Dividir el DataFrame en dos grupos según el sexo
grupo_hombres = data[data['Sexo'] == 'Hombre']['Estatura']
grupo_mujeres = data[data['Sexo'] == 'Mujer']['Estatura']

# Prueba t independiente para la diferencia de medias
t_stat, p_valor = ttest_ind(grupo_hombres, grupo_mujeres)

if p_valor < alpha:
    print("Rechazamos la hipótesis nula. Hay una diferencia significativa en la estatura media entre hombres y mujeres.")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula. No hay una diferencia significativa en la estatura media entre hombres y mujeres.")
