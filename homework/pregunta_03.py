"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """

    suma_letras = {}  # Diccionario para almacenar la suma de la columna 2 por cada letra

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separa la línea en columnas
            letra = partes[0]  # Primera columna (letra)
            valor = int(partes[1])  # Segunda columna (número convertido a entero)

            # Sumar valores por cada letra
            suma_letras[letra] = suma_letras.get(letra, 0) + valor

    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(suma_letras.items())

    return resultado

# Prueba la función
print(pregunta_03())
