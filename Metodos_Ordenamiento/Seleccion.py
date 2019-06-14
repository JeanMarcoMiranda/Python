def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        minimo=i
        for j in range(i,len(lista)):
            if(lista[j] < lista[minimo]):
                minimo=j
        if(minimo != i):
            aux=lista[i]
            lista[i]=lista[minimo]
            lista[minimo]=aux
    return lista

#llamada a funcion
lista=[6,5,3,1]
lista_ordenada=ordenamiento_seleccion(lista)
print(lista_ordenada)
