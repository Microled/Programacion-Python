# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Pitágoras
Escriba un programa que reciba como entrada las longitudes de los dos catetos 
a y b de un triángulo rectángulo, y que entregue como salida el largo 
de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
"""
import math
print("##################################")
print("#           Pitágoras            #")
print("##################################")
      
a=int(input("Introducir cateto a: "))
b=int(input("Introducir cateto b: "))


print("La hipotenusa 'c' es: %f"%math.sqrt(a**2+b**2))

      
