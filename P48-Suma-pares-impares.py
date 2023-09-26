# Imprime los pares y su suma, los impares y su suma, en el rango de 1 a n

import os

while(True):
    os.system("cls")

    n=int(input("Hasta donde quieres llegar ?\n"))

    s=0

    print("Imprimier los numeros pares y su suma")

    for par in range(2,n+1,2):
        print(par,end=(" "))
        s=s+par
    print(f"La suma de los pares es: {s}")

    print("\nImprimier los numeros impares y su suma")

    s=0
    for impar in range(1,n+1,2):
        print(impar,end=(" "))
        s=s+impar
    print(f"La suma de los impares es: {s}")

    resp=input("Deseas continuar [S/N]").upper()

    if resp == "N": break

print("Proceso terminado")
