# Imprime los numeros del 1 al x de 10 en 10
import os

while(True):
    os.system("cls")

    x=int(input("Hasta que numero quieres llegar? "))

    print('Numeros del 1 al n con incrementos de 10 en 10 con for \n')
    n=0
    for n in range(1,x+1,10):
        print(n,end=' ')
        
    res=input('\n\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
            break    
print("\nPrograma terminado")
