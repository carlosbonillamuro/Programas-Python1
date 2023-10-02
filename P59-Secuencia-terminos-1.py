## Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:

import os

sum=0
while(True):
    os.system("cls")
    n=int(input("Dame el numero del cual deseas los armonicos?:"))

    f=1 
    for h in range(1,n+1):
        print(f"1/{h}!")
        
        f=f*h
        x=1/f
        sum=sum+x
    
    
    print(f"\nLa suma de {n} armonicos es:  {sum}\n")
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
    
        
print("Programa terminado")
