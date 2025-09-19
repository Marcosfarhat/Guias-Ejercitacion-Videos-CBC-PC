'''def empieza_con_m(palabra):
    for i in palabra:
        if palabra[0] != 'm':
            return palabra
            # print(palabra)

lista = ['manzana','pera','zapallo','albondiga']
lista_filtrada = filter(empieza_con_m,lista)
print(list(lista_filtrada))
'''
def empieza_con_m(palabra):
    return palabra !='m'
def ordenar(palabra):
    cant = 0
    for i in ('a','e'):
        cant += palabra.count(i)
        return cant
lista = ['casa','auto','ropero','similitud','alcornoque','casaca']
lista_m = list(filter(empieza_con_m,lista))
lista_m.sort(reverse=True,key=ordenar)
print(list(lista_m))