# otra funcion, busca vocales

string_palabras = 'juan mesa pileta aut cebra semanforo planta'
vocales = 'aeiou'
contador_total = 0
def contar(palabras_1):
    global contador_total
    # print(palabras_1)
    contador = 0
    for letra in palabras_1:
        if letra in vocales:
            contador += 1
            contador_total +=1
            print('vocales',palabras_1)
            print(contador_total)
    return palabras_1

print(len(list(map(contar,string_palabras))))
# print(list(vocales_contadas))
# print('vocales',vocales_contadas)'''