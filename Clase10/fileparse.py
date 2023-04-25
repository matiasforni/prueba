import csv

def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    
    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    filas = csv.reader(lines)

    if has_headers:
        encabezados = next(filas)
    else:
        encabezados = []

    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
    for n_fila, fila in enumerate(filas, start = 1):
        if not fila:
            continue
        if indices:
            fila = [fila[index] for index in indices]
        
        try:
            if types:
            
                fila = [func(val) for func, val in zip(types, fila)]
                
            if encabezados:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)

            registros.append(registro)
        
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {n_fila}: No pude convertir {fila}')
                print(f'Fila {n_fila}: Motivo: {e}')
                
    return registros

    





