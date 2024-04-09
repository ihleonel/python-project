# Crear una clase que contenga:
# Un método que reciba como parametro una lista de número enteros se determine si la lista esta ordenada 
# ascendentemente o no, retornado True si la lista es esta ordenada o False si la lista no esta ordenada

class listas:

	def __init__ (self, lista):
		self.lista = lista

	def __str__(self):
		return f"{self.lista}"

	def es_ascendente(self):
		banda = 0
		i = 0
		while banda != 1 and i < len(self.lista)-1:
		    if self.lista[i] < self.lista[i+1]:
		    	i += 1
		    else:
		    	banda = 1
		if banda == 0:
			return True
		else:
			return False

l = [-1,0,1,2,3,4,6,7]
Milista = listas(l)
print(Milista.es_ascendente())
