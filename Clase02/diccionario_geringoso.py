def gerin(lista):
    dicc = dict()
    i = 0
    for x in lista:
        palabra = x
        geringoso = ''
        for c in palabra:
            geringoso += c
            if c == 'a':
                geringoso += 'pa'
            if c == 'e':
                geringoso += 'pe'
            if c == 'i':
                geringoso += 'pi'
            if c == 'o':
                geringoso += 'po'
            if c == 'u':
                geringoso += 'pu'
        if x == 'banana':
            dicc['banana'] = geringoso
        if x == 'manzana':
            dicc['manzana'] = geringoso
        if x == 'mandarina':
            dicc['mandarina'] = geringoso
    return dicc

cant=int(input('La cantidad de palabras que va a ingresar en la lista es: '))

i=0
lista = []

for i in range(0,cant):
    print('Ingrese la palabra de la posicion ', i, )
    x = input()
    lista.append(x)

dicc1 = gerin(lista)

print(dicc1)