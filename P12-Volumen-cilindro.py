# Calcula el volumen de un cilindro

import math
print("Calcularemos el volumen de un cilindro\n")

radio = float(input("dame radio del cilindro:    "))
altura = float(input("dame la altura del cilindro:  "))

if radio >0 and altura >0:
    volumen = math.pi * (radio**2) * altura
    print(f"El Volumen del Cilindro es: {volumen:.2f}m3")
else:
    print("valores no validos")

print("Programa Terminado")