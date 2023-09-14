# Uso de las funciones trigonometricas en Python

import math

print("Calculo de las funciones trigonometricas basicas")
angulo=float(input("Dame el angulo en grados"))
angrad=math.radians(angulo)

seno = math.sin(angrad)
coseno = math.cos(angrad)
tangente = math.tan(angrad)

salida = ('Resumen de funciones \n'
f'El seno es: {seno}\n'
f'El coseno es: {coseno}\n'
f'La tangente es: {tangente}\n'
f'El angulo {angulo} equivale a {angrad}')

print(salida) 
