from tkinter import *
from tkinter import messagebox as Mensaje

main = Tk()

def test():
    #========== Nos sirve para dar solo una opcion "OK" ==========
    resultado = Mensaje.askokcancel("Salir", "¿Desea cerrar el programa?")
    if resultado:
        main.destroy()

    #========== Opcion para realizar preguntas ==========
    #resultado = Mensaje.askquestion("Salir", "¿Desea cerrar el programa?")
    #if resultado == "yes":
    #    main.destroy()

    #========== Opciones para mostrar mensajes ==========
    #Mensaje.showerror("Titulo", "Contenido")
    #Mensaje.showinfo("Titulo", "Contenido")
    #Mensaje.showwarning("Titulo", "Contenido")

Button(main, text="Mostrar mensaje", command=test).pack()

mainloop()