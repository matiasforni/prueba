def pascal(n, k):
    if k == 0 or k == n:
        resul = 1
    elif n == 0 or n == 1:
        resul = 1
    else:
        resul = pascal(n-1, k) + pascal(n-1,k-1)
    
    return resul

