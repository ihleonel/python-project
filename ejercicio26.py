# Se deberá crear una función que reciba dos matrices cuadradas como parametros
# y debara retornar si son equivalentes o no.
# Para determinar si la funcion es correcta se debera correr el test python3 test_ejercicio26.py
# y se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".
def comparar_matrices_cuadradas(matriz_1, matriz_2):
    if len(matriz_1) == len(matriz_2):
        band = True
        for i in range(len(matriz_1)):
            if matriz_1[i] != matriz_2[i]:
                band = False
        return band
    else:
        return False


# Clasulas de guarda
# def comparar_matrices_cuadradas(matriz_1, matriz_2):
#     if len(matriz_1) != len(matriz_2):
#         return False

#    if len(matriz_1[0]) != len(matriz_2[0]):
#         return False

#     band = True
#     for i in range(len(matriz_1)):
#         if matriz_1[i] != matriz_2[i]:
#             band = False
#     return band
