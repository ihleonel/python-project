#Crear una funcion que reciba una lista y devulva el ultimo elemento de esa lista.
def ultimo_lista(lista):
    return lista.pop(len(lista)-1)

tam = int(input ("ingrese el tamanio de la lista :"))
print ("    ---- GENERAR LISTA ----")
lista = list()
for i in range(tam) :
    ele = input("  elemento  :  ")
    lista.append(ele)
    
print("ultimo de la lista :", ultimo_lista(lista))

