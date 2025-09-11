# creo las tuplas
argentina= ('argentina',' buenos aires','america')
francia = ('francia','paris','europa')
alemania= ('alemania','berlin','europa')
japon =  ('japon','tokio','asia')
peru = ('peru','lima','america')
# Creo la lista
lista_paises_con_tuplas_como_elementos = []
# Creo la funcion
def agregar_tuplas(a):
    lista_paises_con_tuplas_como_elementos.append(a)
    # print(lista_paises_con_tuplas_como_elementos)
#llamo a la funcion y al argumento ( las tuplas)
agregar_tuplas(argentina)
agregar_tuplas(francia)
agregar_tuplas(japon)
agregar_tuplas(peru)
print(lista_paises_con_tuplas_como_elementos)
# funcion para trabajar con los elementos de cada tupla en la lista
def trabajar_elementos_en_la_tupla_de_la_lista(b):
    for i in b:
        print('----------','\nPais:',i[0],'\nCapital:', i[1],'\nContinente', i[2])

trabajar_elementos_en_la_tupla_de_la_lista(lista_paises_con_tuplas_como_elementos)
