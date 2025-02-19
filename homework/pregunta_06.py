"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """

    from collections import defaultdict

    valores = defaultdict(list)  # Diccionario para almacenar valores por clave

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            diccionario = partes[4].split(",")  # Columna 5 separada por ","

            for par in diccionario:
                clave, valor = par.split(":")  # Separar clave y valor
                valores[clave].append(int(valor))  # Guardar el valor convertido a entero

    # Crear lista de tuplas con (clave, valor mínimo, valor máximo) ordenada alfabéticamente
    resultado = sorted((clave, min(nums), max(nums)) for clave, nums in valores.items())

    return resultado

# Prueba la función
print(pregunta_06())

