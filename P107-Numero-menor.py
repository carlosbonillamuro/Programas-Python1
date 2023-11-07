# Menor de 3 numeros

def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m :
            m = lista[n]

    return m
def leerdatos():
    datos=[]
    while True:
        d=int(input("número: "))
        if d==-1:
            break;
        datos.append(d)
    return datos
# Programa principal
print("Dame una lista con 3 numeros enteros [-1] para salir")

nums = leerdatos()
print(f'Lista de números: {nums}')
men = menor(nums)
print('Resumen estadistico: \n')
print(f'Total numeros : {len(nums)}')
print(f'El menor : {men}')

