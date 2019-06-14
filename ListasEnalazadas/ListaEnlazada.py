class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        
    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato
     #En la siguiente funcion sirve para asignar punteros
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def mostrarDatos(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
            
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado

    def remover(self, item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())

    def eliminarFinal(self):

        if self.estaVacia() == True:
            print("Esta lista esta vacia")
        
        elif self.cabeza.siguiente == None:

            self.cabeza = None
            print("Elemento eliminado, ahora esta lista esta vacia")

        else:

            actual = self.cabeza
            previo = None

            while actual.siguiente is not None:
                previo = actual
                actual = actual.obtenerSiguiente()
            previo.siguiente = None
            print("Ultimo elemento eliminado")

    def insertarFinal(self,item):
        item = Nodo(item)
        actual  = self.cabeza
        while actual.siguiente != None:
            actual = actual.obtenerSiguiente()

        actual.asignarSiguiente(item)
        actual.siguiente.asignarSiguiente(None)
        if item.siguiente == None:
            print("Valor Insertado")

    def insertarMedio(self,item,pos):
        item = Nodo(item)
        previo = None
        actual = self.cabeza
        cont = 0
        if pos <= self.tamano():
            if self.estaVacia() == True:
                    item.asignarSiguiente(actual)
                    self.cabeza = item
            else:
                while cont != pos:
                    cont += 1
                    previo = actual
                    actual = actual.obtenerSiguiente()
                previo.asignarSiguiente(item)
                item.asignarSiguiente(actual)
                print("Valor insertado")
        else:
            print("Esa posicion no existe en esta lista")

    def indicePrimero(self,vBuscar):
        cont = 0
        actual = self.cabeza
        encontrado = False
        if self.estaVacia() != True:
            while cont < self.tamano():
                cont+=1
                if actual.obtenerDato() == vBuscar:
                    encontrado = True
                    break
                else:
                    actual = actual.obtenerSiguiente()
            if encontrado == False:
                return 0
            else:
                return cont
        else:
            return "Esta lista esta vacia"

    def indiceUltimo(self, item):
        cont = 0
        actual = self.cabeza
        pos = 0
        if self.estaVacia() != True:
            while cont < self.tamano():
                cont += 1
                if actual.obtenerDato() == item:
                    pos = cont
                actual = actual.obtenerSiguiente()
            if pos != 0:
                return pos
            else:
                return 0
        else:
            return "Esta lista esta vacia"

    def cortar(self, indice):
        cont = 1
        actual = self.cabeza

        while cont < self.tamano():
            if cont == indice:
                actual.asignarSiguiente(None)
                break
            else:
                actual = actual.obtenerSiguiente()
                cont += 1
