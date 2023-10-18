# Acceder a los elementos de una lista

import os; 
while(True):
    os.system('clear')
    #        1    2    3    4    5    6    7    8    9    10       
    nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
    #       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1                  
    
    print(f'Primero Elemento : {nums[0]}\n')
    print(f'Primero Elemento : {nums[-1]}\n')
    print(f'Elemento 999 : {nums[4]}\n')
    print(f'Del 2 al 5 : {nums[1:5]} \n')
    print(f'Del 1 al 4 : {nums[0:4]} \n')
    print(f'Los elementos del 222 en adelante : {nums[3:]} \n')
    print(f'Los últimos 3 : {nums[-3:]} \n')    
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
            
print("Programa terminado")
