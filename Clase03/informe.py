import csv
from pprint import pprint


def costo_camion(nombre_archivo):
    total = 0.0
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            cajon = dict(zip(headers,row))
            camion.append(cajon)
        for x in camion:
            total += int(x['cajones'])*float(x['precio'])
    return camion,total

def leer_precios():
    camion2={}
    archivo=open('Data/precios.csv','rt')
    rows = csv.reader(archivo)
    for row in rows:
        try:
            camion2[row[0]]=float(row[1])
        except IndexError:
            print('')
    archivo.close()
    return camion2

x='Data/fecha_camion.csv'
var,ptotal=costo_camion(x)
frut=leer_precios()
ganancia=0.0
costototalcamion = 0.0
venta = 0.0

for x in var:
    precio=0.0
    cajones=int(x['cajones'])
    nomb=x['nombre']
    precio=float(x['precio'])
    costototalcamion += cajones*precio
    precio = frut[nomb]
    venta += cajones*precio

ganancia = venta-costototalcamion
    
print('La ganancia es de:', round(ganancia,2))
