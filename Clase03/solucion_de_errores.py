#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Habia varios errores, dentro del if no se consideraba la posibilidad del caracter A mayuscula en su condicion,
# solo funcionaba si la letra "a" se encontraba en la ultima posicion, y como era una funcion que retornaba variables, en la sintaxis de llamar
# a la funcion, no habia otra variable que la recibiera
#    Lo corregí cambiando el if, creando una variable que sólo se modifique si existe la presencia de una "a" o una "A", le cambie la condicion
# al if para que considere el caso de que sea una "A" mayuscula y cambia la sintaxis al llamar a la funcion
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    tiene = ''
    while i<n:
        if expresion[i] == 'a' or  expresion[i]== 'A':
            tiene = 'True'
        i += 1
    return tiene

x1=tiene_a('UNSAM 2020')
x2=tiene_a('abracadabra')
x3=tiene_a('La novela 1984 de George Orwell')

print(x1,x2,x3)

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era la falta de : en varias lineas, en la condicion del if contar con solamente un =, y al llamar a la funcion, 
# no habia variable que recibiera la que devolvia la misma.
# Lo resolvi corrigiendo lo dicho arriba

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == "A":
            return True
        i += 1
    return False

x1=tiene_a('UNSAM 2020')
x2=tiene_a('La novela 1984 de George Orwell')

print (x1,x2)

#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era que se le estaba pasando un entero y aplicandole la funcion len, que es exclusiva de strings
# tampoco estaba bien la sintaxis al llamar la funcion

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


x1=tiene_uno('UNSAM 2020')
x2=tiene_uno('La novela 1984 de George Orwell')
x3=tiene_uno('1984')

print(x1,x2,x3)

#Ejercicio 3.4. Función suma()
#Comentario: El error era que faltaba que devuelva la variable la funcion, se soluciono con un return c.

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#Ejercicio 3.5. Función leer_camion()
#Comentario: El error era que se pisaban los datos cada vez que se iteraba el for, lo solucione declarando la variable camion dentro del mismo for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)