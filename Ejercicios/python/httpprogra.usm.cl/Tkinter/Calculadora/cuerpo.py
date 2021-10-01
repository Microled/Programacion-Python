# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:42:58 2018

@author: Luis
"""

from tkinter import *
root=Tk()
root.geometry('200x330')
root.title("CALCULADORA")
lblPresentacion=Label(root,text="Calculadora Pruebas").grid(row=0,column=0,columnspan=6)
visor=Entry(root).grid(row=1,column=0,columnspan=6)

def number(boton):
    print(boton)

listnum=['Ce','C','<-','/','7','8','9','X','4','5','6','-','1','2','3','+','.','0',',','=']
index=0
textbtn=StringVar()

for f in range(0,5):
    for c in range(0,4):
        
        print(f,c)
        
        textbtn=listnum[index]
        #btnName=listnum[index]
        
        Button(root,textvariable=textbtn,width=3,height=2,borderwidth=8,command=lambda:number(textbtn.get())).grid(row=(f+2),column=c)
        index+=1
root.mainloop()