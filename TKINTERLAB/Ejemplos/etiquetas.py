from tkinter import *
main = Tk()

texto = StringVar()
texto.set("Nuevo Texto")

Label(main, text="Eiqueta 1").pack(anchor="nw")
etiquetaObjeto = Label(main, text="Etiqueta 2")
etiquetaObjeto.pack(anchor="center")
Label(main, text="Etiquta 3").pack(anchor="se")
etiquetaObjeto.config(bg="green", fg="blue", font=("Verdana",24))
etiquetaObjeto.config(textvariable=texto)

main.mainloop()