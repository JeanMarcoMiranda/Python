from tkinter import *
main = Tk()

etiqueta = Label(main,text="Nombre: ")
etiqueta.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entrada = Entry(main)
entrada.grid(row=0, column=1)
entrada.config(justify="right", state="disabled")

etiqueta2 = Label(main,text="Apellidos: ")
etiqueta2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entrada2 = Entry(main)
entrada2.grid(row=1, column=1)
entrada2.config(justify="center", show="*")

mainloop()