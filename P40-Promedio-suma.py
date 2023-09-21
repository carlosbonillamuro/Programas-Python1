# Da la suma y el promedio de los numeros dados, preciona 0 para salir

import os

while(True):
    os.system('cls')
    print('Imprime los numeros pares decsendientes menores a 100')
    su=0
    nu=0
    c=0
    
    while (True):  
        num = int(input('Dame un número entero cuando quieras salir preciona (cero) [0]:  '))
        if num == 0:
            break
        else:
            su=su+num
            c = c + 1
        
    print(f"\n La suma de los numeros capturados es: {su} y el promedio es: {su/c:.2f}")    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")
        

