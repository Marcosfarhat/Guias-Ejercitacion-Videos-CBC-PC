lista= ['manzana','pera','naranjas','kiwi']
def cortar_palabra(palabra):
    if palabra == palabra[:7]:
        return palabra

palabras_cortas = list(filter(cortar_palabra,lista))
print(palabras_cortas)