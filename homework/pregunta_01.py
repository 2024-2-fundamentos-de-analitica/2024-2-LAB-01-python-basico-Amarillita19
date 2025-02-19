"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    suma = 0
    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            suma += int(columnas[1])
    return suma

# Llamar a la función y mostrar el resultado
print(pregunta_01())



"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

