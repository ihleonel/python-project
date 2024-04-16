# Crear una clase que contenga:
# Un método que reciba como parametro una lista de número enteros se determine si la lista esta ordenada 
# ascendentemente o no, retornado True si la lista es esta ordenada o False si la lista no esta ordenada

class ListaNumerosEnteros:

    def es_ascendente(self, lista):
        band = 0
        i = 0
        while band != 1 and i < len(lista)-1:
            if lista[i] < lista[i+1]:
                i += 1
            else:
                band = 1
        return band == 0

l = [-1,5,2,3,4,6,7]
Milista = ListaNumerosEnteros()
print(Milista.es_ascendente(l))
