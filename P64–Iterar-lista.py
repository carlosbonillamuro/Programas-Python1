# Iterar sobre los elementos de la lista
import os

while(True):
    os.system('cls')
    
    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    
    for num in nums:
        print(num, end=" ")
        
    for n in range(len(nums)):
        print(nums[n], end=" ")
    print()
    
    for num in nums:
        print(num+2, end=" ")
    print() 
    
    for n in range(len(nums)):
        print(nums[n]+10, end=" ")
        
    print("\n",nums)
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("Programa terminado")   
