# Lista de string
lista= ['manzana','pera','naranja','kiwi']
tupla= ('manzana','pera','naranja','kiwi')
cuerda = 'chino, kiwi, carne'
# lista de tuplas
lista_tuplas = [('marcas',90),('pera',34),('naranja',43),('kiwi',98)]
lista_tuplas_2=[(32,'mara'),(34,'pedro'),(10,'carla')]
resultado = 'kiwi' in lista
resultado_index = cuerda.index('i')
print(resultado)
print(resultado_index)
print(type(cuerda))

print('-----------------')
lista_tuplas.sort(reverse=True)
print(lista_tuplas)
print('-----------------')
def edad(anios):
    print(type(anios))
    return anios[0]
lista_tuplas.sort(key=edad)
print(lista_tuplas)