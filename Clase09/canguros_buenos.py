class Canguro:

    def __init__(self,nombre, lista = []):
        
        if contenido == None:
            contenido = []
        self._nombre = nombre
        self.contenido_marsupio=lista

    def meter_en_marsupio(self,objeto):
        self.contenido_marsupio.append(objeto)

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objeto a ser agregado
        """
        self.contenido_marsupio.append(item)

# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        if contenido == None:
            contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objeto a ser agregado
        """
        self.contenido_marsupio.append(item)
'''
#%%
madre_canguro = Canguro('Madre') #se crea un objeto de la clase canguro con el nombre madre
cangurito = Canguro('gurito') #se crea un objeto de la clase canguro con el nombre gurito
madre_canguro.meter_en_marsupio('billetera') #para el objeto madre_canguro, se utiliza el metodo meter_en_marsupio para el item billetera
madre_canguro.meter_en_marsupio('llaves del auto') #para el objeto madre_canguro, se utiliza el metodo meter_en_marsupio para el item llaves del auto
madre_canguro.meter_en_marsupio(cangurito) #para el objeto madre_canguro, se utiliza el metodo meter_en_marsupio para el objeto cangurito

print(madre_canguro)'''