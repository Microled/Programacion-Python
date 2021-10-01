# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:04:47 2018

@author: microled
Tabla de multiplicar¶
Escriba un programa que muestre la siguiente tabla de multiplicar gráficamente
----------------------------
| 1 2 3 4 5 6 7 8 9 10      |
| 2 4 6 8 10 12 14 16 18 20 |
| 3 6 9 12 15 18 21 24 27 30|
...
 10 20 30 40 50 60 70 80 90 100|
"""

from tkinter import *
root = Tk()
root.title("Tabla")

''' Ejercício realizado en consola sin gráficos
for i in range(1,11):
    for j in range(1,11):
        print(j * i,end=" ")
    print("\n")
'''
for i in range (1,11):
    for j in range (1,11):
        Label(root,text=j*i).grid(row=i,column=j)
    

root.mainloop()    