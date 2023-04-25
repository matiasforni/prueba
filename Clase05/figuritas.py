import random
from matplotlib.pyplot import axis
import numpy as np

#5.10

def crear_album(figus_total):
    album=np.zeros(figus_total,dtype=np.int64)
    return album

#5.11

def album_incompleto(A):
    o = 0
    for i, e in enumerate(A):
        if e == 0 and i != 0:
            o = 1
        elif e == 0 and i == 0:
            o = 2
    if o == 1 or o == 2:
        return True
    else:
        return False

#5.12

def comprar_figu(figus_total):
    figu = random.randint(1,figus_total)
    return figu

#5.13

def cuantas_figus(figus_total):
    cont = 0
    est = True
    album=np.zeros(figus_total,dtype=np.int64) #creo un album de 670 figus vacio
    while est == True:
        figu = comprar_figu(figus_total) #compro una figu
        cont += 1
        album[figu-1]=1
        est=album_incompleto(album) #me pregunto si complete el album
    return cont #retorno la cantidad de figuritas que tuve que comprar

#5.14
'''
n=6
rep = 0
n_repeticiones = 1000
lista=[]

while rep != n_repeticiones:
    a=cuantas_figus(n)
    lista.append(a)
    rep += 1

prom=np.mean(lista)
print('El promedio es:', prom)

'''

#5.15

def experimento_figus(n_repeticiones, figus_total):
    rep = 0
    lista=[]
    while rep != n_repeticiones:
        a=cuantas_figus(figus_total)
        lista.append(a)
        rep += 1
    prom=np.mean(lista)
    return prom

