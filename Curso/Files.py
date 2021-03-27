#Abriendo un archivo mediante la función open, la cual toma como parametros el nombre del archivo y el modo de apertura (r o w), por defecto es r si no se entrega el parametro

File1 = open("archivo.txt", "r")

#Para leer un archivo es necesario utilizar el método read

leer = File1.read()

#Es posible leer un archivo linea por linea mediante el método readline, cada vez que este es invocado lee la siguiente linea.

leer_linea = File1.readline()

#Para escribir sobre un archivo se debe abrir en modo escritura, DETALLE: si el archivo ya existe, al abrirlo en modo write se sobreescribira

File2 = open("archivo.txt", "w")

File2.write("Hola")

#Para escribir saltos de línea es necesario ser explicito

File2.write("\n Adios")

#Para cerrar un archivo luego de leerlo o escribir sobre el se utiliza el método close.

File1.close()
File2.close()
