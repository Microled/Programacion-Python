from tkinter import *
tk = Tk()
ventana = Frame(tk, relief=RIDGE, borderwidth=2)
ventana.pack(fill=BOTH, expand=1)
tk.title("Saludo")
tk.geometry("300x200")
etiqueta=Label(ventana,text="Python GUI").pack(fill=X, expand=1)
boton=Button(ventana, text="Salir", command=tk.destroy).pack(side=BOTTOM)
tk.mainloop()

