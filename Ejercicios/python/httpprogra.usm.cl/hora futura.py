# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Hora futura
Escriba un programa que pregunte al usuario la hora actual t del reloj y un 
número entero de horas h, que indique qué hora marcará el reloj 
dentro de h horas:
"""
import math
print("##################################")
print("#        Calculo Horas           #")
print("##################################")
      
hora=int(input("Introducir Hora Actual (Entero): "))
hfut=int(input("Cantidad de horas: " ))

if hfut>9:
    nhora=(hora+hfut)
    futuro=((hora+hfut)-(12*(int(nhora/10)-1)))
else:
    futuro=hora+hfut
print("En %d horas, el reloj marcará las %d"%(hfut,futuro))

      
