from tkinter import *
main = Tk()
barra_menu = Menu(main)
main.config(menu=barra_menu)

archivoMenu = Menu(barra_menu, tearoff=0)
editarMenu = Menu(barra_menu, tearoff=0)
ayudaMenu = Menu(barra_menu, tearoff=0)

barra_menu.add_cascade(label="Archivo", menu=archivoMenu)
barra_menu.add_cascade(label="Editar", menu=editarMenu)
barra_menu.add_cascade(label="Ayuda", menu=ayudaMenu)

mainloop()