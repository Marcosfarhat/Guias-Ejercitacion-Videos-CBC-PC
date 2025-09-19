def cadena(palabra):
    return reversed(palabra)

cadenas = ('hola chirillo')
print(type(cadenas))
cadena_inversa = cadena(cadenas)
print(list(cadena_inversa))

cadena_inversa_2 = reversed(cadenas)
print(list(cadena_inversa_2))