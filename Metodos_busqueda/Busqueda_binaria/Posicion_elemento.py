def pos_elemento(lista,elemento):
    pi = 0
    pf = len(lista) - 1
    pos = []
    
    while pi <= pf:
        mitad = int((pi + pf)/2)

        if lista[mitad] == elemento:
            aux = mitad
            pos.append(mitad)
            while lista[mitad - 1] == lista[mitad]:
                pos.append(mitad - 1)
                mitad -= 1
            medio = aux
            while lista[mitad + 1] == lista[mitad]:
                pos.append(mitad + 1)
                mitad += 1

        elif lista[mitad] < elemento:
            pi = mitad + 1
        else :
            pf = mitad - 1
            
        if pi == pf:
            break

    return pos

lista = [1,3,5,8,8,8,15,17,20]
elemento = 8
resultado = pos_elemento(lista,elemento)
print(resultado)