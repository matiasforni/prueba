from pprint import pprint

class Lote:

    def __init__(self,nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        cost= self.precio * self.cajones
        return cost

    def vender(self,x):
        cant= self.cajones - x
        return cant
        
    def __repr__(self):
       return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

x=Lote('Pera',100,104.6)
