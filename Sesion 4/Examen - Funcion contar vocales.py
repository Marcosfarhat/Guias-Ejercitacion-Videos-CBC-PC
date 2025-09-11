'''def mismaVocal(pal):
    cant=0
    for letra in 'aeiou':
        if pal.count(letra)>0:
            cant+=1
        return cant==1

frutas =['pera','naranja']
mismaVocal()'''


def mismaVocal(pal):
    cant=0
    print(cant)
    for letra in 'aeiou':
      if pal.count(letra)>0:
        cant+=1
        print(cant)
    return cant==1

frutas=['aeu','naranja']
i=0
while i<len(frutas):
    if mismaVocal(frutas[i]):
         frutas.pop(i)
    else:
        i+=1
print(frutas)
