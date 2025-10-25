# creo un archivo de escritura pero no habilita lectura
archivo_creado=open('creo_un_archivo_de _escritura','w+')
archivo_creado.write('Escribimos algo \n')
# mal por que en modo 'w' no se puede usar ningun read..
''' a=archivo_creado.readlines()'''
archivo_creado.writelines(['elemento 1 de la lista\n','elemento 2 de la lista'])
archivo_creado.close()