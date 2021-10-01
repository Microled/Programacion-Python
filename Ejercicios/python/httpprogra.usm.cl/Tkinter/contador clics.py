# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Contador de clics
Escriba un programa con la siguiente interfaz:

Cada vez que se haga clic en el botón +1, el número en la parte superior 
debe aumentar en uno

"""

from tkinter import *
root=Tk()

def contador():
    valor=numero.get()
    valor+=1
    numero.set(valor)
    
root.title("t")
numero=IntVar()
numero.set(0)
lblNumero=Label(root,textvariable=numero).pack()
btnMasuno=Button(root, text="+1",command=contador).pack()
btnSalir= Button(root,text="Salir",command=root.destroy).pack()

root.mainloop()



      
