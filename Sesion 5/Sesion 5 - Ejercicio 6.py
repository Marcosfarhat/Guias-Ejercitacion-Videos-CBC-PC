lista_string = ['carne','carne','jamon','humita','humita']
# fuera = lista_string.count(lista_string)
# print(fuera)
def doble(empanadas):
    print(empanadas)
    for i in empanadas:
        cantidad = lista_string.count(i)
        return i,cantidad

lista_contable = doble(lista_string)
print(lista_contable)
