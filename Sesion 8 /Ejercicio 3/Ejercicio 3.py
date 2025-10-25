with open('compras.txt','w+') as archivo_texto:
    print('Que agrego a la lista de compras?, x para terminar')
    # compra es un str
    compra=input()
    while compra!='x':
        # write pasa una str con origen en compra y lo pasa a lista que es un objeto creado que representa un archivo de texto
        archivo_texto.write(compra+'\n')
        compra = input()
