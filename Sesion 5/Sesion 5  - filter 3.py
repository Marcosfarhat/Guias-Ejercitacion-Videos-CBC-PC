def es_par(numero):
    if numero %2 ==0:
        return True
    else:
        return False

lista = (1,2,3,4,4,5,56,6,6,765,33,53,424,6,5,)
lista_filtrada = list(filter(es_par,lista))
print(lista_filtrada)