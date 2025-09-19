cadena = 'abracadabra chupa cabra '
lista= [ 'aj s  kfl j  as ']
cadena_a_lista = sorted(cadena,reverse=True)
print(type(cadena_a_lista))
print(f'cadena organizada en una lista {cadena_a_lista}')
# LISTA de la cadena que le sacamos los espacios
cadena_a_lista_sin_espacios = ''.join(cadena_a_lista)

lista_a_cadena_sin_espacios = ''.join(lista)
print(type(lista_a_cadena_sin_espacios))
print("Cadena que ahora es una lista sin espacion {}".format(cadena_a_lista_sin_espacios))
