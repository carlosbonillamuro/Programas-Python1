## Imprime el factorial de un numero
import os

while(True):
    os.system("cls")
    n=int(input("Dame el numero del cual deseas el factorial?:"))

    f=1 
    for h in range(1,n+1):
        print(h, end= "*")
        f=f*h
    
    print(f"\nEl Factorial es = {f}\n")
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
    
        
print("Programa terminado")
