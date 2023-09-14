# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

print("Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos\n")

horas = int(input("Dame la cantidad de horas a convertir:  \n")) 

if horas > 1 :
    dias = horas // 24
    horas2 =horas % 24
    minutos = horas * 60
    segundos = minutos *60
    print(f"Las horas capturadas equivalen a {dias} dias, {horas2} horas\n")
    print(f"Los minutos son: {minutos} y los segundos son: {segundos}\n")
else: 
    print("informacion invalida")

print("Programa terminado")
    