# Calcula la conjetura de Collatz
import os
while(True):
    os.system('cls')
    print('Imprime la conjetura de collatz')
    while (True):  
        num = int(input('Dame un número positivo = '))
        if num > 0: break
        else:
            print("El numero tiene que ser mayor a cero")
    while num != 1: # Al llegar a 1 salir
        print(num,end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num,end=' ')
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
    
print("\nProceso terminado")
