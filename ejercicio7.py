"""
	autor: jecueva11
	Programación Funcional:
"""
# importación de librería
import csv

# metodo para llamar el archivo y guardarlo en un Diccionario 
def lineasDiccionario(archivo):
	return csv. DictReader(archivo, delimiter="\t")

# para que se abra y se cierre el archivo
with open("data/trabajadores.csv") as midata:
	# almacenamiento de los archivos en una lista
	linea = list(lineasDiccionario(midata))
	
	# impresión de países tengan en su nombre una longitud mayor a 10
	print("\nPaises que tengan en su nombre una longitud mayor a 10:")
	print(list(filter(lambda x: len(list(x.items())[2][1])>10, linea))) 

	# impresión de resultados ordenados por el dia de nacimiento
	print("\nDatos ordenados por el día de nacimiento:")
	print(sorted(linea, key = lambda x: list(x.items())[1][1].split("-")[2]))
	