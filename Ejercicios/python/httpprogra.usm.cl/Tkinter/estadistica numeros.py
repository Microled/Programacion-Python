# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 02:02:26 2018

@author: microled

Estadísticas de números
Escriba un programa que muestre la suma, el promedio, 
el máximo y el mínimo de una secuencia de números.

Al hacer clic en Calcular, deben actualizarse 
los mensajes en la parte inferior.

"""

from tkinter import *
root = Tk()

def calcular():
    #suma=0  #Inicializar valor suma a 0 pora evitar errores de sumas
    numeros=[] # Lista números para poder hacer función max y min
    
    for i in range(12):
        #Solo si no usamos la funciones de lista sum
        #suma=suma+int(listnumero[i].get())# Suma los valores de entrada
        numeros.append(int(listnumero[i].get()))# añado a lista numeros contenido de entradas
   
    ''' Existe una segunda opción que trata de crear los labels sin textvariable
        de este modo aparecen los labels de Suma: promedio: ,etc y al aplicar la 
        función en lugar de enviar los textvariables, se crean los labels de nuevo
        con los valores correctos Suma:15, etc...'''
        
    #print(round(sum(numeros)/len(numeros),3))
    listlabeltxt[0].set("Suma: "+str(sum(numeros))) # Cambio el texto label a Suma
    listlabeltxt[1].set("Promedio: "+str(round(sum(numeros)/len(numeros),3)))# cambio el texto de label a Promedio
    listlabeltxt[2].set("Máximo: "+str(max(numeros))) # cambio el texto de label a funcion max
    listlabeltxt[3].set ("Mínimo: "+ str(min(numeros))) # cambio el texto de label a funcion min
    
root.title("Numeros")
root.geometry("125x360")
root.resizable(width=False,height=False) # Evito que se redimensione la pantalla

listentrada=[] #Crear lista listentrada para nombrar los Entry
listnumero=[] # Crear lista listnumero para dar nombre al contenido entry
listlabeltxt=[""]*4#,"Promedio: ","Máximo: ","Mínimo: "] # Crear lista para los textvariables de los labels
#Aunque no es necesário crear esta lista, lo podemos hacer a modo de organización
#listlabel=["Suma: ","Promedio: ","Máximo: ","Mínimo: "] # Introducimos los valores de 
                                                        # los nombres de los labels
''' Inicializamos el for para crear los 12 Entry, en cada línea se le añade
    a listaentrada el string "entrada" más el valor de i+1 (para no empezar en 0)
    y lo mismo con listnumero para gestionar el textvariable, aprovechamos el 
    bucle para inicializar los valores de listnumero a IntVar()'''
    
for i in range(12):                         
    listentrada.append("entrada"+str(i+1))
    listnumero.append("numero"+str(i+1))
    listnumero[i]=IntVar()
    listentrada[i]=Entry(root,textvariable=listnumero[i]).grid(row=i+1,column=0)

btnCalcular=Button(root,text="Calcular",command=calcular,width=12).grid(row=14,column=0)
#   Realizamos la misma operación que con los Entry, pero con los labels ()

for i in range(4):
    listlabeltxt[i]=StringVar()
    Label(root,textvariable=listlabeltxt[i]).grid(row=15+i,column=0)
    #Solo si queremos usar los nombres de Labels
    #liststlabel[i]=Label(root,textvariable=listlabeltxt[i]).grid(row=15+i,column=0)

root.mainloop()

