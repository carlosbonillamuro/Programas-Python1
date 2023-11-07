# Suma de pares e impares

def leer():
    lista = []
    while True:
        n = int(input('Numero :'))
        if n==-1: break
        lista.append(n)
    return lista

def pares(lista):
    su=0
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
            su=su+n
    return su

def impares(lista):
    su=0
    p = []
    for n in lista:
        if n % 2 != 0:
            p.append(n)
        su=su+n
    return su
#Programa principal
import os

os.system("cls")
    
print("Dama una lista de numeros enteros : press [-1] para terminar")
lista = leer()

print("[ P ] Sumar pares")
print("[ I ] Sumar Impares")

op=input("Elije: ").upper()

if op=="P":
    res = pares(lista)
    print('La suma es: ', pares(lista))

elif op=="I":
    res = impares(lista)
    print('La suma es: ', impares(lista))
else:
    print("Opcion incorrecta")


