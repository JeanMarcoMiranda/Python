from tkinter import *
main = Tk()

texto_amplio = Text(main)
texto_amplio.pack()
texto_amplio.config(width=30,height=10,font=("Consolas",12),padx=15,pady=15,selectbackground="red")

mainloop()