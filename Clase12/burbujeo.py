def ord_burbujeo(lista):
    ok=False
    while ok == False:  
        x=ordenar(lista)
        ok = check(x)
    return x

def ordenar(lista):
    i=0
    largo = len(lista) - 1
    while i < largo:
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
        i += 1
    return lista

def check(lista):
    ok = True
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            ok = False
    return ok

'''
l=[2, 5, 1, 0]
x=ord_burbujeo(l)
print(x)
'''