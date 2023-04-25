import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()

def modulo(n):
    if n >= 0:
        return n
    else:
        return -n

def repeticion(repeticiones,N):
    #N = 10000
    caminata=randomwalk(N)
    plt.plot(caminata)
    dist=max(abs(caminata))
    dist_max=dist
    dist_min=dist
    lejana=caminata
    cercana=caminata
    resultado_rep=[caminata]
    
    for i in range(1,repeticiones):
        caminata=randomwalk(N)
        plt.plot(caminata)
        dist=max(abs(caminata))
        
        if dist>dist_max:
            lejana=caminata
            dist_max=dist
        
        if dist<dist_max:
            cercana=caminata
            dist_min=dist
        
        resultado_rep.append(caminata)
    return lejana,cercana

N = 100000
rep=12
i = 0
m=randomwalk(N)

plt.subplot(2, 1, 1)
plt.title('Caminatas random')
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
lejana,cercana=repeticion(rep,N)

plt.subplot(2, 2, 3)
plt.title('La que mas se aleja')
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.plot(lejana)

plt.subplot(2, 2, 4)
plt.title('La que mas se acerca')
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.plot(cercana)
plt.show()