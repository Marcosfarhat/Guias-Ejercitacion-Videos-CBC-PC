# ordenar lista por orden descendende por cantidad de vocales
#  funcion
# paso 1 hacerlas minusculas
def ordenar(palabra):
    palabra = palabra.lower()
    print('palabra en entrada antes del for ', palabra)
    for i in range(len(palabra)):
        palabra[i]=palabra[i].lower()


    return palabra


lista = ['Juan','ana','Reuteman','clarita','zapatoad','iluminacion']
palabras_en_minuscula = ordenar(lista)
print(palabras_en_minuscula)