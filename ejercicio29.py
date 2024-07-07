 # Se debera crear una funcion y un test para probar dicha funcion como se plantearon en los 
 # ejercicios anteriores (26, 27, y 28). La funcion debera recibir dos numero enteros y retornar
 # su suma. No olvidar crear el test con los casos de prueba
def sumar_numeros(numero1, numero2) :
 	if numero1 == int(numero1) and numero2 == int(numero2) :
 		return numero1 + numero2
 	else : 
 		print ("NUMERO INVALIDADO NO ES ESTERO ")
if __name__ == '__main__':
	suma = sumar_numeros(1.00001, -2)
	print(suma)