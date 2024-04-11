#Crear una función que genere una lista de numeros entros aleatorios de 1000 elementos.
# Importar y usar la función creada en el punto anterior
import ejercicio13
def generar_lista():
    lista = list()
    for i in range(1000):
        lista.append(ejercicio13.random_x())
    return lista

#print(" ---- GENERAR LISTA DE NUMEROS ALEATORIOS ----")
#numeros = generar_lista()
#print(numeros)
