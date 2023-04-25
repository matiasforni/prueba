def buscar_u_elemento(lista,elemen):
    i=0
    pos=0
    y=0
    cant=0
    for x in lista:
        if x == elemen:
            pos = i
            y=1
            cant += 1
        i += 1
    return pos,y,cant

def maximo(lista):
    m=0
    cont = 0
    for x in lista:
        if cont == 0:
            m = x
            cont=1
        if x > m:
            m = x
    return m

x,y,cant=buscar_u_elemento([1,2,3,2,3,4],1)
max=maximo([-5,-4,1,-4])

if y == 0:
    print('-1')
else:
    print('La ultima aparicion del elemento en la lista se da en la posicion',x)

if cant == 1:
    print('El elemento aparece',cant, 'vez en la lista')
else:
    print('El elemento aparece',cant, 'veces en la lista')

print ('El maximo valor de la lista es',max)