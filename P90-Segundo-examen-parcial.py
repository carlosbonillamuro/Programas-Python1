# Segundo examen parcial

import os; os.system('cls')


inicial = ['T', 'P', 'A','Q','I']
ingredientes = ['Tomate', 'Peperoni', 'Aguacate', 'Queso', 'Piña']
precios = [1.5, 3.50, 0.40, 3.74, 2.10]

print(f'Lista de ingredientes : \n{ingredientes}\n')
print(f'Lista de precios: \n{precios}\n')
mezcla = dict(zip(ingredientes,precios))
print(f"\n\nDiccionario \n {mezcla}")

cadena = input("Dame el conjunto de ingredientes que quieres calcular T:Tomate P:Peperoni A:Aguacate Q:Queso I:Piña")
a=set(cadena)

if 'T' in a or 'P' in a or 'A' in a or  'Q' in a or  'I' in a:
    t = "T"
    contador = 0
    for letra in cadena:
        if letra == t:
            contador += 1
    totalt=contador


    p = "P"
    contador = 0
    for letra in cadena:
        if letra == p:
            contador += 1
    totalp=contador
    a = "A"
    contador = 0
    for letra in cadena:
        if letra == a:
            contador += 1
    totala=contador
    q = "Q"
    contador = 0
    for letra in cadena:
        if letra == q:
            contador += 1
    totalq=contador
    i = "I"
    contador = 0
    for letra in cadena:
        if letra == i:
            contador += 1
    totali=contador
    s=c=0
    for k , v in mezcla.items():
        print(f"{k:<12} : {v}")
        print(k)
        print(v)
        
        if k == "Tomate":
            totalt = totalt * v
        if k=='Peperoni':
            totalp = totalp * v
        if k=='Aguacate':
            totala = totala * v
        if k=='Queso':
            totalq = totalq * v
        if k=='Piña':
            totali = totali * v
    subtotal=totalt+totalp+totala+totalq+totali+15      
    print(f"Ingredientes de tu pizza {cadena}")
    print(f'\nEl subtotal es:: {subtotal:.2f}')   
    if subtotal>30:
        total=(subtotal*0.5)+15
    else:
        total=subtotal 
    print(f'\nEl total es es:: {total:.2f}')
else:
    print(f"Ingredientes de tu pizza {cadena}")
    print("No seleccionaste ingredientes validos")