# Se deberá crear una función que reciba una matriz cuadrada nxn y retorne la misma matriz
# pero rotada 90 grados en sentido de las agujas del reloj.
# Ver los casos de prueba en el archivo "test_ejercicio27.py".
# Correr el test python3 test_ejercicio27.py se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".
import copy
from ejercicio26 import comparar_matrices_cuadradas
def rotar_matriz_cuadrada(matriz: list):
    copia = copy.deepcopy(matriz)
    tamaño = len(matriz)
    for i in range(tamaño):
        lista = matriz[2-i]
        for x in range(tamaño):
            copia[x][i] = lista[x]
    
    return copia
