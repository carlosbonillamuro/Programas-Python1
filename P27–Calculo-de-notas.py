# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario

print("Sacar el promedio de 5 calificaciones y mostrar mensaje")

n1,n2,n3,n4,n5 = float(input("Calificacion 1: ")),float(input("Calificacion 2: ")),float(input("Calificacion 3: ")),float(input("Calificacion 4: ")),float(input("Calificacion 5: "))
promedio = (n1+n2+n3+n4+n5)/5


if promedio >10 or promedio < 0:
    print("\nNo capturaste bien las calificaciones")
elif promedio > 9 and promedio <=10:
    print(f"\nPerfecto tu esfuerzo valió la pena... Tu promedio es: {promedio:.2f}")
elif promedio > 8:
    print(f"\nExcelente sigue igual... Tu promedio es: {promedio:.2f}") 
elif promedio > 7:
    print(f"\nMuy bien, puedes mejorar... Tu promedio es: {promedio:.2f}") 
elif promedio > 6:
    print(f"\nPasas de panzazo... Tu promedio es: {promedio:.2f}")
elif promedio >= 0:
    print(f"\nQuedas reprobado... Tu promedio es: {promedio:.2f}")

print("\nFin del programa")
 
    



