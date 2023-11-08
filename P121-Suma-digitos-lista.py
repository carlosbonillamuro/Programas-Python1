#Suma de digitos de la lista

def sumadigitos(n):
    suma=0
    while n!=0:
        dig=n%10
        suma=suma+dig
        n=n//10
    return suma

def leer():
    lista = []
    su = []
    while True:
        n = int(input('Numero :'))
        if n==-1: break
        else:
            suma=sumadigitos(n)
            lista.append(n)
            su.append(suma)
    return lista,su

#Programa principal
import os
os.system("cls")
    
print("Dama una lista de numeros enteros : press [-1] para terminar")
lista = leer()
su=leer()
print(f"La lista original y las sumas son: {lista}")
