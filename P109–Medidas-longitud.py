#Programa que convierte Centimetros a Pulgadas y Pies a Metros

def centimetros(medida):
    return(medida*2.54)

def pies(medida):
    return(medida*3.281)

#Programa principal
print("[ C ] Centometros to Pulgadas")
print("[ P ] Pies to Metros")

op=input("Elije: ").upper()


if op=="C":
    medida=int(input("Dame los centimetros: "))
    print(f"Las pulgadas son {centimetros(medida)}")
elif op=="P":
    medida=int(input("Dame los pies: "))
    print(f"los centigrados son {pies(medida)}")
else:
    print("Opcion incorrecta")
