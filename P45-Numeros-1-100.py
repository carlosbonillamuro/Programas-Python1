# Imprime los numeros del 1 al x 

x=int(input("Desde donde comenzar a decender"))
y=int(input("De cuanto quieres aumentar"))

print('Numeros del 1 al 100 con for \n')
for n in range(1,x+1,y):
    print(n,end=' ')