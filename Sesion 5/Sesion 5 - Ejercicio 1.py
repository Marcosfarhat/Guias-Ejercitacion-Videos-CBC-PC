# Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
cuerdas = ("papapnota chetitotu")
def cuerda(vocales):
    vocal = "aeiouAEIOU"
    for i in vocales:
        for letras in i:
            if letras in vocal:
                print(letras)

cuerda(cuerdas)

'''



lista= ['manzana','pera','naranja','kiwi']
for palabra in lista:
    # list_palabras = list(i)
    for letra in palabra:
        if letra == 'a':
             print('if',letra, type(letra))
    # print(list_palabras)
mapeo = list(map(cuerda,lista))

# print('mapeo',type(mapeo))



 print(mapeo)
nueva_lista = list(filter(cuerda,lista))
print('nueva lista',nueva_lista)
for i in nueva_lista:
    print(i)

'''

# print(type(cuerdas))
