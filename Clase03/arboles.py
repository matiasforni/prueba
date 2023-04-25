import csv

def leer_parque(nombre_archivo, parque):
    
    lista = []
    with open(nombre_archivo, 'rt',encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            coso = row[10]
            if parque == coso:
                informacion = {
                    'long':float(row[0]),
                    'lat':float(row[1]),
                    'id_arbol':int(row[2]),
                    'altura_tot':int(row[3]),
                    'diametro':int(row[4]),
                    'inclinacion':int(row[5]),
                    'id_especie':int(row[6]),
                    'nombre_com':row[7],
                    'nombre_cie':row[8],
                    'tipo_folla':row[9],
                    'ubicacion':row[11],
                    'nombre_fam':row[12],
                    'nombre_gen':row[13],
                    'origen':row[14],
                    'coord_x':float(row[15]),
                    'coord_y':float(row[16])
                }
                lista.append(informacion)
        return lista
'''
x='Data/arboladoenespaciosverdes.csv'
parque=input('Ingrese el nombre de un parque:')
parque=parque.upper()

data=leer_parque(x,parque)

for x in data:
    print(f"{x['long']:<3.3f} {x['lat']:>3.3f} {x['id_arbol']:>3d} {x['altura_tot']:>3d} {x['diametro']:>3d} {x['inclinacion']:>3d} {x['id_especie']:>3d} {x['nombre_com']:>3s} {x['nombre_cie']:>3s} {x['tipo_folla']:>3s} {x['ubicacion']:>3s} {x['nombre_fam']:>3s} {x['nombre_gen']:>3s} {x['origen']:>3s} {x['coord_x']:>3.2f} {x['coord_y']:>3.2f}")
'''


