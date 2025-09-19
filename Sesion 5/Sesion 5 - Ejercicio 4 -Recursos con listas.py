lista = [ 'manzana','apio','zapallo']
ingrediente_nuevo = input('Ingrese el nuevo ingrediente a la lista: ')
if ingrediente_nuevo not in lista:
    lista.append(ingrediente_nuevo)

print(lista)
