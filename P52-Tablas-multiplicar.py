# Imprimir la tabla del 1 a n, de 1 hasta m

import os

while(True):
    os.system("cls")
    n=int(input("Hasta que tabla quieres ? "))
    m=int(input("Hasta donde ? "))


    for i in range(1,n+1):
        print(f"\nTabla del {i}\n")
        for j in range(1,m+1):
            print(f"{i} * {j} = {i*j}")

     
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
            break    
print("\nPrograma terminado")
