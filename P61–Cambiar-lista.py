# Cambiar los elementos de una lista

import os

while(True):
    os.system('clear')
    nums = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]
    
    print(nums,len(nums))
    print(type(nums))   
    nums[0]=7
    nums[1]=7
    print(nums)
    nums[2:5]= [9,9,9]
    print(nums)
    nums[-1]= 6
    print(nums)
    nums[6]=nums[6]+5
    print(nums)
        
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("Programa terminado")