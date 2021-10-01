import random
list=[]
col=int(input("Introduce las columnas de la lista: "))
min=int(input("Mínimo número del random: "))
max=int(input("Máximo númerp del random: "))
for i in range(col):
    list.append(random.randint(min,max))

print(list)
