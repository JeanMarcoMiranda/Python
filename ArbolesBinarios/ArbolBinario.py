class ArbolBinario:
	def __init__(self,objetoRaiz):
		self.clave = objetoRaiz
		self.hijoDerecho = None
		self.hijoIzquierdo = None

	def insertarIzquierdo(self, nuevoNodo):
		if self.hijoIzquierdo == None:
			self.hijoIzquierdo = ArbolBinario(nuevoNodo)
		else:
			t = ArbolBinario(nuevoNodo)
			t.hijoIzquierdo = self.hijoIzquierdo
			self.hijoIzquierdo = t

	def insertarDerecho(self,nuevoNodo):
		if self.hijoDerecho == None:
			self.hijoDerecho = ArbolBinario(nuevoNodo)
		else:
			t = ArbolBinario(nuevoNodo)
			t.hijoDerecho = self.hijoDerecho
			self.hijoDerecho = t

	def obtenerHijoDerecho(self):
		return self.hijoDerecho

	def obtenerHijoIzquierdo(self):
		return self.hijoIzquierdo

	def  asignarVarlorRaiz(self, valor):
		self.clave = valor

	def obtenerValorRaiz(self):
		return self.clave

def verAmplitud(raiz):
	cont = 1
	Ar = [raiz]
	for Ar in range(0,len(Ar)):
		tamaño = len(Ar)
		aux = Ar.pop()
		if cont == 1 and aux == None:
			cont = 0
			return cont
		else:
			if aux.obtenerHijoIzquierdo() != None: