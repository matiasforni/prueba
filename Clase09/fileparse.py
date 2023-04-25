import csv
import gzip

'''Ejercicio 7.6'''


def parse_csv(nombre_archivo, select, types, has_headers=False,silence_errors=False,gz=False):
    '''
    #Parsea un archivo CSV en una lista de registros
'''
    if gz==True:

        with gzip.open(nombre_archivo,'rt',encoding="utf8") as f:
            filas = csv.reader(f)
            if select!=None and has_headers==False:
                raise RuntimeError('Para seleccionar, necesito encabezados.')
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
                for i,fila in enumerate(filas,start=1):
                    if str()==None or int==None or float==None: #especifico cuando seria el error
                        raise ValueError 
                    if not fila:    # Saltea filas sin datos
                        continue
                    # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila) ]
                        except ValueError as e:
                            if silence_errors==False:       #si no quiero que se silencien
                                print(f'Fila {i}: No pude convertir {fila}')
                                print(f'Fila {i}: Motivo: {e}')
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
    
    else:

        with open(nombre_archivo,'rt',encoding="utf8") as f:
            filas = csv.reader(f)
            if select!=None and has_headers==False:
                raise RuntimeError('Para seleccionar, necesito encabezados.')
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
                for i,fila in enumerate(filas,start=1):
                    if str()==None or int==None or float==None: #especifico cuando seria el error
                        raise ValueError 
                    if not fila:    # Saltea filas sin datos
                        continue
                    # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila) ]
                        except ValueError as e:
                            if silence_errors==False:       #si no quiero que se silencien
                                print(f'Fila {i}: No pude convertir {fila}')
                                print(f'Fila {i}: Motivo: {e}')
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
def parse_csv1(nombre_archivo, select, types, has_headers=False,silence_errors=False,gz=False):
    '''
    #Parsea un archivo CSV en una lista de registros
'''
    if gz==True:

        with gzip.open(nombre_archivo,'rt',encoding="utf8") as f:
            filas = csv.reader(f)
            if select!=None and has_headers==False:
                raise RuntimeError('Para seleccionar, necesito encabezados.')
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
                for i,fila in enumerate(filas,start=1):
                    if str()==None or int==None or float==None: #especifico cuando seria el error
                        raise ValueError 
                    if not fila:    # Saltea filas sin datos
                        continue
                    # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila) ]
                        except ValueError as e:
                            if silence_errors==False:       #si no quiero que se silencien
                                print(f'Fila {i}: No pude convertir {fila}')
                                print(f'Fila {i}: Motivo: {e}')
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
    
    else:

        with open(nombre_archivo,'rt',encoding="utf8") as f:
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
                for i,fila in enumerate(filas,start=1):
                    if str()==None or int==None or float==None: #especifico cuando seria el error
                        raise ValueError 
                    if not fila:    # Saltea filas sin datos
                        continue
                    # Filtrar la fila si se especificaron columnas (if indice quiere decir si la variable "indice" no esta vacia)
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila) ]
                        except ValueError as e:
                            if silence_errors==False:       #si no quiero que se silencien
                                print(f'Fila {i}: No pude convertir {fila}')
                                print(f'Fila {i}: Motivo: {e}')
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

types=[str, int, float]
select = []
has_headers=True
coso=parse_csv('Data/camion.csv',select,types,has_headers)
print(coso)
'''