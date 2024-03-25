#Crear una funcion que genere un archivo .txt llamado archivo.txt 
#que tenga de contenido el texto "Hola mundo."
def generar_ArchivoDeTexto():
	f = open("archivo.txt", "w")
	f.write("Hola mundo.")
	f.close()
	return f

archivo = generar_ArchivoDeTexto()
archivo = open("archivo.txt", "r")
print (archivo.read())