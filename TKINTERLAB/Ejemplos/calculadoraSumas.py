from tkinter import *
main = Tk()

n1 = StringVar()
n2 = StringVar()
rpta = StringVar()

def sumar():
    rpta.set(float(n1.get())+float(n2.get()))

def limpiar():
    n1.set("")
    n2.set("")
    rpta.set("")

Label(main, text="Valor 1: ").grid(row=0, column=0)
Entry(main, justify="center", textvariable=n1).grid(row=0, column=1)

Label(main, text="Valor 2: ").grid(row=1, column=0)
Entry(main, justify="center", textvariable=n2).grid(row=1, column=1)

Label(main, text="Respuesta: ").grid(row=2, column=0)
Entry(main, justify="center", textvariable=rpta).grid(row=2, column=1)

Button(main, text="Sumar", command=sumar).grid(row=4, columnspan=2)
Button(main, text="Limpiar", command=limpiar).grid(row=5, columnspan=2)

mainloop()
