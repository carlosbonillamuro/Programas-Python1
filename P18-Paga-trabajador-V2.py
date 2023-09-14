# Calcula la paga de un trabajador, las horas extras se pagan doble

print("Calcula la paga de un trabajador, las horas extras se pagan doble\n")

nombre = input("Nombre:          \n")
horas = int(input("Horas trabajadas: \n"))
paga = float(input("Paga x Hora:     \n"))

if horas > 40:
        extras = horas -40
        total = (40*paga)+(extras*paga*2)
else:
    total = paga*horas

print(f"{nombre} Trabajo {horas} Horas, con paga de {paga}, Horas extra {extras}, Dando un total de {total:.2f}")