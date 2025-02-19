"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """

    from collections import defaultdict

    valores = defaultdict(list)  # Diccionario para almacenar valores de cada letra

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            letra = partes[0]  # Primera columna
            valor = int(partes[1])  # Segunda columna (convertida a entero)

            valores[letra].append(valor)  # Agregar el valor al diccionario

    # Crear lista de tuplas con (letra, valor máximo, valor mínimo) ordenada alfabéticamente
    resultado = sorted((letra, max(nums), min(nums)) for letra, nums in valores.items())

    return resultado

# Prueba la función
print(pregunta_05())
