# -*- coding:utf-8 -*-
from ejercicio28 import casi_ordenado


caso1 = [
    [2, 1, 2, 3, 4], True
]
caso2 = [
    [1, 2, 3, 4], True
]
caso3 = [
    [1, 2, 4, 2, 1], False
]
caso4 = [
    [1, 2, 4, 1, 9], True
]
caso5 = [
    [9, 2, 4, 1, 9], False
]

if (casi_ordenado(caso1[0]) == caso1[1] and
    casi_ordenado(caso2[0]) == caso2[1] and
    casi_ordenado(caso3[0]) == caso3[1] and
    casi_ordenado(caso4[0]) == caso4[1] and
    casi_ordenado(caso5[0]) == caso5[1]) :
    print('PRUEBAS PASADAS CON EXITO')
else:
    print('EL TEST FALLÓ')
