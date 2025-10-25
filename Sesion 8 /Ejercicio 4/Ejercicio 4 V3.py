print('ingresela palbra a reemplazar')
palabra_reemplazar=input()
print('Palabra que reemplaza ')
palabra_reemplazante=input()

with open('paco_peco.txt', 'r') as archivo:
    contenido = archivo.readlines().replace(palabra_reemplazar, palabra_reemplazante)

with open('paco_peco.txt', 'w') as archivo:
    archivo.write(contenido)