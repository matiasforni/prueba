import csv
from pprint import pprint


def costo_camion(nombre_archivo):
    total = 0.0
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            cajon = {
                'nombre':row[0],
                'cajones':int(row[1]),
                'precio':float(row[2])
            }
            camion.append(cajon)
        for x in camion:
            total += x['cajones']*x['precio']
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

def hacer_informe(camion,precios):
    lista=[]
    for x in camion:
        cajones=x['cajones']
        nomb=x['nombre']
        precio=x['precio']
        cambio=precios[nomb]-float(precio)
        info=(nomb,int(cajones),float(precio),float(cambio))
        lista.append(info)
    return lista

x='Data/camion.csv'
var,ptotal=costo_camion(x)
frut=leer_precios()
lista=hacer_informe(var,frut)
ganancia=0.0
costototalcamion = 0.0
venta = 0.0

fila=('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{fila[0]:<10s} {fila[1]:>10s} {fila[2]:>10s} {fila[3]:>10s}')
print('----------''----------''----------''--------------')
for x in lista:
    precio=str(round(x[2],2))
    print(f'{x[0]:<10s} {x[1]:>10d} {"$"+precio:>10s} {x[3]:>10.2f}')

for x in var:
    precio=0.0
    cajones=x['cajones']
    nomb=x['nombre']
    precio=x['precio']
    costototalcamion += cajones*precio
    precio = frut[nomb]
    venta += cajones*precio

ganancia = venta-costototalcamion
    
print('La ganancia es de:', round(ganancia,2))