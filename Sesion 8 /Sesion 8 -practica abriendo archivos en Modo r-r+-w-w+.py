# creo un archivo de escritura pero no habilita lectura
archivo_creado=open('creo_un_archivo_de _escritura','w+')
archivo_creado.write('Escribimos algo \n')
archivo_creado.writelines(['elemento 1 de la lista\n','elemento 2 de la lista'])
archivo_creado.seek(0)
a=archivo_creado.read()
print(a)
archivo_creado.close()

with open('creo_un_archivo_de _escritura','r') as archivo:
    lineas=archivo.readlines()
    for i in lineas:
        print('elemento en lineas: ',i)
    print('Archivo leido con readlines *lista* por el formato with open() as',lineas)

with open('creo_un_archivo_de _escritura','r') as archivo:
    lineas=archivo.read()
    print('Archivo leido *read*str- por el formato with open() as',lineas)