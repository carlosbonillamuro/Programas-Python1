# Imprime la tabla de multiplicar deseada del 1 al n
import os
while(True):
    os.system('cls')
    t = int(input('Que tabla quieres? '))
    n = int(input('Hasta donde la quieres? '))
    c = 1
    while( c <= n):
        print(f'{t}\tx\t{c}\t={t*c}')
        c=c+1
    res=input('Deseas Continuar(S/N)? ')
    if res.upper()=='N':
        break

print("Gracias por utilizar este programa...")
