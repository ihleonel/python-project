# -*- coding:utf-8 -*-
from ejercicio30 import dividir_numeros

caso1 = [[24, 3], 8.0]
caso2 = [[64, 3], 21.333333333333332]
caso3 = [[14, 0], None]
caso4 = [[0, 0], None]
caso5 = [[0, 12], 0]
caso6 = [[-13, 3], -4.333333333333333]
caso7 = [[-21, -7], 3]

if (dividir_numeros(caso1[0][0],caso1[0][1]) == caso1[1] and
    dividir_numeros(caso2[0][0],caso2[0][1]) == caso2[1] and
    dividir_numeros(caso3[0][0],caso3[0][1]) == caso3[1] and
    dividir_numeros(caso4[0][0],caso4[0][1]) == caso4[1] and
    dividir_numeros(caso5[0][0],caso5[0][1]) == caso5[1] and
    dividir_numeros(caso6[0][0],caso6[0][1]) == caso6[1] and
    dividir_numeros(caso7[0][0],caso7[0][1]) == caso7[1]) :

    print('PRUEBAS PASADAS CON EXITO')
    
else:    
    
    print('EL TEST FALLÓ')