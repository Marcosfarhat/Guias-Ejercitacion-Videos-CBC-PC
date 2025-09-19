lista = ['Juan','ana','Reuteman','clarita','zapatoad','iluminacion']
print(len(lista))
# for i in range(len(lista)):
for i in range(0):
    lista[i] = lista[i].lower()
lista.sort()
# print(' '.join(lista))
lista_1 = ' '.join(lista)
print(lista_1)
for i in lista:
    print(i)
