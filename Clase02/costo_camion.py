import csv
def costo_camion(nombre_archivo):
    costo = 0.0
    archivo = open(nombre_archivo,'rt')
    filas = csv.reader(archivo)
    encabezado = next(filas)
    for x in filas:
        costo = costo + float(x[2])

    print ('Costo total es de', round(costo,2))

    archivo.close()

x='Data/camion.csv'
costo_camion(x)