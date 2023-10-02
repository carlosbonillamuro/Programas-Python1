## Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:

import os

while(True):
    os.system("cls")

    n= int(input("Cuantos renglones ?"))

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print() 

    res=input('\n\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break    

    print("\nPrograma terminado")
## Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:

import os

while(True):
    os.system("cls")

    n= int(input("Cuantos renglones ?"))

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print() 

    res=input('\n\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break    

    print("\nPrograma terminado")