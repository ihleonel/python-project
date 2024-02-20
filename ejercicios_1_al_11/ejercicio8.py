#Crear una funcion que tranforma años en días.
def Transformar_AxD(anio):
    return 365 * anio

time = int(input("ingrese anio : "))
print ("transformado en dias son : ",Transformar_AxD(time))
