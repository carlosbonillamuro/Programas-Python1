# Personas
import os; os.system('cls')



conjunto1 = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
conjunto2={'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}
conjunto3={'Pedro', 'Mateo'}
conjunto4={'Reynaldo', 'Angelica'}

print(f"Conjunto 1 : {conjunto1}\nConjunto 2 : {conjunto2}\n")
print("\nUnion: ")
print(f"conjunto1 union conjunto2 : {conjunto1.union(conjunto2)}")

print("\nIntersección: ")
print(f"conjunto1 inteseccion conjunto2: {conjunto1.intersection(conjunto2)}")

print("\nDiferencia:")
print(f"conjunto1 diferencia conjunto2: {conjunto1.difference(conjunto2)}")

print("\nDiferencia simetrica:")
print(f"conjunto1 diferenia simetrica conjunto2:{conjunto1.symmetric_difference(conjunto2)}")

print("\nProbar por subconjuntos:")
print(f"conjunto3 es subconjunto de conjunto2 ? :{conjunto3.issubset(conjunto2)} ")

print("\nProbar por supersubconjuntos:")
print(f"conjunto1 es superconjunto de conjunto4 ? :{conjunto1.issuperset(conjunto4)}")


print("\nVerficar la presencia de un elemento en elconjunto:")
print(f" Pedro esta en conjunto1 ? : {'Pedro' in conjunto1}")
print(f" Lilia no esta en conjunto2 ? : {'Lilia' not in conjunto1}")