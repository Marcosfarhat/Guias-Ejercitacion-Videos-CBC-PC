print('ingresela palbra a reemplazar')
palabra_reemplazar=input()
print('Palabra que reemplaza ')
palabra_reemplazante=input()

with open('paco_peco.txt','r+') as archivo_texto:
    # pasa una LISTA
    x=archivo_texto.readlines()
    archivo_texto.seek(0)
    # lines es cada linea de la LISTA 'x'
    for linea in x:

        print(type(linea))
        # por eso puedo utilizar WRITE sobre el archivo 'archivo_texto' y REPLACE sobre el str (cadena de texto LINEA)
        archivo_texto.write(linea.replace(palabra_reemplazar,palabra_reemplazante))
