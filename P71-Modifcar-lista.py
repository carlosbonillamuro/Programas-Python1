# Modificar lista

import os

while(True):
    os.system('cls')
    nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
    print(nums)
    print("Remplazar 100 por 200")
    nums[0]=200
    print(nums)
    print("Remplazar 999 por 1000")
    nums[4]=1000
    print(nums)
    print("Remplazar 988 por 999")
    nums[-1]=999
    print(nums)
    print("Remplazar el rango [123,456,222] por [555,666,777]")
    nums[1:3]= [555,666,777]
    print(nums)
        
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("Programa terminado")

