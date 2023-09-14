# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana

print("Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana\n\n")

dia = int(input("Dame un numero del 1 al 7 para determinar el dia de la demana:  "))

if dia > 7 or dia < 1:
    print("\nEl numero que introduciste no es un dia de la semana")
else:
    if dia == 1:
        print("\nDomingo")
    elif dia == 2:
        print("\nLunes")
    elif dia == 3:
        print("\nMartes")
    elif dia == 4:
        print("\nMiercoles")
    elif dia == 5:
        print("\nJueves")
    elif dia == 6:
        print("\nViernes")
    elif dia == 7:
        print("\nSabado")
        
print("\nFin del programa")