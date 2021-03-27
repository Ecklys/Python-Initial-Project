#Es posible concatenar strings mediante el uso del operador +

string1 = "Hola"
string2 = "Adiós"

string3 = string1 + string2

print(string3)

#Es posible multiplicar strings o caracteres mediante el uso del operador *

string4 = string1 * 4 + string2 * 2

print(string4)

#Notar que la operación con operadores no deja espacios en blanco entre caracteres a menos que se deje uno en el string.

#Cada caracter de un string esta asociado a un índice, comenzado con 0 desde la izquierda. De la misma manera se puden utilizar indices negativos (por ejemplo -1 que corresponde al último caracter de la cadena)

#Es posible seleccionar caracteres de una cadena mediante el uso de rango de índices.

string5 = "Hola Mundo"
string6 = string5[3:7]

print(string6)

#Es posible utilizar "\" para utilizar comandos especiales como saltos de linea o tabulación
#Si se desea escribir un \ es necesario utilizar dos \\"

string7 = "Hola \nMundo"
print(string7)

#Algunas funciones utiles para trabajar con strings

#len calcula el largo de un string

print(len(string7))

#upper y lower permite cambiar la capitalización del string

print("Martes".upper())

#strip permite remover elementos de un extremo de un string seleccionando el elemento deseado

print("Hola. Mundo".strip("o"))

#replace permite sustituir algun caracter o substring dentro un string por otro

string8 = "Hola!°°"
print(string8.replace("°","!"))