# Laboratorio-de-Python
Repositorio del grupo C 35. Aquí encontrará el desarrollo del taller de Python de la cátedra "Algoritmos y Estructuras de Datos" 

⭐ Integrantes del grupo:
- ARRIAZU, Nerea Micaela 
- BARCALA, Martin Andres
- FRANCO, Gastón Agustin 
- GONZALEZ, Irina 
- VALUSSI MELENDES, Fabrizio Francisco



⭐¿Qué se encuentra en este repositorio?⭐

En este repositorio se encuentra un simulador del funcionamiento básico de un cajero automático, desarrollado en Python, que permite a un usuario predefinido autenticarse y realizar operaciones bancarias simples como consultar saldo, depositar, extraer y transferir dinero. Además se encuentra un video explicativo del sistema en cuestión.



⭐Función general del sistema⭐

Primero, pide al usuario la autenticación para ingresar a la cuenta, permite hasta 3 intentos; si falla las 3 veces, bloquea el acceso (para esa ejecución del programa). Una vez verificada la sesión, ingresa y genera un menú de opciones.
 1. Consultar el saldo disponible.
 2. Depositar dinero en la cuenta actual
 3. Extraer dinero de la cuenta actual
 4. Transferir dinero a otro usuario existente en el sistema
 5. Ver registro de operaciones de la sesión realizados durante la sesión actual
 6. Salir del sistema, guardando los cambios en el saldo



⭐ERRORES QUE PUEDEN SURGIR EN LA EJECUCIÓN DEL PROGRAMA⭐

* No permite depositar o extraer montos negativos o cero.
* No permite extraer más dinero del que hay disponible.
* No permite transferir a un usuario que no existe.
* Maneja errores si el usuario ingresa texto en vez de números en el menú.



⭐ Estructuras utilizadas en el desarrollo del código:⭐

🟢 Condicionales (If, Elif, Else)

	if opcion == 1:
	…
	Elif opcion == 2:
	…
🟢 Bucles (While, for)
	
	While true:
	…


🟢Funciones (def)


	def usuario(usuario, clave):
			…


🟢Manejo de registros y archivos

	archivo = open(arch_usu, "w", encoding="utf-8")
	    archivo.write("admin;1234;50000;Administrador\n")
	    archivo.write("alumno;0000;15000;Usuario Prueba\n")
	archivo.close()

⭐ Ejecutar el programa ⭐

1. Entrar al repositorio en GitHub.
2. Hacer clic en el botón verde "Code".
3. Ir a la pestaña "Codespaces".
4. Hacer clic en "Create codespace on main".
5. Esperar a que se abra un editor (tipo VS Code) en el navegador, con una terminal integrada.
6. En la terminal, escribir:

       python cajero_automatico.py

7. Darle a enter una vez terminado de escribir en la terminal.


⭐ Instrucciones de ejecución del programa ⭐

Una vez ejecutado el programa se le pedirá al usuario ingresar “Nombre de usuario” y “contraseña”. Existen dos usuarios de prueba disponibles para el simulador:

	Nombre: admin
	Contraseña: 1234
	////////////////
	Nombre: alumno
	Contraseña: 0000

(Nota: Este programa diferencia minúsculas y mayúsculas, ingresar la clave como se indica)

El usuario tiene 3 intentos posibles para ingresar, de lo contrario se bloqueará el acceso y finalizará la ejecución al programa.
Una vez logueado en el programa, se desplegará un menú. Donde el usuario puede seleccionar alguna opción disponible (desde la opción 1 hasta la 6), si ingresa una opción no disponible saltará un error.

El menú disponible es el siguiente:

	--- MENÚ PRINCIPAL ---
	1. Consultar saldo
	2. Depositar dinero
	3. Extraer dinero
	4. Transferir dinero
	5. Ver Registro de Operaciones
	6. Salir

🔶Si el usuario ingresa la “opción 1” se le mostrará el saldo actual en su cuenta.

🔶Si el usuario ingresa la “opción 2” el programa pedirá que ingrese un monto de dinero para depositar en la cuenta.

🔶Si el usuario ingresa la “opción 3” el programa pedirá al usuario que ingrese un monto a retirar. Existe un monto máximo a retirar por cada operación ($10.000) y por cada uso del programa/sesión ($20.000):

			🔸En el caso que el usuario desee retirar un monto superior a $10.000, saltará error y no le permitirá extraer más del monto definido.
			
            🔸Si el monto de la extracción es menor a $10.000, pero hace que el total extraído en el día supere los $20.000, la extracción no podrá realizarse y el programa mostrará el total de dinero disponible a retirar.
			
            🔸Una vez llegado a $20.000 en extracción, no dejará que el usuario realice más extracciones.

🔶Si el usuario ingresa la “opción 4”:

            🔸Se pedirá al usuario que ingrese la cuenta destino a la que quiere enviar el dinero (esta debe ser el otro usuario de prueba disponible, ej.: si ingresó con “admin”, el usuario destino deberá ser “alumno”)
            🔸Si se ingresa un usuario no válido, saltará un error y se enviará nuevamente al menú principal.
            🔸Si el usuario es válido, el simulador pide el monto que se quiera enviar.

🔶Si el usuario ingresa la “opción 5” se mostrará un historial de las operaciones realizadas durante la sesión. 

🔶Si el usuario ingresa la “opción 6” Mostrará la cantidad de operaciones realizadas, finalizando la sesión.

   
⭐ Uso de la Inteligencia Artificial⭐

En general, utilizamos la inteligencia artificial (Code copilot)  para corroborar si algunas partes del código estaban correctamente definidas.
🟡Ej.: En el tratamiento del archivo y registro

	archivo = open(arch_usu, "w", encoding="utf-8")
  	  archivo.write("admin;1234;50000;Administrador\n")
    	archivo.write("alumno;0000;15000;Usuario Prueba\n")
	archivo.close()

La utilizamos para poder hacer pruebas de escritorio en el pseudocódigo desarrollado como borrador.
Para corregir errores de sintaxis, como en la definición de archivos o los bucles.

