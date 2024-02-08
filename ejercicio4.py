#Crear una función que pase minutos a segundos.
def segundos(tiempo):
    return tiempo * 60

minuto = int(input("ingrese minutos  : "))
print (minuto ," minutos  = ", segundos(minuto) , " segundos")
