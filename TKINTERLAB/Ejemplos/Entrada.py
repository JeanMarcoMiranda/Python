from tkinter import*
main = Tk()

frame = Frame(main)
frame.pack()
frame.config(bg="blue")

entrada = Entry(frame)
entrada.pack(side="right")

etiqueta = Label(frame, text="Nombre: ")
etiqueta.pack(side="left")

frame2 = Frame(main)
frame2.pack()
frame2.config(bg="red")

entrada2 = Entry(frame2)
entrada2.pack(side="right")

etiqueta2 = Label(frame2, text="Apellidos: ")
etiqueta2.pack(side="left")


mainloop()