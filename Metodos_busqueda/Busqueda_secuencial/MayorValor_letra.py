def letras(lista):
	mletra = ""
	abcdario = "abcdefghijklmnopqrstuvwxyz"
	mpos = 0
	for i in lista:
		for f in range(0,len(abcdario)):
			if i == abcdario[f]:
				if f > mpos:
					mpos = f
	
	for i in lista:
		for f in range(0,len(abcdario)):
			if i == abcdario[f]:
				if f == mpos:
					mletra += i
	return mletra