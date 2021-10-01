# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:20:20 2018

@author: microled
Círculos¶
Escriba un programa que reciba como entrada el radio de un círculo 
y entregue como salida su perímetro y su área:
"""
import math

print("################################")
print("#        RADIO CIRCULO         #")
print("################################")

radio=int(input("Introduce el rádio de un círculo: "))

perimetro=(math.pi *radio)*2
area= math.pi* radio**2
print ("Perimetro: ",perimetro)
print ("Area: ",area)