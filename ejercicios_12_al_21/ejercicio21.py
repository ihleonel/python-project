#Crear una función que lea un archivo .txt llamado data.txt y retorne la suma de todos los numeros que contiene.
#El archivo data.txt ya esta generado en el repositorio. Ojo hay trampa!
def sumar_numeros():
    data = open("data.txt", "r")
    copia_data = data.read()
    data.close()							                # AL ABRIR EL ARCHIVO , SE REALIZA UNA COPIA EN UNA
    print(copia_data)										# NUEVA LISTA PARA PODER MANIPULAR EL TEXTO
    cantidad = len(copia_data)								# SE RECORRE LA LISTA DE COMIENZO A FIN
    subindice = 0											# OBTENIENDO CADA NUMERO VALIDO PARA PODER IR
    sumando = 0												# ACUMULANDO EN EL SUMANDO
    for i in range(cantidad):
        if copia_data[i] == ' ' or copia_data[i] == '\n':
            numero = copia_data[subindice:i]
            try:
                sumando = sumando + int(numero)
            except ValueError :
                print("Numero invalidado ...")
                print(numero)
            subindice = i
    return sumando

if __name__ == '__main__' :
	print(" RESULTADO = ", sumar_numeros())



# def sumar():
#     with open('data.txt', 'r') as archivo:
#         filas = archivo.readlines()
#     contador = 0
#     for fila in filas:
#         for valor in [valor.strip() for valor in fila.split(' ')]:
#             try:
#                 contador += int(valor)
#             except:
#                 pass

#     return contador



