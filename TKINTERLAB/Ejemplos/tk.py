from tkinter import *
main = Tk()
main.title("Mi primer tkinter")
main.resizable(1,1)
main.iconbitmap('imagen.ico')
#creacion de frame
frame = Frame(main, width=480, height=320)
frame.pack(fill="both", expand="1")
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")
#condiguracion de main
main.config(cursor="arrow")
main.config(bg="blue")
main.config(bd=15)
main.config(relief="ridge")
main.mainloop()

