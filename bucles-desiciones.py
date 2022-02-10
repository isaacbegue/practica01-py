edad = 28
nombre = "Isaac"
edadLegal = 18

# Es muy importante la identanción en python ya que no se usan las llaves para determinar un bloque.

if edad >= edadLegal:
    print(f"Felicidades, {nombre}, ya eres mayor de edad.")
else:
    print(f"Hola {nombre}, aún eres menor de edad.")


#  loops en python
steps = 10

for i in range(steps):
    print(1+i)

steps = 10
i = 0

while(i < steps):
    i += 1
    print(i)