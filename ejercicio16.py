# Crear una función que reciba una lista de numero enteros y retorne el maximo de la lista.
# Importar y usar la funcion creada en el punto 14.
import ejercicio14
def numero_mayor(lista):
    return max(lista)

array = ejercicio14.generar_lista()
print ("el mayor numero de la lista es : ",numero_mayor(array))
