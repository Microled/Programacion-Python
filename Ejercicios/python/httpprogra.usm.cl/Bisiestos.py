# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:38:24 2018

@author: microled

Años bisiestos¶
Bisiestos son los años divisibles por 4
el último año de cada siglo dejaba de ser bisiesto, 
a no ser que fuera divisible por 400

"""

print("##################################")
print("#          Años Bisiestos        #")
print("##################################")

anyo=int(input("Introducir un Año: "))

if anyo %4 == 0:
    if anyo %100==0:
        if anyo %400 !=0:
            print("El año %d no es bisiesto"%anyo)
        else:
            print("El año %d es bisiesto"%anyo)
    else:
        print("El año %d es bisiesto"%anyo)
    #print("El año %d es bisiesto"%anyo)
else:
    print("El año %d no es bisiesto"%anyo)




      
