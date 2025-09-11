stringes = 'como come la lechuza sobre el trigal'

def oracion(palabras):
    vocales= "aeiou"
    for letras in palabras:
        if letras in vocales:
            print(letras)

oracion(stringes)