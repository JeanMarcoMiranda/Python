class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        self.listaVertices = {}

    def agregarVertice(self,clave):
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def cantidadVertices(self):
        count = 0
        for v in self.listaVertices:
            count += 1
        return count

    def cantidadAristas(self):
        count = 0
        for v in self:
            for a in v.obtenerConexiones():
                count += 1
        return count

    def sumaPonderacion(self):
        count = 0
        for v in self:
            for a in v.obtenerConexiones():
                ponderacion = v.obtenerPonderacion(a)
                count += ponderacion
        return count

    def verPodenderacionNodo(self, vertice):
        count = 0
        for v in self:
            if v.obtenerId() == vertice:
                for a in v.obtenerConexiones():
                    ponderacion = v.obtenerPonderacion(a)
                    count += ponderacion
        return count

    def verLongitud(self, v1, v2):
        a = self.listaVertices[v1]
        b = self.listaVertices[v2]
        aux = None
        cont=0
        while v2 != a.obtenerId():
            peso = 0
            for i in a.conectadoA:
                if a.obtenerPonderacion(i) > peso:
                    peso = a.obtenerPonderacion(i)
                    aux = i
            a = aux
            cont += 1
        return cont

    def verNoEnlazados(self, vertice):
        if vertice in self.obtenerVertices():
            ver = self.obtenerVertice(vertice)
            res = []
            aux = []
            for i in self.obtenerVertices():
                conexiones = self.obtenerVertice(i).obtenerConexiones()
                for f in ver.obtenerConexiones():
                    aux.append(f.obtenerId())
                if i not in aux and ver not in conexiones:
                    if i != vertice:
                        res.append(i)
                aux = []
            print(res)
        else:
            print("No existe el vertice en el Grafo")


