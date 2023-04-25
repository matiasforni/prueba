'''
def busqueda_binaria(lista, x):
    '''#Búsqueda binaria
    #Precondición: la lista está ordenada
    #Devuelve -1 si x no está en lista;
    #Devuelve p tal que lista[p] == x, si x está en lista
'''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
'''

def bbinaria_rec(lista, e):
        
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        n = lista[medio]
        if n <= e:
            nlista = lista[medio:]
        else:
            nlista = lista[:medio]
        res = bbinaria_rec(nlista,e)

    return res
    
'''
l= [1,2,3,4,5,6,7,8]
h=5
x=bbinaria_rec(l,h)
print(x)
'''