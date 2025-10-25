lista = []
diccionario={
    'Producto 1': ('clavo',13,55),
    'Producto 2': ('tuerca',  12,  75),
    # 'Producto 3': ('silla',  17,  85)

}



# monto=float
def f_ticket(dic):
    print(lista)
    lista.append(dic)
    total=sum(valor[1]*valor[2] for valor in dic.values())
    print(total)


    return lista

f_ticket(diccionario)
print(lista)

