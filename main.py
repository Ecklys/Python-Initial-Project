# Importamos las funciones desde el módulo Funciones_Portal
from Funciones_Portal import *

#Damos la bienvenida a la red

mensaje_bienvenida()

#Obtenemos los datos iniciales del usuario: nombre, género, país de nacimiento, residencia actual y correo electrónico

(nombre, genero, pais_nac, residencia, correo) = obtener_datos()
print('Bienvenido, crearemos tu nuevo perfil utilizando los siguientes datos:')
ver_perfil(nombre, genero, pais_nac, residencia, correo)

# Entramos al menú inicial, donde el usuario puede seleccionar una opción.

print("Bienvenido al menú del Portal")
opcion = 1
while opcion:
    opcion = int(ver_menu())
    if opcion == 1:
        ver_perfil(nombre, genero, pais_nac, residencia, correo)

    elif opcion == 2:
        print("")
        (nombre, genero, pais_nac, residencia, correo) = obtener_datos()
        print('Actualizaremos tu perfil utilizando los siguientes datos:')
        ver_perfil(nombre, genero, pais_nac, residencia, correo)

    elif opcion == 3:
        escribir_mensaje(nombre)

    elif opcion == 0:
        print("!Hasta pronto¡")
        continuar = False

    else:
        print("Opcion incorrecta, seleccione otra opción")






