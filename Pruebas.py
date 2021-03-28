def mcd(n1,n2):
    if (n1 >= n2):
        for i in range(1,n2+1):
            if not((n1 % i ) or (n2 % i)):
                maximo = i
    else:
        for i in range(1,n1+1):
            if not((n1 % i ) or (n2 % i)):
                maximo = i
    return maximo


print(mcd(18,27))


def exponente(n):
    for i in range(n+1):
        maximo = 2 ** i
        if maximo > n:
            return i-1

print(exponente(128))


def panprimo(n):
    es_panprimo = True
    es_primo = True
    divisores = 0
    for i in range(10):
        if not(str(i) in str(n)):
            es_panprimo = False
    tres_digitos = n % 1000
    for i in range (1, tres_digitos+1):
        if (tres_digitos % i == 0):
            divisores += 1
        if divisores > 2:
            es_primo = False
    return (es_panprimo and es_primo)

print(panprimo(2424643))


def mezclador(string_a, string_b):
  # aquí debes escribir el código de tu programa
  string_c=""
  string_d=""
  for i in range(2):
    string_c += string_a[i]
    string_d += string_b[-2+i]
  return string_c + string_d # aquí debes retornar el resultado

print(mezclador("hola","chao"))

def intercalar(string_a, string_b):
  string_c=""
  for i in range(len(string_a)):
    string_c += string_a[i] + string_b
  return string_c # aquí debes retornar el resultado

print(intercalar("paz","oso"))

def ocurrencias(string):
  unos=0
  ceros=0
  for i in range(len(string)):
    if string[i]=="1":
      unos += 1
    else:
      ceros += 1
  return unos - ceros # aquí debes retornar el resultado

print(ocurrencias("10101010100"))

def remover_enesimo(s, n):
  nuevo_string=""
  for i in range(len(s)):
    if i != n:
        nuevo_string += s[i]

  return nuevo_string # aquí debes retornar el resultado

print(remover_enesimo("Hasta luego",10))


def reemplazo(string):
  nuevo_string=""
  for i in range(len(string)):
    if string[i] == string[i].upper() and string[i] != " ":
      nuevo_string += "$"
    else:
      nuevo_string += string[i]
  return nuevo_string # aquí debes retornar el resultado

print(reemplazo("Hola Mundo"))


def promedio_std(lista):
    suma = 0
    suma_desv_std = 0
    for i in lista:
        suma += i
    promedio = suma / len(lista)

    for i in lista:
        suma_desv_std += (i - promedio) ** 2
    desv_std = (suma_desv_std / len(lista)) ** 0.5

    return (promedio,desv_std)

print(promedio_std([8, 79, 96, 4, 43, 35, 23, 36, 82, 66, 40, 10, 97, 85, 11, 70, 7, 56, 11, 40]))


def color_frecuente(lista):
    colores = [0,0,0,0]
    for elem in lista:
        if elem == "azul":
            colores[0] += 1
        elif elem == "rojo":
            colores[1] += 1
        elif elem == "verde":
            colores[2] += 1
        elif elem == "amarillo":
            colores[3] += 1

    if colores[0] >= colores[1] and colores[0] >= colores[2] and colores[0] >= colores[3]:
        mas_repetido = ["azul", colores[0]]

    elif colores[1] > colores[0] and colores[1] >= colores[2] and colores[1] >= colores[3]:
        mas_repetido = ["rojo", colores[1]]

    elif colores[2] > colores[0] and colores[2] > colores[1] and colores[2] >= colores[3]:
        mas_repetido = ["verde", colores[2]]

    else:
        mas_repetido = ["amarillo", colores[3]]

    return mas_repetido

print(color_frecuente(['rojo','rojo','azul','azul']))


def buscaminas(tablero,i,j):
    minas = 0
    #borde superior
    if i == 0:

        #borde superior izquierdo
        if j == 0:
            for fila_i in range(i,i+2):
                for columna_j in range(j,j+2):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

        #borde superior derecho
        elif j == len(tablero[0])-1:
             for fila_i in range(i,i+2):
                 for columna_j in range(j-1,j+1):
                     if fila_i == i and columna_j == j:
                         minas = minas
                     else:
                         if "X" in tablero[fila_i][columna_j]:
                             minas += 1


        else:
            for fila_i in range(i,i+2):
                for columna_j in range(j-1,j+2):
                     if fila_i == i and columna_j == j:
                         minas = minas
                     else:
                         if "X" in tablero[fila_i][columna_j]:
                             minas += 1

    #borde inferior
    elif i == len(tablero)-1:

        #borde inferior izquierdo
        if j == 0:
            for fila_i in range(i-1,i+1):
                for columna_j in range(j,j+2):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

        #borde inferior derecho
        elif j == len(tablero[0])-1:
            for fila_i in range(i-1,i+1):
                for columna_j in range(j-1,j+1):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

        else:
            for fila_i in range(i-1,i+1):
                for columna_j in range(j-1,j+2):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

    #bordes laterales
    else:

        #borde izquierdo
        if j == 0:
            for fila_i in range(i-1,i+2):
                for columna_j in range(j,j+2):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

        #borde derecho
        elif j == len(tablero[0])-1:
            for fila_i in range(i-1,i+2):
                for columna_j in range(j-1,j+1):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

        #bloques internos
        else:
            for fila_i in range(i-1,i+2):
                for columna_j in range(j-1,j+2):
                    if fila_i == i and columna_j == j:
                        minas = minas
                    else:
                        if "X" in tablero[fila_i][columna_j]:
                            minas += 1

    return minas

print(buscaminas([[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']],3,3))




