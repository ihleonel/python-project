# -*- coding:utf-8 -*-
from ejercicio26 import comparar_matrices_cuadradas
from ejercicio27 import rotar_matriz_cuadrada


caso1 = [
    [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]],
    [[3, 2, 1],
     [3, 2, 1],
     [3, 2, 1]]
]
caso2 = [
    [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]],
    [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
]
caso3 = [
    [[1, 4, 2],
     [3, 5, 9],
     [9, 2, 3]],
    [[9, 3, 1],
     [2, 5, 4],
     [3, 9, 2]]
]

if (comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso1[0]), caso1[1]) and
    comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso2[0]), caso2[1]) and
    comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso3[0]), caso3[1])) :

    print('PRUEBAS PASADAS CON EXITO')
else:
    print('EL TEST FALLÓ')
