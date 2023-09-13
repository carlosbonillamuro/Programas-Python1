# Calcular el area de un triangulo


import math # Importamos la libreria de funciones y constantes matematicas

print("Calcular el area de un triangulo conociendo la base y la altura")

print("Dame la base y la altura separado por un enter")

base,altura=int(input()),int(input())

area=base*altura/2

print(f"El triangulo de {base} y de altura {altura} es: {area:.2f}")
