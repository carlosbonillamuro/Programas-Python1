# Verifica si la suma de sos numeros es igual a un tercero

# 4 5 6       5 9 4      4 9 5      3 3 3      6 6 7

print("Dame tres numeros separados por espacio")

n1, n2, n3 = input().split()
n1, n2, n3 = {int(n1),int(n2),int(n3)}

if n1 + n2 == n3:
    print("n1+n2=n3")
elif n1 + n3 == n2:
    print("n1+n3=n2")
elif n2 + n3 == n1:
    print("n2+n3 == n1")
elif n1 == n2 == n3:
    print("Son Iguales")
else:
    print("Hay dos iguales o todos son diferentes")
    
print("Proceso terminado")