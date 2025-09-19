lista_string = ['carne','carne','jamon','humita','humita']
nueva_lista = []
for i in lista_string:
    if i not in nueva_lista:
        print(nueva_lista)
        cantidad = lista_string.count(i)
        nueva_lista = i, cantidad
