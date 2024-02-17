#Crear una función recursiva que devuleva los 100 primeros numero de Fibonacci.
def fibonacci(num1,num2,cantidad):
    if  (cantidad - 2) == 0 :
        print (num1)
        print (num2)
        print ("  -- FIN --")
    else :
        print ( num1 )
        return  fibonacci(num2,num1+num2,cantidad-1)

valor = int (input("ingrese cantidad  de numeros fibonacci  : "))
fibonacci(0,1,valor)
        
