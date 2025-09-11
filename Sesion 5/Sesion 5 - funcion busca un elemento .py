lista = [('manteca',354), ('pan', 876),('zapallo',983)]
def precio(valor):
    valor_elemento = []
    for elemento in valor:
        segundo_elemento = elemento[1]
        print(segundo_elemento)
        valor_elemento.append(segundo_elemento)
    return valor_elemento
precio_de_supermercado = precio(lista)
print('precio de supermercado',precio_de_supermercado)
busco = 'manteca' in lista
print('busco',busco)
print(lista.index(('manteca',354)))

