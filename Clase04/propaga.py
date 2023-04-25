def propagar(lista):
    list2=[]
    list3=[]
    list4=[]
    fue = 0
    for x in lista:
        if x == 1:
            fue = 1
            fos = 1
        if x == 0:
            if fue == 1:
                fos = 1
            else:
                fos = 0
        if x == -1:
            fue = 0
            fos = -1
        list2.append(fos)
    
    fue = 0

    for x in reversed(list2):
        if x == 1:
            fue = 1
            fos = 1
        if x == 0:
            if fue == 1:
                fos = 1
            else:
                fos = 0
        if x == -1:
            fue = 0
            fos = -1
        list3.append(fos)

    for x in reversed(list3):
        list4.append(x)
    
    return list4


fosforos=propagar([ 0, 0, 0, 1, 0, 0])

print(fosforos)
            