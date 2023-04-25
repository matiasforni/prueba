class TorreDeControl:

    def __init__(self):
        self.part = []
        self.arribo = []

    def nuevo_arribo(self,x):
        self.arribo.append(x)

    def nueva_partida(self,y):
        self.part.append(y)

    def ver_estado(self):
        
        print('Vuelos esperando para aterrizar:')
        for x in self.arribo:
            print(x)

        print('Vuelos esperando para despegar:')
        for x in self.part:
            print(x)
    
    def asignar_pista(self):
        if self.nohay() == True:
            print('No hay aviones en espera')
            
        if len(self.arribo):
            asig = self.arribo.pop(0)
            print(f'El vuelo {asig} aterrizó con exito.')
        elif len(self.part):
            asig = self.part.pop(0)
            print(f'El vuelo {asig} despegó con exito.')
    
    def nohay(self):
        return len(self.arribo) + len(self.part) == 0

'''
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
'''