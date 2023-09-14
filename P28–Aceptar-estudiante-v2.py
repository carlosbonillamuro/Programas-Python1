# Criterio de acceso a la Universidad Kitty Kat SA

# Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el 
# estudiante  es aceptado. La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años 
# con un # promedio de entre 8 y 9.5.

print("Acceso a la Universidad Kitty Kat SA")
sexo = input("Sexo [F]emenino [M]asculino  ")
sexo = str.upper(sexo)

if(sexo == "F"):
    nombre = input("Nombre:          ")
    edad = int(input("Edad:   "))
    n1,n2,n3 = float(input("Calificacion 1: ")),float(input("Calificacion 2: ")),float(input("Calificacion 3: "))
    promedio = (n1+n2+n3)/3
    if edad < 21 or promedio >10 or promedio < 0:
        print("\nNo Tienes la edad necesaria")
    else: 
        if (promedio >=8 and promedio <= 9.5) :
            print(f"\nFelicidades {nombre}, eres apto para entar a la Universidad Kitty Kat SA, \n\nCon un promedio de {promedio:.2f}")
        else:
            print("No cumples con el criterio para entar a la Universidad Kitty Kat SA")
else:
    print("Lo siento Esta universidad es solo para Mujeres")




