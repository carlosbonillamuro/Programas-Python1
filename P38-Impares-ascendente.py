# Numeros impares Acendente

import os

while(True):
    os.system('cls')
    print('Imprime los numeros ascendentes impares y los suma')
    while (True):  
        num = int(input('Dame un número positivo = '))
        if num > 0: break
        else:
            print("El numero tiene que ser mayor a cero")
    c=1
    su=0
    while c <= num:
        
        if c % 2 == 1:
            print(f'{c}\t ')
            su = su + c
            c = c+1 
        else:
            c=c+1     
    print(f"\n La suma de los impares es: {su}")    
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")