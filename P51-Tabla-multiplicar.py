## Imprimir la tabla de multiplicar que el usuario pida usando el ciclo for

import os

while(True):
    os.system("cls")
    
    t= int(input("Que tabla deseas?"))
    n= int(input("Hasta donde     ?"))
    
    for i in range(1,n+1):
        print(f"{t} * {i} = {t*i}")
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
            break
        
        
print("Programa terminado")

    