lista_palabras = [
    'juan',
    'mesa',
    'pileta',
    'auto',
    'cebra',
    'semanforo',
    'planta'
]
cuerdas = 'hola manotas como estas'
def mapeo(palabra):
    return palabra[0:4]
mapeos = map(mapeo,lista_palabras)
print(list(mapeos))

mapeos = map(mapeo,cuerdas)
print('lista el string',list(mapeos))




