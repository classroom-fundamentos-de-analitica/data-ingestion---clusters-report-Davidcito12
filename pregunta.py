"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re
def ingest_data():
    with open('clusters_report.txt') as text:
        row = text.readlines()

    row = row[4:]
    for i in range(len(row)):
        row[i] = row[i].strip()

    categories = ''
    numeros = []
    cantidades =[]
    porcentajes = []
    for i in row:

        try:
            int((i[0]+i[1]))
            numero, cantidad, porcentaje, basura, *palabras = i.split()
            numeros.append(int(numero))
            porcentajes.append(float(re.sub("[,]",".",porcentaje)))
            cantidades.append(int(cantidad))
            palabras[0] = "-x-x-x-x-" + palabras[0]
            for palab in palabras:
                categories += " " + palab
        except:
            if i == "":
                continue
            k = i.split()
            k[0] = " " + k[0]
            for palab in k:
                categories += "  " + palab

    categories = re.sub(" +"," ",categories)
    categories = re.sub("[.]","",categories)
    categories = categories.split('-x-x-x-x-')
    categories = list(map(lambda x: x.strip(), categories))
    del(categories[0])

    dataframe = pd.DataFrame()
    dataframe['cluster'] = numeros
    dataframe['cantidad_de_palabras_clave'] = cantidades
    dataframe['porcentaje_de_palabras_clave'] = porcentajes
    dataframe['principales_palabras_clave'] = categories

    return dataframe
