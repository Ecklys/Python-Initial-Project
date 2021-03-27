def mensaje_bienvenida():
    print("Bienvenido a ...")
    print("""              _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)
    return


def escribir_mensaje(nombre_usuario):
    usuario_mensaje = str(input("Ingrese su mensaje: "))
    print(nombre_usuario, "dice:", usuario_mensaje)
    return usuario_mensaje


def enviar_mensaje_amigo(nombre_usuario):
    continuar = True
    nombre = nombre_usuario
    usuario_mensaje = ""
    while continuar:
        nombre_amigo = str(input("¿A que amigo le enviarás un un mensaje? "))
        while usuario_mensaje == "":
            usuario_mensaje = str(input("Ingrese su mensaje: "))

        print(nombre, "dice a", nombre_amigo, ":", usuario_mensaje)
        continuar = False
    return


def asignar_nombre():
    nombre = input("¿Cuál es tu nombre? ")
    return nombre


def asignar_pais_nacimiento():
    pais_nac = input("¿Cual es tu país de nacimiento? ")
    return pais_nac


def asignar_genero():
    genero = input("¿Con que género te identificas? ")
    return genero


def asignar_residencia():
    residencia = input("¿Cuál es tu país de residencia actual? ")
    return residencia


def asignar_correo():
    correo = input("¿Cuál es tu correo electrónico? ")
    return correo


def obtener_datos():
    nombre = asignar_nombre()
    genero = asignar_genero()
    pais_nac = asignar_pais_nacimiento()
    residencia = asignar_residencia()
    correo = asignar_correo()
    return nombre,genero,pais_nac,residencia,correo


def leer_archivo_usuario(nombre):
    archivo = open(nombre + ".user", "r")
    nombre = archivo.readline().rstrip()
    genero = archivo.readline().rstrip()
    pais_nac = archivo.readline().rstrip()
    residencia = archivo.readline().rstrip()
    correo = archivo.readline().rstrip()
    archivo.close()
    return nombre, genero, pais_nac, residencia, correo


def escribir_archivo_usuario(nombre):
    archivo = open(nombre + ".user", "w")
    archivo.write(nombre + "\n")
    archivo.write(asignar_genero() + "\n")
    archivo.write(asignar_pais_nacimiento() + "\n")
    archivo.write(asignar_residencia() + "\n")
    archivo.write(asignar_correo() + "\n")
    archivo.close()
    return

def cambiar_usuario(nombre):
    return leer_archivo_usuario(nombre)


def ver_perfil(datos):
    nombre, genero, pais_nac, residencia, correo = datos
    print("\nTus datos son los siguiente:\n")
    print("Nombre:"+nombre)
    print("Género:"+genero)
    print("País de Nacimiento:"+pais_nac)
    print("País de Residencia:"+residencia)
    print("Correo Electrónico:"+correo)
    return

def ver_menu():
    print("")
    print("Que opción desea acceder")
    print("1.- Ver perfil")
    print("2.- Actualizar perfil")
    print("3.- Escribir mensaje")
    print("4.- Enviar mensaje a amigo")
    print("5.- Cambiar de usuario")
    print("0.- Salir del Portal")
    seleccion_opcion = int(input("Seleccione una opción:\n"))
    return seleccion_opcion
