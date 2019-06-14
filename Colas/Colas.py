class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

def verCola(cola):
    while cola.items != []:
        print(cola.avanzar()," ",end="")

def invertirCola(cola):
    cInv = Cola()

    while cola.items != []:
        tope = cola.avanzar()
        cInv.agregar(tope)
        while tope != cInv.items[len(cInv.items)-1]:
            cInv.agregar(cInv.avanzar())
    return cInv

def ordenarCola(cola):
    numeros = Cola()
    letras = Cola()

    while cola.items != []:
        if type(cola.items[len(cola.items) - 1]) is int:
            numeros.agregar(cola.avanzar())
        else:
            letras.agregar(cola.avanzar())
    if numeros.items != []:
        while numeros.items != []:
            cola.agregar(numeros.avanzar())
    if letras.items != []:
        while letras.items != []:
            cola.agregar(letras.avanzar())
    return cola

def unirColas(c1,c2):
    c2I = invertirCola(c2)
    while c2I.items != []:
        c1.agregar(c2I.avanzar())
    return c1 

def intercambiarColas(c1,c2):
     t1 = c1.tamano()
     t2 = c2.tamano()
     while t1 != 0 or t2 != 0:
        if t1 != 0:
            c2.agregar(c1.avanzar())
        if t2 != 0:
            c1.agregar(c2.avanzar())
        t1 -= 1
        t2 -= 1

     verCola(c1)
     print("\n","-"*15)
     verCola(c2)    