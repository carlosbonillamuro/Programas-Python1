# Lista de numeros, promedio

import os

while(True):
    os.system('cls')
    print('Inserta numeros enteros y agregarlos a una lista')
    su=0
    nu=0
    c=0
    nums=[]
    
    while (True):  
        num = int(input('Dame un número entero cuando quieras salir preciona [0]:  '))
        if num==0:
            break
        else:
            nums.insert(c,num)
            #nums.append(num)
            su=su+num
            c = c + 1
    
    print(f"\n\nSe registraron {c} elementos a la lista La suma de los numeros capturados es: {su} y el promedio es: {su/c:.2f}\nCuya lista fue:\n")
    print(nums)
       
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")
