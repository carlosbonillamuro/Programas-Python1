# Eliminar diccionario

municipios={
    'Apozol' : 1863,
    'Calera' : 1868,
    'Fresnillo' : 1554,
    'Guadalupe' : 1821,
    'Jalpa' : 1824,
    'Jerez' : 1824,
    'Loreto' : 1931,
    'Mazapil' : 1824,
    'Momax' : 1857
}
print(f"\n\nDiccionario \n {municipios}")

del municipios['Apozol']
print(f"\n\nDiccionario \n {municipios}")
municipios.pop('Fresnillo')
print(f"\n\nDiccionario \n {municipios}")
municipios.popitem()
print(f"\n\nDiccionario \n {municipios}")
municipios.clear()
print(f"\n\nDiccionario \n {municipios}")