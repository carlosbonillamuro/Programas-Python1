# Inscripcion a Evento academico

import os

while(True):
    os.system('cls')

    print("Universidad Patio SA de CV\n")
    print("Sistema de Inscripción Congreso de Sistemas\n\n")

    while (True):
        usuario = int(input('Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ?  '))
        if usuario == 1 or usuario == 2 or usuario ==3 : break
        else: 
            print("La opcion seleccionada no es Valida... las opciones validad solo son [1] [2] [3]  ")

    if usuario == 1:
        costo=100
        cliente = "Alumno"
        descuento = 0.2
    else:
        if usuario == 2:
            costo=200
            cliente = "Trabajador"
            descuento = 0.1
        else:
            costo=500
            cliente = "Docente"
            descuento = 0.05
    while (True):
        paquete = int(input('Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ?  '))
        if paquete == 1 or paquete == 2 or paquete ==3 : break
        else:
            print("La opcion seleccionada no es Valida... las opciones validad solo son [1] [2] [3]  ")

    if paquete == 1:
        costo2=600
        evento="Solo conferencias"
    else:
        if paquete == 2:
            costo2=800
            evento="Con eventos sociales"
        else:
            costo2=900
            evento="Con kit de acceso"

    cantidad=int(input('Cantidad ?  '))
    subtotal=(cantidad*costo)+(cantidad*costo2)
    desc = subtotal*descuento
    total=subtotal-desc
    print(f"\n\nTu pedido fue: {cantidad}, Tipo de Usuario: {cliente}, Tipo de paquete: {evento} \n")
    print(f"Subtotal: ${subtotal:.2f}, Con un descuento de: ${desc:.2f} por ser {cliente} de ({descuento*100}%) y un total de ${total:.2f})")
    
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break
print("\nProceso terminado")
