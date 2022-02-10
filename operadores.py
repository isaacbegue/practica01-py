numero1 = 2
numero2 = 4

multiplicacion = numero1 * numero2
suma = numero1 + numero2
resta = numero2 - numero1
division = numero2 / numero1

print(multiplicacion)
print(suma)
print(resta)
print(division)

# Toda operación de división termina como número flotante

# si se desea eliminar los decimales en la división, se puede usar doble barra

divisionSinDecimales = numero2 // numero1

print(divisionSinDecimales)

modulo = numero1 % numero2

print(modulo)


# operador ternario
operadorTernario = "numero1 es mayor a número 2" if numero1 > numero2 else "hola"
print(operadorTernario)