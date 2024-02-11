#Crear una función que te permita pasar horas a munutos.
def convertir_HxM(horas):
    return horas*60

time = int(input("ingrese horas :"))
print(convertir_HxM(time)," minutos ")
