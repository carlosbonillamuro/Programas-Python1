#Calcula factoriales

def factorial(n):
    f=1
    for n in range(1,n+1):
        f=f*n
    return f

def leer():
    lista = []
    fa = []
    while True:
        n = int(input('Numero :'))
        if n==-1: break
        else:
            fact=factorial(n)
            lista.append(n)
            fa.append(fact)
    return lista,fa

#Programa principal
import os
os.system("cls")
    
print("Dama una lista de numeros enteros : press [-1] para terminar")
lista = leer()

print(f"La lista original y los factoriales son: {lista}")
