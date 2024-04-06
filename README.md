# Python Project

## Tareas

22. Crear una clase que contenga:
- Un método que reciba como parametro una lista de número enteros se determine si la lista esta ordenada ascendentemente o no, retornado True si la lista es esta ordenada o False si la lista no esta ordenada

23. Crear la clase Usuario que contenga:
- Dos atributos: *nombre* y *clave*
- Un método `__init__` que reciba los parametros para cargar los atributos de la clase.
- Un método que reciba como parámetro un nombre para poder modificar el atributo *nombre* de la clase.

24. Importando y usando la clase "Usuario" creada en el ejercicio anterior. Crear la clase "LectorUsuario" que contenga:
- Un metodo "obtener_usuarios" que obtenga los datos del archivo "database.txt" y retorne una lista de elementos de la clase Usuario cargando casa usuario con los datos del archivo.

25. Importando y usando la clase "Usuario". Crear la clase CreadorUsuario que contenga:
- Un metodo "crear_usuario" que reciba como parametro un objeto "Usuario" y que guarde los datos de ese objeto en el archivo "database.txt". No debera sobreescribir o borrar los datos que ya existen en el archivo el nuevo usuario debera agregarse al final del archivo.

26. Se deberá crear una función que reciba dos matrices cuadradas como parametros y debara retornar si son equivalentes o no. Para determinar si la funcion es correcta se debera correr el test `python3 test_ejercicio26.py` y se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".

27. Se deberá crear una función que reciba una matriz cuadrada nxn y retorne la misma matriz pero rotada 90 grados en sentido de las agujas del reloj. Ver los casos de prueba en el archivo "test_ejercicio27.py". Correr el test `python3 test_ejercicio27.py` se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".

28. Se deberá crear una función que reciba una lista de numeros enteros como parametro y determine si eliminando como maximo un elemento de la lista la misma queda ordenada ascendentemente, si es asi la funcion deberá retornar un True, en caso contrario retornar False. Ejemplo dado [1, 2, 4, 2] la funcion retorna un True. Correr el test `python3 test_ejercicio28.py` se deberá mostrar el mensaje "PRUEBAS PASADAS CON EXITO".

29. Se debera crear una funcion y un test para probar dicha funcion como se plantearon en los ejercicios anteriores (26, 27, y 28). La funcion debera recibir dos numero enteros y retornar su suma. No olvidar crear el test con los casos de prueba

30. Se debera crear una funcion y un test para probar dicha funcion como se plantearon en los ejercicios anteriores (26, 27, y 28). La funcion debera recibir dos numeros enteros y retornar su division. No olvidar crear el test con los casos de prueba

31. Se debera crear una funcion y un test para probar dicha funcion como se plantearon en los ejercicios anteriores (26, 27, y 28). La funcion debera recibir una cadena de texto y debera retornar la cantidad de repeticiones del caracter que mas se repite en la cadena. Ejemplo, dado "abbbbbbc" la funcion debera retornar 6 ya que es la cantidad de veces que se repite la letra 'b'. No olvidar crear el test con los casos de prueba

> En este repositorio se van a ir dejando los ejercicios resueltos. Cada ejercicio deberá estar resuelto en un archivo diferente y deberá ser nombrado como ejercicio1.py, etc. Cada ejercicio deberá ser enviado en un commit diferente.
