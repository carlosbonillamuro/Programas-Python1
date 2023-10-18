# Procesar diccionario

import os; os.system('cls')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
print(f'Lista de materias : \n{nombres}\n')
print(f'Lista de calficaciones: \n{sueldos}\n')
mezcla = dict(zip(nombres, sueldos))
print(f"\n\nDiccionario \n {mezcla}")


print("\nLas Llaves: ")
for k in mezcla.keys():
    print(k,end=" ")

print("\n\n Valores")    
for v in mezcla.values():
    print(v,end=" ")

print("\n\nLlaves y valores a la vez")

s=c=0
for k , v in mezcla.items():
    print(f"{k:<12} : {v}")
    s+=v
    p=s/len(mezcla)
print(f'\nLa suma: {s} y el promedio: {p:.2f}')   


