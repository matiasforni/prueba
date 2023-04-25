import random
import matplotlib.pyplot as plt
import numpy as np

def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_seleccion(lista):
    
    n = len(lista) - 1
    comparaciones = 0

    while n > 0:
        p = buscar_max(lista, 0, n)
        comparaciones += n
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    
    return comparaciones

def reubicar(lista, i):
    comparaux = 0
    v = lista[i]

    j = i
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        comparaux += 1
        j -= 1

    lista[j] = v
    return comparaux

def ord_insercion(lista):
    comparaciones = 0
    for i in range(len(lista) - 1):                
        if lista[i + 1] < lista[i]:
            comparaciones = reubicar(lista, i + 1)
        comparaciones += 1
        
    return comparaciones

def ord_burbujeo(lista):
    n = len(lista)
    comparaciones = 0
    while n > 1:
        burbujas(lista, n)
        comparaciones += n-1
        n -= 1
    return comparaciones

def burbujas(lista, n):
    for i in range(n-1):
        if lista[i+1] < lista[i]:
            lista[i], lista[i-1] = lista[i-1], lista[i]    

def generar_lista(N):
    list=[]
    for i in range(N):
        list.append(random.randint(1,1000))
    return list

def merge(lista1,lista2):
    i, j = 0, 0
    resultado = []
    comparaciones_aux = 0
    while i < len(lista1) and j < len(lista2):
        comparaciones_aux += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    
    return resultado, comparaciones_aux

def experimento_vectores(Nmax):
    selec = []
    inserc = []
    burbu = []
    mergesort = []
    for N in range(Nmax):
        lista = generar_lista(N)
        selecl = ord_seleccion(lista.copy())
        insercl = ord_insercion(lista.copy())
        burbul = ord_burbujeo(lista.copy())
        mergesortl = merge_sort(lista.copy())[1]
        selec.append(selecl)
        inserc.append(insercl)
        burbu.append(burbul)
        mergesort.append(mergesortl)
    selecl = np.array(selec)
    insercl = np.array(inserc)
    burbul = np.array(burbu)
    mergesortl = np.array(mergesort)
    
    return selec, inserc, burbu, mergesort

def merge_sort(lista):       
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        medio = len(lista)//2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_merge
    return lista_nueva, comparaciones

'''
s,i,b,m = experimento_vectores(256)
plt.figure(figsize = [7, 7])
plt.title('Cantidad de comparacion de cada método')
plt.plot(s, c = 'blue', label = 'Selección')
plt.plot(i, c = 'green', label = 'Inserción')
plt.plot(b, c = 'red', label = 'Burbujeo')
plt.plot(m, c = 'yellow', label = 'Mergesort')
plt.legend()
plt.show()
'''