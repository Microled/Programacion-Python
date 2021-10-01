# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Mayusculizador

Al hacer clic en el botón Mayusculizar, el texto del campo superior 
debe ser convertido a mayúsculas:
Al hacer clic en Minusculizar, debe ser convertido a minúsculas.
Al hacer clic en Limpiar, debe borrarse el contenido del campo.

"""

from tkinter import *
from tkinter import ttk
root=Tk()

def Mayusculizar():
    maytexto=texto.get()
    texto.set((maytexto.upper()))
    

def Minisculizar():
    maytexto=texto.get()
    texto.set((maytexto.lower()))

def Limpiar():
    texto.set("")
    

texto=StringVar()
texto.set("Introduce texto")

entTexto=Entry(root,textvariable=texto).pack()
btnMayusculizar=ttk.Button(root,text="Mayusculizar",command=Mayusculizar).pack()
btnMinusculizar=ttk.Button(root,text="Minisculizar",command=Minisculizar).pack()
btnLimpiar=ttk.Button(root,text="Limpiar",command=Limpiar).pack()
btnSalir=ttk.Button(root,text="Salir",command=root.destroy).pack()

root.mainloop()



      
