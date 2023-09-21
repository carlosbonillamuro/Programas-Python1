# Imprime los numeros pares menores a 100 hasta el numero que el usuario quiera

import os

while(True):
    os.system('cls')
    print('Imprime los numeros pares decsendientes menores a 100')
    while (True):  
        num = int(input('Dame un número positivo menor a 100 '))
        if num > 0 and num <= 100:
            break
        else:
            print("El numero no esta dentro del rango")

    c=100
    su=0
    while num <= c:
        if c % 2 == 0:
            print(f'{c}\t ')
            su = su + c
            c = c-1 
        else:
            c=c-1     
    print(f"\n La suma de los impares es: {su}")    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break

print("\nProceso terminado")

        

