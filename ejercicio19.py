# Crear una funcion que reciba una matriz cuadrada y retorne la suma de su diagonal.
# Importar y usar la funcion creada en el punto anterior.
import ejercicio14
import ejercicio18
def sumar_diagonal(matriz, indice):
	if indice == 9 :
		print("\n",matriz[indice][indice])
		return matriz[indice][indice]
	else:
		print("\n",matriz[indice][indice])
		return sumar_diagonal(matriz, indice+1) + matriz[indice][indice]

lista = ejercicio14.generar_lista()
mtz = ejercicio18.generar_matriz(lista)
print(mtz[0],"\n",mtz[1],"\n",mtz[2],"\n",mtz[3],"\n",mtz[4],"\n")
print(mtz[5],"\n",mtz[6],"\n",mtz[7],"\n",mtz[8],"\n",mtz[9],"\n")
print("resultado = ",sumar_diagonal(mtz, 0))