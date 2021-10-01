# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
root = Tk()
root.title("Calculadora")
root.geometry("270x400")

# Variables globales
i=0
linea=1
columna=0

# Funciones
def borrar():
    eTexto.delete(0,END)
    
def evaluar():
    global i
    global linea
    global columna

    columna+=1
    linea=0
    
    resultado=eval(eTexto.get())
    indicel=str(linea)
    indicec=str(columna)
    historicoTexto.insert("indicel.indicec",resultado)
    #historicoTexto.insert(indice,resultado)
    
    eTexto.delete(0,END)
    eTexto.insert(0,resultado)
    i=0

def poner_texto(valor):
    global i
    indice=str(float(i+1))
    valorTexto=str(valor)
    eTexto.insert(i,valor)
    historicoTexto.insert(indice,valor)
    i+=1
    
# Historico
historicoTexto=Text(root, height=5, width=30)
historicoTexto.grid(row=0, column=0, padx=5, pady=5, columnspan=4)

# Entrada
eTexto=Entry(root, width=40)
eTexto.grid(row=1, column=0, padx=5, pady=5, columnspan=4)

# Botones
boton1=Button(root, text="1",command=lambda:poner_texto(1), width=5, height=2)
boton2=Button(root, text="2",command=lambda:poner_texto(2), width=5, height=2)
boton3=Button(root, text="3",command=lambda:poner_texto(3), width=5, height=2)
boton4=Button(root, text="4",command=lambda:poner_texto(4), width=5, height=2)
boton5=Button(root, text="5",command=lambda:poner_texto(5), width=5, height=2)
boton6=Button(root, text="6",command=lambda:poner_texto(6), width=5, height=2)
boton7=Button(root, text="7",command=lambda:poner_texto(7), width=5, height=2)
boton8=Button(root, text="8",command=lambda:poner_texto(8), width=5, height=2)
boton9=Button(root, text="9",command=lambda:poner_texto(9), width=5, height=2)
boton0=Button(root, text="0",command=lambda:poner_texto(0), width=13, height=2)

boton_borrar=Button(root, text="Ac",command=borrar, width=5, height=2)
boton_parentesis1=Button(root, text="(",command=lambda:poner_texto("("), width=5, height=2)
boton_parentesis2=Button(root, text=")",command=lambda:poner_texto(")"), width=5, height=2)
boton_punto=Button(root, text=".",command=lambda:poner_texto("."), width=5, height=2)

boton_dividir=Button(root, text="/",command=lambda:poner_texto("/"), width=5, height=2)
boton_multip=Button(root, text="*",command=lambda:poner_texto("*"), width=5, height=2)
boton_sumar=Button(root, text="+",command=lambda:poner_texto("+"), width=5, height=2)
boton_restar=Button(root, text="-",command=lambda:poner_texto("-"), width=5, height=2)

boton_igual=Button(root, text="=",command=lambda:evaluar, width=5, height=2)


# Posición Botones
boton1.grid(row=5, column=0, padx=5, pady=5)
boton2.grid(row=5, column=1, padx=5, pady=5)
boton3.grid(row=5, column=2, padx=5, pady=5)
boton4.grid(row=4, column=0, padx=5, pady=5)
boton5.grid(row=4, column=1, padx=5, pady=5)
boton6.grid(row=4, column=2, padx=5, pady=5)
boton7.grid(row=3, column=0, padx=5, pady=5)
boton8.grid(row=3, column=1, padx=5, pady=5)
boton9.grid(row=3, column=2, padx=5, pady=5)
boton0.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

boton_borrar.grid(row=2, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=2, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=2, column=2, padx=5, pady=5)
boton_punto.grid(row=6, column=2, padx=5, pady=5)

boton_dividir.grid(row=2, column=3, padx=5, pady=5)
boton_multip.grid(row=3, column=3, padx=5, pady=5)
boton_sumar.grid(row=4, column=3, padx=5, pady=5)
boton_restar.grid(row=5, column=3, padx=5, pady=5)

boton_igual.grid(row=6, column=3, padx=5, pady=5)


root.mainloop()





