# Encuentra cual es el numero mayor de una secuencia de numeros

import os

while(True):
    os.system('cls')
    num2=0
    while (True):  
        num = float(input('Dame un número para determinar si es mayor, para salir preciona (cero) [0]:  '))
        if num == 0:
            break
        else:
            if num >num2:
                num2 = num
            
    print(f"\n El numero Mayor fue {num2}")    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")