def fun(t):
    vocales='AEIOUÁÉÍÓÚÜ'
    repes=False
    repetidas=''
    for letra in t:
        if letra in vocales and t.count(letra)>0:
            print(t.count(letra))
            repes=True
            repetidas+=letra
    return repes
txt='astaba La rana cantando dEbajo dEl agUA'
print(fun(txt))