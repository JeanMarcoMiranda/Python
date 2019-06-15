from tkinter import *

def crearEtiqueta():
    Label(main, text="Etiqueta dinamica creada").pack()

main = Tk()
Button(main, text="Clic para probar", command=crearEtiqueta).pack()

mainloop()