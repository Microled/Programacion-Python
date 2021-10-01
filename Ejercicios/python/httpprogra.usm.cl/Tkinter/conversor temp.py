# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Conversor de temperatura
Escriba un programa para convertir grados Fahrenheit a Celsius. 
Al hacer clic en el botón, debe actualizarse el mensaje 
en la parte inferior de la ventana.
"""

from tkinter import *
from tkinter import ttk

def conversor():
    valor=((grados.get()-32)*5)/9
    convert=(str(grados.get())+' F = '+ str(round(valor,2))+' C')
    gradosconv.set(convert)
    
    


root=Tk()

root.title("Convertit F to C")
root.geometry('210x90')
grados=DoubleVar()
#grados.set("Introduce Faherenheit")
gradosconv=StringVar()
gradosconv.set("... F = ... C")
entrada=Entry(root,textvariable=grados,width=30,justify="center").pack()
btnConversor=Button(root,text="F -> C",command=conversor,width=15,
                    justify="center").pack()
lblConversor=Label(root,textvariable=gradosconv,justify="center").pack()

root.mainloop()



      
