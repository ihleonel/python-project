# -*- coding:utf-8 -*-
from ejercicio31 import caracter_mas_repetido

caso1 = ["aaabbbaacccc", 5]
caso2 = ["abcdef", 1]
caso3 = ["", None]
caso4 = ["    ", 4]
caso5 = ["abababababababab", 8]

if (caracter_mas_repetido(caso1[0]) == caso1[1] and
    caracter_mas_repetido(caso2[0]) == caso2[1] and
    caracter_mas_repetido(caso3[0]) == caso3[1] and
    caracter_mas_repetido(caso4[0]) == caso4[1] and
    caracter_mas_repetido(caso5[0]) == caso5[1] ) :

    print('PRUEBAS PASADAS CON EXITO')
    
else:    
    
    print('EL TEST FALLÓ')
