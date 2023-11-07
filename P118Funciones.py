# Creamos un modulo con las funciones

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
            
def promedio(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

def leer():
    lista = []
    while True:
        n = float(input('Numero :'))
        if n==1: break
        lista.append(n)
    return lista
