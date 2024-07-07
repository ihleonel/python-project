# -*- coding:utf-8 -*-
from ejercicio29 import sumar_numeros

caso1 = [[17, 13], 30]
caso2 = [[-11, -23], -34]
caso3 = [[-1, 10], 9]
caso4 = [[6.5, 5.5], None]
caso5 = [[1.00001, 5], None]
caso6 = [[1.0000, 10], 11.0]

if (sumar_numeros(caso1[0][0],caso1[0][1]) == caso1[1] and
    sumar_numeros(caso2[0][0],caso2[0][1]) == caso2[1] and
    sumar_numeros(caso3[0][0],caso3[0][1]) == caso3[1] and
    sumar_numeros(caso4[0][0],caso4[0][1]) == caso4[1] and
    sumar_numeros(caso5[0][0],caso5[0][1]) == caso5[1] and 
    sumar_numeros(caso6[0][0],caso6[0][1]) == caso6[1]) :
    print('PRUEBAS PASADAS CON EXITO')
    
else:    
	
    print('EL TEST FALLÓ')

