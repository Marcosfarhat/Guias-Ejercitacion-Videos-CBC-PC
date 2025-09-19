def ordenar(palabra):
    palabra = palabra.lower()
    cant=0
    for v in ('a','e','i','o','u'):
        cant += palabra.count(v)
    return cant
lista = ['Juan', 'ana', 'Reuteman', 'clarita', 'zapatoad', 'iluminacion']

for i in range(len(lista)):
     lista[i] = lista[i].lower()
print(type(lista))
print("lista despues de lower ",lista)
# lista.sort(key=ordenar)
print('Lista ordenada')
for i in lista:
    print(i)