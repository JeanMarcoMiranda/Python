def valor_maximo(lista):
	vmax = 0
	for i in range(0,len(lista)):
		if lista[i] > vmax:
			vmax = lista[i]
	return vmax