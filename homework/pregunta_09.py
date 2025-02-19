"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """

    from collections import defaultdict

    conteo_claves = defaultdict(int)

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            col5 = partes[4]  # Columna 5 (diccionario codificado)
            
            pares = col5.split(",")  # Separar los pares clave:valor
            
            for par in pares:
                clave, _ = par.split(":")  # Extraer la clave
                conteo_claves[clave] += 1  # Incrementar la cuenta de la clave

    return dict(sorted(conteo_claves.items()))  # Devolver diccionario ordenado por clave

# Prueba la función
print(pregunta_09())

