# Crear una funcion que reciba una lista de numero enteros y retorne la misma lista orndenada de mayor a menor.
# Importar y usar la funcion creada en el punto 14.

import ejercicio14
def ordenar_lista(lista):
	return lista.sort(reverse = True)

array = ejercicio14.generar_lista()
ordenar_lista(array)
print("\n\n-----LISTA ORDENADA DESCENDENTE----\n\n", array)