# Tabla de conversion de Peso a Dollar
import os
print("Tabla de conversion de Peso a Dollar")
tc =17.13;tcl=21.22
while (True):
    os.system('cls')
    while(True):
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        if (pi<pf):
            break
    c = pi
    print("\nPesos\tDollar\tLibra")
    print("-"*25)
    while c<=pf :
        print(f'{c}\t{c/tc:.4f}\t{c/tcl:.4f}')
        c+=1
    print("-"*25)
    res = input('Deseas Continuar(S/N)? ')
    if res.upper()=='N': break

print("\nProceso terminado....")
