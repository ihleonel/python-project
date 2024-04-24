# Importando y usando la clase "Usuario" creada en el ejercicio anterior.
# Crear la clase "LectorUsuario" que contenga:
# Un metodo "obtener_usuarios" que obtenga los datos del archivo "database.txt" y
# retorne una lista de elementos de la clase Usuario cargando casa usuario con los datos del archivo.
# Ejemplo retornar [Usuario(JuanGar28,Rt7#2Ky9), Usuario(), ..., Usuario()]
from ejercicio23 import Usuario
class LectorUsuario():

    def obtener_usuarios(self):
        usuario = open("database.txt", "r")
        fila_usuarios = usuario.readlines()
        usuario.close()
        lista_usuarios = []
        for user in fila_usuarios:
            nombre = user[0:user.index(',')]
            clave = user[user.index(',')+1 : user.index('\n')]
            persona = Usuario(nombre, clave)
            lista_usuarios.append(persona)
        return lista_usuarios

if __name__ == '__main__':
    lista_clientes = LectorUsuario()
    l = lista_clientes.obtener_usuarios()
    for x in l: print(x)