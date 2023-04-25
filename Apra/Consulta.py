import csv
from pprint import pprint
from fileparse import parse_csv

def imprimir(n):
    camion = parse_csv(n, select = ['NOM_CLIENTE', 'DIRECCION', 'MEDIDOR','FECHA_LEC_DESDE','IMP_TOTAL_FACTURA','ENERGIA_ACTIVA','POT_CONTR','POT_EXCESO'], types = [str, str, int, str, float, float, int, float],has_headers=True)
    print(camion)

def f_principal(argv):
    if len(argv) != 2:
        raise TypeError('La funcion trabaja con 2 argumentos')
    nomb = argv[1]
    imprimir(nomb)

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:
        raise TypeError('Necesita 2 argumentos')
    else:
        f_principal(sys.argv)