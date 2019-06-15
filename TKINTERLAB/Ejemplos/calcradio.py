from tkinter import *
main = Tk()

opcion = StringVar()
n1 = StringVar()
n2 = StringVar()
rpta = StringVar()

def sumar():
    rpta.set(float(n1.get()) + float(n2.get()))

def restar():
    rpta.set(float(n1.get()) - float(n2.get()))

def multiplicar():
    rpta.set(float(n1.get()) * float(n2.get()))

Label(main, text="Valor 1: ").grid(row=0, column=0)
Entry(main, justify="center", textvariable=n1).grid(row=0, column=1)

Label(main, text="Valor 2: ").grid(row=1, column=0)
Entry(main, justify="center", textvariable=n2).grid(row=1, column=1)

Radiobutton(main, text="Sumar", variable=opcion, value=1, command=sumar).grid(row=2, column=1)
Radiobutton(main, text="Restar", variable=opcion, value=2, command=restar).grid(row=3, column=1)
Radiobutton(main, text="Multiplicar", variable=opcion, value=3, command=multiplicar).grid(row=4, column=1)

Label(main, text="Respuesta: ").grid(row=5, column=0)
Entry(main, justify="center", textvariable=rpta).grid(row=5, column=1)

mainloop()
