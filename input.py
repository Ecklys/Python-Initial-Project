#Input permite asignar valores a la variable mediante texto de entrada.
#Input siempre lee caracteres y es de tipo string

nombre = input("¿Cuál es tu nombre? ")
saludo = "Buen día"
pregunta = "¿Que cuenta?"

print( saludo, nombre, pregunta)

#Es posible convertir el tipo de dato de input mediantes casting

lec = int(input("¿Cuantas lecciones has visto? "))
total = 15
faltan = total - lec
print ("Te faltan", faltan, "lecciones, !Ánimo")