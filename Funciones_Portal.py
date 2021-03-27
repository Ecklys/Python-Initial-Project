def mensaje_bienvenida():
    print("Bienvenido a ...")
    print("""              _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

    print("Bienvenido al portal, a continuación te haremos algunas preguntas para comenzar la creación de tu perfil")

    return

def escribir_mensaje(nombre_usuario):
    continuar = True
    nombre = nombre_usuario
    while continuar:
        mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))
        if mensaje == "S" or mensaje == "s":
            usuario_mensaje = str(input("Ingrese su mensaje: "))
            print(nombre, "dice:", usuario_mensaje)

        elif mensaje == "N" or mensaje == "n":
            print("Gracias por compartir tu opinión.")
            continuar = False

        else:
            print("Opcion incorrecta, por favor ingrese (S/N)")
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
    return (nombre,genero,pais_nac,residencia,correo)



def ver_perfil(nombre, genero, pais_nac, residencia, correo):
    print("")
    print("Tus datos son los siguientes:")
    print("Nombre: ", nombre)
    print("Género: ", genero)
    print("País de nacimiento: ", pais_nac)
    print("Residencia actual: ", residencia)
    print("Correo Electrónico: ", correo)
    return

def ver_menu():
    print("")
    print("Que opción desea acceder")
    print("1.- Ver perfil")
    print("2.- Actualizar perfil")
    print("3.- Escribir mensaje")
    print("0.- Salir del Portal")
    seleccion_opcion = int(input("Seleccione una opción "))
    return seleccion_opcion
