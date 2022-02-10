numero1 = int(input("Número1: "))
numero2 = int(input("Número2: "))

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a,b):
    return a / b

def modulo(a,b):
    return a % b

print("La suma es " + str(suma(numero1, numero2)))
print("La resta es " +  str(resta(numero1, numero2)))
print("La multiplicación es " +  str(multiplicacion(numero1, numero2)))
print("La división es " +  str(division(numero1, numero2)))
print("El módulo es " +  str(modulo(numero1, numero2)))