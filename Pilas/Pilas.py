class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)




def verpila(p):
    while p.items != []:
        print(p.extraer())


def validaSignos(string):
    p1 = Pila()
    p2 = Pila()
    signosA = ['[','(','{']
    signosC = [']',')','}']
    coincide = False
    for i in range(0, len(string)):
        if string[i] in signosA or string[i] in signosC:
            p1.incluir(string[i])
            
    while p1.inspeccionar() in signosC:
        p2.incluir(p1.extraer())

    if p1.tamano() == p2.tamano():
        coincide = True
        while coincide == True:
            if p1.estaVacia() == False and p2.estaVacia() == False:
                sp1 = p1.extraer()
                sp2 = p2.extraer()
                if sp1 == "[" and sp2 == "]":
                    continue
                elif sp1 == "(" and sp2 == ")":
                    continue
                elif sp1 == "{" and sp2 == "}":
                    continue
                else:
                    coincide = False
            else:
                break
        return coincide
    else:
        return coincide

def invertirPila(p):
    Npila = Pila()
    while p.items != []:
        Npila.incluir(p.extraer())
    return Npila

def unirPila(p1,p2):
    Np = Pila()
    while p1.estaVacia() == False or p2.estaVacia() == False:
        if p1.estaVacia() == True and p2.estaVacia() == False:
            Np.incluir(p2.extraer())
        elif p1.estaVacia() == False and p2.estaVacia() == True:
            Np.incluir(p1.extraer())
        else:
            Np.incluir(p1.extraer())
            Np.incluir(p2.extraer())
    return Np

def postfija(cadena):
    operadores = ["+","-","/","*"]
    res = Pila()
    for i in range(0,len(cadena)):
        if cadena[i] in operadores:
            v1 = res.extraer()
            v2 = res.extraer()
            vIn = 0
            if cadena[i] == "+":
                vIn = v1 + v2
            elif cadena[i] == "-":
                vIn = v2 - v1
            elif cadena[i] == "/":
                vIn = v2 / v1
            else:
                vIn = v1 * v2
            res.incluir(vIn)
            continue
        else:
            num = int(cadena[i])
            res.incluir(num)

    if res.tamano() > 1:
        return "Error"
    else:
        return res.extraer()
            