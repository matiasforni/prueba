from vigilante import vigilar
import csv
import informe_final
import formato_tabla

def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        rowdata = [row['nombre'], str(row['precio']), str(row['volumen'])]
        formateador.fila(rowdata)

def elegir_columnas(rows, indices):
    return((row[index] for index in indices) for row in rows)

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows

def cambiar_tipo(rows, types):
    return((func(val) for func, val in zip(types, row)) for row in rows)

def hace_dicts(rows, headers):
    return((dict(zip(headers, row))) for row in rows)

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    return((fila for fila in rows if fila['nombre'] in nombres))
    
if __name__ == '__main__':
    ticker('Data/camion.csv', 'Data/mercadolog.csv', 'txt')