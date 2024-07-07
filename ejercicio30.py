# Se debera crear una funcion y un test para probar dicha funcion como se plantearon en 
# los ejercicios anteriores (26, 27, y 28). La funcion debera recibir 
# dos numeros enteros y retornar su division. No olvidar crear el test con los casos de prueba

def dividir_numeros(numero1: int, numero2: int)->int:
	if numero1 == numero2 == 0 or numero2 == 0 :
		print ("DIVISION NO DIVISIBLE POR CERO ")
	else:
		return numero1 / numero2
if __name__ == "__main__" :
	resultado = dividir_numeros(64, 3)
	print(resultado)
