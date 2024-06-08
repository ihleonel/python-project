# Se deberá crear una función que reciba una lista de numeros enteros como parametro y determine
# si eliminando como maximo un elemento de la lista la misma queda ordenada ascendentemente,
# si es asi la funcion deberá retornar un True, en caso contrario retornar False.
# Ejemplo dado [1, 2, 4, 2] la funcion retorna un True. Correr 
# el test python3 test_ejercicio28.py se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".

def casi_ordenado(lista: list)->bool:
    if lista != "" :
        menor = lista[0]
        antes_del_menor = 0
        cantidad = len(lista)-1
        i = 1
        contador = 0
        while i < cantidad and contador <= 1 :
            if menor < lista[i] :
                antes_del_menor = menor
                menor = lista[i]
                i += 1
            elif menor >= lista[i] and antes_del_menor == lista[i]:
                lista.remove(lista[i])
                cantidad = len(lista)
                contador += 1
            else :
                lista.remove(menor)
                cantidad = len(lista)
                menor = lista[i-1]
                contador += 1
                
        if contador == 1 or contador == 0 :
            return True
        else :
            return False
    else :
        print("--- LISTA VACIA ----")
if __name__ == '__main__':
    lista = [1, 2, 3, 1]
    print(casi_ordenado(lista))
    print(lista)
