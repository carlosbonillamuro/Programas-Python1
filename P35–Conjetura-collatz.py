# Calcula la conjetura de Collatz
import os
while(True):
    os.system('clear')
    print('Imprime la conjetura de collatz')
    num = int(input('Dame un número = '))
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