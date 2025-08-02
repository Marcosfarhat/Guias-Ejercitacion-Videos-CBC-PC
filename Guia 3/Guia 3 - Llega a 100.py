def limito ():
    limite = int(input("Ingresa el valor sobre el cual vamos a calcular cuanto falta para llegar, sumando a los dos numeros que te vamos a pedir"))
    sumando_1 =int(input("Ingresa el primer sumando "))
    sumando_2 = int(input("Ingresa el segundo sumando "))

    if limite < sumando_2+sumando_1:
        print("Llega a ",limite)
    elif limite > sumando_1+sumando_2:
        falta = limite - sumando_2 - sumando_1
        print("Te falta ", falta ," para llegar a ",limite)

limito()

