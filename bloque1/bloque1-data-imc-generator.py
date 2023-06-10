import numpy as np
import pandas as pd

# Establecer la semilla para reproducibilidad
np.random.seed(123)

# Generar datos aleatorios
n = 100  # Número de personas

# Generar edades siguiendo una distribución normal
edad = np.random.normal(loc=40, scale=10, size=n).astype(int)
edad = np.clip(edad, 18, 65)  # Limitar edades entre 18 y 65 años

# Generar estaturas y pesos dependiendo del sexo y la edad
estatura = np.zeros(n)
peso = np.zeros(n)
sexos = np.random.choice(['Femenino', 'Masculino'], size=n)

for i in range(n):
    if sexos[i] == 'Femenino':
        # Estatura para mujeres: edad * 0.4 + 160 cm
        estatura[i] = edad[i] * 0.4 + 160
        estatura[i] = np.clip(estatura[i], 140, 185)  # Limitar la estatura entre 140 y 185 cm
        
        # Peso para mujeres: edad * 2.2 + 45 kg
        peso[i] = edad[i] * 2.2 + 45
        peso[i] = np.clip(peso[i], 45, 120)  # Limitar el peso entre 45 y 120 kg
    else:
        # Estatura para hombres: edad * 0.5 + 165 cm
        estatura[i] = edad[i] * 0.5 + 165
        estatura[i] = np.clip(estatura[i], 150, 185)  # Limitar la estatura entre 150 y 185 cm
        
        # Peso para hombres: edad * 2.5 + 55 kg
        peso[i] = edad[i] * 2.5 + 55
        peso[i] = np.clip(peso[i], 45, 120)  # Limitar el peso entre 45 y 120 kg

# Crear DataFrame con los datos generados
data = pd.DataFrame({'Id': range(1, n+1), 'Sexo': sexos, 'Edad': edad, 'Estatura': estatura, 'Peso': peso})

# Mostrar los datos generados
print(data)

# Exportar los datos generados a un archivo xlsx
data.to_excel('datos-generados.xlsx', index=False)