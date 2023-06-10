# Variables y tipos de datos

# Variables numéricas
edad = 25
salario = 1500.50

# Cadenas de texto
nombre = "Juan"
apellido = 'Pérez'

# Listas
numeros = [1, 2, 3, 4, 5]
frutas = ['manzana', 'plátano', 'naranja']

# Diccionarios
persona = {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}

# Estructuras de control:**

# Condicionales (if/else)
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Bucles (for/while)
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Operadores lógicos
a = True
b = False
if a and b:
    print("Ambas condiciones son verdaderas")
elif a or b:
    print("Al menos una condición es verdadera")
else:
    print("Ninguna condición es verdadera")

# Funciones y módulos

# Definición y llamada de funciones
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print("Resultado:", resultado)

# Importación y uso de módulos predefinidos y personalizados
import math

valor_absoluto = math.fabs(-5)
print("Valor absoluto:", valor_absoluto)

import mi_modulo

mi_modulo.saludar()

# Manipulación de datos

# Lectura y escritura de archivos CSV o Excel
import pandas as pd

# Lectura de un archivo CSV
datos = pd.read_csv('archivo.csv')

# Escritura de un DataFrame a un archivo CSV
datos.to_csv('nuevo_archivo.csv', index=False)

# Lectura de un archivo Excel
datos = pd.read_excel('archivo.xlsx')

# Escritura de un DataFrame a un archivo Excel
datos.to_excel('nuevo_archivo.xlsx', index=False)

# Limpieza de datos
datos_limpios = datos.dropna()

# Filtrado de datos
datos_filtrados = datos[datos['edad'] > 18]

# Transformación de datos
datos['edad'] = datos['edad'] + 1
