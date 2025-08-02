def absoluto():
    valor= int(input("ingrese un valor "))
    if valor <= 0:
        valor = valor * -1
        print(valor)
    else:
        print(valor)
absoluto()