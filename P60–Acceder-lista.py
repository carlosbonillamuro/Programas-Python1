# Acceder a los elementos de una lista

import os; 
while(True):
    os.system('clear')
    #        1   2   3   4   5   6   7   8   9           
    nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
    #       -9  -8  -7  -6  -5  -4  -3  -2  -1                  
    
    print('Acceder a los elementos de una lista\n')
    print(f'Cuantos números son : {len(nums)} \n')
    print(f'Todos los números : {nums} \n')
    print(f'Primero y último : {nums[0]}, {nums[-1]} \n')
    print(f'Del 2 al 6 : {nums[2:6]} \n')
    print(f'Los primeros 3 : {nums[:3]} \n')
    print(f'Los últimos 3 : {nums[6:]} \n')
    print(f'Los de enmedio: {nums[2:5]} \n')
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
            
print("Programa terminado")
