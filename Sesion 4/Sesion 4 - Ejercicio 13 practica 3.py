lista = [("Carlos",12),('alberto',23),('viviana',54)]

def buscando_segundo(argumento):
    #  declaro dentro de la funcion a lista_de_segundo_elemento
    lista_de_segundo_elemento =[]
    for elemento in argumento:
        # elijo el segundo elemento de la tupla
        segundo_elemento= elemento[1]
        # Se lo agrego al final de la nueva lista
        lista_de_segundo_elemento.append(segundo_elemento)
        # los sumo
        suma = sum(lista_de_segundo_elemento)
    return suma
devolucion_de_la_funcion = buscando_segundo(lista)

print('EL total a pagar es ', devolucion_de_la_funcion)