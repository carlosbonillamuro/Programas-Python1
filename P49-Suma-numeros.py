# Imprime la suma y el promedio de n numeros introducidos por el usuario

n=int(input("Cuantos numeros deseas procesar ?"))

suma=0
promedio=0

for c in range(1,n+1):
    num=int(input(f"Numero {c}? "))
    suma=suma+num
    
print(f"la suma es: {suma} u el promedio es {suma/n:.2f}")