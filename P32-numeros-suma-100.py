# Imprime los numeros de 1 a 200 hasta alcanzar la suma 100

c = 0  #?
s = 0  #100
while c < 200:
    c = c + 1
    s = s + c
    print(c,end=" ")
    if s >=1500:
        print()
        break
    
print(f"Hemos alcanzado la cantidad limite {s} , sumando {c} numeros")
    