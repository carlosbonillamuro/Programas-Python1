#Da un numero entre 1 y 7 y refresa el dia de la semana

#regresa una letra y un mensaje de acuerdo al promedio

def diasem(dia):
    letra=""
    if dia==1:
        letra="Lunes"
    elif dia==2:
        letra="Martes"
    elif dia==3:
        letra="Miercoles"
    elif dia==4:
        letra="Jueves"
    elif dia==5:
        letra="Viernes"
    elif dia==6:
        letra="Sabado"
    elif dia==7:
        letra="Domingo"
    return letra

#Programa principal

dia=int(input("Dame tu promedio entre 1 y 7: "))

if dia>7:
    print(dia)
    print("Dia de la semana no valido")
else:
    
    letra=diasem(dia)
    print(f"El dia de la semana escrito fue: {dia} corresponde al dia de la semana: {letra}")

