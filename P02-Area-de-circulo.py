# Calcula el Area de Circulo dado el raidio

import math # Importamos la libreria de funciones y constantes matematicas

print("Calcular el area de un circulo")


radio=float(input("Dame el radio: "))

area= math.pi * math.pow(radio,2)

# area=3.1416*radio*radio

print(f"Para un circulo de radio {radio} el area es: {area:.2f}")