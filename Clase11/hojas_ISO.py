
def medidas_hoja_A(N):
 
    if N == 0:
        a0 = [841,1189]
        return tuple(a0)

    if N>=1:
        an1 = medidas_hoja_A(N-1)
        an = int(an1[1]/2),an1[0]
        return tuple(an)
        
'''
x=medidas_hoja_A(1)
print(x)
'''