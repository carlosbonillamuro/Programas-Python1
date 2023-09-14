# Dividir un numero entero de 3 cifras (Unidades, Decenas y Centenas)

print("Dividir un numero entero de 3 cifras   - Centenas - Decenas - Unidades")

numero = int(input("Dame un numero de 3 cifras"))
centenas = numero // 100
residuo = numero -(centenas * 100)
decenas = residuo // 10
unidades = residuo - (decenas*10) 

print(f"Centenas {centenas}\nDecenas {decenas}\nUnidades {unidades}")
print("La suma de los numeros es, ",centenas+decenas+unidades)