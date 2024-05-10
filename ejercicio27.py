# Se deberá crear una función que reciba una matriz cuadrada nxn y retorne la misma matriz
# pero rotada 90 grados en sentido de las agujas del reloj.
# Ver los casos de prueba en el archivo "test_ejercicio27.py".
# Correr el test python3 test_ejercicio27.py se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".
import copy
from ejercicio26 import comparar_matrices_cuadradas
def es_matriz_cuadrada(matriz: list)-> bool:
    cantidad_de_filas = len(matriz)
    for lista in matriz:
        if len(lista) != cantidad_de_filas : 
            return False

    return True

def rotar_matriz_cuadrada(matriz: list):
    if es_matriz_cuadrada(matriz) == True:
        copia = copy.deepcopy(matriz)
        tamaño = len(copia)
        j = 0
        for i in range(tamaño-1,-1,-1):        
            for x in range(tamaño):
                copia[x][j] = matriz[i][x]
            j += 1 
        return copia
    else :
        print("--- NO ES UNA MATRIZ CUADRADA ---")

if __name__ == '__main__':
    m = [[1,2,3,4],[2,5,3,4],[1,2,3,4],[6,5,4,3]]
    r = rotar_matriz_cuadrada(m)
    print(m,"\n\n",r)
