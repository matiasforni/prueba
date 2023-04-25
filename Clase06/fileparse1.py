# fileparse.py
import csv
'''
#6.7

def parse_csv(nombre_archivo, select):
    '''
    #Parsea un archivo CSV en una lista de registros
'''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

         # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select #le pongo los encabezados que se seleccionaron al llamar a la funcion
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila:    # Saltea filas sin datos
                continue
            # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
            if indices:
                fila = [fila[index] for index in indices]
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
'''
'''
#6.8

def parse_csv(nombre_archivo, select, types):
    '''
    #Parsea un archivo CSV en una lista de registros
'''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

         # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select #le pongo los encabezados que se seleccionaron al llamar a la funcion
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila:    # Saltea filas sin datos
                continue
            # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
            if indices:
                fila = [fila[index] for index in indices]
            
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
'''

#6.9

def parse_csv(nombre_archivo, select, types, has_headers):
    '''
    #Parsea un archivo CSV en una lista de registros
'''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers == True:
            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select #le pongo los encabezados que se seleccionaron al llamar a la funcion
            else:
                indices = []
            registros = []
            for fila in filas:
                if not fila:    # Saltea filas sin datos
                    continue
                # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            indices = []
            registros = []
            for fila in filas:
                if not fila:    # Saltea filas sin datos
                    continue
                if types:
                    fila0 = str(fila[0])
                    fila1 = float(fila[1])
                registro = (fila0,fila1)
                registros.append(registro)
        
    return registros


'''
types=[str, float]
select = []
has_headers=False
coso=parse_csv('Data/precios.csv',select,types,has_headers)
print(coso)
'''