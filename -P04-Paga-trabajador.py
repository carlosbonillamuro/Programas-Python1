#Calcula el salario total de un trabajador

print("Calcula la paga total de un trabajador \n")

nombre = input("Dame tu nombre: ")
horas = int(input("Horas trabajadas"))
paga = float(input("Paga por hora"))

tasa = 0.03

pagabruta = horas*paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("\nResumen de pagos\n")

print(f"{nombre} trabajo {horas} con paga por hora de: {paga} pesos a una tasa de {tasa}")
print(f"\nImpuesto {impuesto}")
print(f"\nPaga Neta {paganeta}")