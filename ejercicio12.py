#Crear una función que reciba un string y determine si es un palindromo.
def palindromo( texto ):
    cont = 0
    for ind1,ind2 in zip(texto,reversed(texto)):
        if ind1 == ind2:
            cont+=1

    if cont == len(texto):
        return True
    else:
        return False

frase=input("ingrese texto : ")
print(palindromo(frase))
