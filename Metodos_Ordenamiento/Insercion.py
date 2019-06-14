def ordenamiento_insercion(lista):
    for indice in range(1,len(lista)):
        valorActual = lista[indice]
        posicion = indice
        while posicion>0 and lista[posicion-1]>valorActual:
            lista[posicion]=lista[posicion-1]
            posicion = posicion-1
            lista[posicion]=valorActual
    return lista

#Invocacion de funcion
lista = [54,26,93,17]
lista_ordenada=ordenamiento_insercion(lista)
print(lista_ordenada)
