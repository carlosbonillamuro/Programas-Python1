# Imprime la tabla de multiplicar deseada del 1 al n
import os
while(True):
    os.system('clear')
    t = int(input('Que tabla quieres? '))
    n = int(input('Hasta donde la quieres? '))
    c = 1
    while( c <= n):
        print(f'{t} x {c} = {t*c}')
        c+=1
    res=input('Deseas Continuar(S/N)? ')
    if res.upper()=='N':
        break

print("Gracias por utilizar este programa...")