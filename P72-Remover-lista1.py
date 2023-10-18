# Remover eelementosd de la lista
import os

while(True):
    os.system('cls')
    nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
    print(nums,len(nums))
    
    ele=0
    c=0
    while(True): 
        nums.pop(ele)
        c=c+1
        if c==3:
            break
            
    print(nums,len(nums)) 
    nums.remove(322)
    nums.remove(988)
    print(nums,len(nums))
        
    nums.pop(0)
    print(nums,len(nums))
    x=len(nums)
    nums.pop(x-1)
    print(nums,len(nums))
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("Programa terminado")

