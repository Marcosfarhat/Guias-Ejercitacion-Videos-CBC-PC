lista = [2,3,56,8,98,90]
nuevo_numero = int(input('ingresa un numero y te lo ordeno en la lista de menor a mayor'))

def agregar_numero_y_ordeno(agrego):
    lista.append(agrego)
    lista.sort()
    return lista
agregar_numero_y_ordeno(nuevo_numero)
print(lista)