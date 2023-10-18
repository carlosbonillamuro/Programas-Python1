# Crear un diccionario de los dias de la semana

semana = {
    '1' : 'Lunes', '2' : 'Martes', '3' : 'Miércoles', '4' : 'Jueves', '5' : 'Viernes', '6' : 'Sabado', '7' : 'Domingo'}

for v in semana.values():
        print(v,end=" ")
    
print(f"\nPrimer Elemento:  {semana['1']}")
print(f"\nUltimo Elemento:  {semana['7']}")
print(f"\nQuinto Elemento:  {semana.get('5')}")
print(f"\nSeptimo Elemento:  {semana.get('7')}")

print(f"\nDiccionario \n {semana}")