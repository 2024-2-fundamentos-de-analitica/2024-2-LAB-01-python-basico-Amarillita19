"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """

    resultado = {}

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            
            letra_col1 = partes[0]  # Columna 1 (clave)
            valores_col5 = partes[4].split(",")  # Lista de claves con valores de columna 5
            
            # Extraer solo los valores numéricos después del ":"
            suma_col5 = sum(int(x.split(":")[1]) for x in valores_col5)

            if letra_col1 in resultado:
                resultado[letra_col1] += suma_col5
            else:
                resultado[letra_col1] = suma_col5

    return dict(sorted(resultado.items()))  # Ordenar alfabéticamente por clave

# Prueba la función
print(pregunta_12())


