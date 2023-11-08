#Estadistica basica
# Promedio y mayores que el promedio
def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)
def mayor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m :
            m = lista[n]

    return m
def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m :
            m = lista[n]

    return m
def varianza(lista):
    s = 0
    sx = 0
    x=promedio(nums)
    for n in lista:
        sx = (n-x)**2
        s=sx+s
    return s / len(lista)

def leerdatos():
    datos=[]
    while True:
        d=int(input("número: "))
        if d==-1:
            break;
        datos.append(d)
    return datos

#Programa principal
import os
import math
os.system("cls")
nums = leerdatos()
prom = promedio(nums)
print(f'Lista de números: {nums} y son {len(nums)}')
print(f'La media es : {prom}')
may = mayor(nums)
men = menor(nums)
var = varianza(nums)
print(f'El mayor : {may}')
print(f'El menor : {men}')
print(f'La varianza : {var:.3f}')
print(f"La desviacion Estandar es: {math.sqrt(var):.3f}")