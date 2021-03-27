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

print(exponente_max(128))


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