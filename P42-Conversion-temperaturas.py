# Convertir Temperatura 

import os

while(True):
    os.system('cls')
    while (True):  
        temp1 = int(input('Dame la temperatura inicial en °C: '))
        temp2 = int(input('Dame la temperatura final en °C: '))
        if  temp2 > temp1:
            break
        else:
            print("La temperatura final debe de ser mayor a la inicial")
    far1 = (temp1* 9/5)+32
    far2 = (temp2* 9/5)+32
    print(f"\n La convercion a Farenheit inicial es: {far1} y la final es {far2}\n")

    while (True):  
        if far1 >= far2:
            break
        else:
            print(f"{far1}")
            far1 = far1 + 1        
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")

