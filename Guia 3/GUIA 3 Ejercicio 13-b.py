def fichas():
    fichas_a_ingresar = int(input("Decime el precio de F para comenzar el juego "))
    # f_a_ingresar = int(input(f"Ingresa {fichas_a_ingresar} fichas para comenzar"))
    f_a_ingresar = 0
    while f_a_ingresar < fichas_a_ingresar:
        f_a_ingresar_letra = str(input(f"Ingresa {fichas_a_ingresar} fichas para comenzar "))
        if f_a_ingresar_letra.upper() == "F":
            f_a_ingresar += 1
            print(f"Faltan ingresar {fichas_a_ingresar - f_a_ingresar} fichas")
    print("A jugar")

fichas()