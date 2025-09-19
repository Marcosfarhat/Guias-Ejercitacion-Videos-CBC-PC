def ordenar(palabra):
    # palabra = palabra.lower()
    cant=0
    for v in ('a','e','i','o','u'):
        cant += palabra.count(v)
    return cant
lista = ['Juan', 'ana', 'Reuteman', 'clarita', 'zapatoad', 'iluminacion']

lista_lower = lista.sort(key=str.lower)
lista.sort(reverse=True,key=ordenar)

print('Lista ordenada')
for i in lista:
    print(i)