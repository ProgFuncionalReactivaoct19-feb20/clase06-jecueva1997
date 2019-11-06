"""
	autor: jecueva11
	Programación Funcional:
		
"""
# importación de librería
import csv

# método para dar lectura al crchivo csv
def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

# with para abrir y cerrar archivos
with open("data/data-estudiantes.csv") as midata:
	# impresión de datos que no tenga "email"
	print(list(filter( lambda x: x != "email", map(lambda x: x[1], \
		lineas(midata)))))


	# resultado1 = map(lambda x: x[1], lineas(midata))
	# resultado2 = filter( lambda x: x != "email", resultado1)

	# print(list(resultado2))

