import csv
from pprint import pprint
import os
import matplotlib.pyplot as plt
import numpy as np
'''
def leer_parque(nombre_archivo, parque):
    
    lista = []
    with open(nombre_archivo, 'rt',encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            coso = row[10]
            if parque == coso:
                informacion = {
                    'long':float(row[0]),
                    'lat':float(row[1]),
                    'id_arbol':int(row[2]),
                    'altura_tot':int(row[3]),
                    'diametro':int(row[4]),
                    'inclinacion':int(row[5]),
                    'id_especie':int(row[6]),
                    'nombre_com':row[7],
                    'nombre_cie':row[8],
                    'tipo_folla':row[9],
                    'ubicacion':row[11],
                    'nombre_fam':row[12],
                    'nombre_gen':row[13],
                    'origen':row[14],
                    'coord_x':float(row[15]),
                    'coord_y':float(row[16])
                }
                lista.append(informacion)
        return lista
'''
#ejercicio 4.16:
'''
def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt',encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            informacion = {
                'long':float(row[0]),
                'lat':float(row[1]),
                'id_arbol':int(row[2]),
                'altura_tot':int(row[3]),
                'diametro':int(row[4]),
                'inclinacion':int(row[5]),
                'id_especie':int(row[6]),
                'nombre_com':row[7],
                'nombre_cie':row[8],
                'tipo_folla':row[9],
                'espacio_ve':row[10],
                'ubicacion':row[11],
                'nombre_fam':row[12],
                'nombre_gen':row[13],
                'origen':row[14],
                'coord_x':float(row[15]),
                'coord_y':float(row[16])
                }
            arboleda.append(informacion)
        H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacaranda']
    return H
'''
#ejercicio 4.17:

def leer_arboles(nombre_archivo):
    resultado = []
    arboleda = []
    with open(nombre_archivo, 'rt',encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            informacion = {
                'long':float(row[0]),
                'lat':float(row[1]),
                'id_arbol':int(row[2]),
                'altura_tot':int(row[3]),
                'diametro':int(row[4]),
                'inclinacion':int(row[5]),
                'id_especie':int(row[6]),
                'nombre_com':row[7],
                'nombre_cie':row[8],
                'tipo_folla':row[9],
                'espacio_ve':row[10],
                'ubicacion':row[11],
                'nombre_fam':row[12],
                'nombre_gen':row[13],
                'origen':row[14],
                'coord_x':float(row[15]),
                'coord_y':float(row[16])
                }
            arboleda.append(informacion)
        for x in arboleda:
            if x['nombre_com'] == 'Jacaranda':
                altura=x['altura_tot']
                diametro=x['diametro']
                tupla=(altura,diametro)
                resultado.append(tupla)
    return resultado

'''
x='Data/arboladoenespaciosverdes.csv'
#parque=input('Ingrese el nombre de un parque:')
#parque=parque.upper()

#data=leer_parque(x,parque)
data=leer_arboles(x)

pprint(data)
'''
#5.25


nombre_archivo='Data/arboladoenespaciosverdes.csv'
arboleda = leer_arboles(nombre_archivo)
array=np.array(arboleda)
plt.hist(array,bins=15)
plt.show()  

#5.26

listad=[]
listaa=[]

def scatter_hd(lista_de_pares):
    for x in lista_de_pares:
        listad.append(x[1])    
        listaa.append(x[0])
    diametros=np.array(listad)    
    altos=np.array(listaa)
    plt.scatter(diametros,altos,alpha=0.1)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

nombre_archivo='Data/arboladoenespaciosverdes.csv'
scatter_hd(leer_arboles(nombre_archivo))







