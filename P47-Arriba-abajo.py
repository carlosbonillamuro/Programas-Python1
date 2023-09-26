# Imprimir los numeros de 1 a n o de n a 1, segun el usuario lo decida

import os

os.system("cls")

while(True)
    print("[1] Imprimr los numeros de 1 a n")
    print("[2] Imprimr los numeros de n a 1")

    op=int(input("Elige la opcion ..?"))

    if  op == 1:
        print("Imprime de 1 hasta n\n")
        n=int(input("Dame el valor de n?"))
        for z in range(1,n+1):
            print(z,end=(" "))
            
    elif  op == 2:
        print("Imprime de n hasta 1\n")
        n=int(input("Dame el valor de n?"))
        for w in range(n,0,-1):
            print(w,end=(" "))
            
    else: 
        print("Opcion invalida")
            
    resp=input("Deseas continuar [S/N]").upper()

    if resp == "N": break

print("Proceso terminado")
