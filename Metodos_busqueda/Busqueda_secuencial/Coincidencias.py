def buscar_coincidencia(lista,elemento):
	repite = 0
	for i in range(0,len(lista)):
		if lista[i] == elemento:
			repite+=1
	return repite