# Cuenta numeros, los suma, cuenta positivos, negativos y ceros, se detiene al introducir 999
import os
cuenta = suma =cp =cn =cc = 0
os.system("cls")
while(True):
    numero = int(input("Numero? "))
    if numero != 999:
        cuenta = cuenta + 1
        suma = suma + numero
        if numero > 0:
            cp = cp + 1
        elif numero < 0:
            cn = cn + 1
        else:
            cc = cc +1  
    else:
        break

print(f"Se introdujeron {cuenta} numeros")
print(f"La suma de los numeros es: {suma}")
print(f"La suma de los numeros positivos es: {cp}")
print(f"La suma de los numeros negativos es: {cn}")
print(f"La suma de los ceros son: {cc}")