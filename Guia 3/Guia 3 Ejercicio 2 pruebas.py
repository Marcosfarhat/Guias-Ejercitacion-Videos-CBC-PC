# Solicitar la palabra
palabra = input("Ingresa una palabra y reemplazo las letras por espacios: ")

# Letras vocales
vocales = "aeiou"

# Crear una nueva cadena reemplazando las vocales por espacios
nueva_palabra = ""

for letra in palabra:
    print(letra)
    if letra.lower() in vocales:
        nueva_palabra += " "
    else:
        nueva_palabra += letra

print(nueva_palabra)