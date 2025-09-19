def cuadrado(numero):
    return numero*numero
tupla = (1,2,3,4,4,5,5,)
cuadrados = map(cuadrado,tupla)
cuadrados_1 = list(map(cuadrado,tupla))
print(list(cuadrados))
print(cuadrados_1)