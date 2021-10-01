print("#############################")
nom=input("Introduce tu nombre:")
if nom=="Labbox":
    dato=1
elif nom=="Intexteis":
    dato=2
elif nom=="Interface":
    dato=3
else:
    dato=4

while(dato>0 and dato<4):
    print("Hola %s que tal hoy?"%nom)
    break

print("Te has pasado de indice")
