"""
	autor: jecueva11
	Programación Funcional:
		
"""
# importación de librería
import csv

# método para la lectura del archivo csv
def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

# with para abrir y cerrar archivos
with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata)))


# midata = open("data/data-estudiantes.csv") # en usos de grandes volúmenes de \
	# datos es necesario cerrar el archivo *.

# print(list(lineas(midata)))

# midata.close() 