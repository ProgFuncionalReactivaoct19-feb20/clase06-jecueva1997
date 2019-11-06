"""
	autor: jecueva11
	Programación Funcional:
		
"""
# importación de librería
import csv

# def lineas(archivo):
#	return csv.reader(archivo, delimiter=";")

# metodo para la lectura del archivo pero en Diccionario
def lineasDiccionario(archivo):
	return csv. DictReader(archivo, delimiter=";")

# with para abrir y cerrar archivos
with open("data/data-estudiantes.csv") as midata:
	# impresión de resultados de la posición de los nombres  
	print(list(map(lambda x: list(x.items())[0][1], lineasDiccionario(midata))))