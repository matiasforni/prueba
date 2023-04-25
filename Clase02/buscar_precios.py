def buscar_precio(fruta):
    fruta=fruta.capitalize()
    with open ('Data/precios.csv','rt') as archivo:
        for line in archivo:
            row = line.split(',',2)
            if row[0] == fruta:
                precio=row[1]
    return precio
    
x = ''
precio=''
x = input('\nInserte el nombre de la fruta para saber su precio: ')
precio = buscar_precio(x)

if precio=='':
    print(x, 'no figura en el listado de precios' )
else:
    print('\nEl precio de un cajon de', x, 'es:', precio)