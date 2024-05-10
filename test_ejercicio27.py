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
    [[1, 4, 2, 1],
     [3, 5, 9, 1],
     [9, 2, 3, 1],
     [1, 1, 1, 1]],
    [[1, 9, 3, 1],
     [1, 2, 5, 4],
     [1, 3, 9, 2],
     [1, 1, 1, 1]],
     True
]

if (comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso1[0]), caso1[1]) == caso1[2] and
    comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso2[0]), caso2[1]) == caso2[2] and
    comparar_matrices_cuadradas(rotar_matriz_cuadrada(caso3[0]), caso3[1]) == caso3[2]) :
    
    print('PRUEBAS PASADAS CON EXITO')
else:
    print('EL TEST FALLÓ')
