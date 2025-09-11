lista = [('damasco',433),('frutilla',522),('aguacate-melon', 32)]

def ordenados(fruta):
    return fruta[0]

lista.sort(key=ordenados, reverse=True)
print(lista)