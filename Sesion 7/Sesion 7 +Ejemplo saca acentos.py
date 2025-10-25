def sacaAcen (t):
    con='áéíóú'
    sin='aeiou'
    traductor= str.maketrans(con,sin)
    print(traductor)
    return t.translate(traductor)

txt=input("Ingresa un texto")
txt=sacaAcen(txt.lower())
print("texto sin acentos")
print(txt.capitalize())
