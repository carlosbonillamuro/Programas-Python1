# Estudiante

estudiante = {
    'nombre' : 'Juan Perez',
    'edad' : 45,
    'correo' : 'jperez@msn.com',
    'carrera' : 'Sistemas'
}

print(f"\nDiccionario original: \n {estudiante}")
estudiante['calificacion']=9.5
estudiante['correo']='juanp@gmail.com'
print(f"\nDiccionario actualizado \n {estudiante}")

print("\nLas Llaves: ")
for k in estudiante.keys():
    print(k,end=" ")

print("\n Valores")    
for v in estudiante.values():
    print(v,end=" ")

print("\n Llaves y valores a la vez")


for k , v in estudiante.items():
    print(f"{k:<12} : {v}")