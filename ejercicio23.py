# Crear la clase Usuario que contenga:
# Dos atributos: nombre y clave
# Un método __init__ que reciba los parametros para cargar los atributos de la clase.
# Un método que reciba como parámetro un nombre para poder modificar el atributo nombre de la clase.

class Usuario :

	def __init__(self, nombre, clave):
		self.nombre = nombre
		self.clave = clave

	def __str__(self):
		return f"{"USUARIO : "+self.nombre}{"  CLAVE : "+self.clave}"

	def modificar_nombre(self, nombre_nuevo):
		self.nombre = nombre_nuevo

persona = Usuario("MauricioV2024", "aWqeasWQ")
print(persona)
nuevo_dato = "Villca2024"
persona.modificar_nombre(nuevo_dato)
print(persona)