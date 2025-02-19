"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 2 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """

    from collections import defaultdict

    asociaciones = defaultdict(list)  # Diccionario para agrupar letras por valores de la columna 2

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            letra = partes[0]  # Columna 1 (letra)
            valor = int(partes[1])  # Columna 2 (valor numérico)

            asociaciones[valor].append(letra)  # Agregar la letra al valor correspondiente

    # Convertir el diccionario en una lista de tuplas ordenada por la clave numérica
    resultado = sorted(asociaciones.items())

    return resultado

# Prueba la función
print(pregunta_07())

