#Condicion if, retorna verdadero o falso segun se cumpla la condición, la cual es evaluada mediantes operadores de comparación

llueve = False
if llueve == True:
    print("Llevaré paraguas")
else:
    print("No llevaré paraguas")

#Es posible evaluar numerosas condiciones mediante el uso de elif.

llueve = True
temperatura = 12
if llueve == True and temperatura < 20:
    print("Llevaré paraguas y abrigo")
elif llueve == True and temperatura >= 20:
    print("Solo llevaré paraguas")
else:
    print("No llevaré paraguas")



