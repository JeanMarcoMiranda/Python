def buscar_posiciones(lista,elemento):
	coincide = []
	for i in range(0,len(lista)):
		if lista[i] == elemento:
			coincide.append(i)
	return coincide