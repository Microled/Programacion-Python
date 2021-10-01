# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:30:23 2018

@author: microled
Cachipún
Escriba un programa para jugar cachipún contra el computador.
La interfaz debe ser la siguiente:

Cada vez que usted haga clic en un botón, el computador debe elegir al azar
su jugada (piedra, papel o tijera), y mostrarla en la etiqueta
(«El computador eligió...»).
Además, hay que actualizar el marcador que indica cuántas veces
ha ganado cada uno. En el ejemplo de la imagen,
el humano ha ganado cuatro veces, y el computador una.

La regla para saber quién ganó es:
    piedra le gana a tijera, tijera le gana a papel, papel le gana a piedra.
    El resto de las combinaciones posibles son todas empates.

"""

from tkinter import *
import random
import time
root=Tk()

user=0
pc=0

def jugar(eleccUser):
    global user, pc
    list=['Piedra','Papel','Tijera']
    eleccPc=random.randrange(3)
    #print(eleccPc, list[eleccPc])
    if eleccUser=='Piedra' and list[eleccPc]=='Tijera':
        user+=1
    elif eleccUser=='Tijera' and list[eleccPc]=='Papel':
        user+=1
    elif eleccUser=='Papel' and list[eleccPc]=='Piedra':
        user+=1
    elif eleccUser==list[eleccPc]:
        eleccionpc.set("Elección Empatada")
        pass
    else:
        pc+=1

    eleccionpc.set("El computador elegió "+list[eleccPc])
    contador.set("User: "+ str(user) + " PC: " + str(pc))
    #print("Tu has elegido: ",eleccUser)
    #print("user %d Pc %d"%(user,pc))


root.title("Capuchin")
root.geometry("230x100")

contador=IntVar()
contador.set("Contador")
eleccionpc=StringVar()
eleccionpc.set("El computador eligió ....")

lblContador = Label(root,textvariable=contador,justify="center",font=("Arial Bold", 20)).pack()
lbltanteopc = Label(root,textvariable=eleccionpc,justify="center", font=("Arial Bold",11),fg="RED").pack()
btnPiedra= Button(root, text= "Piedra",width=8,command=lambda:jugar("Piedra")).pack(side=LEFT, padx=10)
btnPapel= Button(root, text= "Papel", width=8,command=lambda:jugar("Papel")).pack(side=LEFT)
btnTijera= Button(root, text= "Tijera", width=8,command=lambda:jugar("Tijera")).pack(side = LEFT, padx=10)
root.mainloop()