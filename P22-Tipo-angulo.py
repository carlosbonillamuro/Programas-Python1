# Muestra el tipo de Angulo
# <90° Angulo agudo, =90° Angulo recto, <180° Angulo obtuso, =180° Angulo llano, <360° Angulo concavo, =360° Angulo completo

angulo = int(input("Dame un angulo:"))

if angulo >=0 and angulo <= 360:
      if angulo < 90 and angulo > 0:
          print("Angulo agudo")
      elif angulo == 90:
          print("Angulo recto")
      elif angulo > 90 and angulo < 180:
          print("Angulo obtuso")
      elif angulo == 180:
          print("Angulo llano")
      elif angulo > 180 and angulo <360:
          print("Angulo concavo")
      elif angulo == 360 or angulo ==0: 
          print("Angulo completo")
else:
    print("Angulo fuera de rango")