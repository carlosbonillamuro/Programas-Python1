# Convertir grados Celcius a grados Farenheit y viseversa

print("Convertir grados Celcius a grados Farenheit y viseversa\n")
opcion = input("[C]entigrados a Farenheit o [F]arenheit a Celcius\nElije")

opcion = str.upper(opcion)

if opcion == "C":
    print("\n Convertir grados Farenheit a Celcius")
    temp = float(input("Dame la temperatura en grados Farenheit"))
    result = (temp-32)*5/9
    print(f"{temp} grados Farenheit equivalen a {result:.2f} Grados Celcius")  

else:
    print("\nConvertir grados Celcius a Farenheit")
    temp = float(input("Dame la temperatura en grados Celcius"))
    result = (temp* 9/5)+32 
    print(f"{temp} grados Celcius equivalen a {result:.2f} Grados Farenheit")

print("\nProceso terminado")
