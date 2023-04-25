
def busqueda_binaria(lista, x, verbose = False):
    '''#Búsqueda binaria
    #Precondición: la lista está ordenada
    #Devuelve -1 si x no está en lista;
    #Devuelve p tal que lista[p] == x, si x está en lista
'''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    f = 0
    flag = 0
    mayor = 0
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        for i in lista:
            if x>i:
                flag = 1
                mayor = 1
            if x<i and flag == 1:
                break
            f += 1
        if mayor == 0:
            f = 0
    if pos == -1:
        flag = 1
        return f,flag,comps
    else:
        flag = 0
        return pos,flag,comps

def insertar(lista,x):
    u,flag,c=donde_insertar(lista, x)
    if flag == 1:
        lista.insert(u,x)
        return u
    else:
        return u

#x=insertar([0,2,4,6], 3)
#x=busqueda_binaria([1, 3, 5], 0, verbose = True)
