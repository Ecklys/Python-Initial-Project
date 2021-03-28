#Tipos de Listas

#Declaracion de variable tipo List

#nombre_lista = ["string", int, float] (Se puede declarar una lista vacia)

no_olvidar = ["Cursos de Python", "Curso de Data Science", "Pagar Tarjeta", 100000]
print(type(no_olvidar))
print(no_olvidar)

#Es posible utilizar variables o expresiones como elementos de una lista. Acepta todo tipo de datos

#Es posible anidar listas -> lo convierte en un arreglo matricial

#Listas son mutables -> se pueden modificar los elementos, cada elemento de una lista pertenece a un índice.

#Como acceder a elementos:

print(no_olvidar[2])
no_olvidar[2] = "Tarjeta Pagada"
print(no_olvidar)

#Slice de elementos
#lista[inicio:fin:step]

print(no_olvidar[2:4])

#Nota: recorrer elementos de orden inverso con slices

print(no_olvidar[::-1])

#Se pueden utilizar funciones iterativas para recorrer una lista

for elem in no_olvidar:
    print("No olvidar: "+str(elem))


#Es posible concatenar y repetir listas

otra_lista = ["Correr", "Vivir", "Saltar"]

nueva_lista = no_olvidar + otra_lista
print(nueva_lista)

nueva_lista_2 = nueva_lista * 2
print(nueva_lista_2)

#Agregar elementos a la lista mediante el método append, lo cual inserta un nuevo elemento al final de la lista con el índice correspondiente

otra_lista.append("Agregue otro elemento")
print(otra_lista)


#Si deseo agregar más de un elemento a la lista se puede utilizar el método extend con sus índices

otra_lista.extend(["1 mas", "2 mas"])
print(otra_lista)

#El método insert permite insertar un elemento en cualquier índice de la lista, modificando los índices de los elementos siguientes.

otra_lista.insert(2, "Insertado")
print(otra_lista)

#El método pop extrae el elemento del índice indicado, por defecto extrae el último
extraido = otra_lista.pop(0)
print(otra_lista)
print(extraido)

#El método remove permite eliminar un elemento de la lista

otra_lista.remove("Vivir")
print(otra_lista)

#Existen funciones predefinidas para la interacción con listas
#El método len nos permite obtener el número de elementos dentro de la lista

print(len(otra_lista))

#Operador in permite consultar si la lista posee un elemento en particular

print("¿Hay que saltar?", ("Saltar" in otra_lista))

#El método index no permite obtener el índice del elemento buscado en la lista. En caso que el elemento no exista el método retorna un error.

print("Insertado:", (otra_lista.index("Insertado")))

#El método split (de tipo string) permite separar un texto segun el separador ingresado.

#otra_lista2 = texto.split(",") Separa el texto cada vez que encuentre un ,

#El método sort permite ordenar una lista de menor a mayor. (Pero no permite ordenar listas con multiples tipos de variable).
#En caso de intentar ordenar listas dentro de listas, sort considerara el primer elemento de la lista anidada.

otra_lista.sort()
print(otra_lista)