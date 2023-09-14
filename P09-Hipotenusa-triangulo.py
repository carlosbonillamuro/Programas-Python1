# Calvula la Hipotenusa de un triangulo Rectangulo

import math

print("Calvular la Hipotenusa de un triangulo Rectangulo\n")

catop = float(input("Dame el Cateto opuesto:\n"))
catad = float(input("Dame el Cateto adyacente:\n"))

print("Calculo de teorema de pitagoras igual a la raiz de la suma de los catetos")

hipotenusa = math.sqrt((catop**2)+(catad**2))
print(f"La Hipotenusa del tiangulo rectangulos cuyos Catetos son {catop} y {catad} es: {hipotenusa:.2f}")
