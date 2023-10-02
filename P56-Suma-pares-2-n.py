# Imprime los numeros pares de 2 a n y su suma
import os

while(True):
    os.system("cls")

    x=int(input("Hasta que numero quieres llegar? "))
    sum = 0
    print('Numeros del 2 al n con incrementos pares con for \n')
    
    for n in range(2,x+1,2):
        print(n,end=' ')
        sum = sum + n
    print(f"\n\nLa suma es: {sum}\n")    
    res=input('\n\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
            break    
    
    
print("\nPrograma terminado")
