string_palabras = 'juan mesa pileta aut cebra semanforo planta'
vocales = 'aeiou'
def contar(palabra):
    # trae al string como lista de palabras
    print(palabra)
    # para cada elemento de la LISTA palabra
    for palabras_sola in palabra:
        print('palabra sola',palabras_sola)
        #  itera cada letra de palabra_sola
        for caracter in palabras_sola:
            print(caracter)
            if caracter  in vocales:
                 print(f"esta la  vocal '{caracter}' ")
                 print("este es la vocal de la otra format {}".format(caracter))

string_palabras_cortadas = string_palabras.split()
print(contar(string_palabras_cortadas))