def invertir_lista(lista):
    invertida=[]
    for x in reversed(lista):
        invertida.append(x)
    return invertida

inv=invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
print(inv)