#JUEGO DE MESA , COMPLETAR  LA BARAJA DEL RESPECTIVO PALO DE LA PRIMERA CARTA QUE SACO CADA JUGADOR
# GANA QUIEN COMPLETE  PRIMERO LA BARAJA 
numeros = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
palos= ["PICA","DIAMANTE","CORAZON","TREBOL"]
cartas= {"PICA" : numeros , "DIAMANTE" : numeros ,"CORAZON": numeros ,"TREBOL": numeros}
print(cartas)
import random
c_c=c_p=c_t=c_d=0
while len(palos)>3 :
            x_p=palos[random.randint(0,len(palos)-1)]
            lista = list(cartas.get(x_p))
            if x_p == "PICA" and lista != []:
                  x_n=lista[random.randint(0,len(lista)-1)]
                  print(x_p ,":" ,x_n)
                  lista.remove(x_n)
                  cartas[x_p]=lista
            elif x_p == "DIAMANTE" and lista != []:
                  x_n=lista[random.randint(0,len(lista)-1)]
                  print(x_p ,":" ,x_n)
                  lista.remove(x_n)
                  cartas[x_p]=lista     

            elif x_p == "TREBOL" and lista != []:
                  x_n=lista[random.randint(0,len(lista)-1)]
                  print(x_p ,":" ,x_n)
                  lista.remove(x_n)
                  cartas[x_p]=lista

            elif x_p == "CORAZON" and lista != []:
                  x_n=lista[random.randint(0,len(lista)-1)]
                  print(x_p ,":" ,x_n)
                  lista.remove(x_n)
                  cartas[x_p]=lista

            if lista == [] :
                print(cartas)
                print("--------GANO LA BARAJA DE  ",x_p,"------------")
                palos.remove(x_p)
            
                                
