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