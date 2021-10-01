def crealista():
	print("Hemos creado la lista \"lista\" ")
	
while True:
	print("Introduce tu selección para las listas: ")
	print("0- Crear lista")
	print("1- Borrar lista")
	print("2- Introducir contenido lista")
	print("3- Mostrar contenido lista")
	print("4- Añadir dato a final de lista")
	print("5- Añadir dato en posición determinada de lista")
	print("6- Eliminar dato de final de lista")
	print("7- Eliminar dato en posición deterrminada de lista")
	print("8- Eliminar todo el contenido de lista")
	print("9- Contar elemento en lista")
	print("10- Mostrar posición elemento en lista")
	print("11- Longitud lista")
	print("99- Fin")

	seleccion=int(input("Introduce tu selección: "))
	if seleccion==0:
		crealista()
		lista=[]
		print("El nombre de la lista es: lista")

	if seleccion==2:
		datoslista()

	if seleccion==99:
		break


