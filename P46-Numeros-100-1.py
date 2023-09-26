# Numeros de x a con decrementos de y con for

x=int(input("Desde donde comenzar a decender"))
y=int(input("De cuanto en cuanto desiende"))

print('Numeros del 100 al 1 \n')
for x in range(x,0,-y):
    print(x,end=' ')