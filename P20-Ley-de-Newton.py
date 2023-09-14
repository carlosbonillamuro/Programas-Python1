# Calcula la segunda Ley de Newton

print("[F]uerza    F = m * a\n")
print("[M]uerza    m = F / a\n")
print("[A]uerza    a = F / m\n")

op = input("Elige  ?").upper()

if op == "F":
    print("Calculando la Fuerza")
    m=int(input("Dame la masa"))
    a=int(input("Dame la Aceletacion"))
    f=m*a
    print(f"\nLa Fuerza es {f:.2f} ")    

elif op == "M":
    print("Calculando la Masa")
    f=int(input("Dame la fuerza"))
    a=int(input("Dame la Aceletacion"))
    m=f/a
    print(f"\nLa Masa es {m:.2f} ")    

elif op == "A":
    print("Calculando la Aceleracion")
    f=int(input("Dame la fuerza"))
    m=int(input("Dame la Masa"))
    a=f/m
    print(f"\nLa Aceleracion es {a:.2f} ")    

else:
    print("\nOpcion invalida")

print("\nProceso Terminado") 