#Uso de while: permite ejecutar instrucciones internas de manera iterativa mientras la condición evaluada sea verdadera.

'''while condicion:
    instrucciones
'''

temp = 32
while temp < 73:
    celsius = "{:.2f}".format((temp-32)*(5/9))
    print("Hay", temp, "°F, lo cual corresponde a", celsius, "°C")
    temp+=1

#Uso de for: permite ejecutar instrucciones internas de manera iterativa durante un número determinado de veces.

temp = 32

for temp in range(45,61):
    print(temp, " ", "{:.2f}".format((temp-32)*(5/9)))


