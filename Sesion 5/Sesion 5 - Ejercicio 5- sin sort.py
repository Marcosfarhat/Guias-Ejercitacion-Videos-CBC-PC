lista = [2,3,56,8,98,90]
nuevo_numero = int(input('ingresa un numero y te lo ordeno en la lista de menor a mayor'))

def busqueda_posicion(posicion):
    for i in posicion:
       print(i)
       if nuevo_numero < i:
            posicion = lista.index(i)
            return posicion

lista_con_busqueda= busqueda_posicion(lista)
print("lista con buqueda", lista_con_busqueda)

lista.insert(lista_con_busqueda,nuevo_numero)
print(" con la nueva posiscion ",lista)

