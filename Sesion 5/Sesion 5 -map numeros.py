lista = [1,3,54,6,7,87,7,732]
tupla  = (1,3,54,6,7,87,7,732)

def multiplico(numero):
     numero_2 = numero*2
     return numero * 2


# print(list(map(multiplico,lista)))
numero_por_2 = list(map(multiplico,tupla))
print('esto es numero 2', numero_por_2)