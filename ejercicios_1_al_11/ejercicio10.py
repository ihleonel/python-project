#Crear una función que reciba un número entero y determine si es un número primo.
def primo(numero):
    c=2
    d=2
    while d<= (numero/2) and c <= 2 :
        if numero % d == 0 :
            c+=1
            d+=1
        else :
            d=d+1
    if c > 2 :
        print ( "---- NO ES PRIMO ----")
    else :
        print( " ---- ES PRIMO ---- " )

numero = int(input("ingrese un numero entero : "))
primo(numero)
