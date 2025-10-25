lista_diccionario=[
    {'Titulo':'LODR','anio':2001,'puntuacion':(10,9)},
    {'Titulo':'tiburon','anio':1978,'puntuacion':(90,120)},
    {'Titulo':'Alien','anio':1977,'puntuacion':(6,10)}
]
def mayor_puntaje(peli):
    for dic in peli:
        if 'puntuacion' in dic:
             puntuacion_clave = dic['puntuacion']
             if puntuacion_clave[0]>7:
                 print(dic)
mayor_puntaje(lista_diccionario)
 