import os

def mensaje_bienvenida():
    print("Bienvenido a ...")
    print("""              _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)
    return


def existe_archivo(nombre):
    return os.path.isfile(nombre + ".user")

def escribir_mensaje(nombre_usuario):
    usuario_mensaje = str(input("Ingrese su mensaje: "))
    print(nombre_usuario, "dice:", usuario_mensaje)
    return usuario_mensaje


def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", mensaje)
    print("--------------------------------------------------")
    muro.append(mensaje)
    for amigo in amigos:
        if existe_archivo(amigo):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()


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

def lista_amigos():
    lista_amigos = input("Ingresa tu listado de amigos separados por coma (,): ")
    amigos = lista_amigos.split(",")
    return amigos

'''def obtener_datos():
    nombre = asignar_nombre()
    genero = asignar_genero()
    pais_nac = asignar_pais_nacimiento()
    residencia = asignar_residencia()
    correo = asignar_correo()
    return (nombre,genero,pais_nac,residencia,correo)
'''



def leer_archivo_usuario(nombre):
    archivo = open(nombre + ".user", "r")
    nombre = archivo.readline().rstrip()
    genero = archivo.readline().rstrip()
    pais_nac = archivo.readline().rstrip()
    residencia = archivo.readline().rstrip()
    correo = archivo.readline().rstrip()
    amigos = archivo.readline().rstrip().split(",")
    estado = archivo.readline().rstrip()
    muro = []
    mensaje = archivo.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo.readline().rstrip()
    archivo.close()
    return (nombre, genero, pais_nac, residencia, correo, amigos, estado, muro)


def escribir_archivo_usuario(nombre, genero, pais_nac, residencia, correo, amigos, estado, muro):
    archivo = open(nombre + ".user", "w")
    archivo.write(nombre + "\n")
    archivo.write(genero + "\n")
    archivo.write(pais_nac + "\n")
    archivo.write(residencia + "\n")
    archivo.write(correo + "\n")
    archivo.write(",".join(amigos) + "\n")
    archivo.write(estado + "\n")
    for mensaje in muro:
        archivo.write(mensaje+"\n")
    archivo.close()
    return

def cambiar_usuario(nombre):
    return leer_archivo_usuario(nombre)

def agregar_amigo(lista_amigos):
    nuevo_amigo = input("Ingrese el nombre de su nuevo amigo: ")
    lista_amigos.append(nuevo_amigo)
    return lista_amigos

def ver_estados_amigos(lista_amigos):
    for amigo in lista_amigos:
        if existe_archivo(amigo):
            archivo_amigo = leer_archivo_usuario(amigo)
            print(amigo, "dice:", archivo_amigo[6])
    return


def ver_perfil(nombre, genero, pais_nac, residencia, correo, amigos):
    print("\nTus datos son los siguiente:\n")
    print("Nombre: "+nombre)
    print("Género: "+genero)
    print("País de Nacimiento: "+pais_nac)
    print("País de Residencia: "+residencia)
    print("Correo Electrónico: "+correo)
    print("Lista de Amigos: "+ (",".join(amigos)))
    return

def ver_menu():
    print("")
    print("Que opción desea acceder")
    print("1.- Ver perfil")
    print("2.- Actualizar perfil")
    print("3.- Publicar estado")
    print("4.- Publicar mensaje en el muro")
    print("5.- Ver estado de amigos")
    print("6.- Agregar amigo")
    print("7.- Cambiar de usuario")
    print("0.- Salir del Portal")
    seleccion_opcion = int(input("Seleccione una opción:\n"))
    return seleccion_opcion
