#Crear una función que reciba una lista de numeros enteros y retorne su promedio.
#Importar y usar la funcion creada en el punto anterior.
import ejercicio14
def promedio (lista):
    c = 0
    for i in range (len(lista)):
        c = c + lista[i]
    return c / len(lista)

l_num= ejercicio14.generar_lista()
prom = promedio(l_num)
print(" EL PROMEDIO DE LA LISTA ES  : ", prom)
