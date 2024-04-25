# Importando y usando la clase "Usuario". Crear la clase "CreadorUsuario" que contenga:
# Un metodo "crear_usuario" que reciba como parametro un objeto "Usuario" y 
# que guarde los datos de ese objeto en el archivo "database.txt".
# No debera sobreescribir o borrar los datos que ya existen en el archivo,
# el nuevo usuario debera agregarse al final del archivo.
from ejercicio23 import Usuario
class CreadorUsuario():
    def crear_usuario(self, Usuario_nuevo: Usuario):
        archivo = open("database.txt", "w")
        nombre = Usuario_nuevo.nombre
        clave = Usuario_nuevo.clave
        archivo.write(nombre + "," + clave + "\n")
        archivo.close()

if __name__ == '__main__':
    nuevo_usuario = Usuario("Mauricio2024", "Ky4&Wc6%")
    modificar = CreadorUsuario()
    modificar.crear_usuario(nuevo_usuario)





