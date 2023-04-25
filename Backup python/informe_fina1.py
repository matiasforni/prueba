import csv
from pprint import pprint
from fileparse import parse_csv

def leer_camion(nombre_archivo_camion):
    camion = parse_csv(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float],has_headers=True)
    return camion
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
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    lista=[]
    precios={}
    camion = leer_camion(nombre_archivo_camion)
    camion2 = leer_precios(nombre_archivo_precios)
    for x in camion2:
        x0=x[0]
        x1=x[1]
        precios[x0]=x1
    for x in camion:
        cajones=x['cajones']
        nomb=x['nombre']
        precio=x['precio']
        cambio=precios[nomb]-float(precio)
        info=(nomb,int(cajones),float(precio),float(cambio))
        lista.append(info)
    fila=('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    print(f'{fila[0]:<10s} {fila[1]:>10s} {fila[2]:>10s} {fila[3]:>10s}')
    print('----------''----------''----------''--------------')
    for x in lista:
        precio=str(round(x[2],2))
        print(f'{x[0]:<10s} {x[1]:>10d} {"$"+precio:>10s} {x[3]:>10.2f}')

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
