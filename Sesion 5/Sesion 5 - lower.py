lista = ['Juan','ana','Reuteman','clarita','zapatoad','iluminacion']
print('Elementos de lista ')
for i in lista:
    print(i)
lista.sort()
print("lista ordenada |",lista)

lista = ['Juan','ana','Reuteman','clarita','zapatoad','iluminacion']
lista_lower = []
lista_lower_1 =[]
for i in lista:
    i = i.lower()
    lista_lower_1 = lista_lower.append(i)
    print('lista lower',lista_lower)