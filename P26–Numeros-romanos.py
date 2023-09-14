# Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano

print("Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano\n\n")

numero = int(input("Dame un numero del 1 al 10 para convertirlo a Romano:  "))

if numero > 10 or numero < 1:
    print("\nEl numero que introduciste no esta dentro del rango")
else:
    if numero == 1:
        print("\nEl numero {numero} convertido en Romano es: I")
    elif numero == 2:
        print("\nEl numero {numero} convertido en Romano es: II")
    elif numero == 3:
        print("\nEl numero {numero} convertido en Romano es: III")
    elif numero == 4:
        print("\nEl numero {numero} convertido en Romano es: IV")
    elif numero == 5:
        print("\nEl numero {numero} convertido en Romano es: V")
    elif numero == 6:
        print("\nEl numero {numero} convertido en Romano es: VI")
    elif numero == 7:
        print("\nEl numero {numero} convertido en Romano es: VII")
    elif numero == 8:
        print("\nEl numero {numero} convertido en Romano es: VIII")
    elif numero == 9:
        print("\nEl numero {numero} convertido en Romano es: IX")
    elif numero == 10:
        print("\nEl numero {numero} convertido en Romano es: X")
        
print("\nFin del programa")