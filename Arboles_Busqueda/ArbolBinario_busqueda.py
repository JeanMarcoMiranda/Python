class Nodo:
    def __init__(self, valor, padre):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.padre = padre

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getIzquierdo(self):
        return self.izquierdo

    def setIzquierdo(self, izquierdo):
        self.izquierdo = izquierdo

    def getDerecho(self):
        return self.derecho

    def setDerecho(self, derecho):
        self.derecho = derecho

    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

class ArbolBusquedaBinaria:

    def __init__(self):
        self.raiz = None

    def vacio(self):
        if self.raiz is None:
            return True
        return False

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor, None)
        # Si el árbol esta vacio
        if self.vacio():
            self.raiz = nuevo_nodo
        else:
            # Si el árbol no esta vacio
            actual_nodo = self.raiz
            while actual_nodo is not None:
                padre_nodo = actual_nodo
                if nuevo_nodo.getValor() < actual_nodo.getValor():
                    actual_nodo = actual_nodo.getIzquierdo()
                else:
                    actual_nodo = actual_nodo.getDerecho()
            if nuevo_nodo.getValor() < padre_nodo.getValor():
                padre_nodo.setIzquierdo(nuevo_nodo)
            else:
                padre_nodo.setDerecho(nuevo_nodo)

            nuevo_nodo.setPadre(padre_nodo)

    def mostrarNodo(self, actual_nodo):
        if actual_nodo is not None:
            if actual_nodo.getIzquierdo()  is not None:
                print(str(actual_nodo.getValor()) +
                      " izq(" + str(actual_nodo.getIzquierdo().getValor()) + ")",end=" ")
            if actual_nodo.getDerecho() is not None:
                print(str(actual_nodo.getValor()) +
                      " der(" + str(actual_nodo.getDerecho().getValor()) + ")")
            self.mostrarNodo(actual_nodo.getIzquierdo())
            self.mostrarNodo(actual_nodo.getDerecho())

    def mostrarArbol(self):
        if self.raiz is not None:
            print(str(self.raiz.getValor()) + " (raiz)")
            self.mostrarNodo(self.raiz)
        else:
            print("Arbol vacio")

    def buscarNodo(self,nodo):
        valor = Nodo(nodo,None)
        if self.vacio():
            return False
        else:
            actual_nodo = self.raiz
            while actual_nodo is not None:
                if actual_nodo.getValor() == nodo:
                    return True
                if valor.getValor() < actual_nodo.getValor():
                    actual_nodo = actual_nodo.getIzquierdo()
                else:
                    actual_nodo = actual_nodo.getDerecho()   
        return False

    def insertarNodoUnico(self, valor):
        n_nodo = Nodo(valor,None)
        if self.buscarNodo(n_nodo.getValor()):
            print("El nodo ya existe no puede insertarse")
        else:
            self.insertar(valor)
            print("El valor se ha insertado")

    def inOrden(self):

        if actual.vacio():
            return None

        actual = self.raiz
        while actual.getIzquierdo is not None:
            actual = actual.getIzquierdo()
        if actual.getDerecho() is not None:
            actual = actual.getDerecho()
            while actual.getIzquierdo():
                actual = actual.getIzquierdo()
        else:
            while actual.getPadre() is not None and actual == actual.getPadre().getDerecho():
                actual = actual.getPadre()


    def inOrden(self):
        def inOrdenAux(nodo):
            if nodo != None:
                inOrdenAux(nodo.getIzquierdo())
                print(nodo.getValor(), end=" ")
                inOrdenAux(nodo.getDerecho())
        inOrdenAux(self.raiz)

    
    def eliminarNodo(self, valor):
        eliminar = Nodo(valor, None)
        if self.vacio():
            return None
        actual = self.raiz
        while actual.getIzquierdo() is not None:
            if actual.getValor() == valor:
                if actual.getIzquierdo() is None and actual.getDerecho() is None:
                    if actual.getPadre().getIzquierdo() == valor:
                        actual.getPadre().setIzquierdo(None)
                    elif actual.getPadre().getDerecho() == valor:
                        actual.getPadre().setDerecho(None)

                elif actual.getIzquierdo() is None or actual.getDerecho() is None:
                    if actual.getIzquierdo() is not None and actual.getDerecho() is None:
                        actual.getPadre().setIzquierdo(actual.getIzquierdo())
                    else:
                        actual.getPadre().setDerecho(actual.getDerecho())
            elif eliminar.getValor() < actual.getValor():
                    actual = actual.getIzquierdo()
            else:
                actual = actual.getDerecho()

    def eliminarNodo2(self, v1):
        valor = Nodo(v1, None)
        actual = self.raiz
        while actual is not None:
            if actual.getValor() == v1:
                if actual.getIzquierdo() is None and actual.getDerecho() is None:
                    if actual.getValor() < actual.getPadre():
                        actual.getPadre().setIzquierdo(None)
                        return "Valor borrado"
                    else:
                        actual.getPadre().setDerecho(None)
                        return "Valor borrado"
            if valor.getValor() < actual.getValor():
                actual_nodo = actual.getIzquierdo()
            else:
                actual_nodo = actual.getDerecho()  