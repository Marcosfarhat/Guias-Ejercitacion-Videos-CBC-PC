lista_diccionario=['Titulo','LODR','anio',2001,'puntuacion',10]

def mayor_puntaje(peli):
     for dic in peli:
        try:
            dic1=int(dic)
            if dic1>7:
                print('aca ta',dic1)
        except:
            continue


mayor_puntaje(lista_diccionario)
