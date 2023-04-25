import random

def tirar():
    n=4
    lista=[]
    lista1=[]
    lista2=[]
    lista3=[]
    for i in range(5):
        tirada1 = random.randint(1,6)
        lista1.append(tirada1)
    prim = lista1[0]
    if n != 0:
        for x in lista1:
            if x == prim:
                n = n - 1
    for i in range(n):
        tirada2 = random.randint(1,6)
        lista2.append(tirada2)
    if n != 0:
        for x in lista2:
            if x == prim:
                n = n - 1
    for i in range (n):
        tirada3 = random.randint(1,6)
        lista3.append(tirada3)
    s=5-n
    for i in range(s):
        h=prim
        lista.append(h)
    
    lista = lista3 + lista

    return lista

def es_generala(tirada):
    resul= True
    prim=tirada[0]
    for x in tirada:
        if x != prim:
            resul= False
            break
   
    return resul

def prob_generala(N):
    prob=0.0
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N

    return prob


N=10000

x=prob_generala(N)

print(f'Podemos estimar la probabilidad de sacar generala servida mediante {x:.6f}.')

