# Aceptar Estudiante en base a su edad y sus calificaciones

print("Aceptar Estudiante en base a su edad y sus calificaciones")

nombre = (print(input("Dame tu nombre:?")))
edad = int(input("Dame tu edad:?"))

if edad >= 18:
    print("Continuamos")
    print("Dame dos calificaciones separados por un Enter")
    c1,c2= int(input()),int(input())
    if c1>=8 and c2>8:
        print(f"{nombre} Bienvenido tus calificaciones son aceptadas {c1} y {c2}")
    else:
        print("Solo aceptamos calificaciones mayores a 8")
else:
    print("Solo aceptamos mayores de 18")

print("Proceso terminado")