#Crear una función que te permita calcular el área de un triángulo.
def  area_triangulo(base,altura) :
    return (base*altura)/2

a = int (input("ingrese altura : "))
b = int (input("ingrese base : "))
area = area_triangulo(a,b)
print ("el area dek triangulo es ",area)
