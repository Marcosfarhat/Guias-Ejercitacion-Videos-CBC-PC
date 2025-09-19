from os.path import split

lista = ['Juan','ana','Reuteman','clarita','zapatoad','iluminacion']

lista.sort(key=len)
print(f'listas antes de minuscula {lista}')
for i in range(len(lista)):
    lista[i]=lista[i].lower()

print(f'listas despues de minuscula {lista}\n')
print("lista ordenada ")
lista_1 = ' '.join(lista)
print(lista_1)
# lista_1=list(lista_1)

print(type(lista_1))
lista_1 = 'ana juan clarita reuteman zapatoad iluminacion'
lista_1.split(',')
print(lista_1)
'''
for i in lista_1:
    print(i)
'''
