# Importamos las funciones desde el módulo Funciones_Portal
import Funciones_Portal as Funciones
import os

#Damos la bienvenida a la red

Funciones.mensaje_bienvenida()

#Verificamos si el usuario ya existe.
#En caso que el usuario exista, le damos la bienvenida, en caso contrario obtenemos sus datos.

nombre = Funciones.asignar_nombre()
if os.path.isfile(nombre + ".user"):
    print("Leyendo datos del usuario", nombre, "desde archivo")
    datos_usuario = Funciones.leer_archivo_usuario(nombre)
else:
    print("Bienvenido " + nombre + ", a continuación solicitaremos tus datos para crear tu perfil\n")
    Funciones.escribir_archivo_usuario(nombre)
    datos_usuario = Funciones.leer_archivo_usuario(nombre)

# Entramos al menú inicial, donde el usuario puede seleccionar una opción.

print("\nBienvenido/a al menú del Portal")
opcion = 1
while opcion:
    opcion = int(Funciones.ver_menu())

    #Opcion 1 para ver perfil del usuario actual
    if opcion == 1:
        Funciones.ver_perfil(datos_usuario)

    #Opcion 2 para actualizar datos del perfil
    elif opcion == 2:
        Funciones.escribir_archivo_usuario(nombre)
        datos_usuario = Funciones.leer_archivo_usuario(nombre)
        Funciones.ver_perfil(datos_usuario)

    #Opcion 3 para escribir un mensaje.
    elif opcion == 3:
        Funciones.escribir_mensaje(nombre)

    #Opcion 4 para enviar un mensaje a un amigo
    elif opcion == 4:
        Funciones.enviar_mensaje_amigo(nuevo_usuario)

    #Opcion 5 para cambiar de usuario
    elif opcion == 5:
        nuevo_usuario=input("Ingrese el nombre de su usuario: ")
        if os.path.isfile(nuevo_usuario + ".user"):
            datos_usuario = Funciones.cambiar_usuario(nuevo_usuario)
        else:
            print("Usuario no existe")

    elif opcion == 0:
        print("!Hasta pronto¡")

    else:
        print("No conozco esta opción, seleccione otra opción")






