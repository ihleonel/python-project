# -*- coding:utf-8 -*-
from ejercicio26 import comparar_matrices_cuadradas


caso1 = [
    [[1]],
    [[1]],
    True
]
caso2 = [
    [[1, 2],
     [2, 1]],
    [[1, 2],
     [2, 1]],
    True
]
caso3 = [
    [[1, 9],
     [2, 1]],
    [[1, 2],
     [2, 1]],
    False
]

if (comparar_matrices_cuadradas(caso1[0], caso1[1]) == caso1[2] and
    comparar_matrices_cuadradas(caso2[0], caso2[1]) == caso2[2] and
    comparar_matrices_cuadradas(caso3[0], caso3[1]) == caso3[2]) :

    print('PRUEBAS PASADAS CON EXITO')
else:
    print('EL TEST FALLÓ')
