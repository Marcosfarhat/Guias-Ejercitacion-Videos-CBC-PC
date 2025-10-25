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
total = sum(item['precio'] * item['cantidad'] for item in diccionario2)


# ticket(diccionario2)
print(total)