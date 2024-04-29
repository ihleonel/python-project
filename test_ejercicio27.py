# -*- coding:utf-8 -*-
from ejercicio26 import comparar_matrices_cuadradas
from ejercicio27 import rotar_matriz_cuadrada


caso1 = [
    [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]],
    [[3, 2, 1],
     [3, 2, 1],
     [3, 2, 1]],
    True
]
caso2 = [
    [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]],
    [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]],
    False
]
caso3 = [
    [[1, 2],
     [3, 4]],
    [[3, 1],
     [4, 2]],
    True
]
caso4 = [
    [[1, 4, 2],
     [3, 5, 9],
     [9, 2, 3]],
    [[9, 3, 1],
     [2, 5, 4],
     [3, 9, 2]],
    True
]
caso5 = [
    [2],
    [4],
    False
]

if (comparar_matrices_cuadradas(
        rotar_matriz_cuadrada(caso1[0]), caso1[1]) == caso1[2] and
    comparar_matrices_cuadradas(
        rotar_matriz_cuadrada(caso2[0]), caso2[1]) == caso2[2] and
    comparar_matrices_cuadradas(
        rotar_matriz_cuadrada(caso3[0]), caso3[1]) == caso3[2] and
    comparar_matrices_cuadradas(
        rotar_matriz_cuadrada(caso4[0]), caso4[1]) == caso4[2] and
    comparar_matrices_cuadradas(
        rotar_matriz_cuadrada(caso5[0]), caso5[1]) == caso5[2]):

    print('PRUEBAS PASADAS CON EXITO')
else:
    print('EL TEST FALLÓ')
