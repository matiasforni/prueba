import timeit as tt
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
    
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    
    return

def reubicar(lista, i):
    v = lista[i]

    j = i
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return

def ord_insercion(lista):
    
    for i in range(len(lista) - 1):                
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
                
    return

def ord_burbujeo(lista):
    n = len(lista)
    while n > 1:
        burbujas(lista, n)
        n -= 1
    return

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
    while i < len(lista1) and j < len(lista2):        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    
    return resultado

def generar_listas(Nmax):
    listas = []
    for N in range(Nmax):
        listas.append(generar_lista(N+1))
    return listas

def experimento_timeit(Nmax):
    selec = []
    inserc = []
    burbu = []
    mergesort = []
    m=10
    global i
    global lista
    for lista in listas:
        print ('Lista de longitud', len(lista))
        selecl = tt.timeit('ord_seleccion(lista.copy())', number = m, globals = globals()) 
        insercl = tt.timeit('ord_insercion(lista.copy())', number = m, globals = globals())
        burbul = tt.timeit('ord_burbujeo(lista.copy())', number = m, globals = globals())
        mergesortl = tt.timeit('merge_sort(lista.copy())', number = m, globals = globals())
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
        ln = lista
    else:
        medio = len(lista)//2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        ln = merge(izq, der)
    return ln

'''
listas = generar_listas(256)
sel,ins,bur,mer = experimento_timeit(listas)
plt.figure(figsize = [7, 7])
plt.title('Tiempo que tarda cada método')
plt.plot(mer, c = 'red', label = 'Mergesort')
plt.plot(ins, c = 'yellow', label = 'Inserción')
plt.plot(bur, c = 'blue', label = 'Burbujeo')
plt.plot(sel, c = 'green', label = 'Selección')
plt.legend()
plt.show()
'''