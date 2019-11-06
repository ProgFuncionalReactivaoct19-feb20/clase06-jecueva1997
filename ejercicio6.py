"""
	autor: jecueva11
	Programación Funcional:
		
"""
# importación de librería
import csv

# metodo para la lectura del archivo pero en Diccionario
def lineasDiccionario(archivo):
	return csv. DictReader(archivo, delimiter=";")

# with para abrir y cerrar archivos
with open("data/data-estudiantes.csv") as midata:
	# almacenamiento de los datos en una lista
	linea = list(lineasDiccionario(midata))
	# impresión de el nombre con su correo utilizando .split()
	print(list(map(lambda x: "%s-%s" %(list(x.items())[0][1].split(" ")[1], \
		list(x.items())[1][1].split(".")[0]), linea)))

	