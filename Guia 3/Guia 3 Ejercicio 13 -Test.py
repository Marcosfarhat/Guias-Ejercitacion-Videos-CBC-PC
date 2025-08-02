def fichas():
    fichas_a_ingresar = int(input("Decime el precio de F para comenzar el juego: "))
    f_a_ingresar = 0

    while f_a_ingresar < fichas_a_ingresar:
        print(f"Añadidas: {f_a_ingresar} fichas")
        f_a_ingresar_letra = input(
            f"Ingresa 'F' para agregar una ficha (te faltan {fichas_a_ingresar - f_a_ingresar} fichas): ")

        if f_a_ingresar_letra.upper() == "F":  # Convertir a mayúsculas para aceptar 'f' o 'F'
            f_a_ingresar += 1
            faltan = fichas_a_ingresar - f_a_ingresar
            print(f"Faltan ingresar {faltan} fichas")

    print("A jugar")
fichas()