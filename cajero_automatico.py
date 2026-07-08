import os

arch_usu = "usuarios.txt" # nombre del archivo donde se guardan los datos de los usuarios

limite_ext = 10000   # máximo permitido por operación
limite_diario = 20000           # máximo acumulado de extracciones en la sesión


def prueba():
 # escribe dos usuarios de prueba adentro (admin y alumno), con formato: "usuario; clave; saldo; nombre"

    archivo = open(arch_usu, "w", encoding="utf-8")

    archivo.write("admin;1234;50000;Administrador\n")
    archivo.write("alumno;0000;15000;Usuario Prueba\n")

    archivo.close()


def usuario(usuario, clave):

    # busca en el archivo si existe un usuario con ese id y esa contraseña, devuelve True/False y la línea completa de datos

    archivo = open(arch_usu, "r", encoding="utf-8")

    encontrado = False
    datos = ""

    for linea in archivo: # recorre el archivo línea por línea

        id_usuario, contra, saldo, nombre = linea.strip().split(";") # separa cada línea en sus 4 campos usando ";"

        if id_usuario == usuario and contra == clave: # compara con lo que ingresó el usuario

            encontrado = True
            datos = linea.strip()

            break

    archivo.close()

    return encontrado, datos


def actualizar(usu_modif):

    archivo = open(arch_usu, "r", encoding="utf-8")

    contenido = ""  # comienza el archivo actualizado 

    for linea in archivo:

        id_usuario, contra, saldo, nombre = linea.strip().split(";") 

        id_mod, contra_mod, saldo_mod, nombre_mod = usu_modif.split(";") # datos del usuario que se quiere actualizar

        if id_usuario == id_mod:

            contenido += usu_modif + "\n"

        else:

            contenido += linea


    archivo.close()


    archivo = open(arch_usu, "w", encoding="utf-8") # se abre el archivo para escribirlo

    archivo.write(contenido)

    archivo.close()



def obtiene_usu(usuario): 

    # Busca el usuario solo por id, sin verificar contraseña. Se usa para ver que exista el destino de la transferencia

    archivo = open(arch_usu, "r", encoding="utf-8")

    datos = ""

    for linea in archivo:

        id_usuario, contra, saldo, nombre = linea.strip().split(";")

        if id_usuario == usuario:

            datos = linea.strip()

            break


    archivo.close()

    return datos


def cajero_automatico():

    # Permite hasta 3 intentos de login. Si acierta, guarda los datos del usuario y continúa. Si falla 3 veces, bloquea el acceso

    prueba()

    intentos = 0    # cantidad de intentos fallidos de login
    cont_op = 0     # cantidad de operaciones realizadas en la sesión

    operaciones = ""    # historial de operaciones de la sesión

    cont_ext = 0   # acumula lo extraído en la sesión para controlar el límite diario

    sesion_valida = False

    usu_actual = ""


    print("Bienvenido al Sistema de Cajero Automático")


    while True:

        usu_ingresado = input("Ingrese su identificador de usuario: ")
        cont_ingresada = input("Ingrese su contraseña: ")


        valido, datos = usuario(
            usu_ingresado,
            cont_ingresada
        )


        if valido:  # si el usuario y clave son correctos, se guarda la sesión y sale del bucle

            sesion_valida = True
            usu_actual = datos

            break
        else: # si no, suma un intento fallido

            intentos += 1

            print(f"Usuario o clave incorrectos. Intentos restantes: {3-intentos}")


        if intentos == 3:

            break


    if sesion_valida:


        id_usuario, contra, saldo, nombre = usu_actual.split(";")

        saldo = float(saldo) # convierte el saldo de texto a número 


        print(f"\nAcceso autorizado. Bienvenido/a {nombre}")

        while True: # repetir menú hasta que opcion = 6

            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Extraer dinero")
            print("4. Transferir dinero")
            print("5. Ver Registro de Operaciones")
            print("6. Salir")

            try:

                opcion = int(input("Seleccione una opción: "))

            except ValueError: # si se ingresa un caracter, se vuelve 0 para opción no válida

                opcion = 0

            if opcion == 1:

                # muestra el saldo actual y lo anota en el registro de operaciones

                print(f"Su saldo actual es: ${saldo:.2f}")

                operaciones += "Consulta de saldo realizada\n"

                cont_op += 1

            elif opcion == 2:

                # pide un monto, si es mayor a 0 lo suma al saldo y lo anota, si no, avisa error

                monto = float(input("Ingrese el monto a depositar: "))

                if monto > 0:

                    saldo += monto

                    operaciones += (f"Depósito realizado: ${monto:.2f}\n")

                    cont_op += 1

                    print("Depósito realizado correctamente.")
                else:

                    print("El monto debe ser mayor a cero.")

            elif opcion == 3:

                # pide un monto, verifica que no sea mayor al saldo ni menor/igual a 0, si está todo bien lo resta del saldo

                monto = float(input("Ingrese el monto a extraer: "))
                   

                if monto > saldo:

                    print("Error: Fondos insuficientes.")
                elif monto <= 0:

                    print("El monto debe ser mayor a cero.")

                elif monto > limite_ext:

                    # no se puede extraer más del límite de extracción en una sola operación
                    print(f"Error: no se pueden extraer más de ${limite_ext} por operación.")

                elif cont_ext + monto > limite_diario:

                    # no se puede superar el límite diario en la sesión
                    disponible = limite_diario - cont_ext
                    print(f"Error: se superó el límite diario de extracción. Disponible para extraer hoy: ${disponible:.2f}")

                else:

                    saldo -= monto

                    cont_ext += monto   # actualiza lo extraído en la sesión

                    operaciones += (f"Extracción realizada: ${monto:.2f}\n")
                        
                    cont_op += 1

                    print("Extracción realizada correctamente.")

            elif opcion == 4:

                destino = input("Ingrese el usuario al que desea transferir: ") # pide el usuario destino
                    

                datos_dest = obtiene_usu(destino) # busca ese usuario con obtiene_usu()


                if datos_dest == "":

                    print("Error: El usuario destino no existe.") # error porque no existe el usuario

                else:


                    monto = float( input("Ingrese el monto a transferir: ")) # si existe, pide el monto, valida que sea correcto y que haya saldo suficiente
                       

                    if monto > saldo:

                        print("Error: Fondos insuficientes.") 


                    elif monto <= 0:

                        print("El monto debe ser mayor a cero.")


                    else:

                        id_dest, con_dest, saldo_dest, nom_dest = datos_dest.split(";")

                        saldo_dest = float(saldo_dest)
                        
                        # resta el monto al usuario actual y se lo suma al usuario destino

                        saldo -= monto

                        saldo_dest += monto 

                        
                        # guarda los cambios del usuario destino 

                        actualizar(
                            id_dest + ";" +
                            con_dest + ";" +
                            str(saldo_dest) + ";" +
                            nom_dest
                        )


                        operaciones += (f"Transferencia enviada a {destino}: ${monto:.2f}\n")

                        cont_op += 1


                        print("Transferencia realizada correctamente.")

            elif opcion == 5: # muestra el historial de opercaiones de la sesión
               

                print("\n--- REGISTRO DE OPERACIONES ---")      

                if operaciones == "":

                    print("No existen operaciones realizadas.")

                else:

                    print(operaciones)

            elif opcion == 6:

                break # corta el bucle del menú principal

            else:

                print("Error: Opción no válida.") # cualquier opción diferente no es válida

        # guarda los cambios del usuario actual
        actualizar(
            id_usuario + ";" +
            contra + ";" +
            str(saldo) + ";" +
            nombre
        )

        print( f"\nCantidad de operaciones realizadas en esta sesión: {cont_op}") # muestra cuántas operaciones se hicieron en la sesión

    else:

        print("\nCajero bloqueado temporalmente por seguridad.") # muestra el mensaje de "cajero bloqueado" si nunca se validó la sesión


if __name__ == "__main__":

    cajero_automatico()
