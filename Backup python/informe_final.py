import csv
from os import chdir
from pprint import pprint
from fileparse import parse_csv
import lote
import formato_tabla

def leer_camion(nombre_archivo_camion):
    camion = parse_csv(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float],has_headers=True)
    cd = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion]
    return cd
    '''total = 0.0
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
    return camion,total'''
        
def leer_precios(nombre_archivo_precios):
    camion2=parse_csv(nombre_archivo_precios, select = None, types = [str, float], has_headers = False)
    return camion2
    '''camion2={}
    archivo=open('Data/precios.csv','rt')
    rows = csv.reader(archivo)
    for row in rows:
        try:
            camion2[row[0]]=float(row[1])
        except IndexError:
            print('')
    archivo.close()
    return camion2
'''

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateo(fmt)
    imprimir_informe(data_informe, formateador)

'''
def f_principal(argv):
    if len(argv) != 3:
        raise TypeError('La funcion trabaja con 3 argumentos')
    camion = argv[1]
    precios = argv[2]
    informe_camion(camion, precios)

if __name__=='__main__':
    import sys
    if len(sys.argv)!=3:
        raise TypeError('Necesita 3 argumentos')
    else:
        f_principal(sys.argv)

'''
x='Data/camion.csv'
y='Data/precios.csv'
informe_camion(x, y)
