lista = ['juan',' antonella','zurich']
def palabra_corta(palabra):
    longitud = len(palabra)
    if (longitud>5):
        return True
    else:
        return False
palabras_4= list(filter(palabra_corta,lista))
print(palabras_4)