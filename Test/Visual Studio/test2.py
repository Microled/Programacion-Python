from tkinter import *
root=Tk()

Label(root, text="Nombre:").grid(ipady=5, row=0, column=0)
Label(root, text="Apellido:").grid(ipady=5, row=1, column=0)

Entry(root, width=40).grid(padx=5, row=0, column=1)
Entry(root, width=40).grid(padx=5, row=1, column=1)

Button(root, text="Aceptar", width=50).grid(padx=10,pady=10 ,row=2, column=2, columnspan=2)



root.mainloop()
