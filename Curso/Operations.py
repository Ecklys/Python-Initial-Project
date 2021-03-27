#Tipos de operacion y precedencia

'''
1. potencias -> ** (de derecha a izquierda)
2. operandos unitarios -> + o - (positivos o negativos)
3. multiplicación y división
4. suma y resta
5. operadores lógicos
'''

#Operaciones entre parentesis tienen precedencia 0

Suma = 3 + 54.2 + 0.123 - 4 - 13.5
print(Suma)

Multiplicacion = (6 * 2) / (4 * 5) // 0.17 % 0.5
print(Multiplicacion)

Potencia = 3**(2**4)
print(Potencia)



distancia = 1
tiempo = 900
tiempo_km = distancia / (tiempo / 3600)
tiempo_s = (distancia * 1000) / tiempo
resultado = 'La velocidad es ' +  str(tiempo_km) + ' km/h o ' + str(tiempo_s) + ' m/s'
print (resultado)