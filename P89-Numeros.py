# Numeros
import os; os.system('cls')

conjunto1 = {50,60,70,80,90,100,200}
conjunto2={60,90,100,300,400,500}
conjunto3={10,20,60,90,70,100,600,700}

print(f"Conjunto 1 : {conjunto1}\nConjunto 2 : {conjunto2}\nConjunto 3 : {conjunto3}\n")

print("\nUnion: ")
print(f"conjunto1 union conjunto2 : {conjunto1.union(conjunto2)}")
print(f"conjunto2 union conjunto3 : {conjunto1 | conjunto3}")

print("\nDiferencia:")
print(f"conjunto1 diferencia conjunto3: {conjunto1.difference(conjunto3)}")

print("\nDiferencia simetrica:")
print(f"conjunto2 diferenia simetrica conjunto3:{conjunto2.symmetric_difference(conjunto3)}")

print("\nIntersección: ")
print(f"conjunto2 inteseccion conjunto3: {conjunto2.intersection(conjunto3)}")

print("\nProbar por subconjuntos:")
print(f"conjunto1 es subconjunto de conjunto2 ? :{conjunto1.issubset(conjunto2)} ")
print(f"conjunto3 es subconjunto de conjunto1 ? : {conjunto3<=conjunto1} ")

print("\nVerficar la presencia de un elemento en elconjunto:")
print(f" 100 esta en conjunto1 ? : {100 in conjunto1}")
print(f" 60 esta en conjunto1, en el conjunto2 y en el conjunto3 ? : {60 in conjunto1 and 60 in conjunto2 and 60 in conjunto3}")
print(f" 900 no esta en conjunto3 ? : {900 not in conjunto3}")