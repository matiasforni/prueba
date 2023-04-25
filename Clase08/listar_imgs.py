import os

def archivos_png(directorio):
    imag=[]
    for r,d,f in os.walk(directorio):
        for name in f:
            if 'png' in name:
                imag.append(name)
        for name in d:
            if 'png' in name:
                imag.append(name)
    print(imag)

def f_principal(argv):
    if len(argv) != 2:
        raise TypeError('La funcion trabaja con 2 argumentos')
    d = argv[1]
    archivos_png(d)

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:
        raise TypeError('Necesita 2 argumentos')
    else:
        f_principal(sys.argv)
