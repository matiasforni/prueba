# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0.0
    archivo = open(nombre_archivo,'rt')
    filas = csv.reader(archivo)
    encabezado = next(filas)
    for x in filas:
        costo = costo + float(x[2])
    return costo
    archivo.close()

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', round(costo,2))