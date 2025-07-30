def masgrande():
    entero_1 = int(input("Ingrese un numero para comparar si es mas grande que el que vas a poner despues"))
    entero_2 = int(input("Ingrese un segunedo para comparar si es mas grande que el que escribiste"))
    if entero_1>entero_2:
        print(entero_1, " es mas grande ")
    elif entero_2>entero_1:
        print(entero_2, " es mas grande")
    else:
        print("Son iguales")
masgrande()