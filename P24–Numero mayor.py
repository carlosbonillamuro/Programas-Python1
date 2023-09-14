# Dados tres números enteros, verificar cual es el mayor

print("Dados tres números enteros, verificar cual es el mayor\n")

n1 = int(input("Dame el numero 1: "))
n2 = int(input("Dame el numero 2: "))
n3 = int(input("Dame el numero 3: "))

if n1>n2 and n1>n3:
    print(f"\nEl numero {n1} es mayor Opcion 1\n")
elif n2>n3:
    print(f"\nEl numero {n2} es mayor Opcion 2\n")
else:
    print(f"\nEl numero {n3} es mayor Opcion 3\n")
    
print("Fin del programa")

    