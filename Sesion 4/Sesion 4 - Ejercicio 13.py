def precio(lista):
    segundo_elemento=[]
    for i in lista:
        segundo =i[1]
        segundo_elemento.append(segundo)
    return segundo_elemento

hola=[]
listas=[
    ("detergente",123),
    ("Coco",324),
    ("jakdjlfa",881)
]
hola.append(precio(listas))
print(hola)