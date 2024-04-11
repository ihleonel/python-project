#Crear una funcion que genere una matriz cuadrada de 10 filas y 10 columnas de números aleatorios.
#Importar y usar la funcion creada en el punto 14.
import ejercicio14
def generar_matriz(lista):
	return [lista[(ind*10)-10:ind*10] for ind in range(1,11)] 
	#ind = "indice" Se recorre la lista de a 10 elemento para generar la matriz  
#matriz = generar_matriz(ejercicio14.generar_lista())
#print(matriz)