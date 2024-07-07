# Se debera crear una funcion y un test para probar dicha funcion como se plantearon en los
# ejercicios anteriores (26, 27, y 28). La funcion debera recibir
# una cadena de texto y debera retornar la cantidad de repeticiones del caracter que mas 
# se repite en la cadena. Ejemplo, dado "abbbbbbc" la funcion debera retornar 6 ya que es la
# cantidad de veces que se repite la letra 'b'. No olvidar crear el test con los casos de prueba

def caracter_mas_repetido(cadena :str )-> int:
    if cadena == "" :
        print("cadena VACIA")
        return None
    else :
        caracter = ''
        contador = 0
        while len(cadena) != 0 :
            sub_caracter = cadena[0]
            sub_contador = cadena.count(sub_caracter)
            for i in range(len(cadena)) : 
                x = cadena.replace(sub_caracter, '')
            cadena = x
            if contador < sub_contador :
                contador = sub_contador
                caracter = sub_caracter
    return contador
if __name__ == '__main__':
    texto = ''
    print(caracter_mas_repetido(texto))