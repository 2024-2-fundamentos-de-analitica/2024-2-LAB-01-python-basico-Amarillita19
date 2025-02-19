"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """

    resultado = {}

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            
            valor_col2 = int(partes[1])  # Convertir la columna 2 a entero
            letras_col4 = partes[3].split(",")  # Lista de letras en columna 4

            for letra in letras_col4:
                if letra in resultado:
                    resultado[letra] += valor_col2
                else:
                    resultado[letra] = valor_col2

    return dict(sorted(resultado.items()))  # Ordenar alfabéticamente por clave

# Prueba la función
print(pregunta_11())

