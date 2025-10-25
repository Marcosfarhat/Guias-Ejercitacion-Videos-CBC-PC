
print('ingresela palbra a reemplazar')
palabra_reemplazar=input()
print('Palabra que reemplaza ')
palabra_reemplazante=input()

#Guardo el archivo en 'ARCHIVO_LECTURA' que despues voy autilizar para sobreescribir el original 'paco_peco'
# por eso lo abro en modo 'r'
archivo_lectura=open('paco_peco.txt','r')
# lo transformo en una lista con ' READLINES()' si escribo en el modo  '.READ()' lo transformo en una sola cadena que despues cuando lo quiera
# iterar va a leer caracter por caracter en vez de LINEA por LINEA si lo hago con '. READLINES()'
archivo_guardado=archivo_lectura.readlines()
archivo_lectura.close()

# abro el archivo en modo 'w' para poder sobreescribirlo comparandolo con el archivo de 'ARCHIVO_LECTURA'
archivo_escritura=open('paco_peco.txt','w')
# funciona por que 'ARCHIVO_GUARDADO '   es una LISTA
for linea in archivo_guardado:
    archivo_escritura.write(linea.replace(palabra_reemplazar,palabra_reemplazante))

archivo_escritura.close()
