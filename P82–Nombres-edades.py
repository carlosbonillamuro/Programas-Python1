# Nombres y edades
import os; os.system('cls')
datos = {}
print('Introduce nombres y edades, * en el nombre para terminar')
while True:
    nombre = input('Nombre ? ')
    if nombre == '*':
        break
    else:
        datos[nombre]=int(input('Edad : '))

print('\nLos datos introducidos son;\n',datos,len(datos))


print(f'El diccionario de datos creado: \n{len(datos)} - {datos}\n')
print('\nListado y promedio de edades:')
s=p=0
for n,e in datos.items():
    print(f'{n:<20} - {e:3}')
    s=s+e
p=s/len(datos)
print(f'\n\nLa Suma es: {s} y promedio es: {p:.2f}')