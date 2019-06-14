def maximo (lista):
    posmax = 0
    posmin = 0
    for i in range (0,len(lista)):
        if i == 0:
            max = lista [i]
            min = lista [i]
        else:
            if lista [i] > max:
                max = lista [i]
                posmax = i
            if lista [i] < min:
                min = lista [i]
                posmin = i
    vector = [[max, posmax], [min, posmin]]
    return vector