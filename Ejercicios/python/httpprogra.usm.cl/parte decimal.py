# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Parte decimal
Escriba un programa que entregue la parte decimal de un número real 
ingresado por el usuario.
"""
import math
print("##################################")
print("#          Parte decimal         #")
print("##################################")
numero=float(input("Introducir un número: "))

print(" El número decimal es: %.2f"%math.modf(numero)[0])


      
