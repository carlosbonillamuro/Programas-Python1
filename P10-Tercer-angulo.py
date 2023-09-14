# Calcular el tercer Angulo de un triangulo

print("Encuentra el angulo desconocido del triangulo\n")

an1 = int(input("Dame el primer Angulo:  "))
an2 = int(input("Dame el segundo Angulo:  "))

if an1 + an2 >=180 or an1<=0 or an2<=0:
    print("Valores no pertenecen a un triangulo")
else:
    an3 = 180-(an1+an2)
    print(f"El angulo desconocido es: {an3}")

print("Fin del proceso")
