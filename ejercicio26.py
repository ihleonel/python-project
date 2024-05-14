# Se deberá crear una función que reciba dos matrices cuadradas como parametros 
# y debara retornar si son equivalentes o no. 
# Para determinar si la funcion es correcta se debera correr el test python3 test_ejercicio26.py
# y se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".
def comparar_matrices_cuadradas(matriz_1, matriz_2):
    if len(matriz_1) != len(matriz_2):
        return False 
    elif len(matriz_1[0]) == len(matriz_1):
        for indice in range(len(matriz_1)):
            if matriz_1[indice] != matriz_2[indice] or len(matriz_1[indice]) != len(matriz_1[0]):
                    return False
        return True
    else:
        return False

if __name__ == '__main__':
    m = [[1,2],[2,2,2]]
    p = [[1,2],[2,2,2]]
    print(comparar_matrices_cuadradas(m, p))