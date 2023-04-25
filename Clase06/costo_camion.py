import csv
from informe_funciones import leer_camion

x='Data/camion.csv'
camion,total=leer_camion(x)

print('El total es',total)