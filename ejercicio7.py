#Crear una funcion que reciba un numero entero y lo devulva como un string.
def cambio_NxS(numero):
    return str(numero)

num = int (input("ingrese numero entero : "))
cadena = cambio_NxS(num)
print(cadena , type (cadena) )

