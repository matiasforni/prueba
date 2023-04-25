import random
import statistics
import numpy as np
import os

def medir_temp(n):
    lista=[]
    for i in range(n):
        temp=37.5
        x=random.normalvariate(0,0.2)
        temp = temp + x
        lista.append(round(temp,3))
    arrayl=np.array(lista)
    np.save(os.path.join('Data','temperaturas'), arrayl)
    return arrayl

def resumen_temp(n):
    lista=medir_temp(n)
    max=lista[0]
    min=lista[0]
    prom=0
    for x in lista:
        if x>max:
            max=x
        elif x<min:
            min=x
        prom = prom + x
    prom = prom/n
    mediana=statistics.median(lista)

    tupla = (max,min,prom,mediana)
        
    return tupla 
'''

N=999
o=medir_temp(N)
print(o)

print('')
print(f"{'Maximo':<7s}{'Minimo':<7s}{'Promedio':<9s}{'Mediana':<8s}")
print('------------------------------')
print(f"{o[0]:<7.2f}{o[1]:<7.2f}{o[2]:<9.2f}{o[3]:<8.2f}")
'''

