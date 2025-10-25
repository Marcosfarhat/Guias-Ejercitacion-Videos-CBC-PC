diccionario ={
    'producto':'clavo',
    'precio':12,
    'cantidad':10
}
diccionario2 ={
    'producto':'silla',
    'precio':12,
    'cantidad':10
}

lista=[]
def ticket(dic):
    lista.append(dic)
    total = sum(item['precio'] * item['cantidad'] for item in lista)
    print(total)
    return lista
ticket(diccionario)
# ticket(diccionario2)
print(lista)