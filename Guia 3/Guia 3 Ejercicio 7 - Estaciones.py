def estaciones ():
    estacion = input("Ingrese la estacion del anio V-Verano O-Otonio I-Invierno P-Primavera")
    if estacion == "V":
        print("Verano")
    elif estacion== "O":
        print("Otonio")
    elif estacion == "I":
        print("Invierno")
    elif estacion == "P":
        print("Primavera")
    else:
        print("Error")
estaciones()