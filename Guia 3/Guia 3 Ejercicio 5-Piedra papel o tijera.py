def juego ():
    tirada = input("¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)")
    if tirada == "R":
        print("Papel")
    elif tirada == "P":
        print("Tijera")
    elif tirada == "T":
        print("Piedra")
    else:
        print("error")
juego()