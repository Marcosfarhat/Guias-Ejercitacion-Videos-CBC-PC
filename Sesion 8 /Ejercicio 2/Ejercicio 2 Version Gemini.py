
with open('regalo.txt', 'r') as nombres:
    nombre_pasaado_a_cadena = nombres.read().replace('\n', '')
print(nombre_pasaado_a_cadena)
