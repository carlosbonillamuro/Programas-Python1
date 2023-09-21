# Da la suma y el numero de datos y salir cuando la suma sea >=200

import os

while(True):
    os.system('cls')
    print('Da la suma y el numero de datos y salir cuando la suma sea >=200')
    su=0
    nu=0
    c=0
    
    while (True):  
        num = int(input('Dame un número entero menor a 200:  '))        
        
        su=su+num
        c = c + 1
        if su >= 200:
            su2=su-num
            c2=c-1
        
            break
    
    print(f"\nLa suma de los numeros capturados despues de 200 es: {su}\nY la cantidad de numeros despues de 200 fue: {c}\n")
    print(f"\nLa suma de los numeros capturados antes de 200 es: {su2}\nY la cantidad de numeros antes de 200 fue: {c2}")    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")
        

