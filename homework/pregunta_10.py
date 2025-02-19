"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """

    resultado = []

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            
            letra = partes[0]  # Columna 1 (letra)
            col4_count = len(partes[3].split(","))  # Cantidad de elementos en la columna 4
            col5_count = len(partes[4].split(","))  # Cantidad de elementos en la columna 5
            
            resultado.append((letra, col4_count, col5_count))

    return resultado

# Prueba la función
print(pregunta_10())

