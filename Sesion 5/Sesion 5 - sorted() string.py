from time import perf_counter
tupla= ('abracabrachupacabra',2)
cadena = 'abracabrachupacabra'
cadena_ordenada = sorted(cadena)
print(cadena_ordenada)
cadena_ordenada_sin_espacios = "".join(cadena_ordenada)
print(cadena_ordenada_sin_espacios)

print('--------------------')
print('con numeros')
tupla_numero = (10,3,0.3,-7)
# ordena la tupla pero la transforma en LISTA
tupla_numero_ordenada_como_lista = sorted(tupla_numero)
print("{} tupla ordenada como lista".format(tupla_numero_ordenada_como_lista))
tupla_numero_ordenada_como_tupla = tuple(tupla_numero_ordenada_como_lista)
print(f"tupla ordenada nuevamente como tupla {tupla_numero_ordenada_como_tupla}" )
print(type(tupla_numero_ordenada_como_tupla))