# Remover elementos de la lista
import os

while(True):
    nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
    print(nums,len(nums))
    nums.remove(99)
    print(nums,len(nums))
    nums.pop(8)
    print(nums,len(nums))
    nums.pop()
    print(nums,len(nums))
    nums.clear()
    print(nums,len(nums))
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("Programa terminado")