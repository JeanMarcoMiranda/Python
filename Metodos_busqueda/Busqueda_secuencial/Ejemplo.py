def busqueda_secuencia(lista,elemento):
	for i in range(0,len(lista)):
		if lista[i] == elemento:
			return i
	else:
			return -1

lista = [9,8,5,4,7,12,46,62,31,0]
elemento = 46
resultado = busqueda_secuencia(lista,elemento)

if(resultado != -1):
	print("El elemento: ",elemento," esta en la posicion: ",resultado)
else:
	print("El elemento: ",elemento," no se encuentra en la lista")"""
