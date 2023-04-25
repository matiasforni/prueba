'''
CONTRATO: Precondicion: La variable que recibe debe ser del tipo entera o flotante
Poscondicion: En caso de que sea un numero positivo, retorna el mismo, en caso de que sea negativo, lo multi
plica por -1 y lo retorna (en este caso modifica el parametro recibido)

Recibee un numero y devuelve su modulo'''
def valor_absoluto(n):
    if n >= 0:
        return n
    else:

        return -n

'''
CONTRATO: Precondicion: Debe recibir una variable que sea iterable, para poder recorrerla, pero no puede ser una
cadena de caracteres (ya que no puede efectuar operaciones matematicas a posterior)
Poscondicion: Retorna una variable que tiene la suma de todos los numeros pares que se encontraban dentro de
la variable que le fue pasada como input, no se modifican los valores dentro de la variable input

Recibe un objeto iterable (posiblemente una lista), la recorre y suma todos sus numeros pares'''
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

'''
CONTRATO: Precondicion: El parametro 'a' puede ser entero o flotante, pero el parametro 'b' debe ser entero,
porque si es flotante se quedaria en un bucle infinito ya que nunca seria 0
Poscondicion: Retorna la suma de 'b' veces el numero 'a' en una variable llamada 'res', ambos parametros de 
entrada no se modifican ya que se trabaja con otros que son decretados de manera local dentro de la funcion

Recibe un numero 'a' y lo suma 'b' veces a si mismo'''
def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

'''
CONTRATO: Precondicion: Se debe otorgar como parametro un numero entero positivo
Poscondicion: La variable de input es operada hasta que termina obteniendo el valor 1 y se retorna una variable
res que contiene la cantidad de pasos que realizo el bucle while

Recibe un numero, y hasta que el numero sea igual a '1' se fija si es par (en ese caso lo divide por 2 
y se queda con la parte entera del resultado) y si es impar (en ese caso se multiplica por 3 y se suma 1).
 Se considera conjetura de Collatz, la cual dice que sea cual sea el numero 'x' inicial tras un numero finito 
 de repeticiones, la operacion siempre llega a 1. Hay un contador de pasos'''
def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res