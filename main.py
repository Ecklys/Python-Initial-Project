# Importamos las funciones desde el módulo Funciones_Portal
import Funciones_Portal as Funciones

#Damos la bienvenida a la red

Funciones.mensaje_bienvenida()

#Verificamos si el usuario ya existe.
#En caso que el usuario exista, le damos la bienvenida, en caso contrario obtenemos sus datos.

nombre = Funciones.asignar_nombre()
if Funciones.existe_archivo(nombre):
    print("Leyendo datos del usuario", nombre, "desde archivo")
    nombre, genero, pais_nac, residencia, correo, amigos, estado, muro = Funciones.leer_archivo_usuario(nombre)
else:
    print("Bienvenido " + nombre + ", a continuación solicitaremos tus datos para crear tu perfil\n")
    genero = Funciones.asignar_genero()
    pais_nac = Funciones.asignar_genero()
    residencia = Funciones.asignar_residencia()
    correo = Funciones.asignar_correo()
    amigos = Funciones.lista_amigos()
    estado = ""
    muro = []
# Entramos al menú inicial, donde el usuario puede seleccionar una opción.

print("\nBienvenido/a al menú del Portal")
opcion = 1
while opcion:
    opcion = int(Funciones.ver_menu())

    #Opcion 1 para ver perfil del usuario actual
    if opcion == 1:
        Funciones.ver_perfil(nombre, genero, pais_nac, residencia, correo, amigos)

    #Opcion 2 para actualizar datos del perfil
    elif opcion == 2:
        genero = Funciones.asignar_genero()
        pais_nac = Funciones.asignar_genero()
        residencia = Funciones.asignar_residencia()
        correo = Funciones.asignar_correo()
        amigos = Funciones.lista_amigos()
        Funciones.ver_perfil(nombre, genero, pais_nac, residencia, correo, amigos)

    #Opcion 3 para publicar un estado.
    elif opcion == 3:
        estado = Funciones.escribir_mensaje(nombre)

    #Opcion 4 para publicar un mensaje
    elif opcion == 4:
        mensaje = Funciones.escribir_mensaje(nombre)
        Funciones.publicar_mensaje(nombre, amigos, mensaje, muro)

    #Opcion 5 para ver el estado de todos tus amigos
    elif opcion == 5:
        Funciones.ver_estados_amigos(amigos)


    #Opcion 6 para agregar amigo
    elif opcion == 6:
        amigos = Funciones.agregar_amigo(amigos)

    #Opcion 7 para cambiar de usuario
    elif opcion == 7:
        nuevo_usuario=input("Ingrese el nombre de su usuario: ")
        if Funciones.existe_archivo(nombre):
            nombre, genero, pais_nac, residencia, correo, amigos, estado, muro = Funciones.cambiar_usuario(nuevo_usuario)
        else:
            print("Usuario no existe")

    elif opcion == 0:
        print("Guardando datos de usuario ", nombre , " en archivo")
        Funciones.escribir_archivo_usuario(nombre, genero, pais_nac, residencia, correo, amigos, estado, muro)
        print("!Hasta pronto¡")

    else:
        print("No conozco esta opción, seleccione otra opción")








