"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """

    from collections import Counter

    conteo_meses = Counter()  # Diccionario para contar registros por mes

    with open(r"C:\Users\Sara Castaño\Downloads\2024-2-LAB-01-python-basico-Amarillita19\files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")  # Separar por tabulación
            fecha = partes[2]  # Tercera columna (fecha)
            mes = fecha[5:7]  # Extraer el mes (MM) de "YYYY-MM-DD"

            conteo_meses[mes] += 1  # Incrementar el conteo del mes

    # Convertir el diccionario en una lista de tuplas y ordenarla por mes
    resultado = sorted(conteo_meses.items())

    return resultado

# Prueba la función
print(pregunta_04())
