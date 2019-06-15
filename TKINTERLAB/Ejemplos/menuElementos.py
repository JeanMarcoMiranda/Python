from tkinter import *
main = Tk()
barra_menu = Menu(main)
main.config(menu=barra_menu)

archivoMenu = Menu(barra_menu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=main.quit())

editarMenu = Menu(barra_menu, tearoff=0)
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Pegar")

ayudaMenu = Menu(barra_menu, tearoff=0)
ayudaMenu.add_command(label="Ayuda")
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Acerca de")

barra_menu.add_cascade(label="Archivo", menu=archivoMenu)
barra_menu.add_cascade(label="Editar", menu=editarMenu)
barra_menu.add_cascade(label="Ayuda", menu=ayudaMenu)

mainloop()

