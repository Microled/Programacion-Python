# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 17:49:11 2018

@author: microled
"""

#-------------------------------------------------------------------------------
# Nombre:      Estadisticas de numeros
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from tkinter import *
 
def calcular():
    # Se agregan los elementos de las entradas a una lista normal para poder
    # obtener la suma, promeio, maximo y minimo.
    lista = []
    for i in range(len(valores)):
        lista.append(float(valores[i].get()))
 
    # Se asigna a los elementos de la lista salida los textos correspondientes.
    # Esta parte no se puede hacer con ciclos (al menos desconozco como)
    # ya que cada elemento es distintivo al resto y dificil hacerlo con un ciclo
    salida[0].set("Suma: " + str(sum(lista)))
    salida[1].set("Promedio: " + str(sum(lista) / len(lista)))
    salida[2].set("Maximo: " + str(max(lista)))
    salida[3].set("Minimo: " + str(min(lista)))
 
w = Tk()
w.title("Estadisticas de numeros")
 
valores = [0] * 12      # Lista que tendra los elementos de las entradas
salida = [0] * 4        # Lista que tendra la suma, promedio, maximo y minimo
 
# Con un ciclo se ahorra bastaaaaante codigo :D
cont=0
for i in valores:
#for i in range(12):
    valores[i] = StringVar()
    entrada = Entry(w, textvariable = valores[i])
    entrada.pack()
    cont+=1
 
boton_calcular = Button(w, text = "Calcular", command = calcular)
boton_calcular.pack()
 
# Otro ciclo para mostrar los textos tras calcular
for i in range(4):
    salida[i] = StringVar()
    salida_texto = Label(w, textvariable = salida[i])
    salida_texto.pack()
 
w.mainloop()