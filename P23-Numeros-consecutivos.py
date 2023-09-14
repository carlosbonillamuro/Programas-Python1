# Dados tres números enteros, verificar si son consecutivos

print("Dados tres números enteros, verificar si son consecutivos\n")

n1 = int(input("Dame el numero 1: "))
n2 = int(input("Dame el numero 2: "))
n3 = int(input("Dame el numero 3: "))

if (n2==n1+1 and n3==n2+1) or (n2==n3+1 and n1==n2+1):
    print("Los numeros son consecutivos")
else:
    print("Error... Los numeros no son consecutivos")

print("Fin de programa")